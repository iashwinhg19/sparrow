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
- Where no free image exists (reduction en masse, the three indirect-hernia types, the myopectineal orifice, TEP vs TAPP planes, the laparoscopic danger triangles, mesogastrium, rotation anomalies, omphalocele) the note has a collapsed **🎨 Image prompt** callout you can paste into an image generator.
- Videos are YouTube / Osmosis / JOMI / Behind-the-Knife links found by search; the first one in each section is also embedded (`![](youtube url)`, which Obsidian renders as a player). Content and quality were judged from titles and descriptions only.
- Every note ends with a **🖼 Infographic prompt** — a single, long prompt describing one A4 page with every section of the note as a panel.

## What goes where in each main note

Frontmatter → core definition → mental model → the page's sections in the original order (tables kept as tables, lists as lists) → **Core Dictum & Pattern Recognition** (five callouts exactly in the format of your *Medical Notes Enhancement Prompt*) → pearls → one-line recall → Anki flash points → video library → infographic prompt → references → footnotes. Footnotes (`[^n]`) hold anything that is *not* on your page: cut-off values, eponym history, a textbook fact that completes a line, or a note on an unreadable word.

## For the next batch

Send each page as a **file upload** (PNG/JPG at full resolution, one file per page) rather than pasted into the chat — pasted images arrive at ~200–350 px wide. At full size every line can be transcribed exactly, with no reconstruction. If you want the pearl IDs from your PYQ list (`pearls/pearls.csv` in this repo) cross-referenced into the notes' `past_exam_questions` field, say so and I'll add them.
