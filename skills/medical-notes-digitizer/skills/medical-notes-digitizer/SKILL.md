---
name: "medical-notes-digitizer"
description: "Turn images of handwritten medical notes into Obsidian notes in the user's house style: faithful transcription, Wikimedia images and videos where the page had figures, image prompts where no free image exists, footnotes, a Core Dictum & Pattern Recognition section, an infographic prompt, an anatomed 3D block, and a separate mdmap mind-map note. Use when asked to digitise, OCR, convert or make Obsidian notes from note images or scans."
---

# Handwritten note images → Obsidian notes + mind map

Turns photographed or scanned pages of the user's medical notes into **two Obsidian files per topic**:

1. **The main note** — the page transcribed faithfully in the user's house style (section D), with every figure on the page replaced by a **free web image**, or **cropped out of the page itself** when the web has none (an **image-generation prompt** only as the last resort), one or more **videos** per section, **footnotes** for anything not on the page, **etymology footnotes** that pop up on hover for every eponym and Greek/Latin term, a **Core Dictum & Pattern Recognition** block, an **anatomed** 3D block, and an **infographic prompt** at the end.
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
2. **Helper script:** copy `scripts/notes_digitize.py` (next to this file) to `_tools/notes_digitize.py`. `pip install pillow numpy`, plus `pip install pymupdf` for PDF pages (or poppler's `pdftoppm`). If installing is blocked, run the steps in your workspace and copy the finished notes back.
3. **Vault:** `devd` must be a connected folder. Ask the user **once** which folder the notes go in (for example `ATLAS/<Subject>/`) and keep using it. Until the vault is connected, every note goes to `obsidian-pending/`.
4. **Hover popovers:** the etymology footnotes show on hover only when Obsidian's core plugin **Page preview** is on (Settings → Core plugins → Page preview). Say so once if the user asks why they do not pop up.
5. **Plugins the notes are written for** (both are optional on the user's side; the notes degrade gracefully without them):
   - **mdmap** (`pererinha/mdmap`) — opens the *current note* as an editable mind map ("Edit current note as mind map"). Headings and bullets are nodes; tables, callouts, code blocks and images are only *body text* of the node above. This is why the mind-map note is a separate, bare file.
   - **anatomed** (`pitfa19/anatomed-obsidian`) — renders a fenced ```anatomed block as a rotatable 3D model (Z-Anatomy catalogue). It is **not** a mind-map plugin. Section I has the syntax.

---

## B. Each run ("digitise my notes", "make Obsidian notes from these pages", images dropped in)

1. **Gather and group.** Each page image has a title at the top (e.g. `HERNIA, THORAX AND SKIN`, `EMBRYOLOGY`). One topic = one page title. A **PDF** is turned into page images first — `python3 _tools/notes_digitize.py pages inbox/<file>.pdf --out work/<topic>/pages --native` pulls the scanned page images out at their own resolution (best for scanned or photographed notes; without `--native` the PDF is rendered at 200 dpi) — and each page image is then treated like a photographed page. A folder of many PDFs (a whole subject) follows section B2. A page usually holds several timestamped section headings (`Hernia and Hernia Surgeries 00:00:52`); keep them as `##` sections. Split a topic into two notes only when the transcript passes ~450 lines, and then at a major heading.
2. **Resolution gate.** `python3 _tools/notes_digitize.py slice inbox/<page> --out work/<topic>/strips`. If it prints a **WARNING (< 1000 px wide)**, stop and ask the user for the original file (one full-size PNG/JPG per page, uploaded as a *file*, not pasted into the chat — pasted images arrive at 200–350 px). Only if the user says to go ahead anyway: write the note with `transcription_status: reconstructed-from-low-res-scan`, a `[!warning]` banner at the top saying what was and was not legible, and **⚠ verify** after every line you filled from a textbook instead of the page.
3. **Read every strip in order** and write `work/<topic>/transcript.md` first — the raw, faithful transcript (section C). Do not start the note before the transcript is complete.
4. **Build the main note** from the template in section D, section by section in page order.
5. **Replace each figure.** `python3 _tools/notes_digitize.py detect <page> --out work/<topic>/figs` boxes the pictures on the page; open the `_boxes.png` overlay, then for each figure in the transcript's list: web image → crop from the page → image prompt (section E).
6. **Add videos** (section F).
7. **Add footnotes** (section G) and the three etymology layers — term footnotes, process/mechanism footnotes with prefix-root-suffix split and differentiation, and prefix/suffix footnotes on the first word that carries each affix (section G2).
8. **Write the Core Dictum & Pattern Recognition block** (section H).
9. **Add the anatomed block** (section I) and the **infographic prompt** (section J).
10. **Write the mind-map note** (section K): `python3 _tools/notes_digitize.py skeleton work/<topic>/<Title>.md --out "work/<topic>/<Title> — Mind Map.md"`, then fill it.
11. **Check:** `check` on the main note and `mapcheck` on the map. Fix every line until both print `OK`. With network, add `--net` to `check` so every image URL is HEAD-requested.
12. **Write into the vault.** Never overwrite a note that already has content — if the target exists and is not empty, save the new version to `obsidian-pending/` and say so. If the vault is not connected, everything goes to `obsidian-pending/`.
13. **Move** the page images from `inbox/` to `done/<topic>/`.
14. **Report** (section M).

---

## B2. A whole subject (a folder of chapter PDFs)

When the user hands over a subject split into many PDFs ("Physiology main notes", one PDF per topic):

1. **Pages:** `pages <all pdfs> --out work/<subject>/pages --native` → one folder per PDF.
2. **Chapter list first.** Read the big centred title on the first page of every PDF, and scan the remaining pages for **a second title page inside a PDF** (OCR every page and look for the title line next to the "Active space" marker, then look at the candidates) — several PDFs hold two chapters. Each chapter (not each PDF) gets one main note + one mind map, named exactly by its title in title case. Write the list (number, title, unit, page folder, image range, book pages) before writing any note; it fixes every file name and every cross-link.
3. **Units:** group chapters into numbered unit folders that follow the book (`01. General Physiology/`, `02. Nerve-Muscle Physiology/` …) — the running header on inner pages ("74 Central Nervous System") tells you the unit. Mind maps go in `<unit>/Mind Maps/`; all crops in one `<subject>/attachments/` named `<Title> - <what it shows>.png`.
4. **Frontmatter for a chapter:** add `chapter: <n>`, `pages: "<a>–<b>"`, `index: "[[<Subject> — Index]]"`; `topic:` is the subject, `subtopic:` the unit; `source:` lists every section heading with its timestamp.
5. **Pilot, then fan out.** Write the first chapter yourself to the full standard and get it through `check`/`mapcheck`. Then split the rest across parallel workers (~15–20 pages each), each given this skill, the pilot as the exact template, its chapters from the list, the watermark list and the "no git" rule. Re-check every returned note yourself.
6. **Index note** `<Subject> — Index.md` at the subject root: one table per unit (chapter link · map link · pages) plus a short "threads that run through the subject" callout linking chapters that belong together.
7. **Cross-links:** each note's *Related Concepts* callout links 4–6 other chapters by exact title. When all notes exist, `check --vault <vault> --links` fails any wikilink that does not match a note.
8. **Watermarks:** scanned course notes carry a buyer's email, an ID hash, a site name, "Active space", a "Feedback" tab, page footers and the lecturer's video thumbnail. None of it is transcribed; crops avoid it or white it out with `"mask"` rectangles in the crop spec. `check` fails a note that contains any email address, a long hex ID hash, or a string listed in the script's `WATERMARKS`.
9. **Search budget is shared.** Web searches (≈200 per turn) are counted across *all* parallel workers. Fifteen workers that each search freely for figures and videos exhaust it within minutes, and the later ones end up with crops only and YouTube *search* links. So: tell each worker it may search only for **figures** (≤ 2 searches per chapter), write notes with `youtube.com/results?search_query=…` placeholders for videos, and run the **video pass** afterwards as its own small job — about 10 chapters per worker, ≤ 3 searches per chapter, real `watch?v=` ids taken only from search results, one embed per note, Video Library rows rewritten.
10. **Hidden chapters.** A PDF can hold two or three chapters (a second big centred title on an inner page, timestamps that restart at 00:00:xx, a new "Page 1/n" counter). Workers must report any title page they find that is not in your list; give each its own note and slot it in order. Number chapters with whole numbers only **after** every worker has reported — a script rewrites `chapter:` / `rank:` from the final ordered list and regenerates the index from each note's `pages:` field.
11. **Crops are big.** Page crops are upscaled 2× when small; hundreds of them reach ~100 MB. Before committing, re-save each as a 256-colour PNG at most 1100 px wide (keep the file name; embeds point at it) — about 55 % smaller with no loss of legibility for line drawings and handwriting.
12. **Unknown image widths.** A Wikimedia thumbnail wider than the original file fails to load. For PNG/JPG/GIF whose width you do not know, use the direct URL from `wmurl` (no `--width`); thumbnails are safe for SVG.
13. **Validate the whole vault at the end:** `check <all notes> --vault <vault> --links`, `mapcheck <all maps>`, then confirm every `![[embed]]` exists and every attachment is embedded somewhere.

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

## 🎬 Video Library
| What to watch | Link |  (every video used in the note)

## 🖼 Infographic Prompt — One-Page Summary
<section J>

## 📚 References
- Handwritten notes — <page title> (sections …)
- <textbooks / guidelines actually drawn on>
- Wikimedia Commons — all embedded images (licence noted in captions)

[^1]: …   (footnote definitions — ordinary notes, then the term, process and affix etymology notes — last thing in the file)
```

**Callout vocabulary** (keep to these): `[!abstract]` definition / infographic prompt · `[!info]` mechanism or key fact · `[!tip]` mnemonic or "why" · `[!note]` side box from the page · `[!warning]` caution, exception · `[!danger]` complication, contraindication, applied anatomy that kills · `[!success]` most-commons, pearls · `[!example]-` collapsed image prompt. Use `>` continuation lines; a blank `>` line separates paragraphs inside a callout.

**Tables:** header row + `|---|` row; one fact per cell; `—` for an empty cell the page left empty; a side-by-side comparison on the page becomes a two-column table with the two names as headers.

---

## E. Figures → web image, page crop, or image prompt

For every figure listed in the transcript, in this order of preference:

1. **The user's own image**, if they uploaded the figure separately → keep it as `![[name]]` in the vault's attachments.
2. **A clear free image from the web — search hard before giving up.** (public domain, CC BY, CC BY-SA):
   - Run **at least three searches** per figure before concluding there is none: the English term, the Latin / eponymous name, and a synonym or the structure's parent region, each with `diagram`, `illustration` or `photograph`; use the thorough search mode. Look in `site:commons.wikimedia.org … file`, the Commons *category* page for the structure (it lists every file), the images used by the Wikipedia article, Gray's Anatomy plates (1918, public domain), OpenStax Anatomy & Physiology, CDC / NIH / NLM Open-i, the Wellcome Collection, and open-access journal figures on PMC that carry a CC BY licence. Take the **exact file title from the result URL** (`File:Hernia_mesh_1.jpg` → `Hernia mesh 1.jpg`). Never guess a title.
   - A web image must be **clear and correct**: labels readable at 800 px and showing the same structures as the page's figure. A pretty picture of the wrong thing is worse than a crop.
   - `python3 _tools/notes_digitize.py wmurl "Hernia mesh 1.jpg" --width 800` prints the direct URL (and a thumbnail URL for SVG/GIF/TIFF, which Obsidian needs).
   - `python3 _tools/notes_digitize.py look <url> --out work/<topic>/img` then **open the file and look at it**. Embed it only if it shows what the page's figure shows. If you cannot download (network blocked), say so in the report and ask the user to glance at the images once.
   - Embed as `![<alt>](<direct url>)` followed **on the next line** by an italic caption: what it shows, mapped to the page's wording, plus attribution and licence. `check` rejects an image without a caption.
3. **No free equivalent → crop the figure out of the page.** The page is the user's own notes, so its pictures belong in the user's vault:
   - `detect` has already proposed boxes (it finds photographs and coloured diagrams; pale line drawings it misses you box by hand from the strip images — the strip file names carry the y offset, and strips are zoomed, so divide by the zoom).
   - Write `work/<topic>/crops.json` — one entry per figure with the page file, the box `[x0, y0, x1, y1]` in page pixels (tight to the figure, keep its labels, leave out surrounding text and the page's own caption), the file name `"<Topic> - <figure>.png"` and a caption.
   - `python3 _tools/notes_digitize.py crop --spec work/<topic>/crops.json --out "<vault>/<attachments folder>"` (ask once where the vault keeps attachments; default `attachments/` next to the note). It prints the `![[name]]` embeds with captions — paste each where the figure sits on the page. A crop item can carry `"mask": [[x0, y0, x1, y1], …]` (page pixels) — those rectangles are painted white before cropping, for a watermark, an email or a video thumbnail that falls inside the figure. Open every crop and check nothing is cut off; adjust the box and re-run with `"overwrite": true`.
   - **If the crop is blurred** (page narrower than ~1000 px, labels unreadable, or the figure is itself a poor photocopy) or the page's figure is **not correct**, go back to step 2 and search again, harder, with new terms — a clear web image beats a blurred crop. Keep the crop only when that second search finds nothing, embed it anyway (it is the user's own figure), add the image prompt from step 4 directly below so the figure can be regenerated, and say in the caption that the crop came from a low-resolution page.
4. **Image prompt** — only when there is no free image *and* the page's figure cannot be cropped (missing, illegible, or the user asked for a drawn version). A collapsed callout where the figure sat:
   ```markdown
   > [!example]- 🎨 Image prompt — <figure name>
   > "<style: medical textbook illustration / surgical atlas / Netter-like>, <view and section>, white background, <palette>. <Every structure and label from the page's figure, named explicitly>. Label: <the page's labels>. <what to exclude: no text other than labels, no watermark>."
   ```
   One prompt per figure; name every label the page shows so the generated image matches the notes.
5. **Never** draw figures yourself as SVG, HTML or data-URI images, and never hotlink textbook scans or non-free sites. ASCII flowcharts in code blocks are fine (that is house style for flows and ladders).

Place each image, crop or prompt **exactly where the page had the figure** — not collected at the end. A page with a photograph the web does not have (a clinical picture, an operative photo) is the normal case for step 3.

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

## G2. Etymology footnotes (hover popovers) — terms, processes, prefixes and suffixes

Everything etymological lives in footnotes, so the reader hovers a marker and reads; there is **no separate glossary or word-parts section**. Three layers, all required:

**1. Term footnotes.** Every **eponym** (Hesselbach, Meckel, Bochdalek, DiGeorge…) and every anatomical or clinical term built from **Greek or Latin roots** (hernia, bubonocele, meralgia paraesthetica, notochord, mesonephric…) gets a footnote **immediately after the term's first use** in the body (inside a table cell or heading is fine).

**2. Process and mechanism footnotes.** Every word that names a **process, mechanism, state or failure** — the *-ation / -ion / -sis / -y* words and their verbs: reduction, obstruction, strangulation, incarceration, peristalsis, occlusion, invagination, entrapment, recurrence, adhesion, ischaemia, necrosis, inflammation vs infection, resection vs dissection vs excision; neurulation, induction, fusion, migration, rotation, regression, obliteration, persistence, herniation, descent, hypoplasia, atresia, degeneration, differentiation, septation, ossification… Each of these footnotes:
   - **splits the word into its parts** — prefix + root + suffix, each with its meaning in quotes (*ob-* "against" + *struere* "to build" + *-ion* "the process");
   - gives the sense that joins the parts to the medical meaning;
   - **differentiates it from its look-alikes and the terms it is graded against** — the stage sequence (irreducible → obstructed → strangulated), the sibling words (hypoplasia / aplasia / agenesis / atrophy / dysplasia; cyst / sinus / fistula; ischaemia / necrosis / gangrene), or the prefix family (extra- / pre- / intra- / trans- / retro-peritoneal).

**3. Prefix and suffix footnotes.** Every prefix and every suffix that occurs in the note gets its own footnote, attached to the **first word in the note that carries it** — placed right after that word's own term footnote if it has one (`**Bubonocele**[^ety-bubonocele][^suf-cele]`). Its text gives the affix, its meaning, the note's own examples, and the look-alikes it must not be confused with. A classic set (-tomy / -ectomy / -stomy / -tome · -plasia / -plasty / -trophy / -genesis · -rrhage / -rrhoea / -rrhaphy · hypo- / hyper- / sub- · para- / peri- / pre- / post- · ecto- / meso- / endo- · pro- / meso- / meta-nephros · ilio- / ileo- · -cele / -coele) goes in whenever one member appears, because the point of the note is to separate them. Typically 12–25 prefixes and 10–15 suffixes per note; `check` requires at least 10 affix footnotes.

**Footnote wording — the word, then the explanation, nothing else in front:**

```markdown
**Bubonocele**[^ety-bubonocele][^suf-cele] | sac limited to the canal
… loses its cough impulse[^ety-impulse] …
… meralgia **para**esthetica[^ety-meralgia][^pre-para] …

[^ety-bubonocele]: **bubonocele** — Greek *boubōn*, "groin; a swelling in the groin" (the same root as the *bubo* of plague) + *kēlē*, "hernia" — a hernia still within the groin.
[^ety-obstruction]: **obstruction** — Latin *ob-*, "against, in the way" + *struere*, "to build" + *-ion*, the process → something built in the way; the lumen is blocked. **Differentiate the three stages:** *irreducible / incarcerated* (stuck; blood supply may be fine) → *obstructed* (lumen blocked, supply intact) → *strangulated* (supply throttled).
[^suf-cele]: **-cele** — swelling, hernia: omentocele, enterocele, bubonocele, hydrocele. Don't confuse with **-coele / -coel** a body cavity (coelom) · **-cle** small (tubercle, vesicle).
[^pre-para]: **para-** — beside, abnormal: meralgia paraesthetica. Don't confuse with **peri-** around (peritoneum) · **pre-** before (preperitoneal) · **post-** after.
```

Rules for all three layers:
- Keys: `ety-<term>` for terms and processes, `pre-<affix>` for prefixes, `suf-<affix>` for suffixes, lower-case ASCII (`ety-corona-mortis`, `pre-para`, `suf-rrhaphy`). The definition **starts with the bold word or affix, then an em dash** — never a label such as "Etymology"; `check` enforces this.
- One to three lines each: root language, root words with meanings in quotes, the connecting sense, and the differentiation. For an eponym: full name, dates, nationality and role, year of the description. Add nothing you are unsure of — a wrong date in a footnote is worse than none; if the origin is disputed say so in four words ("origin uncertain").
- One footnote per term or affix; a term that recurs is marked once. Related words may share one note (`ety-tomes` for dermatome / myotome / sclerotome; `ety-section` for resection / dissection / excision / incision) and one key may be referenced from each of them.
- A marker never goes inside an image's alt text, a wikilink or a code block — put it in the italic caption line instead. Several markers may sit side by side after one word.
- Aim for **every** eponym, root-built term, process word and affix on the page — typically 60–100 footnotes per note; `check` rejects fewer than 12 term/process notes or fewer than 10 affix notes.
- Obsidian shows the footnote text in a popover when the reader hovers the marker (core plugin **Page preview** must be on), so the reader never has to scroll.

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

- [ ] `check` and `mapcheck` print `OK` (no Anki section — the user's cards come from the PYQ skill, not from these notes).
- [ ] Every section heading from the page is present, in page order, with its table/list intact.
- [ ] Every figure on the page has an image (seen by you) or an image prompt at the same place; every Wikimedia image has an italic caption with licence.
- [ ] No figure was drawn by you (no SVG / HTML / data-URI images).
- [ ] Every page crop is in the vault's attachments folder, embedded with `![[name]]`, captioned, and checked with your own eyes; crops from a low-resolution page are paired with an image prompt.
- [ ] No footnote marker inside a ``` code block (ASCII flows, recall blocks) — markers there do not render; `check` fails it.
- [ ] No watermark text (emails, ID hashes, site names) anywhere in the note or inside a crop.
- [ ] Etymology: every eponym, Greek/Latin term **and process/mechanism word** has a `[^ety-…]` footnote after its first use; every prefix and suffix has a `[^pre-…]` / `[^suf-…]` footnote on the first word that carries it; each definition starts with the bold word or affix and an em dash (no "Etymology" label); process notes split into prefix + root + suffix and differentiated from look-alikes; no marker inside alt text.
- [ ] Every blurred crop or doubtful web image triggered a second, harder search before it was kept.
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
- figures: how many from Wikimedia (and whether you could view them), how many cropped from the page (and whether the page was full-resolution), how many image prompts and for which figures
- etymology footnotes added (count: terms + processes / prefixes / suffixes), and any term whose origin you could not source
- figures where a blurred crop or doubtful image sent you back to search, and what the second search found
- videos used
- anatomed names that may need the autocomplete
- any page-vs-textbook conflicts (now in footnotes)

Do not paste the note text into the report.
