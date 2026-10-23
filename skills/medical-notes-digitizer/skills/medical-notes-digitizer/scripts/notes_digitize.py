#!/usr/bin/env python3
"""notes_digitize.py — helper for turning images of handwritten medical notes into Obsidian notes.

  slice    PAGE [PAGE ...] --out DIR [--zoom N] [--strip PX]
             cut each page image into overlapping, zoomed strips you can read one by one
  wmurl    "File title.jpg" [...] [--width 800]
             print the direct upload.wikimedia.org URL for a Wikimedia Commons file title
             (the path is derived from the file name, so no network is needed)
  look     URL [URL ...] --out DIR
             download images so you can open and check what they show before embedding them
  check    NOTE.md [...] [--vault VAULT]
             validate a main note (frontmatter, required sections, footnotes, image URLs, anatomed block)
  mapcheck MAP.md [...]
             validate a mind-map note for the mdmap plugin (one root, consecutive heading levels,
             no tables / callouts / paragraphs that would become body text)
  skeleton NOTE.md --out MAP.md
             write a starting mind-map note from the headings of a main note (you then fill the bullets)

Needs: pip install pillow   (only `slice` uses it)
"""
import argparse, hashlib, os, re, sys, urllib.parse, urllib.request

REQUIRED_FM = ["title", "aliases", "status", "topic", "subtopic", "target_exams", "difficulty",
               "high_yield", "source", "mindmap"]
REQUIRED_SECTIONS = ["Core Dictum & Pattern Recognition", "Pearls", "One-Line Recall",
                     "Anki Flash Points", "Video Library", "Infographic Prompt", "References"]
CORE_DICTUM_CALLOUTS = ["[!check]+", "[!example]+", "[!warning]+", "[!danger]+", "[!tip]+"]
ALLOWED_IMG_HOSTS = ("upload.wikimedia.org",)
VIDEO_HOSTS = ("youtube.com", "youtu.be", "osmosis.org", "jomi.com", "behindtheknife.org",
               "ninjanerd.org", "upload.wikimedia.org")


# ---------------------------------------------------------------- slice
def cmd_slice(a):
    from PIL import Image
    os.makedirs(a.out, exist_ok=True)
    for page in a.pages:
        im = Image.open(page).convert("RGB")
        w, h = im.size
        stem = os.path.splitext(os.path.basename(page))[0]
        if w < 1000:
            print(f"WARNING {page}: only {w}px wide — handwriting will not be readable. "
                  "Ask for the original full-resolution file (one PNG/JPG per page, uploaded as a file).")
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
        print(f"{page}: {w}x{h}, {n} strips (zoom x{zoom}) -> {a.out}")


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
            req = urllib.request.Request(u, headers={"User-Agent": "notes-digitizer/1.0 (Obsidian study notes)"})
            with urllib.request.urlopen(req, timeout=60) as r, open(path, "wb") as f:
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


def head_ok(url):
    try:
        req = urllib.request.Request(url, method="HEAD",
                                     headers={"User-Agent": "notes-digitizer/1.0 (Obsidian study notes)"})
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status == 200
    except Exception:
        return None


def strip_fences(s):
    """Blank out fenced code blocks so '#' comments inside them are not read as headings."""
    return re.sub(r"^```.*?^```", lambda m: "\n" * m.group(0).count("\n"), s, flags=re.S | re.M)


def problems(path, s, vault=None):
    p = []
    keys, body = frontmatter(s)
    if keys is None:
        p.append("no YAML frontmatter")
        keys = []
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
    refs = set(re.findall(r"\[\^(\w+)\](?!:)", body))
    defs = set(re.findall(r"^\[\^(\w+)\]:", body, re.M))
    for r in sorted(refs - defs):
        p.append(f"footnote [^{r}] used but never defined")
    for d in sorted(defs - refs):
        p.append(f"footnote [^{d}] defined but never used")
    if not refs:
        p.append("no footnotes — add [^n] for every fact that is not on the page")
    imgs = re.findall(r"!\[[^\]]*\]\((https?://[^)\s]+)\)", body)
    for u in imgs:
        host = urllib.parse.urlparse(u).netloc
        if any(v in host for v in ("youtube.com", "youtu.be")):
            continue
        if not host.endswith(ALLOWED_IMG_HOSTS):
            p.append(f"image not from an allowed free host: {u}")
    for u in re.findall(r"!\[[^\]]*\]\(([^)\s]+)\)", body):
        if u.lower().endswith(".svg") and not u.startswith("http"):
            p.append(f"local SVG embedded — the user does not want generated SVG figures: {u}")
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
    if not re.search(r"\[!example\]-.*🎨", body) and len(imgs) < 3:
        p.append("fewer than 3 images and no image prompts — every figure on the page needs an image or a prompt")
    cap_missing = 0
    for m in re.finditer(r"!\[[^\]]*\]\(https://upload\.wikimedia\.org[^)]+\)\n(?!\*)", body):
        cap_missing += 1
    if cap_missing:
        p.append(f"{cap_missing} Wikimedia image(s) without an italic caption line directly below")
    if vault:
        rel = os.path.relpath(path, vault) if path.startswith(vault) else None
        if rel is None:
            p.append("note is outside the vault — write it into the vault (or obsidian-pending/)")
    return p, imgs


def cmd_check(a):
    bad = 0
    for path in a.notes:
        s = open(path, encoding="utf-8").read()
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
    for m in re.finditer(r"^(#{2,3}) (.+)$", body, re.M):
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
    s = sub.add_parser("slice"); s.add_argument("pages", nargs="+"); s.add_argument("--out", required=True)
    s.add_argument("--zoom", type=int, default=0); s.add_argument("--strip", type=int, default=700)
    w = sub.add_parser("wmurl"); w.add_argument("titles", nargs="+"); w.add_argument("--width", type=int, default=0)
    l = sub.add_parser("look"); l.add_argument("urls", nargs="+"); l.add_argument("--out", required=True)
    c = sub.add_parser("check"); c.add_argument("notes", nargs="+"); c.add_argument("--vault", default="")
    c.add_argument("--net", action="store_true", help="also HEAD-request every image URL")
    m = sub.add_parser("mapcheck"); m.add_argument("maps", nargs="+")
    k = sub.add_parser("skeleton"); k.add_argument("note"); k.add_argument("--out", required=True)
    a = ap.parse_args()
    {"slice": cmd_slice, "wmurl": cmd_wmurl, "look": cmd_look, "check": cmd_check,
     "mapcheck": cmd_mapcheck, "skeleton": cmd_skeleton}[a.cmd](a)


if __name__ == "__main__":
    main()
