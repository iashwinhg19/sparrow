---
title: Endocrine Pancreas
aliases: [Endocrine Pancreas, Islets of Langerhans, Insulin, Glucagon, Incretins]
rank: 55
status: not-started
topic: Physiology
subtopic: Endocrine System
chapter: 55
pages: "235–238"
target_exams:
  - NEET PG
  - INI-CET
  - FMGE
past_exam_questions: []
anki_link: ""
case_files: []
difficulty: medium
high_yield: true
guideline_criteria: ""
source: "Physiology main notes (Marrow 8) — Endocrine Pancreas, pp. 235–238 (sections: Insulin 00:07:35)"
mindmap: "[[Endocrine Pancreas — Mind Map]]"
index: "[[Physiology — Index]]"
review_day_2: false
review_day_4: false
review_day_7: false
review_day_10: false
review_day_15: false
---
# 🍬 Endocrine Pancreas

> [!abstract] Core Definition
> The endocrine pancreas[^ety-pancreas][^pre-pan] is the **islets of Langerhans** — clusters of α, β, δ and F cells scattered through the exocrine gland (most abundant in the **tail**). Its central hormone, **insulin** from β cells, is the body's **only hypoglycaemic hormone** and its **major anabolic (storage) hormone**. The chapter answers:
> - ✅ **How does a β cell "sense" glucose and release insulin?** — GLUT-2 → glucokinase → ATP → K-ATP channel closes → depolarisation → Ca²⁺ → exocytosis
> - ✅ **How does insulin act?** — tyrosine-kinase receptor → IRS → PI-3-kinase (GLUT-4, metabolism) and MAPK (growth)
> - ✅ **What raises or lowers it, and how do drugs exploit that?** — glucose, incretins, ANS; sulfonylureas, diazoxide, GLP-1 analogues, gliptins

---

## 🧠 Mental Model — A Fuel Gauge Wired to a Fuse

Think of the β cell as a **fuel gauge wired to a fuse**. Glucose flows in freely (GLUT-2) and is burned; the more fuel, the more **ATP**. ATP is the hand that **closes the K-ATP "fuse"** — K⁺ can no longer leak out, the cell depolarises, Ca²⁺ gates open and insulin granules are fired out. Insulin then tells muscle and fat to **open their own doors (GLUT-4)** and store the fuel. Every drug in this chapter either holds that fuse shut (sulfonylureas → more insulin) or forces it open (diazoxide → less insulin), or amplifies the gut's "food is coming" signal (incretins).

```
GLUCOSE ─GLUT-2─► glucokinase ─► G6P ─► pyruvate ─► ↑ ATP ─► K-ATP channel CLOSES (sulfonylurea receptor)
     ─► K+ retained ─► DEPOLARISATION ─► voltage-gated Ca2+ channel OPENS ─► Ca2+ in ─► SNARE ─► EXOCYTOSIS
     (insulin + amylin + C-peptide, 1 : 1)

INSULIN ─► receptor (α outside, β = tyrosine kinase) ─► IRS ─┬─► PI-3-kinase → GLUT-4 insertion, metabolic actions
                                                            └─► MAPK          → growth
STORE (↑ glycogenesis, lipogenesis, glycolysis)  ·  STOP (↓ glycogenolysis, gluconeogenesis, lipolysis, ketogenesis)
```

---

## 🏝 Islets of Langerhans — Cell Types

![[Endocrine Pancreas - pancreas and islet of Langerhans.png]]
*The pancreas — head, body and tail (tail: "abundant in islet of Langerhans"), the pancreatic duct and common bile duct, lobules; enlarged below, the acini (acinar cells secrete digestive enzymes; exocrine cells secrete pancreatic juice) surrounding a pale pancreatic islet whose cells secrete hormones — "islet of Langerhans aka endocrine pancreas" (cropped from the handwritten page).*

| Cell type | Hormone(s) secreted & functions |
|---|---|
| **α cells** | • **Glucagon**[^ety-glucagon]**: ↑ blood glucose.** |
| **β cells (majority of cells: 55 %)** | • **Insulin**[^ety-insulin]**: ↓ blood glucose.** • **Amylin**[^ety-amylin]**:** – potentiates action of insulin; – **drug form: Pramlintide**[^ety-pramlintide] **(Rx of DM).** • **C peptide**[^ety-c-peptide] **(endogenous**[^ety-endogenous][^pre-endo] **insulin marker):** – **C peptide assay used to estimate insulin release.** (**C peptide : Insulin = 1 : 1 → equimolar**[^ety-equimolar][^pre-equi] **ratio**) |
| **δ cells** | • **Somatostatin**[^ety-somatostatin]**: universal inhibitor.** |
| **F cells (least % of cells)** | • **Pancreatic polypeptide (PP)**[^ety-polypeptide][^pre-poly]. |

🧠 Because insulin and C-peptide are cut from the same proinsulin molecule and released together one-for-one, C-peptide tells you how much insulin the patient's **own** β cells are making — injected insulin carries no C-peptide.[^1]

- **Islet of Langerhans**[^ety-langerhans] **aka endocrine pancreas**; most abundant in the **tail of pancreas**.
- **Acinar**[^ety-acinar] **cells** secrete digestive enzymes — the **exocrine**[^ety-exocrine][^pre-exo] pancreas.

```anatomed
# pancreas and its ducts — retype a name with the plugin's autocomplete if it shows as "unmatched"
region: pancreas
parts: head of pancreas, body of pancreas, tail of pancreas, pancreatic duct, common bile duct, duodenum, spleen
detail: related
title: Pancreas — islets are densest in the tail
```

---

## 💉 Insulin

### Properties

- **Large protein hormone.**
- **Contains 51 amino acids.**
- **First protein:**
  - **Completely sequenced (by Sanger**[^ety-sanger]**).**
  - **Produced by recombinant**[^ety-recombinant] **DNA technology.**
- **Zinc stabilizes structure of insulin.**[^2]
- **Mutation in HNF (Hepatocyte**[^ety-hepatocyte][^suf-cyte] **Nuclear Factor) → Maturity Onset Diabetes of the Young (MODY)**[^ety-mody].

![[Endocrine Pancreas - insulin structure.png]]
*Structure of insulin: chain B (30 amino acids, red) and chain A (21 amino acids, green) — 51 in all — joined by two inter-chain disulphide (S–S) bridges, with one more S–S loop inside chain A (cropped from the handwritten page).*

### Release

```
Food intake → ↑ Blood glucose → Insulin release → ↓ Blood glucose
└─────────────────── Negative feedback system ───────────────────┘
```

- **Food intake → ↑ blood glucose → insulin release → ↓ blood glucose** = **negative feedback system**.

### Pancreatic β cell — mechanism of insulin release

![[Endocrine Pancreas - insulin release from the beta cell.png]]
*The pancreatic β cell (RMP = −90 mV). Step 1: glucose enters by GLUT-2 (glucose sensor) → glucokinase → glucose-6-phosphate → pyruvate → ATP. Step 2: ATP closes the ATP-sensitive K⁺ channel (sulfonylurea receptor) → K⁺ ↑↑↑ inside → depolarisation. Step 3: depolarisation opens the voltage-gated Ca²⁺ channel → Ca²⁺ → SNARE proteins act on the secretory granules. Step 4: exocytosis of insulin, amylin and C-peptide. Side notes: drugs that open or close the K-ATP channel; glucokinase mutation → MODY 2; GLUT-2 mutation → Fanconi–Bickel syndrome (cropped from the handwritten page).*

**RMP = −90 mV**

