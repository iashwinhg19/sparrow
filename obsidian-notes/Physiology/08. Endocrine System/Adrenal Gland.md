---
title: Adrenal Gland
aliases: [Adrenal Gland, Suprarenal gland, Adrenal cortex and medulla, Aldosterone and cortisol]
rank: 56
status: not-started
topic: Physiology
subtopic: Endocrine System
chapter: 56
pages: "239–244"
target_exams:
  - NEET PG
  - INI-CET
  - FMGE
past_exam_questions: []
anki_link: ""
case_files: []
difficulty: hard
high_yield: true
guideline_criteria: ""
source: "Physiology main notes (Marrow 8) — Adrenal Gland, pp. 239–244 (sections: Anatomy 00:00:56 · Physiology 00:05:05 · Adrenocortical Hormones 00:16:05)"
mindmap: "[[Adrenal Gland — Mind Map]]"
index: "[[Physiology — Index]]"
review_day_2: false
review_day_4: false
review_day_7: false
review_day_10: false
review_day_15: false
---
# 🎩 Adrenal Gland

> [!abstract] Core Definition
> The **adrenal**[^ety-adrenal][^pre-ad] gland is a hat-shaped endocrine gland on the upper pole of each kidney, built as two glands in one: an outer **cortex**[^ety-cortex] that makes **steroid**[^ety-steroid][^suf-oid] hormones[^ety-hormone] from cholesterol, and an inner **medulla**[^ety-medulla] that makes **catecholamines**[^ety-catecholamine]. Everything in the chapter answers three questions:
> - ✅ **Which zone makes which hormone** — and which enzyme does it need (the synthesis[^ety-synthesis][^pre-syn] map)?
> - ✅ **Who controls it** — ACTH (HPA axis) for the cortex, but **not** for the medulla; K⁺ for aldosterone.
> - ✅ **What happens with too much or too little** — Conn's, Cushing's, Addison's, SAME, CAH / adrenogenital syndrome.

---

## 🧠 Mental Model — A Three-Storey Factory with a Basement

Picture the gland as a factory. Every storey of the cortex gets the same raw material (cholesterol), but each storey owns a different set of machines (enzymes), so each turns out a different product — **salt, sugar, sex** as you go deeper. The basement (medulla) is a separate nerve-run plant making adrenaline.

```
CAPSULE (connective tissue)
ZONA GLOMERULOSA  → SALT  → aldosterone (mineralocorticoid)        ← K⁺ (and ACTH only transiently)
ZONA FASCICULATA  → SUGAR → cortisol (glucocorticoid)  — 50 %      ← ACTH (HPA axis, –ve feedback)
ZONA RETICULARIS  → SEX   → DHEA, DHEAS, androstenedione           ← ACTH
──────────────────────────────────────────────────────────────────────────────
MEDULLA           → FIGHT → epinephrine, norepinephrine, dopamine  ← sympathetic nerves — NOT ACTH
Memory: "GFR" (outside → in) = Salt, Sugar, Sex — "the deeper you go, the sweeter it gets"
```

---

## 🔬 Anatomy

**Gross anatomy:** the adrenal gland sits on the **superior surface of the kidney**; it has an outer **cortex (78 %)** and an inner **medulla (22 %)**.[^1]

**Histopathology** — from outside in, the layers and what each produces:

| Layer | Produces | Note on the page |
|---|---|---|
| **Connective tissue capsule** | — | Outer covering |
| **Zona glomerulosa**[^ety-zona][^ety-glomerulosa][^suf-ule] | **Aldosterone**[^ety-aldosterone][^suf-one] (**mineralocorticoid**[^ety-corticoid]) | **Contains stem cells for regeneration**[^ety-regeneration][^pre-re] of cortical cells |
| **Zona fasciculata (50 %)**[^ety-fasciculata] | **Cortisol**[^ety-cortisol][^suf-ol] (**glucocorticoid**[^pre-gluco]) | The widest zone[^2] |
| **Zona reticularis**[^ety-reticularis] | **Adrenal sex steroids** | — |
| **Medulla** | **Catecholamines:** epinephrine[^ety-epinephrine][^pre-epi], norepinephrine[^pre-nor], dopamine[^ety-dopamine] | Separated from the cortex by the dashed line on the page |

![The adrenal glands — gland on the kidney, cortex with its three zones and the medulla, with a micrograph (OpenStax)](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/1818_The_Adrenal_Glands.jpg/800px-1818_The_Adrenal_Glands.jpg)
*The adrenal gland on the superior surface of the kidney; the capsule, zona glomerulosa, zona fasciculata, zona reticularis and medulla with the hormones each makes — the same gross-anatomy + histology pair as the page's figure (OpenStax Anatomy & Physiology, Fig. 17.17, CC BY 4.0).*

Rotate it in 3D — the glands cap the upper poles of the kidneys, the right one tucked behind the inferior vena cava:

```anatomed
# adrenal glands — retype a name with the plugin's autocomplete if it shows as "unmatched"
parts: right suprarenal gland, left suprarenal gland, right kidney, left kidney, inferior vena cava, abdominal aorta, left renal vein
detail: related
title: Adrenal (suprarenal) glands on the kidneys
```

---

## ⚗️ Physiology

### Steroid hormone synthesis

All three zones start from **cholesterol (precursor)**[^ety-cholesterol][^pre-chole]. Which hormone a zone ends with depends only on which **enzymes**[^ety-enzyme] it carries — that is why a missing enzyme diverts the whole flow into the other columns. The **zona fasciculata** column is shaded green on the page (the cortisol pathway — the most tested).

```
ZONA GLOMERULOSA                 ZONA FASCICULATA                 ZONA RETICULARIS
                                                                  Source of DHEA: adrenal cortex (90 %) · ovary (10 %)
Cholesterol (precursor)
   │ Desmolase
   ↓        17-α hydroxylase                      17,20 lyase                             Sulfotransferase
Pregnenolone ──────────────────→ 17-OH pregnenolone ────────────→ Dehydroepiandrosterone ─────────────────→ DHEAS
   │ 3β HSD                         │ 3β HSD                         │ 3β HSD                  (present exclusively
   ↓        17-α hydroxylase        ↓                                ↓                          in adrenal cortex)
Progesterone ──────────────────→ 17-OH progesterone               Androstenedione
   │ 21-hydroxylase                 │ 21-hydroxylase                 │ peripheral tissues
   ↓                                ↓                                ↓
11-Deoxycorticosterone           11-Deoxycortisol                 Testosterone ── Aromatase ──→ Estrogen
(weak mineralocorticoid)            │ 11-β hydroxylase
   │ 11-β hydroxylase               ↓
   ↓                             CORTISOL (glucocorticoid)
Corticosterone (weak glucocorticoid)
   │ Aldosterone synthetase
   ↓
ALDOSTERONE (mineralocorticoid)
```

The enzymes, in the order the page uses them:

| Step | Enzyme | Zone (column) on the page |
|---|---|---|
| Cholesterol → pregnenolone | **Desmolase**[^ety-desmolase][^suf-ase][^3] | All zones (first step) |
| Pregnenolone → progesterone · 17-OH pregnenolone → 17-OH progesterone · DHEA → androstenedione | **3β hydroxy steroid dehydrogenase (3β HSD)**[^ety-dehydrogenase][^pre-de] | All three columns |
| Pregnenolone / progesterone → 17-OH forms | **17-α hydroxylase**[^ety-hydroxylase] | Glomerulosa → fasciculata (the entry to the cortisol column) |
| Progesterone → 11-deoxycorticosterone · 17-OH progesterone → 11-deoxycortisol | **21-hydroxylase** | Glomerulosa and **fasciculata** |
| 11-deoxycorticosterone → corticosterone · 11-deoxycortisol → cortisol | **11-β hydroxylase** | Glomerulosa and **fasciculata** |
| Corticosterone → aldosterone | **Aldosterone synthetase**[^4] | Glomerulosa only |
| 17-OH pregnenolone → dehydroepiandrosterone[^ety-dhea] | **17,20 lyase**[^ety-lyase] | Reticularis |
| DHEA → **DHEAS** | **Sulfotransferase**[^ety-sulfotransferase][^pre-trans] | Reticularis — DHEAS is present **exclusively in adrenal cortex** |
| Androstenedione[^ety-androstenedione] → testosterone[^ety-testosterone] | (in **peripheral tissues**)[^pre-peri] | Reticularis |
| Testosterone → estrogen[^ety-estrogen][^suf-gen] | **Aromatase**[^ety-aromatase] | — |

- **Deficiency of enzymes involved → Congenital**[^ety-congenital][^pre-con] **adrenal hyperplasia**[^ety-hyperplasia][^pre-hyper][^suf-plasia].[^5]
- **Note:** major source of testosterone → **testis**.[^6]

![Human steroidogenesis — enzymes, cellular locations, substrates and products of every steroid class](https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Steroidogenesis.svg/800px-Steroidogenesis.svg.png)
*The full steroidogenesis map — cholesterol → pregnenolone → the mineralocorticoid, glucocorticoid and androgen/estrogen columns with every enzyme named; it matches the page's three columns and adds the gonadal steps (Häggström M & Richfield D, WikiJournal of Medicine 2014; Wikimedia Commons, CC0).*

### Regulation of hormone synthesis — Hypothalamic–pituitary–adrenal (HPA axis)

The **hypothalamus**[^ety-hypothalamus][^pre-hypo] releases **corticotropin-releasing hormone (CRH)**[^ety-corticotropin][^suf-tropic], the **anterior pituitary**[^ety-pituitary] answers with **adrenocorticotropic hormone (ACTH)**, and ACTH drives the adrenal cortex. Cortisol then switches the top two off — **negative feedback**[^ety-feedback].

```
     ┌──(–)──────────────── Hypothalamus
     │                           │ Corticotropin-releasing hormone (CRH)
     │                           ↓
     ├──(–)──────────────── Anterior pituitary
     │                           │ Adrenocorticotropic hormone (ACTH)
     │  Negative feedback        ↓
     │                      Adrenal cortex
     │            ┌──────────────┼───────────────────┐
     │            ↓              ↓                   ↓
     └─────── Cortisol      Aldosterone      Adrenal sex steroids
```

> [!warning] Note: **Adrenal medulla is not under ACTH control.**
> The medulla is a modified sympathetic ganglion — it is switched on by nerves, not by the pituitary.[^7]

