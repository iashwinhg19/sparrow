# Obsidian notes digitised from handwritten pages

Four notes built from the two page images you shared, plus this guide.

| File | What it is | Source page |
|---|---|---|
| `Hernia and Hernia Surgeries.md` | Full digitised note — tables, web images, videos, footnotes, Core Dictum & Pattern Recognition, Anki flash points, infographic prompt | *Hernia, Thorax and Skin* (fully legible) |
| `Hernia — Mind Map.md` | Same topic restructured for the **mdmap** plugin | — |
| `Embryology — Germ Layers to Genital Ducts.md` | Full note in the same style — **reconstructed**: the scan was 192 px wide, so headings/tables were kept and body text filled from standard texts; lines marked **⚠ verify** need checking against your original | *Embryology* (headings only legible) |
| `Embryology — Mind Map.md` | Same topic restructured for **mdmap** | — |

Drop the four `.md` files into your vault. Nothing else is needed — every image and video is a public URL.

## The two plugins (what they actually are)

**anatomed-obsidian** (`pitfa19/anatomed-obsidian`) is **not a mind-map plugin**. It renders a fenced `anatomed` code block as a rotatable **3D anatomy model** (Z-Anatomy catalogue, ~3,500 structures, desktop only). Both main notes carry one block, for example:

````markdown
```anatomed
region: inguinal canal
parts: external oblique, internal oblique, transversus abdominis, inferior epigastric artery
detail: related
title: Inguinal region
```
````

- `region:` / `parts:` take comma-separated structure names (English or Latin). `detail:` is `isolated` (default), `related` or `regional`. `title:` is optional.
- Any other line inside the block is treated as a structure name — so no bullets, bold or wikilinks inside it. Lines starting with `#` are comments.
- A name the catalogue does not know shows as "unmatched" in the header; retype it with the plugin's autocomplete. I could not check the catalogue from here, so expect one or two of my names to need that.
- Editing in the widget rewrites the block (comments are lost).

**mdmap** (`pererinha/mdmap`) opens the *current note* as an editable mind map (command: **Edit current note as mind map**). It reads the note's own structure, so the shape of the note *is* the map:

- One `#` heading = the root. `##`, `###` … = child nodes by level; don't skip levels.
- `- bullet` items = nodes, nested by two-space indentation.
- A paragraph becomes a node titled by its first line. Tables, callouts, code blocks and images are **not** nodes — they attach as "body" to the node above.
- Nothing before the first heading becomes a node.

That is why the mind-map notes are separate files: a main note full of callouts and tables would collapse into a few bloated nodes. The mind-map notes have no callouts, no tables and no prose — only a heading tree and short bullets, each line one idea with `→` for "gives rise to / leads to". Open one, run the command, and use *Tidy tree* or *Radial* from the map's gear.

## How the images and videos were chosen

- Images are direct Wikimedia Commons URLs (public domain, CC BY or CC BY-SA; attribution is in each caption). Wikimedia and YouTube are blocked from the environment I worked in, so I confirmed each **file name** through search results and built the standard Commons URL from it — but I could not *view* the files. Glance at each image once; if any shows as broken, the file name is the fix.
- Where the web had no equivalent, the figure was **cropped out of your page** into `attachments/` and embedded with `![[Hernia - …png]]` (seven crops in the Hernia note: reduction en masse, the three indirect types, Hesselbach's triangle, Fruchaud's orifice, TEP vs TAPP, your laparoscopic sketch, the triangles photo). Copy the `attachments/` folder into your vault next to the notes. The page reached me at 346 px wide, so these crops are small; each has a collapsed **🎨 Image prompt** under it to regenerate the figure, and a full-resolution page will give clean crops. The Embryology page (192 px) was too small to crop, so its figures have prompts only.
- **Etymology footnotes — three layers, all as hover popovers:** (1) every eponym and Greek/Latin term; (2) every process word (reduction, strangulation, peristalsis, neurulation, migration, hypoplasia…), split into prefix + root + suffix and differentiated from its look-alikes (irreducible → obstructed → strangulated; hypoplasia / aplasia / agenesis / atrophy; cyst / sinus / fistula; -rrhage / -rrhoea / -rrhaphy); (3) every prefix and suffix, as a `[^pre-…]` / `[^suf-…]` footnote on the first word that carries it, with a "don't confuse with" list (para-/peri-/pre-, -tomy/-ectomy/-stomy, -plasia/-plasty/-trophy, pro-/meso-/meta-nephros…). Each footnote starts with the bold word and an em dash — no label. Hover the marker to read it; turn on the core plugin *Page preview* if the popover does not appear.
- **No Anki section** in the notes — your cards come from the PYQ skill.
- **Blurred crops were re-searched.** For each of the seven page crops I searched again for a clear free image: Hesselbach's triangle has one on Commons (that crop was dropped); reduction en masse has a clear open-access diagram on PMC (linked under the crop); Fruchaud's orifice, the TEP/TAPP planes, the three indirect types and the danger triangles exist only as copyrighted journal figures (linked as 📎 "clear diagram" references) — so those crops stay, each with its regeneration prompt.

