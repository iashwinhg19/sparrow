---
title: Hemodynamics
aliases: [Haemodynamics, Poiseuille law, Korotkoff sounds, Reynolds number, Laplace law]
rank: 38
status: not-started
topic: Physiology
subtopic: Cardiovascular System and Blood
chapter: 38
pages: "171–173"
target_exams:
  - NEET PG
  - INI-CET
  - FMGE
past_exam_questions: []
anki_link: ""
case_files: []
difficulty: medium
high_yield: true
guideline_criteria: "Korotkoff phases 1–5; Reynolds number < 2000 / 2000–3000 / > 3000; cuff bladder length 80 % and width 40 % of arm circumference"
source: "Physiology main notes (Marrow 8) — Hemodynamics, pp. 171–173 (sections: Poiseuille-Hagen Law 00:02:07 · Blood Pressure 00:11:50 · Other Parameters Determining Blood Flow 00:26:50)"
mindmap: "[[Hemodynamics — Mind Map]]"
index: "[[Physiology — Index]]"
review_day_2: false
review_day_4: false
review_day_7: false
review_day_10: false
review_day_15: false
---
# 🌊 Hemodynamics

> [!abstract] Core Definition
> **Hemodynamics**[^ety-hemodynamics][^pre-haemo][^suf-ics] is the physics of blood flow — how **pressure**, **radius**, **length** and **viscosity** decide how much blood flows (Poiseuille), how blood pressure is defined and measured (Bernoulli, Korotkoff), and what decides whether flow is quiet or noisy and whether a wall holds or bursts (Reynolds, Laplace).
> - ✅ The single most testable idea: **flow ∝ r⁴** and **resistance ∝ 1/r⁴** — halve the radius and flow falls **16 times**.

---

## 🧠 Mental Model — A Garden Hose

Think of a garden hose. Water flows because the tap end has more pressure than the nozzle end (**PA − PB**). A **wider** hose carries vastly more water (r⁴), a **longer** hose less (1/L), and **honey** would barely move (1/viscosity). Squeeze the nozzle and the jet gets fast and noisy (**Reynolds** — turbulence); a hose with a weak bulge keeps ballooning until it bursts, because a wider bulge carries more wall tension (**Laplace**).

```
FLOW (Poiseuille)   Q ∝ (PA − PB) × r⁴ / (L × viscosity)     → r halves → flow ÷ 16
RESISTANCE          R ∝ 1 / r⁴                               → arterioles control it
PRESSURE (Bernoulli) potential energy (BP) + kinetic energy (flow) = constant
MEASURE             cuff → Korotkoff 1 (SBP) … 5 (DBP) · MAP = DBP + ⅓ PP
TYPE OF FLOW        Reynolds = density × diameter × velocity / viscosity → > 3000 turbulent (murmur)
WALL (Laplace)      P = 2T / r → T ∝ r → dilated heart fails · aneurysm ruptures · capillary survives
```

---

## 📐 Poiseuille-Hagen Law[^ety-poiseuille]

```latex
\text{Blood flow} \;\propto\; \frac{(P_A - P_B) \times (\text{Radius})^4}{\text{Length} \times \text{viscosity}}
```

![[Hemodynamics - Poiseuille tube.png]]
*The blood vessel as a tube: **length (L)**, **radius (r)**, inlet pressure **PA** and outlet pressure **PB** (**pressure difference = PA − PB**); the **number of RBC determines viscosity** (cropped from the handwritten page).*[^1]

🧠 *In plain words:* blood moves only because pressure at the start (PA) is higher than at the end (PB). A wider vessel lets far more through, a longer or a stickier (more viscous[^ety-viscosity]) column lets less through.

![[Hemodynamics - radius length viscosity tubes.png]]
*The four consequences drawn on the page: 1 — radius (normal vs renal artery stenosis, ½ r); 2 — length (L vs 2L); 3 — viscosity (↑ RBC number); 4 — fourth power law (r, 2r, ½ r) (cropped from the handwritten page).*

**1. Blood flow ∝ r⁴**
- Normal blood vessel → radius **r**.
- **Renal**[^ety-renal] **artery stenosis**[^ety-stenosis][^suf-osis] → radius **½ r** → (½)⁴ = 1/16 → **blood flow reduced by 16 times**.[^2]

**2. Blood flow ∝ 1/L**
- Length **L** → **2L** → **blood flow reduced to ½**.

**3. Blood flow ∝ 1/viscosity**
- **↑ RBC number (↑ viscosity)** → **blood flow ↓ in hyperviscosity**[^pre-hyper] (polycythaemia).

**4. Fourth power law: Resistance**[^ety-resistance] **∝ 1/radius⁴**

| Vessel | Radius | Resistance |
|---|---|---|
| Normal | r | Normal |
| Dilated | **2r** | **↓ resistance** (÷ 16) |
| Narrowed | **½ r** | **↑ resistance** (× 16) |

**5. Blood flow ∝ 1/area**[^3]

