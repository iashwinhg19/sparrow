#!/usr/bin/env python3
"""notes_digitize.py — helper for turning images or PDFs of handwritten medical notes into Obsidian notes.

  pages    FILE.pdf [...] --out DIR [--dpi 200]
             rasterise every PDF page to a PNG (needs PyMuPDF `pip install pymupdf`, or the `pdftoppm` CLI)
  slice    PAGE [PAGE ...] --out DIR [--zoom N] [--strip PX]
             cut each page image into overlapping, zoomed strips you can read one by one
  detect   PAGE [PAGE ...] --out DIR
             find the pictures on a page (photos, coloured diagrams) and write boxes.json + <page>_boxes.png
             with numbered red boxes so you can decide which to crop
  crop     --spec CROPS.json --out ATTACH_DIR
             cut figures out of the pages into the vault's attachments folder; prints the ![[...]] embeds
  wmurl    "File title.jpg" [...] [--width 800]
             print the direct upload.wikimedia.org URL for a Wikimedia Commons file title
             (the path is derived from the file name, so no network is needed)
  look     URL [URL ...] --out DIR
             download images so you can open and check what they show before embedding them
  check    NOTE.md [...] [--vault VAULT] [--net]
             validate a main note (frontmatter, required sections, footnotes incl. etymology, images, anatomed)
  mapcheck MAP.md [...]
             validate a mind-map note for the mdmap plugin
  skeleton NOTE.md --out MAP.md
             write a starting mind-map note from the headings of a main note

CROPS.json = [{"page": "inbox/hernia.png", "box": [x0, y0, x1, y1], "name": "Hernia - reduction en masse.png",
               "caption": "Reduction en masse — contents and constriction ring reduced together",
               "mask": [[x0, y0, x1, y1], ...]}]          # optional: page-pixel boxes painted white first
             (watermarks, e-mail addresses, site names, IDs)
             boxes are in the page image's own pixels; "upscale": 2 optional (default: x2 when narrower than 600 px)

Needs: pip install pillow numpy   (pymupdf for PDFs)
"""
import argparse, hashlib, json, os, re, shutil, subprocess, sys, urllib.parse, urllib.request

REQUIRED_FM = ["title", "aliases", "status", "topic", "subtopic", "target_exams", "difficulty",
               "high_yield", "source", "mindmap"]
REQUIRED_SECTIONS = ["Core Dictum & Pattern Recognition", "Pearls", "One-Line Recall",
                     "Video Library", "Infographic Prompt", "References"]
FORBIDDEN_SECTIONS = ["Anki Flash Points", "Word Parts"]
CORE_DICTUM_CALLOUTS = ["[!check]+", "[!example]+", "[!warning]+", "[!danger]+", "[!tip]+"]
WATERMARKS = ("ksusanta", "660eacb2787e5e31381ec737", "medicalstudyzone")
ALLOWED_IMG_HOSTS = ("upload.wikimedia.org",)
MIN_ETYMOLOGY = 12
MIN_AFFIX = 10
UA = {"User-Agent": "notes-digitizer/1.1 (Obsidian study notes)"}


# ---------------------------------------------------------------- pages
def cmd_pages(a):
    os.makedirs(a.out, exist_ok=True)
    for pdf in a.pdfs:
        stem = os.path.splitext(os.path.basename(pdf))[0]
        if shutil.which("pdfimages") and a.native:
            out_dir = os.path.join(a.out, stem)
            os.makedirs(out_dir, exist_ok=True)
            subprocess.run(["pdfimages", "-j", pdf, os.path.join(out_dir, "p")], check=True)
            for f in sorted(os.listdir(out_dir)):
                print(os.path.join(out_dir, f))
            continue
        try:
            import fitz                                            # PyMuPDF
            doc = fitz.open(pdf)
            for i, page in enumerate(doc, 1):
                pix = page.get_pixmap(dpi=a.dpi)
                out = os.path.join(a.out, f"{stem}_p{i:02d}.png")
                pix.save(out)
                print(f"{out}: {pix.width}x{pix.height}")
            continue
        except ImportError:
            pass
        if shutil.which("pdftoppm"):
            prefix = os.path.join(a.out, f"{stem}_p")
            subprocess.run(["pdftoppm", "-r", str(a.dpi), "-png", pdf, prefix], check=True)
            for f in sorted(os.listdir(a.out)):
                if f.startswith(f"{stem}_p"):
                    print(os.path.join(a.out, f))
        else:
            sys.exit("no PDF renderer: pip install pymupdf  (or install poppler for pdftoppm)")