![The HPA axis — hypothalamus → CRH → anterior pituitary → ACTH → adrenal cortex → cortisol, with cortisol's negative feedback](https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/HPA_Axis_Diagram_(Brian_M_Sweis_2012).png/800px-HPA_Axis_Diagram_(Brian_M_Sweis_2012).png)
*The hypothalamic–pituitary–adrenal axis with its negative feedback loops — the same chain as the page's flowchart (Brian M. Sweis 2012, Wikimedia Commons — free licence, see file page).*

🎬 **Watch:** [Adrenal Cortex: Synthesis and Secretion](https://www.youtube.com/watch?v=lq_s0bgC5L4) · [Anatomy and Physiology of the Adrenal Glands, Animation](https://www.youtube.com/watch?v=-d-9gRgz9pY) · [HPA axis explained (YouTube search)](https://www.youtube.com/results?search_query=HPA+axis+CRH+ACTH+cortisol+physiology)

![](https://www.youtube.com/watch?v=-d-9gRgz9pY)

---

## 💊 Adrenocortical Hormones

### 🧂 Aldosterone

- **Steroid hormone (life saving).**[^8]
- **60 %:** present in **bound form** with binding proteins.
- **t½: 20 mins.**

#### Mechanism of action

**Kidneys:** in the **collecting duct**[^ety-duct] of the **nephron**[^ety-nephron] aldosterone acts on two cells:

**1. Site: principal cell**[^ety-principal]
- Aldosterone enters the cell and binds the **inactive**[^pre-in] **MR (mineralocorticoid receptor)**[^ety-receptor] → **active form** → enters the nucleus → makes **proteins**[^ety-protein].
- These proteins **insert / activate** three transporters:
  - **ENaC** (luminal) — Na⁺ enters from the lumen; **H₂O** follows.
  - **ROMK** (luminal) — K⁺ is secreted into the lumen.
  - **Na⁺–K⁺ ATPase** (basolateral) — pumps Na⁺ out into blood and K⁺ into the cell.
- **Spironolactone**[^ety-spironolactone] blocks the **MR**; **Amiloride**[^ety-amiloride] blocks **ENaC**.[^9]

**2. Type A intercalated cell**[^ety-intercalated][^pre-inter] (written in orange on the page)
- CO₂ + H₂O → H₂CO₃ → HCO₃⁻ + H⁺.
- **H⁺** is pumped into the lumen by the **H⁺ ATPase** and the **H⁺–K⁺ ATPase** — aldosterone **stimulates (+)** the H⁺–K⁺ ATPase; K⁺ is taken back in exchange.
- **HCO₃⁻** leaves to the blood through the **Cl⁻–HCO₃⁻ exchanger**; Cl⁻ recycles through a Cl⁻ channel.[^10]

| Abbreviation | Stands for |
|---|---|
| **ENaC** | **Epithelial**[^ety-epithelial] **Na⁺ channel** |
| **ROMK** | **Renal Outer Medullary (K⁺) Channel** |
| **MR** | **Mineralocorticoid Receptor** |

![[Adrenal Gland - aldosterone action on principal and type A intercalated cells.png]]
*Aldosterone in the collecting duct — principal cell (MR → proteins → ENaC, ROMK, Na⁺–K⁺ ATPase; spironolactone blocks MR, amiloride blocks ENaC) and type A intercalated cell (H⁺ ATPase, H⁺–K⁺ ATPase stimulated by aldosterone, Cl⁻–HCO₃⁻ exchanger) (cropped from the handwritten page).*

**MR sites:** kidneys, colon, **hippocampus**[^ety-hippocampus], salivary glands, sweat glands.[^11]

#### Factors regulating aldosterone synthesis

- **Hyperkalemia**[^ety-hyperkalemia][^suf-emia] → **stimulates aldosterone release.**
- **ACTH → ↑ aldosterone transiently.**[^12]

#### Disorders

##### ⬆️ Hyperaldosteronism[^ety-hyperaldosteronism][^suf-ism]

**1. Conn's syndrome**[^ety-conn][^ety-syndrome]
- **Etiology**[^ety-etiology]**:** aldosterone producing **adrenal adenomas**[^ety-adenoma][^suf-oma].
- **Clinical features:**
  - a. **Metabolic**[^ety-metabolic] **alkalosis**[^ety-alkalosis][^suf-osis].
  - b. **Hypokalemia**[^ety-hypokalemia] →
    - muscle cramps
    - interstitial **atony**[^ety-atony][^pre-a][^13]
    - **nephropathy**[^ety-nephropathy][^suf-pathy]
  - c. **Hypertension**[^ety-hypertension]**:** Na⁺ & H₂O **retention**[^ety-retention] → ↑ ECF → ↑ BP **but no edema**[^ety-edema].

**Aldosterone escape**[^ety-escape] — why Conn's has hypertension but no edema:

```
Pressure diuresis (d/t ↑ BP)        Atrial natriuretic peptide: natriuresis
            └───────────────────┬───────────────────┘
                                ↓
        Na⁺ & H₂O excretion (in spite of ↑ aldosterone)
                                ↓
                            No edema
```

**Pressure diuresis**[^ety-diuresis][^pre-dia] and the **atrial natriuretic peptide**[^ety-natriuretic][^ety-peptide] both push Na⁺ and water out in the urine (**natriuresis**[^suf-uresis]), so the ECF stops expanding once the BP has risen.[^14]

**2. Glucocorticoid remediable hyperaldosteronism**[^ety-remediable]
- **Pathophysiology:**
  - **Aldosterone synthase + 11 β-hydroxylase → hybrid enzyme**[^ety-hybrid].
  - **↑ ACTH → sustained release of aldosterone** (d/t hybrid enzyme).
- **Treatment: Dexamethasone**[^ety-dexamethasone] (inhibits ACTH).[^15]

```
Aldosterone synthase  +  11 β-hydroxylase
          └──────────┬──────────┘
               Hybrid enzyme
                     ↓
↑ ACTH → sustained release of aldosterone (d/t hybrid enzyme)
                     ↓
Dexamethasone suppresses ACTH → aldosterone falls (glucocorticoid "remedies" it)
```

##### ⬇️ Hypoaldosteronism

**1. Addison's disease**[^ety-addison] **(adrenal insufficiency**[^ety-insufficiency]**)**
- **Features:**
  - a. **Hyponatremia**[^ety-hyponatremia]
  - b. **Postural hypotension**[^ety-hypotension]
  - c. **Hyperkalemia**
  - d. **Microcardia**[^ety-microcardia][^pre-micro][^suf-cardia][^16]

### 🍬 Cortisol

- **90–95 % bound** to **cortisol binding globulin (CBG)**[^ety-globulin] / **transcortin**[^ety-transcortin].
- **t½: 60–90 mins.**[^17]

#### Mechanism of action — Glucocorticoid receptor (GR)

Cortisol diffuses into the cell and binds the **inactive GR** in the **cytoplasm**[^ety-cytoplasm][^pre-cyto]; the **active GR** moves into the **nucleus**[^ety-nucleus], sits on DNA as a pair and switches genes on (**transcription**[^ety-transcription]).[^18]

```
Inactive GR ──→ [GR] + cortisol ──→ Active GR (cytoplasm)
                                         ↓
                              Nucleus: GR–GR on DNA → gene transcription
```

![[Adrenal Gland - glucocorticoid receptor mechanism.png]]
*Glucocorticoid receptor — inactive GR in the cytoplasm binds cortisol, becomes active GR and enters the nucleus to bind DNA (cropped from the handwritten page).*

#### Functions

| System | **Physiological** (normal cortisol) | **Pathological: Cushing's syndrome**[^ety-cushing] (cortisol excess) |
|---|---|---|
| **1. Protein metabolism** | **Muscle:** proteolysis[^ety-proteolysis][^suf-lysis] → **alanine** (**catabolic**[^ety-catabolic][^pre-cata]) · **Liver:** synthesis of plasma proteins (**anabolic**[^pre-ana]) | Muscle weakness · **proximal myopathy**[^ety-myopathy] (**steroid myopathy**) |
| **2. Carbohydrate metabolism** | **Gluconeogenesis**[^ety-gluconeogenesis][^pre-neo][^suf-genesis] → **hyperglycemia**[^ety-hyperglycemia] (alanine → glucose) | Glucose intolerance · **diabetes mellitus**[^ety-diabetes] (**adrenal diabetes**) |
| **3. Lipid metabolism** | **Lipolysis**[^pre-lipo] → ↑ free fatty acids | **Dyslipidemia**[^ety-dyslipidemia][^pre-dys] · **Buffalo hump** · **Moon face**[^19] |
| **4. Immune system** | **Universal anti-inflammatory**[^ety-inflammation][^pre-anti] **agent** — inhibits **leukotrienes**[^ety-leukotriene][^pre-leuko] and **phospholipase A₂**[^ety-phospholipase][^20] | ↑ susceptibility to infections |
| **5. Blood cells** | **↓:** **eosinophils**[^ety-eosinophil][^suf-phil], basophils[^ety-basophil] & lymphocytes[^ety-lymphocyte][^suf-cyte] · **↑:** RBCs, neutrophils[^ety-neutrophil] & **platelets** | **Eosinopenia**[^ety-eosinopenia][^suf-penia] · **Hypercoagulable**[^ety-coagulable] **state**[^21] |
| **6. Nervous system** | ↑ appetite → weight gain · alters mood & behavior | Irritability · **psychosis**[^ety-psychosis] |
| **7. Heart** | ↑ cardiac output · ↑ vascular tone | **Hypertension** · **atherosclerosis**[^ety-atherosclerosis] |
| **8. Kidney** | ↑ GFR · ↑ Ca²⁺ excretion[^ety-excretion][^pre-ex] | **Hypercalciuria**[^ety-hypercalciuria][^suf-uria] → renal stones[^22] |
| **9. Bone & connective tissues** | **Inhibits:** fibroblast[^ety-fibroblast][^suf-blast] proliferation[^ety-proliferation], collagen[^ety-collagen] formation · **Promotes:** bone resorption[^ety-resorption] | Thin skin · bruising / **ecchymosis**[^ety-ecchymosis] · **hypertension** · pendulous abdomen · **purple striae**[^ety-striae] · osteoporosis[^ety-osteoporosis][^pre-osteo] · thin arms and legs[^23] |
| **10. GIT** | ↑ gastric acid production | **Peptic ulcer**[^ety-peptic] |
| **11. Reproduction** | **Inhibits GnRH** (negative regulator of reproduction) | **Amenorrhea**[^ety-amenorrhea][^suf-rrhoea] · loss of **libido**[^ety-libido] · **infertility** |

![Main symptoms of Cushing's syndrome — moon face, buffalo hump, central obesity, thin skin, purple striae, bruising, muscle weakness, osteoporosis, hypertension](https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Cushing's_syndrome.png/800px-Cushing's_syndrome.png)
*Cushing's syndrome — the features drawn in the page's two figures (buffalo hump and moon face; thin skin, ecchymosis, hypertension, pendulous abdomen, purple striae, osteoporosis, thin arms and legs) on one body map (Mikael Häggström, Wikimedia Commons — free licence).*

**12. Effect on catecholamines**

```
Catecholamines ──(in presence of cortisol)──→ Enhanced actions:  • Lipolysis
                                                                 • Bronchodilation
```

Cortisol does not cause these effects itself — it lets adrenaline and noradrenaline work at full strength (**permissive**[^ety-permissive] action); **bronchodilation**[^ety-bronchodilation] is one reason steroids help in asthma.[^24]

#### Other diseases

**Addison's disease — cortisol deficiency** →
1. **Hypoglycemia**[^ety-hypoglycemia]
2. **Fatigue**
3. **Eosinophilia**[^ety-eosinophilia][^suf-philia]
4. **Lymphocytosis**[^ety-lymphocytosis]

Each is the mirror image of the functions table: no gluconeogenesis → low sugar; no eosinophil and lymphocyte suppression → both rise.

#### Syndrome of apparent mineralocorticoid excess (SAME)

| Normal physiology | Pathology |
|---|---|
| **Cortisol** has **↑ affinity to MR** — if it reached the MR it would cause **↑ mineralocorticoid action** | **Licorice**[^ety-licorice] **consumption** → **glycyrrhetinic acid**[^ety-glycyrrhetinic] |
| **11 β-HSD type 2** converts cortisol → **inactive cortisol**, which cannot bind the MR (the crossed arrow) | Glycyrrhetinic acid **blocks 11 β-HSD type 2** (the red cross) → cortisol is not inactivated |
| MR is left free for aldosterone | **Cortisol binds the MR** → cortisol–MR complex → mineralocorticoid excess (looks like ↑ aldosterone, but aldosterone itself is low)[^25] |

![[Adrenal Gland - syndrome of apparent mineralocorticoid excess.png]]
*SAME — normally 11 β-HSD type 2 inactivates cortisol so it cannot reach the MR; licorice (glycyrrhetinic acid) blocks the enzyme, and cortisol occupies the MR (cropped from the handwritten page).*

### 🧔 Sex steroids

**Hormones:**
1. **Dehydroepiandrosterone (DHEA).**
2. **DHEA sulfate (DHEAS): most circulating hormone in humans.**[^26]
3. **Androstenedione.**
4. **Testosterone (small amounts).**

**Functions:** axillary hair growth · pubic hair growth · libido.[^27]

**Disorders:**

| Causes | Result |
|---|---|
| 1. Adrenocortical tumors · 2. Congenital adrenal hyperplasia · 3. Adrenogenital[^ety-adrenogenital] syndrome | **↑ adrenal androgens**[^ety-androgen] |

**Adrenogenital syndrome — clinical features:**

```
                      Clinical features
              ┌──────────────┴──────────────┐
              ↓                             ↓
     Females (more severe)        Males (prepubertal time)
              ↓                             ↓
   Pseudohermaphroditism:          Rapid development of
   • Beard growth                  male sex organs
   • Deep voice
   • Baldness
   • Hirsutism
   • Clitoromegaly
```

- **Females (more severe) → pseudohermaphroditism**[^ety-pseudohermaphroditism][^pre-pseudo]**:** beard growth · deep voice · baldness · **hirsutism**[^ety-hirsutism] · **clitoromegaly**[^ety-clitoromegaly][^suf-megaly].
- **Males (prepubertal time) → rapid development of male sex organs.**[^28]

---

## Core Dictum & Pattern Recognition

> [!check]+ **🎯 Core Dictum - The Unifying Principle**
>
> The adrenal cortex is one assembly line (cholesterol → pregnenolone → …) split into three columns by **which enzymes each zone owns**: the glomerulosa alone has aldosterone synthase (salt), the fasciculata has 17α-hydroxylase + 21- + 11β-hydroxylase (sugar), the reticularis has 17,20 lyase (sex). So every enzyme block (CAH) is predictable: whatever is upstream of the block piles up and spills into the column that is still open — usually androgens — and the low cortisol removes negative feedback, so ACTH rises and the gland becomes hyperplastic.
>
> The second principle is **receptor sharing**: cortisol binds the MR as avidly as aldosterone, and only the enzyme 11β-HSD2 keeps it out. Block that guard (licorice) and cortisol becomes a mineralocorticoid; express aldosterone synthase under ACTH control (GRA) and a glucocorticoid drug cures hypertension.

> [!example]+ **📊 Clinical Pattern Recognition**
>
> Understanding how the condition progresses through stages helps you recognize it at different phases and predict outcomes.
>
> **Stage 1 - Normal Physiology:**
> CRH → ACTH → cortisol, with cortisol feeding back on the hypothalamus and pituitary; aldosterone follows K⁺ (and angiotensin II), acting on the principal cell (Na⁺ in, K⁺ out) and the type A intercalated cell (H⁺ out). DHEAS circulates in the highest concentration of any hormone; the medulla answers only to sympathetic nerves.
>
> **Stage 2 - Compensated/Early Pathology:**
> An aldosterone-producing adenoma retains Na⁺ and water, but within days pressure diuresis and ANP produce "aldosterone escape": BP rises while the ECF stops expanding, so there is hypertension without edema, and K⁺ and H⁺ keep leaking out (mild hypokalemia, metabolic alkalosis). Early cortisol excess shows first as glucose intolerance, weight gain and eosinopenia.
>
> **Stage 3 - Decompensated/Overt Disease:**
> Conn's: severe hypokalemia → muscle cramps, atony, hypokalemic nephropathy. Cushing's: moon face, buffalo hump, purple striae, proximal myopathy, adrenal diabetes, osteoporosis, renal stones, infections, psychosis. Addison's: hyponatremia, hyperkalemia, postural hypotension with a small heart (microcardia), hypoglycemia, eosinophilia and lymphocytosis — an adrenal crisis can kill (aldosterone is "life saving").
>
> **Progression Timeline:**
> Normal → hormone excess or deficiency (adenoma / exogenous steroid / autoimmune destruction / enzyme block) → biochemical change (K⁺, Na⁺, glucose, eosinophils) → compensation (aldosterone escape, ↑ ACTH) → decompensation → full clinical syndrome (Conn's, Cushing's, Addison's, CAH)
>
> **Why This Matters Clinically:**
> The stage decides the test and the drug: spironolactone blocks the MR in Conn's (and in SAME, where aldosterone is low), dexamethasone suppresses ACTH in GRA and CAH, and Addison's needs both glucocorticoid and mineralocorticoid replacement. Missing an evolving Addison's turns a hyperkalemic, hypotensive patient into a crisis.

> [!warning]+ **🔍 Diagnostic Buzzwords & Pattern Recognition**
>
> These are the key terms, phrases, and clinical patterns that should immediately trigger specific diagnoses in your mind. When you see these in a clinical vignette or real patient, you should think of the associated condition instantly.
>
> **Buzzwords by Condition:**
>
> **Conn's syndrome:** "Hypertension with hypokalemia and metabolic alkalosis, no edema" → An aldosterone-producing adenoma drives ENaC (Na⁺ in), ROMK (K⁺ out) and the H⁺ pumps (H⁺ out); escape via pressure diuresis and ANP prevents edema.
>
> **Glucocorticoid remediable hyperaldosteronism:** "Familial hypertension cured by dexamethasone", "hybrid enzyme" → aldosterone synthase is driven by ACTH, so suppressing ACTH lowers aldosterone.
>
> **Cushing's syndrome:** "Moon face, buffalo hump, purple striae, proximal myopathy, eosinopenia, hypercoagulable" → cortisol excess acting on every row of the functions table.
>
> **Addison's disease:** "Hyponatremia, hyperkalemia, postural hypotension, microcardia, hypoglycemia, eosinophilia" → loss of both aldosterone and cortisol.
>
> **SAME:** "Hypertension and hypokalemia after eating licorice, with low aldosterone" → glycyrrhetinic acid blocks 11β-HSD2; cortisol occupies the MR.
>
> **Adrenogenital syndrome / CAH:** "Clitoromegaly, hirsutism, deep voice in a girl", "rapid development of male sex organs in a prepubertal boy" → enzyme block diverts precursors to androgens; ACTH drives hyperplasia.
>
> **Visual/Imaging Buzzwords:**
> Buffalo hump + moon face + pendulous abdomen with purple striae and thin limbs = Cushing's habitus; a small heart on chest X-ray in a hypotensive patient = microcardia of Addison's; zona fasciculata = the widest, foamy (lipid-laden) middle zone on histology.
>
> **Severity Indicators:**
> Aldosterone t½ 20 min, 60 % bound; cortisol t½ 60–90 min, 90–95 % bound to CBG; zona fasciculata 50 %; cortex 78 % vs medulla 22 % on the page; DHEA comes 90 % from the adrenal cortex and 10 % from the ovary.

> [!danger]+ **⚠️ Common Traps & Pitfalls**
>
> These are the mistakes that students and clinicians commonly make with this topic. Being aware of these traps helps you avoid diagnostic errors and answer tricky exam questions correctly.
>
> **Trap 1: "ACTH controls the whole adrenal"**
>
> **What students think:** ACTH regulates every adrenal hormone, including adrenaline.
>
> **Why this is wrong:** ACTH drives cortisol and adrenal androgens, has only a transient effect on aldosterone, and has no direct control of the medulla, which is a sympathetic ganglion fired by preganglionic nerves. Hyperkalemia (and angiotensin II) are the real aldosterone switches — which is why pituitary failure spares aldosterone and does not cause hyperkalemia.
>
> **How to avoid this trap:** "Cortex = ACTH (aldosterone only transiently); medulla = nerves."
>
> **Trap 2: Expecting edema in Conn's syndrome**
>
> **What students think:** Na⁺ and water retention must cause edema.
>
> **Why this is wrong:** Aldosterone escape — once BP and ECF rise, pressure diuresis and ANP excrete Na⁺ and water despite high aldosterone. The patient has hypertension, hypokalemia and alkalosis but no edema.
>
> **How to avoid this trap:** "Primary hyperaldosteronism: high BP, low K⁺, no edema."
>
> **Trap 3: Calling SAME a disease of high aldosterone**
>
> **What students think:** Licorice raises aldosterone.
>
> **Why this is wrong:** Glycyrrhetinic acid blocks 11β-HSD2, so cortisol (present at far higher concentration) occupies the MR. Aldosterone and renin are actually suppressed; the picture only *looks* like mineralocorticoid excess — hence "apparent".
>
> **How to avoid this trap:** "Apparent = the MR is fooled by cortisol; aldosterone is low."
>
> **Trap 4: Mixing up which white cells cortisol raises**
>
> **What students think:** Steroids suppress all white cells.
>
> **Why this is wrong:** Cortisol lowers eosinophils, basophils and lymphocytes but raises neutrophils (and RBCs and platelets). So Cushing's shows eosinopenia with neutrophilia, while Addison's shows eosinophilia and lymphocytosis.
>
> **How to avoid this trap:** "Cortisol: ↑ N, R, P — ↓ E, B, L."
>
> **Trap 5: Thinking the adrenal is the main testosterone source**
>
> **What students think:** Adrenal androgens are the main source of testosterone.
>
> **Why this is wrong:** The page notes the testis is the major source of testosterone; the adrenal makes mainly weak androgens (DHEA, DHEAS, androstenedione) and only small amounts of testosterone — these matter in women and in CAH, where they virilise.
>
> **How to avoid this trap:** "DHEAS = adrenal fingerprint (present exclusively in adrenal cortex); testosterone = testis."

> [!tip]+ **🔗 Related Concepts & Cross-Topic Connections**
>
> Understanding how this topic connects to other areas of medicine deepens your knowledge and helps you see the bigger picture. These connections also help you answer integrated questions on exams.
>
> **Related Topic 1: [[Pituitary Gland]]**
> ACTH from the anterior pituitary is the middle link of the HPA axis; pituitary ACTH-secreting adenoma is Cushing's *disease*, a subset of Cushing's syndrome.
>
> **Related Topic 2: [[Collecting Duct and Micturition Reflex]]**
> The principal cell (ENaC, ROMK, Na⁺–K⁺ ATPase) and the type A intercalated cell are where aldosterone, spironolactone and amiloride act.
>
> **Related Topic 3: [[Acid Base Balance]]**
> Aldosterone-driven H⁺ secretion explains the metabolic alkalosis of Conn's and the hyperkalemic acidosis of hypoaldosteronism.
>
> **Related Topic 4: [[Regulation of Blood Pressure]]**
> Renin–angiotensin–aldosterone, pressure diuresis and ANP are the mechanisms behind hypertension in Conn's and aldosterone escape.
>
> **Related Topic 5: [[Endocrine Pancreas]]**
> Cortisol is a counter-regulatory hormone: gluconeogenesis and insulin resistance cause the "adrenal diabetes" of Cushing's.
>
> **Related Topic 6: [[Male Reproduction]]**
> Testosterone, DHT and the major testicular source of testosterone — the counterpart of the adrenal's weak androgens and the adrenogenital syndrome.
>
> **Clinical Integration:**
> Hypertension with hypokalemia sends you to the aldosterone–renin ratio (Conn's vs SAME vs GRA); hyponatremia with hyperkalemia and hypotension sends you to a cortisol/ACTH test (Addison's); a virilised newborn girl or salt-wasting baby sends you to 17-OH progesterone (21-hydroxylase CAH). Long-term steroid therapy reproduces every Cushing's row in the functions table.
>
> **Exam Integration:**
> Expect questions on which zone makes which hormone, the enzyme column of each step (21-hydroxylase, 11β-hydroxylase, 17α-hydroxylase, aldosterone synthase, sulfotransferase), the half-lives and binding (20 min / 60 %; 60–90 min / 90–95 % CBG), aldosterone escape, SAME and licorice, GRA and dexamethasone, and "most circulating hormone = DHEAS".

---

## 🏆 Pearls (High-Yield Summary)

> [!success] Must-Know Pearls
> 1. Cortex **78 %**, medulla **22 %** (page values); **zona fasciculata = 50 %** — the widest zone.
> 2. **Glomerulosa → aldosterone** (+ stem cells for regeneration); **fasciculata → cortisol**; **reticularis → sex steroids**; **medulla → epinephrine, norepinephrine, dopamine**.
> 3. **Cholesterol** is the precursor; **desmolase** is the first step; **3β HSD** works in all three columns.
> 4. **21-hydroxylase** and **11-β hydroxylase** make cortisol; **aldosterone synthetase** finishes aldosterone; **sulfotransferase** makes **DHEAS** (present exclusively in adrenal cortex); **aromatase** turns testosterone → estrogen.
> 5. Enzyme deficiency → **congenital adrenal hyperplasia**; major source of testosterone = **testis**.
> 6. HPA axis: CRH → ACTH → adrenal cortex, cortisol gives negative feedback; **adrenal medulla is not under ACTH control**.
> 7. Aldosterone: life saving, **60 % bound**, **t½ 20 min**; acts on the **principal cell** (MR → ENaC, ROMK, Na⁺–K⁺ ATPase) and **type A intercalated cell** (H⁺ secretion); **spironolactone** blocks MR, **amiloride** blocks ENaC.
> 8. MR sites: kidneys, colon, hippocampus, salivary and sweat glands. **Hyperkalemia stimulates aldosterone**; ACTH only transiently.
> 9. **Conn's:** metabolic alkalosis, hypokalemia (cramps, atony, nephropathy), hypertension **without edema** (aldosterone escape: pressure diuresis + ANP).
> 10. **GRA:** aldosterone synthase + 11β-hydroxylase = **hybrid enzyme** under ACTH → treat with **dexamethasone**.
> 11. **Addison's:** hyponatremia, postural hypotension, hyperkalemia, microcardia + hypoglycemia, fatigue, eosinophilia, lymphocytosis.
> 12. Cortisol: **90–95 % bound to CBG/transcortin**, **t½ 60–90 min**; GR in the cytoplasm → nucleus; Cushing's = **buffalo hump, moon face, eosinopenia, hypercoagulable state, purple striae, hypertension**; cortisol is **permissive** for catecholamine lipolysis and bronchodilation.
> 13. **SAME:** licorice → glycyrrhetinic acid blocks **11β-HSD type 2** → cortisol acts on MR. **DHEAS = most circulating hormone in humans**; adrenogenital syndrome → females pseudohermaphroditism (beard, deep voice, baldness, hirsutism, clitoromegaly), prepubertal males rapid development of sex organs.

---

## 🔁 One-Line Recall

```
CORTEX 78 % · MEDULLA 22 % — G: aldosterone (salt) · F 50 %: cortisol (sugar) · R: DHEA/DHEAS (sex) · M: Epi, NE, DA
SYNTHESIS: cholesterol →desmolase→ pregnenolone → 3β HSD / 17α-OH / 21-OH / 11β-OH → aldosterone (synthetase) | cortisol | DHEA (17,20 lyase) → DHEAS (sulfotransferase)
HPA: CRH → ACTH → cortex (–ve feedback by cortisol) · medulla NOT under ACTH
ALDOSTERONE: 60 % bound, t½ 20 min · principal cell (MR → ENaC/ROMK/Na-K ATPase) · type A IC (H⁺ out) · ↑ by hyperkalemia
CONN'S: alkalosis + ↓K⁺ + HTN, no edema (escape) · GRA → hybrid enzyme → dexamethasone · ADDISON'S: ↓Na⁺ ↑K⁺ ↓BP microcardia
CORTISOL: 90–95 % CBG, t½ 60–90 min · GR → nucleus · Cushing's: hump, moon face, eosinopenia, hypercoagulable · SAME = licorice ⊣ 11β-HSD2
SEX STEROIDS: DHEAS most circulating · ↑ adrenal androgens → girls virilised, prepubertal boys precocious
```

---

## 🎬 Video Library

| What to watch | Link |
|---|---|
| Adrenal Cortex: Synthesis and Secretion — steroid hormones of the cortex | https://www.youtube.com/watch?v=lq_s0bgC5L4 |
| Anatomy and Physiology of the Adrenal Glands, Animation — cortex zones, medulla, regulation | https://www.youtube.com/watch?v=-d-9gRgz9pY |
| Zones of the Adrenal Cortex | https://www.youtube.com/watch?v=-wweKu9SI7s |
| Mineralocorticoids (Aldosterone) - Zona Glomerulosa - Adrenal Cortex - Endocrine Physiology Series | https://www.youtube.com/watch?v=P7EWCs0bWqk |
| Conn's Syndrome (Primary Hyperaldosteronism) | https://www.youtube.com/watch?v=cnaeJtq10vo |
| HPA axis — CRH, ACTH, cortisol (YouTube search) | https://www.youtube.com/results?search_query=HPA+axis+CRH+ACTH+cortisol+physiology |

---

## 🖼 Infographic Prompt — One-Page Summary

> [!abstract]- 🎨 Prompt for an image generator (copy everything inside)
> "Design a single-page, portrait A4 medical study infographic titled **'ADRENAL GLAND — SALT, SUGAR, SEX & ADRENALINE'** for a postgraduate physiology exam. Flat-vector textbook style, off-white background; colour code used everywhere: yellow = zona glomerulosa / aldosterone, green = zona fasciculata / cortisol, purple = zona reticularis / sex steroids, red = medulla / catecholamines, grey = disorders. Thin icons, crisp legible text, generous white space. Five panels:
>
> **Panel 1 — 'Anatomy'.** A triangular adrenal gland capping the superior surface of the kidney, labelled 'cortex 78 %' and 'medulla 22 %'. Beside it a layered histology column from top: 'connective tissue capsule', 'zona glomerulosa — aldosterone (mineralocorticoid); stem cells for regeneration', 'zona fasciculata (50 %) — cortisol (glucocorticoid)', 'zona reticularis — adrenal sex steroids', a dashed line, 'medulla — catecholamines: epinephrine, norepinephrine, dopamine'.
>
> **Panel 2 — 'Steroid hormone synthesis'.** Three coloured columns. Glomerulosa: cholesterol (precursor) → desmolase → pregnenolone → 3β HSD → progesterone → 21-hydroxylase → 11-deoxycorticosterone (weak mineralocorticoid) → 11-β hydroxylase → corticosterone (weak glucocorticoid) → aldosterone synthetase → aldosterone. Fasciculata: 17-α hydroxylase arrows to 17-OH pregnenolone → 3β HSD → 17-OH progesterone → 21-hydroxylase → 11-deoxycortisol → 11-β hydroxylase → cortisol. Reticularis: 17,20 lyase → dehydroepiandrosterone (source: adrenal cortex 90 %, ovary 10 %) → sulfotransferase → DHEAS (present exclusively in adrenal cortex); DHEA → 3β HSD → androstenedione → peripheral tissues → testosterone → aromatase → estrogen. Footnote box: 'enzyme deficiency → congenital adrenal hyperplasia; major source of testosterone → testis'.
>
> **Panel 3 — 'HPA axis'.** Hypothalamus → CRH → anterior pituitary → ACTH → adrenal cortex → cortisol, aldosterone, adrenal sex steroids; red dashed negative-feedback arrows from cortisol to hypothalamus and pituitary. Warning badge: 'Adrenal medulla is NOT under ACTH control'.
>
> **Panel 4 — 'Aldosterone (yellow)'.** Facts: life saving, 60 % bound, t½ 20 min. Two cell cartoons: principal cell (MR → proteins → ENaC Na⁺ in, ROMK K⁺ out, Na⁺–K⁺ ATPase; spironolactone ⊣ MR, amiloride ⊣ ENaC) and type A intercalated cell (CO₂ + H₂O → H⁺ + HCO₃⁻, H⁺ ATPase and H⁺–K⁺ ATPase stimulated by aldosterone, Cl⁻–HCO₃⁻ exchanger). 'MR sites: kidneys, colon, hippocampus, salivary glands, sweat glands'. 'Regulators: hyperkalemia ↑; ACTH ↑ transiently'. Disorder cards: Conn's (adenoma → metabolic alkalosis, hypokalemia → muscle cramps, atony, nephropathy, hypertension without edema); aldosterone escape (pressure diuresis + ANP → Na⁺ & H₂O excretion → no edema); GRA (aldosterone synthase + 11β-hydroxylase hybrid enzyme, ↑ ACTH → sustained aldosterone, treat dexamethasone); Addison's (hyponatremia, postural hypotension, hyperkalemia, microcardia).
>
> **Panel 5 — 'Cortisol & sex steroids (green / purple)'.** Facts: 90–95 % bound to CBG/transcortin, t½ 60–90 min; GR cartoon cytoplasm → nucleus → DNA. A two-column table of the 11 systems, physiological vs Cushing's (proteolysis → alanine / proximal myopathy; gluconeogenesis / adrenal diabetes; lipolysis / dyslipidemia, buffalo hump, moon face; anti-inflammatory, inhibits leukotrienes and phospholipase A₂ / infections; ↓ eosinophils, basophils, lymphocytes, ↑ RBC, neutrophils, platelets / eosinopenia, hypercoagulable state; appetite and mood / irritability, psychosis; ↑ CO and vascular tone / hypertension, atherosclerosis; ↑ GFR and Ca²⁺ excretion / hypercalciuria → renal stones; inhibits fibroblasts and collagen, promotes bone resorption / thin skin, ecchymosis, purple striae, osteoporosis; ↑ gastric acid / peptic ulcer; inhibits GnRH / amenorrhea, loss of libido, infertility). Small boxes: 'permissive — catecholamine lipolysis and bronchodilation'; 'Addison's cortisol deficiency → hypoglycemia, fatigue, eosinophilia, lymphocytosis'; 'SAME — licorice → glycyrrhetinic acid ⊣ 11β-HSD type 2 → cortisol binds MR'. Purple strip: 'DHEA, DHEAS (most circulating hormone), androstenedione, testosterone (small) → axillary & pubic hair, libido; ↑ adrenal androgens (tumors, CAH, adrenogenital syndrome) → females pseudohermaphroditism: beard, deep voice, baldness, hirsutism, clitoromegaly; prepubertal males: rapid development of male sex organs'.
>
> Footer strip: 'Salt · Sugar · Sex — the deeper you go, the sweeter it gets · medulla answers to nerves, not ACTH'. No watermark, no photographs of patients, illustration quality."

---

## 📚 References

- Physiology main notes (Marrow 8) — *Adrenal Gland*, pp. 239–244
- Guyton & Hall Textbook of Medical Physiology — Adrenocortical hormones
- Ganong's Review of Medical Physiology — The adrenal medulla and adrenal cortex
- OpenStax *Anatomy & Physiology* (CC BY 4.0) — 17.6 The Adrenal Glands
- Häggström M, Richfield D. Diagram of the pathways of human steroidogenesis. *WikiJournal of Medicine* 2014
- Wikimedia Commons — all embedded web images (licence noted in captions); `Adrenal Gland - ….png` files in `attachments/` are crops of the handwritten pages

[^1]: The page labels the gross figure "Cortex 78 %" and "Medulla 22 %". Most textbooks give the cortex about 80–90 % of the gland and the medulla about 10–20 %; the page's values are kept in the body.
[^2]: Textbooks put the zona fasciculata at roughly 75 % of the *cortex* (≈ 50 % of the whole gland), the glomerulosa ~15 % and the reticularis ~10 %. The glomerulosa lacks 17α-hydroxylase (so it cannot make cortisol or androgens) and the fasciculata/reticularis lack aldosterone synthase — the enzyme split behind the three columns. The fasciculata also makes some androgens and the reticularis some cortisol.
[^3]: "Desmolase" = cholesterol side-chain cleavage enzyme (P450scc, CYP11A1), in the mitochondria. The delivery of cholesterol into the mitochondrion by **StAR** protein is the rate-limiting step, and it is what ACTH acutely stimulates.
[^4]: The page reads "aldosterone synthetase"; standard texts call it **aldosterone synthase** (CYP11B2), a single enzyme that performs 11β-hydroxylation, 18-hydroxylation and 18-oxidation. It is expressed only in the zona glomerulosa.
[^5]: CAH: **21-hydroxylase deficiency** is ~90–95 % of cases (↓ cortisol and aldosterone, salt-wasting, ↑ 17-OH progesterone, ↑ androgens). **11β-hydroxylase deficiency** causes virilisation with hypertension (11-deoxycorticosterone is a mineralocorticoid); **17α-hydroxylase deficiency** causes hypertension with absent sex steroids. Low cortisol removes feedback, ACTH rises and the glands become hyperplastic.
[^6]: About 95 % of circulating testosterone in men comes from the Leydig cells of the testis; the adrenal makes mainly the weak androgens DHEA, DHEAS and androstenedione ([[Male Reproduction]]).
[^7]: The adrenal medulla is innervated by preganglionic sympathetic fibres (greater splanchnic nerves; acetylcholine on nicotinic receptors). Cortisol still matters indirectly: cortisol-rich blood reaching the medulla through the intra-adrenal portal flow induces PNMT, the enzyme that converts norepinephrine to epinephrine.
[^8]: "Life saving": removal of both adrenals kills within days unless mineralocorticoid is replaced, because the kidneys lose Na⁺ and retain K⁺ (hyperkalemia → arrhythmia, hypovolaemia → shock). Glucocorticoids are also needed to survive stress.
[^9]: Spironolactone and eplerenone are MR antagonists; amiloride and triamterene block ENaC. Both groups are potassium-sparing diuretics because less Na⁺ entry means a less negative lumen and less K⁺ secretion through ROMK.
[^10]: Aldosterone stimulates the H⁺-secreting pumps of the type A intercalated cell; this, together with hypokalemia, is why hyperaldosteronism causes metabolic alkalosis and hypoaldosteronism a hyperkalemic (type 4 RTA) acidosis.
[^11]: In the hippocampus (and heart) the MR has no 11β-HSD2 guard, so it is mostly occupied by cortisol; in the "epithelial" sites (kidney, colon, salivary and sweat glands) 11β-HSD2 keeps cortisol out so aldosterone can act. Sweat and salivary Na⁺ falls under aldosterone (Na⁺ conservation in heat).
[^12]: The main stimuli for aldosterone are **angiotensin II** (renin–angiotensin system) and **↑ plasma K⁺**; ↓ plasma Na⁺ is minor, and ACTH has only a brief, permissive effect — so pituitary failure does not cause aldosterone deficiency. ANP and dopamine inhibit aldosterone.
[^13]: The page reads "interstitial atony"; standard texts describe hypokalemic **intestinal** atony (paralytic ileus, constipation). Hypokalemic nephropathy = vacuolation of the tubules with a loss of urinary concentrating ability (nephrogenic diabetes insipidus → polyuria).
[^14]: Aldosterone escape begins after about 3–5 days of mineralocorticoid excess: the volume expansion raises arterial pressure (pressure natriuresis) and stretches the atria (ANP release), so Na⁺ balance is restored at a higher ECF and BP. K⁺ and H⁺ loss do **not** escape — hence the persistent hypokalemia and alkalosis.
[^15]: GRA = familial hyperaldosteronism type I (autosomal dominant): unequal crossing-over fuses the ACTH-responsive promoter of the 11β-hydroxylase gene (CYP11B1) to the coding sequence of aldosterone synthase (CYP11B2), so aldosterone is made in the zona fasciculata under ACTH control. Dexamethasone suppresses ACTH and therefore aldosterone.
[^16]: Addison's disease = primary adrenal insufficiency (most often autoimmune; tuberculosis in India), so both aldosterone and cortisol are lost; the ↑ ACTH (and its precursor POMC, which carries MSH) causes hyperpigmentation. Microcardia = a small heart shadow on chest X-ray, from reduced blood volume.
[^17]: Cortisol is ~75–80 % bound to CBG (transcortin) and ~15 % to albumin, leaving ~5–10 % free and active — together the page's "90–95 % bound". Its longer half-life (60–90 min) than aldosterone's (20 min) reflects this higher binding.
[^18]: The inactive GR sits in the cytoplasm attached to heat-shock protein 90 (hsp90); cortisol binding releases hsp90, the receptors dimerise and bind **glucocorticoid response elements (GRE)** on DNA (the "XXXXXX" in the figure). The MR works the same way — both are nuclear-receptor superfamily members.
[^19]: Cortisol redistributes fat: lipolysis in the limbs (thin arms and legs) with fat deposited centrally — face (moon face), dorsocervical pad (buffalo hump), supraclavicular fossae and trunk. Insulin (raised by the hyperglycemia) favours fat storage in these insulin-sensitive central depots.
[^20]: Cortisol induces **lipocortin-1 (annexin A1)**, which inhibits phospholipase A₂ — so less arachidonic acid is released and fewer **prostaglandins and leukotrienes** are made; it also suppresses COX-2, IL-1, IL-2 and histamine release.
[^21]: The white-cell changes are redistribution, not production: cortisol releases neutrophils from the marginal pool (neutrophilia) and sequesters eosinophils and lymphocytes in the spleen, lungs and lymph nodes (and triggers lymphocyte apoptosis). Hypercoagulability comes from ↑ clotting factors (VIII, fibrinogen, von Willebrand factor).
[^22]: Cortisol increases GFR and free-water excretion (a reason Addison's patients cannot excrete a water load), and it reduces intestinal Ca²⁺ absorption and tubular Ca²⁺ reabsorption → hypercalciuria and stones ([[Calcium Homeostasis]]).
[^23]: ⚠ The top label of the page's Cushing body figure is cut off; it reads like "(easy) bruising", written above "ecchymosis". Thin skin, easy bruising and wide purple striae are all due to the inhibition of fibroblasts and collagen formation.
[^24]: Permissive action: cortisol up-regulates β-adrenergic receptors and is needed for catecholamines (and glucagon) to produce their full lipolytic, glycogenolytic, vasoconstrictor and bronchodilator effects. Without it (Addison's) catecholamine-driven responses to stress fail — circulatory collapse in an adrenal crisis.
[^25]: Cortisol circulates at 100–1000 × the concentration of aldosterone and binds the MR with equal affinity. 11β-HSD2 converts cortisol to **cortisone** (the page's "inactive cortisol"). SAME can be congenital (*HSD11B2* mutation) or acquired (liquorice, carbenoxolone): hypertension, hypokalemia, metabolic alkalosis with **low renin and low aldosterone**; treated with spironolactone or dexamethasone.
[^26]: DHEAS is the most abundant circulating steroid hormone (micromolar levels, ~1000 × other steroids), peaking at 20–30 years and declining with age ("adrenopause"). Because sulfotransferase is adrenal, a very high DHEAS points to an adrenal (not ovarian) androgen source.
[^27]: In women the adrenal androgens supply about half of all androgen activity — pubic and axillary hair and libido at adrenarche; in men they are trivial beside testicular testosterone.
[^28]: In girls, excess adrenal androgens in fetal life virilise the external genitalia (46,XX — female pseudohermaphroditism, now "46,XX DSD") with normal ovaries and uterus. In boys there is no ambiguity at birth but **precocious pseudopuberty** (macrogenitosomia praecox) — pseudo because the gonads are not activated (no GnRH-driven spermatogenesis).
[^ety-adrenal]: **adrenal** — Latin *ad-*, "near, at" + *ren*, "kidney" + *-al*, "relating to" → the gland near the kidney. Its Greek-root synonym is *suprarenal* (*supra-*, above + *ren*). **Differentiate:** *adrenaline* (Latin route, British usage) = *epinephrine* (Greek route, American usage) — the same hormone.
[^ety-cortex]: **cortex** — Latin, "bark, rind, outer layer" → the outer part of an organ (adrenal, renal, cerebral cortex). Opposite *medulla*, the inner core. *Cortico-* (corticosteroid, corticotropin) means "of the adrenal cortex".
[^ety-steroid]: **steroid** — *ster-* from Greek *stereos*, "solid" (as in cholesterol, "solid bile") + *-oid*, "like" → a molecule like the sterols, built on the four-ring cyclopentanoperhydrophenanthrene nucleus. **Differentiate:** *sterol* (steroid alcohol, e.g. cholesterol) vs *steroid hormone* (cortisol, aldosterone, sex steroids).
[^ety-hormone]: **hormone** — Greek *hormōn*, "setting in motion, urging on" (*horman*, to impel) → a chemical messenger carried by blood that sets distant cells in motion; coined by Starling and Bayliss (1905). **Differentiate:** *endocrine* (via blood) · *paracrine* (to neighbours) · *autocrine* (to itself).
[^ety-synthesis]: **synthesis** — Greek *syn-*, "together" + *thesis*, "a placing" (*tithenai*, to put) → putting together: building a molecule from smaller parts. **Differentiate:** *synthesis* (building) vs *secretion* (releasing what was built) vs *-lysis* (breaking down); a *synthase* is an enzyme that builds without ATP, a *synthetase* one that uses ATP (the page's "aldosterone synthetase" is properly a synthase).
[^ety-medulla]: **medulla** — Latin, "marrow, pith, innermost part" → the inner core of an organ: adrenal medulla, renal medulla, medulla oblongata. Same root as *medullary carcinoma*.
[^ety-catecholamine]: **catecholamine** — *catechol* (from *catechu*, a Malay plant extract; a benzene ring with two –OH groups) + *amine* (an –NH₂ compound) → amines carrying a catechol ring: dopamine, norepinephrine, epinephrine. **Differentiate:** *catecholamines* vs *indoleamines* (serotonin, melatonin).
[^ety-zona]: **zona** — Latin, "belt, girdle" (Greek *zōnē*) → a belt-like layer; the three cortical zones are concentric belts. Same word in *zona pellucida* and *herpes zoster* ("girdle").
[^ety-glomerulosa]: **glomerulosa** — Latin *glomus*, "ball of yarn" + *-ulus*, small + *-osa*, "full of" → full of little balls: the cells form rounded clusters (arches). Same root as *glomerulus* of the kidney.
[^ety-aldosterone]: **aldosterone** — *ald-* (aldehyde, its C-18 –CHO group) + *-sterone* (a steroid ketone, as in testosterone) → the aldehyde steroid; isolated by Simpson and Tait in 1953.
[^ety-corticoid]: **mineralocorticoid / glucocorticoid** — *cortic-* "of the cortex" + *-oid* "like" → corticoids are cortex-like (cortex-derived) steroids; *mineralo-* = acting on minerals (Na⁺, K⁺) and *gluco-* = acting on glucose. **Differentiate:** cortisol has some mineralocorticoid action; aldosterone has almost no glucocorticoid action.
[^ety-regeneration]: **regeneration** — Latin *re-*, "again" + *generare*, "to produce, beget" + *-ation*, the process → producing again: replacement of lost cells by the same tissue. **Differentiate:** *regeneration* (same tissue restored) vs *repair / fibrosis* (replaced by scar) vs *hyperplasia* (more cells) vs *hypertrophy* (bigger cells).
[^ety-fasciculata]: **fasciculata** — Latin *fasciculus*, "little bundle" (*fascis*, bundle + *-culus*, small) + *-ata*, "having" → arranged in bundles: long straight cords of cells running radially. Same root as *fascicle* and *fasciculation*.
[^ety-cortisol]: **cortisol** — *cortis-* (adrenal cortex) + *-ol* (an alcohol –OH group) → the hydroxylated cortical steroid (hydrocortisone). **Differentiate:** *cortisol* (active, 11-OH) vs *cortisone* (inactive, 11-keto; "-one" = ketone) — 11β-HSD2 turns the first into the second.
[^ety-reticularis]: **reticularis** — Latin *reticulum*, "little net" (*rete*, net + *-culum*) → net-like: cords of cells anastomose into a network. Same root as *reticulocyte* and *endoplasmic reticulum*.
[^ety-epinephrine]: **epinephrine / norepinephrine** — Greek *epi-*, "upon" + *nephros*, "kidney" + *-ine* (chemical suffix) → the substance from the gland upon the kidney; *nor-* marks the molecule without the N-methyl group. Latin twin: *adrenaline / noradrenaline*.
[^ety-dopamine]: **dopamine** — *DOPA* (3,4-**d**ihydr**o**xy**p**henyl**a**lanine, its precursor) + *amine* → the amine made from DOPA; the first catecholamine in the chain dopamine → norepinephrine → epinephrine.
[^ety-cholesterol]: **cholesterol** — Greek *cholē*, "bile" + *stereos*, "solid" + *-ol*, alcohol → the solid alcohol of bile (first found in gallstones). Every steroid hormone is cut from it.
[^ety-enzyme]: **enzyme** — Greek *en*, "in" + *zymē*, "leaven, yeast" → "in yeast" (Kühne, 1877). Enzymes named with *-ase* are proteins that speed one reaction; a missing one blocks a pathway (CAH).
[^ety-desmolase]: **desmolase** — Greek *desmos*, "bond, band" + *-ol* + *-ase*, enzyme → the enzyme that breaks a C–C bond (cuts the cholesterol side chain). **Differentiate:** *desmolase* (side-chain cleavage, CYP11A1) vs *lyase* (17,20 lyase also cuts a C–C bond, but on the 17-OH steroids → androgens).
[^ety-dehydrogenase]: **dehydrogenase** — Latin *de-*, "away, removing" + *hydrogen* + *-ase*, enzyme → an enzyme that removes hydrogen (oxidises). 3β-HSD = 3β-hydroxysteroid dehydrogenase/isomerase; 11β-HSD2 = 11β-hydroxysteroid dehydrogenase type 2. **Differentiate:** *dehydrogenase* (removes H) vs *hydroxylase* (adds –OH) vs *reductase* (adds H, e.g. 5α-reductase).
[^ety-hydroxylase]: **hydroxylase** — *hydroxyl* (the –OH group: *hydr-* water + *oxy-* oxygen + *-yl*, a radical) + *-ase*, enzyme → an enzyme that attaches an –OH group at a numbered carbon: 17α-, 21-, 11β-hydroxylase. The number names the carbon; α/β name the side of the ring.
[^ety-dhea]: **dehydroepiandrosterone (DHEA)** — *de-* "removed" + *hydro-* "hydrogen" + *epi-* "upon" (an isomer) + *andro-* "male" + *-sterone* (steroid ketone) → an epi-isomer of androsterone with two hydrogens removed: a weak androgen. DHEA**S** = its sulfate ester.
[^ety-lyase]: **lyase** — Greek *lyein*, "to loosen, split" + *-ase* → an enzyme that splits a bond without water or oxidation; 17,20 lyase splits the side chain between C-17 and C-20. **Differentiate:** *lyase* (non-hydrolytic split) vs *hydrolase* (split by water) vs *-lysis* (the process, as in lipolysis).
[^ety-sulfotransferase]: **sulfotransferase** — *sulfo-*, "sulfate group" + *trans-*, "across" + *ferre*, "to carry" + *-ase* → an enzyme that carries a sulfate group across onto a molecule: DHEA → DHEAS.
[^ety-androstenedione]: **androstenedione** — *andro-*, "male" (Greek *anēr, andros*) + *-st-* (steroid) + *-ene* (one C=C double bond) + *-dione* (two ketone groups) → the male steroid with one double bond and two ketones; the direct precursor of testosterone and (by aromatase) estrone.
[^ety-testosterone]: **testosterone** — Latin *testis*, "testicle" (literally "witness") + *-sterone*, steroid ketone → the steroid of the testis; named by Ernst Laqueur's group (1935).
[^ety-estrogen]: **estrogen** — Greek *oistros*, "gadfly, frenzy, heat (of animals)" + *-gen*, "producing" → producer of oestrus (heat). **Differentiate:** *estrogen* (the class) vs *estradiol / estrone / estriol* (the three molecules).
[^ety-aromatase]: **aromatase** — *aromatic* (a benzene-type ring; Greek *arōma*, "spice") + *-ase* → the enzyme that turns ring A of an androgen into an aromatic ring: testosterone → estradiol, androstenedione → estrone. Aromatase inhibitors (letrozole) block it.
[^ety-congenital]: **congenital** — Latin *con-*, "together, with" + *genitus*, "born" + *-al* → present at birth. **Differentiate:** *congenital* (present at birth, cause may be genetic or not) vs *genetic* (in the genes, may appear later) vs *hereditary* (passed from parents).
[^ety-hyperplasia]: **hyperplasia** — Greek *hyper-*, "over, excessive" + *plasis*, "formation, moulding" + *-ia*, condition → excessive formation: an increase in cell *number*. In CAH, ↑ ACTH makes the cortex hyperplastic. **Differentiate:** *hyperplasia* (more cells) · *hypertrophy* (bigger cells) · *hypoplasia* (underdeveloped) · *aplasia* (absent) · *dysplasia* (disordered) · *neoplasia* (new, autonomous growth).
[^ety-hypothalamus]: **hypothalamus** — Greek *hypo-*, "below" + *thalamos*, "inner chamber" → the region below the thalamus; it secretes CRH, the top of the HPA axis.
[^ety-corticotropin]: **corticotropin / adrenocorticotropic** — *cortico-* "adrenal cortex" + Greek *tropos*, "a turning (towards)" → turning towards (stimulating) the adrenal cortex; *adreno-* adds "adrenal". ACTH = adrenocorticotropic hormone; CRH = corticotropin-releasing hormone.
[^ety-pituitary]: **pituitary** — Latin *pituita*, "phlegm, slime" → Galen thought the gland drained mucus from the brain into the nose. Its other name, *hypophysis* (Greek *hypo-* below + *physis* growth), is more accurate: the outgrowth below the brain.
[^ety-feedback]: **feedback** — English *feed* + *back*, from 1920s radio engineering: part of the output is returned to the input. **Differentiate:** *negative feedback* (the output switches its own stimulus off — cortisol on CRH/ACTH) vs *positive feedback* (the output boosts its stimulus — LH surge).
[^ety-duct]: **duct** — Latin *ductus*, "a leading, a conduit" (*ducere*, to lead) → a tube that leads fluid onward: the collecting duct leads urine to the renal pelvis. Same root as *abduction*, *conduction*.
[^ety-nephron]: **nephron** — Greek *nephros*, "kidney" + *-on*, a unit → the functional unit of the kidney (glomerulus + tubule + collecting duct).
[^ety-principal]: **principal cell** — Latin *principalis*, "first, chief" (*princeps*, the one who takes first place) → the main cell type of the collecting duct (~70 %), doing Na⁺ reabsorption and K⁺ secretion. **Differentiate:** *principal cells* (Na⁺/K⁺, water via aquaporin-2) vs *intercalated cells* (acid–base).
[^ety-receptor]: **receptor** — Latin *recipere*, "to take back, receive" (*re-* + *capere*) + *-tor*, the agent → the protein that receives a hormone. MR and GR are intracellular (nuclear) receptors, unlike membrane receptors for peptide hormones.
[^ety-protein]: **protein** — Greek *prōteios*, "of the first rank, primary" (*prōtos*, first) → named by Berzelius / Mulder (1838) as the primary substance of living matter.
[^ety-spironolactone]: **spironolactone** — *spiro-* (a spiro ring junction, Latin *spira*, coil) + *-lactone* (a cyclic ester, from Latin *lac*, milk — lactic acid) → a steroid lactone with a spiro ring; the MR blocker. Side-effect gynaecomastia because it also blocks androgen receptors.
[^ety-amiloride]: **amiloride** — a coined drug name (a pyrazine-carbonyl-guanidine; *-ide* is a chemical suffix) — origin of the stem uncertain. Remember it with triamterene as the ENaC-blocking potassium-sparing diuretics.
[^ety-intercalated]: **intercalated** — Latin *inter-*, "between" + *calare*, "to call, proclaim" → *intercalare*, to insert (a day into the calendar) → cells inserted between the principal cells. Same word in *intercalated discs* of cardiac muscle. **Differentiate:** type A (α) intercalated cell secretes H⁺; type B (β) secretes HCO₃⁻.
[^ety-epithelial]: **epithelial** — Greek *epi-*, "upon" + *thēlē*, "nipple" (originally the thin skin of the lips and nipple) + *-al* → the lining layer upon a surface. ENaC = the Na⁺ channel of such linings (kidney, colon, lung, sweat ducts).
[^ety-hippocampus]: **hippocampus** — Greek *hippos*, "horse" + *kampos*, "sea monster" → the seahorse, which the curled ridge in the temporal lobe resembles (Arantius, 1587). It carries MR and GR — cortisol shapes memory and mood here.
[^ety-hyperkalemia]: **hyperkalemia** — Greek *hyper-*, "excess" + New Latin *kalium*, "potassium" (from Arabic *al-qaly*, plant ashes) + *-emia*, "blood condition" → excess potassium in the blood (> 5.0–5.5 mmol/L). Its symbol K comes from *kalium*.
[^ety-hyperaldosteronism]: **hyperaldosteronism** — Greek *hyper-*, "excess" + *aldosterone* + *-ism*, a state → a state of excess aldosterone. **Differentiate:** *primary* (adrenal source, renin low — Conn's) vs *secondary* (renin-driven, renin high — heart failure, renal artery stenosis).
[^ety-conn]: **Conn's syndrome** — Jerome W. Conn (1907–1994), American endocrinologist at the University of Michigan, who described primary aldosteronism from an adrenal adenoma in 1955.
[^ety-syndrome]: **syndrome** — Greek *syn-*, "together" + *dromos*, "a running" → symptoms that run together. **Differentiate:** *syndrome* (a recognised cluster, cause may vary — Cushing's syndrome) vs *disease* (a specific cause — Cushing's disease = pituitary ACTH adenoma).
[^ety-etiology]: **etiology (aetiology)** — Greek *aitia*, "cause" + *-logia*, "study of" → the cause of a disease. **Differentiate:** *etiology* (why it happens) vs *pathogenesis* (how it develops) vs *pathophysiology* (the disordered function that results).
[^ety-adenoma]: **adenoma** — Greek *adēn*, "gland" + *-ōma*, "tumour, swelling" → a benign tumour of glandular epithelium. **Differentiate:** *adenoma* (benign) vs *adenocarcinoma* (malignant, *karkinos* crab) vs *hyperplasia* (non-neoplastic increase).
[^ety-metabolic]: **metabolic** — Greek *metabolē*, "change" (*meta-* change + *ballein* to throw) + *-ic* → relating to the chemical changes of the body; a *metabolic* acid–base disorder starts from HCO₃⁻, a *respiratory* one from PCO₂.
[^ety-alkalosis]: **alkalosis** — Arabic *al-qaly*, "the ashes (of saltwort)" → *alkali* + Greek *-ōsis*, "a condition" → a condition of too much base (pH > 7.45). **Differentiate:** *alkalosis* (the process/condition) vs *alkalemia* (the blood pH actually high) — likewise *acidosis* vs *acidemia*.
[^ety-hypokalemia]: **hypokalemia** — Greek *hypo-*, "under, deficient" + *kalium*, potassium + *-emia* → low blood potassium (< 3.5 mmol/L): weakness, cramps, ileus, U waves, polyuria.
[^ety-atony]: **atony** — Greek *a-*, "without" + *tonos*, "tension, tone" + *-y* → loss of muscle tone. **Differentiate:** *atony* (no tone) · *hypotonia* (reduced tone) · *dystonia* (abnormal sustained tone) · *atrophy* (wasting).
[^ety-nephropathy]: **nephropathy** — Greek *nephros*, "kidney" + *pathos*, "suffering, disease" + *-y* → disease of the kidney. **Differentiate:** *nephropathy* (any kidney damage) vs *nephritis* (inflammation) vs *nephrosis* (non-inflammatory, protein-losing).
[^ety-hypertension]: **hypertension** — Greek *hyper-*, "over" + Latin *tensio*, "stretching" (*tendere*, to stretch) → excessive arterial pressure. Opposite *hypotension*.
[^ety-retention]: **retention** — Latin *re-*, "back" + *tenere*, "to hold" + *-ion*, the process → holding back. **Differentiate:** *retention* (kept in the body — Na⁺ retention) vs *reabsorption* (taken back from the tubule) vs *excretion* (sent out in urine).
[^ety-edema]: **edema (oedema)** — Greek *oidēma*, "a swelling" (*oidein*, to swell) → excess fluid in the interstitial space. **Differentiate:** *edema* (interstitial fluid) vs *effusion* (fluid in a body cavity) vs *ascites* (peritoneal effusion).
[^ety-escape]: **escape** — Old French *escaper* from Latin *ex-*, "out of" + *cappa*, "cloak" → to slip out of one's cloak (and a captor's grip) → the kidney "slips out" of aldosterone's Na⁺-retaining hold after a few days.
[^ety-diuresis]: **diuresis / natriuresis** — Greek *dia-*, "through" + *ourein*, "to urinate" + *-sis*, the process → passing (water) through as urine; *natri-* (Latin *natrium*, sodium) + *-uresis* → passing sodium in the urine. **Differentiate:** *diuresis* (water) · *natriuresis* (Na⁺) · *kaliuresis* (K⁺) · *polyuria* (large volume, a symptom).
[^ety-natriuretic]: **natriuretic** — Latin *natrium*, "sodium" (from Egyptian/Greek *nitron*, soda) + Greek *ourētikos*, "promoting urine" → promoting sodium excretion. ANP comes from atrial myocytes when they are stretched.
[^ety-peptide]: **peptide** — Greek *peptos*, "digested, cooked" (*peptein*, to digest) + *-ide* → a short chain of amino acids (originally a product of digestion). **Differentiate:** *peptide* (< ~50 amino acids) vs *polypeptide* vs *protein* (folded, larger).
[^ety-remediable]: **remediable** — Latin *re-*, "again, back" + *mederi*, "to heal" + *-abilis*, "able to be" → able to be healed again; "glucocorticoid remediable" = cured by giving a glucocorticoid (dexamethasone).
[^ety-hybrid]: **hybrid** — Latin *hybrida*, "offspring of a tame sow and a wild boar" → a thing made of two different parents; here a chimeric gene with the 11β-hydroxylase promoter and the aldosterone synthase coding sequence.
[^ety-dexamethasone]: **dexamethasone** — a coined drug name of the corticosteroid *-asone / -methasone* family (a 9α-fluoro-16α-**meth**yl prednisolone, like betamethasone); the syllable *dexa-* is of uncertain origin. A potent, long-acting glucocorticoid with almost no mineralocorticoid action, so it suppresses ACTH strongly.
[^ety-addison]: **Addison's disease** — Thomas Addison (1793–1860), English physician at Guy's Hospital, London, who described the "disease of the suprarenal capsules" in 1855 (also Addisonian pernicious anaemia).
[^ety-insufficiency]: **insufficiency** — Latin *in-*, "not" + *sufficere*, "to be enough" (*sub-* under + *facere* to make) + *-ency*, state → the state of not being enough; adrenal insufficiency = too little cortical hormone. **Differentiate:** *insufficiency* (inadequate output) vs *failure* (complete loss) vs *crisis* (acute life-threatening decompensation).
[^ety-hyponatremia]: **hyponatremia** — Greek *hypo-*, "under" + Latin *natrium*, sodium + *-emia*, blood condition → low blood sodium (< 135 mmol/L). The symbol Na comes from *natrium*.
[^ety-hypotension]: **postural hypotension** — Latin *positura*, "position" + Greek *hypo-*, "under" + Latin *tensio*, "stretching" → low pressure on changing position: a fall of ≥ 20 mmHg systolic / 10 mmHg diastolic on standing. Same as *orthostatic* (Greek *orthos*, upright + *statos*, standing).
[^ety-microcardia]: **microcardia** — Greek *mikros*, "small" + *kardia*, "heart" + *-ia*, condition → a small heart (on chest X-ray). **Differentiate:** *microcardia* (small heart — Addison's, starvation) vs *cardiomegaly* (enlarged) vs *dextrocardia* (on the right).
[^ety-globulin]: **globulin** — Latin *globulus*, "little ball" (*globus*, ball + *-ulus*, small) + *-in*, protein → globular proteins of plasma. CBG = cortisol-binding globulin; SHBG, TBG are its cousins for sex steroids and thyroxine.
[^ety-transcortin]: **transcortin** — Latin *trans-*, "across" + *cortin* (cortical hormone) → the protein that carries cortisol across (through) the blood; another name for CBG.
[^ety-cytoplasm]: **cytoplasm** — Greek *kytos*, "hollow vessel, cell" + *plasma*, "something moulded" → the moulded material of the cell outside the nucleus. **Differentiate:** *cytoplasm* (all of it incl. organelles) vs *cytosol* (the fluid part only) vs *nucleoplasm*.
[^ety-nucleus]: **nucleus** — Latin, "kernel, little nut" (diminutive of *nux*, nut) → the kernel of the cell holding DNA, where activated GR and MR switch genes on.
[^ety-transcription]: **transcription** — Latin *trans-*, "across" + *scribere*, "to write" + *-ion* → copying across: DNA → mRNA. **Differentiate:** *transcription* (DNA → RNA, in the nucleus — what steroid receptors control) vs *translation* (RNA → protein, on ribosomes) vs *replication* (DNA → DNA).
[^ety-cushing]: **Cushing's syndrome** — Harvey Williams Cushing (1869–1939), American neurosurgeon at Johns Hopkins and Harvard, who described "pituitary basophilism" in 1932. **Differentiate:** *Cushing's syndrome* (cortisol excess from any cause, most often exogenous steroids) vs *Cushing's disease* (pituitary ACTH adenoma) vs *Cushing's reflex* (hypertension + bradycardia in raised ICP).
[^ety-proteolysis]: **proteolysis / lipolysis** — *protein* or Greek *lipos*, "fat" + *lysis*, "loosening, breaking down" → breakdown of protein (to amino acids) or of fat (triglyceride → fatty acids + glycerol). **Differentiate:** *-lysis* (breaking down) vs *-genesis* (making) vs *-poiesis* (producing cells).
[^ety-catabolic]: **catabolic / anabolic** — Greek *kata-*, "down" or *ana-*, "up" + *ballein*, "to throw" + *-ic* → throwing down (breaking molecules down, releasing energy) vs throwing up (building molecules up, using energy). Cortisol is catabolic in muscle but anabolic in liver.
[^ety-myopathy]: **myopathy** — Greek *mys, myos*, "muscle" (literally "mouse", for a muscle rippling under the skin) + *pathos*, disease + *-y* → muscle disease; *proximal* (Latin *proximus*, nearest) = of the limb girdles. **Differentiate:** *myopathy* (muscle itself) vs *neuropathy* (nerve) vs *myositis* (inflamed muscle).
[^ety-gluconeogenesis]: **gluconeogenesis** — Greek *glykys*, "sweet" (→ glucose) + *neos*, "new" + *genesis*, "creation" → creation of new glucose from non-carbohydrates (alanine, lactate, glycerol). **Differentiate:** *gluconeogenesis* (new glucose) · *glycogenolysis* (glycogen broken down to glucose) · *glycogenesis* (glycogen made) · *glycolysis* (glucose broken down).
[^ety-hyperglycemia]: **hyperglycemia** — Greek *hyper-*, "over" + *glykys*, "sweet" + *-emia*, blood condition → too much sugar in the blood (fasting > 126 mg/dL = diabetes). Cortisol causes it by gluconeogenesis and insulin resistance.
[^ety-diabetes]: **diabetes mellitus** — Greek *diabētēs*, "a siphon, passing through" (*dia-* through + *bainein* to go) + Latin *mellitus*, "honeyed" → honey-sweet urine passing through. **Differentiate:** *diabetes mellitus* (sweet urine, glucose) vs *diabetes insipidus* (*insipidus*, tasteless — dilute urine, ADH problem).
[^ety-dyslipidemia]: **dyslipidemia** — Greek *dys-*, "bad, abnormal" + *lipos*, "fat" + *-emia*, blood condition → abnormal blood lipids (↑ LDL, ↑ triglycerides, ↓ HDL). **Differentiate:** *dyslipidemia* (any abnormal pattern) vs *hyperlipidemia* (only raised).
[^ety-inflammation]: **inflammation** — Latin *in-*, "in" + *flamma*, "flame" + *-ation*, the process → setting on fire: Celsus' *rubor, calor, tumor, dolor*. **Differentiate:** *inflammation* (the tissue response) vs *infection* (invasion by microbes, which may cause inflammation); *anti-inflammatory* = against that response.
[^ety-leukotriene]: **leukotriene** — Greek *leukos*, "white" (first found in white cells) + *-triene* (three conjugated double bonds) → lipid mediators of white cells made by 5-lipoxygenase from arachidonic acid: bronchoconstriction, chemotaxis.
[^ety-phospholipase]: **phospholipase A₂** — *phospho-* (phosphate) + Greek *lipos*, fat + *-ase* → an enzyme that splits phospholipids; A₂ cuts the fatty acid at position 2, releasing arachidonic acid — the first step of prostaglandin and leukotriene synthesis.
[^ety-eosinophil]: **eosinophil** — Greek *Ēōs*, "dawn" (rosy) → *eosin*, the pink acid dye + *philos*, "loving" → a cell whose granules love eosin (stain pink-red). **Differentiate:** *eosinophil* (acid dye) · *basophil* (basic dye) · *neutrophil* (neither).
[^ety-basophil]: **basophil** — *base* (alkaline dye such as haematoxylin / methylene blue) + Greek *philos*, "loving" → a cell whose granules stain blue-purple with basic dyes; carries histamine.
[^ety-lymphocyte]: **lymphocyte** — Latin *lympha*, "clear water" + Greek *kytos*, "cell" → the cell of lymph. B and T lymphocytes fall under cortisol (lymphopenia; steroids are lympholytic).
[^ety-neutrophil]: **neutrophil** — Latin *neuter*, "neither" + Greek *philos*, "loving" → granules that take neither the acid nor the basic dye strongly (lilac). Cortisol raises them by demargination.
[^ety-eosinopenia]: **eosinopenia** — *eosin(ophil)* + Greek *penia*, "poverty, lack" → too few eosinophils (< 0.05 × 10⁹/L); a sensitive marker of cortisol excess or acute stress.
[^ety-coagulable]: **hypercoagulable** — Greek *hyper-*, "over" + Latin *coagulare*, "to curdle" (*co-* together + *agere* to drive) + *-abilis*, "able to be" → too easily clotted. **Differentiate:** *hypercoagulable state* (tendency) vs *thrombosis* (an actual clot in a vessel) vs *embolism* (a clot that travels).
[^ety-psychosis]: **psychosis** — Greek *psychē*, "mind, soul" + *-ōsis*, a condition → a condition of the mind with loss of contact with reality (delusions, hallucinations). **Differentiate:** *psychosis* (reality testing lost) vs *neurosis* (reality intact, distress) — steroid psychosis is a recognised side-effect.
[^ety-atherosclerosis]: **atherosclerosis** — Greek *athērē*, "gruel, porridge" + *sklērōsis*, "hardening" → hardening of arteries by porridge-like fatty plaques. **Differentiate:** *atherosclerosis* (intimal lipid plaque) vs *arteriosclerosis* (any arterial hardening) vs *arteriolosclerosis* (small vessels, hypertension).
[^ety-excretion]: **excretion** — Latin *ex-*, "out" + *cernere*, "to sift, separate" + *-ion* → sifting out: removal of wastes from the body. **Differentiate:** *excretion* (out of the body) vs *secretion* (*se-* apart — a cell releasing a useful product) vs *egestion* (passing faeces).
[^ety-hypercalciuria]: **hypercalciuria** — Greek *hyper-*, "excess" + Latin *calx, calcis*, "lime" (calcium) + Greek *ouron*, "urine" + *-ia* → too much calcium in the urine (> 4 mg/kg/day) → stones. **Differentiate:** *hypercalciuria* (urine) vs *hypercalcemia* (blood).
[^ety-fibroblast]: **fibroblast** — Latin *fibra*, "fibre" + Greek *blastos*, "germ, bud" → the "budding" cell that makes fibres (collagen, elastin). **Differentiate:** *-blast* (immature/building cell: osteoblast) vs *-cyte* (mature cell: osteocyte) vs *-clast* (breaking cell: osteoclast).
[^ety-proliferation]: **proliferation** — Latin *proles*, "offspring" + *ferre*, "to bear" + *-ation* → bearing offspring: multiplication of cells by division. **Differentiate:** *proliferation* (more cells by division) vs *differentiation* (cells becoming specialised) vs *hyperplasia* (the resulting increase in a tissue).
[^ety-collagen]: **collagen** — Greek *kolla*, "glue" + *-gen*, "producing" → glue-producing: boiled collagen gives glue / gelatin. Cortisol inhibits its synthesis → thin skin, striae, poor wound healing.
[^ety-resorption]: **resorption** — Latin *re-*, "back, again" + *sorbere*, "to suck in" + *-ion* → sucking back: osteoclasts dissolving bone and returning its mineral to the blood. **Differentiate:** *resorption* (bone or tissue removed) vs *reabsorption* (tubular fluid taken back into blood) vs *absorption* (from the gut).
[^ety-ecchymosis]: **ecchymosis** — Greek *ek-*, "out" + *chymos*, "juice" + *-ōsis*, condition → juice (blood) poured out into the skin: a bruise > 1 cm. **Differentiate by size:** *petechiae* (< 3 mm) · *purpura* (3 mm–1 cm) · *ecchymosis* (> 1 cm) · *haematoma* (a raised collection).
[^ety-striae]: **striae** — Latin *stria*, "furrow, groove, streak" (plural *striae*) → stretch marks. In Cushing's they are wide (> 1 cm) and purple because the thin dermis shows the venous blood beneath. Same root as *striated* muscle.
[^ety-osteoporosis]: **osteoporosis** — Greek *osteon*, "bone" + *poros*, "pore, passage" + *-ōsis*, condition → porous bone: normal mineralisation but too little bone mass. **Differentiate:** *osteoporosis* (less bone, normally mineralised) vs *osteomalacia* (*malakia*, softness — poorly mineralised bone) vs *osteopenia* (mild loss, a DEXA category).
[^ety-peptic]: **peptic ulcer** — Greek *peptikos*, "able to digest" (*peptein*, to digest) + Latin *ulcus*, "sore" → a sore digested by acid and pepsin. Cortisol raises acid and lowers mucosal prostaglandins.
[^ety-amenorrhea]: **amenorrhea** — Greek *a-*, "without" + *mēn*, "month" + *rhoia*, "flow" → absence of the monthly flow. **Differentiate:** *amenorrhea* (absent) · *oligomenorrhea* (infrequent) · *menorrhagia* (heavy) · *dysmenorrhea* (painful).
[^ety-libido]: **libido** — Latin, "desire, longing" (*libere*, to please) → sexual desire; the term was made famous by Freud. Androgens (testicular and adrenal) sustain it in both sexes.
[^ety-permissive]: **permissive** — Latin *permittere*, "to let through, allow" (*per-* through + *mittere* to send) + *-ive* → allowing: a hormone that does not cause an effect itself but must be present for another hormone to produce it fully (cortisol for catecholamines and glucagon; thyroid hormone for adrenaline).
[^ety-bronchodilation]: **bronchodilation** — Greek *bronchos*, "windpipe" + Latin *dilatare*, "to spread wide" (*dis-* apart + *latus* broad) + *-ation* → widening of the airways. **Differentiate:** *bronchodilation* (β₂, relaxes smooth muscle) vs *bronchoconstriction* (muscarinic M₃, leukotrienes).
[^ety-hypoglycemia]: **hypoglycemia** — Greek *hypo-*, "under" + *glykys*, sweet + *-emia* → low blood glucose (< 70 mg/dL; symptomatic < 55). In Addison's it follows the loss of cortisol-driven gluconeogenesis.
[^ety-eosinophilia]: **eosinophilia** — *eosinophil* + *-ia*, a condition → too many eosinophils in the blood (> 0.5 × 10⁹/L). **Differentiate:** *-philia* (an increase, a state of "loving" — eosinophilia, haemophilia is "love of bleeding") vs *-penia* (a lack).
[^ety-lymphocytosis]: **lymphocytosis** — *lymphocyte* + Greek *-ōsis*, a condition (here an increase) → too many lymphocytes. **Differentiate:** *-cytosis* (increase in a cell type: lymphocytosis, leukocytosis) vs *-penia* (decrease) vs *-cythemia* (polycythemia — red cells).
[^ety-licorice]: **licorice (liquorice)** — Greek *glykyrrhiza*, "sweet root" (*glykys* sweet + *rhiza* root) → Latin *liquiritia* → Old French *licorece*. The plant *Glycyrrhiza glabra* gives both the English and the chemical names.
[^ety-glycyrrhetinic]: **glycyrrhetinic acid** — from *Glycyrrhiza* (Greek *glykys*, "sweet" + *rhiza*, "root") + *-etinic* (a triterpenoid acid) → the active metabolite of glycyrrhizin, the sweet principle of licorice; it inhibits 11β-HSD2.
[^ety-adrenogenital]: **adrenogenital syndrome** — Latin *ad-* + *ren* (adrenal) + *genitalis*, "of generation" (*gignere*, to beget) → genital (sexual) changes caused by the adrenal: virilisation from adrenal androgens, usually congenital adrenal hyperplasia.
[^ety-androgen]: **androgen** — Greek *anēr, andros*, "man, male" + *-gen*, "producing" → producer of maleness: testosterone, DHT, DHEA, androstenedione.
[^ety-pseudohermaphroditism]: **pseudohermaphroditism** — Greek *pseudēs*, "false" + *Hermaphroditos*, son of Hermes and Aphrodite who merged with a nymph into one body of both sexes + *-ism*, state → false hermaphroditism: the gonads are of one sex (ovaries in a 46,XX girl) but the external genitalia look like the other. **Differentiate:** *true hermaphroditism* (both ovarian and testicular tissue — ovotesticular DSD) vs *pseudo-* (one gonad type, discordant genitalia).
[^ety-hirsutism]: **hirsutism** — Latin *hirsutus*, "shaggy, bristly" + *-ism*, state → male-pattern terminal hair in a woman (face, chest, linea alba), androgen-driven. **Differentiate:** *hirsutism* (androgen-dependent, male pattern) vs *hypertrichosis* (excess hair anywhere, not androgen-driven) vs *virilisation* (hirsutism + deep voice + clitoromegaly + muscle).
[^ety-clitoromegaly]: **clitoromegaly** — Greek *kleitoris*, "small hill" (possibly from *kleiein*, to close) + *megas, megalē*, "large" + *-y* → enlargement of the clitoris (the female homologue of the penis) under androgen excess.
[^pre-ad]: **ad- (af-, ac-, ag-…)** — to, towards, near: adrenal (near the kidney), adrenogenital, adrenocorticotropic. Don't confuse with **ab-** away from (abduction) · **a- / an-** without (atony, amenorrhea) · **aden-** gland (adenoma — a Greek root, not a prefix).
[^suf-oid]: **-oid** — like, resembling: steroid, mineralocorticoid, glucocorticoid, corticoid. Don't confuse with **-ode** a path or form (electrode, cathode) · **-ose** a sugar (glucose, fructose) · **-ol** an alcohol (cortisol).
[^pre-re]: **re-** — back, again: regeneration, resorption, receptor, retention, remediable. Don't confuse with **retro-** backwards, behind (retroperitoneal) · **pre-** before.
[^suf-ol]: **-ol** — a chemical alcohol (–OH group): cortisol, cholesterol, estradiol, calcitriol. Don't confuse with **-one** a ketone (C=O: progesterone, aldosterone, cortisone) · **-ole** small (arteriole) · **-ose** a sugar.
[^pre-gluco]: **gluco- / glyco- / glyc-** — sweet, glucose, sugar: glucocorticoid, gluconeogenesis, hyperglycemia, glycyrrhetinic. Don't confuse with **glia-** glue (neuroglia) · **glomer-** ball (glomerulosa).
[^pre-epi]: **epi-** — upon, over, beside: epinephrine (upon the kidney), epiandrosterone (an isomer). Don't confuse with **endo-** within · **ecto-** outside · **hypo-** under.
[^pre-nor]: **nor-** — a chemical prefix meaning "the parent compound without a methyl (–CH₃) group" (from German *N ohne Radikal*, "nitrogen without radical"): norepinephrine = epinephrine minus the N-methyl group. Don't confuse with **normo-** normal (normotension) · **neuro-** nerve.
[^pre-chole]: **chole- / chol-** — bile: cholesterol (solid of bile), cholecalciferol, cholecystokinin. Don't confuse with **chondro-** cartilage · **chloro-** green / chlorine · **cholin-** (choline, also first isolated from bile).
[^suf-ase]: **-ase** — an enzyme: desmolase, dehydrogenase, hydroxylase, lyase, sulfotransferase, aromatase, ATPase, phospholipase. Don't confuse with **-ose** a sugar (glucose) · **-ate** a salt or ester (sulfate, phosphate).
[^pre-de]: **de-** — away, down, removing, reversing: dehydrogenase (removes hydrogen), dehydroepiandrosterone, deoxycortisol (oxygen removed). Don't confuse with **di-** two (dione, dihydro-) · **dis- / dys-** apart / bad.
[^pre-trans]: **trans-** — across, through, beyond: sulfotransferase, transcortin, transcription. Don't confuse with **inter-** between · **intra-** within · **cis-** on the same side.
[^suf-one]: **-one** — a ketone (C=O) group in a chemical name: progesterone, aldosterone, androstenedione (two = *-dione*), cortisone, testosterone. Don't confuse with **-ol** an alcohol (cortisol) · **-ine / -amine** a nitrogen compound (dopamine).
[^pre-peri]: **peri-** — around, surrounding: peripheral (around the edge — tissues away from the gland), peritubular. Don't confuse with **para-** beside · **pre-** before · **post-** after.
[^suf-gen]: **-gen / -genic** — producing, giving rise to: estrogen, androgen, collagen, pathogen. Don't confuse with **-genesis** the process of making (gluconeogenesis) · **-gene** a unit of heredity.
[^pre-con]: **con- / com- / co-** — together, with: congenital, coagulable, contraction. Don't confuse with **contra-** against (contraindication) · **counter-** opposite (countercurrent).
[^pre-hyper]: **hyper-** — over, above, excessive: hyperplasia, hyperkalemia, hyperaldosteronism, hypertension, hyperglycemia, hypercalciuria, hypercoagulable. Don't confuse with **hypo-** under, deficient · **supra- / super-** above (Latin equivalents).
[^suf-plasia]: **-plasia** — formation, growth (of tissue): hyperplasia, hypoplasia, aplasia, dysplasia, neoplasia. Don't confuse with **-plasty** surgical repair (rhinoplasty) · **-plasm** formed substance (cytoplasm) · **-trophy** nourishment, size (hypertrophy).
[^pre-hypo]: **hypo-** — under, below, deficient: hypothalamus, hypokalemia, hyponatremia, hypotension, hypoglycemia, hypoaldosteronism. Don't confuse with **hyper-** over · **hypno-** sleep · **sub- / infra-** below (Latin).
[^suf-tropic]: **-tropic / -tropin** — turning towards, stimulating a target: adrenocorticotropic, corticotropin, gonadotropin, thyrotropin. Don't confuse with **-trophic** nourishing, enlarging (*trophē*, food — "adrenocorticotrophic" is a variant spelling with a different literal sense) · **-tropy** (isotropy, a direction).
[^pre-inter]: **inter-** — between: intercalated (inserted between), interstitial (standing between cells). Don't confuse with **intra-** within (intracellular) · **infra-** below.
[^suf-emia]: **-emia / -aemia** — a condition of the blood: hyperkalemia, hypokalemia, hyponatremia, hyperglycemia, dyslipidemia. Don't confuse with **-uria** a condition of the urine (hypercalciuria) · **-osis** a general condition.
[^suf-ism]: **-ism** — a state, condition or doctrine: hyperaldosteronism, hirsutism, pseudohermaphroditism, metabolism. Don't confuse with **-itis** inflammation · **-osis** a (disease) condition.
[^pre-syn]: **syn- / sym-** — together, with: synthesis (putting together), syndrome (running together), synthase, sympathetic. Don't confuse with **sin-** (Latin *sine*, without) · **semi-** half.
[^suf-oma]: **-oma** — a tumour or swelling: adenoma, carcinoma, lipoma. Don't confuse with **-osis** a condition (alkalosis) · **-stomy** a surgical opening (colostomy) · **-ectomy** removal.
[^suf-osis]: **-osis** — a condition, often abnormal or an increase: alkalosis, psychosis, atherosclerosis, osteoporosis, lymphocytosis, ecchymosis. Don't confuse with **-itis** inflammation · **-iasis** a disease state (lithiasis, giardiasis) · **-esis** a process (diuresis).
[^pre-a]: **a- / an-** — without, not: atony (without tone), amenorrhea (without menses). Don't confuse with **ad-** towards (adrenal) · **ab-** away from · **ana-** up (anabolic).
[^suf-pathy]: **-pathy** — disease, suffering: nephropathy, myopathy. Don't confuse with **-pathic** idiopathic (of unknown cause) · **sympathy** (feeling with — as in *sympathetic*).
[^pre-dia]: **dia-** — through, across, apart: diuresis (urine passing through), diabetes (siphon), diagnosis. Don't confuse with **di-** two (dione) · **dys-** bad · **dia-** with **diplo-** double.
[^suf-uresis]: **-uresis / -uria** — urination / a condition of the urine: diuresis, natriuresis, hypercalciuria, phosphaturia. Don't confuse with **-emia** blood · **-urea** the compound urea.
[^pre-in]: **in- (negative)** — not: insufficiency, intolerance, infertility. Don't confuse with **in- (directional)** into (inflammation — set on fire, inhalation) · **intra-** within.
[^pre-micro]: **micro-** — small: microcardia, microtubule. Don't confuse with **macro-** large · **mega- / -megaly** enlarged (clitoromegaly, cardiomegaly).
[^suf-cardia]: **-cardia** — a condition of the heart: microcardia, tachycardia, bradycardia, dextrocardia. Don't confuse with **-cardium** a layer (pericardium) · the **cardia** of the stomach.
[^suf-ule]: **-ule / -ulus / -culus** — small (diminutive): globulin (little ball), fasciculata (little bundle), glomerulosa, reticularis (little net). Don't confuse with **-ole** (arteriole — also small) with **-ol** an alcohol.
[^pre-cyto]: **cyto- / -cyte** — cell: cytoplasm, lymphocyte, osteocyte. Don't confuse with **cysto-** bladder, sac (cystitis) · **cysteine** (an amino acid).
[^suf-lysis]: **-lysis** — breaking down, loosening: proteolysis, lipolysis, glycogenolysis. Don't confuse with **-lyase** an enzyme that splits · **-lytic** (adjective: lympholytic) · **dialysis** (separating through a membrane).
[^pre-cata]: **cata- / kata-** — down: catabolic (breaking down). Don't confuse with **ana-** up (anabolic) · **meta-** change (metabolic) — and *catechol*amine, whose *cat-* is a plant name (catechu), not this prefix.
[^pre-ana]: **ana-** — up, again, back: anabolic (building up), anaphylaxis. Don't confuse with **an- / a-** without (anaemia) · **ante-** before · **anti-** against.
[^pre-neo]: **neo-** — new: gluconeogenesis (new glucose), neoplasia. Don't confuse with **neuro-** nerve · **nephro-** kidney.
[^suf-genesis]: **-genesis** — creation, origin (the process): gluconeogenesis, spermatogenesis, pathogenesis. Don't confuse with **-gen** the producer (estrogen) · **-genic** producing (pathogenic) · **-lysis** breaking down.
[^pre-lipo]: **lipo- / lip-** — fat: lipolysis, lipid, dyslipidemia, phospholipase. Don't confuse with **litho-** stone (lithotripsy) · **leio-** smooth (leiomyoma).
[^pre-dys]: **dys-** — bad, abnormal, difficult: dyslipidemia, dysplasia, dysmenorrhea. Don't confuse with **dis-** apart (dissection) · **de-** removal.
[^pre-anti]: **anti-** — against: anti-inflammatory, antimullerian, antidiuretic. Don't confuse with **ante-** before (antenatal) · **anti-** with **ana-** up.
[^pre-leuko]: **leuko- / leuco-** — white: leukotriene, leukocyte. Don't confuse with **luteo-** yellow (luteinising) · **leio-** smooth (leiomyoma) · **lympho-** lymph.
[^suf-phil]: **-phil** — a cell "loving" a dye or substance: eosinophil, basophil, neutrophil. Don't confuse with **-phobe** fearing (chromophobe) · **-philia** the state (eosinophilia).
[^suf-cyte]: **-cyte** — a cell (usually mature): lymphocyte, osteocyte, spermatocyte. Don't confuse with **-blast** an immature or building cell (fibroblast) · **-clast** a breaking cell (osteoclast).
[^suf-penia]: **-penia** — lack, deficiency: eosinopenia, lymphopenia, osteopenia, neutropenia. Don't confuse with **-philia** increase (eosinophilia) · **-plasia** formation.
[^pre-ex]: **ex- (e-, ef-)** — out of, away: excretion, escape. Don't confuse with **exo-** outside (exocrine) · **extra-** beyond (extracellular).
[^suf-uria]: **-uria** — a condition of the urine: hypercalciuria, polyuria, phosphaturia, haematuria. Don't confuse with **-emia** a condition of the blood · **-uresis** urination (diuresis).
[^suf-blast]: **-blast** — a bud, germ, immature or building cell: fibroblast, osteoblast. Don't confuse with **-clast** breaker (osteoclast) · **-cyte** mature cell (osteocyte).
[^pre-osteo]: **osteo- / oste-** — bone: osteoporosis, osteoclast, osteoblast. Don't confuse with **ostium / ostia** a mouth or opening · **oto-** ear.
[^suf-rrhoea]: **-rrhea / -rrhoea** — flow, discharge: amenorrhea (no flow), diarrhoea. Don't confuse with **-rrhage / -rrhagia** heavy bleeding (menorrhagia) · **-rrhaphy** suturing · **-rrhexis** rupture.
[^suf-philia]: **-philia** — a state of love for, an increase or tendency: eosinophilia, haemophilia. Don't confuse with **-phil** the cell itself (eosinophil) · **-penia** decrease · **-phobia** fear.
[^pre-pseudo]: **pseudo-** — false: pseudohermaphroditism, pseudopuberty, pseudohypoparathyroidism. Don't confuse with **pseudo-** with **proto-** first · **para-** beside, abnormal.
[^suf-megaly]: **-megaly** — enlargement: clitoromegaly, cardiomegaly, hepatomegaly, splenomegaly. Don't confuse with **micro-** small (microcardia) · **macro-** large (as a prefix: macrogenitosomia) · **-trophy** growth by cell size.
