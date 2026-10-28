---
title: Vision
aliases: [Vision, Physiology of vision, Retina and phototransduction, Visual pathway, Colour vision]
rank: 17
status: not-started
topic: Physiology
subtopic: Central Nervous System
chapter: 17
pages: "83–88"
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
source: "Physiology main notes (Marrow 8) — Vision, pp. 83–88 (sections: Organisation of vision (opening, no timestamp) · Retina 00:02:00 · Visual Pathway 00:33:00 · Thalamus 00:38:00 · Visual Cortex 00:46:21 · Colour Vision 00:51:08 · Order of neurons & light reflex 01:01:10)"
mindmap: "[[Vision — Mind Map]]"
index: "[[Physiology — Index]]"
review_day_2: false
review_day_4: false
review_day_7: false
review_day_10: false
review_day_15: false
---
# 👁️ Vision

> [!abstract] Core Definition
> **Vision is a special sense.** Light is turned into a nerve signal in the **retina**[^ety-retina], relayed in the **thalamus** (lateral geniculate body) and interpreted in the **occipital**[^ety-occipital] **visual cortex**. Every line of the chapter answers one of three questions:
> - ✅ **How does the retina turn light into a signal?** — seven cell types, rods vs cones, lateral inhibition, **phototransduction**.
> - ✅ **Which way does the signal travel?** — optic nerve → chiasma → tract → **LGB (6 layers)** → radiation → **area 17**, and the parallel M, P and K channels.
> - ✅ **What do the clinical tests check?** — colour vision (cones, colour blindness, Ishihara), order of neurons, **pupillary light reflex**.

---

## 🧠 Mental Model — A Camera That Is Switched On in the Dark

Think of the photoreceptor as a **tap that runs in the dark**: in darkness its Na⁺ channel is held open by cGMP, the cell is depolarised and keeps releasing glutamate. **Light turns the tap off** — rhodopsin activates transducin, phosphodiesterase destroys cGMP, the Na⁺ channel shuts and the cell **hyperpolarises**. Everything downstream (bipolar, ganglion, LGB, cortex) reads *changes* in that glutamate stream, sharpened at each step by lateral inhibition and sorted into "where/motion" (M), "detail/colour" (P) and "blue" (K) channels.

```
LIGHT → passes ganglion & bipolar layers → PHOTORECEPTOR (1st) → BIPOLAR (2nd) → GANGLION (3rd: only AP, only output)
      → optic nerve → CHIASMA (nasal fibres cross) → optic tract → LGB (4th; 6 layers: 1,2 = M · 3–6 = P · K between)
      → optic radiation → VISUAL CORTEX (calcarine, area 17, striate) → parietal (M: eye movements) / temporal (P: colour, faces)

DARK  : cGMP high → Na⁺ (funny) channel OPEN → depolarised (−60 mV on the page) → glutamate RELEASED
LIGHT : 11-cis → all-trans retinal → transducin → phosphodiesterase → ↓ cGMP → channel SHUT → HYPERPOLARISED → glutamate ↓
```

---

## 🪜 Organisation of Vision

- **Vision is a special sense.**
- **Organisation of vision: 3 levels**

```
Retina
  ↓
Thalamus
  ↓
Occipital visual cortex
```

> [!note] Note
> **General senses have 4 levels of organisation** (they include the **spinal cord**): skin → spinal cord → thalamus → sensory cortex — see [[Somatosensory Pathways]].

![[Vision - organisation of vision.png]]
*Organisation of vision — retina → thalamus → occipital cortex, the three levels (cropped from the handwritten page).*

---

## 🔬 Retina

**7 types of cells:**
- **1st – 6th:** play a role in vision.
- **7th:** supporting cell.

### Retinal cells

| Retinal cell | Features |
|---|---|
| 1. **Rods** | Rod shaped |
| 2. **Cones** | Cone shaped |
| 3. **Bipolar**[^ety-bipolar][^pre-bi] **cell** | Has **2 poles** → one to **receive** information, one to **conduct** information |
| 4. **Ganglion**[^ety-ganglion] **cells (GC)** | **Only retinal cell to:** <br>– **have an output:** axons → **optic nerve** → **thalamus** <br>– **generate action potential** (for impulses to travel long distances)[^1] |
| 5. **Horizontal cell** | Connects **cones & rods** |
| 6. **Amacrine**[^ety-amacrine][^pre-a] **cell** | Connects **bipolar cell to ganglion cells** |
| 7. **Muller's cell**[^ety-muller-cell] (AKA retinal glial[^ety-glia] cell) | • AKA **retinal glial cell** <br>• **Supportive function** |

![[Vision - retinal cells.png]]
*Retinal cells — cones and rods at the back of the eye, Müller's cell spanning the retina, horizontal, bipolar, amacrine and ganglion cells; light enters from the ganglion-cell side (cropped from the handwritten page).*

> [!info] Light travels "backwards" through the retina
> Light passes the ganglion, amacrine, bipolar and horizontal cells **before** it reaches the rods and cones, which lie against the pigment epithelium at the back of the eye. The signal then travels the other way: photoreceptor → bipolar → ganglion → optic nerve.[^2]

### Photoreceptors[^ety-photoreceptor][^pre-photo]

| | **Rods** | **Cones** |
|---|---|---|
| **Sensitive to** | **Dim lights (night vision)** | **Colour vision (day vision)** |
| **Number** | 100 million | 5 million[^3] |
| **Pigment** | **Rhodopsin**[^ety-rhodopsin][^suf-opsin] / visual purple | **Iodopsin**[^ety-iodopsin] |
| **Abundant in** | **Peripheral retina** | • **Central retina** <br>• **Foveola**[^ety-fovea][^suf-ola]: **only cones (rod free zone)** |

### Lateral inhibition[^ety-inhibition][^pre-in]

```
Horizontal / Amacrine cell
          ↓
Inhibits lateral cells
          ↓
Enhanced output from central cell
          ↓
↑ contrast & sharpness
```

- 🧠 The horizontal/amacrine cells **subtract** activity from the neighbours (L) of a stimulated cell (C), so the edge between light and dark looks sharper than it really is.

![[Vision - lateral inhibition.png]]
*Lateral inhibition — horizontal/amacrine cells inhibit (−) the lateral cells (L) so the output of the central cell (C) stands out (cropped from the handwritten page).*

### Melanopsin ganglion cells (mGC)[^ety-melanopsin]

- **mGC → directly stimulated by light.**
- **Pigment: melanopsin.**
- Contains **PACAP**[^ety-pacap]: **pituitary adenylate cyclase activating polypeptide** → for signalling.[^4]

**Projections of mGCs:**

```
                     Projections of mGCs
             ┌──────────────┴──────────────┐
  Hypothalamus: Retinal              Pretectal nucleus
  hypothalamic tract (RHT)                  ↓
             ↓                     Edinger Westphal nucleus:
  Suprachiasmatic nucleus:         regulates pupillary light reflex
  regulates 24 hr circadian rhythm
```

- **Hypothalamus → retinal hypothalamic tract (RHT) → suprachiasmatic**[^ety-suprachiasmatic][^pre-supra] **nucleus: regulates 24 hr circadian**[^ety-circadian][^pre-circa] **rhythm.**
- **Pretectal**[^ety-pretectal][^pre-pre] **nucleus → Edinger Westphal**[^ety-edinger-westphal] **nucleus: regulates pupillary light reflex.**

### Phototransduction[^ety-phototransduction][^pre-trans]

**Changes in the retina when light strikes it.**

**Rods:**
- Contain **rhodopsin** → **opsin + vitamin A**.
- **Forms of vit A:**
  - **11-cis**[^pre-cis] **retinal** — **dark state**.
  - **All-trans retinal** — **light state**.

#### In dark state