| Step | Event |
|---|---|
| **Step 1** | **Glucose → GLUT-2**[^ety-glut] **(glucose sensor)** → glucose →(**glucokinase**[^ety-glucokinase][^suf-ase]) **glucose 6 phosphate → pyruvate → ATP** |
| **Step 2** | **ATP closes K⁺ channels** — **ATP sensitive potassium channel (sulfonylurea**[^ety-sulfonylurea] **receptor)** → **K⁺ ↑↑↑** inside → **depolarisation**[^ety-depolarisation][^pre-de] |
| **Step 3** | Depolarisation **opens voltage gated calcium channel** → **Ca²⁺** in |
| **Step 4** | Ca²⁺ → **SNARE proteins**[^ety-snare] → **secretory granules** → **exocytosis**[^ety-exocytosis][^suf-osis] **of insulin, amylin, C peptide** |

> [!tip] **Drugs acting on the ATP-sensitive K⁺ channel**
> | Channel | Insulin | Use | Eg |
> |---|---|---|---|
> | **Opened** | **↓ Insulin** | **Rx of insulinoma**[^ety-insulinoma][^suf-oma] | **Diazoxide**[^ety-diazoxide] |
> | **Closed** | **↑ Insulin** | **Rx of DM** | **Sulfonylureas (insulin secretagogues**[^ety-secretagogue]**)** |

> [!warning] Mutations along the pathway
> - **Glucokinase —mutation→ MODY 2.**[^3]
> - **GLUT-2 —mutation→ Fanconi Bickel syndrome**[^ety-fanconi-bickel]**: defect in glucose sensing → ↓ insulin release → hyperglycemia**[^ety-hyperglycaemia][^pre-hyper][^suf-aemia].

```
GLUT-2 mutation → FANCONI–BICKEL SYNDROME: defect in glucose sensing → ↓ insulin release → hyperglycemia
Glucokinase mutation → MODY 2
```

### Transport

- **Sites (insulin dependent areas): muscle, adipose tissue, heart.**
- **Process: facilitated diffusion**[^ety-facilitated].
- **Transport protein: GLUT-4.**
- **During exercise, glucose enters skeletal muscle independent of insulin.**

```
Exercise ──activates──► AMP ──────► Insertion of GLUT-4 in skeletal muscle
└──────────────── AMP-activated kinase pathway ────────────────┘
```

- **Exercise → activates AMP → insertion of GLUT-4 in skeletal muscle** = **AMP-activated kinase pathway**[^ety-ampk].
- **Significance: exercise is important in Rx of DM.**

🧠 Two keys open the GLUT-4 door: insulin (through PI-3-kinase) and muscle contraction (through AMP-kinase). That is why exercise lowers blood glucose even in insulin resistance.[^4]

### Insulin receptor

![[Endocrine Pancreas - insulin receptor signalling.png]]
*The insulin receptor: two α subunits outside the cell membrane, two β subunits spanning it with tyrosine kinase activity → insulin-receptor substrates (IRS) → phosphatidylinositol-3′-kinase (PI-3-kinase) pathway, which mediates GLUT-4 insertion and metabolic actions, and mitogen-activated protein kinase (MAPK) pathway, which mediates promotion of growth (cropped from the handwritten page).*

```
        α   α        (outside)
   ─β───┴───┴───β─   Cell membrane
        Tyrosine kinase
              │
Insulin-receptor substrates (IRS)
        ┌─────┴─────┐
PI-3-kinase pathway      MAPK pathway
 • GLUT-4 insertion       • Promotion of growth
 • Metabolic actions
```

- **α α + β β subunits → tyrosine kinase**[^ety-tyrosine-kinase] → **insulin-receptor substrates (IRS).**
- **Phosphatidylinositol-3′-kinase (PI-3-kinase)**[^ety-phosphatidylinositol] **pathway → mediates GLUT 4 insertion, metabolic actions.**
- **Mitogen Activated Protein Kinase (MAPK)**[^ety-mitogen] **pathway → mediates promotion of growth.**

### Actions

```
                         Time dependent
            ┌──────────────────┴──────────────────┐
Rapid actions (within seconds)         Long term actions (in days)
• ↓ Blood glucose (via GLUT-4)        Major anabolic hormone : STORAGE
• ↓ K+ levels
   – Rx of hyperkalemia: insulin + dextrose
```

| Rapid actions (within seconds) | Long term actions (in days) |
|---|---|
| • **↓ Blood glucose (via GLUT-4).** • **↓ K⁺ levels** – **Rx of hyperkalemia**[^ety-hyperkalaemia]**: insulin + dextrose**[^ety-dextrose]. | **Major anabolic**[^ety-anabolic][^pre-ana] **hormone: storage.** |

**Pathways mediated:**

| Pathways stimulated | Pathways inhibited |
|---|---|
| • **Glycogenesis**[^ety-glycogenesis][^suf-genesis][^pre-glyco] | • **Glycogenolysis**[^suf-lysis] |
| • **Lipogenesis**[^ety-lipogenesis][^pre-lipo] | • **Neoglucogenesis**[^ety-neoglucogenesis][^pre-neo] |
| • **Glycolysis**[^ety-glycolysis] | • **Lipolysis** |
| — | • **Ketogenesis**[^ety-ketogenesis] |

🧠 Insulin's rule is "store, don't break": every pathway that builds a store (glycogen, fat) or burns glucose is switched on; every pathway that releases fuel (glycogen breakdown, new glucose, fat breakdown, ketones) is switched off. Its absence (type 1 DM) therefore produces hyperglycaemia **and** ketoacidosis.

### Factors affecting insulin secretion

| ↑ Insulin secretion | ↓ Insulin secretion |
|---|---|
| 1. **High blood glucose.** | 1. **Somatostatin.** |
| 2. **α cells: Glucagon.** | 2. **Streptozocin, Alloxan**[^ety-streptozocin]**: destroy β cells — used only for research experiments.** |
| 3. **Amino acids: Arginine, Leucine**[^ety-arginine-leucine]**.** | 3. **Sympathetic: α action (dominant action).** |
| 4. **Autonomic**[^ety-autonomic][^pre-auto] **nervous system:** – **Parasympathetic**[^pre-para]**: vagal**[^ety-vagus] **stimulation, acetylcholine**[^ety-acetylcholine]. – **Sympathetic**[^ety-sympathetic][^pre-syn]**: only β receptor stimulation.** | — |
| 5. **Gastrin**[^ety-gastrin]**, CCK**[^ety-cck]**, secretin**[^ety-secretin]**.** | — |
| 6. **Incretins**[^ety-incretin]**.** | — |
| 7. **Protein rich meal: also ↑ glucagon to prevent hypoglycemia**[^pre-hypo]**.** | — |

🧠 A protein-only meal raises insulin (to store the amino acids) — on its own that would drop glucose, so the same amino acids also raise glucagon to hold glucose steady. Sympathetic stimulation normally *lowers* insulin because the β-cell's α₂ receptors dominate; isolated β-receptor stimulation raises it.[^5]

### Applied aspect of incretins

- **Glucagon like Peptide 1 (GLP-1)**, **Glucose dependent insulinotropic**[^ety-insulinotropic] **peptide (GIP).**
- **Degraded by Dipeptidyl peptidase 4 (DPP-4)**[^ety-dpp4][^pre-di].
- **Oral glucose → stimulates incretins (GIT hormones) → ↑ insulin release compared to IV glucose.**

![[Endocrine Pancreas - incretin effect.png]]
*Incretin effect: the same glucose load raises plasma insulin far more when taken by mouth (blue) than when given IV (black), because oral glucose releases GLP-1 and GIP from the gut (cropped from the handwritten page).*