🎬 **Watch:** [YouTube search — Poiseuille's law blood flow resistance physiology](https://www.youtube.com/results?search_query=poiseuille+law+blood+flow+resistance+physiology) · [YouTube search — Ninja Nerd hemodynamics](https://www.youtube.com/results?search_query=ninja+nerd+hemodynamics+blood+flow+pressure+resistance)

---

## 🩺 Blood Pressure

**The lateral pressure exerted by the blood on a vessel wall.**

### Principle

> [!info] **Bernoulli's principle**[^ety-bernoulli]: **Potential energy + Kinetic**[^ety-kinetic] **energy = Constant**
> - Potential energy = **blood pressure**; kinetic energy = **blood flow**.
> - Hence **BP + blood flow = constant** — where blood speeds up (a narrowing), the pressure on the wall drops, and vice versa.[^4]

### Measurement

| | |
|---|---|
| **SI unit** | **Pascal**[^ety-pascal][^5] |
| **Preferred unit** | **mm Hg** — **Systolic**[^ety-systole][^pre-syn] **blood pressure = 120 mm Hg**; **Diastolic**[^pre-dia] **blood pressure = 80 mm Hg** |

**Formulas:**
- **Pulse**[^ety-pulse] **pressure = SBP − DBP** (120 − 80 = 40 mm Hg).
- **Mean arterial pressure (MAP) = DBP + ⅓ pulse pressure = 93–100 mm Hg.**[^6]

### Modes of measurement

| Direct | Indirect |
|---|---|
| **Invasive**[^ety-invasive][^pre-in] | **Non invasive** |
| Measures **intraarterial**[^pre-intra] BP | **Underestimates SBP by 10 mm Hg**[^7] |
| Used in **animals (research purpose)** | **Used in clinical practice** |

![[Hemodynamics - sphygmomanometer.png]]
*A mercury **sphygmomanometer**[^ety-sphygmomanometer][^pre-sphygmo][^suf-meter] with its cuff and bulb — the instrument of the indirect method (cropped from the handwritten page).*

### Indirect method — Korotkoff's[^ety-korotkoff] sounds

| Phase | Sound | Marks |
|---|---|---|
| **Phase 1** | **Faint tapping sound** | **SBP** |
| **Phase 2** | **Murmur**[^ety-murmur] **like sound** | — |
| **Phase 3** | **Crisp & clear sound** | — |
| **Phase 4** | **Muffled sound** | — |
| **Phase 5** | **Sound disappears** | **DBP** |

![[Hemodynamics - Korotkoff sounds cuff deflation.png]]
*Why the sounds appear and vanish: **complete obstruction** (cuff above SBP) → **no flow, no sound**; **little deflation** → blood spurts through the narrowed artery → turbulent **Korotkoff sound**; **complete deflation** (cuff below DBP) → **non-constricted flow, no sound** (cropped from the handwritten page).*[^8]

### False BP recordings

- **Small size cuff used.**
- **Obesity**[^ety-obesity].
- **Thick & calcified**[^ety-calcified] **vessel.**[^9]

**Correct cuff (bladder):**
- **Length: cover 80 % of arm circumference**[^ety-circumference][^pre-circum].
- **Width: cover 40 % of arm circumference.**

![[Hemodynamics - Riva-Rocci cuff.png]]
*The **Riva-Rocci**[^ety-riva-rocci] **cuff** — the inflatable bladder whose length and width must match the arm (cropped from the handwritten page).*

### Auscultatory[^ety-auscultatory] gap

- **Significance: DBP overestimated.**[^10]

![[Hemodynamics - auscultatory gap.png]]
*Auscultatory gap: as the cuff falls from 200 mm Hg, sounds start (true **SBP**), then fall silent (**silent gap**), then return (a false "SBP") and finally stop (**DBP**); the bracket shows the **actual reading** an examiner may record if he misses the first sounds or stops at the gap (cropped from the handwritten page).*

### Direct method — blood pressure in heart chambers

| Heart chambers | SBP (mm Hg) | DBP (mm Hg) |
|---|---|---|
| **Right atrium**[^ety-atrium] | 4 | 0 |
| **Right ventricle**[^ety-ventricle][^suf-icle] | 25 | 5 |
| **Left atrium** | 12 | 4 |
| **Left ventricle** | 140 | 4 |

*(Page values; see footnote for the usual textbook values.)*[^11]

**Pulmonary**[^ety-pulmonary] **capillary wedge pressure (PCWP):**
- **Measures left atrial pressure: 4–12 mm Hg (average 10 mm Hg).**[^12]

🎬 **Watch:** [YouTube search — Korotkoff sounds blood pressure measurement](https://www.youtube.com/results?search_query=korotkoff+sounds+blood+pressure+measurement+phases) · [YouTube search — auscultatory gap explained](https://www.youtube.com/results?search_query=auscultatory+gap+explained) · [YouTube search — Osmosis blood pressure, MAP and pulse pressure](https://www.youtube.com/results?search_query=osmosis+mean+arterial+pressure+pulse+pressure)

---

## 🌀 Other Parameters Determining Blood Flow

### 1. Reynold's number[^ety-reynolds]

![[Hemodynamics - laminar and turbulent flow.png]]
*Blood flow in a vessel is either **laminar (silent)** or **turbulent (noise present)** — turbulent flow is **seen in aorta & pulmonary artery** and is the **basis of murmurs** (cropped from the handwritten page).*

| Type of flow | Sound | Where |
|---|---|---|
| **Laminar**[^ety-laminar][^suf-ar] **flow** | **Silent** | Most vessels — concentric layers sliding over each other |
| **Turbulent**[^ety-turbulent] **flow** | **Noise present** | **Seen in aorta & pulmonary artery**; **basis of murmurs** |

```latex
\text{Reynold's number} \;\propto\; \frac{\text{Density of blood} \times \text{Diameter} \times \text{Velocity of flow}}{\text{Viscosity}}
```

- **Use:** helps to **predict type of blood flow**.
- **Interpretation:**[^13]

| < 2000 | 2000–3000 | > 3000 |
|---|---|---|
| **Laminar flow** | **Transitional**[^ety-transitional][^pre-trans] **flow** | **Turbulent flow** |

> [!tip] **Clinical significance — pregnancy**[^ety-pregnancy]
> In pregnancy **flow murmurs** are heard — d/t **anaemia**[^ety-anaemia][^pre-an][^suf-aemia] (↓ RBC): **↓ viscosity → ↑ Reynold's number** → turbulence → murmur, with no heart disease at all.

### 2. Laplace's law[^ety-laplace]

```latex
\text{Pressure } (P) = \frac{2 \times \text{Tension } (T)}{\text{Radius } (r)}
```

**Clinical significance: Tension**[^ety-tension] **∝ Radius** (at a given pressure).[^14]

![[Hemodynamics - Laplace law clinical significance.png]]
*Laplace's law at three sizes: the **capillary** (small radius, thin wall — "doesn't rupture"), the **normal vs dilated heart** (↑ radius : ↑ tension) and the **aortic aneurysm** (↑ radius) (cropped from the handwritten page; the first word "Doesn't" is partly lost under the page's side tab).*

| Vessel / chamber | Radius | Consequence |
|---|---|---|
| **Capillary** | **Small radius** | **Thin wall** → (d/t low tension) **doesn't rupture** |
| **Dilated cardiomyopathy**[^ety-cardiomyopathy][^pre-myo][^suf-pathy] | **↑ radius : ↑ tension** | (d/t tension) → **heart failure** |
| **Aortic aneurysm**[^ety-aneurysm][^pre-ana] | **↑ radius** | (d/t tension) → **rupture → death** |

![An aortic aneurysm (Wikimedia Commons)](https://upload.wikimedia.org/wikipedia/commons/0/0b/Aortic_aneurysm.jpg)
*An aortic aneurysm — once a segment widens, its wall tension rises with the radius, so it keeps widening until it ruptures (Wikimedia Commons; licence on the file page).*

```anatomed
# vessels and chambers of this chapter — retype a name with the plugin's autocomplete if it shows as "unmatched"
parts: brachial artery, radial artery, arch of aorta, pulmonary trunk, renal artery, right atrium, right ventricle, left atrium, left ventricle
detail: related
title: Where pressure is measured and where Laplace bites
```

🎬 **Watch:** [YouTube search — Reynolds number laminar turbulent blood flow](https://www.youtube.com/results?search_query=reynolds+number+laminar+turbulent+blood+flow+physiology) · [YouTube search — Laplace law heart aneurysm](https://www.youtube.com/results?search_query=law+of+laplace+heart+aneurysm+physiology)

---

## Core Dictum & Pattern Recognition

> [!check]+ **🎯 Core Dictum - The Unifying Principle**
>
> Blood obeys plumbing physics: **flow = pressure difference ÷ resistance**, and resistance is dominated by the **fourth power of the radius**. That is why a modest narrowing (renal artery stenosis, an atheroma) cuts flow dramatically, why the arterioles — whose radius the body can change — control blood pressure, and why viscosity (RBC count) and length matter far less in daily life.
>
> The same radius also governs two other fates: a large radius and high velocity push the Reynolds number into turbulence (murmurs, Korotkoff sounds), and a large radius raises wall tension (Laplace) so a dilated ventricle fails and an aneurysm bursts, while the tiny capillary survives with a one-cell wall.

> [!example]+ **📊 Clinical Pattern Recognition**
>
> Understanding how the condition progresses through stages helps you recognize it at different phases and predict outcomes.
>
> **Stage 1 - Normal Physiology:**
> BP 120/80 mm Hg, pulse pressure 40, MAP 93–100. Flow is laminar and silent almost everywhere (Reynolds < 2000); brief turbulence at peak systole in the aorta and pulmonary artery. Capillaries tolerate their pressure because their radius is tiny.
>
> **Stage 2 - Compensated/Early Pathology:**
> A vessel narrows (renal artery stenosis): flow falls with the fourth power of the radius, the kidney senses low perfusion and raises BP via renin to restore flow. Anaemia or pregnancy lowers viscosity and raises velocity → Reynolds rises → soft flow murmurs without structural disease. A ventricle dilates to keep stroke volume up (Frank–Starling).
>
> **Stage 3 - Decompensated/Overt Disease:**
> Severe stenosis → renovascular hypertension and organ ischaemia; turbulence beyond a narrowed valve or artery → loud murmurs and bruits. The dilated ventricle's wall tension climbs with its radius → oxygen demand outstrips supply → heart failure (dilated cardiomyopathy). An aneurysm's tension rises as it widens → it grows ever faster → rupture and death.
>
> **Progression Timeline:**
> Normal → narrowing or dilatation (change in r) → flow / tension change by r⁴ or r → compensation (renin, Frank–Starling, wall thickening) → compensation exhausted → ischaemia / failure / rupture
>
> **Why This Matters Clinically:**
> Small changes in radius are the biggest lever: a stent that restores half the lost radius gives back most of the flow, vasodilators lower BP by acting on arteriolar radius, and an aneurysm is repaired at a size threshold because its rupture risk climbs with its radius.

> [!warning]+ **🔍 Diagnostic Buzzwords & Pattern Recognition**
>
> These are the key terms, phrases, and clinical patterns that should immediately trigger specific diagnoses in your mind. When you see these in a clinical vignette or real patient, you should think of the associated condition instantly.
>
> **Buzzwords by Condition:**
>
> **Poiseuille / fourth power law:** "radius halved", "flow reduced 16 times", "resistance ∝ 1/r⁴" → arteriolar control of resistance; renal artery stenosis.
>
> **Hyperviscosity:** "↑ RBC number", "polycythaemia", "sluggish flow" → flow ∝ 1/viscosity; thrombosis risk.
>
> **Bernoulli:** "potential + kinetic energy = constant", "pressure falls where velocity rises" → lateral pressure falls at a narrowing.
>
> **Korotkoff phases:** "faint tapping" = phase 1 = SBP; "sound disappears" = phase 5 = DBP; "muffled" = phase 4.
>
> **False high BP:** "small cuff", "obese arm", "thick calcified (stiff) arteries".
>
> **Auscultatory gap:** "silent gap between sounds", "hypertensive, stiff arteries" → DBP overestimated (page) / SBP underestimated if cuff not pumped high enough.
>
> **Flow murmur:** "pregnant woman / anaemic patient, soft systolic murmur, normal echo" → ↓ viscosity → ↑ Reynolds number.
>
> **Laplace:** "dilated ventricle", "aneurysm enlarging and rupturing", "capillary does not burst despite a thin wall" → tension ∝ radius.
>
> **Visual/Imaging Buzzwords:**
> Concentric flow layers = laminar; swirling eddies = turbulent; a cuff diagram with complete obstruction / little deflation / complete deflation = Korotkoff mechanism.
>
> **Severity Indicators:**
> Reynolds < 2000 laminar, 2000–3000 transitional, > 3000 turbulent; PCWP 4–12 mm Hg normal (higher → left-sided congestion); radius ½ → flow ÷ 16.

> [!danger]+ **⚠️ Common Traps & Pitfalls**
>
> These are the mistakes that students and clinicians commonly make with this topic. Being aware of these traps helps you avoid diagnostic errors and answer tricky exam questions correctly.
>
> **Trap 1: Halving the radius halves the flow**
>
> **What students think:** Flow is proportional to radius, or to area (r²).
>
> **Why this is wrong:** Poiseuille's law makes flow proportional to **r⁴**: halving r gives (½)⁴ = **1/16** of the flow, and doubling r gives 16 times the flow. Length and viscosity act only in the first power (2L → ½ flow).
>
> **How to avoid this trap:** "Radius is raised to the fourth — everything else is first power."
>
> **Trap 2: Phase 4 vs phase 5 for diastolic pressure**
>
> **What students think:** DBP is where the sounds become muffled.
>
> **Why this is wrong:** In the page's (and the standard adult) scheme **DBP = phase 5 — the sound disappears**. Phase 4 (muffling) is used only when sounds go on to zero — children, pregnancy, aortic regurgitation, high-output states.
>
> **How to avoid this trap:** "1 starts it (SBP), 5 stops it (DBP)."
>
> **Trap 3: The auscultatory gap is harmless**
>
> **What students think:** A brief silence during deflation does not change the reading.
>
> **Why this is wrong:** If the examiner stops listening at the start of the gap he records DBP far too high (**overestimated**); if he pumps the cuff only into the gap he records the second onset as SBP (**underestimated**). Hypertensive patients with stiff arteries are exactly the ones in whom the error matters.
>
> **How to avoid this trap:** Always find the palpatory SBP first (radial pulse disappears) and inflate 20–30 mm Hg above it.
>
> **Trap 4: Turbulence means disease**
>
> **What students think:** Any murmur means a valve lesion.
>
> **Why this is wrong:** Reynolds number rises whenever viscosity falls or velocity rises — anaemia, pregnancy, fever, thyrotoxicosis, exercise. These give soft "flow" murmurs with a structurally normal heart.
>
> **How to avoid this trap:** Ask "has viscosity fallen or velocity risen?" before blaming a valve.
>
> **Trap 5: A thin wall must burst first**
>
> **What students think:** The capillary, with a one-cell wall, should rupture before the aorta.
>
> **Why this is wrong:** Laplace's law: wall tension ∝ pressure × radius. The capillary's radius is ~4 µm, so its tension is tiny despite a thin wall; the aorta's large radius gives huge tension, which is why it needs a thick wall and why a dilated aorta ruptures.
>
> **How to avoid this trap:** "Radius, not wall thickness, sets tension."

> [!tip]+ **🔗 Related Concepts & Cross-Topic Connections**
>
> Understanding how this topic connects to other areas of medicine deepens your knowledge and helps you see the bigger picture. These connections also help you answer integrated questions on exams.
>
> **Related Topic 1: [[Characteristics of Blood Vessels]]**
> Arterioles are the resistance vessels because Poiseuille's r⁴ lets their small muscle-driven changes in radius dominate total peripheral resistance; velocity ∝ 1/area explains max velocity in the aorta.
>
> **Related Topic 2: [[Regulation of Blood Pressure]]**
> MAP = cardiac output × total peripheral resistance; the baroreflex and vasoactive chemicals act by changing arteriolar radius.
>
> **Related Topic 3: [[Cardiac Cycle]]**
> The chamber pressures, PCWP and the timing of systole and diastole come from the pressure–volume events of each beat; murmurs are turbulence across valves.
>
> **Related Topic 4: [[Cardiac Output]]**
> Laplace's law sets ventricular wall stress (afterload) and explains why a dilated heart needs more oxygen for the same output.
>
> **Related Topic 5: [[Hematopoiesis and Blood Groups]]**
> The haematocrit sets viscosity: polycythaemia slows flow, anaemia speeds it and lowers Reynolds' threshold for turbulence.
>
> **Related Topic 6: [[Structure Function Relationship in Lungs]]**
> Laplace's law (P = 2T/r) is also why small alveoli would collapse into large ones without surfactant.
>
> **Clinical Integration:**
> Correct BP measurement (cuff size, palpatory method, phase 5), interpreting flow murmurs in pregnancy and anaemia, and timing aneurysm repair are bedside applications of this chapter.
>
> **Exam Integration:**
> Classic MCQs: "radius halved — flow?" (1/16), "Korotkoff phase for DBP" (5), "auscultatory gap significance", "Reynolds number > 3000", "MAP formula", "Laplace — why the dilated heart fails".

---

## 🏆 Pearls (High-Yield Summary)

> [!success] Must-Know Pearls
> 1. **Poiseuille–Hagen:** flow ∝ (PA − PB) × r⁴ / (L × viscosity).
> 2. **Flow ∝ r⁴** — renal artery stenosis with ½ r → **flow reduced 16 times**; **resistance ∝ 1/r⁴** (fourth power law).
> 3. Flow ∝ 1/L (2L → ½ flow); flow ∝ 1/viscosity (↑ RBC → ↓ flow in **hyperviscosity**).
> 4. **BP = lateral pressure exerted by blood on the vessel wall**; principle — **Bernoulli: potential energy (BP) + kinetic energy (flow) = constant**.
> 5. SI unit **pascal**; preferred **mm Hg** — SBP **120**, DBP **80**.
> 6. **Pulse pressure = SBP − DBP**; **MAP = DBP + ⅓ PP = 93–100 mm Hg**.
> 7. Direct = invasive, intra-arterial, animals (research); indirect = non-invasive, **underestimates SBP by 10 mm Hg**, clinical use.
> 8. **Korotkoff:** 1 faint tapping (**SBP**) → 2 murmur → 3 crisp & clear → 4 muffled → 5 disappears (**DBP**).
> 9. False readings: **small cuff, obesity, thick calcified vessels**; cuff length **80 %**, width **40 %** of arm circumference (**Riva-Rocci cuff**).
> 10. **Auscultatory gap → DBP overestimated.**
> 11. Chamber pressures: RA 4/0, RV 25/5, LA 12/4, LV 140/4; **PCWP = LA pressure, 4–12 (avg 10) mm Hg**.
> 12. **Reynolds ∝ density × diameter × velocity / viscosity** — < 2000 laminar, 2000–3000 transitional, **> 3000 turbulent**; turbulence in **aorta & pulmonary artery**, basis of **murmurs**; **pregnancy/anaemia → ↓ viscosity → ↑ Reynolds → flow murmurs**.
> 13. **Laplace: P = 2T/r → tension ∝ radius** — capillary (small r) doesn't rupture; **dilated cardiomyopathy → heart failure**; **aortic aneurysm → rupture → death**.

---

## 🔁 One-Line Recall

```
POISEUILLE: Q ∝ ΔP·r⁴ / (L·η) → ½ r = flow ÷ 16 (renal artery stenosis) · R ∝ 1/r⁴ · 2L → ½ · ↑RBC → ↓flow
BP: lateral pressure on wall · Bernoulli PE (BP) + KE (flow) = const · Pa (SI) / mm Hg · 120/80
PP = SBP − DBP · MAP = DBP + ⅓ PP = 93–100
KOROTKOFF: 1 tap (SBP) · 2 murmur · 3 crisp · 4 muffled · 5 silent (DBP) · gap → DBP overestimated
CUFF: 80 % length · 40 % width · small cuff / obesity / calcified → false high
CHAMBERS: RA 4/0 · RV 25/5 · LA 12/4 · LV 140/4 · PCWP = LA 4–12 (10)
REYNOLDS: ρ·D·v/η · <2000 laminar · 2000–3000 transitional · >3000 turbulent → murmurs (pregnancy, anaemia)
LAPLACE: P = 2T/r → T ∝ r → capillary safe · DCM → failure · aneurysm → rupture
```

---

## 🎬 Video Library

| What to watch | Link |
|---|---|
| Poiseuille's law — flow, resistance and radius (YouTube search) | https://www.youtube.com/results?search_query=poiseuille+law+blood+flow+resistance+physiology |
| Hemodynamics — blood flow, pressure, resistance (YouTube search: Ninja Nerd) | https://www.youtube.com/results?search_query=ninja+nerd+hemodynamics+blood+flow+pressure+resistance |
| Korotkoff sounds and BP measurement (YouTube search) | https://www.youtube.com/results?search_query=korotkoff+sounds+blood+pressure+measurement+phases |
| Reynolds number — laminar vs turbulent flow (YouTube search) | https://www.youtube.com/results?search_query=reynolds+number+laminar+turbulent+blood+flow+physiology |
| Law of Laplace — heart and aneurysm (YouTube search) | https://www.youtube.com/results?search_query=law+of+laplace+heart+aneurysm+physiology |

---

## 🖼 Infographic Prompt — One-Page Summary

> [!abstract]- 🎨 Prompt for an image generator (copy everything inside)
> "Design a single-page, portrait A4 medical study infographic titled **'HEMODYNAMICS — THE PHYSICS OF BLOOD FLOW'** for a postgraduate physiology exam. Flat-vector textbook style, off-white background; colour code: red = pressure, blue = flow, orange = resistance/radius, purple = measurement, green = clinical significance. Thin icons, crisp legible text, generous white space. Three panels:
>
> **Panel 1 — 'Poiseuille-Hagen law'.** A horizontal tube labelled length (L), radius (r), PA at the inlet and PB at the outlet, red cells inside 'number of RBC determines viscosity'. Formula 'Blood flow ∝ (PA − PB) × r⁴ / (length × viscosity)'. Four mini-tubes: '1 — flow ∝ r⁴: renal artery stenosis ½ r → flow reduced 16 times'; '2 — flow ∝ 1/L: 2L → flow ½'; '3 — flow ∝ 1/viscosity: ↑ RBC → hyperviscosity → ↓ flow'; '4 — fourth power law: resistance ∝ 1/r⁴: 2r ↓ resistance, ½ r ↑ resistance'; '5 — flow ∝ 1/area'.
>
> **Panel 2 — 'Blood pressure'.** Definition 'lateral pressure exerted by blood on the vessel wall'; a see-saw 'Bernoulli: potential energy (BP) + kinetic energy (flow) = constant'. Unit badges 'SI: pascal · preferred: mm Hg — SBP 120, DBP 80'. Formula cards 'pulse pressure = SBP − DBP' and 'MAP = DBP + ⅓ PP = 93–100 mm Hg'. A two-column table 'Direct: invasive, intra-arterial, animals (research)' vs 'Indirect: non-invasive, underestimates SBP by 10 mm Hg, clinical practice' with a sphygmomanometer icon. A cuff-and-stethoscope diagram with five numbered sound bars 'Korotkoff: 1 faint tapping (SBP), 2 murmur, 3 crisp & clear, 4 muffled, 5 disappears (DBP)'; three artery drawings 'complete obstruction — no flow, no sound / little deflation — Korotkoff sound / complete deflation — no sound'. Warning box 'false BP: small cuff, obesity, thick calcified vessel; cuff length 80 %, width 40 % of arm circumference (Riva-Rocci cuff)'. A vertical mm Hg scale 0–200 showing 'auscultatory gap — DBP overestimated'. A heart outline with chamber pressures 'RA 4/0, RV 25/5, LA 12/4, LV 140/4' and 'PCWP = LA pressure 4–12 (avg 10) mm Hg'.
>
> **Panel 3 — 'Other parameters'.** Two flow tubes 'laminar — silent' and 'turbulent — noise, aorta & pulmonary artery, basis of murmurs'. Formula 'Reynolds ∝ density × diameter × velocity / viscosity' and a three-colour bar '< 2000 laminar | 2000–3000 transitional | > 3000 turbulent'; a pregnant-woman icon 'anaemia → ↓ viscosity → ↑ Reynolds → flow murmur'. Formula 'Laplace: P = 2T / r → tension ∝ radius' with three drawings 'capillary: small radius, thin wall → doesn't rupture', 'normal vs dilated heart → ↑ radius ↑ tension → dilated cardiomyopathy → heart failure', 'aortic aneurysm → ↑ radius → rupture → death'.
>
> Footer strip: 'Radius rules everything — r⁴ for flow, r for tension'. No watermark, no photographs, illustration quality."

---

## 📚 References

- Physiology main notes (Marrow 8) — *Hemodynamics*, pp. 171–173
- Guyton & Hall Textbook of Medical Physiology — Ch. 14 (Overview of the circulation; pressure, flow and resistance), Ch. 15 (Vascular distensibility; measurement of BP)
- Ganong's Review of Medical Physiology — Biophysical considerations of blood flow; arterial pressure measurement
- Wikimedia Commons — embedded web image (licence noted in caption); `Hemodynamics - ….png` files in `attachments/` are crops of the handwritten pages

[^1]: The full Poiseuille equation is Q = π·ΔP·r⁴ / (8·η·L), where η is viscosity; resistance R = 8·η·L / (π·r⁴). It strictly applies to steady laminar flow of a Newtonian fluid in a rigid tube — blood is none of these, but the law still predicts the direction and size of effects well.
[^2]: Renal artery stenosis lowers flow and pressure to the kidney, which releases renin → angiotensin II → renovascular (Goldblatt) hypertension — a classic cause of secondary hypertension.
[^3]: "Blood flow ∝ 1/area" is read with the previous chapter: at a constant total flow it is the **velocity** of flow that varies inversely with the total cross-sectional area (flow = velocity × area). See [[Characteristics of Blood Vessels]].
[^4]: Bernoulli's full statement also includes the gravitational (height) term. In the circulation it explains why the lateral pressure is slightly lower than the end-on (impact) pressure and why pressure drops inside a stenosis where velocity rises.
[^5]: 1 mm Hg ≈ 133.3 Pa (1 kPa ≈ 7.5 mm Hg). The pascal is a newton per square metre.
[^6]: With the page's values, MAP = 80 + ⅓ × 40 ≈ 93 mm Hg. The ⅓ weighting works because diastole lasts about two-thirds of the cycle at a normal heart rate; at fast heart rates MAP moves closer to the arithmetic mean.
[^7]: Cuff readings and intra-arterial readings differ, and the size and direction of the difference vary between studies and between arteries; the page's figure of 10 mm Hg for systolic pressure is kept in the body.
[^8]: The sounds are produced by turbulent, jet-like flow and the vibration of the arterial wall each time blood spurts under the partly deflated cuff. Phase 5 is the standard DBP in adults; phase 4 is used where sounds persist to zero (children, pregnancy, aortic regurgitation, high-output states).
[^9]: A cuff that is too small (or an arm too large for the cuff) needs extra pressure to compress the artery → falsely high reading; a very stiff, calcified artery (Mönckeberg sclerosis, elderly) resists compression → "pseudohypertension".
[^10]: The auscultatory gap is a silent interval between phase 1 and the return of sounds, common in hypertension and arterial stiffness. If the cuff is inflated only into the gap, the next onset is taken as SBP → SBP is **underestimated**; if the start of the gap is taken as the end of the sounds, DBP is **overestimated** — the page's point. Palpating the radial pulse during inflation avoids both.
[^11]: Usual textbook values: RA mean 0–5 mm Hg; RV 25/0–5; pulmonary artery 25/8; LA mean ~8 (2–12); LV 120/0–10 mm Hg. The page's LV systolic value of 140 is kept in the body.
[^12]: PCWP is measured with a balloon-tipped (Swan–Ganz) catheter wedged in a branch of the pulmonary artery: the still column of blood beyond the balloon transmits left atrial pressure. Values > 18–20 mm Hg suggest cardiogenic pulmonary oedema.
[^13]: Reynolds number (Re = ρ·D·v / η) is dimensionless. The 2000 / 3000 cut-offs are for long straight tubes; Guyton notes that turbulence can appear at Re of 200–400 at branches and in the proximal aorta and pulmonary artery, where Re briefly reaches thousands at peak ejection.
[^14]: Laplace for a sphere is P = 2T / r (heart, alveolus); for a cylinder P = T / r (vessels). Wall stress also depends on wall thickness h (σ = P·r / 2h), which is why a dilated ventricle hypertrophies to share the tension.
[^ety-hemodynamics]: **hemodynamics / haemodynamics** — Greek *haima*, "blood" + *dynamis*, "power, force" + *-ics*, "the study of" → the study of the forces that move blood.
[^ety-poiseuille]: **Poiseuille–Hagen law** — Jean Léonard Marie Poiseuille (1797–1869), French physician and physiologist, who measured flow through glass capillaries in 1838–1846; Gotthilf Heinrich Ludwig Hagen (1797–1884), German hydraulic engineer, found the same law independently in 1839. The unit of viscosity, the *poise*, is named after Poiseuille.
[^ety-viscosity]: **viscosity** — Latin *viscum*, "mistletoe; birdlime" (a sticky paste made from mistletoe berries) + *-osity*, "the quality of" → stickiness, a fluid's internal friction. Blood is ~3–4 times as viscous as water, mainly because of its red cells. Not related to *vicious* (Latin *vitium*, fault).
[^ety-renal]: **renal** — Latin *renes*, "kidneys" + *-al*, "pertaining to" → of the kidney. **Differentiate:** Latin *ren-* (renal, adrenal, renin) vs Greek *nephr-* (nephron, nephritis) — same organ, two languages.
[^ety-stenosis]: **stenosis** — Greek *stenos*, "narrow" + *-osis*, "condition" → a narrowing of a passage. **Differentiate:** *stenosis* (narrowing) · *atresia* (no lumen at all) · *occlusion* (complete blockage) · *stricture* (narrowing by scar).
[^ety-resistance]: **resistance** — Latin *re-*, "against" + *sistere*, "to stand" → standing against; the opposition to flow, R = ΔP / Q. **Differentiate:** *resistance* (opposition to flow, ∝ 1/r⁴) · *impedance* (opposition to pulsatile flow, including compliance) · *viscosity* (the fluid's own internal friction — one component of resistance).
[^ety-bernoulli]: **Bernoulli's principle** — Daniel Bernoulli (1700–1782), Swiss mathematician and physicist, who published it in *Hydrodynamica* (1738): along a streamline, pressure + kinetic energy + potential energy stays constant.
[^ety-kinetic]: **kinetic / potential** — Greek *kinētikos*, "of motion" (*kinein*, "to move") → energy of movement; Latin *potentia*, "power" → stored energy that can do work (here, pressure).
[^ety-pascal]: **pascal** — Blaise Pascal (1623–1662), French mathematician, physicist and philosopher, who showed that pressure in a fluid is transmitted equally in all directions; the SI unit of pressure (1 N/m²) honours him.
[^ety-systole]: **systolic / diastolic** — Greek *systolē*, "a drawing together, contraction" (*syn-* + *stellein*, "to draw") vs *diastolē*, "a drawing apart" (*dia-* + *stellein*). Systolic pressure = peak during ventricular ejection; diastolic = lowest, during relaxation.
[^ety-pulse]: **pulse** — Latin *pulsus*, "a beating, a push" (*pellere*, "to drive") → the beat felt over an artery; pulse pressure = the size of each beat's pressure swing (SBP − DBP).
[^ety-invasive]: **invasive** — Latin *in-*, "into" + *vadere*, "to go" → going into the body (a needle or catheter in the artery). **Differentiate:** *invasive* (enters the body) vs *non-invasive* (from outside — cuff); *minimally invasive* (small entry).
[^ety-sphygmomanometer]: **sphygmomanometer** — Greek *sphygmos*, "pulse" + *manos*, "thin, rare" (as in *manometer*, a gauge for gases) + *metron*, "measure" → an instrument that measures the pressure of the pulse.
[^ety-korotkoff]: **Korotkoff sounds** — Nikolai Sergeyevich Korotkov (1874–1920), Russian surgeon, who in 1905 described listening below the cuff and using the appearance and disappearance of sounds to read systolic and diastolic pressure.
[^ety-murmur]: **murmur** — Latin *murmur*, "a humming, a low rumbling" (imitative of the sound) → the sound of turbulent flow heard with a stethoscope. **Differentiate:** *murmur* (turbulence in the heart or great vessels) · *bruit* (French "noise" — turbulence in a peripheral artery) · *thrill* (a murmur strong enough to be felt).
[^ety-obesity]: **obesity** — Latin *obesus*, "having eaten until fat" (*ob-* "over, completely" + *edere* "to eat") → excess body fat (BMI ≥ 30; ≥ 25 in Asian Indian cut-offs).
[^ety-calcified]: **calcified** — Latin *calx*, "lime, limestone" + *facere*, "to make" → made chalky by calcium salts deposited in the vessel wall.
[^ety-circumference]: **circumference** — Latin *circum-*, "around" + *ferre*, "to carry" → the line carried around; the distance around the mid-upper arm, used to choose the cuff.
[^ety-riva-rocci]: **Riva-Rocci cuff** — Scipione Riva-Rocci (1863–1937), Italian internist and paediatrician, who in 1896 introduced the easy-to-use mercury sphygmomanometer with an inflatable arm cuff; "RR" on old charts means a Riva-Rocci reading.
[^ety-auscultatory]: **auscultatory** — Latin *auscultare*, "to listen attentively" (*auris*, "ear") + *-ory*, "pertaining to" → by listening. **Differentiate:** *auscultation* (listening) · *palpation* (feeling) · *percussion* (tapping) · *inspection* (looking).
[^ety-atrium]: **atrium** — Latin *atrium*, "the entrance hall of a Roman house" → the receiving chamber of the heart; plural *atria*. Older name *auricle* ("little ear") now means only the atrial appendage.
[^ety-ventricle]: **ventricle** — Latin *ventriculus*, "little belly" (*venter*, "belly" + *-iculus*, "small") → a small cavity; the pumping chambers of the heart (and the CSF cavities of the brain).
[^ety-pulmonary]: **pulmonary** — Latin *pulmo*, "lung" + *-ary*, "pertaining to" → of the lungs; Greek equivalent *pneumon*.
[^ety-reynolds]: **Reynolds number** — Osborne Reynolds (1842–1912), Irish-born British engineer, whose 1883 dye-in-a-pipe experiments showed when flow turns from laminar to turbulent; the page spells it "Reynold's".
[^ety-laminar]: **laminar** — Latin *lamina*, "a thin plate, a layer" + *-ar*, "pertaining to" → flow in layers that slide over one another, fastest in the centre (parabolic profile), silent.
[^ety-turbulent]: **turbulent** — Latin *turba*, "a crowd, an uproar" (*turbulentus*, "full of commotion") → flow broken into eddies and whorls; it wastes energy and makes noise. Same root as *disturb*.
[^ety-transitional]: **transitional** — Latin *trans-*, "across" + *ire*, "to go" + *-tion* → going across from one state to another; the zone between laminar and turbulent flow.
[^ety-pregnancy]: **pregnancy** — Latin *prae-*, "before" + *gnasci / nasci*, "to be born" → the state before birth. Plasma volume rises more than red-cell mass → physiological (dilutional) anaemia.
[^ety-anaemia]: **anaemia** — Greek *an-*, "without" + *haima*, "blood" + *-ia*, "condition" → "lack of blood" — a low haemoglobin. **Differentiate:** *anaemia* (low Hb) · *hypovolaemia* (low blood volume) · *ischaemia* (blood held back from a tissue).
[^ety-laplace]: **Laplace's law** — Pierre-Simon, marquis de Laplace (1749–1827), French mathematician and astronomer, who with Thomas Young (1805–1806) related the pressure across a curved wall to its tension and radius (Young–Laplace equation).
[^ety-tension]: **tension** — Latin *tensio*, "a stretching" (*tendere*, "to stretch") → the pulling force in a wall per unit length. **Differentiate:** *tension* (force in the wall) · *pressure* (force per area on the wall from inside) · *stress* (tension per unit wall thickness).
[^ety-cardiomyopathy]: **cardiomyopathy** — Greek *kardia*, "heart" + *mys, myos*, "muscle" + *pathos*, "suffering, disease" + *-y* → disease of the heart muscle itself. **Differentiate** the three types: *dilated* (big thin chamber — systolic failure) · *hypertrophic* (thick wall — outflow obstruction) · *restrictive* (stiff wall — diastolic failure).
[^ety-aneurysm]: **aneurysm** — Greek *aneurysma*, "a widening" (*ana-* "up, throughout" + *eurys* "wide") → a permanent localised dilatation of an artery to ≥ 1.5 times its normal diameter. **Differentiate:** *true aneurysm* (all three wall layers) · *false (pseudo-) aneurysm* (a haematoma contained by the adventitia) · *dissection* (blood splitting the wall layers).
[^pre-haemo]: **haemo- / hemo- / haemat-** — blood: hemodynamics, haemorrhage, haematocrit, haemophilia. Don't confuse with **hemi-** half (hemiplegia) · **hepato-** liver.
[^suf-ics]: **-ics** — the science or study of: hemodynamics, physics, genetics, kinetics. Don't confuse with **-ic** simple adjective (cardiac) · **-ology** the study of (cardiology).
[^suf-osis]: **-osis** — a condition or process: stenosis, sclerosis, thrombosis. Don't confuse with **-iasis** disease due to an organism · **-itis** inflammation.
[^pre-hyper]: **hyper-** — over, above, excessive: hyperviscosity, hypertension, hypertrophic. Don't confuse with **hypo-** under, deficient · **supra- / super-** above (Latin).
[^pre-syn]: **syn- / sys- / sym-** — together: systolic (*sy-* before *s*), synapse, sympathetic. Don't confuse with **dia-** apart (diastolic).
[^pre-dia]: **dia-** — through, across, apart: diastolic, diameter, dialysis. Don't confuse with **di-** two · **dys-** bad, difficult (dyspnoea).
[^pre-in]: **in- (im-, il-, ir-)** — two different Latin prefixes: **in-** "into, in" (invasive, inspiration, infusion) and **in-** "not" (inactive, insufficient). Context decides. Don't confuse with **non-** not (non-invasive) · **en- / em-** in (Greek: endemic).
[^pre-intra]: **intra-** — within, inside: intraarterial, intracellular, intravascular. Don't confuse with **inter-** between (interstitial) · **intro-** into.
[^pre-sphygmo]: **sphygmo-** — pulse: sphygmomanometer, sphygmograph. Don't confuse with **sphincter** (a ring muscle) · **spheno-** wedge (sphenoid).
[^suf-meter]: **-meter / -metry** — an instrument for measuring / the act of measuring: sphygmomanometer, spirometer, oximetry. Don't confuse with **-graph** an instrument that records a trace (sphygmograph) · **-gram** the record itself (electrocardiogram) · **-scope** an instrument for viewing.
[^pre-circum]: **circum-** — around (Latin): circumference, circumflex, circumcision. Don't confuse with **peri-** around (Greek equivalent: pericardium) · **circa-** about, approximately (circadian).
[^suf-icle]: **-icle / -iculus / -cule** — small (diminutive): ventricle, follicle, molecule, ossicle. Don't confuse with **-cele** a swelling, hernia (hydrocele) · **-cyte** a cell.
[^suf-ar]: **-ar / -al / -ary** — pertaining to: laminar, valvular, renal, pulmonary. Don't confuse with **-ia** a condition · **-oid** resembling (sphenoid).
[^pre-trans]: **trans-** — across, through, beyond: transitional, transfusion, transmural. Don't confuse with **inter-** between · **dia-** through (Greek equivalent).
[^pre-an]: **a- / an- (before a vowel)** — without, not: anaemia, anoxia, afibrinogenaemia. Don't confuse with **ana-** up, again (anastomosis, aneurysm) · **ante-** before · **anti-** against.
[^suf-aemia]: **-aemia / -emia** — a condition of the blood: anaemia, hypoxaemia, uraemia, polycythaemia. Don't confuse with **-uria** a condition of the urine (proteinuria, haematuria) · **haemo-** blood as a prefix (haemorrhage).
[^pre-myo]: **myo- / my-** — muscle: cardiomyopathy, myocardium, myoglobin. Don't confuse with **myelo-** marrow, spinal cord (myeloma, myelitis) · **myco-** fungus (mycosis).
[^suf-pathy]: **-pathy** — disease, suffering: cardiomyopathy, neuropathy, nephropathy. Don't confuse with **-path** a practitioner (osteopath) · **-pathic** of unknown cause in *idiopathic*.
[^pre-ana]: **ana-** — up, again, throughout: aneurysm (*ana-* + *eurys*, widening throughout), anastomosis, anabolism. Don't confuse with **an- / a-** without (anaemia) · **anti-** against.