- **RMP of rods = −60 mV** (passive K⁺ diffusion).[^5]

```
Funny current channel remains open
          ↓
Allows Na⁺ influx
          ↓
DEPOLARIZATION
          ↓
Glutamate release (neurotransmitter)
```

- **Depolarization**[^ety-depolarization][^pre-de] → **glutamate**[^ety-glutamate] release (neurotransmitter).
- **K⁺ efflux maintains a RMP = −60 mV** through the K⁺ channel of the inner segment.

![[Vision - rod in dark state depolarisation.png]]
*Rods during depolarization (dark) — the cGMP-dependent (funny current) Na⁺ channel is open, K⁺ efflux through the K⁺ channel maintains RMP ≈ −60 mV, glutamate is released (cropped from the handwritten page).*

#### In light state

```
11 cis retinal                         K⁺ channels remain open
     ↓ light                                    ↓
All trans retinal                          K⁺ efflux
     ↓ (+)                                      ↓
Transducin                              HYPERPOLARISATION
     ↓ (+)                                      ↓
Phosphodiesterase                     ↓ glutamate release
     ↓
Degrades cGMP
     ↓
Closure of funny Na⁺ channel
```

- **All trans retinal** → (+) **transducin**[^ety-transducin][^suf-in] → (+) **phosphodiesterase**[^ety-phosphodiesterase][^suf-ase] → degrades **cGMP** → **closure of funny Na⁺ channel**.
- **K⁺ channels remain open → K⁺ efflux → Hyperpolarisation**[^ety-hyperpolarisation][^pre-hyper] **→ ↓ glutamate release.**

![[Vision - rod in light state hyperpolarisation.png]]
*Hyperpolarisation (light) — the cGMP-dependent Na⁺ channel is closed (✗), the K⁺ channel stays open, glutamate release decreased (cropped from the handwritten page).*

#### Wald's visual cycle[^ety-wald]

- **Constant cycling between 2 forms of vitamin A during day & night.**

```
        ┌──────────────── light ───────────────┐
        │                                      ↓
 11 cis retinal (Dark)              All trans retinal (Light)
        ↑                                      │
        └──────────── regenerated ─────────────┘
```

#### Funny current channels / hyperpolarisation cyclic nucleotide (HCN) channels[^ety-hcn]

- **Na⁺ channels.**
- **Location & function:**
  - **Retina: vision.**
  - **SA node: generation of HR.**
- **Opened by cGMP.**[^6]

#### Amacrine cells

- **Purely depolarizing cells of retina (no hyperpolarisation).**
- **Role in lateral inhibition.**
- **Neurotransmitter: Acetylcholine**[^ety-acetylcholine].[^7]

