---
title: Membrane Potentials
aliases: [Resting membrane potential, Equilibrium potential, Nernst equation, Gibbs-Donnan effect, Driving force]
rank: 7
status: not-started
topic: Physiology
subtopic: General Physiology
chapter: 7
pages: "35–38"
target_exams:
  - NEET PG
  - INI-CET
  - FMGE
past_exam_questions: []
anki_link: ""
case_files: []
difficulty: medium
high_yield: true
guideline_criteria: "Nernst equation; Goldman's equation"
source: "Physiology main notes (Marrow 8) — Membrane Potentials, pp. 35–38 (sections: Resting Membrane Potential 00:01:35 · Equilibrium Potential (E) 00:15:00 · Driving Force (DF) 00:29:06)"
mindmap: "[[Membrane Potentials — Mind Map]]"
index: "[[Physiology — Index]]"
review_day_2: false
review_day_4: false
review_day_7: false
review_day_10: false
review_day_15: false
---
# 🔋 Membrane Potentials

> [!abstract] Core Definition
> A **membrane potential**[^ety-potential][^ety-membrane] is the voltage across the cell membrane — the inside is **negative** compared with the outside. It is measured by a **membrane connected to a voltmeter**, and comes in two types:
> - ✅ **Resting membrane potential (RMP)** — the actual voltage of a cell at rest; AKA **diffusion potential**, because it is made by **diffusion of K⁺** out of the cell.
> - ✅ **Equilibrium potential (EP)** — the voltage at which **one ion's concentration gradient = its electrical gradient**, so it stops moving (Nernst); the gap between the two is the **driving force (DF = RMP − EP)**.

---

## 🧠 Mental Model — A Leaky Battery Charged by K⁺

Picture the cell as a room full of K⁺ with one leaky door that only K⁺ can use. K⁺ walks out down its concentration slope, but each K⁺ that leaves carries a + charge, leaving the room more negative — and that negativity pulls K⁺ back. The point where "out" (concentration) and "back in" (charge) cancel is the **equilibrium potential**; because the door is mostly a K⁺ door, the **resting potential sits close to K⁺'s equilibrium potential**.

```
K⁺ inside HIGH, outside LOW → K⁺ leaks OUT (permeable at rest) → inside left NEGATIVE → RMP
   Diffusion of K⁺ −86 mV  +  Na⁺-K⁺ pump −4 mV  +  Na⁺ leak (very less)  →  ≈ −90 mV (muscle) / −70 mV (neuron)
EQUILIBRIUM POTENTIAL (Nernst, one ion): concentration gradient = electrical gradient → no net movement
   Na⁺ +60 · K⁺ −90 · Cl⁻ −70 (= neuron RMP) · Ca²⁺ +130 (highest)
DRIVING FORCE = RMP − EP  →  Na⁺: −70 − (+60) = −130 mV → cations ENTER, anions LEAVE
GIBBS–DONNAN: trapped protein anions inside → shape ion distribution (RMP) · plasma proteins → oncotic pressure (edema if lost)
```

---

## 📖 Introduction — The Voltmeter and the Types

![[Membrane Potentials - membrane connected to voltmeter.png]]
*Membrane connected to a voltmeter — a **recording microelectrode** pierces the membrane into the cytosol, a **reference electrode** sits in the extracellular fluid; the voltmeter reads the inside relative to the outside (here about −70 mV). The outer face of the membrane is lined with + charges, the inner face with − charges (cropped from the handwritten page).*

🧠 The voltmeter[^ety-voltmeter][^suf-meter] needs two electrodes[^ety-electrode][^pre-electro] — one inside, one outside — because a potential is always a *difference* between two places.[^1]

**Types:**
1. **Resting membrane potential (RMP).**
2. **Equilibrium potential (EP).**

---

## 🔋 Resting Membrane Potential

**AKA diffusion**[^ety-diffusion][^pre-dis] **potential (d/t diffusion of K⁺).**

### Factors determining negative RMP

1. **Charge:** **positively charged K⁺ ion move out of cell.**
2. **Concentration gradient**[^ety-gradient] **of K⁺:**
   - Intracellular[^pre-intra] concentration: **High**.
   - Extracellular[^pre-extra] concentration: **Low**.
3. **Permeability**[^ety-permeability][^pre-per] **of cell to K⁺ at rest:**

```
Passive diffusion of K⁺
          ↓
↑ Intracellular negative charge
```

![[Membrane Potentials - simple diffusion of K+.png]]
*Simple diffusion of K⁺ — K⁺ (high inside) leaves the cell down its gradient (blue arrow); every K⁺ that leaves takes a + charge out, so + charges collect outside and − charges are left on the inner face of the membrane (cropped from the handwritten page).*

🧠 Three things together make the inside negative: K⁺ **wants** to leave (gradient), it **can** leave (the resting membrane is permeable mainly to K⁺), and it **takes its + charge with it** — the large protein anions it leaves behind cannot follow.

### Types

**Stable:**

| Cell | Resting membrane potential[^2] |
|---|---|
| **Neuron**[^ety-neuron] | **−70 mV** |
| **Skeletal**[^ety-skeletal] **muscle** | **−90 mV** |
| **Heart: ventricles**[^ety-ventricle][^suf-cle] | **−90 mV** |

**Unstable / oscillating**[^ety-oscillating]**:**

| Pacemakers | Resting membrane potential |
|---|---|
| **Heart: SA node**[^ety-sinoatrial] | **−60 mV to −40 mV** |
| **GIT: Cajal**[^ety-cajal] **cells** | **−60 mV to −40 mV** |
| **Respiratory: Pre-Botzinger**[^ety-botzinger][^pre-pre] **complex (medulla**[^ety-medulla]**)** | **−60 mV to −40 mV** |

🧠 Pacemaker cells never truly "rest": their potential drifts up by itself until it fires, then resets — that self-drift is what sets the heart rate, the gut's slow waves and the breathing rhythm.[^3]

### Contributing factors

| Factor | Contribution[^4] |
|---|---|
| **1. Diffusion of K⁺ ion** | **−86 mV** |
| **2. Na⁺–K⁺ pump** | **−4 mV** |
| **3. Diffusion of Na⁺ ion** | **Very less** |

### Clinical significance

**1. Hyperkalemia**[^ety-kalaemia][^pre-hyper][^suf-aemia]**:**

