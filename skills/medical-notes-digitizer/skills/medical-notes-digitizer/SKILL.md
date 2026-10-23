---
name: "medical-notes-digitizer"
description: "Turn images of handwritten medical notes into Obsidian notes in the user's house style: faithful transcription, Wikimedia images and videos where the page had figures, image prompts where no free image exists, footnotes, a Core Dictum & Pattern Recognition section, an infographic prompt, an anatomed 3D block, and a separate mdmap mind-map note. Use when asked to digitise, OCR, convert or make Obsidian notes from note images or scans."
---

# Handwritten note images → Obsidian notes + mind map

Turns photographed or scanned pages of the user's medical notes into **two Obsidian files per topic**:

1. **The main note** — the page transcribed faithfully in the user's house style (section D), with every figure on the page replaced by a **free web image** or an **image-generation prompt**, one or more **videos** per section, **footnotes** for anything not on the page, a **Core Dictum & Pattern Recognition** block, an **anatomed** 3D block, Anki flash points, and an **infographic prompt** at the end.
2. **The mind-map note** — the same topic rebuilt as a heading-and-bullet tree for the **mdmap** plugin (section K). It is a different file with a different shape, never a copy of the main note.

The page is the source of truth. You add structure, pictures, videos and footnotes; you do not change what the page says.

---

## A. One-time setup

1. **Folder:** the user's connected folder `Notes-Digitizer` (any name; ask if more than one could be it) with:
   - `inbox/` — page images arrive here
   - `work/<topic>/` — strips, transcript and drafts
   - `done/` — processed pages (moved, never deleted)
   - `obsidian-pending/` — notes that could not go straight into the vault
   - `_tools/` — the helper script