🎬 **Watch:** [YouTube search — phototransduction in rods](https://www.youtube.com/results?search_query=phototransduction+rods+animation) · [YouTube search — retina cell layers physiology](https://www.youtube.com/results?search_query=retina+layers+cells+physiology+lecture)

---

## 🛣️ Visual Pathway

![[Vision - visual pathway.png]]
*Visual pathway — temporal and nasal fields of the left (L) and right (R) eyes → optic nerve (I/L nasal & temporal fibres) → optic chiasma (nasal fibres cross) → optic tract (I/L temporal & C/L nasal fibres) → thalamic nucleus: lateral geniculate body (LGB) → optic radiation → visual cortex (cropped from the handwritten page).*

| Structure | Fibres it carries (from the page) |
|---|---|
| **Optic nerve** | **I/L nasal & temporal fibres** |
| **Optic chiasma**[^ety-chiasma] | **Nasal fibres cross** |
| **Optic tract** | **I/L temporal & C/L nasal fibres** |
| **Thalamic nucleus** | **Lateral geniculate body (LGB)**[^ety-geniculate] |
| **Optic radiation** | LGB → visual cortex |
| **Visual cortex** | Occipital lobe |

- **I/L** = ipsilateral[^ety-ipsilateral][^pre-ipsi], **C/L** = contralateral[^pre-contra].
- **Significance: visual defect depends upon the location of lesion.**[^8]

🎬 **Watch:** [Visual pathway and its defects — optic nerve, chiasm, tract, lateral geniculate body](https://www.youtube.com/watch?v=7YCl0C5cCcU) · [Visual field defects and optic nerve pathway](https://www.youtube.com/watch?v=2ZbFBlwWm3Q)

![](https://www.youtube.com/watch?v=7YCl0C5cCcU)

---

## 🔀 Thalamus

### Lateral geniculate body

- **Has 6 layers.**

| | **Magnocellular**[^ety-magnocellular][^pre-magno] **pathway** (M cells / big) | **Parvocellular**[^pre-parvo] **pathway** (P cells / small) | **Koniocellular**[^pre-konio] **pathway** (K cells) |
|---|---|---|---|
| **Origin** | **1, 2 layers** | **3, 4, 5, 6 layers** | **Between P & M cells** |
| **Termination** | **Layer 4 of visual cortex** | **Layer 4 of visual cortex** | — |
| **Function** | • **Extraocular**[^pre-extra] **movements** <br>• **Detection of flickering** | • **Colour vision** <br>• **Finer details in the visual field** | **Colour vision: Blue** |

### Inputs to LGB

- **I/L LGB receives input from I/L & C/L eye.**
- **Layers 1, 4, 6 → receive C/L fibres.**
- **Layers 2, 3, 5 → receive I/L fibres.**[^9]

![[Vision - right LGB fibres.png]]
*Right LGB fibres — the right (ipsilateral) eye feeds layers 2, 3, 5 and the left (contralateral) eye feeds layers 1, 4, 6 (cropped from the handwritten page).*

![[Vision - layers of LGB.png]]
*Layers of the LGB, numbered 1–6 from the ventral (magnocellular) to the dorsal (parvocellular) side (cropped from the handwritten page).*

---

## 🧩 Visual Cortex

### Location

- **Calcrine cortex**[^ety-calcarine] **(in occipital lobe): Brodman's area 17, 18, 19.**[^ety-brodmann][^10]
- **Heavily myelinated.**
- **Stripes / striae appearance: Striae of Gennasi**[^ety-gennari] **(AKA striate**[^ety-striate][^suf-ate] **cortex).**

![[Vision - visual cortex Brodmann areas.png]]
*Visual cortex — areas 17, 18, 19 circled at the occipital pole; the other numbers mark other Brodmann areas (cropped from the handwritten page).*

### Cells

| | **Simple cell** | **Complex cell** | **Blobs** |
|---|---|---|---|
| **Function** | • **Higher order processing.** <br>• **Feature detectors: detect minute changes.** | (same as simple cell — the page writes one box across both) | • **Colour vision.** <br>• **Expresses cytochrome oxidase**[^ety-cytochrome][^suf-ase]**.** |

- 🧠 Simple and complex cells respond to **lines and edges of a particular orientation** (simple: at one place; complex: anywhere in their field, often moving), so they "detect minute changes"; blobs are colour-processing patches.[^11]

### Extra striate cortices[^pre-extra]

| | **Parietal lobe** | **Temporal lobe** |
|---|---|---|
| **Projections from** | **Magnocellular pathway** | **Parvocellular pathway** |
| **Function** | **Eyeball movements** | **Colour vision** |

![[Vision - extrastriate cortex.png]]
*Extrastriate cortex — the parietal lobe (magnocellular input) and the temporal lobe (parvocellular input) (cropped from the handwritten page).*

### Inferior temporal cortex

- **Function: face recognition by sight.**
- **Lesion: Prosopagnosia**[^ety-prosopagnosia][^suf-gnosia] **→ loss of recognition of faces.**[^12]

---

## 🌈 Colour Vision

### Pathway

```
Retina : Cones
   ↓
Thalamus : Parvocellular pathway
   ↓
Visual cortex : Blobs
```

![[Vision - Ishihara chart.png]]
*Ishihara chart — the numeral is visible to a normal trichromat and hidden from a red–green colour-blind person (cropped from the handwritten page).*

### Cones

- **Primary colours: Red, blue, green.**
- **Types of cones:**[^ety-trichromacy]

| | **L cone** | **M cone** | **S cone** |
|---|---|---|---|
| **Wavelength detection** | **Long** | **Medium** | **Small**[^13] |
| **Colour** | **Red** | **Green** | **Blue** |

### Colour blindness

- **X-linked**[^ety-x-linked] **recessive**[^ety-recessive] **disorders.**
- **Affects males > females (carriers).**
- **m/c: Red green defect.**[^14]

| Colour defect | Name |
|---|---|
| **Red** | **Protanopia**[^ety-protanopia][^pre-proto][^suf-anopia] |
| **Green** | **Deuteranopia**[^pre-deutero] |
| **Blue** | **Tritanopia**[^pre-trito] |

![[Vision - colour blindness simulation.png]]
*The same picture seen with normal colour vision and with deuteranopia, tritanopia and protanopia (cropped from the handwritten page).*

🎬 **Watch:** [YouTube search — colour vision, cones and colour blindness](https://www.youtube.com/results?search_query=colour+vision+cones+colour+blindness+physiology)

---

## 🔦 Order of Neurons & Light Reflex

### Order of neurons

| Order | Neuron |
|---|---|
| **1st order neuron** | **Photoreceptors** (cone, rod) |
| **2nd order neuron** | **Bipolar cell** |
| **3rd order neuron** | **Ganglion cell** → optic nerve → optic chiasma |
| **4th order neuron** | **Lateral geniculate body** → optic radiation → visual cortex |

![[Vision - order of neurons.png]]
*Order of neurons — photoreceptors (1st), bipolar cell (2nd), ganglion cell (3rd) → optic nerve → optic chiasma → lateral geniculate body (4th order neuron) → optic radiation → visual cortex (cropped from the handwritten page).*[^15]

### Light reflex

| Component | Structure |
|---|---|
| **Afferent** | **Optic nerve** |
| Relay | **Pretectal nucleus** — fibres **cross over** to both sides |
| **Centre** | **Edinger Westphal nucleus** |
| **Efferent** | **Oculomotor**[^ety-oculomotor] **nerve** (the page spells "occulomotor") |
| Relay | **Ciliary**[^ety-ciliary] **ganglion** |
| Effector | **Sphincter pupillae**[^ety-sphincter-pupillae] → **pupils constrict** |

```
Light source → R eye
      ↓
Optic nerve (afferent) → optic chiasm → optic tract
      ↓
Pretectal nucleus ── cross over ──► both Edinger-Westphal nuclei (centre)
      ↓                                       ↓
Oculomotor nerve (efferent, R)          Oculomotor nerve (efferent, L)
      ↓                                       ↓
Ciliary ganglion                        Ciliary ganglion
      ↓                                       ↓
Sphincter pupillae → pupil constricts   Sphincter pupillae → pupil constricts
      ↓                                       ↓
DIRECT LR (lit eye)                     INDIRECT LR (other eye)
```

- 🧠 Because the pretectal fibres **cross over** to both Edinger-Westphal nuclei, light in one eye constricts **both** pupils: the lit eye = **direct** light reflex, the other eye = **indirect** (consensual)[^ety-consensual] light reflex.[^16]

![[Vision - light reflex pathway.png]]
*Light reflex pathway — optic nerve (afferent) → pretectal nucleus → cross over → Edinger–Westphal nucleus (centre) → oculomotor nerve (efferent) → ciliary ganglion → sphincter pupillae → pupils constrict: direct LR (right, lit eye) and indirect LR (left) (cropped from the handwritten page).*

Rotate the visual pathway in 3D — eyeball, optic nerve, chiasm, tract, LGB, radiation and the calcarine cortex, with the oculomotor nerve and ciliary ganglion of the light reflex:

```anatomed
# visual pathway and light reflex — retype a name with the plugin's autocomplete if it shows as "unmatched"
parts: eyeball, retina, optic nerve, optic chiasm, optic tract, lateral geniculate body, optic radiation, calcarine sulcus, occipital lobe, oculomotor nerve, ciliary ganglion
detail: related
title: Visual pathway and pupillary light reflex
```

🎬 **Watch:** [YouTube search — pupillary light reflex pathway](https://www.youtube.com/results?search_query=pupillary+light+reflex+pathway)

---

## Core Dictum & Pattern Recognition

> [!check]+ **🎯 Core Dictum - The Unifying Principle**
>
> Vision is a chain of **four neurons** (photoreceptor → bipolar → ganglion → LGB) feeding the **striate cortex (area 17)**, and its key oddity is that the photoreceptor is **active in the dark**: cGMP keeps its Na⁺ channel open, the cell is depolarised and releases glutamate; **light hyperpolarises it** by activating transducin and phosphodiesterase, which destroy cGMP. Only the **ganglion cell** fires action potentials and sends an axon out of the eye.
>
> After the retina the signal is **sorted, not mixed**: nasal fibres cross at the chiasma so each optic tract carries the opposite visual field; each LGB keeps the two eyes in separate layers (1, 4, 6 contralateral; 2, 3, 5 ipsilateral) and separates **M** (motion, flicker → parietal), **P** (detail, colour → temporal) and **K** (blue) channels. A lesion therefore produces a defect whose shape tells you exactly where it is.

> [!example]+ **📊 Clinical Pattern Recognition**
>
> Understanding how the condition progresses through stages helps you recognize it at different phases and predict outcomes.
>
> **Stage 1 - Normal Physiology:**
> Rods (100 million, rhodopsin, peripheral, night vision) and cones (5 million, iodopsin, foveola, colour) transduce light by hyperpolarisation; lateral inhibition sharpens contrast; Wald's cycle regenerates 11-cis retinal; melanopsin ganglion cells set the circadian clock (SCN) and drive the pupillary light reflex (pretectal → Edinger-Westphal).
>
> **Stage 2 - Compensated/Early Pathology:**
> Early vitamin A deficiency slows regeneration of 11-cis retinal, so rods recover slowly in dim light (night blindness) while cone vision is still normal. An inherited cone-pigment defect (red–green) is silent in daily life and found only on an Ishihara chart. A small pathway lesion causes a field defect the patient may not notice (a quadrant, a scotoma).
>
> **Stage 3 - Decompensated/Overt Disease:**
> Complete lesions give fixed defects that localise: optic nerve (one eye blind, no direct reflex in it), chiasma (bitemporal hemianopia), tract or radiation (homonymous defects), occipital cortex (homonymous hemianopia, macula often spared), inferior temporal cortex (prosopagnosia). A pretectal lesion abolishes the light reflex while near-response survives.
>
> **Progression Timeline:**
> Normal → trigger (vitamin A lack, X-linked cone defect, pituitary tumour, stroke) → subtle loss (night blindness, colour confusion, partial field cut) → full defect (hemianopia, blindness, prosopagnosia) → fixed disability
>
> **Why This Matters Clinically:**
> The shape of the field defect and the pupil responses localise the lesion before imaging; colour testing (Ishihara) screens occupations; vitamin A replacement reverses early night blindness but not late corneal damage.

> [!warning]+ **🔍 Diagnostic Buzzwords & Pattern Recognition**
>
> These are the key terms, phrases, and clinical patterns that should immediately trigger specific diagnoses in your mind. When you see these in a clinical vignette or real patient, you should think of the associated condition instantly.
>
> **Buzzwords by Condition:**
>
> **Phototransduction:** "Rhodopsin → transducin → phosphodiesterase → ↓ cGMP" → light closes the cGMP-gated Na⁺ channel and the rod hyperpolarises; the photoreceptor is the cell that hyperpolarises to its stimulus.
>
> **Night blindness:** "Vitamin A", "11-cis retinal", "Wald's cycle" → rhodopsin cannot be regenerated, rods fail first.
>
> **Red–green colour blindness:** "X-linked recessive", "males", "Ishihara", "protanopia / deuteranopia" → L or M cone pigment missing; tritanopia (blue) is the rare one.
>
> **Prosopagnosia:** "Cannot recognise faces, can recognise voices" → inferior temporal (fusiform) cortex lesion.
>
> **Pupillary light reflex:** "Afferent optic nerve, efferent oculomotor", "Edinger-Westphal", "direct and indirect" → light in one eye constricts both pupils because the pretectal fibres cross over.
>
> **Circadian rhythm:** "Melanopsin", "retinohypothalamic tract", "suprachiasmatic nucleus" → light-setting of the 24-hour clock by mGCs.
>
> **Visual/Imaging Buzzwords:**
> White stripe in the grey matter of the occipital pole = stria of Gennari (striate cortex, area 17); six curved layers = LGB; cytochrome-oxidase blobs = colour; an X at the base of the brain = optic chiasma.
>
> **Severity Indicators:**
> Numbers: rods 100 million, cones 5 million; RMP of rods −60 mV (page); LGB 6 layers (1, 2 M; 3–6 P; K between); contralateral 1, 4, 6 / ipsilateral 2, 3, 5; area 17 (with 18, 19); 4 orders of neurons.

> [!danger]+ **⚠️ Common Traps & Pitfalls**
>
> These are the mistakes that students and clinicians commonly make with this topic. Being aware of these traps helps you avoid diagnostic errors and answer tricky exam questions correctly.
>
> **Trap 1: "Light depolarises the photoreceptor"**
>
> **What students think:** Like every other receptor, the rod depolarises when stimulated.
>
> **Why this is wrong:** In the dark cGMP holds the Na⁺ channel open (dark current) and the rod is depolarised, releasing glutamate. Light activates transducin and phosphodiesterase, cGMP falls, the channel closes and K⁺ efflux hyperpolarises the cell, so glutamate release **falls**.
>
> **How to avoid this trap:** "Photoreceptors shout in the dark and go quiet in the light."
>
> **Trap 2: Thinking the bipolar cell fires action potentials**
>
> **What students think:** Every retinal neuron sends spikes.
>
> **Why this is wrong:** Photoreceptors, bipolar and horizontal cells use graded potentials over short distances; the **ganglion cell is the only retinal cell with an output axon and action potentials**, needed because the optic nerve is long.
>
> **How to avoid this trap:** "Ganglion = the only exit, the only spike."
>
> **Trap 3: Mixing up which LGB layers get which eye**
>
> **What students think:** The magnocellular layers get the ipsilateral eye, the parvocellular layers the contralateral.
>
> **Why this is wrong:** The rule cuts across M and P: layers **1, 4, 6 contralateral**, **2, 3, 5 ipsilateral**; layers 1–2 are M and 3–6 are P.
>
> **How to avoid this trap:** "1 + 4 + 6 = 11 → C/L (Cross); 2 + 3 + 5 = 10 → I/L."
>
> **Trap 4: Calling every colour defect X-linked**
>
> **What students think:** All three colour blindnesses are X-linked recessive.
>
> **Why this is wrong:** The L (red) and M (green) opsin genes are on the X chromosome, so protan and deutan defects are X-linked recessive and common in males. The S (blue) opsin gene is on chromosome 7: tritanopia is autosomal (dominant) and equally rare in both sexes.
>
> **How to avoid this trap:** "Red and green ride on X; blue is on 7."
>
> **Trap 5: Confusing direct and indirect light reflex lesions**
>
> **What students think:** If the left pupil does not constrict, the left optic nerve is damaged.
>
> **Why this is wrong:** An afferent (optic nerve) lesion abolishes both pupils' response to light in **that** eye but both still react to light in the other eye. An efferent (oculomotor) lesion leaves **that** pupil unreactive whichever eye is lit.
>
> **How to avoid this trap:** Ask "which eye was lit, which pupil moved?" — afferent fault = lit eye matters; efferent fault = pupil matters.

> [!tip]+ **🔗 Related Concepts & Cross-Topic Connections**
>
> Understanding how this topic connects to other areas of medicine deepens your knowledge and helps you see the bigger picture. These connections also help you answer integrated questions on exams.
>
> **Related Topic 1: [[Sensory Receptors]]**
> Rods and cones are receptors that hyperpolarise to their adequate stimulus — the exception to the depolarising receptor potential described there.
>
> **Related Topic 2: [[Somatosensory Pathways]]**
> General senses use four levels (including the spinal cord) and a thalamic relay (VPL); vision uses three levels with its own thalamic relay (LGB) and the same four-neuron logic.
>
> **Related Topic 3: [[Cardiac Action Potentials]]**
> The page links the "funny current" (HCN) channel of the retina to the SA node, where If drives pacemaker depolarisation and heart rate.
>
> **Related Topic 4: [[Limbic System and Hypothalamus]]**
> Melanopsin ganglion cells project through the retinohypothalamic tract to the suprachiasmatic nucleus, the master circadian clock.
>
> **Related Topic 5: [[Synaptic Transmission and Neurotransmitters]]**
> Glutamate is the photoreceptor and bipolar transmitter, acetylcholine (with GABA and glycine) the amacrine transmitters, and lateral inhibition is a synaptic circuit.
>
> **Clinical Integration:**
> Visual field testing, pupil examination, colour testing and dark adaptation are the bedside applications: a pituitary adenoma pressing on the chiasma, a stroke in the occipital lobe, vitamin A deficiency and congenital colour blindness are the classic cases.
>
> **Exam Integration:**
> Expect questions on rods vs cones, the cascade of phototransduction and the photoreceptor's hyperpolarisation, the seven retinal cells and which fires action potentials, LGB layers and M/P/K pathways, area 17 and stria of Gennari, prosopagnosia, types of colour blindness, the order of neurons and the light reflex arc.

---

## 🏆 Pearls (High-Yield Summary)

> [!success] Must-Know Pearls
> 1. Vision has **3 levels** (retina → thalamus → occipital cortex); general senses have **4** (add spinal cord).
> 2. **7 retinal cells:** rods, cones, bipolar, **ganglion**, horizontal, amacrine, **Müller (glial, supportive)**.
> 3. **Ganglion cell = only retinal cell with an output (optic nerve) and action potentials.**
> 4. **Rods:** dim light (night), 100 million, **rhodopsin (visual purple)**, peripheral retina. **Cones:** colour (day), 5 million, **iodopsin**, central retina; **foveola = only cones (rod-free)**.
> 5. **Lateral inhibition** by horizontal/amacrine cells → **↑ contrast & sharpness**.
> 6. **Melanopsin ganglion cells:** directly light-sensitive, PACAP; → **RHT → suprachiasmatic nucleus (circadian rhythm)** and → **pretectal → Edinger-Westphal (pupillary light reflex)**.
> 7. **Dark:** funny (cGMP) Na⁺ channel open → **depolarisation (−60 mV)** → **glutamate released**. **Light:** 11-cis → all-trans → **transducin → phosphodiesterase → ↓ cGMP** → channel closes → **hyperpolarisation → ↓ glutamate**.
> 8. **Wald's visual cycle** = 11-cis (dark) ⇄ all-trans (light) retinal; **HCN channels** in retina (vision) and SA node (HR), opened by cGMP; **amacrine** = purely depolarising, lateral inhibition, **ACh**.
> 9. Pathway: optic nerve (I/L nasal + temporal) → **chiasma (nasal fibres cross)** → tract (I/L temporal + C/L nasal) → **LGB** → radiation → cortex; defect depends on the lesion site.
> 10. **LGB: 6 layers** — **M (1, 2; flicker, extraocular movements)**, **P (3–6; colour, fine detail)**, **K (between; blue)**; M and P end in **layer 4**; **1, 4, 6 contralateral, 2, 3, 5 ipsilateral**.
> 11. Visual cortex = **calcarine cortex, area 17 (18, 19)**, heavily myelinated, **stria of Gennari (striate cortex)**; simple/complex cells = feature detectors; **blobs = colour, cytochrome oxidase**.
> 12. Extrastriate: **parietal ← M (eye movements)**, **temporal ← P (colour)**; **inferior temporal cortex lesion → prosopagnosia**.
> 13. Colour pathway: **cones → parvocellular → blobs**; **L red, M green, S blue**; colour blindness **X-linked recessive, males, m/c red–green**; **protanopia (red), deuteranopia (green), tritanopia (blue)**.
> 14. Order: **photoreceptor 1st, bipolar 2nd, ganglion 3rd, LGB 4th**. Light reflex: **afferent optic nerve → pretectal → Edinger-Westphal (centre) → efferent oculomotor → ciliary ganglion → sphincter pupillae**; direct + indirect.

---

## 🔁 One-Line Recall

```
3 LEVELS: retina → thalamus (LGB) → occipital cortex · 7 retinal cells · GANGLION = only output + only AP
RODS: dim/night · 100 M · rhodopsin · periphery    CONES: colour/day · 5 M · iodopsin · foveola (rod-free)
DARK: cGMP → Na⁺ open → depolarised → glutamate ↑   LIGHT: all-trans → transducin → PDE → ↓cGMP → hyperpolarised → glutamate ↓
mGC: melanopsin + PACAP → SCN (circadian) · pretectal → Edinger-Westphal (light reflex)
PATHWAY: nerve → CHIASMA (nasal cross) → tract → LGB 6 layers (M 1-2 · P 3-6 · K) · C/L 1,4,6 · I/L 2,3,5 → radiation → AREA 17
CORTEX: calcarine · stria of Gennari · simple/complex = feature detectors · blobs = colour · IT lesion = prosopagnosia
COLOUR: L red · M green · S blue · X-linked · protan / deutan / tritan · LIGHT REFLEX: II in → pretectal → EW → III out → ciliary ganglion → sphincter
```

---

## 🎬 Video Library

| What to watch | Link |
|---|---|
| Phototransduction in rods (YouTube search) | https://www.youtube.com/results?search_query=phototransduction+rods+animation |
| Retina — cell layers (YouTube search) | https://www.youtube.com/results?search_query=retina+layers+cells+physiology+lecture |
| Visual pathway and its defects — optic nerve, chiasm, tract, lateral geniculate body | https://www.youtube.com/watch?v=7YCl0C5cCcU |
| Visual field defects and optic nerve pathway | https://www.youtube.com/watch?v=2ZbFBlwWm3Q |
| Colour vision and colour blindness (YouTube search) | https://www.youtube.com/results?search_query=colour+vision+cones+colour+blindness+physiology |
| Pupillary light reflex pathway (YouTube search) | https://www.youtube.com/results?search_query=pupillary+light+reflex+pathway |

---

## 🖼 Infographic Prompt — One-Page Summary

> [!abstract]- 🎨 Prompt for an image generator (copy everything inside)
> "Design a single-page, portrait A4 medical study infographic titled **'VISION'** for a postgraduate physiology exam. Flat-vector textbook style, off-white background; colour code used everywhere: dark blue = dark state and rods, yellow = light, red/green/blue = the three cone types, purple = thalamus and cortex. Thin icons, crisp legible text, generous white space. Seven panels:
>
> **Panel 1 — 'Organisation of vision'.** A brain seen from below with eyes, optic pathway and occipital pole: 'retina → thalamus → occipital visual cortex = 3 levels; general senses = 4 levels (include spinal cord)'.
>
> **Panel 2 — 'Retina'.** A vertical retina section with light arrow coming from below through ganglion → amacrine → bipolar → horizontal → rods and cones against the back of the eye, Müller cell spanning it. Mini-table of 7 cells: rods (rod shaped), cones (cone shaped), bipolar (2 poles: receive / conduct), ganglion (only output → optic nerve → thalamus; only action potential), horizontal (connects cones & rods), amacrine (connects bipolar to ganglion), Müller (retinal glial, supportive). Rods vs cones table: dim light/night vs colour/day; 100 million vs 5 million; rhodopsin (visual purple) vs iodopsin; peripheral retina vs central retina and foveola (only cones). A small L–C–L diagram 'lateral inhibition by horizontal/amacrine → ↑ contrast & sharpness'. A tag 'melanopsin ganglion cells — PACAP → RHT → suprachiasmatic nucleus (24 h circadian rhythm); → pretectal → Edinger-Westphal (pupillary light reflex)'.
>
> **Panel 3 — 'Phototransduction'.** Two side-by-side rods: DARK — cGMP-dependent funny Na⁺ channel open, Na⁺ influx, depolarisation, K⁺ efflux keeps RMP −60 mV, glutamate released; LIGHT — 11-cis retinal → all-trans retinal → transducin (+) → phosphodiesterase (+) → degrades cGMP → Na⁺ channel closed, K⁺ efflux → hyperpolarisation → ↓ glutamate. A circular arrow 'Wald's visual cycle: 11-cis (dark) ⇄ all-trans (light)'. Side notes: 'HCN channels: Na⁺, retina (vision) and SA node (HR), opened by cGMP'; 'amacrine: purely depolarising, lateral inhibition, ACh'.
>
> **Panel 4 — 'Visual pathway & LGB'.** Both eyes with temporal and nasal fields; optic nerve (I/L nasal + temporal) → optic chiasma (nasal fibres cross) → optic tract (I/L temporal + C/L nasal) → lateral geniculate body → optic radiation → visual cortex; caption 'defect depends on the lesion site'. A six-layer LGB: layers 1–2 magnocellular (big; flicker, extraocular movements), 3–6 parvocellular (small; colour, fine detail), koniocellular between (blue); M and P → layer 4 of visual cortex; layers 1, 4, 6 contralateral eye, 2, 3, 5 ipsilateral eye.
>
> **Panel 5 — 'Visual cortex'.** Occipital pole with the calcarine cortex, 'Brodmann 17, 18, 19 · heavily myelinated · stria of Gennari = striate cortex'. Three cell icons: simple cell and complex cell 'higher-order processing, feature detectors', blobs 'colour vision, cytochrome oxidase'. Extrastriate arrows: parietal lobe ← magnocellular (eyeball movements), temporal lobe ← parvocellular (colour vision); inferior temporal cortex 'face recognition — lesion: prosopagnosia'.
>
> **Panel 6 — 'Colour vision'.** Pathway 'cones → parvocellular → blobs'; three cone icons L (long, red), M (medium, green), S (short, blue); an Ishihara plate; a table red–protanopia, green–deuteranopia, blue–tritanopia; caption 'X-linked recessive, males > females (carriers), most common red–green'.
>
> **Panel 7 — 'Order of neurons & light reflex'.** A chain photoreceptor (1st) → bipolar (2nd) → ganglion (3rd) → LGB (4th) → radiation → cortex. A light-reflex loop: light into the right eye → optic nerve (afferent) → pretectal nucleus → cross over → Edinger-Westphal nucleus (centre) → oculomotor nerve (efferent) → ciliary ganglion → sphincter pupillae → both pupils constrict (direct in the lit eye, indirect in the other).
>
> Footer strip: 'Dark = depolarised · light = hyperpolarised · ganglion = only spike · nasal fibres cross · LGB 1-4-6 contralateral'. No watermark, no photographs, illustration quality."

---

## 📚 References

- Physiology main notes (Marrow 8) — *Vision*, pp. 83–88
- Guyton & Hall Textbook of Medical Physiology — The eye: receptor and neural function of the retina; central neurophysiology of vision
- Ganong's Review of Medical Physiology — Vision
- Kandel, *Principles of Neural Science* — The retina; intermediate-level visual processing
- Page crops: `Vision - ….png` files in `attachments/` are crops of the handwritten pages (no free web image could be confirmed for these figures in this run)

[^1]: Photoreceptors, horizontal and bipolar cells work by graded (electrotonic) potentials, which are enough over the few hundred micrometres of the retina; the ganglion cell axons must travel ~5 cm to the LGB, so they need action potentials. (Some amacrine cells also spike.)
[^2]: This "inverted" retina is why the fovea is a pit: the inner layers are pushed aside at the foveola so light reaches the cones with the least scattering — the point of sharpest vision.
[^3]: Textbook figures vary: Ganong ~120 million rods and ~6 million cones per eye; Guyton ~100 million rods and 3 million cones. The page's 100 million / 5 million is kept in the body.
[^4]: Melanopsin ganglion cells are the "intrinsically photosensitive retinal ganglion cells" (ipRGCs), about 1–2 % of ganglion cells; they use glutamate and PACAP as co-transmitters onto the suprachiasmatic nucleus. They work even in people who have lost all rods and cones, so their circadian entrainment and pupil reflex can survive "blindness".
[^5]: Guyton gives the rod membrane potential in the dark as about **−40 mV** (because of the dark current of Na⁺), hyperpolarising to **−70 to −80 mV** in bright light. The page's −60 mV is kept in the body.
[^6]: In standard texts the channel that cGMP opens in the rod **outer segment** is the cyclic-nucleotide-gated (CNG) cation channel. **HCN** channels (hyperpolarisation-activated cyclic-nucleotide-gated) carry the "funny" current *I*f: in the SA node they open on hyperpolarisation and are modulated by cAMP, producing pacemaker depolarisation; photoreceptor inner segments also have HCN channels (*I*h) that shape their light responses. The page treats the two as one "funny current channel".
[^7]: There are some 30 types of amacrine cell; most use GABA or glycine, and the "starburst" amacrines release acetylcholine (with GABA). Several types do fire action potentials. The page's "purely depolarising" and "ACh" are kept as written.
[^8]: Classic lesions: optic nerve → blindness of that eye; chiasma (e.g. pituitary adenoma) → bitemporal hemianopia; optic tract → contralateral homonymous hemianopia; Meyer's loop (temporal radiation) → contralateral superior quadrantanopia ("pie in the sky"); parietal radiation → inferior quadrantanopia; occipital cortex → contralateral homonymous hemianopia with macular sparing.
[^9]: Mnemonic: the contralateral layers add up to 1 + 4 + 6 = 11 and the ipsilateral to 2 + 3 + 5 = 10. The two eyes' inputs first meet in the cortex (binocular cells), not in the LGB.
[^10]: Strictly, **area 17** is the primary visual (striate) cortex, V1, in the walls of the calcarine sulcus; **areas 18 and 19** surrounding it are visual association (extrastriate) cortex. The page lists all three under "visual cortex".
[^11]: David Hubel and Torsten Wiesel (Nobel Prize 1981) described simple cells (respond to a bar of light at a specific orientation and position) and complex cells (same orientation anywhere in a larger field, often direction-selective). Blobs are cytochrome-oxidase-rich patches in layers 2–3 of V1, rich in colour-opponent cells.
[^12]: Face recognition depends on the fusiform face area on the inferior (ventral) surface of the temporal–occipital cortex; bilateral lesions there cause prosopagnosia. Patients still recognise people by voice or gait.
[^13]: Textbooks call the S cone the **short**-wavelength cone. Peak sensitivities: S ~420–445 nm (blue), M ~530–535 nm (green), L ~560–565 nm (red). The trichromatic theory is Young–Helmholtz.
[^14]: Red–green defects affect about 8 % of males and 0.5 % of females because the L and M opsin genes are on the X chromosome; the commonest form is **deuteranomaly** (weak green). The S (blue) opsin gene lies on chromosome 7, so **tritanopia is autosomal** (dominant) and rare — the page's "X-linked recessive" applies to red and green defects.
[^15]: Some textbooks count the bipolar cell as the 1st order neuron (treating rods and cones as receptor cells), which makes the ganglion cell 2nd order and the LGB neuron 3rd. The page counts the photoreceptor as the 1st order neuron, giving four orders.
[^16]: The pretectal neurons project to **both** Edinger–Westphal nuclei (crossing in the posterior commissure), and EW sends preganglionic parasympathetic fibres in the oculomotor nerve to the ciliary ganglion; short ciliary nerves then supply the sphincter pupillae. In the **Argyll Robertson pupil** (pretectal lesion, classically neurosyphilis) the light reflex is lost but the near (accommodation) reflex is kept.
[^ety-retina]: **retina** — Medieval Latin, probably from *rete*, "net" → the net-like inner coat of the eye (its blood vessels look like a net). **Differentiate:** *retina* (light-sensitive layer) · *choroid* (vascular layer) · *sclera* (Greek *sklēros*, hard — the white outer coat).
[^ety-occipital]: **occipital** — Latin *ob-*, "against, at the back" + *caput*, "head" + *-al* → of the back of the head; the occipital lobe holds the visual cortex.
[^ety-bipolar]: **bipolar** — Latin *bi-*, "two" + *polus*, "end of an axis, pole" + *-ar* → having two poles (a dendrite end and an axon end). **Differentiate:** *unipolar / pseudounipolar* (one process — dorsal root ganglion) · *bipolar* (retina, olfactory, spiral ganglion) · *multipolar* (most CNS neurons, motor neurons).
[^ety-ganglion]: **ganglion** — Greek *ganglion*, "a knot, a swelling" → a knot of nerve-cell bodies; in the retina the name is kept for the innermost layer of neurons, although it lies inside the CNS.
[^ety-amacrine]: **amacrine** — Greek *a-*, "without" + *makros*, "long" + *is, inos*, "fibre" → "without a long fibre": these cells have no axon, only dendrites. Named by Santiago Ramón y Cajal.
[^ety-muller-cell]: **Müller cell** — Heinrich Müller (1820–1864), German anatomist at Würzburg, who described these radial glial cells of the retina in 1851. Not the same person as Johannes Müller of the "law of specific nerve energies".
[^ety-glia]: **glia / glial** — Greek *glia*, "glue" → the "nerve glue", supporting cells of the nervous system (Rudolf Virchow, 1856). **Differentiate:** *astrocytes*, *oligodendrocytes*, *microglia*, *ependyma* (CNS); *Schwann cells* (PNS); *Müller cells* (retina).
[^ety-photoreceptor]: **photoreceptor** — Greek *phōs, phōtos*, "light" + Latin *receptor*, "receiver" (*re-* + *capere*, to take) → a light receiver: rods and cones.
[^ety-rhodopsin]: **rhodopsin** — Greek *rhodon*, "rose" + *opsis*, "sight" + *-in* → "rose-coloured visual pigment" (also called *visual purple*), named by Willy Kühne (1878). **Differentiate:** *rhodopsin* (rods) · *iodopsin / photopsins* (cones) · *melanopsin* (ipRGCs).
[^ety-iodopsin]: **iodopsin** — Greek *ion*, "violet" + *opsis*, "sight" + *-in* → "violet visual pigment", the old name for the cone pigments (George Wald, 1937). Nothing to do with *iodine* — both share the Greek *ion*, "violet".
[^ety-fovea]: **fovea / foveola** — Latin *fovea*, "small pit" + *-ola*, diminutive → the pit of sharpest vision and the tiny rod-free pit at its centre. Part of the *macula lutea* (Latin, "yellow spot").
[^ety-inhibition]: **inhibition** — Latin *in-*, "in, on" + *habere*, "to hold" + *-ition* → holding in, restraining. **Differentiate:** *lateral inhibition* (neighbours suppressed → contrast) · *presynaptic inhibition* (less transmitter released) · *feedback inhibition* (output suppresses its own source).
[^ety-melanopsin]: **melanopsin** — Greek *melas, melanos*, "black, dark" + *opsis*, "sight" + *-in* → first found in the dark pigment cells (melanophores) of frog skin (Provencio, 1998); in humans the pigment of ipRGCs.
[^ety-pacap]: **PACAP** — *pituitary adenylate cyclase activating polypeptide*: Latin *pituita*, "phlegm" (the gland was thought to drain mucus to the nose) + *adenylate cyclase*, the enzyme that makes cAMP (*cyclase*, "ring-maker") + Greek *poly-*, "many" + *peptide* (*peptos*, digested) → a peptide first found because it activates cAMP production in pituitary cells.
[^ety-suprachiasmatic]: **suprachiasmatic** — Latin *supra-*, "above" + Greek *chiasma*, "a cross-shaped mark" + *-tic* → the nucleus lying just above the optic chiasma; the master circadian clock of the hypothalamus.
[^ety-circadian]: **circadian** — Latin *circa*, "about" + *dies*, "day" + *-an* → about a day long; coined by Franz Halberg (1959). **Differentiate:** *circadian* (~24 h) · *ultradian* (shorter, e.g. sleep cycles) · *infradian* (longer, e.g. menstrual cycle).
[^ety-pretectal]: **pretectal** — Latin *prae-*, "in front of" + *tectum*, "roof" + *-al* → in front of the tectum (roof) of the midbrain; the pretectal nuclei relay the light reflex. *Tectospinal* tract starts in the tectum (superior colliculus).
[^ety-edinger-westphal]: **Edinger–Westphal nucleus** — Ludwig Edinger (1855–1918), German neuroanatomist (1885), and Carl Friedrich Otto Westphal (1833–1890), German neurologist-psychiatrist (1887), who described this parasympathetic part of the oculomotor nucleus.
[^ety-phototransduction]: **phototransduction** — Greek *phōs*, "light" + Latin *trans-*, "across" + *ducere*, "to lead" + *-tion* → leading light across into another form: converting a photon into an electrical signal. **Differentiate:** *transduction* (stimulus → electrical signal at a receptor) · *transmission* (signal across a synapse) · *transformation* (change of form, e.g. of cells).
[^ety-depolarization]: **depolarization** — Latin *de-*, "away, removal" + *polus*, "pole" + *-ization*, the process → removing the polarity (membrane becomes less negative). **Differentiate:** *depolarisation* (toward 0) · *repolarisation* (*re-*, back — returning to rest) · *hyperpolarisation* (*hyper-*, beyond — more negative than rest).
[^ety-glutamate]: **glutamate** — Latin *gluten*, "glue" + *-amate* (amino acid salt) → first isolated from wheat gluten (Ritthausen, 1866); the main excitatory neurotransmitter of the CNS and retina.
[^ety-transducin]: **transducin** — Latin *transducere*, "to lead across" + *-in*, protein → the G protein (Gt) that carries the signal from light-activated rhodopsin to phosphodiesterase.
[^ety-phosphodiesterase]: **phosphodiesterase** — *phospho-* (phosphate) + *di-*, "two" + *ester* + *-ase*, enzyme → an enzyme that splits one of the two ester bonds of a cyclic nucleotide, turning cGMP into 5′-GMP. The rod enzyme is PDE6 (sildenafil inhibits PDE5 and slightly PDE6 — hence its blue-tinged vision side effect).
[^ety-hyperpolarisation]: **hyperpolarisation** — Greek *hyper-*, "over, beyond" + *polus*, "pole" + *-isation* → making the membrane more polarised (more negative) than at rest; the photoreceptor's response to light.
[^ety-wald]: **Wald's visual cycle** — George Wald (1906–1997), American biochemist at Harvard, Nobel Prize 1967 (with Granit and Hartline) for showing that vitamin A (retinal) is the chromophore of rhodopsin and that light isomerises 11-cis to all-trans retinal.
[^ety-hcn]: **HCN channel** — *hyperpolarisation-activated cyclic nucleotide-gated* channel: Greek *hyper-* "beyond" + *polus* "pole"; Greek *kyklos* "ring" + *nucleotide* (Latin *nucleus*, kernel) → a channel opened by hyperpolarisation and modulated by a ring-shaped nucleotide (cAMP/cGMP). Its current is called "funny" (*I*f) because, unlike most currents, it is activated by hyperpolarisation.
[^ety-acetylcholine]: **acetylcholine** — Latin *acetum*, "vinegar" (acetyl group) + Greek *cholē*, "bile" + *-ine* → choline was first isolated from bile (Strecker, 1862); acetylcholine was the first neurotransmitter identified (Otto Loewi, 1921).
[^ety-chiasma]: **chiasma / chiasm** — Greek *chiasma*, "a cross-shaped mark", from the letter *chi* (X) → the X-shaped crossing of the optic nerves where the nasal fibres decussate. **Differentiate:** *chiasma* (partial crossing — only nasal fibres) · *decussation* (complete crossing of a tract) · *commissure* (links identical areas of both sides).
[^ety-geniculate]: **geniculate** — Latin *geniculum*, "little knee" (*genu*, knee) + *-ate* → bent like a knee; the lateral geniculate body is knee-shaped. *Medial* geniculate body = hearing.
[^ety-ipsilateral]: **ipsilateral / contralateral** — Latin *ipse*, "same" / *contra*, "opposite" + *latus*, "side" → on the same side / on the opposite side; abbreviated I/L and C/L on the page.
[^ety-magnocellular]: **magnocellular / parvocellular / koniocellular** — Latin *magnus*, "large" / *parvus*, "small" + *cellula*, "small room, cell" + *-ar*; Greek *konis*, "dust" → large-celled, small-celled and "dust-like" (very small) cells of the LGB.
[^ety-calcarine]: **calcarine** — Latin *calcar*, "spur" (*calx*, heel) + *-ine* → spur-shaped; the calcarine sulcus raises a spur (calcar avis, "bird's spur") in the posterior horn of the lateral ventricle. The page writes "calcrine".
[^ety-brodmann]: **Brodmann areas** — Korbinian Brodmann (1868–1918), German neurologist, who divided the cortex into 52 numbered areas by cell structure (1909); area 17 = primary visual, 18–19 = visual association. The page spells "Brodman's".
[^ety-gennari]: **stria of Gennari** — Francesco Gennari (1752–1797), Italian medical student and anatomist at Parma, who saw this white line in the occipital cortex in 1776 (published 1782). The page spells "Gennasi".
[^ety-striate]: **striate** — Latin *stria*, "a furrow, a stripe" + *-ate*, "having" → striped; the primary visual cortex is the *striate cortex* because the stria of Gennari is visible to the naked eye. Not the same as *corpus striatum* (basal ganglia), which is striped by fibre bundles.
[^ety-cytochrome]: **cytochrome oxidase** — Greek *kytos*, "cell" + *chrōma*, "colour" (coloured cell pigments) + *oxidase*, an enzyme that oxidises → complex IV of the respiratory chain; staining for it reveals the blobs of V1.
[^ety-prosopagnosia]: **prosopagnosia** — Greek *prosōpon*, "face" + *a-*, "without" + *gnōsis*, "recognition" + *-ia* → inability to recognise faces; coined by Joachim Bodamer (1947). **Differentiate:** *prosopagnosia* (faces) · *visual agnosia* (objects) · *alexia* (written words) · *achromatopsia* (colour, cortical).
[^ety-trichromacy]: **trichromacy** — Greek *tri-*, "three" + *chrōma*, "colour" + *-cy* → three-colour vision with L, M and S cones (Young–Helmholtz trichromatic theory, 1802/1850s).
[^ety-x-linked]: **X-linked** — the gene lies on the **X chromosome** (named "X" by Hermann Henking, 1891, because its nature was unknown). Males (XY) have one X, so a single recessive allele shows; females (XX) are usually carriers.
[^ety-recessive]: **recessive** — Latin *re-*, "back" + *cedere*, "to go" + *-ive* → "going back, receding": the allele hides when a normal allele is present. Opposite *dominant* (Latin *dominari*, to rule). Terms from Gregor Mendel (1866).
[^ety-protanopia]: **protanopia / deuteranopia / tritanopia** — Greek *prōtos* "first", *deuteros* "second", *tritos* "third" + *an-* "without" + *ōps* "eye, sight" + *-ia* → blindness for the first (red, L), second (green, M) or third (blue, S) primary colour. **Differentiate:** *-anopia* (pigment absent) · *-anomaly* (pigment shifted, weaker: protanomaly, deuteranomaly).
[^ety-oculomotor]: **oculomotor** — Latin *oculus*, "eye" + *motor*, "mover" (*movere*, to move) → the eye-mover; cranial nerve III carries the efferent (parasympathetic) limb of the light reflex.
[^ety-ciliary]: **ciliary** — Latin *cilium*, "eyelash, eyelid" + *-ary* → "eyelash-like"; the ciliary body's folds were likened to eyelashes. The ciliary ganglion relays parasympathetic fibres to the sphincter pupillae and ciliary muscle.
[^ety-sphincter-pupillae]: **sphincter pupillae** — Greek *sphinktēr*, "a band, that which binds tight" (*sphingein*, to bind) + Latin *pupilla*, "little doll" (the tiny reflection of oneself seen in another's pupil) → the ring muscle that constricts the pupil (miosis). Its opponent, *dilator pupillae*, is sympathetic.
[^ety-consensual]: **consensual** — Latin *con-*, "together" + *sentire*, "to feel" + *-al* → "feeling together": the other pupil reacts along with the lit one (= indirect light reflex on the page).
[^pre-bi]: **bi-** — two (Latin): bipolar, bilateral, biconvex. Don't confuse with **di-** two (Greek: diester) · **dis-** apart · **bio-** life.
[^pre-a]: **a- / an-** — without, not: amacrine, anopia (protanopia), agnosia. Don't confuse with **ab-** away from (abduction) · **ad-** towards (afferent) · **ana-** up, again (anabolism).
[^pre-photo]: **photo-** — light: photoreceptor, phototransduction, photopic (cone) vision. Don't confuse with **phono-** sound · **phospho-** phosphate (phosphodiesterase) · **phobo-** fear (photophobia combines two).
[^suf-opsin]: **-opsin / -opsia / -opia** — sight, vision: rhodopsin, melanopsin, iodopsin; achromatopsia; protanopia, myopia. Don't confuse with **-opsy** examination (biopsy) · **-ops** in *Cyclops* (eye/face).
[^suf-ola]: **-ola / -ole / -ule** — small (Latin diminutive): foveola, arteriole, venule. Don't confuse with **-ol** an alcohol (retinol) · **-oma** a tumour.
[^pre-in]: **in- (im-)** — in, on, into: inhibition, influx, input. Don't confuse with the other **in-** not (insensitive) · **intra-** within · **infra-** below.
[^pre-supra]: **supra-** — above: suprachiasmatic, supraoptic, suprarenal. Don't confuse with **super-** above, excess (superior colliculus) · **sub-** below · **hyper-** over (Greek).
[^pre-circa]: **circa- / circum-** — around, about: circadian, circumference, circumcision. Don't confuse with **cyclo-** circle (Greek: cyclic nucleotide) · **cirrh-** yellow-tawny (cirrhosis).
[^pre-pre]: **pre- / prae-** — before, in front: pretectal, premotor, preganglionic. Don't confuse with **pro-** forward, favouring · **post-** after · **peri-** around.
[^pre-trans]: **trans-** — across, through, beyond: phototransduction, all-trans retinal, transducin. Don't confuse with **cis-** on this side (11-cis retinal) · **inter-** between · **dia-** through (Greek: dialysis).
[^pre-cis]: **cis-** — on this side, on the same side: 11-cis retinal (both chain parts on the same side of the double bond). Don't confuse with **trans-** across, the opposite side (all-trans retinal) · **cyst-** bladder, sac.
[^pre-de]: **de-** — away, removal, reversal: depolarisation, degeneration, decussation (unrelated — *decem*, ten). Don't confuse with **dis-** apart · **di-** two · **dys-** bad, abnormal.
[^suf-in]: **-in / -ine** — a substance, often a protein or chemical: transducin, rhodopsin, melanopsin, glutamine, acetylcholine. Don't confuse with **-ase** an enzyme (phosphodiesterase) · **-itis** inflammation.
[^suf-ase]: **-ase** — an enzyme: phosphodiesterase, oxidase, adenylate cyclase. Don't confuse with **-ose** a sugar (glucose) · **-ate** a salt or "having" (glutamate, striate).
[^pre-hyper]: **hyper-** — over, beyond, excessive: hyperpolarisation, hyperacusis. Don't confuse with **hypo-** under · **hyper-** has a Latin twin **super- / supra-**.
[^pre-ipsi]: **ipsi-** — same, self: ipsilateral (I/L). Don't confuse with **iso-** equal · **idio-** one's own (idiopathic).
[^pre-contra]: **contra-** — against, opposite: contralateral (C/L), contraindication. Don't confuse with **con-** together · **counter-** against (countercurrent).
[^pre-magno]: **magno- / magni-** — large: magnocellular, magnify. Don't confuse with **mega- / macro-** large (Greek: macula is a different word — Latin, "spot") · **micro-** small.
[^pre-parvo]: **parvo-** — small: parvocellular, parvovirus. Don't confuse with **par-** equal or beside (paraesthesia) · **pauci-** few.
[^pre-konio]: **konio- / conio-** — dust: koniocellular, pneumoconiosis (dust lung). Don't confuse with **cono-** cone (conus) · **kino-** movement (kinocilium).
[^pre-extra]: **extra-** — outside, beyond: extraocular, extrastriate, extrapyramidal. Don't confuse with **exo-** outside (Greek) · **ecto-** outer · **intra-** within.
[^suf-ate]: **-ate** — having, characterised by (adjectives) or a salt (nouns): striate, geniculate; glutamate. Don't confuse with **-ase** an enzyme · **-ite** another salt ending (nitrite vs nitrate).
[^suf-gnosia]: **-gnosia / -gnosis** — knowledge, recognition: prosopagnosia, agnosia, stereognosis, diagnosis. Don't confuse with **-genesis** formation · **-gnathia** jaw (prognathia).
[^pre-proto]: **proto- / prot-** — first: protanopia (first cone, red), protein, protoplasm. Don't confuse with **pro-** before, forward · **pros-** toward (prosopagnosia is *prosōpon*, face).
[^suf-anopia]: **-anopia / -anopsia** — absence of vision (*an-* without + *ōps* eye): protanopia, hemianopia, quadrantanopia. Don't confuse with **-opia** a vision state (myopia, presbyopia) · **-anomaly** a shifted, weaker form (deuteranomaly).
[^pre-deutero]: **deutero- / deuter-** — second: deuteranopia (second cone, green), deuterium. Don't confuse with **di- / bi-** two · **dextro-** right.
[^pre-trito]: **trito-** — third: tritanopia (third cone, blue). Don't confuse with **tri-** three (trichromacy) · **tropo-** turning.