- **Eg: in rhabdomyolysis**[^ety-rhabdomyolysis][^pre-rhabdo][^pre-myo][^suf-lysis] **(breakdown of muscle cell).**

```
↑ Extracellular K⁺
        ↓
Inhibit passive diffusion of K⁺
        ↓
↑ Intracellular K⁺ (↑ Positive charge)
        ↓
Depolarized cell (more excitable)
```

- ↑ extracellular K⁺ → **inhibit passive diffusion of K⁺** → ↑ intracellular K⁺ (**↑ positive charge**) → **depolarized**[^ety-polarisation][^pre-de] **cell (more excitable**[^ety-excitable]**)**.[^5]

![[Membrane Potentials - hyperkalemia.png]]
*Hyperkalemia — K⁺ crowds the outside of the cell; the outward K⁺ arrow is crossed out (red ✕): K⁺ stops leaving, more + charge stays inside and the cell depolarises (cropped from the handwritten page).*

**2. Hypokalemia**[^pre-hypo]**:**

```
↓ Extracellular K⁺
        ↓
↑ Passive diffusion of K⁺
        ↓
↓ Intracellular K⁺ (↑ Negative charge)
        ↓
Hyperpolarized cell (Less excitable)
```

- ↓ extracellular K⁺ → **↑ passive diffusion of K⁺** → ↓ intracellular K⁺ (**↑ negative charge**) → **hyperpolarized cell (less excitable)**.[^6]

![[Membrane Potentials - hypokalemia.png]]
*Hypokalemia — few K⁺ outside, so K⁺ streams out of the cell (four outward arrows); more − charge is left inside and the cell hyperpolarises (cropped from the handwritten page).*

Where the pacemakers and the K⁺-sensitive tissues of this section sit — rotate them:

```anatomed
# pacemaker and excitable tissues of this chapter — retype a name with the plugin's autocomplete if it shows as "unmatched"
parts: heart, sinoatrial node, medulla oblongata, stomach, small intestine, skeletal muscle
detail: related
title: Pacemakers and excitable tissues
```