2. **Helper script:** copy `scripts/notes_digitize.py` (next to this file) to `_tools/notes_digitize.py`. `pip install pillow`. If installing is blocked, run the steps in your workspace and copy the finished notes back.
3. **Vault:** `devd` must be a connected folder. Ask the user **once** which folder the notes go in (for example `ATLAS/<Subject>/`) and keep using it. Until the vault is connected, every note goes to `obsidian-pending/`.
4. **Plugins the notes are written for** (both are optional on the user's side; the notes degrade gracefully without them):
   - **mdmap** (`pererinha/mdmap`) — opens the *current note* as an editable mind map ("Edit current note as mind map"). Headings and bullets are nodes; tables, callouts, code blocks and images are only *body text* of the node above. This is why the mind-map note is a separate, bare file.
   - **anatomed** (`pitfa19/anatomed-obsidian`) — renders a fenced ```anatomed block as a rotatable 3D model (Z-Anatomy catalogue). It is **not** a mind-map plugin. Section I has the syntax.

---

## B. Each run ("digitise my notes", "make Obsidian notes from these pages", images dropped in)

1. **Gather and group.** Each page image has a title at the top (e.g. `HERNIA, THORAX AND SKIN`, `EMBRYOLOGY`). One topic = one page title. A page usually holds several timestamped section headings (`Hernia and Hernia Surgeries 00:00:52`); keep them as `##` sections. Split a topic into two notes only when the transcript passes ~450 lines, and then at a major heading.
2. **Resolution gate.** `python3 _tools/notes_digitize.py slice inbox/<page> --out work/<topic>/strips`. If it prints a **WARNING (< 1000 px wide)**, stop and ask the user for the original file (one full-size PNG/JPG per page, uploaded as a *file*, not pasted into the chat — pasted images arrive at 200–350 px). Only if the user says to go ahead anyway: write the note with `transcription_status: reconstructed-from-low-res-scan`, a `[!warning]` banner at the top saying what was and was not legible, and **⚠ verify** after every line you filled from a textbook instead of the page.
3. **Read every strip in order** and write `work/<topic>/transcript.md` first — the raw, faithful transcript (section C). Do not start the note before the transcript is complete.
4. **Build the main note** from the template in section D, section by section in page order.
5. **Replace each figure** with an image or an image prompt (section E).
6. **Add videos** (section F).
7. **Add footnotes** (section G).
8. **Write the Core Dictum & Pattern Recognition block** (section H).
9. **Add the anatomed block** (section I) and the **infographic prompt** (section J).
10. **Write the mind-map note** (section K): `python3 _tools/notes_digitize.py skeleton work/<topic>/<Title>.md --out "work/<topic>/<Title> — Mind Map.md"`, then fill it.
11. **Check:** `check` on the main note and `mapcheck` on the map. Fix every line until both print `OK`. With network, add `--net` to `check` so every image URL is HEAD-requested.
12. **Write into the vault.** Never overwrite a note that already has content — if the target exists and is not empty, save the new version to `obsidian-pending/` and say so. If the vault is not connected, everything goes to `obsidian-pending/`.
13. **Move** the page images from `inbox/` to `done/<topic>/`.
14. **Report** (section M).

---

## C. Transcription rules

- **Faithful first.** Every heading, table, list, arrow and side note on the page goes into the transcript in page order. Tables stay tables (pipe tables, same rows and columns), lists stay lists, flow arrows stay arrows.
- **Keep the user's shorthand** exactly: `m/c`, `d/t`, `a/w`, `b/w`, `Sx`, `Rx`, `IOC`, `TOC`, `C/I`, `⊕/⊖`, `↑/↓`, `→`, `F ≫ M`. Do not expand them in the body; expand once in a footnote if a reader could misread one.
- **Colour means emphasis.** Text the user wrote in red/pink (or circled, boxed, highlighted) becomes **bold** in the note and is the first candidate for a pearl and an Anki row.
- **Unreadable** → write `[unclear]`. Never guess a drug name, number or eponym. A word you can read but think is wrong (page says X, textbook says Y) → keep X in the body and put Y in a footnote: "The page reads X; standard texts give Y."
- **Figures.** For every picture on the page write one line in the transcript: position, what it shows, every label you can read. This list drives section E.
- **Timestamps** (`00:08:36`) next to headings are the lecture video position; keep them in the frontmatter `source` line, not in the headings.
- Keep the page's own section names as the `##` headings (add one emoji in front, house style). Do not merge, reorder or rename sections.

---

## D. Main note template (house style)

Filename: the page title in title case, e.g. `Hernia and Hernia Surgeries.md`. Frontmatter keys are fixed — `check` rejects a missing one:

```markdown
---
title: <Topic>
aliases: [<2–4 search terms>]
rank: 1
status: not-started
topic: <Subject, e.g. Surgery / Anatomy>
subtopic: <chapter name from the page title>
target_exams:
  - NEET PG
  - INI-CET
  - FMGE
past_exam_questions: []
anki_link: ""
case_files: []
difficulty: easy | medium | hard
high_yield: true
guideline_criteria: "<named classifications / criteria on the page, or empty>"
source: "Handwritten notes — <page title> (sections: <heading> <timestamp> · …)"
mindmap: "[[<Topic> — Mind Map]]"
review_day_2: false
review_day_4: false
review_day_7: false
review_day_10: false
review_day_15: false
---
# <emoji> <Topic>

> [!abstract] Core Definition
> <two or three lines: what the topic is and the two or three questions everything in it answers>

---

## 🧠 Mental Model — <one phrase>
<two or three sentences, then an ASCII flow in a ``` code block — flows and ladders are drawn this way, never as images>

---

## <emoji> <Page section 1, in page order>
<tables / lists exactly as on the page, callouts for boxed notes, images or image prompts where the page had figures, 🎬 Watch line, one embedded video>

…one `##` per page section…

---

## Core Dictum & Pattern Recognition
<section H, verbatim format>

---

## 🏆 Pearls (High-Yield Summary)
> [!success] Must-Know Pearls
> 1. … (8–13 numbered lines; every red/boxed item from the page appears here)

## 🔁 One-Line Recall
``` <a 3–8 line ASCII recall chain> ```

## 🧩 Anki Flash Points
| ❓ | ✅ |  (one row per testable fact, answer in bold; 20–50 rows)

## 🎬 Video Library
| What to watch | Link |  (every video used in the note)

## 🖼 Infographic Prompt — One-Page Summary
<section J>

## 📚 References
- Handwritten notes — <page title> (sections …)
- <textbooks / guidelines actually drawn on>
- Wikimedia Commons — all embedded images (licence noted in captions)

[^1]: …   (footnote definitions, last thing in the file)
```

**Callout vocabulary** (keep to these): `[!abstract]` definition / infographic prompt · `[!info]` mechanism or key fact · `[!tip]` mnemonic or "why" · `[!note]` side box from the page · `[!warning]` caution, exception · `[!danger]` complication, contraindication, applied anatomy that kills · `[!success]` most-commons, pearls · `[!example]-` collapsed image prompt. Use `>` continuation lines; a blank `>` line separates paragraphs inside a callout.

**Tables:** header row + `|---|` row; one fact per cell; `—` for an empty cell the page left empty; a side-by-side comparison on the page becomes a two-column table with the two names as headers.

---

## E. Figures → images or image prompts

For every figure listed in the transcript, in this order of preference:

1. **The user's own image**, if they uploaded the figure separately → keep it as `![[name]]` in the vault's attachments.
2. **Wikimedia Commons** (public domain, CC BY, CC BY-SA):
   - Search `site:commons.wikimedia.org <term> file` (also try Gray's Anatomy plates, OpenStax, CDC, Wellcome Collection, NIH). Take the **exact file title from the result URL** (`File:Hernia_mesh_1.jpg` → `Hernia mesh 1.jpg`). Never guess a title.
   - `python3 _tools/notes_digitize.py wmurl "Hernia mesh 1.jpg" --width 800` prints the direct URL (and a thumbnail URL for SVG/GIF/TIFF, which Obsidian needs).
   - `python3 _tools/notes_digitize.py look <url> --out work/<topic>/img` then **open the file and look at it**. Embed it only if it shows what the page's figure shows. If you cannot download (network blocked), say so in the report and ask the user to glance at the images once.
   - Embed as `![<alt>](<direct url>)` followed **on the next line** by an italic caption: what it shows, mapped to the page's wording, plus attribution and licence. `check` rejects a Wikimedia image without a caption.
3. **No free image** → a collapsed image-generation prompt where the figure sat:
   ```markdown
   > [!example]- 🎨 Image prompt — <figure name>
   > "<style: medical textbook illustration / surgical atlas / Netter-like>, <view and section>, white background, <palette>. <Every structure and label from the page's figure, named explicitly>. Label: <the page's labels>. <what to exclude: no text other than labels, no watermark>."
   ```
   One prompt per figure; name every label the page shows so the generated image matches the notes.
4. **Never** draw figures yourself as SVG, HTML or data-URI images, and never hotlink textbook scans or non-free sites. ASCII flowcharts in code blocks are fine (that is house style for flows and ladders).

Place each image or prompt **exactly where the page had the figure** — not collected at the end.

---

## F. Videos

- For every major section search `youtube.com <topic> <section> lecture OR animation` and, for clinical topics, `osmosis.org <topic>`. Preferred sources: Osmosis, Ninja Nerd, Armando Hasudungan, MedicoVisual, Dr Najeeb, Behind the Knife (surgery), JOMI and World Laparoscopy Hospital (operative videos).
- Under each section add a `🎬 **Watch:**` line with 1–3 links (title as link text), and embed the best one as `![](https://www.youtube.com/watch?v=…)` — Obsidian renders this as a player. One embed per major section is enough.
- Only link videos that appeared in a search result. If nothing fits, link a YouTube search instead: `https://www.youtube.com/results?search_query=<terms>` and say so in the report.
- Collect every link in the **🎬 Video Library** table at the end.

---

## G. Footnotes

Obsidian footnotes: `[^n]` in the text, `[^n]: …` definitions as the last block of the file (after References). Number in order of first use. Add one when:
- a fact is **not on the page** but completes a line (a cut-off value, a drug dose, the other half of a classification);
- an **eponym, date or guideline** deserves a sentence of history or the published definition;
- a word on the page was **unreadable or doubtful** — say what the page seems to read and what the textbook says;
- the page and the textbook **disagree** — the page stays in the body, the textbook goes in the footnote;
- an abbreviation could be misread.

Every main note needs at least a few footnotes; `check` rejects a note with none. Do not footnote things the page already explains.

---

## H. Core Dictum & Pattern Recognition

Analyse the finished transcript through five lenses — the single unifying principle; normal → compensated → decompensated progression; buzzwords that trigger each diagnosis; traps with what students think / why it is wrong / how to avoid it; connections to other topics — and write the block **in exactly this shape** (the user's "Medical Notes Enhancement Prompt"). Be specific: numbers, names, mechanisms; no generic advice.

```markdown
## Core Dictum & Pattern Recognition

> [!check]+ **🎯 Core Dictum - The Unifying Principle**
>
> [Two to four sentences: the one principle that makes the whole topic reason-able — WHY, not WHAT.]
>
> [Optional second paragraph reinforcing it.]

> [!example]+ **📊 Clinical Pattern Recognition**
>
> Understanding how the condition progresses through stages helps you recognize it at different phases and predict outcomes.
>
> **Stage 1 - Normal Physiology:**
> [2–3 sentences]
>
> **Stage 2 - Compensated/Early Pathology:**
> [3–4 sentences; symptoms minimal]
>
> **Stage 3 - Decompensated/Overt Disease:**
> [3–4 sentences; classic signs]
>
> **Progression Timeline:**
> Normal → [Trigger] → Early Changes → Compensation → Decompensation → Full Clinical Syndrome
>
> **Why This Matters Clinically:**
> [2–3 sentences: how the stage changes management]

> [!warning]+ **🔍 Diagnostic Buzzwords & Pattern Recognition**
>
> These are the key terms, phrases, and clinical patterns that should immediately trigger specific diagnoses in your mind. When you see these in a clinical vignette or real patient, you should think of the associated condition instantly.
>
> **Buzzwords by Condition:**
>
> **[Condition]:** "[buzzword phrase]" → [2–3 sentences tying it to mechanism]
> …
>
> **Visual/Imaging Buzzwords:**
> [findings with what they represent]
>
> **Severity Indicators:**
> [thresholds, scores, grades with numbers]

> [!danger]+ **⚠️ Common Traps & Pitfalls**
>
> These are the mistakes that students and clinicians commonly make with this topic. Being aware of these traps helps you avoid diagnostic errors and answer tricky exam questions correctly.
>
> **Trap 1: [name]**
>
> **What students think:** …
>
> **Why this is wrong:** [3–4 sentences, mechanism-based]
>
> **How to avoid this trap:** [a rule, mnemonic or framework]
>
> [3 to 5 traps]

> [!tip]+ **🔗 Related Concepts & Cross-Topic Connections**
>
> Understanding how this topic connects to other areas of medicine deepens your knowledge and helps you see the bigger picture. These connections also help you answer integrated questions on exams.
>
> **Related Topic 1: [[Topic Name]]**
> [2–3 sentences]
> … (3–6 topics; use [[wikilinks]] so they become vault links)
>
> **Clinical Integration:**
> [3–4 sentences]
>
> **Exam Integration:**
> [2–3 sentences]
```

For an anatomy or embryology page the "stages" are: the normal developmental/anatomical plan → the silent variant or compensated state → the clinical syndrome when it is loaded, infected or twisted.

---

## I. anatomed block

Add one block in the section where the anatomy is densest. Only these keys exist; every other line is read as a structure name, so **no bullets, bold, prose or wikilinks inside the fence**; `#` lines are comments:

````markdown
```anatomed
# retype a name with the plugin's autocomplete if it shows as "unmatched"
region: inguinal canal
parts: external oblique, internal oblique, transversus abdominis, inferior epigastric artery, spermatic cord
detail: related
title: Inguinal region
```
````

- `region:` / `parts:` — comma-separated structure names, English or Latin (up to ~15; the plugin caps at 60).
- `detail:` — `isolated` (default) | `related` (adds a few translucent neighbours) | `regional` (more neighbours). Case-sensitive.
- `title:` — optional heading.
- You cannot check the catalogue from here; say in the report that one or two names may need the autocomplete. Editing in the widget rewrites the block and drops the comment line — that is fine.

---

## J. Infographic prompt

The last content section of the main note. A single collapsed callout holding **one long prompt** that an image generator can turn into **one A4 portrait page** summarising the whole note:

```markdown
## 🖼 Infographic Prompt — One-Page Summary

> [!abstract]- 🎨 Prompt for an image generator (copy everything inside)
> "Design a single-page, portrait A4 medical study infographic titled **'<TOPIC>'** for a postgraduate <subject> exam. Flat-vector textbook style, off-white background, palette <3–4 named colours, each tied to a meaning>, thin icons, crisp legible text, generous white space. Lay it out as <N> panels in a <grid>:
>
> **Panel 1 — '<section 1 name>'.** <Every fact from that section, written out — tables as mini-tables, flows as arrows, with the exact labels.>
>
> **Panel 2 — …** (one panel per `##` section of the note, in order)
>
> Footer strip: <the 3–5 'most commons' or the one-line recall>. No watermark, no stock-photo people, illustration quality."
```

Rules: one panel per page section, every number and name in the note appears in some panel, name the colours and what they encode, say what to exclude.

---

## K. The mind-map note (mdmap)

Filename `<Topic> — Mind Map.md`, linked from the main note's `mindmap:` field and linking back in its own frontmatter (`source_note: "[[<Topic>]]"`). mdmap turns the note's own structure into the map, so the file must be shaped like a tree:

- Frontmatter, then **exactly one `# Root`** (the topic). Several `#` headings make mdmap add a root named after the file.
- `##` = main branches (the page's sections), `###` = sub-branches. **Never skip a level.**
- Leaves are `- bullets`, nested by **two spaces** per level. One idea per bullet, under ~100 characters, `→` for "gives rise to / leads to / implies", `≫` for "much more than".
- **No tables, no callouts, no code blocks, no prose paragraphs, no images.** Each would collapse into body text of the node above (a paragraph becomes a node titled by its first line). Turn every table row into a bullet and every callout into bullets under a heading.
- Nothing before the first heading except frontmatter.
- The map must **differ from the main note**: it is the skeleton of the topic, not a summary with pictures. Keep the page's section names as `##` so the two files line up, but drop the mental model, pearls, recall, Anki, video and infographic sections.

Skeleton (the `skeleton` command writes this from the main note's headings):

```markdown
---
title: <Topic> — Mind Map
type: mindmap
source_note: "[[<Topic>]]"
plugin: mdmap
status: not-started
---

# <Topic>

## <Section 1>
- <idea>
  - <sub-idea> → <consequence>
- <idea>

## <Section 2>
### <Subsection>
- …
```

`mapcheck` rejects a second `#`, a skipped heading level, a table/callout/fence line, a bare paragraph, odd-space indentation and over-long bullets.

---

## L. Final self-check (silently, before writing to the vault)

- [ ] `check` and `mapcheck` print `OK`.
- [ ] Every section heading from the page is present, in page order, with its table/list intact.
- [ ] Every figure on the page has an image (seen by you) or an image prompt at the same place; every Wikimedia image has an italic caption with licence.
- [ ] No figure was drawn by you (no SVG / HTML / data-URI images).
- [ ] Every major section has a 🎬 line; one video embedded per section; all collected in the Video Library.
- [ ] Footnotes: every fact not on the page has one; every `[^n]` is defined; the page's wording wins in the body.
- [ ] Core Dictum block has all five callouts in the exact format, specific to this topic.
- [ ] anatomed block uses only `region/parts/detail/title`.
- [ ] Infographic prompt covers every section.
- [ ] Mind-map note: one root, consecutive levels, bullets only, nothing copied from the main note's callouts.
- [ ] Low-resolution page → banner + `transcription_status` + ⚠ verify marks; otherwise no reconstruction at all.
- [ ] Existing vault note with content was not overwritten.

---

## M. Report (brief, per topic)

- note path and mind-map path (vault, or `obsidian-pending/` and why)
- page resolution and whether anything was reconstructed; every `[unclear]`
- images: how many from Wikimedia (and whether you could view them), how many image prompts and for which figures
- videos used
- anatomed names that may need the autocomplete
- any page-vs-textbook conflicts (now in footnotes)

Do not paste the note text into the report.