# ---------------------------------------------------------------- slice
def cmd_slice(a):
    from PIL import Image
    os.makedirs(a.out, exist_ok=True)
    for page in a.pages:
        im = Image.open(page).convert("RGB")
        w, h = im.size
        stem = os.path.splitext(os.path.basename(page))[0]
        if w < 1000:
            print(f"WARNING {page}: only {w}px wide — handwriting will not be readable and crops will be blurry. "
                  "Ask for the original full-resolution file (one PNG/JPG/PDF per page, uploaded as a file).")
        zoom = a.zoom or (3 if w < 1200 else 2 if w < 2400 else 1)
        step, overlap, n = a.strip, 60, 0
        for y in range(0, h, step - overlap):
            c = im.crop((0, y, w, min(h, y + step)))
            if zoom > 1:
                c = c.resize((c.width * zoom, c.height * zoom), Image.LANCZOS)
            c.save(os.path.join(a.out, f"{stem}_{n:02d}_y{y}.png"))
            n += 1
            if y + step >= h:
                break
        print(f"{page}: {w}x{h}, {n} strips (zoom x{zoom}) -> {a.out}   (strip file names carry the y offset)")


# ---------------------------------------------------------------- detect
def find_pictures(im, min_frac=0.025):
    """Pictures on a notes page = blocks that are colour-saturated or photo-dark, unlike ink on paper.
    Returns boxes [x0, y0, x1, y1] in page pixels."""
    import numpy as np
    hsv = np.asarray(im.convert("HSV")).astype(int)
    rgb = np.asarray(im.convert("RGB")).astype(int)
    h, w = hsv.shape[:2]
    sat, val = hsv[..., 1], hsv[..., 2]
    spread = rgb.max(axis=2) - rgb.min(axis=2)
    pic = ((sat > 60) & (val > 40) & (spread > 40)) | (val < 70)       # colour or photo-dark
    # blur the mask by block pooling so handwriting (thin, sparse) drops out and pictures (dense) stay
    b = max(4, w // 160)
    H, W = h // b, w // b
    grid = pic[:H * b, :W * b].reshape(H, b, W, b).mean(axis=(1, 3)) > 0.18
    seen = np.zeros_like(grid, bool)
    boxes = []
    for gy in range(H):
        for gx in range(W):
            if not grid[gy, gx] or seen[gy, gx]:
                continue
            stack, ys, xs = [(gy, gx)], [], []
            seen[gy, gx] = True
            while stack:
                y, x = stack.pop(); ys.append(y); xs.append(x)
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < H and 0 <= nx < W and grid[ny, nx] and not seen[ny, nx]:
                            seen[ny, nx] = True; stack.append((ny, nx))
            x0, x1, y0, y1 = min(xs) * b, (max(xs) + 1) * b, min(ys) * b, (max(ys) + 1) * b
            if (x1 - x0) * (y1 - y0) >= min_frac * w * w:
                pad = b
                boxes.append([max(0, x0 - pad), max(0, y0 - pad), min(w, x1 + pad), min(h, y1 + pad)])
    boxes.sort(key=lambda bx: (bx[1], bx[0]))
    return boxes


def cmd_detect(a):
    from PIL import Image, ImageDraw
    os.makedirs(a.out, exist_ok=True)
    report = []
    for page in a.pages:
        im = Image.open(page).convert("RGB")
        boxes = find_pictures(im)
        sheet = im.copy()
        d = ImageDraw.Draw(sheet)
        for i, bx in enumerate(boxes, 1):
            d.rectangle(bx, outline=(255, 0, 0), width=max(2, im.width // 400))
            d.rectangle([bx[0], bx[1], bx[0] + 28, bx[1] + 18], fill=(255, 0, 0))
            d.text((bx[0] + 5, bx[1] + 3), str(i), fill=(255, 255, 255))
        stem = os.path.splitext(os.path.basename(page))[0]
        sheet.save(os.path.join(a.out, f"{stem}_boxes.png"))
        report.append({"page": page, "size": list(im.size), "boxes": [{"n": i, "box": bx} for i, bx in enumerate(boxes, 1)]})
        print(f"{page}: {im.width}x{im.height}, {len(boxes)} picture box(es) -> {stem}_boxes.png")
        for i, bx in enumerate(boxes, 1):
            print(f"  #{i}: {bx}")
    with open(os.path.join(a.out, "boxes.json"), "w") as f:
        json.dump(report, f, indent=1)
    print("Open the _boxes.png overlay, keep/merge/adjust the boxes, then write crops.json for `crop`.")


# ---------------------------------------------------------------- crop
def cmd_crop(a):
    from PIL import Image
    os.makedirs(a.out, exist_ok=True)
    embeds = []
    for item in json.load(open(a.spec)):
        im = Image.open(item["page"]).convert("RGB")
        x0, y0, x1, y1 = item["box"]
        if item.get("mask"):                                   # blank out watermarks / third-party text
            from PIL import ImageDraw
            dr = ImageDraw.Draw(im)
            for m in item["mask"]:
                dr.rectangle(m, fill=tuple(item.get("mask_fill", (255, 255, 255))))
        c = im.crop((x0, y0, x1, y1))
        up = item.get("upscale") or (2 if c.width < 600 else 1)
        if up > 1:
            c = c.resize((c.width * up, c.height * up), Image.LANCZOS)
        name = item["name"]
        path = os.path.join(a.out, name)
        if os.path.exists(path) and not item.get("overwrite"):
            print(f"kept existing {name} (set \"overwrite\": true to replace)")
        else:
            c.save(path, optimize=True) if name.lower().endswith(".png") else c.save(path, quality=92)
            print(f"saved {name} {c.size[0]}x{c.size[1]}")
        cap = item.get("caption", "")
        embeds.append(f"![[{name}]]\n*{cap} (cropped from the handwritten page).*" if cap else f"![[{name}]]")
    print("\n--- paste where the figure sits on the page ---")
    print("\n\n".join(embeds))


# ---------------------------------------------------------------- wmurl
def wm_direct(title, width=None):
    name = title.strip().replace(" ", "_")
    if name.lower().startswith("file:"):
        name = name[5:]
    h = hashlib.md5(name.encode("utf-8")).hexdigest()
    enc = urllib.parse.quote(name, safe="()',-._~!$&*+;=:@")
    if width:
        ext = name.rsplit(".", 1)[-1].lower()
        suffix = ".png" if ext in ("svg", "gif", "tif", "tiff", "pdf", "webp") else ""
        return f"https://upload.wikimedia.org/wikipedia/commons/thumb/{h[0]}/{h[:2]}/{enc}/{width}px-{enc}{suffix}"
    return f"https://upload.wikimedia.org/wikipedia/commons/{h[0]}/{h[:2]}/{enc}"


def cmd_wmurl(a):
    for t in a.titles:
        print(t)
        print("  ", wm_direct(t))
        if a.width:
            print("  ", wm_direct(t, a.width))


# ---------------------------------------------------------------- look
def cmd_look(a):
    os.makedirs(a.out, exist_ok=True)
    for u in a.urls:
        name = urllib.parse.unquote(u.rsplit("/", 1)[-1])
        path = os.path.join(a.out, name)
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60) as r, open(path, "wb") as f:
                f.write(r.read())
            print(f"saved {path}")
        except Exception as e:
            print(f"FAILED {u}: {e}")


# ---------------------------------------------------------------- check
def frontmatter(s):
    m = re.match(r"^---\n(.*?)\n---\n", s, re.S)
    if not m:
        return None, s
    keys = re.findall(r"^([A-Za-z_][\w-]*):", m.group(1), re.M)
    return keys, s[m.end():]


def strip_fences(s):
    """Blank out fenced code blocks so '#' comments inside them are not read as headings."""
    return re.sub(r"^```.*?^```", lambda m: "\n" * m.group(0).count("\n"), s, flags=re.S | re.M)


def head_ok(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, method="HEAD", headers=UA), timeout=20) as r:
            return r.status == 200
    except Exception:
        return None


def problems(path, s, vault=None):
    p = []
    keys, body = frontmatter(s)
    if keys is None:
        p.append("no YAML frontmatter")
        keys = []
    elif re.search(r"\[\^[\w-]+\]", s[:len(s) - len(body)]):
        p.append("footnote marker inside the frontmatter — markers belong in the body only")
    for k in REQUIRED_FM:
        if k not in keys:
            p.append(f"frontmatter missing '{k}'")
    h1 = re.findall(r"^# .+", strip_fences(body), re.M)
    if len(h1) != 1:
        p.append(f"expected exactly one '# Title' heading, found {len(h1)}")
    for sec in REQUIRED_SECTIONS:
        if not re.search(r"^## .*" + re.escape(sec), body, re.M):
            p.append(f"missing section '## … {sec}'")
    for c in CORE_DICTUM_CALLOUTS:
        if c not in body:
            p.append(f"Core Dictum block missing callout {c}")
    refs = set(re.findall(r"\[\^([\w-]+)\]", re.sub(r"^\[\^[\w-]+\]:", "", body, flags=re.M)))
    defs = set(re.findall(r"^\[\^([\w-]+)\]:", body, re.M))
    for r in sorted(refs - defs):
        p.append(f"footnote [^{r}] used but never defined")
    for d in sorted(defs - refs):
        p.append(f"footnote [^{d}] defined but never used")
    if not refs:
        p.append("no footnotes — add [^n] for every fact that is not on the page")
    ety = {r for r in refs if r.startswith("ety-")}
    if len(ety) < MIN_ETYMOLOGY:
        p.append(f"only {len(ety)} etymology footnote(s) [^ety-…] — every eponym and Greek/Latin term gets one (≥ {MIN_ETYMOLOGY})")
    affix = {r for r in refs if r.startswith(("pre-", "suf-"))}
    if len(affix) < MIN_AFFIX:
        p.append(f"only {len(affix)} prefix/suffix footnote(s) [^pre-…]/[^suf-…] — every affix in the note gets one on its first word (≥ {MIN_AFFIX})")
    for d in defs:
        if d.startswith(("ety-", "pre-", "suf-")):
            m = re.search(r"^\[\^" + re.escape(d) + r"\]:\s*(.*)$", body, re.M)
            txt = m.group(1).lstrip() if m else ""
            if not re.match(r"\*\*[^*]+\*\* — ", txt):
                p.append(f"[^{d}] must read '**word** — explanation' (bold word, em dash, then the explanation; no 'Etymology' label)")
    for sec in FORBIDDEN_SECTIONS:
        if re.search(r"^## .*" + re.escape(sec), body, re.M):
            p.append(f"section '{sec}' is not part of the format any more — remove it (affixes go in footnotes; cards come from the PYQ skill)")
    for blk in re.findall(r"^```.*?^```", body, flags=re.S | re.M):
        for mk in re.findall(r"\[\^[\w-]+\]", blk):
            p.append(f"footnote marker {mk} inside a code block — it will not render; move it to a prose line")
    for wm in WATERMARKS:
        if wm.lower() in s.lower():
            p.append(f"watermark / third-party text '{wm}' copied into the note — remove it")
    if vault and getattr(problems, "check_links", False):
        names = {os.path.splitext(f)[0] for _, _, fs in os.walk(vault) for f in fs if f.endswith(".md")}
        for t in re.findall(r"(?<!!)\[\[([^\]|#]+)", body):
            if t.strip() not in names:
                p.append(f"wikilink [[{t}]] does not match any note in the vault")
    for m in re.finditer(r"!\[[^\]]*\[\^[\w-]+\][^\]]*\]\(", body):
        p.append("footnote marker inside an image's alt text — move it to the caption line")
    imgs = re.findall(r"!\[[^\]]*\]\((https?://[^)\s]+)\)", body)
    local = re.findall(r"!\[\[([^\]|]+)", body)
    for u in imgs:
        host = urllib.parse.urlparse(u).netloc
        if any(v in host for v in ("youtube.com", "youtu.be")):
            continue
        if not host.endswith(ALLOWED_IMG_HOSTS):
            p.append(f"image not from an allowed free host: {u}")
    for u in re.findall(r"!\[[^\]]*\]\(([^)\s]+)\)", body) + local:
        if u.lower().endswith(".svg") and not u.startswith("http"):
            p.append(f"local SVG embedded — the user does not want generated SVG figures: {u}")
    if vault:
        for name in local:
            att = os.path.join(vault, "attachments", os.path.basename(name))
            if not os.path.isfile(att) and not any(os.path.isfile(os.path.join(r, os.path.basename(name)))
                                                   for r, _, _ in os.walk(vault)):
                p.append(f"embedded file not found in the vault: {name}")
    if "```anatomed" in body:
        block = re.search(r"```anatomed\n(.*?)```", body, re.S).group(1)
        for line in block.split("\n"):
            t = line.strip()
            if not t or t.startswith(("#", "//")):
                continue
            key = t.split(":", 1)[0].lower() if ":" in t else ""
            if key not in ("region", "regions", "part", "parts", "detail", "title"):
                p.append(f"anatomed block: line '{t[:40]}' will be read as a structure name (no bullets / bold / prose inside the block)")
            if key == "detail" and t.split(":", 1)[1].strip() not in ("isolated", "related", "regional"):
                p.append("anatomed block: detail must be isolated | related | regional (case-sensitive)")
    if "🎬" not in body and "youtube.com" not in body:
        p.append("no videos linked")
    prompts = len(re.findall(r"\[!example\]-.*🎨", body))
    if len(imgs) + len(local) + prompts < 3:
        p.append("fewer than 3 figures (web image / page crop / prompt) — every figure on the page needs one")
    cap_missing = len(re.findall(r"!\[[^\]]*\]\(https://upload\.wikimedia\.org[^)]+\)\n(?!\*)", body))
    cap_missing += len(re.findall(r"!\[\[[^\]]+\]\]\n(?!\*)", body))
    if cap_missing:
        p.append(f"{cap_missing} image(s) without an italic caption line directly below")
    return p, imgs


def cmd_check(a):
    bad = 0
    for path in a.notes:
        s = open(path, encoding="utf-8").read()
        problems.check_links = a.links
        p, imgs = problems(path, s, a.vault)
        if a.net:
            for u in imgs:
                if "youtube" in u:
                    continue
                ok = head_ok(u)
                if ok is False:
                    p.append(f"image URL returns an error (wrong file name?): {u}")
                elif ok is None:
                    p.append(f"image URL could not be reached from here (check it once in Obsidian): {u}")
        print(("OK   " if not p else "FIX  ") + path)
        for x in p:
            print("     - " + x)
        bad += bool(p)
    sys.exit(1 if bad else 0)


# ---------------------------------------------------------------- mapcheck
def map_problems(s):
    p = []
    _, body = frontmatter(s)
    lines = body.split("\n")
    h1 = [l for l in lines if re.match(r"^# ", l)]
    if len(h1) != 1:
        p.append(f"mind map needs exactly one '# Root' heading (found {len(h1)}); several make mdmap add a root named after the file")
    prev = 0
    for i, l in enumerate(lines, 1):
        m = re.match(r"^(#{1,6}) ", l)
        if m:
            lvl = len(m.group(1))
            if lvl > prev + 1:
                p.append(f"line {i}: heading jumps from level {prev} to {lvl} — keep levels consecutive")
            prev = lvl
            continue
        if l.startswith("|"):
            p.append(f"line {i}: table — becomes body text, not nodes; turn rows into bullets")
        if l.startswith(">"):
            p.append(f"line {i}: callout/quote — becomes body text, not a node; turn it into bullets")
        if l.startswith("```"):
            p.append(f"line {i}: code fence — becomes body text; remove from the mind map")
        if l.strip() and not re.match(r"^\s*([-*+]|\d+[.)])\s", l) and not re.match(r"^#{1,6} ", l):
            if i > 1 and prev > 0:
                p.append(f"line {i}: paragraph '{l.strip()[:40]}' becomes a node titled by its first line — use a bullet instead")
        bm = re.match(r"^(\s*)[-*+] ", l)
        if bm and len(bm.group(1)) % 2:
            p.append(f"line {i}: bullet indented by an odd number of spaces — use multiples of 2")
        if bm and len(l) > 110:
            p.append(f"line {i}: bullet longer than 110 characters — split it; nodes should be one idea")
    return p


def cmd_mapcheck(a):
    bad = 0
    for path in a.maps:
        p = map_problems(open(path, encoding="utf-8").read())
        print(("OK   " if not p else "FIX  ") + path)
        for x in p:
            print("     - " + x)
        bad += bool(p)
    sys.exit(1 if bad else 0)


# ---------------------------------------------------------------- skeleton
SKIP = ("Core Dictum", "Pearls", "One-Line Recall", "Anki Flash Points", "Video Library",
        "Infographic Prompt", "References", "Mental Model")


def cmd_skeleton(a):
    s = open(a.note, encoding="utf-8").read()
    keys, body = frontmatter(s)
    title = re.search(r"^title:\s*(.+)$", s, re.M)
    title = title.group(1).strip().strip('"') if title else os.path.splitext(os.path.basename(a.note))[0]
    out = ["---", f"title: {title} — Mind Map", "type: mindmap",
           f'source_note: "[[{os.path.splitext(os.path.basename(a.note))[0]}]]"', "plugin: mdmap",
           "status: not-started", "---", "", f"# {re.sub(r'^[^A-Za-z]+', '', title)}", ""]
    for m in re.finditer(r"^(#{2,3}) (.+)$", strip_fences(body), re.M):
        lvl, text = len(m.group(1)), m.group(2)
        text = re.sub(r"^[^\w(]+", "", text).strip()             # drop leading emoji
        if any(k in text for k in SKIP):
            continue
        out.append(f"{'#' * lvl} {text}")
        out.append("- ")
        out.append("")
    open(a.out, "w", encoding="utf-8").write("\n".join(out).rstrip() + "\n")
    print(f"wrote {a.out} — now fill each '- ' with one-idea bullets (two-space nesting), no tables/callouts")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    pg = sub.add_parser("pages"); pg.add_argument("pdfs", nargs="+"); pg.add_argument("--out", required=True); pg.add_argument("--dpi", type=int, default=200)
    pg.add_argument("--native", action="store_true", help="extract the embedded page images as-is (best for scanned/photographed PDFs)")
    s = sub.add_parser("slice"); s.add_argument("pages", nargs="+"); s.add_argument("--out", required=True)
    s.add_argument("--zoom", type=int, default=0); s.add_argument("--strip", type=int, default=700)
    d = sub.add_parser("detect"); d.add_argument("pages", nargs="+"); d.add_argument("--out", required=True)
    c = sub.add_parser("crop"); c.add_argument("--spec", required=True); c.add_argument("--out", required=True)
    w = sub.add_parser("wmurl"); w.add_argument("titles", nargs="+"); w.add_argument("--width", type=int, default=0)
    l = sub.add_parser("look"); l.add_argument("urls", nargs="+"); l.add_argument("--out", required=True)
    k = sub.add_parser("check"); k.add_argument("notes", nargs="+"); k.add_argument("--vault", default="")
    k.add_argument("--net", action="store_true", help="also HEAD-request every image URL")
    k.add_argument("--links", action="store_true", help="also require every [[wikilink]] to match a note in --vault")
    m = sub.add_parser("mapcheck"); m.add_argument("maps", nargs="+")
    sk = sub.add_parser("skeleton"); sk.add_argument("note"); sk.add_argument("--out", required=True)
    a = ap.parse_args()
    {"pages": cmd_pages, "slice": cmd_slice, "detect": cmd_detect, "crop": cmd_crop, "wmurl": cmd_wmurl,
     "look": cmd_look, "check": cmd_check, "mapcheck": cmd_mapcheck, "skeleton": cmd_skeleton}[a.cmd](a)


if __name__ == "__main__":
    main()