🎬 **Watch:** [YouTube search — resting membrane potential (Ninja Nerd)](https://www.youtube.com/results?search_query=ninja+nerd+resting+membrane+potential) · [YouTube search — hyperkalemia and hypokalemia effect on membrane potential](https://www.youtube.com/results?search_query=hyperkalemia+hypokalemia+resting+membrane+potential+excitability)

---

## ⚖️ Equilibrium Potential (E)

- **AKA isoelectric**[^ety-isoelectric][^pre-iso] **potential (No ion movement).**
- **At EP: Concentration gradient = Electrical gradient.**

![[Membrane Potentials - equilibrium potential of K+.png]]
*Equilibrium (isoelectric) potential — left, K⁺ is **more** inside and **less** outside, so the **K⁺ concentration gradient** pushes K⁺ out, while the negative inside creates a **K⁺ electrical gradient** pulling it back in; right, when the two arrows are equal both are cancelled (✕) — no net movement (cropped from the handwritten page).*

### Determining factors

- **Movement of ions from high concentration to low concentration.**
- **Charge inside cell at equilibrium**[^ety-equilibrium][^pre-equi].

### Values

| Ions | Potential | Diagram (inside vs outside) |
|---|---|---|
| **Na⁺** | **+60 mV** | Na⁺ **low** inside, **high** outside → Na⁺ enters → inside becomes **+** |
| **K⁺** | **−90 mV** | K⁺ **high** inside, **low** outside → K⁺ leaves → inside becomes **−** |
| **Cl⁻** — **same as RMP of neuron** | **−70 mV** | Cl⁻ **low** inside, **high** outside → Cl⁻ enters → inside becomes **−** |
| **Ca²⁺** | **+130 mV (Highest)** | Ca²⁺ **low** inside, **high** outside → Ca²⁺ enters → inside becomes **+** |

![[Membrane Potentials - equilibrium potential values table.png]]
*The page's values table with its diagrams — for each ion the circle (cell) shows its inside concentration, the arrow the direction it moves, and the sign the charge it leaves inside at equilibrium (cropped from the handwritten page).*

🧠 *Rule of thumb:* an ion's equilibrium potential has the **sign of the charge that ion would carry in** — Na⁺ and Ca²⁺ rush in → positive EP; Cl⁻ rushes in → negative EP; K⁺ rushes out → negative EP. The steeper the gradient (Ca²⁺ is ~10 000× higher outside), the bigger the number.[^7]

### Equations determining EP

#### Nernst equation[^ety-nernst]

- **To calculate equilibrium potential of single ion.**

```latex
E = \pm 61 \log \frac{C_o}{C_i} \qquad \text{(OR)} \qquad E = \pm 61 \log \frac{C_i}{C_o}
```

- **E = ±61 log Co/Ci (OR) E = ±61 log Ci/Co** — Co = concentration outside, Ci = concentration inside.
- **Limitation: single ion considered.**[^8]

#### Goldman's equation[^ety-goldman]

- **Consider multiple ions based on:**
  - a. **Concentration.**
  - b. **Permeability.**
- **Applied aspect: rapid changes in permeability of multiple ions → generation of action potential.**[^9]

🎬 **Watch:** [YouTube search — Nernst equation and equilibrium potential explained](https://www.youtube.com/results?search_query=nernst+equation+equilibrium+potential+explained) · [YouTube search — Goldman equation membrane potential](https://www.youtube.com/results?search_query=goldman+hodgkin+katz+equation+membrane+potential)

---

## ➡️ Driving Force (DF)

### Equation

```latex
DF = RMP - EP
```

- **DF = RMP − EP.**
- **Eg: DF (Na⁺) = −70 − (+60 mV) = −130 mV.**[^10]

### Implication

```
            Driving force: Negative (Intracellular)
               ┌──────────────┴──────────────┐
          Cation (Na⁺)                  Anion (Cl⁻)
               ↓                             ↓
          Enter cells                Moves out of cells
```

- **Driving force: negative (intracellular)** →
  - **Cation**[^ety-cation][^pre-kata] **(Na⁺) → enter cells.**
  - **Anion**[^pre-ana] **(Cl⁻) → moves out of cells.**

![[Membrane Potentials - driving force on Na+.png]]
*Driving force on Na⁺ — a cell at −130 mV of driving force for Na⁺: Na⁺ is pulled strongly inward (three arrows) (cropped from the handwritten page).*

🧠 The driving force is "how far the ion is from where it wants to be". Na⁺ wants the inside at +60 mV, the cell sits at −70 mV — a 130 mV gap — so the moment Na⁺ channels open, Na⁺ floods in. That is the upstroke of every action potential.

### Gibbs Donnan effect[^ety-gibbs-donnan]

- **Presence of non-diffusible ions (Proteins) affects the distribution of diffusible ions.**

| X (Inside) | m | Y (Outside) | |
|---|---|---|---|
| K⁺ | ┃ | K⁺ | **Diffusible** |
| Cl⁻ | ┃ | Cl⁻ | **Diffusible** |
| **Proteins (Anions)** | ┃ | — | **Non diffusible** |

![[Membrane Potentials - Gibbs Donnan effect.png]]
*Gibbs–Donnan box — compartment **X (inside)** and **Y (outside)** separated by a membrane **m**: K⁺ and Cl⁻ are on both sides (**diffusible**), the **proteins (anions)** are only inside (**non diffusible**) (cropped from the handwritten page).*

**Implication:**
- **In neuron: RMP is negative d/t non-diffusible protein.**[^11]

**In blood vessel:**
- **Physiology: colloid**[^ety-colloid][^suf-oid] **oncotic**[^ety-oncotic] **pressure (πc) d/t plasma**[^ety-plasma] **proteins → reabsorb fluids.**
- **Pathology: loss of πc (kidney diseases) → interstitial**[^ety-interstitial][^pre-inter] **fluid → edema**[^ety-oedema].[^12]

![[Membrane Potentials - blood vessel colloid oncotic pressure.png]]
*Blood vessel — a capillary running from its **arterial end** to its **venous end** through **tissue cells** bathed in **interstitial fluid**; the **plasma proteins** stay inside the capillary (non-diffusible) and their oncotic pull draws **fluid** back in (cropped from the handwritten page).*

```
Plasma proteins (non-diffusible) → colloid oncotic pressure (πc) → fluid reabsorbed into capillary   [physiology]
Kidney disease → protein lost → ↓ πc → fluid stays in interstitium → EDEMA                          [pathology]
```

🎬 **Watch:** [YouTube search — Gibbs-Donnan equilibrium physiology](https://www.youtube.com/results?search_query=gibbs+donnan+equilibrium+physiology) · [YouTube search — driving force electrochemical gradient membrane potential](https://www.youtube.com/results?search_query=driving+force+electrochemical+gradient+membrane+potential)

---

## Core Dictum & Pattern Recognition

> [!check]+ **🎯 Core Dictum - The Unifying Principle**
>
> **Every membrane potential is a tug-of-war between a concentration gradient and an electrical gradient, and the membrane's permeability decides which ion wins.** Each ion has its own balance point (its equilibrium potential, from the Nernst equation): K⁺ −90, Na⁺ +60, Cl⁻ −70, Ca²⁺ +130 mV. At rest the membrane is permeable mostly to K⁺, so the RMP sits near E_K (−86 mV from K⁺ diffusion, −4 mV from the pump); when permeability shifts (Goldman), the potential moves towards whichever ion now dominates — Na⁺ during the action potential.
>
> The **driving force (RMP − EP)** tells you which way and how hard an ion will move the moment its channel opens, and the **Gibbs–Donnan effect** reminds you that trapped proteins (inside cells, inside capillaries) quietly bias both charge and water distribution.

> [!example]+ **📊 Clinical Pattern Recognition**
>
> Understanding how the condition progresses through stages helps you recognize it at different phases and predict outcomes.
>
> **Stage 1 - Normal Physiology:**
> Plasma K⁺ 3.5–5 mEq/L against ~140 mEq/L inside gives a stable RMP (neuron −70, muscle and ventricle −90 mV); pacemakers (SA node, Cajal cells, pre-Bötzinger complex) oscillate between −60 and −40 mV and fire rhythmically. Plasma proteins hold fluid in the capillaries.
>
> **Stage 2 - Compensated/Early Pathology:**
> Mild hyperkalaemia (e.g. early rhabdomyolysis, renal failure) shrinks the K⁺ gradient → the RMP moves towards threshold → cells become *more* excitable: peaked T waves, paraesthesia. Mild hypokalaemia hyperpolarises skeletal muscle → weakness, cramps. Mild hypoproteinaemia causes only pitting at the ankles because lymph flow compensates.
>
> **Stage 3 - Decompensated/Overt Disease:**
> Severe hyperkalaemia keeps cells partly depolarised so Na⁺ channels stay inactivated → paradoxically **inexcitable**: wide QRS, sine-wave ECG, ventricular fibrillation or asystole, flaccid paralysis. Severe hypokalaemia → paralysis, ileus, arrhythmias (U waves). Nephrotic syndrome with albumin < 2.5 g/dL → generalised oedema/anasarca.
>
> **Progression Timeline:**
> Normal → Trigger (K⁺ shift: rhabdomyolysis, renal failure, diuretics, vomiting; protein loss) → Early Changes (RMP shift, mild oedema) → Compensation (K⁺ redistribution into cells, renal excretion, lymph flow) → Decompensation (Na⁺-channel inactivation or deep hyperpolarisation; ↓ πc beyond safety factor) → Full Clinical Syndrome (arrhythmia, paralysis, anasarca)
>
> **Why This Matters Clinically:**
> Hyperkalaemia is an emergency treated by moving the RMP back: calcium gluconate (stabilises the membrane), insulin–glucose and β₂-agonists (push K⁺ into cells via the Na⁺–K⁺ pump), and then removal (binders, dialysis). Knowing that K⁺ sets the RMP explains every ECG change of K⁺ disorders.

> [!warning]+ **🔍 Diagnostic Buzzwords & Pattern Recognition**
>
> These are the key terms, phrases, and clinical patterns that should immediately trigger specific diagnoses in your mind. When you see these in a clinical vignette or real patient, you should think of the associated condition instantly.
>
> **Buzzwords by Condition:**
>
> **Hyperkalaemia:** "Crush injury / rhabdomyolysis", "renal failure", "tall peaked T waves", "depolarised, more excitable" → ↑ ECF K⁺ narrows the K⁺ gradient so the RMP moves towards threshold.
>
> **Hypokalaemia:** "Muscle weakness after diuretics or vomiting", "U waves, flat T waves", "hyperpolarised, less excitable" → ↓ ECF K⁺ steepens the gradient; more K⁺ leaves; RMP more negative.
>
> **Nephrotic syndrome / liver failure oedema:** "Low albumin", "↓ colloid oncotic pressure", "generalised oedema" → the non-diffusible plasma proteins that hold water in the capillary are lost.
>
> **Equilibrium potential:** "Isoelectric", "no net ion movement", "concentration gradient = electrical gradient" → the Nernst potential of a single ion.
>
> **Visual/Imaging Buzzwords:**
> On ECG: peaked T → widened QRS → sine wave = rising K⁺; flattened T with U wave = low K⁺. On the page: a ✕ on the outward K⁺ arrow = hyperkalaemia; four outward arrows = hypokalaemia.
>
> **Severity Indicators:**
> K⁺ > 6.5 mEq/L or any ECG change = treat as emergency; K⁺ < 2.5 mEq/L risks paralysis and arrhythmia. Plasma oncotic pressure normally ≈ 25–28 mmHg; serum albumin < 2.5 g/dL usually brings oedema.

> [!danger]+ **⚠️ Common Traps & Pitfalls**
>
> These are the mistakes that students and clinicians commonly make with this topic. Being aware of these traps helps you avoid diagnostic errors and answer tricky exam questions correctly.
>
> **Trap 1: "The Na⁺–K⁺ pump creates the RMP"**
>
> **What students think:** The pump's 3:2 exchange is what makes the inside negative.
>
> **Why this is wrong:** The pump's electrogenic contribution is only about −4 mV; the big −86 mV comes from **K⁺ diffusion** through leak channels. The pump's real job is to maintain the K⁺ and Na⁺ gradients that diffusion uses.
>
> **How to avoid this trap:** "K⁺ diffusion −86, pump −4, Na⁺ leak very little."
>
> **Trap 2: Hyperkalaemia always makes cells more excitable**
>
> **What students think:** Depolarised = more excitable, so high K⁺ = hyperexcitability at any level.
>
> **Why this is wrong:** A small depolarisation brings the cell closer to threshold (more excitable), but a sustained large one keeps voltage-gated Na⁺ channels **inactivated**, so the cell cannot fire at all — the heart stops in diastole and muscles become flaccid.
>
> **How to avoid this trap:** "Mild ↑K⁺ = irritable; severe ↑K⁺ = paralysed."
>
> **Trap 3: Equilibrium potential = resting membrane potential**
>
> **What students think:** Both describe a cell "at rest", so they are the same.
>
> **Why this is wrong:** EP belongs to **one ion** (Nernst) and is the voltage where that ion has no net movement; the RMP is the **actual** voltage of the cell, a weighted average of all permeable ions (Goldman). Only Cl⁻ in neurons happens to sit at the RMP (−70 mV) — which is why the page marks it.
>
> **How to avoid this trap:** "Nernst = one ion's wish; Goldman = the whole cell's compromise."
>
> **Trap 4: Ca²⁺ has the most negative equilibrium potential**
>
> **What students think:** The biggest number goes with K⁺ or Cl⁻.
>
> **Why this is wrong:** Ca²⁺ has the **highest** (most positive) equilibrium potential, +130 mV, because its outside concentration is about 10 000 times the free intracellular level; Na⁺ is +60 mV.
>
> **How to avoid this trap:** "Ca²⁺ +130 = highest; K⁺ −90 = most negative."
>
> **Trap 5: Mixing the sign of the driving force**
>
> **What students think:** A negative driving force pushes ions out.
>
> **Why this is wrong:** With DF = RMP − EP, Na⁺'s DF is −130 mV, which on the page's convention means a strong pull of the **cation inward** (and an anion outward). The sign tells you about the inside being too negative for Na⁺, not about the direction of a positive current leaving.
>
> **How to avoid this trap:** Work it in words: "the inside is 130 mV more negative than Na⁺ wants → Na⁺ comes in."

> [!tip]+ **🔗 Related Concepts & Cross-Topic Connections**
>
> Understanding how this topic connects to other areas of medicine deepens your knowledge and helps you see the bigger picture. These connections also help you answer integrated questions on exams.
>
> **Related Topic 1: [[Membrane Transport]]**
> The Na⁺–K⁺ ATPase (3:2, electrogenic, −4 mV) builds the gradients; K⁺ leak is simple diffusion through channels.
>
> **Related Topic 2: [[Characteristics of Nerve Fibres]]**
> Goldman's "rapid changes in permeability" become the action potential: Na⁺ rushes towards +60 mV, K⁺ brings the cell back towards −90 mV.
>
> **Related Topic 3: [[Cardiac Action Potentials]]**
> Ventricular muscle rests at −90 mV, SA node oscillates (−60 to −40 mV) — the basis of pacemaker prepotentials and of K⁺-related ECG changes.
>
> **Related Topic 4: [[Gastrointestinal Motility]]**
> Interstitial cells of Cajal are the oscillating pacemakers that generate the gut's slow waves.
>
> **Related Topic 5: [[Neural Regulation of Respiration]]**
> The pre-Bötzinger complex in the medulla is the oscillating pacemaker of breathing.
>
> **Related Topic 6: [[Cellular Fluids]]**
> Plasma proteins (Gibbs–Donnan, colloid oncotic pressure), interstitial fluid and the safety factors against oedema continue here.
>
> **Clinical Integration:**
> Managing hyper- and hypokalaemia, interpreting their ECGs, explaining muscle weakness after diuretics, and understanding oedema in nephrotic syndrome all rest on the RMP, the Nernst potentials and the Gibbs–Donnan effect.
>
> **Exam Integration:**
> Expect: RMP of neuron/skeletal muscle/SA node; contribution of K⁺ diffusion vs the pump; which ion has the highest EP (Ca²⁺); which ion's EP equals the neuron RMP (Cl⁻); Nernst vs Goldman; DF of Na⁺ = −130 mV; Gibbs–Donnan definition.

---

## 🏆 Pearls (High-Yield Summary)

> [!success] Must-Know Pearls
> 1. Types of membrane potential: **RMP** and **equilibrium potential (EP)**.
> 2. RMP **AKA diffusion potential — d/t diffusion of K⁺**.
> 3. Negative RMP needs: **charge (K⁺ leaves with +)**, **K⁺ gradient (high inside, low outside)**, **permeability to K⁺ at rest**.
> 4. Stable RMP: **neuron −70 mV, skeletal muscle −90 mV, ventricles −90 mV**.
> 5. Oscillating (pacemakers): **SA node, Cajal cells (GIT), pre-Bötzinger complex (medulla) — −60 to −40 mV**.
> 6. Contributions: **K⁺ diffusion −86 mV, Na⁺–K⁺ pump −4 mV, Na⁺ diffusion very less**.
> 7. **Hyperkalaemia** (eg rhabdomyolysis) → K⁺ efflux inhibited → **depolarised, more excitable**; **hypokalaemia** → ↑ K⁺ efflux → **hyperpolarised, less excitable**.
> 8. EP **AKA isoelectric potential** — **concentration gradient = electrical gradient**, no net ion movement.
> 9. EP values: **Na⁺ +60, K⁺ −90, Cl⁻ −70 (= neuron RMP), Ca²⁺ +130 mV (highest)**.
> 10. **Nernst** = single ion, **E = ±61 log Co/Ci**; **Goldman** = multiple ions, by concentration and permeability → **action potential**.
> 11. **DF = RMP − EP**; **DF(Na⁺) = −70 − (+60) = −130 mV** → **cations enter, anions leave**.
> 12. **Gibbs–Donnan**: non-diffusible proteins alter distribution of diffusible ions → **neuron RMP negative**; in vessels **plasma proteins → colloid oncotic pressure → reabsorb fluid**; **loss (kidney disease) → oedema**.

---

## 🔁 One-Line Recall

```
RMP = DIFFUSION POTENTIAL of K⁺ (charge + gradient + permeability) → K⁺ −86 · pump −4 · Na⁺ very less
STABLE: neuron −70 · skeletal −90 · ventricle −90 | OSCILLATING −60→−40: SA node · Cajal · pre-Bötzinger
↑K⁺ → K⁺ efflux blocked → DEPOLARISED (more excitable) · ↓K⁺ → more efflux → HYPERPOLARISED (less excitable)
EP (isoelectric): conc. gradient = electrical gradient → Na⁺ +60 · K⁺ −90 · Cl⁻ −70 · Ca²⁺ +130 (highest)
NERNST ±61 log Co/Ci (one ion) · GOLDMAN (many ions, conc. + permeability → AP) · DF = RMP − EP → Na⁺ −130
GIBBS–DONNAN: trapped protein anions → negative RMP · plasma proteins → πc → reabsorb · lose πc → EDEMA
```

---

## 🎬 Video Library

| What to watch | Link |
|---|---|
| Resting membrane potential (YouTube search — Ninja Nerd) | https://www.youtube.com/results?search_query=ninja+nerd+resting+membrane+potential |
| Hyperkalaemia and hypokalaemia — effect on membrane potential (YouTube search) | https://www.youtube.com/results?search_query=hyperkalemia+hypokalemia+resting+membrane+potential+excitability |
| Nernst equation and equilibrium potential (YouTube search) | https://www.youtube.com/results?search_query=nernst+equation+equilibrium+potential+explained |
| Goldman–Hodgkin–Katz equation (YouTube search) | https://www.youtube.com/results?search_query=goldman+hodgkin+katz+equation+membrane+potential |
| Gibbs–Donnan equilibrium (YouTube search) | https://www.youtube.com/results?search_query=gibbs+donnan+equilibrium+physiology |

---

## 🖼 Infographic Prompt — One-Page Summary

> [!abstract]- 🎨 Prompt for an image generator (copy everything inside)
> "Design a single-page, portrait A4 medical study infographic titled **'MEMBRANE POTENTIALS'** for a postgraduate physiology exam. Flat-vector textbook style, off-white background; colour code used everywhere: purple = K⁺, orange = Na⁺, green = Cl⁻, red = Ca²⁺, blue = proteins and fluid. Thin icons, crisp legible text, generous white space. Four panels:
>
> **Panel 1 — 'Introduction'.** A membrane connected to a voltmeter: recording microelectrode inside the cytosol, reference electrode in the extracellular fluid, the dial reading −70 mV; + charges lining the outer face and − charges the inner face. Two labels: 'Types: 1. Resting membrane potential (RMP) 2. Equilibrium potential (EP)'.
>
> **Panel 2 — 'Resting membrane potential = diffusion potential of K⁺'.** A cell with many purple K⁺ inside and an outward arrow; three numbered factors: charge (K⁺ leaves with +), concentration gradient (high inside, low outside), permeability at rest → ↑ intracellular negative charge. Two mini-tables: stable — neuron −70, skeletal muscle −90, ventricles −90 mV; oscillating pacemakers — SA node, Cajal cells (GIT), pre-Bötzinger complex (medulla) −60 to −40 mV. A stacked bar 'K⁺ diffusion −86 mV + Na⁺–K⁺ pump −4 mV + Na⁺ diffusion very little'. Two side-by-side cells: hyperkalaemia (rhabdomyolysis) — outward arrow crossed → ↑ positive charge → depolarised, more excitable; hypokalaemia — four outward arrows → ↑ negative charge → hyperpolarised, less excitable.
>
> **Panel 3 — 'Equilibrium potential (isoelectric)'.** A cell with opposing arrows 'K⁺ concentration gradient out' and 'K⁺ electrical gradient in', both crossed when equal. A four-row table with ion icons: Na⁺ +60, K⁺ −90, Cl⁻ −70 (same as neuron RMP), Ca²⁺ +130 (highest). Formula cards: 'Nernst: E = ±61 log Co/Ci — single ion (limitation)'; 'Goldman: multiple ions by concentration and permeability → generation of action potential'.
>
> **Panel 4 — 'Driving force and Gibbs–Donnan'.** Formula 'DF = RMP − EP; DF(Na⁺) = −70 − (+60) = −130 mV' with a cell drawing Na⁺ arrows inward; a split 'negative DF → cations (Na⁺) enter, anions (Cl⁻) leave'. A two-compartment box X (inside) | Y (outside) with K⁺ and Cl⁻ on both sides (diffusible) and proteins only inside (non-diffusible) → 'neuron RMP negative'. A capillary from arterial to venous end with plasma proteins inside: 'colloid oncotic pressure (πc) → reabsorb fluid'; a red inset 'kidney disease → loss of πc → interstitial fluid → oedema'.
>
> Footer strip: 'Concentration gradient vs electrical gradient — permeability decides the winner'. No watermark, no photographs, illustration quality."

---

## 📚 References

- Physiology main notes (Marrow 8) — *Membrane Potentials*, pp. 35–38
- Guyton & Hall Textbook of Medical Physiology — Ch. 5, Membrane potentials and action potentials
- Ganong's Review of Medical Physiology — Ch. 2 and 4 (membrane potential, Nernst and Goldman equations)
- `Membrane Potentials - ….png` files in `attachments/` are crops of the handwritten pages (no Commons image could be searched for this run)
- Video links are YouTube searches (no verified individual video could be searched for this run)

[^1]: The voltmeter figure comes from OpenStax *Anatomy & Physiology* ("Measuring charge across a membrane with a voltmeter"): by convention the potential is given as the inside relative to the outside, so a resting neuron reads about −70 mV.
[^2]: Textbook values vary a little: large myelinated nerve fibres about −90 mV (Guyton), many CNS neurons −65 to −70 mV, smooth muscle about −50 to −60 mV, erythrocytes only about −10 mV. The page's values are kept.
[^3]: In the SA node the "resting" potential is really a slowly rising **prepotential** (pacemaker potential) driven by the funny current (If, through HCN channels) and T-type Ca²⁺ channels; the interstitial cells of Cajal produce the gut's **slow waves**; the pre-Bötzinger complex generates the inspiratory rhythm.
[^4]: Guyton's arithmetic: K⁺ alone (Nernst) would give −94 mV; the small Na⁺ leak (permeability about 1/100 of K⁺) pulls this to **−86 mV**; the electrogenic Na⁺–K⁺ pump adds **−4 mV** → net **−90 mV** in large nerve and skeletal muscle fibres.
[^5]: The page's wording is kept. In standard terms: ↑ ECF K⁺ reduces the K⁺ concentration gradient, so the K⁺ equilibrium potential (Nernst) becomes less negative and the RMP moves towards threshold → depolarisation. A small rise makes cells more excitable; a large sustained rise inactivates voltage-gated Na⁺ channels and makes them **less** excitable (cardiac arrest, flaccid paralysis).
[^6]: In standard terms: ↓ ECF K⁺ steepens the K⁺ gradient → E_K and the RMP become more negative → hyperpolarisation → skeletal muscle weakness or paralysis. In the heart, hypokalaemia slows repolarisation and favours arrhythmias (U waves, torsades).
[^7]: Typical concentrations (mEq/L, outside / inside): Na⁺ 142 / 14, K⁺ 4 / 140, Cl⁻ 103 / 4–30, Ca²⁺ 2.4 mM / ~0.0001 mM free. Textbook equilibrium potentials: E_Na ≈ +61 to +66 mV, E_K ≈ −94 mV, E_Cl ≈ −70 mV in neurons (nearer −90 mV in skeletal muscle), E_Ca ≈ +120 to +130 mV.
[^8]: Full form: **E (mV) = ± (61 / z) × log (C_outside / C_inside)** at 37 °C, where z is the valence (61 = 2.303 RT/F); z = 2 for Ca²⁺ halves the factor to ~30.5. Worked example: E_K = 61 × log (4/140) ≈ −94 mV. The "±" means the sign is chosen by the ion's charge — hence the two forms on the page.
[^9]: The **Goldman–Hodgkin–Katz equation**: V = 61 log [(P_K K_o + P_Na Na_o + P_Cl Cl_i) / (P_K K_i + P_Na Na_i + P_Cl Cl_o)]. At rest P_K ≫ P_Na, so V is near E_K; at the peak of the action potential P_Na rises ~100-fold and V swings towards E_Na.
[^10]: The page's convention (DF = RMP − EP) is kept. Many textbooks write the driving force as **Vm − E_ion**, which gives the same −130 mV for Na⁺; a negative value for a cation means an inward current. For K⁺: −70 − (−90) = +20 mV → K⁺ tends to leave.
[^11]: The Gibbs–Donnan effect: impermeant intracellular protein anions hold extra diffusible cations (K⁺) inside and push diffusible anions (Cl⁻) out, so the product [K⁺]×[Cl⁻] is equal on both sides while total osmoles are higher inside. Its direct contribution to the RMP is small; the page's wording is kept.
[^12]: Normal plasma colloid oncotic pressure is about 25–28 mmHg, ~80 % from albumin; ~19 mmHg is from protein molecules themselves and the rest from the extra cations they hold by the Donnan effect. Nephrotic syndrome (urinary protein loss), liver cirrhosis (↓ synthesis) and malnutrition lower it and cause oedema.
[^ety-potential]: **potential** — Latin *potentia*, "power, capability" (*posse*, to be able) → stored ability to do work; electrically, the voltage difference that can drive charge. **Differentiate:** *resting potential* (steady voltage at rest) · *equilibrium potential* (one ion's balance voltage) · *action potential* (brief all-or-none reversal) · *graded / local potential* (small, decremental change).
[^ety-membrane]: **membrane** — Latin *membrana*, "skin covering a limb, parchment" (from *membrum*, limb) → a thin sheet covering or dividing; the cell membrane is the lipid bilayer across which the potential is measured.
[^ety-voltmeter]: **voltmeter / volt** — from **Alessandro Volta** (1745–1827), Italian physicist who built the first electric battery (the voltaic pile, 1800) + Greek *metron*, "measure" → an instrument that measures voltage.
[^ety-electrode]: **electrode** — Greek *ēlektron*, "amber" + *hodos*, "way, path" → the path by which current enters or leaves (Faraday, 1834). **Differentiate:** *recording (active) electrode* (inside the cell) · *reference electrode* (outside) · *anode* (+) / *cathode* (−).
[^ety-diffusion]: **diffusion** — Latin *dis-*, "apart" + *fundere*, "to pour" + *-ion* → pouring out in all directions: movement down a concentration gradient. **Differentiate:** *diffusion potential* (made by an ion diffusing) · *osmosis* (water diffusion) · *filtration* (pressure-driven).
[^ety-gradient]: **gradient** — Latin *gradi*, "to step" (*gradus*, a step) → a slope: here the difference in concentration (chemical gradient) or voltage (electrical gradient) across the membrane; together the *electrochemical gradient*.
[^ety-permeability]: **permeability** — Latin *per-*, "through" + *meare*, "to pass" + *-ability* → the ease with which an ion passes through the membrane (set by open channels). **Differentiate:** *permeability* (how easily) · *conductance* (electrical ease of current flow) · *permeant / impermeant* (can / cannot cross).
[^ety-neuron]: **neuron** — Greek *neuron*, "sinew, cord, nerve" → the nerve cell; the term was popularised by Wilhelm Waldeyer (1891). **Differentiate:** *neuron* (the whole cell) · *nerve* (a bundle of axons) · *neuroglia* (*glia*, glue — supporting cells).
[^ety-skeletal]: **skeletal** — Greek *skeletos*, "dried up" (a dried body, mummy) → of the skeleton; skeletal muscle is the striated, voluntary muscle attached to bones. **Differentiate:** *skeletal* (voluntary, striated) · *cardiac* (involuntary, striated) · *smooth* (involuntary, non-striated).
[^ety-ventricle]: **ventricle** — Latin *ventriculus*, "little belly" (diminutive of *venter*, belly) → a small cavity: the pumping chambers of the heart (and the cavities of the brain). **Differentiate:** *ventricle* (pumping chamber) · *atrium* (Latin, "entrance hall" — receiving chamber).
[^ety-oscillating]: **oscillating** — Latin *oscillare*, "to swing" (*oscillum*, a small mask hung to swing in the wind) → swinging up and down rhythmically; a pacemaker potential oscillates instead of staying steady.
[^ety-sinoatrial]: **sinoatrial (SA) node** — Latin *sinus*, "a curve, hollow" (the sinus venosus) + *atrium*, "entrance hall" + *-al* → the node at the junction of the sinus venosus and the right atrium; described by Arthur Keith and Martin Flack (1907). The heart's normal pacemaker.
[^ety-cajal]: **interstitial cells of Cajal** — **Santiago Ramón y Cajal** (1852–1934), Spanish neuroanatomist (Nobel Prize 1906, shared with Golgi), who described these cells between the gut's muscle layers in the 1890s; they are the pacemakers of intestinal slow waves.
[^ety-botzinger]: **pre-Bötzinger complex** — a group of medullary neurons lying just in front of (*pre-*) the Bötzinger complex, identified as the inspiratory rhythm generator by Jack Feldman's group (1991); the Bötzinger complex itself was named, half in jest, after a Bötzinger wine served at the meeting where the region was discussed.
[^ety-medulla]: **medulla (oblongata)** — Latin *medulla*, "marrow, pith, innermost part" + *oblongata*, "elongated" → the lowest, elongated part of the brainstem holding the respiratory and cardiovascular centres. Same word in *adrenal medulla* and *renal medulla* — the inner part of an organ.
[^ety-kalaemia]: **hyperkalaemia / hypokalaemia** — Latin *kalium*, "potassium" (from Arabic *al-qalī*, plant ashes — hence the symbol K) + Greek *haima*, "blood" + *-ia* → too much / too little potassium in the blood. **Differentiate:** *-kalaemia* (K⁺) · *-natraemia* (Na⁺) · *-calcaemia* (Ca²⁺) · *-chloraemia* (Cl⁻).
[^ety-rhabdomyolysis]: **rhabdomyolysis** — Greek *rhabdos*, "rod" (striated, "rod-like" muscle) + *mys, myos*, "muscle" + *lysis*, "breaking down" → breakdown of striated muscle, releasing K⁺, myoglobin and CK into blood (crush injury, statins, extreme exertion). **Differentiate:** *rhabdomyolysis* (muscle breakdown) · *rhabdomyoma* (benign tumour) · *rhabdomyosarcoma* (malignant tumour of striated muscle).
[^ety-polarisation]: **polarisation / depolarisation / hyperpolarisation / repolarisation** — Greek *polos*, "pivot, pole" + *-ize* + *-ation* → having two opposite poles (inside −, outside +). *De-* (reducing) → the inside becomes less negative; *hyper-* (beyond) → more negative than rest; *re-* (back) → returning to rest. **Differentiate:** depolarised (towards 0, towards threshold) · hyperpolarised (away from threshold).
[^ety-excitable]: **excitable / excitability** — Latin *excitare*, "to rouse, call out" (*ex-* out + *ciere* to set in motion) + *-able* → able to be roused: the ability to fire an action potential in response to a stimulus. **Differentiate:** *excitability* (ability to fire) · *conductivity* (ability to propagate) · *threshold* (the voltage that must be reached).
[^ety-isoelectric]: **isoelectric** — Greek *isos*, "equal" + *ēlektron*, "amber" (electricity) + *-ic* → of equal electrical (charge) balance: no net movement of the ion. On an ECG, the *isoelectric line* is the flat baseline.
[^ety-equilibrium]: **equilibrium** — Latin *aequus*, "equal" + *libra*, "balance, scales" → equal balance: the chemical push and the electrical pull on an ion cancel. **Differentiate:** *equilibrium* (no net flow, no energy needed) · *steady state* (constant because of continuous energy use — the RMP with the pump running).
[^ety-nernst]: **Nernst equation** — **Walther Hermann Nernst** (1864–1941), German physical chemist, who derived the equation for the potential of an ion in 1888–89; Nobel Prize in Chemistry 1920 (for the third law of thermodynamics).
[^ety-goldman]: **Goldman equation** — **David E. Goldman** (1910–1998), American physiologist, who published the constant-field equation in 1943; Alan Hodgkin and Bernard Katz applied it to the squid axon in 1949, hence the **Goldman–Hodgkin–Katz (GHK) equation**.
[^ety-cation]: **cation / anion** — Greek *kata-*, "down" / *ana-*, "up" + *ion*, "going" → the ion that goes down to the cathode (positive: Na⁺, K⁺, Ca²⁺) / up to the anode (negative: Cl⁻, HCO₃⁻, proteins) — Faraday's terms (1834).
[^ety-gibbs-donnan]: **Gibbs–Donnan effect** — **Josiah Willard Gibbs** (1839–1903), American physicist who laid the thermodynamic basis, and **Frederick George Donnan** (1870–1956), British (Irish-born) chemist who described the membrane equilibrium experimentally in 1911.
[^ety-colloid]: **colloid** — Greek *kolla*, "glue" + *-eidēs*, "like" → glue-like: large particles (proteins) dispersed in a fluid that do not pass through membranes; Thomas Graham's term (1861). **Differentiate:** *colloid* (large, non-diffusible: albumin) · *crystalloid* (small, diffusible: NaCl, glucose).
[^ety-oncotic]: **oncotic** — Greek *onkos*, "mass, bulk, swelling" + *-tic* → the osmotic pressure exerted by the bulky plasma proteins. Same root as *oncology* (study of masses, tumours). **Differentiate:** *oncotic pressure* (from proteins only, ~25 mmHg) · *osmotic pressure* (from all solutes, ~5800 mmHg) · *hydrostatic pressure* (fluid pressure pushing out).
[^ety-plasma]: **plasma** — Greek *plasma*, "something moulded or formed" (*plassein*, to mould) → the fluid part of blood (term by Johannes Purkinje / Karl Schultze, 19th century). **Differentiate:** *plasma* (fluid with clotting factors) · *serum* (fluid after clotting — no fibrinogen).
[^ety-interstitial]: **interstitial** — Latin *inter*, "between" + *sistere*, "to stand" (*interstitium*, a space between) + *-al* → the fluid in the spaces between cells. **Differentiate:** *interstitial* (between cells) · *intravascular* (inside vessels) · *intracellular* (inside cells) · *transcellular* (in special cavities).
[^ety-oedema]: **oedema / edema** — Greek *oidēma*, "a swelling" (*oidein*, to swell) → excess fluid in the interstitial space. **Differentiate:** *oedema* (interstitial fluid excess) · *effusion* (fluid in a body cavity — pleural, pericardial) · *anasarca* (*ana-* throughout + *sarx* flesh — generalised oedema).
[^suf-meter]: **-meter / -metry** — measure (Greek *metron*): voltmeter, spirometer, osmometer, audiometry. Don't confuse with **-mere** a segment (sarcomere) · **-mer** a part (dimer) · **metr-** uterus (endometrium, Greek *mētra*).
[^pre-electro]: **electro-** — electricity (Greek *ēlektron*, amber): electrode, electrolyte, electrogenic, electrocardiogram. Don't confuse with **elect-** choose (Latin *eligere*) · **electron** the particle.
[^pre-dis]: **dis- (di-, dif-)** — apart, away, in different directions: diffusion, dissociation, dissolve. Don't confuse with **di-** two · **dys-** bad, difficult · **dia-** through.
[^pre-intra]: **intra-** — within: intracellular, intravascular, intra-arterial. Don't confuse with **inter-** between (interstitial) · **intro-** inward · **endo-** within (Greek).
[^pre-extra]: **extra-** — outside, beyond: extracellular, extrasystole, extrapyramidal. Don't confuse with **exo-** outside (Greek) · **ex-** out of · **intra-** within.
[^pre-per]: **per-** — through, thoroughly: permeability, perfusion, percutaneous. Don't confuse with **peri-** around (pericardium) · **pre-** before · **para-** beside.
[^suf-cle]: **-cle / -cule / -icle / -ule** — small (Latin diminutive): ventricle (little belly), vesicle, molecule, tubule. Don't confuse with **-cele** hernia, swelling (hydrocele) · **-coele** a cavity.
[^pre-pre]: **pre- / prae-** — before, in front of: pre-Bötzinger (in front of the Bötzinger complex), precursor, prevertebral. Don't confuse with **pro-** forward, for · **post-** after · **per-** through.
[^pre-hyper]: **hyper-** — over, above, excessive: hyperkalaemia, hyperpolarised, hypertension. Don't confuse with **hypo-** under, deficient · **supra- / super-** above (Latin equivalents).
[^suf-aemia]: **-aemia / -emia** — a condition of the blood: hyperkalaemia, hypokalaemia, anaemia, uraemia. Don't confuse with **haemo-** blood (prefix) · **-uria** a condition of the urine (proteinuria).
[^pre-rhabdo]: **rhabdo-** — rod, striated (Greek *rhabdos*): rhabdomyolysis, rhabdomyoma, rhabdomyosarcoma. Don't confuse with **rhaphe / -rrhaphy** a seam, suture · **rhino-** nose.
[^pre-myo]: **myo- / my-** — muscle (Greek *mys*, also "mouse" — a flexing muscle looks like a mouse under the skin): rhabdomyolysis, myocardium, myoglobin. Don't confuse with **myelo-** marrow or spinal cord (myelin, myeloid) · **myco-** fungus · **myx-** mucus.
[^suf-lysis]: **-lysis / -lytic** — breaking down, loosening: rhabdomyolysis, haemolysis, hydrolysis. Don't confuse with **-lyte** a dissolved substance (electrolyte) · **-lith** stone.
[^pre-de]: **de-** — down, away, reversing: depolarised, dehydration, desensitisation. Don't confuse with **dis-** apart · **di-** two · **dys-** bad.
[^pre-hypo]: **hypo-** — under, below, deficient: hypokalaemia, hypoproteinaemia, hypothalamus. Don't confuse with **hyper-** over · **hypno-** sleep · **sub- / infra-** below (Latin equivalents).
[^pre-iso]: **iso-** — equal, same (Greek *isos*): isoelectric, isotonic, isometric, isotope. Don't confuse with **eso-** inward (esotropia) · **equi-** equal (Latin equivalent) · **homo-** same (identical).
[^pre-equi]: **equi-** — equal (Latin *aequus*): equilibrium, equivalent, equimolar. Don't confuse with **equine** of a horse (*equus*) · **iso-** equal (Greek equivalent).
[^pre-kata]: **kata- / cata- / cat-** — down, against, completely: cation (goes down to the cathode), catabolism, cataract. Don't confuse with **ana-** up (anion, anabolism) · **meta-** change, after.
[^pre-ana]: **ana-** — up, back, again: anion (goes up to the anode), anabolism, anasarca (throughout the flesh). Don't confuse with **an- / a-** without (anaemia) · **kata-** down.
[^suf-oid]: **-oid** — like, resembling (Greek *-eidēs*): colloid (glue-like), crystalloid, steroid, thyroid. Don't confuse with **-ode** a path (electrode) · **-ide** a chemical compound (chloride).
[^pre-inter]: **inter-** — between, among: interstitial, intercellular, intercalated discs. Don't confuse with **intra-** within · **intro-** inward · **infra-** below.