## What goes where in each main note

Frontmatter → core definition → mental model → the page's sections in the original order (tables kept as tables, lists as lists) → **Core Dictum & Pattern Recognition** (five callouts exactly in the format of your *Medical Notes Enhancement Prompt*) → pearls → one-line recall → Anki flash points → video library → infographic prompt → references → footnotes. Footnotes (`[^n]`) hold anything that is *not* on your page: cut-off values, eponym history, a textbook fact that completes a line, or a note on an unreadable word.

## For the next batch

Send each page as a **file upload** (PNG/JPG at full resolution, one file per page) rather than pasted into the chat — pasted images arrive at ~200–350 px wide. At full size every line can be transcribed exactly, with no reconstruction. If you want the pearl IDs from your PYQ list (`pearls/pearls.csv` in this repo) cross-referenced into the notes' `past_exam_questions` field, say so and I'll add them.

---

# Physiology main notes (Marrow 8) — `Physiology/`

The whole Physiology course notes digitised: **61 chapters**, each a full note plus its own mind map, grouped in ten unit folders, with an index note.

| What | Where |
|---|---|
| Start here | `Physiology/Physiology — Index.md` — every chapter in Marrow order, with page ranges, mind-map links and cross-chapter "threads" |
| Main notes | `Physiology/<unit folder>/<Chapter>.md` |
| Mind maps (mdmap plugin) | `Physiology/<unit folder>/Mind Maps/<Chapter> — Mind Map.md` |
| Page crops | `Physiology/attachments/` — 435 figures cropped from your pages, shrunk to 256-colour PNGs; copy the folder next to the notes |

**Unit folders:** 01 General Physiology · 02 Nerve-Muscle Physiology · 03 Central Nervous System · 04 Respiratory System · 05 Cardiovascular System and Blood · 06 Gastrointestinal System · 07 Renal Physiology · 08 Endocrine System · 09 Reproductive System · 10 Exercise and Body Temperature.

**Chapters hidden inside PDFs.** Three of your PDFs held a second chapter, found by scanning every page for a title page: *Classification of Nerve Fibres* (inside the nerve-fibre PDF), *Mechanics of Breathing* (inside the lung-structure PDF) and *Learning and Memory* (inside the limbic PDF). Each has its own note, so 58 PDFs/titles became 61 chapters.

**What every chapter has** — same layout as the Hernia and Embryology notes: core definition → mental model → your page's sections in page order (tables kept as tables, flowcharts as ASCII) → Core Dictum & Pattern Recognition → pearls → one-line recall → video library → infographic prompt → references → footnotes. Footnotes pop up on hover: numbered ones carry facts not on your page and **⚠ places where the page and the textbook differ** (the page's wording is kept in the body); `ety-` ones are etymology for every term and process word; `pre-` / `suf-` ones are the prefixes and suffixes.

**Figures.** Each page figure is a crop of your page (clear at the native 1080 px), and 30 chapters also carry a Wikimedia / OpenStax diagram; where a page figure was blurred or hidden by a watermark there is a collapsed 🎨 image prompt under it. Third-party watermarks on your pages (an email address, an ID hash, a site name, the "Feedback" tab and the lecturer's thumbnail) are **not** in any note and are masked out of every crop.

**Videos.** 314 real YouTube videos, every note with one embedded player and 2–10 links. Video links were taken from search results only and matched by title — I could not watch them, so glance at a few. Where no matching video turned up for a topic the link is a YouTube **search** link (235 such lines across 55 notes); swap in a video whenever you find one.

**Things to check once in Obsidian**
- Wikimedia is blocked in the environment I worked in, so I could not look at the 93 web images; each file name comes from a search result. A broken image means the file name needs fixing.
- anatomed: each chapter has one 3D block; some structure names may show as "unmatched" and need the plugin's autocomplete.
- ⚠ lines: wherever your page and the textbook disagree (for example "creatinine phosphate", the left-shift row in the O₂–Hb table, "300 mmol/L mannitol = hypertonic") the footnote says so.
