---
title: Membrane Transport
aliases: [Membrane transport, Passive and active transport, Na-K ATPase, Vesicular transport, Fick's law]
rank: 6
status: not-started
topic: Physiology
subtopic: General Physiology
chapter: 6
pages: "30–34"
target_exams:
  - NEET PG
  - INI-CET
  - FMGE
past_exam_questions: []
anki_link: ""
case_files: []
difficulty: medium
high_yield: true
guideline_criteria: "Fick's law of simple diffusion"
source: "Physiology main notes (Marrow 8) — Membrane Transport, pp. 30–34 (sections: Passive Transport 00:04:33 · Active Transport 00:18:46)"
mindmap: "[[Membrane Transport — Mind Map]]"
index: "[[Physiology — Index]]"
review_day_2: false
review_day_4: false
review_day_7: false
review_day_10: false
review_day_15: false
---
# 🚪 Membrane Transport

> [!abstract] Core Definition
> **Membrane transport**[^ety-transport][^pre-trans] is how substances cross the cell membrane. One question sorts every mechanism — **is ATP used?**
> - ✅ **ATP absent → passive**[^ety-passive] **transport** — **high conc. → low conc.** (downhill): simple, facilitated, non-ionic and osmotic diffusion.
> - ✅ **ATP present → active transport** — **low conc. → high conc.** (uphill): primary, secondary and vesicular transport.

---

## 🧠 Mental Model — Water, Pumps and Delivery Trucks

Passive transport is **water running downhill** — it needs no energy, only a slope (the concentration gradient) and an open path (lipid bilayer, carrier or channel). Active transport is a **pump lifting water uphill** — it burns fuel (ATP), either directly (primary) or by borrowing the slope another pump created (secondary). Vesicular transport is a **delivery truck** — cargo is packed in a membrane bag and driven in or out, whatever the gradient.

```
PASSIVE  (no ATP, high → low)  simple (bilayer, Fick's law) · facilitated (carrier: GLUT, aquaporin) · non-ionic · osmotic (water)
ACTIVE   (ATP,   low → high)   PRIMARY   — pump has its own ATPase: Na⁺-K⁺ (3:2), H⁺-K⁺, Ca²⁺
                               SECONDARY — rides the Na⁺ gradient: symport (SGLT, Na⁺-K⁺-2Cl⁻, Na⁺-I⁻) · antiport (Cl⁻-HCO3⁻)
                               VESICULAR — vesicles, Ca²⁺ + SNARE: exocytosis · endocytosis · transcytosis
SATURATION KINETICS: carrier / pump → plateau     ·     simple diffusion → straight line, no saturation
```

---

## ⚡ ATP and the Classification of Transport

![[Membrane Transport - structure of ATP.png]]
*ATP — a **nitrogenous base** (adenine) + a **ribose sugar** + **three phosphate groups**; the last two phosphate links are the **high-energy bonds** that transport pumps break (cropped from the handwritten page).*

**ATP**[^ety-atp][^pre-tri] = adenine (nitrogenous[^ety-nitrogen] base) + **ribose**[^ety-ribose][^suf-ose] **sugar** + **three phosphate groups** (high-energy bonds).

**Awarded Nobel prize for ATP discovery:**[^1]
- **Boyer**[^ety-boyer-walker]
- **Walker**
- **Jens Skou**[^ety-skou]

**Classification:**

![[Membrane Transport - passive and active transport classification.png]]
*Passive transport — **simple diffusion** straight through the lipid bilayer and **facilitated diffusion** through a carrier protein or a channel protein, both from high to low concentration — versus **active transport**, a carrier that uses ATP → ADP + Pi to move the substance from low to high concentration (cropped from the handwritten page).*

**Based on ATP requirement:**

```
                                   ATP
                ┌───────────────────┴───────────────────┐
             Absent                                   Present
                ↓                                        ↓
        Passive transport                        Active transport
       (High conc. → Low conc.)                 (Low conc. → High conc.)
   ┌──────────┬──────┴─────┬───────────┐        ┌────────┼─────────┐
 Simple   Facilitated  Non-ionic    Osmotic   Primary  Secondary  Vesicular
diffusion  diffusion   diffusion   diffusion                          │
          (Carrier                                     ┌──────────────┼──────────────┐
          protein +)                               Exocytosis    Endocytosis   Transcytosis
```

- **ATP absent → Passive transport (high conc. → low conc.):** **simple diffusion**[^ety-diffusion][^pre-dis] · **facilitated**[^ety-facilitated] **diffusion (carrier protein +)** · **non-ionic diffusion** · **osmotic**[^ety-osmosis][^suf-osis] **diffusion**.
- **ATP present → Active transport (low conc. → high conc.):** **primary** · **secondary** · **vesicular**[^ety-vesicle][^suf-cle] → **exocytosis**[^ety-cytosis][^pre-exo] · **endocytosis**[^pre-endo] · **transcytosis**.

---

## ⬇️ Passive Transport

### Simple diffusion

- **Along concentration gradient**[^ety-gradient].
- **Without utilizing ATP.**

![[Membrane Transport - simple diffusion.png]]
*Simple diffusion — molecules pass straight through the lipid bilayer (hydrophilic heads, hydrophobic tails) from high to low concentration; the rate depends on the membrane's **area** and **thickness** (cropped from the handwritten page).*

**Factors affecting transport:**

**Membrane — Fick's law**[^ety-fick] **of simple diffusion:**

| Factor | Relation to diffusion (D) |
|---|---|
| **Concentration gradient (CG)** | D ∝ CG |
| **Surface area (A)** | D ∝ A |
| **Thickness (T)** | D ∝ 1 / T |

```latex
D \;\propto\; \frac{\text{Concentration gradient (CG)} \times \text{Surface area (A)}}{\text{Thickness (T)}}
```

**Substance:**

| Factor | Relation to diffusion (D) |
|---|---|
| **Solubility** (lipid soluble — eg: **O₂ diffusion across lung alveoli**[^ety-alveolus][^suf-olus]) | D ∝ solubility |
| **Size** | D ∝ 1 / size |

🧠 Fick's law in one breath: diffusion is **faster down a steeper slope, over a bigger area, through a thinner wall, for a smaller and more fat-soluble molecule**.[^2]

**Clinical application:**
- **Emphysema**[^ety-emphysema][^pre-en]: **↓ surface area of membrane → ↓ diffusion of gases.**
- **Pulmonary**[^ety-pulmonary] **fibrosis**[^ety-fibrosis]: due to fibrosis → **↑ thickness of membrane → ↓ diffusion of gases.**[^3]

### Facilitated diffusion

- Through **carrier protein**:
  - **Glucose transporter (GLUT)**: transports glucose.
  - **Aquaporin**[^ety-aquaporin]: transports water.[^4]
- **Along concentration gradient.**
- **Without utilizing ATP.**

![[Membrane Transport - facilitated diffusion.png]]
*Facilitated diffusion — substances that cannot cross the bilayer pass through a **carrier protein** (left, changes shape) or a **channel protein** (right, an open pore), still from high to low concentration and without ATP (cropped from the handwritten page).*

### Non-ionic diffusion

![[Membrane Transport - non-ionic diffusion.png]]
*Non-ionic diffusion — only the **non-ionised (lipid-soluble) form** crosses the membrane from the outer to the inner side; once across, it turns into the **ionised** form and cannot get back — examples **ammonia diffusion** and **salicylate absorption** (cropped from the handwritten page).*

```
Non-ionised form (outer side)
          ↓  crosses the lipid membrane
Non-ionised (inner side)  →  Ionised  (trapped — cannot diffuse back)
```

- **Examples:**
  - **Ammonia**[^ety-ammonia] **diffusion.**
  - **Salicylate**[^ety-salicylate] **absorption.**[^5]

🧠 A charged (ionised[^ety-ion]) molecule is repelled by the fatty core of the membrane; its uncharged form slips through. Change the pH on the far side so the molecule picks up a charge, and it is **trapped** there.

### Osmotic diffusion

```
          Passive
High H₂O ─────────────→ Low H₂O
     Semipermeable membrane
```

- **Osmosis = passive movement of water from high H₂O (dilute side) to low H₂O (concentrated side) across a semipermeable**[^pre-semi][^ety-permeable][^pre-per] **membrane.**

![[Membrane Transport - osmotic diffusion.png]]
*Osmotic diffusion — a U-tube divided by a **semipermeable membrane**: pure solvent (water) on the left, **solution** with **solute (Na⁺)** on the right; water moves towards the solute side (cropped from the handwritten page).*

![[Membrane Transport - osmotic pressure.png]]
*Osmotic pressure — the pressure that must be **applied to stop movement of H₂O** into the solution side; the difference in column heights is the **osmotic pressure** (cropped from the handwritten page; the first words of the label, "Pressure applied to", were overwritten by a watermark and have been blanked).*

🧠 Osmotic pressure is the "pull" of the solute[^ety-solute] on water, measured as the push you would need to cancel it.[^6]

**Role of sodium:**
- **Sodium (osmotically active): drags H₂O.**

**Plasma osmolarity (Posm):**

```latex
P_{osm} = 2\,(\text{Na}^+) + 0.05\,(\text{Glu}) + 0.36\,(\text{Blood urea nitrogen})
```

- **Posm = 2 (Na⁺) + 0.05 (Glu) + 0.36 (Blood urea**[^ety-urea] **nitrogen).**
- **Normal osmolarity of Na⁺: 300 mosm/L.**[^7]

> [!note] Note
> **Osmoles: concentration of osmotically active substance.**[^8]
>
> | Osmolarity[^ety-osmolarity] | Osmolality |
> |---|---|
> | **mosm/L** of solvent | **mosm/Kg** of solvent |
> | Most common | — |

🎬 **Watch:** [YouTube search — passive transport, simple and facilitated diffusion, osmosis](https://www.youtube.com/results?search_query=passive+transport+simple+facilitated+diffusion+osmosis+physiology) · [YouTube search — Fick's law of diffusion physiology](https://www.youtube.com/results?search_query=fick%27s+law+of+diffusion+physiology+lecture)

---

## ⬆️ Active Transport

- **ATP utilized as source of energy.**
- **Types:**
  1. **Primary active transport.**
  2. **Secondary active transport.**

![[Membrane Transport - active transport.png]]
*Active transport — a carrier protein uses ATP (→ ADP + Pi) to move the substance from **low substance concentration** (cytosol side) to **high substance concentration**, against its gradient (cropped from the handwritten page).*

### Primary active transport

- **Transport channel have own ATPase**[^ety-atpase][^suf-ase].
- **Examples:**
  - **Na⁺–K⁺ ATPase.**
  - **H⁺–K⁺ ATPase (Proton**[^ety-proton] **pump).**
  - **Ca²⁺ ATPase.**

#### Na⁺–K⁺ ATPase

- **Transmembrane protein in cell membrane.**
- **Heterogenous**[^pre-hetero] **heterodimer**[^ety-dimer][^pre-di][^suf-mer] **(2 different subunits): α and β.**
- **Coupling ratio: 3:2**
  - Movement of **3 Na⁺ out** and **2 K⁺ inside** cell: **Electrogenic**[^ety-electrogenic][^pre-electro][^suf-genic] **pump.**[^9]

**Structure:**

![[Membrane Transport - structure of Na-K pump.png]]
*Na⁺–K⁺ pump — the **β subunit** carries the **glycosylation sites** on its outer end; the **α subunit** spans the membrane, binds **K⁺** and **ouabain (blocker of Na⁺–K⁺ ATPase)** on the outer surface, and **ATP** and **Na⁺** on the inner surface, where it is **phosphorylated**; **3 Na⁺** leave and **2 K⁺** enter per cycle (cropped from the handwritten page).*

| Part | Detail on the page |
|---|---|
| **β subunit** | **Glycosylation**[^ety-glycosylation][^pre-glyco] **sites** (outer end) |
| **α subunit — outer membrane side** | **K⁺** binding · **Ouabain**[^ety-ouabain] **(blocker of Na⁺–K⁺ ATPase)** |
| **α subunit — inner membrane side** | **ATP**, **Na⁺** binding · **Phosphorylation**[^ety-phosphorylation] |
| **Net movement** | **3 Na⁺ out, 2 K⁺ in** |

**Functions:**
1. **Regulation of cell volume:** cell swollen with H₂O → pump expels Na⁺ (and water follows) → **cell shape returns back to normal**.
2. **Resting membrane potential: contributes 4 mV (minor).**
3. **Indirect energy source: for secondary active transport.**

![[Membrane Transport - Na-K pump regulates cell volume.png]]
*Regulation of cell volume — a cell swollen with H₂O → the Na⁺–K⁺ pump moves Na⁺ out (water follows) → cell shape returns to normal (cropped from the handwritten page).*

**Regulation: activity of Na⁺–K⁺ pump**[^10]

| | **Increase** [↑ ATP hydrolysis[^ety-hydrolysis][^pre-hydro][^suf-lysis] (metabolically[^ety-metabolism][^pre-meta] active)] | **Decrease** |
|---|---|---|
| **Examples** | **Thyroid hormone** | **Ouabain** |
| | **Insulin**[^ety-insulin] | **Digitalis**[^ety-digitalis] |
| | **Aldosterone** | **Dopamine (Physiological)** |

### Secondary active transport

- **Secondary to energy gradient established by primary active transport.**

![[Membrane Transport - secondary active transport SGLT.png]]
*Secondary active transport — the Na⁺–K⁺ pump (right, red; ATP → ADP + Pi, 3 Na⁺ out / 2 K⁺ in) keeps cell Na⁺ low; **SGLT** (left) lets Na⁺ run back in down that gradient and drags **glucose (Glu)** in with it, uphill. The figure's labels are Spanish: *espacio extracelular* = extracellular space, *citosol* = cytosol, *glucosa* = glucose (cropped from the handwritten page).*

**Types:**

**1. Symporter**[^ety-symport][^pre-syn]**: both substances move in same direction.**

| Example | | Site[^11] |
|---|---|---|
| **SGLT (Sodium glucose linked transporter)** | **SGLT-1** | **GIT** |
| | **SGLT-2** | **PCT** |
| **Na⁺–K⁺–2Cl⁻ cotransporter**[^pre-co] | | **Thick ascending limb of loop of Henle**[^ety-henle] |
| **Na⁺–I⁻ symporter** | | **Thyroid gland** |

**2. Antiport**[^pre-anti] **(Exchanger): substances move in opposite direction.**
- **Eg: Cl⁻–HCO₃⁻ exchanger (Anion**[^ety-anion][^pre-ana] **exchanger) in RBC.**[^12]

### Vesicular transport

- **Active transport in the form of vesicles.**
- **Irrespective of concentration gradient.**
- **Help of Ca²⁺ and special protein.**

**Types:**

#### 1. Exocytosis (Emeiocytosis)

- **Exocytosis** AKA **emeiocytosis**[^ety-emeiocytosis] — the vesicle fuses with the membrane and empties its contents outside.

![[Membrane Transport - exocytosis and SNARE proteins.png]]
*Exocytosis — left, a vesicle fusing with the membrane and releasing its contents outside; right, the **SNARE proteins (special proteins)**: **SNAP-25** and **syntaxin** in the cell membrane, **synaptobrevin** on the **vesicle** and **synaptotagmin (Ca²⁺ sensor)**; **↑ Ca²⁺** zips them together → **exocytosis** (cropped from the handwritten page).*

| SNARE protein (special protein) | Where |
|---|---|
| **SNAP-25** | Cell membrane |
| **Syntaxin**[^ety-syntaxin] | Cell membrane |
| **Synaptobrevin**[^ety-synaptobrevin] | Vesicle |
| **Synaptotagmin (Ca²⁺ sensor)** | Vesicle |

> [!note] Note — Botulinum toxin
> ```
> Botulinum toxin ──→ Breakdown of synaptobrevin ──(No exocytosis)──→ Inhibit ACh release from vesicles ──→ Flaccid paralysis
> (To treat achalasia cardia)
> ```
> **Botulinum**[^ety-botulinum] **toxin** (**to treat achalasia**[^ety-achalasia][^pre-a] **cardia**) → **breakdown synaptobrevin** → (no exocytosis) → **inhibit ACh release from vesicles** → **flaccid**[^ety-flaccid] **paralysis**[^ety-paralysis][^pre-para].[^13]

#### 2. Endocytosis

![[Membrane Transport - endocytosis, phagocytosis and pinocytosis.png]]
*Endocytosis — left, the membrane dips in (outside → inside) and pinches off a vesicle; right, **a. phagocytosis** (a bacterium engulfed into a large vacuole) and **b. pinocytosis** (small vesicles of fluid) (cropped from the handwritten page; the receptor-mediated panel beside them carried a watermark and is given as a prompt below).*

**Types:**
- **a. Phagocytosis**[^ety-phagocytosis] — cell eating: **bacteria**.
- **b. Pinocytosis**[^ety-pinocytosis] — cell drinking: **fluid**.
- **c. Receptor mediated endocytosis** — **substance with receptors**.
  - **Eg: LDL cholesterol**[^pre-lipo] **with receptor proteins (Clathrin**[^ety-clathrin]**, Dynamin**[^ety-dynamin]**).**[^14]

> [!example]- 🎨 Image prompt — Receptor-mediated endocytosis
> "Flat-vector medical textbook illustration, white background, orange cell membrane drawn as a double line. Outside the cell: scattered red stars (ligand, e.g. LDL) and black squares (other molecules). On the membrane: small black Y-shaped 'Receptors' that bind only the red stars. The membrane dips into a 'Coated pit' lined with a 'Clathrin' lattice beneath; a ring labelled 'Dynamin' pinches the neck; below, a free round 'Coated vesicle' with receptors and red stars inside, spikes of clathrin around it. Labels: 'Substance with receptors', 'Receptor', 'Clathrin', 'Dynamin', 'Coated vesicle', 'Eg: LDL cholesterol'. Title 'c. Receptor mediated endocytosis'. No other text, no watermark."

#### 3. Transcytosis (Cytopempsis)

![[Membrane Transport - transcytosis.png]]
*Transcytosis — a substance (blue) is taken in by **endocytosis** on one surface of an epithelial cell, carried across in a vesicle, and released by **exocytosis** on the opposite surface (cropped from the handwritten page).*

- **Transcytosis** AKA **cytopempsis**[^ety-cytopempsis] = **endocytosis** on one side → vesicle carried across → **exocytosis** on the other side.[^15]

> [!note] Note — Saturation kinetics
> **Obeyed by:**
> - **Active transport (channel).**
> - **Facilitated diffusion (carrier protein).**
>
> **Plateau**[^ety-plateau] occurs as **synthesis of channel / carrier protein takes time on ↑ demand.**
>
> - **Not obeyed by: Simple diffusion.**

![[Membrane Transport - saturation kinetics graph.png]]
*Graph of saturation kinetics — rate of transport (Y) against concentration of substance (X): line **1** (simple diffusion) rises straight — **no saturation**; line **2** (carrier / pump) rises and then flattens at a **plateau** — **saturation**[^ety-saturation] **kinetics**[^ety-kinetics] (cropped from the handwritten page).*

🧠 A carrier is a ferry with a fixed number of seats: once every seat is taken, more passengers on the shore do not make the crossing any faster — the line flattens (the transport maximum). Simple diffusion has no ferry, so more passengers always means more crossings.[^16]

Where the transporters of this chapter work — rotate the organs:

```anatomed
# transport sites of this chapter — retype a name with the plugin's autocomplete if it shows as "unmatched"
parts: lung, small intestine, kidney, thyroid gland, stomach, esophagus
detail: isolated
title: Membrane transport — where it happens
```

🎬 **Watch:** [YouTube search — sodium potassium pump (Na-K ATPase) mechanism](https://www.youtube.com/results?search_query=sodium+potassium+pump+Na+K+ATPase+mechanism+animation) · [YouTube search — secondary active transport symport antiport SGLT](https://www.youtube.com/results?search_query=secondary+active+transport+symport+antiport+SGLT) · [YouTube search — exocytosis, endocytosis and SNARE proteins](https://www.youtube.com/results?search_query=exocytosis+endocytosis+SNARE+proteins+physiology)

---

## Core Dictum & Pattern Recognition

> [!check]+ **🎯 Core Dictum - The Unifying Principle**
>
> **Downhill is free, uphill costs ATP — and almost every uphill move in the body is paid for by one pump.** Passive transport only needs a gradient and a path (bilayer for small lipid-soluble molecules, carriers/channels for the rest), and its rate follows Fick's law. Active transport needs energy: the Na⁺–K⁺ ATPase spends ATP directly to push 3 Na⁺ out and 2 K⁺ in, and that Na⁺ gradient is then "spent" by secondary transporters (SGLT, Na⁺–K⁺–2Cl⁻, Na⁺–I⁻) to drag glucose, chloride and iodide uphill.
>
> Two corollaries explain most exam questions: anything with a carrier **saturates** (has a plateau, a Tm), simple diffusion never does; and anything that blocks the Na⁺–K⁺ pump (ouabain, digitalis) indirectly cripples every Na⁺-coupled transporter and lets cells swell.

> [!example]+ **📊 Clinical Pattern Recognition**
>
> Understanding how the condition progresses through stages helps you recognize it at different phases and predict outcomes.
>
> **Stage 1 - Normal Physiology:**
> O₂ and CO₂ cross a thin (0.5 µm), vast (~70 m²) alveolar membrane by simple diffusion; glucose enters cells by GLUT and is absorbed from gut and tubule by SGLT-1/2 riding the Na⁺ gradient; the Na⁺–K⁺ pump keeps cell volume and contributes −4 mV to the resting potential.
>
> **Stage 2 - Compensated/Early Pathology:**
> Early emphysema (↓ area) or interstitial fibrosis (↑ thickness) lowers the diffusing capacity, but at rest blood still equilibrates with alveolar O₂ before leaving the capillary, so saturation is normal and only exercise unmasks desaturation. A partial pump block (therapeutic digoxin) raises intracellular Na⁺ and Ca²⁺ just enough to strengthen contraction.
>
> **Stage 3 - Decompensated/Overt Disease:**
> Advanced emphysema/fibrosis → resting hypoxaemia and dyspnoea; digitalis toxicity → arrhythmias and hyperkalaemia as the pump fails; glucose load above the SGLT transport maximum → glycosuria; botulinum toxin destroys SNARE proteins → no ACh exocytosis → descending flaccid paralysis.
>
> **Progression Timeline:**
> Normal → Trigger (↓ area / ↑ thickness / pump block / carrier saturation / SNARE toxin) → Early Changes (↓ transport rate) → Compensation (reserve capacity, more carriers) → Decompensation (gradient or Tm exceeded) → Full Clinical Syndrome
>
> **Why This Matters Clinically:**
> Drugs work on these exact transporters: SGLT-2 inhibitors (gliflozins) cause glycosuria on purpose, loop diuretics block Na⁺–K⁺–2Cl⁻, proton-pump inhibitors block H⁺–K⁺ ATPase, digoxin blocks Na⁺–K⁺ ATPase, and botulinum toxin is used deliberately in achalasia cardia and spasticity.

> [!warning]+ **🔍 Diagnostic Buzzwords & Pattern Recognition**
>
> These are the key terms, phrases, and clinical patterns that should immediately trigger specific diagnoses in your mind. When you see these in a clinical vignette or real patient, you should think of the associated condition instantly.
>
> **Buzzwords by Condition:**
>
> **Emphysema:** "↓ DLCO", "loss of alveolar walls", "↓ surface area" → Fick's law: diffusion ∝ area, so destroyed septa reduce gas transfer.
>
> **Pulmonary fibrosis:** "↑ thickness of membrane", "restrictive pattern with ↓ DLCO" → diffusion ∝ 1/thickness.
>
> **Botulism:** "Descending flaccid paralysis", "home-canned food", "dilated pupils" → toxin cleaves SNARE proteins → no ACh exocytosis.
>
> **Digitalis toxicity:** "Yellow vision, arrhythmia, hyperkalaemia" → Na⁺–K⁺ ATPase blocked.
>
> **Salicylate poisoning:** "Alkalinise the urine" → non-ionic diffusion / ion trapping: the ionised salicylate cannot cross back from tubule to blood.
>
> **Visual/Imaging Buzzwords:**
> A straight rising line = simple diffusion (no saturation); a curve that flattens = carrier-mediated (saturation kinetics, Tm); a U-tube with unequal columns = osmotic pressure.
>
> **Severity Indicators:**
> Plasma osmolarity: normal ≈ 285–295 mOsm/kg; the calculated Posm uses 2 Na⁺ + glucose + BUN; an osmolar gap > 10 points to an unmeasured osmole (methanol, ethylene glycol, mannitol).

> [!danger]+ **⚠️ Common Traps & Pitfalls**
>
> These are the mistakes that students and clinicians commonly make with this topic. Being aware of these traps helps you avoid diagnostic errors and answer tricky exam questions correctly.
>
> **Trap 1: "Facilitated diffusion uses energy because it uses a protein"**
>
> **What students think:** A carrier protein means active transport.
>
> **Why this is wrong:** The carrier in facilitated diffusion (GLUT, aquaporin) only offers a path; the substance still moves down its gradient and no ATP is spent. What it shares with active transport is **saturation** (finite carriers), not energy use.
>
> **How to avoid this trap:** Ask two separate questions — "ATP?" (active vs passive) and "carrier?" (saturable vs not).
>
> **Trap 2: Secondary active transport uses ATP directly**
>
> **What students think:** SGLT has its own ATPase.
>
> **Why this is wrong:** SGLT, Na⁺–K⁺–2Cl⁻ and Na⁺–I⁻ carriers have no ATPase; they use the Na⁺ gradient that the Na⁺–K⁺ pump created with ATP. Block the pump (ouabain) and secondary transport stops even though the transporter itself is untouched.
>
> **How to avoid this trap:** "Primary = own ATPase; secondary = second-hand energy."
>
> **Trap 3: The Na⁺–K⁺ pump makes the resting membrane potential**
>
> **What students think:** The −70/−90 mV resting potential is mainly the pump.
>
> **Why this is wrong:** The pump's electrogenic 3:2 ratio adds only about −4 mV directly; its real contribution is indirect — it builds the K⁺ gradient that K⁺ diffusion (−86 mV) then uses.
>
> **How to avoid this trap:** "Pump = −4 mV (minor); K⁺ leak = the major part."
>
> **Trap 4: All botulinum toxins cleave synaptobrevin**
>
> **What students think:** Botulinum toxin always targets synaptobrevin, as the page states.
>
> **Why this is wrong:** Serotypes differ — types B, D, F, G cleave synaptobrevin, type A (the therapeutic "Botox") cleaves SNAP-25, type C cleaves syntaxin; all end in the same result (no ACh exocytosis → flaccid paralysis). Tetanus toxin also cleaves synaptobrevin, but in inhibitory spinal interneurons → spastic paralysis.
>
> **How to avoid this trap:** Remember the final common path — "no SNARE, no exocytosis" — and the contrast "botulinum = flaccid, tetanus = spastic".
>
> **Trap 5: Osmolarity and osmolality are interchangeable units**
>
> **What students think:** mOsm/L and mOsm/kg are the same thing.
>
> **Why this is wrong:** Osmolarity is per litre (volume, changes with temperature and with solids such as lipids and proteins); osmolality is per kilogram of solvent (mass). In plasma the values are close, which is why "osmolarity" is the term most commonly used, but laboratories measure osmolality.
>
> **How to avoid this trap:** "L = Litre = osmolarity; K = Kilogram = osmolality."

> [!tip]+ **🔗 Related Concepts & Cross-Topic Connections**
>
> Understanding how this topic connects to other areas of medicine deepens your knowledge and helps you see the bigger picture. These connections also help you answer integrated questions on exams.
>
> **Related Topic 1: [[Membrane Potentials]]**
> The Na⁺–K⁺ pump's −4 mV and the K⁺ gradient it creates are the foundations of the resting membrane potential.
>
> **Related Topic 2: [[Cellular Fluids]]**
> Osmosis, osmolarity, tonicity and the role of Na⁺ as the osmotically active ECF solute decide water shifts between ICF and ECF.
>
> **Related Topic 3: [[Diffusion and Transport of Gases]]**
> Fick's law applied to the alveolar membrane — emphysema (↓ area) and fibrosis (↑ thickness) lower the diffusing capacity.
>
> **Related Topic 4: [[Proximal Convoluted Tubule]]**
> SGLT-2, Na⁺–H⁺ exchange, glucose transport maximum (saturation kinetics) and glycosuria are membrane transport in the kidney.
>
> **Related Topic 5: [[Loop of Henle and Distal Convoluted Tubule]]**
> The Na⁺–K⁺–2Cl⁻ cotransporter of the thick ascending limb — the target of loop diuretics.
>
> **Related Topic 6: [[Synaptic Transmission and Neurotransmitters]]**
> SNARE-mediated exocytosis of transmitter vesicles and its block by botulinum and tetanus toxins.
>
> **Clinical Integration:**
> Gliflozins, loop diuretics, proton-pump inhibitors, digoxin, botulinum toxin therapy and urinary alkalinisation for salicylate poisoning are all transport physiology at the bedside.
>
> **Exam Integration:**
> Typical questions: which transport shows saturation; coupling ratio of the Na⁺–K⁺ pump; SGLT-1 vs SGLT-2 site; example of an antiporter in RBC; which SNARE protein botulinum toxin breaks; factors in Fick's law; the Posm formula.

---

## 🏆 Pearls (High-Yield Summary)

> [!success] Must-Know Pearls
> 1. Nobel prize named on the page for ATP: **Boyer, Walker, Jens Skou**.
> 2. **ATP absent → passive (high → low)**: simple, facilitated (carrier +), non-ionic, osmotic. **ATP present → active (low → high)**: primary, secondary, vesicular.
> 3. **Fick's law: D ∝ concentration gradient × surface area / thickness**; substance: **D ∝ solubility, ∝ 1/size**.
> 4. **Emphysema → ↓ area**, **pulmonary fibrosis → ↑ thickness** → both **↓ diffusion of gases**.
> 5. Facilitated diffusion: **GLUT (glucose), aquaporin (water)** — along gradient, no ATP.
> 6. Non-ionic diffusion: **ammonia diffusion, salicylate absorption** — only the non-ionised form crosses.
> 7. **Sodium is osmotically active — drags water**; **Posm = 2 Na⁺ + 0.05 Glu + 0.36 BUN**; normal ≈ **300 mosm/L**.
> 8. **Osmolarity = mosm/L (most common)**; **osmolality = mosm/kg** of solvent.
> 9. Primary active: **Na⁺–K⁺ ATPase, H⁺–K⁺ ATPase (proton pump), Ca²⁺ ATPase** — the transporter has its own ATPase.
> 10. Na⁺–K⁺ ATPase: **heterodimer α + β**, **3 Na⁺ out : 2 K⁺ in** → **electrogenic**; **ouabain** blocks; functions — **cell volume, −4 mV of RMP, energy for secondary transport**.
> 11. Pump ↑ by **thyroid hormone, insulin, aldosterone**; ↓ by **ouabain, digitalis, dopamine**.
> 12. Symport: **SGLT-1 (GIT), SGLT-2 (PCT), Na⁺–K⁺–2Cl⁻ (thick ascending limb), Na⁺–I⁻ (thyroid)**; antiport: **Cl⁻–HCO₃⁻ in RBC**.
> 13. Vesicular: **Ca²⁺ + SNARE** (SNAP-25, syntaxin, synaptobrevin, **synaptotagmin = Ca²⁺ sensor**); **botulinum toxin → breaks synaptobrevin → no ACh release → flaccid paralysis** (used in **achalasia cardia**).
> 14. Endocytosis: **phagocytosis, pinocytosis, receptor-mediated (LDL; clathrin, dynamin)**; **transcytosis = cytopempsis**.
> 15. **Saturation kinetics**: obeyed by **active transport and facilitated diffusion**, **not by simple diffusion**.

---

## 🔁 One-Line Recall

```
ATP? NO → PASSIVE (high→low): simple (Fick: CG × A / T; solubility, 1/size) · facilitated (GLUT, AQP) · non-ionic (NH3, salicylate) · osmotic
ATP? YES → ACTIVE (low→high): PRIMARY own ATPase — Na⁺-K⁺ (α+β, 3 out : 2 in, electrogenic, ouabain) · H⁺-K⁺ · Ca²⁺
          SECONDARY: symport SGLT-1 GIT / SGLT-2 PCT / NKCC2 TAL / NIS thyroid · antiport Cl⁻-HCO3⁻ RBC
          VESICULAR (Ca²⁺ + SNARE): exo (botulinum → synaptobrevin → flaccid) · endo (phago, pino, receptor/LDL) · transcytosis
Posm = 2 Na⁺ + 0.05 Glu + 0.36 BUN ≈ 300 · SATURATION: carriers & pumps plateau, simple diffusion never
```

---

## 🎬 Video Library

| What to watch | Link |
|---|---|
| Passive transport — simple and facilitated diffusion, osmosis (YouTube search) | https://www.youtube.com/results?search_query=passive+transport+simple+facilitated+diffusion+osmosis+physiology |
| Fick's law of diffusion (YouTube search) | https://www.youtube.com/results?search_query=fick%27s+law+of+diffusion+physiology+lecture |
| Sodium–potassium pump mechanism (YouTube search) | https://www.youtube.com/results?search_query=sodium+potassium+pump+Na+K+ATPase+mechanism+animation |
| Secondary active transport — symport, antiport, SGLT (YouTube search) | https://www.youtube.com/results?search_query=secondary+active+transport+symport+antiport+SGLT |
| Exocytosis, endocytosis and SNARE proteins (YouTube search) | https://www.youtube.com/results?search_query=exocytosis+endocytosis+SNARE+proteins+physiology |

---

## 🖼 Infographic Prompt — One-Page Summary

> [!abstract]- 🎨 Prompt for an image generator (copy everything inside)
> "Design a single-page, portrait A4 medical study infographic titled **'MEMBRANE TRANSPORT'** for a postgraduate physiology exam. Flat-vector textbook style, off-white background; colour code used everywhere: green = passive transport (no ATP), red = active transport (ATP), purple = vesicular transport, grey = notes and formulas. Thin icons, crisp legible text, generous white space. Five panels:
>
> **Panel 1 — 'ATP and classification'.** An ATP molecule labelled 'nitrogenous base – ribose sugar – three phosphate groups (high-energy bonds)'; a ribbon 'Nobel prize: Boyer, Walker, Jens Skou'. A tree: ATP absent → passive (high → low): simple, facilitated (carrier +), non-ionic, osmotic diffusion; ATP present → active (low → high): primary, secondary, vesicular (exocytosis, endocytosis, transcytosis).
>
> **Panel 2 — 'Passive transport (green)'.** Simple diffusion through a bilayer with the formula 'D ∝ CG × A / T' and 'substance: D ∝ solubility, ∝ 1/size (O₂ across alveoli)'; two lung icons 'emphysema ↓ area → ↓ diffusion' and 'pulmonary fibrosis ↑ thickness → ↓ diffusion'. Facilitated diffusion through a carrier: GLUT (glucose), aquaporin (water). Non-ionic diffusion: non-ionised form crosses → becomes ionised (ammonia, salicylate). Osmosis U-tube with semipermeable membrane and 'osmotic pressure = pressure to stop water movement'; 'Na⁺ drags water'; formula 'Posm = 2 Na⁺ + 0.05 Glu + 0.36 BUN ≈ 300 mosm/L'; mini-table osmolarity mosm/L (most common) vs osmolality mosm/kg.
>
> **Panel 3 — 'Primary active transport (red)'.** The Na⁺–K⁺ ATPase: β subunit with glycosylation sites, α subunit with ouabain and K⁺ sites outside, ATP, Na⁺ and phosphorylation inside, arrows '3 Na⁺ out, 2 K⁺ in — electrogenic, coupling 3:2'. Functions: cell volume, −4 mV of RMP, energy for secondary transport. Two-column regulation: ↑ thyroid hormone, insulin, aldosterone; ↓ ouabain, digitalis, dopamine. Other pumps: H⁺–K⁺ (proton pump), Ca²⁺ ATPase.
>
> **Panel 4 — 'Secondary active transport (red, lighter)'.** SGLT beside the Na⁺–K⁺ pump; table: SGLT-1 GIT, SGLT-2 PCT, Na⁺–K⁺–2Cl⁻ thick ascending limb, Na⁺–I⁻ thyroid (symport, same direction); Cl⁻–HCO₃⁻ exchanger in RBC (antiport, opposite direction).
>
> **Panel 5 — 'Vesicular transport and saturation (purple)'.** SNARE proteins: SNAP-25 and syntaxin on the membrane, synaptobrevin on the vesicle, synaptotagmin as Ca²⁺ sensor, '↑Ca²⁺ → exocytosis'; a red warning box 'botulinum toxin → breaks synaptobrevin → no ACh release → flaccid paralysis (used in achalasia cardia)'. Endocytosis icons: phagocytosis (bacteria), pinocytosis (fluid), receptor-mediated (LDL, clathrin, dynamin); transcytosis (cytopempsis) across an epithelial cell. A graph: rate vs concentration — straight line 'simple diffusion, no saturation' and a plateau curve 'active transport & facilitated diffusion — saturation kinetics'.
>
> Footer strip: 'Downhill is free, uphill costs ATP — carriers saturate, simple diffusion never does'. No watermark, no photographs, illustration quality."

---

## 📚 References

- Physiology main notes (Marrow 8) — *Membrane Transport*, pp. 30–34
- Guyton & Hall Textbook of Medical Physiology — Ch. 4, Transport of substances through cell membranes
- Ganong's Review of Medical Physiology — Ch. 2, Overview of cellular physiology (transport across cell membranes)
- `Membrane Transport - ….png` files in `attachments/` are crops of the handwritten pages (no Commons image could be searched for this run)
- Video links are YouTube searches (no verified individual video could be searched for this run)

[^1]: The 1997 Nobel Prize in Chemistry was shared by **Paul D. Boyer** and **John E. Walker** (for the enzymatic mechanism of ATP **synthase**) and **Jens C. Skou** (for the first discovery of an ion-transporting enzyme, the **Na⁺–K⁺ ATPase**, 1957). ATP itself was discovered in 1929 (Karl Lohmann; Fiske and Subbarow). The page's heading "Nobel prize for ATP discovery" is kept.
[^2]: Fick's first law in full: net diffusion rate J = D × A × (C₁ − C₂) / ΔX, where D (the diffusion coefficient) ∝ solubility / √molecular weight. This is why CO₂, though heavier than O₂, diffuses about 20 times faster — it is ~24 times more soluble.
[^3]: Both conditions lower the **diffusing capacity of the lung (DLCO)**: emphysema by destroying alveolar walls (less area), fibrosis by thickening the alveolar–capillary membrane (longer path). The normal membrane is ~0.5 µm thick with ~70 m² of area.
[^4]: Strictly, **GLUT** is a **carrier** (it changes shape — "ping-pong") while **aquaporin** is a **channel** (an open pore); both are facilitated diffusion because both move the substance down its gradient without ATP. The page groups them under "carrier protein".
[^5]: This is **ion trapping**: in the renal tubule NH₃ diffuses into the acidic lumen, picks up H⁺ to become NH₄⁺ and cannot return (diffusion trapping, the way the kidney excretes acid). Aspirin (a weak acid) stays largely un-ionised in the acidic stomach and is absorbed there; in salicylate poisoning, alkalinising the urine ionises the drug in the tubule so it is trapped and excreted.
[^6]: Van 't Hoff's law: π = CRT; each 1 mOsm/L of an impermeant solute exerts about **19.3 mmHg** at body temperature, so 300 mOsm/L corresponds to ~5800 mmHg — which is why small solute shifts move large volumes of water.
[^7]: The usual bedside formula is **Posm = 2 [Na⁺] + glucose/18 + BUN/2.8** (glucose and BUN in mg/dL); 1/18 ≈ 0.055 and 1/2.8 ≈ 0.36 — the page's 0.05 and 0.36. Normal plasma osmolality is ≈ 285–295 mOsm/kg (rounded to 300 in the notes); Na⁺ with its accompanying anions supplies most of it (2 × 140 = 280).
[^8]: Strictly, **osmolarity** is osmoles per litre of **solution** and **osmolality** osmoles per kilogram of **solvent** (water). Osmolality is what a freezing-point osmometer measures and is not changed by temperature or by the volume occupied by plasma proteins and lipids.
[^9]: The Na⁺–K⁺ ATPase is a **P-type ATPase**: the α subunit (with the binding sites for Na⁺, K⁺, ATP and ouabain) is phosphorylated on an aspartate residue during each cycle, while the glycosylated β subunit is needed to deliver α to the membrane. One ATP moves 3 Na⁺ out and 2 K⁺ in; the pump uses about a quarter of a resting person's energy (far more in neurons).
[^10]: Thyroid hormone increases the **number** of pumps (part of its calorigenic action); insulin drives K⁺ into cells (used to treat hyperkalaemia); aldosterone up-regulates pumps in the collecting duct. Digitalis/ouabain inhibit the pump → ↑ intracellular Na⁺ → less Na⁺–Ca²⁺ exchange → ↑ intracellular Ca²⁺ → stronger cardiac contraction. Dopamine inhibits the pump in the PCT → natriuresis.
[^11]: **SGLT-1** carries 2 Na⁺ with 1 glucose (or galactose) in the small intestine (and the late PCT); **SGLT-2** carries 1 Na⁺ with 1 glucose in the early PCT and reabsorbs ~90 % of filtered glucose — the target of gliflozins. The Na⁺–K⁺–2Cl⁻ cotransporter (NKCC2) is blocked by loop diuretics; the Na⁺–I⁻ symporter (NIS) traps iodide in the thyroid.
[^12]: The Cl⁻–HCO₃⁻ exchanger (band 3 protein) produces the **chloride shift (Hamburger shift)**: HCO₃⁻ made from CO₂ in the RBC leaves in exchange for Cl⁻. Other antiporters: Na⁺–H⁺ exchanger (PCT), Na⁺–Ca²⁺ exchanger (heart).
[^13]: Botulinum serotypes B, D, F and G cleave **synaptobrevin (VAMP)**; type A — the one used therapeutically as "Botox" — cleaves **SNAP-25**, and type C cleaves syntaxin. All stop ACh exocytosis at the neuromuscular junction. In **achalasia cardia** it is injected into the lower oesophageal sphincter to relax it. The page's wording is kept in the body.
[^14]: In receptor-mediated endocytosis, ligand–receptor complexes cluster in **clathrin-coated pits**; **dynamin** (a GTPase) pinches the vesicle off. The LDL receptor pathway was described by Michael Brown and Joseph Goldstein (Nobel 1985); a defective LDL receptor causes familial hypercholesterolaemia.
[^15]: Examples of transcytosis: maternal IgG crossing the placenta, IgA crossing the intestinal epithelium into the gut lumen, and macromolecules crossing capillary endothelium.
[^16]: The plateau is the **transport maximum (Tm)** — e.g. renal glucose Tm ≈ 375 mg/min, above which glucose appears in urine. The page writes "active transport (channel)"; strictly it is carriers and pumps that saturate, while open ion channels behave much more like simple diffusion.
[^ety-transport]: **transport** — Latin *trans-*, "across" + *portare*, "to carry" → to carry across: moving a substance across the cell membrane. Same root as *portal* and *portable*.
[^ety-passive]: **passive / active** — Latin *passivus*, "capable of suffering, enduring" (*pati*, to suffer) vs *activus*, "doing" (*agere*, to do) → passive transport happens *to* the molecule (driven by its own gradient); active transport is *done* by the cell with energy. **Differentiate:** *passive* (no ATP, downhill) · *active* (ATP, uphill) · *secondary active* (ATP used indirectly).
[^ety-atp]: **ATP (adenosine triphosphate)** — *adenine* (Greek *adēn*, "gland" — first isolated from pancreas) + *-osine* (ribose sugar) + Greek *tri-*, "three" + *phosphate* (from *phosphorus*, Greek *phōs* "light" + *phoros* "bearing") → adenosine with three phosphates. **Differentiate:** ATP (three) · ADP (*di-*, two) · AMP (*mono-*, one) · cAMP (cyclic).
[^ety-nitrogen]: **nitrogen / nitrogenous** — Greek *nitron*, "native soda, saltpetre" + *-gen*, "producing" → "saltpetre-former" (Chaptal, 1790); a nitrogenous base is a ring compound rich in nitrogen — adenine in ATP.
[^ety-ribose]: **ribose** — a rearranged form of *arabinose* (from *gum arabic*) + *-ose*, sugar → the five-carbon sugar of RNA and ATP; *deoxyribose* (one oxygen less) is the sugar of DNA.
[^ety-boyer-walker]: **Boyer and Walker** — **Paul Delos Boyer** (1918–2018), American biochemist, proposed the "binding change" (rotary) mechanism of ATP synthase; **Sir John Ernest Walker** (born 1941), British chemist, solved its structure — they shared half of the 1997 Nobel Prize in Chemistry.
[^ety-skou]: **Jens Christian Skou** — Danish physician and physiologist (1918–2018) who discovered the Na⁺–K⁺ ATPase in crab nerves (1957), the first known ion-pumping enzyme; the other half of the 1997 Nobel Prize in Chemistry.
[^ety-diffusion]: **diffusion** — Latin *dis-*, "apart, in different directions" + *fundere*, "to pour" + *-ion*, the process → pouring out in all directions: random molecular movement from high to low concentration. **Differentiate:** *diffusion* (random, down a gradient) · *osmosis* (diffusion of water across a semipermeable membrane) · *filtration* (movement driven by pressure) · *bulk flow / convection* (movement with a moving fluid).
[^ety-facilitated]: **facilitated** — Latin *facilis*, "easy" (*facere*, to do) + *-ate* → made easy: the carrier makes it easy for a molecule to cross, but cannot push it uphill.
[^ety-osmosis]: **osmosis / osmotic** — Greek *ōsmos*, "a push, thrust" + *-osis*, the process → the "push" of water through a membrane towards the solute (term from Dutrochet's *endosmose*, 1826). **Differentiate:** *osmosis* (water moves) · *diffusion* (solute moves) · *oncotic pressure* (osmotic pressure due to proteins).
[^ety-vesicle]: **vesicle / vesicular** — Latin *vesicula*, "small bladder" (diminutive of *vesica*, bladder) → a small membrane-bound sac. **Differentiate:** *vesicle* (small sac) · *vacuole* (large one) · *vesica* (the urinary bladder itself).
[^ety-cytosis]: **exocytosis / endocytosis / transcytosis** — Greek *exō*, "outside" / *endon*, "within" / Latin *trans*, "across" + *kytos*, "hollow vessel, cell" + *-osis*, the process → moving material out of / into / across the cell in vesicles. **Differentiate** the endocytosis family: *phagocytosis* (eating particles) · *pinocytosis* (drinking fluid) · *receptor-mediated endocytosis* (selective, via receptors).
[^ety-gradient]: **gradient** — Latin *gradi*, "to step, to walk" (*gradus*, a step) → a slope of steps: the change in concentration (or pressure, or voltage) from one place to another. **Differentiate:** *concentration gradient* · *electrical gradient* · *electrochemical gradient* (the two combined).
[^ety-fick]: **Fick's law** — **Adolf Eugen Fick** (1829–1901), German physiologist, who stated the law of diffusion in 1855; he also devised the Fick principle for measuring cardiac output (1870).
[^ety-alveolus]: **alveolus (alveoli)** — Latin *alveolus*, "a small hollow, trough" (diminutive of *alveus*, a cavity) → the tiny air sacs of the lung; the same word names the tooth socket.
[^ety-emphysema]: **emphysema** — Greek *en-* (*em-* before *ph*), "in" + *physan*, "to blow" + *-ema*, result → something blown up, an inflation: permanent enlargement of air spaces with destruction of their walls. **Differentiate:** *emphysema* (destroyed walls, ↓ area) · *atelectasis* (collapsed alveoli) · *bulla* (a large air space > 1 cm).
[^ety-pulmonary]: **pulmonary** — Latin *pulmo, pulmonis*, "lung" + *-ary*, "relating to" → of the lungs; the Greek equivalent is *pneumon* (pneumonia).
[^ety-fibrosis]: **fibrosis** — Latin *fibra*, "fibre, filament" + Greek *-osis*, a condition → a condition of excess fibrous (collagen) tissue. **Differentiate:** *fibrosis* (scarring by collagen) · *sclerosis* (hardening) · *cirrhosis* (fibrosis with nodules, in the liver).
[^ety-aquaporin]: **aquaporin** — Latin *aqua*, "water" + *porus*, "passage, pore" + *-in* → water-channel protein; discovered by Peter Agre (Nobel Prize in Chemistry 2003).
[^ety-ammonia]: **ammonia** — from *sal ammoniacus*, "salt of Ammon", a salt collected near the temple of the Egyptian god Amun (Ammon) in Libya → NH₃, the un-ionised form that diffuses freely; NH₄⁺ (ammonium) is the ionised, trapped form.
[^ety-salicylate]: **salicylate** — Latin *salix*, "willow" + *-ate*, a salt → salt of salicylic acid, first obtained from willow bark; aspirin is acetyl-salicylic acid.
[^ety-ion]: **ion / ionised** — Greek *ion*, "going" (*ienai*, to go) → a charged particle that goes towards an electrode (Faraday, 1834); *ionised* = carrying a charge. **Differentiate:** *cation* (goes to the cathode, +) · *anion* (goes to the anode, −) · *non-ionised* (neutral, lipid-soluble).
[^ety-permeable]: **permeable** — Latin *per-*, "through" + *meare*, "to pass" + *-able* → able to be passed through. **Semipermeable** = lets the solvent (water) through but not the solute; **impermeable** = lets nothing through.
[^ety-solute]: **solute / solvent / solution** — Latin *solvere*, "to loosen, dissolve" → *solvent*, the dissolving liquid (water); *solute*, what is dissolved (Na⁺, glucose); *solution*, the mixture of both.
[^ety-urea]: **urea** — Greek *ouron*, "urine" → the main nitrogenous waste of the urine; synthesised by Friedrich Wöhler in 1828, the first organic compound made from inorganic material. **BUN** = blood urea nitrogen (the nitrogen part of urea measured in blood).
[^ety-osmolarity]: **osmolarity / osmolality** — *osmole* (*osmo-*, push, osmosis + *mole*) + *-arity* (per litre, as in molarity) or *-ality* (per kilogram, as in molality) → concentration of osmotically active particles per litre of solution / per kilogram of solvent.
[^ety-atpase]: **ATPase** — **ATP** + *-ase*, enzyme → an enzyme that hydrolyses ATP to ADP + Pi and uses the released energy (here to pump ions).
[^ety-proton]: **proton** — Greek *prōton*, "first" → the first (simplest) particle, named by Ernest Rutherford (1920); a hydrogen ion (H⁺) is a bare proton, hence "proton pump" for the H⁺–K⁺ ATPase of gastric parietal cells.
[^ety-dimer]: **dimer / heterodimer** — Greek *di-*, "two" + *meros*, "part" → a molecule of two parts; *hetero-*, "different" → a dimer of two different subunits (α and β of the Na⁺–K⁺ pump). **Differentiate:** *homodimer* (two identical parts) · *heterodimer* (two different) · *trimer / tetramer* (three / four).
[^ety-electrogenic]: **electrogenic** — Greek *ēlektron*, "amber" (rubbed amber gathers charge) + *-genic*, "producing" → producing an electrical potential: the pump moves 3 positive charges out for 2 in, so each cycle makes the inside more negative. **Differentiate:** *electrogenic* (net charge moved) · *electroneutral* (no net charge, e.g. Cl⁻–HCO₃⁻ exchange).
[^ety-glycosylation]: **glycosylation** — Greek *glykys*, "sweet" (sugar) + *-yl* (a chemical group) + *-ation*, the process → attaching sugar chains to a protein; the β subunit's sugars face outward.
[^ety-ouabain]: **ouabain** — from Somali *waabaayo*, an arrow poison prepared from the *Acokanthera* tree → a cardiac glycoside that blocks the Na⁺–K⁺ ATPase from the outside; used experimentally like digitalis.
[^ety-phosphorylation]: **phosphorylation** — *phosphoryl* (the –PO₃ group, from *phosphorus*) + *-ation*, the process → adding a phosphate group to a molecule; the pump's α subunit is phosphorylated by ATP in each cycle. **Differentiate:** *phosphorylation* (adding phosphate) · *dephosphorylation* (removing it) · *oxidative phosphorylation* (ATP synthesis in mitochondria).
[^ety-hydrolysis]: **hydrolysis** — Greek *hydōr*, "water" + *lysis*, "loosening" → splitting a bond by adding water (ATP + H₂O → ADP + Pi + energy).
[^ety-metabolism]: **metabolism / metabolically** — Greek *metabolē*, "change" (*meta-*, change + *ballein*, to throw) + *-ism* → the sum of chemical changes in the body. **Differentiate:** *anabolism* (*ana-*, up — building up) · *catabolism* (*kata-*, down — breaking down).
[^ety-insulin]: **insulin** — Latin *insula*, "island" + *-in* → the hormone of the islets of Langerhans; it stimulates the Na⁺–K⁺ pump and moves K⁺ into cells.
[^ety-digitalis]: **digitalis** — Latin *digitus*, "finger" → the foxglove plant (*Digitalis purpurea*), whose flowers fit over a finger; William Withering described its use for "dropsy" (heart failure) in 1785. Digoxin is its glycoside.
[^ety-symport]: **symport / antiport / uniport** — Greek *syn-*, "together" / *anti-*, "against, opposite" / Latin *unus*, "one" + Latin *portare*, "to carry" → carrying together (same direction) / in opposite directions / a single substance. **Differentiate:** *symporter = cotransporter* · *antiporter = exchanger* · *uniporter* (GLUT).
[^ety-henle]: **loop of Henle** — **Friedrich Gustav Jakob Henle** (1809–1885), German anatomist and pathologist, who described the hairpin loop of the nephron in 1862; also remembered for Henle's layer of the hair follicle.
[^ety-anion]: **anion / cation** — Greek *ana-*, "up" / *kata-*, "down" + *ion*, "going" → the ion that goes *up* to the anode (negative ion: Cl⁻, HCO₃⁻) / *down* to the cathode (positive ion: Na⁺, K⁺) — Faraday's terms (1834).
[^ety-emeiocytosis]: **emeiocytosis** — Greek *emein*, "to vomit" + *kytos*, "cell" + *-osis* → "cell vomiting", an old synonym for exocytosis (the cell ejects its vesicle contents). Same root as *emesis* and *antiemetic*.
[^ety-syntaxin]: **syntaxin** — Greek *syntaxis*, "arrangement, putting together in order" (*syn-* together + *taxis* arrangement) + *-in* → the membrane SNARE protein that puts the fusion machinery together.
[^ety-synaptobrevin]: **synaptobrevin / synaptotagmin** — *synapse* (Greek *syn-* together + *haptein* to fasten) + Latin *brevis*, "short" → a short synaptic (vesicle) protein (VAMP); *synaptotagmin* — Greek *tagma*, "an ordered body" → the vesicle protein that senses Ca²⁺ and triggers fusion. **SNARE** = soluble NSF-attachment protein receptor.
[^ety-botulinum]: **botulinum** — Latin *botulus*, "sausage" → *Clostridium botulinum* was first linked to poisoning from badly preserved sausages (Justinus Kerner, 1820s, "sausage poison"). **Differentiate:** *botulism* (flaccid paralysis, blocks ACh release) · *tetanus* (spastic paralysis, blocks inhibitory transmitter release).
[^ety-achalasia]: **achalasia (cardia)** — Greek *a-*, "not" + *chalasis*, "relaxation" → failure to relax: the lower oesophageal sphincter fails to relax on swallowing (loss of inhibitory neurons in the myenteric plexus); *cardia* (Greek *kardia*, heart) = the part of the stomach next to the heart.
[^ety-flaccid]: **flaccid** — Latin *flaccidus*, "flabby, drooping" (*flaccus*, flap-eared) → limp, without tone. **Differentiate:** *flaccid* (no tone — lower motor neuron or NMJ block) · *spastic* (↑ tone, velocity-dependent — upper motor neuron) · *rigid* (↑ tone in all directions — extrapyramidal).
[^ety-paralysis]: **paralysis** — Greek *para-*, "beside, faulty" + *lyein*, "to loosen" + *-sis* → a loosening (disabling) at the side: loss of muscle power. **Differentiate:** *paralysis / -plegia* (complete loss) · *paresis* (partial weakness) · *palsy* (old English form of paralysis).
[^ety-phagocytosis]: **phagocytosis** — Greek *phagein*, "to eat" + *kytos*, "cell" + *-osis* → cell eating: engulfing large particles (bacteria, debris) into a phagosome; described by Élie Metchnikoff (1882).
[^ety-pinocytosis]: **pinocytosis** — Greek *pinein*, "to drink" + *kytos*, "cell" + *-osis* → cell drinking: taking in droplets of extracellular fluid in small vesicles. **Differentiate:** *phagocytosis* (eating particles, large vacuole) · *pinocytosis* (drinking fluid, small vesicles).
[^ety-clathrin]: **clathrin** — Latin *clathratus*, "latticed, barred" (*clathri*, a lattice) + *-in* → the protein that forms the lattice-like (basket) coat of endocytic pits; named by Barbara Pearse (1975).
[^ety-dynamin]: **dynamin** — Greek *dynamis*, "power, force" + *-in* → the "powerful" GTPase that constricts and pinches off the neck of the budding vesicle.
[^ety-cytopempsis]: **cytopempsis** — Greek *kytos*, "cell" + *pempsis*, "a sending" (*pempein*, to send) → sending through the cell: the older name for transcytosis.
[^ety-plateau]: **plateau** — French, "a flat tray, tableland" (Old French *platel*, from *plat*, flat) → the flat top of a curve where the rate stops rising.
[^ety-saturation]: **saturation** — Latin *saturare*, "to fill, to satisfy" (*satur*, full) + *-ation* → the state of being completely filled: every carrier is occupied, so the rate cannot rise further.
[^ety-kinetics]: **kinetics** — Greek *kinētikos*, "of motion" (*kinein*, to move) → the study of rates of movement or reaction; *saturation kinetics* = rate behaviour of a carrier-limited process (Michaelis–Menten shape).
[^pre-trans]: **trans-** — across, through, beyond: transport, transcytosis, transmembrane. Don't confuse with **inter-** between · **dia-** through (Greek) · **per-** through, thoroughly.
[^pre-tri]: **tri-** — three: triphosphate, triglyceride, tricuspid. Don't confuse with **tetra-** four · **di- / bi-** two · **mono- / uni-** one.
[^suf-ose]: **-ose** — a sugar (carbohydrate): ribose, glucose, galactose, sucrose. Don't confuse with **-ase** an enzyme (ATPase, lipase) · **-osis** a process or condition · **-ol** an alcohol (cholesterol).
[^pre-dis]: **dis- (di-, dif-)** — apart, away, in different directions: diffusion, dissolve, dissociation. Don't confuse with **di-** two (Greek: dimer) · **dys-** bad, difficult · **dia-** through.
[^suf-osis]: **-osis** — a process, or a (usually abnormal) condition: osmosis, exocytosis, fibrosis, phagocytosis. Don't confuse with **-asis / -iasis** a diseased state (lithiasis) · **-itis** inflammation · **-oma** a tumour.
[^suf-cle]: **-cle / -cule / -ule / -ula** — small (Latin diminutive): vesicle, molecule, tubule, cellula. Don't confuse with **-cele** a hernia or swelling (hydrocele) · **-coele** a cavity (blastocoele).
[^pre-exo]: **exo-** — outside, outward (Greek): exocytosis, exocrine, exogenous. Don't confuse with **ex-** out of (Latin: excretion) · **extra-** beyond · **ecto-** outer layer · **endo-** within.
[^pre-endo]: **endo-** — within, inner (Greek): endocytosis, endothelium, endocrine, endogenous. Don't confuse with **exo-** outside · **ento-** inner (rare) · **intra-** within (Latin equivalent).
[^suf-olus]: **-olus / -ola / -olum / -ole** — small (Latin diminutive): alveolus, arteriole, bronchiole, nucleolus. Don't confuse with **-ol** an alcohol (cholesterol, glycerol) · **-oma** a tumour.
[^pre-en]: **en- / em- (before b, p, ph)** — in, into, within (Greek): emphysema (blown in), embolism, encephalon. Don't confuse with **endo-** within (a separate Greek prefix) · **an- / a-** not, without.
[^pre-semi]: **semi-** — half, partly (Latin): semipermeable, semilunar, semicircular. Don't confuse with **hemi-** half (Greek equivalent: hemiplegia) · **demi-** half (French) · **sym- / syn-** together.
[^pre-per]: **per-** — through, thoroughly: permeable, perfusion, percutaneous. Don't confuse with **peri-** around (Greek: pericardium) · **pre-** before · **para-** beside.
[^suf-ase]: **-ase** — an enzyme: ATPase, kinase, lipase, amylase. Don't confuse with **-ose** a sugar · **-asis** a disease state.
[^pre-hetero]: **hetero-** — other, different: heterodimer, heterogeneous, heterozygous. Don't confuse with **homo-** same (homodimer) · **homeo-** similar (homeostasis) · **iso-** equal.
[^pre-di]: **di-** — two, double (Greek): dimer, disaccharide, diploid, digastric. Don't confuse with **dia-** through · **dis-** apart · **bi-** two (Latin equivalent).
[^suf-mer]: **-mer** — a part, unit (Greek *meros*): dimer, polymer, monomer, isomer. Don't confuse with **-mere** a segment (centromere, sarcomere — same root, used for body segments) · **-meter** a measure.
[^pre-electro]: **electro-** — electricity (Greek *ēlektron*, amber): electrogenic, electrolyte, electrocardiogram. Don't confuse with **electron** the particle · **elect-** choose (Latin *eligere*).
[^suf-genic]: **-genic / -gen / -genesis** — producing, giving rise to: electrogenic, nitrogen, glycogen, carcinogenic. Don't confuse with **-genous** born of, produced in (endogenous) · **-gnosis** knowledge (diagnosis).
[^pre-glyco]: **glyco- / gluco-** — sugar, sweet: glycosylation, glycogen, glucose, glycosuria. Don't confuse with **glia-** glue (glial cells) · **glyc-** in glycine (an amino acid named for its sweetness).
[^pre-hydro]: **hydro- / hydr-** — water: hydrolysis, hydrophilic, hydrophobic, dehydration. Don't confuse with **hygro-** moisture · **hyper-** over · **hypo-** under.
[^suf-lysis]: **-lysis / -lytic** — breaking down, loosening: hydrolysis, haemolysis, glycogenolysis, paralysis (a "loosening" of power). Don't confuse with **-lyte** a dissolved substance (electrolyte) · **-lith** stone.
[^pre-meta]: **meta-** — change, after, beyond: metabolism, metaplasia, metastasis. Don't confuse with **meso-** middle · **para-** beside · **peri-** around.
[^pre-syn]: **syn- / sym- (before b, p, m)** — together, with: symporter, synapse, syntaxin, synaptobrevin. Don't confuse with **anti-** against (antiporter) · **semi-** half.
[^pre-co]: **co- / con- / com-** — together, with (Latin): cotransporter, coupling, concentration, conduction. Don't confuse with **contra-** against · **counter-** opposite (countercurrent).
[^pre-anti]: **anti-** — against, opposite: antiport, antacid, antibody, antidiuretic. Don't confuse with **ante-** before (antenatal) · **contra-** against (Latin equivalent).
[^pre-ana]: **ana-** — up, back, again: anion (goes up to the anode), anabolism, anaphylaxis, anastomosis. Don't confuse with **an- / a-** without, not (anaemia, achalasia) · **kata- / cata-** down (cation, catabolism).
[^pre-a]: **a- / an-** — without, not (Greek): achalasia (no relaxation), anaemia, aphasia, atrophy. Don't confuse with **ab-** away from (abduction) · **ad-** towards · **ana-** up, again.
[^pre-para]: **para-** — beside, alongside, faulty: paralysis, parathyroid, paracellular. Don't confuse with **peri-** around · **pre-** before · **post-** after.
[^pre-lipo]: **lipo-** — fat (Greek *lipos*): lipoprotein (LDL = low-density lipoprotein), lipid, lipase, lipoma. Don't confuse with **lipo-** "leaving" in *lipothymia* (fainting, from *leipein*) · **lith-** stone.