**Management of diabetes:**
- **GLP-1 analogues: Exenatide**[^ety-exenatide].
- **Dipeptidyl peptidase 4 (DPP-4) blockers: Gliptins (Eg. sitagliptin)**[^ety-gliptin] → **↓ degradation → prolonged action of GLP-1.**

### Glucose homeostasis[^ety-homeostasis]

```
                         Glucose homeostasis
              ┌───────────────────┴───────────────────┐
  Decrease in blood glucose                Increase in blood glucose
  (Hypoglycemic hormone): INSULIN          (Counter regulatory hyperglycemic hormones):
  Blood glucose < 30 mg/dl → Coma          • Growth hormone – dawn phenomenon
                                           • Glucagon • T3 • Cortisol • Epinephrine
```

| ↓ Blood glucose | ↑ Blood glucose |
|---|---|
| **Hypoglycemic hormone: Insulin.** | **Counter regulatory**[^ety-counter-regulatory][^pre-counter] **hyperglycemic hormones:** |
| **Blood glucose < 30 mg/dl → Coma**[^ety-coma].[^6] | • **Growth hormone** – **Dawn phenomenon**[^ety-dawn]**: early morning ↑ in glucose.** • **Glucagon** • **T₃** • **Cortisol**[^ety-cortisol] • **Epinephrine**[^ety-epinephrine][^pre-epi] |

🎬 **Watch:** [YouTube search — Ninja Nerd: insulin and glucagon](https://www.youtube.com/results?search_query=ninja+nerd+insulin+glucagon+endocrine+pancreas) · [YouTube search — Armando Hasudungan: insulin secretion from the beta cell](https://www.youtube.com/results?search_query=armando+hasudungan+insulin+secretion+beta+cell) · [YouTube search — incretin effect, GLP-1 and DPP-4 inhibitors](https://www.youtube.com/results?search_query=incretin+effect+GLP-1+DPP-4+inhibitors+explained)

---

## Core Dictum & Pattern Recognition

> [!check]+ **🎯 Core Dictum - The Unifying Principle**
>
> Blood glucose is defended by **one lowering hormone against five raising ones**. Insulin alone pushes glucose down — and it does so by **storing** fuel (glycogenesis, lipogenesis, GLUT-4 uptake) and **stopping** fuel release (glycogenolysis, gluconeogenesis, lipolysis, ketogenesis); glucagon, GH, cortisol, epinephrine and T3 all push it up. Losing insulin therefore removes the only brake: glucose rises and fat is broken into ketones.
>
> The β cell links **metabolism to electricity**: glucose → ATP → closure of the K-ATP channel → depolarisation → Ca²⁺ → exocytosis. Every drug and mutation in the chapter is a point on that chain — GLUT-2 (Fanconi–Bickel), glucokinase (MODY 2), the K-ATP channel (sulfonylureas close it, diazoxide opens it) — and the gut amplifies it through incretins (GLP-1, GIP), which is why oral glucose releases more insulin than IV glucose.

> [!example]+ **📊 Clinical Pattern Recognition**
>
> Understanding how the condition progresses through stages helps you recognize it at different phases and predict outcomes.
>
> **Stage 1 - Normal Physiology:**
> After a meal glucose enters the β cell by GLUT-2, ATP closes K-ATP channels and insulin, amylin and C-peptide are released 1 : 1; incretins amplify the response. Insulin binds its tyrosine-kinase receptor, inserts GLUT-4 in muscle, fat and heart, and switches the body into storage; between meals glucagon and the other counter-regulatory hormones hold glucose up.
>
> **Stage 2 - Compensated/Early Pathology:**
> In insulin resistance (obesity, inactivity) the PI-3-kinase arm weakens; β cells compensate by secreting more insulin, so glucose stays near normal while C-peptide and insulin are high. In monogenic defects (glucokinase MODY 2) the glucose "set point" is shifted up, giving mild, stable fasting hyperglycaemia. Exercise, through AMP-kinase, still opens GLUT-4 and helps compensation.
>
> **Stage 3 - Decompensated/Overt Disease:**
> When β cells fail (autoimmune destruction, exhaustion, streptozocin/alloxan in experiments, GLUT-2 defect in Fanconi–Bickel), insulin falls: hyperglycaemia, glycosuria, and — with no brake on lipolysis and ketogenesis — ketoacidosis. At the other extreme an insulinoma releases insulin regardless of glucose, and glucose below 30 mg/dL produces coma.
>
> **Progression Timeline:**
> Normal → insulin resistance or β-cell injury → compensatory hyperinsulinaemia → β-cell exhaustion → overt diabetes mellitus → ketoacidosis (absolute deficiency) / hyperglycaemic complications
>
> **Why This Matters Clinically:**
> Treatment targets the defective link: sulfonylureas close K-ATP channels if β cells still work, GLP-1 analogues and gliptins amplify the incretin signal, exercise recruits GLUT-4 independently of insulin, insulin replaces the missing hormone, and diazoxide opens K-ATP channels to curb an insulinoma. C-peptide distinguishes endogenous insulin (insulinoma, sulfonylurea misuse) from injected insulin.

> [!warning]+ **🔍 Diagnostic Buzzwords & Pattern Recognition**
>
> These are the key terms, phrases, and clinical patterns that should immediately trigger specific diagnoses in your mind. When you see these in a clinical vignette or real patient, you should think of the associated condition instantly.
>
> **Buzzwords by Condition:**
>
> **Insulinoma:** "Recurrent fasting hypoglycaemia with high insulin and high C-peptide" → autonomous β-cell tumour; diazoxide opens K-ATP channels to reduce release.
>
> **Exogenous insulin (factitious hypoglycaemia):** "High insulin, low C-peptide" → injected insulin has no C-peptide.
>
> **MODY:** "Young, non-obese, autosomal-dominant diabetes over three generations, no ketosis" → HNF mutations; MODY 2 = glucokinase (mild stable fasting hyperglycaemia).
>
> **Fanconi–Bickel syndrome:** "GLUT-2 defect", "hepatorenal glycogen accumulation, impaired glucose sensing" → ↓ insulin release → hyperglycaemia after meals.
>
> **Incretin effect:** "Oral glucose gives more insulin than IV glucose" → GLP-1 and GIP from the gut; exploited by exenatide and gliptins.
>
> **Dawn phenomenon:** "Early-morning rise in glucose in a diabetic" → nocturnal GH (and cortisol) surge — counter-regulation.
>
> **Visual/Imaging Buzzwords:**
> Islets = pale clusters among dark acini, densest in the pancreatic tail; insulin = chain A (21) + chain B (30) joined by disulphide bridges; incretin graph = tall oral curve over a flat IV curve.
>
> **Severity Indicators:**
> β cells 55 % of islet cells, F cells the fewest; insulin 51 amino acids; RMP of β cell −90 mV; C-peptide : insulin = 1 : 1; blood glucose < 30 mg/dL → coma.

> [!danger]+ **⚠️ Common Traps & Pitfalls**
>
> These are the mistakes that students and clinicians commonly make with this topic. Being aware of these traps helps you avoid diagnostic errors and answer tricky exam questions correctly.
>
> **Trap 1: Saying ATP opens the potassium channel**
>
> **What students think:** More ATP opens K⁺ channels to release insulin.
>
> **Why this is wrong:** ATP **closes** the ATP-sensitive K⁺ channel. With the K⁺ leak blocked, K⁺ accumulates inside, the membrane depolarises, voltage-gated Ca²⁺ channels open and Ca²⁺ triggers exocytosis via SNARE proteins. Sulfonylureas copy ATP (close the channel → ↑ insulin); diazoxide does the opposite (opens it → ↓ insulin, used for insulinoma).
>
> **How to avoid this trap:** "ATP shuts the K⁺ door → cell charges up → Ca²⁺ fires the granules."
>
> **Trap 2: Thinking every tissue needs insulin to take up glucose**
>
> **What students think:** Insulin is required for glucose entry into all cells.
>
> **Why this is wrong:** Only the GLUT-4 tissues — **skeletal muscle, adipose tissue and heart** — are insulin-dependent; liver, brain, RBCs, β cells (GLUT-1/2/3) take up glucose without insulin. Even muscle can bypass insulin during exercise through AMP-activated kinase.
>
> **How to avoid this trap:** "GLUT-4 = muscle, fat, heart — and exercise opens it too."
>
> **Trap 3: Mixing up the two sympathetic effects on insulin**
>
> **What students think:** Sympathetic activity raises insulin because the page lists it under ↑ secretion.
>
> **Why this is wrong:** Pure **β-receptor** stimulation raises insulin, but the **dominant** sympathetic effect is through **α (α₂) receptors, which inhibit** insulin release — so stress and exercise lower insulin and let glucose rise.
>
> **How to avoid this trap:** Net sympathetic = α wins = ↓ insulin; "only β" = ↑ insulin.
>
> **Trap 4: Forgetting why oral glucose beats IV glucose**
>
> **What students think:** The same glucose concentration should produce the same insulin response however it is given.
>
> **Why this is wrong:** Oral glucose also stimulates the gut incretins GLP-1 and GIP, which amplify glucose-stimulated insulin release (the incretin effect). DPP-4 normally destroys them within minutes; gliptins block DPP-4 and exenatide is a DPP-4-resistant GLP-1 analogue.
>
> **How to avoid this trap:** "The gut warns the pancreas" — incretins explain both the graph and the drugs.
>
> **Trap 5: Using total insulin to tell insulinoma from injected insulin**
>
> **What students think:** High insulin with hypoglycaemia always means an insulinoma.
>
> **Why this is wrong:** Injected insulin also gives high insulin. C-peptide is released only from the patient's own β cells, in an equimolar (1 : 1) ratio with insulin: high in insulinoma and sulfonylurea use, low after exogenous insulin.
>
> **How to avoid this trap:** "C-peptide = Certificate of own production."

> [!tip]+ **🔗 Related Concepts & Cross-Topic Connections**
>
> Understanding how this topic connects to other areas of medicine deepens your knowledge and helps you see the bigger picture. These connections also help you answer integrated questions on exams.
>
> **Related Topic 1: [[Gastrointestinal Hormones]]**
> Gastrin, CCK, secretin, GIP and GLP-1 all stimulate insulin; the incretin effect is a gut–islet conversation.
>
> **Related Topic 2: [[Pituitary Gland]]**
> GH is a counter-regulatory, diabetogenic hormone (dawn phenomenon); somatostatin, the δ-cell universal inhibitor, also inhibits GH.
>
> **Related Topic 3: [[Adrenal Gland]]**
> Cortisol and epinephrine are counter-regulatory hyperglycaemic hormones; the α-adrenergic brake on insulin release explains stress hyperglycaemia.
>
> **Related Topic 4: [[Membrane Transport]]**
> GLUT-2 and GLUT-4 are facilitated-diffusion carriers; K-ATP and voltage-gated Ca²⁺ channels turn metabolism into an electrical signal.
>
> **Related Topic 5: [[Cellular Messengers and Receptors]]**
> The insulin receptor is the classic receptor tyrosine kinase, signalling through IRS to PI-3-kinase and MAPK.
>
> **Related Topic 6: [[Exercise Physiology]]**
> Exercise inserts GLUT-4 through AMP-activated kinase, independent of insulin — the basis of exercise as diabetes therapy.
>
> **Clinical Integration:**
> Diabetes classification (type 1, type 2, MODY), oral hypoglycaemic drugs, the work-up of hypoglycaemia (insulin vs C-peptide), emergency treatment of hyperkalaemia with insulin + dextrose, and DKA all rest on this chapter.
>
> **Exam Integration:**
> Expect: islet cell percentages and hormones, amylin/pramlintide, C-peptide equimolar ratio, 51 amino acids and Sanger, zinc, HNF → MODY, β-cell steps and RMP, sulfonylurea vs diazoxide, Fanconi–Bickel (GLUT-2), GLUT-4 sites and AMPK, receptor pathways, pathways stimulated/inhibited, factors raising/lowering insulin, incretins and DPP-4, counter-regulatory hormones and the dawn phenomenon.

---

## 🏆 Pearls (High-Yield Summary)

> [!success] Must-Know Pearls
> 1. **α → glucagon (↑ glucose); β (majority, 55 %) → insulin, amylin, C-peptide; δ → somatostatin (universal inhibitor); F (least) → pancreatic polypeptide.**
> 2. **Amylin potentiates insulin — drug form pramlintide**; **C-peptide : insulin = 1 : 1 (equimolar)** → C-peptide assay estimates endogenous insulin release.
> 3. Islets of Langerhans = endocrine pancreas — **most abundant in the tail**.
> 4. Insulin: **large protein, 51 amino acids**, **first protein sequenced (Sanger)** and **first made by recombinant DNA**; **zinc stabilises** it; **HNF mutation → MODY**.
> 5. Release is **negative feedback**: food → ↑ glucose → insulin → ↓ glucose.
> 6. β cell (**RMP −90 mV**): **GLUT-2 (glucose sensor) → glucokinase → G6P → pyruvate → ATP → closes K-ATP (sulfonylurea receptor) → depolarisation → voltage-gated Ca²⁺ → SNARE → exocytosis of insulin, amylin, C-peptide.**
> 7. **K-ATP opened → ↓ insulin (diazoxide, insulinoma); closed → ↑ insulin (sulfonylureas, secretagogues)**; **glucokinase mutation → MODY 2**; **GLUT-2 mutation → Fanconi–Bickel** (↓ glucose sensing → hyperglycaemia).
> 8. **GLUT-4** (facilitated diffusion) in **muscle, adipose, heart**; **exercise → AMP-activated kinase → GLUT-4 insertion without insulin**.
> 9. Receptor: **α α β β, tyrosine kinase → IRS → PI-3-kinase (GLUT-4, metabolic) and MAPK (growth)**.
> 10. Rapid: ↓ glucose, **↓ K⁺ (insulin + dextrose for hyperkalaemia)**; long-term: **major anabolic (storage) hormone**.
> 11. **Stimulates glycogenesis, lipogenesis, glycolysis; inhibits glycogenolysis, gluconeogenesis, lipolysis, ketogenesis.**
> 12. **↑ secretion:** glucose, glucagon, arginine/leucine, vagus/ACh, β-stimulation, gastrin/CCK/secretin, **incretins**, protein meal; **↓:** somatostatin, **streptozocin/alloxan**, **sympathetic α (dominant)**.
> 13. **Incretins GLP-1, GIP** (degraded by **DPP-4**) → oral > IV insulin response; **exenatide** (GLP-1 analogue), **gliptins (sitagliptin)**; counter-regulatory: **GH (dawn phenomenon), glucagon, T3, cortisol, epinephrine**; **glucose < 30 mg/dL → coma**.

---

## 🔁 One-Line Recall

```
ISLETS (tail): α glucagon ↑ · β 55 % insulin + amylin (pramlintide) + C-peptide (1:1) · δ somatostatin · F PP (least)
INSULIN: 51 aa · Sanger · recombinant · zinc · HNF → MODY · release = negative feedback
β CELL (−90 mV): GLUT-2 → glucokinase (MODY 2) → ATP → K-ATP CLOSES (SU ↑ / diazoxide ↓) → depol → Ca2+ → SNARE → exocytosis
GLUT-2 defect = Fanconi–Bickel · GLUT-4 = muscle, fat, heart · exercise → AMPK → GLUT-4 without insulin
RECEPTOR: α2β2 tyrosine kinase → IRS → PI3K (GLUT-4, metabolic) / MAPK (growth) · rapid ↓glucose ↓K+ · long-term STORAGE
↑ glycogenesis, lipogenesis, glycolysis · ↓ glycogenolysis, gluconeogenesis, lipolysis, ketogenesis
INCRETINS GLP-1, GIP (DPP-4) → exenatide, gliptins · COUNTER: GH (dawn), glucagon, T3, cortisol, epinephrine · <30 mg/dL → coma
```

---

## 🎬 Video Library

| What to watch | Link |
|---|---|
| YouTube search — Ninja Nerd: insulin and glucagon | https://www.youtube.com/results?search_query=ninja+nerd+insulin+glucagon+endocrine+pancreas |
| YouTube search — Armando Hasudungan: insulin secretion from the beta cell | https://www.youtube.com/results?search_query=armando+hasudungan+insulin+secretion+beta+cell |
| YouTube search — Incretin effect, GLP-1 and DPP-4 inhibitors | https://www.youtube.com/results?search_query=incretin+effect+GLP-1+DPP-4+inhibitors+explained |
| YouTube search — Osmosis: insulin receptor signalling and actions | https://www.youtube.com/results?search_query=osmosis+insulin+receptor+signaling+actions |

---

## 🖼 Infographic Prompt — One-Page Summary

> [!abstract]- 🎨 Prompt for an image generator (copy everything inside)
> "Design a single-page, portrait A4 medical study infographic titled **'ENDOCRINE PANCREAS — ONE HORMONE DOWN, FIVE UP'** for a postgraduate physiology exam. Flat-vector textbook style, off-white background; colour code used everywhere: blue = insulin / lowering glucose, orange = glucagon and counter-regulatory hormones, green = drugs, red = diseases and mutations. Thin icons, crisp legible text, generous white space. Six panels:
>
> **Panel 1 — 'Islets of Langerhans'.** A pancreas (head, body, tail, pancreatic duct, common bile duct) with an arrow 'islets most abundant in the tail'; a magnified islet among acini ('acinar cells — digestive enzymes, exocrine'). A cell table: α — glucagon ↑ glucose; β (55 %) — insulin ↓ glucose, amylin (potentiates insulin; drug pramlintide), C-peptide (endogenous marker; C-peptide : insulin = 1 : 1, equimolar); δ — somatostatin (universal inhibitor); F (least) — pancreatic polypeptide.
>
> **Panel 2 — 'Insulin — properties and release'.** A bead model of chain A (21 aa) and chain B (30 aa) joined by disulphide bridges, '51 amino acids'. Badges: 'large protein', 'first protein sequenced — Sanger', 'first recombinant DNA protein', 'zinc stabilises', 'HNF mutation → MODY'. A loop 'food → ↑ glucose → insulin → ↓ glucose (negative feedback)'.
>
> **Panel 3 — 'β cell, step by step (RMP −90 mV)'.** Step 1 GLUT-2 (glucose sensor) → glucokinase (mutation → MODY 2) → glucose-6-phosphate → pyruvate → ATP; Step 2 ATP closes the ATP-sensitive K⁺ channel (sulfonylurea receptor) → K⁺ ↑↑↑ → depolarisation; Step 3 voltage-gated Ca²⁺ channel opens; Step 4 SNARE proteins → exocytosis of insulin, amylin, C-peptide. Side drug box: 'channel opened → ↓ insulin → diazoxide (insulinoma)'; 'channel closed → ↑ insulin → sulfonylureas (secretagogues, DM)'. Red tag 'GLUT-2 mutation → Fanconi–Bickel: defective glucose sensing → ↓ insulin → hyperglycaemia'.
>
> **Panel 4 — 'Transport and receptor'.** GLUT-4 icons on muscle, fat and heart 'insulin-dependent, facilitated diffusion'; a runner 'exercise → AMP → AMP-activated kinase → GLUT-4 insertion without insulin — exercise matters in DM'. A receptor: α α outside, β β across the membrane, tyrosine kinase → IRS → PI-3-kinase (GLUT-4 insertion, metabolic actions) and MAPK (growth).
>
> **Panel 5 — 'Actions and secretion'.** Timeline: rapid (seconds) ↓ glucose via GLUT-4, ↓ K⁺ (insulin + dextrose for hyperkalaemia); long-term (days) 'major anabolic hormone — storage'. Two columns: stimulated glycogenesis, lipogenesis, glycolysis / inhibited glycogenolysis, gluconeogenesis, lipolysis, ketogenesis. Secretion table: ↑ high glucose, glucagon, arginine & leucine, vagus/ACh, β-stimulation, gastrin/CCK/secretin, incretins, protein meal (also ↑ glucagon); ↓ somatostatin, streptozocin/alloxan (destroy β cells, research), sympathetic α (dominant).
>
> **Panel 6 — 'Incretins and glucose homeostasis'.** A graph of plasma insulin vs time: tall 'oral glucose' curve over a low 'IV glucose' curve, labelled 'incretin effect'; 'GLP-1, GIP — degraded by DPP-4'; drug chips 'exenatide (GLP-1 analogue)', 'gliptins — sitagliptin (DPP-4 blocker → prolonged GLP-1)'. A balance: left pan 'insulin — the only hypoglycaemic hormone; glucose < 30 mg/dL → coma'; right pan 'GH (dawn phenomenon), glucagon, T3, cortisol, epinephrine'.
>
> Footer strip: 'ATP shuts the K⁺ door · Ca²⁺ fires the granules · insulin stores, the others release'. No watermark, no photographs, illustration quality."

---

## 📚 References

- Physiology main notes (Marrow 8) — *Endocrine Pancreas*, pp. 235–238
- Guyton & Hall Textbook of Medical Physiology — Ch. 79, Insulin, glucagon and diabetes mellitus
- Ganong's Review of Medical Physiology — Endocrine functions of the pancreas and regulation of carbohydrate metabolism
- `Endocrine Pancreas - ….png` files in `attachments/` are crops of the handwritten pages (every figure of this chapter is the page's own)

[^1]: Proinsulin (86 amino acids) is cleaved in the secretory granule into insulin (A + B chains) and the connecting C-peptide; C-peptide has a longer half-life (~30 min vs ~5 min for insulin) and is not cleared by the liver on first pass, so it is the better index of β-cell secretion.
[^2]: In the granule insulin is stored as zinc-containing hexamers (six insulin molecules around two zinc ions); this crystalline packing stabilises it, and insulin analogues are engineered by changing how readily these hexamers dissociate.
[^3]: Glucokinase (hexokinase IV) has a low affinity for glucose (Km ≈ 8 mmol/L) and is not inhibited by its product, so its rate follows the blood glucose — it is the β cell's true "glucose sensor". Heterozygous loss of function (MODY 2) raises the set point; homozygous loss causes permanent neonatal diabetes.
[^4]: Insulin also stimulates GLUT-4 translocation through Akt (protein kinase B) downstream of PI-3-kinase; AMP-activated protein kinase senses the rise in AMP during contraction and triggers translocation by a separate pathway — the two effects are additive.
[^5]: Guyton: epinephrine and norepinephrine inhibit insulin secretion mainly through α₂-adrenergic receptors on β cells — the dominant effect in stress and exercise — whereas β₂ stimulation alone increases it.
[^6]: Textbooks usually define hypoglycaemia as plasma glucose < 70 mg/dL (symptoms from ~55 mg/dL); neuroglycopenic confusion, convulsions and coma appear as glucose falls further, typically below 30–40 mg/dL. The page's figure (< 30 mg/dL → coma) is kept in the body.
[^ety-pancreas]: **pancreas** — Greek *pan-*, "all" + *kreas*, "flesh" → "all flesh": a gland with no bone or cartilage (named by Herophilus/Rufus of Ephesus). Same *kreas* root as *creatine*.
[^ety-glucagon]: **glucagon** — Greek *glykys*, "sweet" (glucose) + *agōn*, "leading, driving" → the hormone that "drives up glucose"; named by Murlin and Kimball (1923) as the hyperglycaemic contaminant of early insulin extracts.
[^ety-insulin]: **insulin** — Latin *insula*, "island" + *-in* → the hormone of the islets; the name was coined by Jean de Meyer (1909), and the hormone isolated by Banting, Best, Macleod and Collip (1921–22).
[^ety-amylin]: **amylin (islet amyloid polypeptide, IAPP)** — Greek *amylon*, "starch" → *amyloid* ("starch-like" deposits) + *-in* → the peptide that forms the amyloid in islets of type 2 diabetics; it slows gastric emptying and suppresses glucagon, potentiating insulin.
[^ety-pramlintide]: **pramlintide** — a coined name for a stable synthetic analogue of amylin (proline-substituted; *-tide* = peptide stem), injected with meal-time insulin in type 1 and type 2 diabetes.
[^ety-c-peptide]: **C-peptide** — **C**onnecting peptide: it connects the A and B chains in proinsulin; *peptide*, Greek *peptos*, "digested" (*peptein*, to digest) → a short chain of amino acids.
[^ety-endogenous]: **endogenous** — Greek *endon*, "within" + *-genēs*, "born, produced" + *-ous* → produced inside the body. Opposite *exogenous* (injected insulin).
[^ety-equimolar]: **equimolar** — Latin *aequus*, "equal" + *moles*, "mass" (mole) + *-ar* → in equal numbers of molecules: one C-peptide for every insulin.
[^ety-somatostatin]: **somatostatin** — Greek *sōma*, "body" + *statos*, "standing still" + *-in* → first found as the inhibitor of growth (body) hormone; the δ-cell "universal inhibitor" suppresses insulin, glucagon and gut hormones.
[^ety-polypeptide]: **polypeptide** — Greek *polys*, "many" + *peptos*, "digested" → a chain of many amino acids; *pancreatic polypeptide* (36 aa) from F (PP) cells inhibits pancreatic exocrine secretion and gallbladder contraction.
[^ety-langerhans]: **islets of Langerhans** — Paul Langerhans (1847–1888), German pathologist, who described these cell clusters in 1869 as a medical student; Édouard Laguesse named them "îlots de Langerhans" (1893). Not to be confused with Langerhans cells of the skin, which he also described.
[^ety-acinar]: **acinar** — Latin *acinus*, "berry, grape" + *-ar* → the grape-like secretory sacs of exocrine glands that make digestive enzymes.
[^ety-exocrine]: **exocrine** — Greek *exō*, "outside" + *krinein*, "to separate, secrete" → secreting into a duct (pancreatic juice). **Differentiate:** *exocrine* (duct) · *endocrine* (blood) · *paracrine* (neighbouring cells — somatostatin within the islet) · *autocrine* (the cell itself).
[^ety-sanger]: **Sanger** — Frederick Sanger (1918–2013), English biochemist, who determined the complete amino-acid sequence of insulin (1951–55) — the first protein sequenced — earning the 1958 Nobel Prize in Chemistry; he won a second (1980) for DNA sequencing.
[^ety-recombinant]: **recombinant** — Latin *re-*, "again" + *com-*, "together" + *binare*, "to join in pairs" → recombined DNA; human insulin made in *E. coli* (1978, marketed 1982) was the first recombinant drug.
[^ety-hepatocyte]: **hepatocyte** — Greek *hēpar, hēpatos*, "liver" + *kytos*, "cell" → a liver cell; HNF (hepatocyte nuclear factors 1α, 4α, 1β) are transcription factors also active in β cells — their mutations cause MODY 1, 3 and 5.
[^ety-mody]: **MODY (maturity-onset diabetes of the young)** — coined by Tattersall and Fajans (1974–75): autosomal-dominant, non-ketotic diabetes in young people from single-gene β-cell defects (HNF, glucokinase).
[^ety-glut]: **GLUT** — **Glu**cose **T**ransporter: a family of facilitated-diffusion carriers. **Differentiate:** GLUT-1 (RBC, brain barrier) · GLUT-2 (β cell, liver, kidney, gut — low affinity, the glucose sensor) · GLUT-3 (neurones) · GLUT-4 (muscle, fat, heart — insulin-regulated) · GLUT-5 (fructose) · SGLT (Na⁺-glucose symporter, active).
[^ety-glucokinase]: **glucokinase** — Greek *glykys*, "sweet" + *kinein*, "to move" + *-ase*, enzyme → the enzyme that moves a phosphate onto glucose (→ glucose-6-phosphate). **Differentiate:** *glucokinase* (liver and β cell, low affinity, glucose sensor) vs *hexokinase* (other tissues, high affinity, inhibited by G6P).
[^ety-sulfonylurea]: **sulfonylurea** — *sulfonyl* (a sulphur–oxygen group; Latin *sulfur*) + *urea* (Greek *ouron*, "urine") → drugs (glibenclamide, glipizide, glimepiride) that bind SUR1 on the K-ATP channel and close it — discovered from hypoglycaemia caused by sulphonamide antibiotics (Janbon, 1942).
[^ety-depolarisation]: **depolarisation** — Latin *de-*, "removal" + *polus* (Greek *polos*, "pivot, pole") + *-isation* → loss of the resting charge difference across the membrane (inside becomes less negative). **Differentiate:** *depolarisation* (towards zero) · *repolarisation* (back to rest) · *hyperpolarisation* (more negative than rest).
[^ety-snare]: **SNARE** — **S**oluble **N**SF **A**ttachment protein **RE**ceptor (NSF = N-ethylmaleimide-sensitive factor): v-SNAREs on the granule and t-SNAREs on the membrane zip together to fuse them; Ca²⁺ (via synaptotagmin) triggers the zipping. The acronym deliberately spells *snare*, "a trap".
[^ety-exocytosis]: **exocytosis** — Greek *exō*, "outside" + *kytos*, "cell" + *-ōsis*, "process" → the process of moving granule contents out of the cell by membrane fusion. **Differentiate:** *exocytosis* (out) · *endocytosis* (in) · *phagocytosis* (cell eating) · *pinocytosis* (cell drinking).
[^ety-insulinoma]: **insulinoma** — insulin + Greek *-ōma*, "tumour" → an insulin-secreting β-cell tumour: Whipple's triad (symptoms of hypoglycaemia, low glucose, relief with glucose), high insulin and C-peptide.
[^ety-diazoxide]: **diazoxide** — *di-* "two" + *az-* (nitrogen, French *azote*, "without life") + *ox-* (oxygen) + *-ide* → a benzothiadiazine that opens K-ATP channels, hyperpolarising the β cell; used to control hypoglycaemia in insulinoma.
[^ety-secretagogue]: **secretagogue** — Latin *secretio* (*se-* "apart" + *cernere* "to sift") + Greek *agōgos*, "leading, drawing forth" → a substance that draws forth a secretion; insulin secretagogues = sulfonylureas, meglitinides.
[^ety-fanconi-bickel]: **Fanconi–Bickel syndrome** — Guido Fanconi (1892–1979), Swiss paediatrician, and Horst Bickel (1918–2000), German paediatrician, who described it in 1949: GLUT-2 deficiency with hepatorenal glycogen accumulation, a Fanconi-type proximal tubulopathy and impaired glucose sensing.
[^ety-hyperglycaemia]: **hyperglycaemia** — Greek *hyper-*, "over" + *glykys*, "sweet" + *haima*, "blood" + *-ia* → too much sugar in the blood. **Differentiate:** *hyperglycaemia* (blood) · *glycosuria* (*-uria* — sugar in urine).
[^ety-facilitated]: **facilitated diffusion** — Latin *facilis*, "easy" (*facere*, to do) + *-ate* + *dis-* "apart" + *fundere* "to pour" → diffusion made easy by a carrier: passive (down the gradient, no ATP), saturable and specific. **Differentiate:** *simple diffusion* (no carrier) · *facilitated diffusion* (carrier, passive — GLUT) · *active transport* (carrier + energy — SGLT, Na⁺-K⁺ ATPase).
[^ety-ampk]: **AMP-activated protein kinase (AMPK)** — AMP (**a**denosine **m**ono**p**hosphate, Greek *monos*, single) + *kinase* → the cell's fuel gauge: it is switched on when ATP falls and AMP rises (exercise, fasting) and inserts GLUT-4. Metformin also activates it.
[^ety-tyrosine-kinase]: **tyrosine kinase** — *tyrosine* (Greek *tyros*, "cheese") + *kinase* (Greek *kinein*, "to move" + *-ase*) → an enzyme that moves a phosphate onto tyrosine residues; the insulin receptor's β subunits phosphorylate themselves and IRS proteins.
[^ety-phosphatidylinositol]: **phosphatidylinositol-3-kinase (PI3K)** — *phosphatidyl* (phosphatidic acid, a phospholipid) + *inositol* (Greek *is, inos*, "sinew, muscle" — first isolated from muscle) + *3-kinase* (adds phosphate at position 3) → the lipid kinase that, via Akt, drives GLUT-4 translocation and insulin's metabolic actions.
[^ety-mitogen]: **mitogen** — Greek *mitos*, "thread" (the chromosome threads of mitosis) + *-gen*, "producer" → a substance that produces cell division; **MAPK** pathways carry growth signals to the nucleus.
[^ety-hyperkalaemia]: **hyperkalaemia** — Greek *hyper-*, "over" + New Latin *kalium*, "potassium" (from Arabic *al-qaly*, plant ashes) + *haima*, "blood" → high blood potassium. Insulin drives K⁺ into cells by stimulating the Na⁺-K⁺ ATPase; dextrose is given with it to prevent hypoglycaemia.
[^ety-dextrose]: **dextrose** — Latin *dexter*, "right" + *-ose*, sugar → D-glucose, so named because its solution rotates polarised light to the right (dextrorotatory).
[^ety-anabolic]: **anabolic** — Greek *ana-*, "up" + *ballein*, "to throw" + *-ic* → building up: synthesising large stores from small molecules. Opposite *catabolic* (*kata-*, down) — glucagon, cortisol, T3.
[^ety-glycogenesis]: **glycogenesis** — Greek *glykys*, "sweet" + *-gen* + *genesis*, "making" → making glycogen from glucose. **Differentiate the four:** *glycogenesis* (glucose → glycogen, ↑ by insulin) · *glycogenolysis* (glycogen → glucose, ↓ by insulin) · *glycolysis* (glucose → pyruvate, ↑) · *gluconeogenesis* (new glucose from amino acids, lactate, glycerol, ↓).
[^ety-lipogenesis]: **lipogenesis** — Greek *lipos*, "fat" + *genesis*, "making" → making fatty acids and triglycerides from glucose and acetyl-CoA. Opposite *lipolysis* (fat breakdown, which insulin inhibits through hormone-sensitive lipase).
[^ety-neoglucogenesis]: **neoglucogenesis / gluconeogenesis** — Greek *neos*, "new" + *glykys*, "sweet" + *genesis*, "making" → making new glucose from non-carbohydrate sources (amino acids, lactate, glycerol) in liver and kidney. The page's "neoglucogenesis" is the older word order of the same term.
[^ety-glycolysis]: **glycolysis** — Greek *glykys*, "sweet" + *lysis*, "loosening, splitting" → splitting glucose into two pyruvate molecules for energy (Embden–Meyerhof pathway).
[^ety-ketogenesis]: **ketogenesis** — German *Keton* (from *Aketon*, acetone) + Greek *genesis*, "making" → making ketone bodies (acetoacetate, β-hydroxybutyrate, acetone) from fatty acids in liver mitochondria — unchecked in insulin deficiency (DKA).
[^ety-streptozocin]: **streptozocin / alloxan** — *streptozocin* from *Streptomyces* (Greek *streptos*, "twisted" + *mykēs*, "fungus") + *-zocin*; *alloxan* from *allantoin* + *oxalic* acid (Wöhler and Liebig, 1838). Both enter β cells via GLUT-2 and destroy them — used to make diabetic laboratory animals.
[^ety-arginine-leucine]: **arginine / leucine** — *arginine*: Greek *argyros*, "silver" (first crystallised as a silver salt, 1886) + *-ine*; *leucine*: Greek *leukos*, "white" (white crystals) + *-ine*. Both are potent insulin secretagogue amino acids.
[^ety-autonomic]: **autonomic** — Greek *autos*, "self" + *nomos*, "law" + *-ic* → self-governing; the involuntary nervous system (term by Langley, 1898).
[^ety-vagus]: **vagus / vagal** — Latin *vagus*, "wandering" → the tenth cranial nerve wanders from the brainstem to the abdomen; its acetylcholine (muscarinic M3) stimulates insulin release in the cephalic phase of eating.
[^ety-acetylcholine]: **acetylcholine** — Latin *acetum*, "vinegar" (acetyl group) + Greek *cholē*, "bile" (choline was first found in bile) + *-ine* → the parasympathetic transmitter.
[^ety-sympathetic]: **sympathetic / parasympathetic** — Greek *syn-* (*sym-* before *p*), "together" + *pathos*, "feeling" → organs "feeling together" (Galen); *para-*, "beside" → the system beside the sympathetic.
[^ety-gastrin]: **gastrin** — Greek *gastēr, gastros*, "stomach" + *-in* → the hormone of the gastric antrum (G cells) that drives acid secretion; named by Edkins (1905).
[^ety-cck]: **CCK (cholecystokinin)** — Greek *cholē*, "bile" + *kystis*, "bladder" + *kinein*, "to move" → the hormone that moves the gallbladder (contracts it); from duodenal I cells.
[^ety-secretin]: **secretin** — Latin *secretio*, "separation" + *-in* → the first hormone ever discovered (Bayliss and Starling, 1902), which stimulates pancreatic bicarbonate secretion; it gave rise to the word *hormone* (1905).
[^ety-incretin]: **incretin** — **In**testinal se**cret**ion of **In**sulin (La Barre, 1932) → gut hormones released by oral nutrients that augment glucose-dependent insulin secretion: GLP-1 (L cells) and GIP (K cells).
[^ety-insulinotropic]: **insulinotropic** — insulin + Greek *tropos*, "a turning" + *-ic* → turning on insulin; GIP was first called *gastric inhibitory polypeptide*, later renamed *glucose-dependent insulinotropic polypeptide* for its main role.
[^ety-dpp4]: **DPP-4 (dipeptidyl peptidase 4)** — Greek *di-*, "two" + *peptide* + *-yl* + *peptidase* (*-ase*, enzyme) → an enzyme that clips two amino acids (a dipeptide) off the N-terminus of GLP-1 and GIP, inactivating them within ~2 minutes.
[^ety-exenatide]: **exenatide** — from **exendin-4**, a peptide found in the saliva of the Gila monster (*Heloderma suspectum*), + *-tide* (peptide stem) → a DPP-4-resistant GLP-1 receptor agonist (Eng, 1992).
[^ety-gliptin]: **gliptins (sitagliptin)** — the WHO stem **-gliptin** for DPP-4 inhibitors (from *gl*ucose + d*ip*eptidyl pep*t*idase *in*hibitor); sitagliptin (2006) was the first.
[^ety-homeostasis]: **homeostasis** — Greek *homoios*, "similar" + *stasis*, "standing still" → staying similar; glucose homeostasis is held between ~70 and 140 mg/dL by insulin against the counter-regulatory hormones.
[^ety-counter-regulatory]: **counter-regulatory** — Latin *contra*, "against" (French *contre*) + *regula*, "rule" + *-ory* → hormones that act against insulin to raise glucose: glucagon, epinephrine (fast), cortisol, GH (slow), T3.
[^ety-coma]: **coma** — Greek *kōma*, "deep sleep" → a state of unrousable unresponsiveness; the brain depends almost entirely on glucose, so severe hypoglycaemia causes coma. Not related to *comma* (punctuation, Greek *komma*, "a piece cut off").
[^ety-dawn]: **dawn phenomenon** — Old English *dagian*, "to become day" + Greek *phainomenon*, "that which appears" → an early-morning (≈ 4–8 a.m.) rise in glucose from the nocturnal surge of GH (and cortisol). **Differentiate** from the *Somogyi effect* — rebound hyperglycaemia after nocturnal hypoglycaemia.
[^ety-cortisol]: **cortisol** — Latin *cortex*, "bark" (adrenal cortex) + *-ol* (alcohol) → the main glucocorticoid; raises glucose by gluconeogenesis and insulin antagonism.
[^ety-epinephrine]: **epinephrine / adrenaline** — Greek *epi-*, "upon" + *nephros*, "kidney" + *-ine*; Latin *ad-*, "near" + *ren*, "kidney" → the hormone of the gland upon the kidney (adrenal medulla); fastest counter-regulatory hormone (glycogenolysis, ↓ insulin via α₂).
[^pre-pan]: **pan- / panto-** — all, every: pancreas (all flesh), pandemic, pancytopenia. Don't confuse with **pen- / pene-** almost (peninsula) · **para-** beside.
[^pre-endo]: **endo-** — within: endocrine, endogenous, endocytosis. Don't confuse with **exo-** outside (exocrine, exocytosis) · **ecto-** outer · **epi-** upon.
[^pre-equi]: **equi-** — equal: equimolar, equilibrium, equivalent. Don't confuse with **equine** of a horse (Latin *equus*) · **iso-** equal (Greek synonym: isotonic).
[^pre-poly]: **poly-** — many: polypeptide, polyuria, polydipsia, polyphagia. Don't confuse with **mono-** one · **oligo-** few · **pleo-** more.
[^pre-exo]: **exo-** — outside, outward: exocrine, exocytosis, exogenous. Don't confuse with **ex- / ec-** out of (Latin/Greek: excretion, ectopic) · **extra-** beyond · **endo-** within.
[^suf-cyte]: **-cyte** — cell: hepatocyte, adipocyte, lymphocyte. Don't confuse with **-blast** immature cell · **-cytosis** an increase in cells or a cell process (exocytosis — see *-osis*).
[^suf-ase]: **-ase** — an enzyme: glucokinase, peptidase, kinase, lipase. Don't confuse with **-ose** a sugar (glucose, dextrose) · **-ate** a salt (pyruvate).
[^pre-de]: **de-** — removal, reversal: depolarisation, degradation, dehydration. Don't confuse with **di- / dis-** two, apart · **dia-** through.
[^suf-osis]: **-osis** — a process or condition: exocytosis, ketosis, glycogenosis. Don't confuse with **-itis** inflammation (pancreatitis) · **-oma** tumour (insulinoma).
[^suf-oma]: **-oma** — tumour, swelling: insulinoma, adenoma, glucagonoma, somatostatinoma. Don't confuse with **-osis** a condition · **coma** (a whole Greek word, deep sleep — not this suffix).
[^pre-hyper]: **hyper-** — over, excessive: hyperglycaemia, hyperkalaemia, hyperinsulinaemia. Don't confuse with **hypo-** under · **supra- / super-** (Latin equivalents).
[^suf-aemia]: **-aemia / -emia** — a state of the blood: hyperglycaemia, hypoglycaemia, hyperkalaemia. Don't confuse with **-uria** a state of the urine (glycosuria).
[^pre-ana]: **ana-** — up, upward, again: anabolic (building up), anaphase. Don't confuse with **an- / a-** without (anuria) · **ante-** before · **anti-** against.
[^suf-genesis]: **-genesis** — making, origin: glycogenesis, lipogenesis, ketogenesis, gluconeogenesis. Don't confuse with **-genic** producing (adjective: diabetogenic) · **-lysis** breaking down (the opposite process).
[^pre-glyco]: **glyco- / gluco-** — sweet, sugar (Greek *glykys*): glycogen, glycolysis, glucagon, glucokinase. Don't confuse with **glyc-** in *glycerol* (sweet alcohol — same root) · **gluteo-** buttock · **glia** glue.
[^suf-lysis]: **-lysis / -lytic** — breaking down: glycogenolysis, lipolysis, glycolysis. Don't confuse with **-genesis** making (the opposite) · **-lithiasis** stones.
[^pre-lipo]: **lipo-** — fat (Greek *lipos*): lipogenesis, lipolysis, lipoprotein. Don't confuse with **lipo-** in *lipothymia* (*leipein*, to fail) · **litho-** stone.
[^pre-neo]: **neo-** — new: neoglucogenesis, neonatal, neoplasm. Don't confuse with **nephro-** kidney · **neuro-** nerve.
[^pre-auto]: **auto-** — self: autonomic, autocrine, autoimmune. Don't confuse with **oto-** ear · **auxo-** growth.
[^pre-para]: **para-** — beside, alongside: parasympathetic, paracrine. Don't confuse with **peri-** around · **pre-** before.
[^pre-syn]: **syn- / sym- (before b, p, m)** — together, with: sympathetic, synapse, syndrome. Don't confuse with **anti-** against · **sin-** (Latin *sinister*, left).
[^pre-hypo]: **hypo-** — under, deficient: hypoglycaemia, hypoglycaemic hormone, hypokalaemia. Don't confuse with **hyper-** over · **hypno-** sleep.
[^pre-di]: **di-** — two, twice (Greek *dis*): dipeptidyl, disaccharide, diazoxide. Don't confuse with **dia-** through (diabetes) · **dis-** apart (Latin) · **dys-** bad.
[^pre-counter]: **counter-** — against, opposite (French *contre*, Latin *contra*): counter-regulatory, countercurrent. Don't confuse with **contra-** (the Latin form: contraindication) · **con-** together.
[^pre-epi]: **epi-** — upon, over: epinephrine (upon the kidney), epithelium, epigastric. Don't confuse with **hypo-** under · **para-** beside · **peri-** around.
