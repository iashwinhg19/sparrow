---
title: Alveolar Ventilation and Pulmonary Circulation
aliases: [Alveolar ventilation, Dead space ventilation, Alveolar gas equation, West zones of the lung, Hypoxic pulmonary vasoconstriction]
rank: 26
status: not-started
topic: Physiology
subtopic: Respiratory System
chapter: 26
pages: "134–136"
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
source: "Physiology main notes (Marrow 8) — Alveolar Ventilation and Pulmonary Circulation, pp. 134–136 (sections: Ventilation 00:02:46 · Perfusion 00:38:57)"
mindmap: "[[Alveolar Ventilation and Pulmonary Circulation — Mind Map]]"
index: "[[Physiology — Index]]"
review_day_2: false
review_day_4: false
review_day_7: false
review_day_10: false
review_day_15: false
---
# 🌬️ Alveolar Ventilation and Pulmonary Circulation

> [!abstract] Core Definition
> **Ventilation**[^ety-ventilation][^suf-ation] brings air to the alveoli[^ety-alveolus][^suf-olus]; **perfusion**[^ety-perfusion][^pre-per] brings blood past them. Only the air that actually reaches perfused alveoli is **useful (alveolar) ventilation** — the rest fills the **dead space**. This chapter answers three questions:
> - ✅ **How much O₂ is in the alveolus?** → the **alveolar gas equation**: PAO₂ = PiO₂ − (PACO₂ / RER) ≈ **100 mmHg**
> - ✅ **How much of each breath is wasted?** → **dead space** (150 of 500 ml = **30 %**), measured by **Fowler's** (anatomical) and **Bohr's** (physiological) methods
> - ✅ **How does blood flow through the lung?** → a **low-pressure, highly distensible** circuit, divided by gravity into **zones I–III**, that **constricts where the alveolus is hypoxic**

---

## 🧠 Mental Model — Air Loses O₂ at Every Step; Blood Follows the Air

Follow one breath of air down to the blood. At each step something dilutes the O₂ — first water vapour, then the CO₂ coming out of the blood. And only the part of the breath that reaches a **perfused** alveolus counts:

```
STEP              WHAT HAPPENS                          PO2 (mmHg)     PCO2
Dry room air      21 % of 760                             160            0
Trachea           warmed + moist: 21 % of (760 − 47)      150            0
Alveolus          CO2 from blood dilutes O2: 150 − 40/0.8 100            40
Arterial blood    equilibrates with alveolus              100            40
Mixed venous      tissues took O2, gave CO2                40            46
Expired air       alveolar air + dead-space air           120            —

EACH BREATH (500 ml)  =  150 ml DEAD SPACE (no exchange)  +  350 ml ALVEOLAR (exchange)
Minute ventilation  = 500 × 12 = 6 L/min     Alveolar ventilation = 350 × 12 = 4.2 L/min

BLOOD SIDE: low pressure, distensible → gravity decides flow
APEX  zone I   PA > Pa > Pv   vessel squashed     → no flow
MID   zone II  Pa > PA > Pv   waterfall           → intermittent flow
BASE  zone III Pa > Pv > PA   vessel always open  → continuous flow
Hypoxic alveolus → its arteriole CONSTRICTS → blood goes where the air is
```

---

## 💨 Ventilation

![[Alveolar Ventilation and Pulmonary Circulation - ventilation perfusion matching at the alveolus.png]]
*Ventilation–perfusion matching — deoxygenated blood flows past the alveolus, O₂ enters the blood and CO₂ leaves it, and oxygenated blood flows on (exchange between O₂ and CO₂) (cropped from the handwritten page).*

![Alveolus with its capillary network — type I and type II cells, alveolar macrophage, capillary (Wikimedia Commons)](https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Alveolus_diagram.svg/800px-Alveolus_diagram.svg.png)
*The alveolus and its capillary — the site where useful ventilation meets perfusion (Mariana Ruiz Villarreal / LadyofHats, Wikimedia Commons, public domain).*

### Useful ventilation

> [!info] The air changes on its way to the alveolus
> Room air is **dry**; by the trachea it is **moist**, and in the alveolus it is **mixed with CO₂** from the blood. Each change lowers the PO₂ a little — that is why alveolar PO₂ is 100, not 160 mmHg.

#### Environmental air

- **Dry.**
- **Pressure: 760 mmHg.**
- **Composition:** N₂[^ety-nitrogen][^suf-gen] – **79 %**, O₂[^ety-oxygen] – **21 %**.

#### Inspired air[^ety-inspiration][^pre-in]

- **Moist.**
- **PO₂ ↓** (d/t **dilution**[^ety-dilution][^pre-di] by **water vapour pressure of 47 mmHg**).[^1]

#### Alveolar air

- **Alveolar gas equation:**

```latex
P_AO_2 = P_iO_2 - \left( \frac{P_ACO_2}{RER} \right)
```

- **P** : partial pressure; **A** : alveolar[^suf-ar] pressure; **i** : inspired air.
- **RER** : **Respiratory**[^ety-respiratory][^pre-re] **exchange ratio**:[^2]

```latex
RER = \frac{\text{Volume of CO}_2 \text{ produced}}{\text{Volume of O}_2 \text{ consumed}} = 0.8
```

- **The inspired PO₂:**

```latex
P_iO_2 = F_iO_2 \, (P_b - P_{H_2O})
```

- **Fi** : fractional concentration; **Pb** : atmospheric[^ety-atmosphere] pressure; **PH₂O** : water pressure.
- **Alveolar (A) – arterial (a) oxygen gradient**[^ety-gradient] = **P(A–a)O₂**.[^3]

🧠 *In words:* the O₂ the alveolus can hold = the O₂ breathed in, minus the room taken up by the CO₂ that the blood is pouring in. Because the body makes only 0.8 molecule of CO₂ for every molecule of O₂ it uses, the CO₂ term is divided by 0.8. Put in normal numbers: 0.21 × (760 − 47) − 40/0.8 = 150 − 50 = **100 mmHg**.

![[Alveolar Ventilation and Pulmonary Circulation - partial pressures from air to blood.png]]
*Partial pressures from air to blood — dry inspired air PO₂ 160 / PCO₂ 0 (21 % of 760 mmHg) → humidified tracheal air 150 / 0 → alveolar air PAO₂ 100 / PACO₂ 40 (d/t gas exchange) → systemic arterial blood 100 / 40; mixed venous blood PvO₂ 40 / PvCO₂ 46 (cropped from the handwritten page).*

> [!example] Worked example — alveolar gas equation
> **Eg:** Patient with **severe RDS**[^ety-syndrome][^pre-syn] is on **ventilator**, his **FiO₂ = 0.5**, **PO₂ = 160 mmHg**, **PCO₂ = 40 mmHg**, **barometric**[^ety-barometric][^pre-baro] **pressure = 747 mmHg**, **RER = 0.8**. Calculate **alveolar O₂ tension**[^ety-tension] and **alveolar–arterial O₂ gradient**.
>
> **Ans:** Alveolar gas equation,
> **PAO₂** = 0.5 − [(747 − 47) − 40] / 0.8 = 350 − 50 = **300 mmHg**.[^4]
>
> Alveolar arterial O₂ gradient,
> **P(A–a)O₂** = 300 − 60 = **140 mmHg**.[^5]

![[Alveolar Ventilation and Pulmonary Circulation - mouth-to-mouth breathing.png]]
*Mouth-to-mouth breathing — the rescuer's expired air still **provides 16 % of O₂**, enough to oxygenate a non-breathing patient (cropped from the handwritten page).*

#### Expired air[^ety-expiration][^pre-ex]

- **PEO₂ = 120 mmHg.**[^6]

### Dead space ventilation

🧠 Not all of a breath reaches the alveoli. The last part of every inspiration stays in the airways (nose → terminal bronchioles), where no gas exchange happens, and is the first part breathed out — that is the **dead space**.

#### Formulas

- **Total volume (V_T) = Dead space (V_D) + Alveolar ventilation (V_A).**[^7]

| Total volume (V_T) | Dead space (V_D) | Alveolar ventilation (V_A) |
|---|---|---|
| **500 ml** | **150 ml** | **350 ml** |

- **Alveolar ventilation (V_A/min) = (V_T − V_D) × Respiratory rate (RR)** [(500 − 150) × 12 = **4.2 L**].
  - **V_D / V_T = 150 / 500 = 30 %.**
- **Minute ventilation = V_T × RR/min** (500 × 12 = **6 L/min**).

> [!tip] Why alveolar ventilation, not minute ventilation, sets the blood gases
> Dead space is a fixed volume per breath. **Fast shallow breathing** (e.g. V_T 150 ml × RR 40 = 6 L/min) keeps minute ventilation normal but makes alveolar ventilation **zero** — every breath only shuttles dead-space air in and out. **Slow deep breathing** wastes the least.[^8]

#### Types

##### 1. Anatomical[^ety-anatomical][^pre-ana] dead space

- **Measured by: Single breath nitrogen method / Fowler's method**[^ety-fowler].

![[Alveolar Ventilation and Pulmonary Circulation - Fowler single breath nitrogen curve.png]]
*Single-breath nitrogen (Fowler's) method — one breath of 100 % O₂, then N₂ concentration is plotted against the volume breathed out. Phases I–IV, closing volume (CV), residual volume (RV) and closing capacity (CC) are marked (cropped from the handwritten page).*

| Phase | What is being breathed out |
|---|---|
| **I** | **Dead space air** (pure O₂ — no N₂) |
| **II** | **Dead space air + alveolar air** (N₂ rises steeply) |
| **III** | **Alveolar air** (the **alveolar plateau**[^ety-plateau]) |
| **IV** | **Alveoli close in dependent**[^ety-dependent][^pre-de] **part** (**CV – closing volume**)[^9] |
| **RV** | **Residual**[^ety-residual] **volume** — what stays in the lung at the end |

- **Dead space air: volume expired b/w the beginning of the expiration & midpoint of transition**[^ety-transition][^pre-trans] **phase** (phase II).

![[Alveolar Ventilation and Pulmonary Circulation - airway generations and anatomical dead space.png]]
*Airway generations (Weibel[^ety-weibel]) — trachea (generation 0) → bronchi → bronchioles → terminal bronchioles (16) form the **conducting zone = anatomical dead space**; respiratory bronchioles (17–19), alveolar ducts (20–22) and alveolar sacs (23) form the transitional and respiratory zones (cropped from the handwritten page).*

🧠 The anatomical dead space is the volume of the **conducting airways** (trachea[^ety-trachea] → bronchi[^ety-bronchus] → bronchioles[^suf-ole] → terminal bronchioles), which carry air but have no alveoli to exchange gas.

##### 2. Alveolar dead space

- **Normal: Nil.**
- **Pathological**[^ety-pathological][^suf-logy]**: dead space occurs** — alveoli that are ventilated but not perfused (e.g. pulmonary embolism, see [[Ventilation Perfusion Ratio]]).

##### 3. Total physiological[^ety-physiological] dead space

- **Normal: anatomical dead space.**
- **Pathological: alveolar + anatomical dead space.**
- **Measured by Bohr's equation**[^ety-bohr]:

```latex
V_D = V_T \times \frac{P_ACO_2 - P_ECO_2}{P_ACO_2}
```

🧠 *Why it works:* dead-space air has no CO₂, alveolar air has plenty. The more dead-space air dilutes the expired breath, the further the expired PCO₂ falls below the alveolar PCO₂ — the fraction by which it falls **is** the dead-space fraction.[^10]

| Dead space | Normal | Pathological | Measured by |
|---|---|---|---|
| **Anatomical** | ~150 ml (conducting airways) | — | **Fowler's** single-breath N₂ method |
| **Alveolar** | **Nil** | Dead space occurs | — |
| **Total physiological** | = anatomical | Alveolar + anatomical | **Bohr's equation** |

🎬 **Watch:** [Alveolar gas equation & A–a gradient (YouTube search)](https://www.youtube.com/results?search_query=alveolar+gas+equation+A-a+gradient+physiology) · [Dead space — anatomical vs physiological, Fowler & Bohr (YouTube search)](https://www.youtube.com/results?search_query=anatomical+physiological+dead+space+Fowler+Bohr+equation) · [Ninja Nerd — alveolar ventilation (YouTube search)](https://www.youtube.com/results?search_query=ninja+nerd+alveolar+ventilation+dead+space)

---

## 🩸 Perfusion

### Zones of perfusion

![[Alveolar Ventilation and Pulmonary Circulation - zones of perfusion.png]]
*Lung zones — the pulmonary artery (left, red) and vein (right, blue) as columns of blood: apex = zone I, middle = zone II, base = zone III; the capillary inside each alveolus is squashed, pinched or open (cropped from the handwritten page).*

| Zone | Part of lung | Pressures | Why |
|---|---|---|---|
| **Zone I** | **Apex** | **P_A > P_a > P_v** | (d/t **compression**[^ety-compression][^pre-con] of blood vessel) |
| **Zone II** | **Middle** | **P_a > P_A > P_v** | (d/t **intermittent**[^ety-intermittent][^pre-inter] flow / **waterfall effect**) |
| **Zone III** | **Base** | **P_a > P_v > P_A** | (d/t **continuous** blood flow) |

- **P_A : alveolar pressure** · **P_a : arterial**[^ety-artery] **pressure** · **P_v : venous**[^ety-vein] **pressure**.

🧠 Alveolar pressure is the same everywhere (≈ atmospheric), but blood pressure in the lung's vessels rises by about 1 cm H₂O for every cm you go down, because of gravity. At the apex the blood pressure is lowest, so the air in the alveoli can **squash** the capillary flat (zone I). In the middle the artery beats the alveolus but the vein does not, so flow depends on the arterial–alveolar difference and switches on and off like a **waterfall** over a dam (zone II). At the base both artery and vein beat the alveolus and the vessel stays **open** (zone III).[^11]

### Properties of pulmonary circulation

![Respiratory zone — terminal and respiratory bronchioles, alveolar duct, alveolar sacs with alveolar pores, and the capillary network fed by the pulmonary artery and drained by the pulmonary vein (OpenStax)](https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/2309_The_Respiratory_Zone.jpg/800px-2309_The_Respiratory_Zone.jpg)
*The respiratory zone — terminal bronchiole with smooth muscle, respiratory bronchiole, alveolar duct, alveolar sac, alveolar pores; deoxygenated blood from the pulmonary artery passes through the capillaries around each alveolus and leaves as oxygenated blood to the pulmonary vein — the same labels as the page's figure (OpenStax Anatomy & Physiology, CC BY 3.0).*

- **Pulmonary**[^ety-pulmonary][^suf-ary] **circulation**[^ety-circulation] **= right ventricular**[^ety-ventricle] **output = 5 L.**
- **Highly distensible**[^ety-distensible][^suf-ible].
- **Low pressure.**[^12]

> [!info] Why low pressure and distensible matter
> The whole cardiac output goes through the lungs at a mean pressure of only about 15 mmHg. When flow rises (exercise), the thin-walled vessels **open up closed capillaries (recruitment)** and **widen open ones (distension)**, so resistance falls and pressure hardly rises — protecting the lung from oedema.

Rotate the pulmonary circuit in 3D — right ventricle → pulmonary trunk → pulmonary arteries → lungs → pulmonary veins → left atrium:

```anatomed
# pulmonary circulation — retype a name with the plugin's autocomplete if it shows as "unmatched"
parts: right ventricle, pulmonary trunk, right pulmonary artery, left pulmonary artery, right lung, left lung, pulmonary veins, left atrium, trachea, right main bronchus, left main bronchus
detail: related
title: Pulmonary circulation — the low-pressure circuit
```

### Physiological response to hypoxia in pulmonary arteries

![[Alveolar Ventilation and Pulmonary Circulation - hypoxic pulmonary vasoconstriction.png]]
*Normal alveoli vs hypoxic alveoli — the vessel to the hypoxic alveolus is constricted, and blood is diverted to well-ventilated alveoli (cropped from the handwritten page).*

**Mechanism of vasoconstriction**[^ety-vasoconstriction][^pre-vaso] **(hypoxic pulmonary vasoconstriction)**[^ety-hypoxia][^pre-hypo][^suf-ia]:

```
Hypoxia
   ↓
O2-sensitive K+ channel closes
   ↓
K+ accumulates (inside the smooth-muscle cell)
   ↓
Depolarization
   ↓
Ca2+ channel opens in vascular smooth muscle
   ↓
Vasoconstriction
```

- **Hypoxia** → **O₂-sensitive K⁺ channel closes** → **K⁺ accumulates** → **depolarization**[^ety-depolarization] → **Ca²⁺ channel opens in vascular smooth muscle** → **vasoconstriction**.[^13]

> [!note] Note — the opposite in the systemic circulation
> **Effect of hypoxia on systemic**[^ety-systemic] **circulation → vasodilation (eg in kidney, heart).**[^14]
>
> 🧠 *Why the difference?* A tissue short of O₂ needs **more blood**, so systemic vessels dilate. A lung alveolus short of O₂ is **not getting air**, so sending blood there would be wasted — the pulmonary vessel constricts and sends the blood to alveoli that are ventilated. This keeps ventilation and perfusion matched.

🎬 **Watch:** [West zones of the lung (YouTube search)](https://www.youtube.com/results?search_query=west+zones+of+the+lung+pulmonary+blood+flow) · [Hypoxic pulmonary vasoconstriction mechanism (YouTube search)](https://www.youtube.com/results?search_query=hypoxic+pulmonary+vasoconstriction+mechanism) · [Pulmonary circulation physiology lecture (YouTube search)](https://www.youtube.com/results?search_query=pulmonary+circulation+physiology+lecture)

---

## Core Dictum & Pattern Recognition

> [!check]+ **🎯 Core Dictum - The Unifying Principle**
>
> Gas exchange happens only where **air and blood meet in the same alveolus**. On the air side, every step dilutes O₂ (water vapour 47 mmHg, then CO₂ ÷ RER), so the alveolus holds ~100 mmHg — and the part of each breath that never reaches a perfused alveolus (**dead space**, 30 % of V_T) is wasted, so **alveolar ventilation, not minute ventilation**, sets the blood gases. On the blood side, the pulmonary circuit is so **low-pressure** that **gravity** decides where blood goes (zones I–III), and the circuit **actively steers blood away from hypoxic alveoli** (hypoxic vasoconstriction).
>
> The alveolar gas equation is the bridge: it predicts what PAO₂ *should* be; the **A–a gradient** tells you how much is lost between the alveolus and the artery — a normal gradient means the lung is fine and the problem is ventilation; a wide gradient means the lung itself is failing.

> [!example]+ **📊 Clinical Pattern Recognition**
>
> Understanding how the condition progresses through stages helps you recognize it at different phases and predict outcomes.
>
> **Stage 1 - Normal Physiology:**
> V_T 500 ml, V_D 150 ml, RR 12 → minute ventilation 6 L/min, alveolar ventilation 4.2 L/min; PAO₂ 100, PACO₂ 40, small A–a gradient. Upright lung shows zones II–III; hypoxic vasoconstriction fine-tunes flow to each alveolus.
>
> **Stage 2 - Compensated/Early Pathology:**
> A local problem (a mucus plug, early pneumonia, a small embolus) creates a few poorly ventilated or poorly perfused alveoli. Hypoxic pulmonary vasoconstriction diverts blood from the hypoxic alveoli, and the patient breathes a little faster and deeper; arterial gases stay near normal and the A–a gradient widens only slightly.
>
> **Stage 3 - Decompensated/Overt Disease:**
> In severe disease (RDS, large embolism, COPD) the dead space and shunt grow beyond what compensation can cover: PaO₂ falls, the A–a gradient widens (140 mmHg in the worked example), and rapid shallow breathing worsens it by increasing the dead-space fraction. Global alveolar hypoxia (high altitude, COPD) makes hypoxic vasoconstriction act everywhere → pulmonary hypertension → right heart strain.
>
> **Progression Timeline:**
> Normal → local V/Q fault → hypoxic vasoconstriction + ↑ ventilation compensate → dead space / shunt grows → wide A–a gradient, hypoxaemia → global vasoconstriction → pulmonary hypertension → cor pulmonale
>
> **Why This Matters Clinically:**
> The A–a gradient sorts hypoxaemia at the bedside: normal gradient = hypoventilation or low inspired O₂ (fix the breathing or the air); wide gradient = diffusion, V/Q mismatch or shunt (fix the lung). On a ventilator, slower deeper breaths reduce wasted dead-space ventilation.

> [!warning]+ **🔍 Diagnostic Buzzwords & Pattern Recognition**
>
> These are the key terms, phrases, and clinical patterns that should immediately trigger specific diagnoses in your mind. When you see these in a clinical vignette or real patient, you should think of the associated condition instantly.
>
> **Buzzwords by Condition:**
>
> **Alveolar gas equation:** "FiO₂, barometric pressure, RER 0.8, calculate alveolar O₂ tension" → PAO₂ = FiO₂ (Pb − 47) − PaCO₂/0.8. Subtract 47 (water vapour) **before** multiplying by FiO₂.
>
> **A–a gradient:** "PAO₂ − PaO₂" → normal is small; a wide gradient means a lung problem (V/Q mismatch, shunt, diffusion), a normal one means hypoventilation or high altitude.
>
> **Anatomical dead space:** "single-breath nitrogen", "Fowler", "100 % O₂ then N₂ meter", "midpoint of phase II" → volume of the conducting airways, ~150 ml.
>
> **Physiological dead space:** "Bohr's equation", "(PACO₂ − PECO₂)/PACO₂" → anatomical + alveolar dead space.
>
> **Closing volume:** "phase IV", "dependent alveoli close" → small airways at the base close first at the end of expiration.
>
> **Zone I:** "P_A > P_a > P_v", "compression of vessel", "apex", "no flow" → seen only when alveolar pressure is high (PEEP) or arterial pressure is low (haemorrhage).
>
> **Zone II:** "waterfall", "intermittent flow", "P_a > P_A > P_v" → flow set by arterial − alveolar pressure, not arterial − venous.
>
> **Hypoxic pulmonary vasoconstriction:** "O₂-sensitive K⁺ channel closes → depolarisation → Ca²⁺ in" → diverts blood to ventilated alveoli; opposite of systemic vasodilation.
>
> **Visual/Imaging Buzzwords:**
> A nitrogen curve with a flat plateau and a late upswing = Fowler's curve with phase IV (closing volume). A lung drawn with three horizontal bands and collapsed/pinched/open capillaries = West's zones.
>
> **Severity Indicators:**
> V_D/V_T > 30 % = increased dead space (rises with rapid shallow breathing, embolism, COPD). A–a gradient 140 mmHg on FiO₂ 0.5 = severe gas-exchange failure (RDS).

> [!danger]+ **⚠️ Common Traps & Pitfalls**
>
> These are the mistakes that students and clinicians commonly make with this topic. Being aware of these traps helps you avoid diagnostic errors and answer tricky exam questions correctly.
>
> **Trap 1: Forgetting water vapour in PiO₂**
>
> **What students think:** Inspired PO₂ = 21 % × 760 = 160 mmHg.
>
> **Why this is wrong:** 160 mmHg is dry room air. Once air is warmed and humidified in the airways, water vapour takes 47 mmHg of the total pressure, so PiO₂ = 0.21 × (760 − 47) ≈ 150 mmHg. The alveolar gas equation uses this humidified value. In the worked example the 47 is subtracted from 747 before multiplying by 0.5.
>
> **How to avoid this trap:** "Subtract 47 first, then multiply by FiO₂, then subtract PaCO₂/0.8."
>
> **Trap 2: Treating minute ventilation as the measure of gas exchange**
>
> **What students think:** If minute ventilation is 6 L/min, the patient is ventilating normally.
>
> **Why this is wrong:** Each breath first refills 150 ml of dead space. Rapid shallow breaths (small V_T, high RR) keep minute ventilation normal while alveolar ventilation collapses, and PaCO₂ rises. Only (V_T − V_D) × RR reaches the alveoli.
>
> **How to avoid this trap:** Always compute alveolar ventilation: (500 − 150) × 12 = 4.2 L, not 6 L.
>
> **Trap 3: Mixing up the methods for dead space**
>
> **What students think:** Bohr's equation measures anatomical dead space.
>
> **Why this is wrong:** Fowler's single-breath nitrogen method measures **anatomical** dead space (conducting airways). Bohr's equation, using CO₂, measures **total physiological** dead space — anatomical plus alveolar. Normally the two are equal because alveolar dead space is nil.
>
> **How to avoid this trap:** "**F**owler = **F**ixed airways (anatomical); **B**ohr = **B**oth (anatomical + alveolar)."
>
> **Trap 4: Getting the zone pressures in the wrong order**
>
> **What students think:** Zone III has the highest alveolar pressure.
>
> **Why this is wrong:** Alveolar pressure is the same throughout the lung; what changes with height is vascular pressure. At the base, gravity adds to arterial and venous pressure so both exceed P_A (zone III: P_a > P_v > P_A). At the apex both vascular pressures are lowest, so P_A comes first (zone I: P_A > P_a > P_v).
>
> **How to avoid this trap:** Read the zone number as the position of P_A in the inequality: zone I → P_A **1st**, zone II → P_A **2nd**, zone III → P_A **3rd**.
>
> **Trap 5: Saying hypoxia dilates all vessels**
>
> **What students think:** Hypoxia always causes vasodilation.
>
> **Why this is wrong:** Systemic vessels (kidney, heart) dilate in hypoxia to bring more O₂ to the tissue. Pulmonary vessels do the opposite — O₂-sensitive K⁺ channels close, the muscle depolarises, Ca²⁺ enters and the vessel constricts — so blood is diverted to ventilated alveoli. Global hypoxia (altitude, COPD) therefore causes pulmonary hypertension.
>
> **How to avoid this trap:** "Lungs constrict, the rest dilate."

> [!tip]+ **🔗 Related Concepts & Cross-Topic Connections**
>
> Understanding how this topic connects to other areas of medicine deepens your knowledge and helps you see the bigger picture. These connections also help you answer integrated questions on exams.
>
> **Related Topic 1: [[Lung Volumes and Capacities]]**
> Tidal volume (500 ml), residual volume, closing volume and closing capacity used in this chapter's formulas and Fowler's curve are defined there.
>
> **Related Topic 2: [[Structure Function Relationship in Lungs]]**
> The conducting zone (generations 0–16) that forms the anatomical dead space and the respiratory zone (17–23) where exchange happens are described there.
>
> **Related Topic 3: [[Ventilation Perfusion Ratio]]**
> Alveolar dead space (V/Q = ∞) and shunt (V/Q = 0), the apex-to-base V/Q gradient and the O₂–CO₂ diagram continue directly from zones of perfusion.
>
> **Related Topic 4: [[Diffusion and Transport of Gases]]**
> What happens after the alveolus: diffusion across the respiratory membrane and the O₂–Hb dissociation curve that turns PaO₂ 100 into ~97 % saturation.
>
> **Related Topic 5: [[Environmental Physiology]]**
> At altitude the barometric pressure in the alveolar gas equation falls, PAO₂ falls, and global hypoxic pulmonary vasoconstriction produces pulmonary hypertension.
>
> **Clinical Integration:**
> The alveolar gas equation and A–a gradient are bedside tools for every hypoxaemic patient; dead-space thinking guides ventilator settings (avoid rapid shallow breaths); hypoxic pulmonary vasoconstriction explains why vasodilator drugs can worsen oxygenation in pneumonia and why COPD and altitude cause cor pulmonale.
>
> **Exam Integration:**
> Expect a numerical (calculate PAO₂ and the A–a gradient), the normal values (V_D 150 ml, V_D/V_T 30 %, V_A 4.2 L/min, minute ventilation 6 L/min, PEO₂ 120), Fowler vs Bohr, the order of pressures in each West zone, and the ion-channel sequence of hypoxic pulmonary vasoconstriction.

---

## 🏆 Pearls (High-Yield Summary)

> [!success] Must-Know Pearls
> 1. Environmental air: **dry, 760 mmHg, N₂ 79 %, O₂ 21 %** → dry PO₂ **160 mmHg**; humidified tracheal air **150 mmHg** (water vapour **47 mmHg**).
> 2. **Alveolar gas equation: PAO₂ = PiO₂ − (PACO₂ / RER)**; **PiO₂ = FiO₂ (Pb − PH₂O)**; **RER = CO₂ produced / O₂ consumed = 0.8**.
> 3. Alveolar air: PAO₂ **100**, PACO₂ **40**; mixed venous **40 / 46**; expired PEO₂ **120 mmHg**; mouth-to-mouth air provides **16 % O₂**.
> 4. **P(A–a)O₂** = alveolar − arterial O₂ gradient; worked example (FiO₂ 0.5, Pb 747): PAO₂ **300**, gradient **140 mmHg**.
> 5. **V_T = V_D + V_A** → **500 = 150 + 350 ml**; **V_D/V_T = 30 %**.
> 6. **Alveolar ventilation = (V_T − V_D) × RR = 4.2 L/min**; **minute ventilation = V_T × RR = 6 L/min**.
> 7. **Anatomical dead space** — **single-breath nitrogen / Fowler's method**; = volume expired from start of expiration to the **midpoint of the transition phase (II)**.
> 8. Fowler's phases: **I dead-space air · II mixed · III alveolar plateau · IV dependent alveoli close (closing volume)**.
> 9. **Alveolar dead space** normally **nil**; **total physiological** = anatomical (normal) or alveolar + anatomical (disease) — **Bohr's equation: V_D = V_T × (PACO₂ − PECO₂)/PACO₂**.
> 10. **Zones:** I apex **P_A > P_a > P_v** (compression) · II middle **P_a > P_A > P_v** (intermittent, **waterfall**) · III base **P_a > P_v > P_A** (continuous).
> 11. Pulmonary circulation = **RV output = 5 L**, **highly distensible, low pressure**.
> 12. **Hypoxia → O₂-sensitive K⁺ channel closes → K⁺ accumulates → depolarisation → Ca²⁺ channel opens → vasoconstriction**; in systemic vessels hypoxia → **vasodilation** (kidney, heart).

---

## 🔁 One-Line Recall

```
AIR 160 → TRACHEA 150 (−47 water) → ALVEOLUS 100/40 (PAO2 = PiO2 − PACO2/0.8) → ARTERY 100/40 → VEIN 40/46 → EXPIRED 120
BREATH 500 = DEAD SPACE 150 + ALVEOLAR 350 · VD/VT 30 % · VA = 350 × 12 = 4.2 L · VE = 500 × 12 = 6 L
DEAD SPACE: anatomical (Fowler, N2, midpoint of phase II) · alveolar (nil normally) · physiological (Bohr, CO2)
ZONES: I apex PA>Pa>Pv squashed · II mid Pa>PA>Pv waterfall · III base Pa>Pv>PA continuous
PULMONARY CIRCULATION: 5 L, distensible, low pressure · HYPOXIA → K+ shut → depolarise → Ca2+ in → CONSTRICT (systemic: DILATE)
```

---

## 🎬 Video Library

| What to watch | Link |
|---|---|
| Alveolar gas equation and the A–a gradient (YouTube search) | https://www.youtube.com/results?search_query=alveolar+gas+equation+A-a+gradient+physiology |
| Dead space — anatomical vs physiological, Fowler's method & Bohr's equation (YouTube search) | https://www.youtube.com/results?search_query=anatomical+physiological+dead+space+Fowler+Bohr+equation |
| West zones of the lung — pulmonary blood flow (YouTube search) | https://www.youtube.com/results?search_query=west+zones+of+the+lung+pulmonary+blood+flow |
| Hypoxic pulmonary vasoconstriction — mechanism (YouTube search) | https://www.youtube.com/results?search_query=hypoxic+pulmonary+vasoconstriction+mechanism |

---

## 🖼 Infographic Prompt — One-Page Summary

> [!abstract]- 🎨 Prompt for an image generator (copy everything inside)
> "Design a single-page, portrait A4 medical study infographic titled **'ALVEOLAR VENTILATION AND PULMONARY CIRCULATION'** for a postgraduate physiology exam. Flat-vector textbook style, off-white background; colour code: sky blue = air and ventilation, red = arterial/oxygenated blood, purple = venous blood, grey = dead space, amber = formulas. Thin icons, crisp legible text, generous white space. Four panels in a 2 × 2 grid:
>
> **Panel 1 — 'Useful ventilation'.** A vertical ladder from room air to blood with PO₂/PCO₂ boxes: 'Environmental air — dry, 760 mmHg, N₂ 79 %, O₂ 21 % → PO₂ 160'; 'Inspired (tracheal) air — moist, PO₂ 150 (diluted by water vapour 47 mmHg)'; 'Alveolar air PAO₂ 100 / PACO₂ 40'; 'Systemic arterial 100 / 40'; 'Mixed venous 40 / 46'; 'Expired PEO₂ 120'. Amber formula boxes: 'PAO₂ = PiO₂ − PACO₂/RER', 'PiO₂ = FiO₂ (Pb − PH₂O)', 'RER = CO₂ produced / O₂ consumed = 0.8', 'P(A–a)O₂ = alveolar − arterial'. A small worked example card: 'RDS on ventilator, FiO₂ 0.5, Pb 747 → PAO₂ = 0.5 × 700 − 40/0.8 = 300; gradient 140 mmHg'. A small mouth-to-mouth icon: 'expired air provides 16 % O₂'.
>
> **Panel 2 — 'Dead space ventilation'.** A bar split 150 ml grey + 350 ml blue labelled 'V_T 500 = V_D 150 + V_A 350; V_D/V_T 30 %'. Formulas: 'Alveolar ventilation = (V_T − V_D) × RR = 4.2 L/min'; 'Minute ventilation = V_T × RR = 6 L/min'. A Fowler's curve (N₂ % vs volume) with phases I dead-space air, II mixed, III alveolar plateau, IV closing volume, and RV marked. A branching airway tree numbered 0–23 with 0–16 bracketed 'anatomical dead space (conducting zone)'. A three-row table: anatomical (Fowler) · alveolar (nil normally) · total physiological (Bohr: V_D = V_T × (PACO₂ − PECO₂)/PACO₂).
>
> **Panel 3 — 'Zones of perfusion & properties'.** An upright lung outline in three bands: apex zone I 'P_A > P_a > P_v — vessel compressed', middle zone II 'P_a > P_A > P_v — intermittent flow, waterfall', base zone III 'P_a > P_v > P_A — continuous flow', each with a drawn capillary (flat / pinched / open). Side card 'Pulmonary circulation = RV output 5 L; highly distensible; low pressure'.
>
> **Panel 4 — 'Hypoxia in pulmonary arteries'.** Two alveoli — normal and hypoxic — with the hypoxic one's vessel constricted and an arrow 'blood diverted to well-ventilated alveoli'. A vertical chain: 'Hypoxia → O₂-sensitive K⁺ channel closes → K⁺ accumulates → depolarisation → Ca²⁺ channel opens in vascular smooth muscle → vasoconstriction'. Contrast box: 'Systemic circulation: hypoxia → vasodilation (kidney, heart)'.
>
> Footer strip: 'PAO₂ 100 · V_D 150 ml = 30 % · V_A 4.2 L · zones I–II–III · lungs constrict, the rest dilate'. No watermark, no photographs, illustration quality."

---

## 📚 References

- Physiology main notes (Marrow 8) — *Alveolar Ventilation and Pulmonary Circulation*, pp. 134–136
- Guyton & Hall Textbook of Medical Physiology — Pulmonary ventilation; Pulmonary circulation, pulmonary edema, pleural fluid; Principles of gas exchange
- West JB — *Respiratory Physiology: The Essentials* (ventilation, blood flow and the zones of the lung)
- Ganong's Review of Medical Physiology — Gas transport and pH; pulmonary circulation
- OpenStax *Anatomy & Physiology* (CC BY) — 22.1 Organs and structures of the respiratory system
- Wikimedia Commons — embedded web images (licence noted in captions); `Alveolar Ventilation and Pulmonary Circulation - ….png` files in `attachments/` are crops of the handwritten pages

[^1]: At body temperature (37 °C) air in the airways is fully saturated with water vapour at 47 mmHg whatever the altitude. That pressure is taken out of the total before the O₂ fraction is applied: 0.21 × (760 − 47) ≈ 150 mmHg, the "humidified tracheal air" value in the figure.
[^2]: **RER vs RQ:** the *respiratory exchange ratio* is measured at the mouth (gas exchanged by the lungs); the *respiratory quotient* is the same ratio at the level of tissue metabolism. In a steady state they are equal — 1.0 for pure carbohydrate, 0.7 for fat, ~0.8 for protein and for the usual mixed diet.
[^3]: A healthy young adult breathing room air has an A–a gradient of roughly 5–15 mmHg; it widens with age and with any diffusion defect, V/Q mismatch or shunt, but stays normal in pure hypoventilation and at high altitude.
[^4]: The page's working puts the brackets in an odd place; the arithmetic it actually does is PAO₂ = FiO₂ × (Pb − PH₂O) − PaCO₂/RER = 0.5 × (747 − 47) − 40/0.8 = 350 − 50 = 300 mmHg, which is the answer the page gives.
[^5]: The page writes "300 − 60"; the question gives the patient's arterial PO₂ as **160 mmHg**, and 300 − 160 = **140 mmHg**, the answer the page gives. "60" is a slip for "160" (300 − 60 would be 240).
[^6]: Mixed expired air is alveolar air (PO₂ 100) diluted with dead-space air (PO₂ ~150), so it ends up between them — about 116–120 mmHg, ~16 % O₂ and ~4 % CO₂. That 16 % is why expired air from a rescuer still oxygenates a patient in mouth-to-mouth breathing.
[^7]: V_T is the **tidal volume** — the page writes "Total volume". The V_A in this equation is the alveolar *volume* of each breath (350 ml); multiplied by the respiratory rate it becomes alveolar *ventilation* (4.2 L/min). Anatomical dead space is roughly 1 ml per pound (≈ 2.2 ml/kg) of body weight.
[^8]: Worked contrast (Guyton): V_T 150 ml × RR 40 = 6 L/min minute ventilation, but (150 − 150) × 40 = 0 alveolar ventilation; V_T 1000 ml × RR 6 = 6 L/min, but (1000 − 150) × 6 = 5.1 L/min alveolar ventilation. Same minute ventilation, very different gas exchange.
[^9]: At the end of a full expiration the small airways at the **base** (the dependent part of the upright lung) close first. The gas still coming out then comes mainly from the **apex**, whose alveoli received less of the 100 % O₂ breath and so hold more N₂ — hence the late upswing (phase IV). Closing volume is about 10 % of vital capacity in the young, rises with age and is an early sign of small-airway disease in smokers; **closing capacity (CC) = CV + RV**.
[^10]: Bohr's original equation (1891) uses alveolar PCO₂. In practice arterial PCO₂ is substituted for it (Enghoff's modification, 1938), which gives the **total physiological** dead space, because arterial PCO₂ reflects only perfused alveoli. Normal V_D/V_T is about 0.2–0.35.
[^11]: West's zones (John B. West and colleagues, 1964). In a normal upright lung **zone I does not exist**: pulmonary arterial pressure is just enough to perfuse the apex. Zone I appears when alveolar pressure is raised (positive-pressure ventilation, PEEP) or arterial pressure falls (haemorrhage) — and it is alveolar dead space. Some texts add a zone IV at the extreme base, where interstitial pressure reduces flow.
[^12]: Pulmonary artery pressure is about 25/8 mmHg (mean ~15 mmHg), pulmonary capillary pressure ~7 mmHg and left atrial pressure ~2–8 mmHg; pulmonary vascular resistance is about one-tenth of systemic. The lungs hold ~450 ml of blood (~9 % of blood volume), which is why they act as a blood reservoir.
[^13]: Hypoxic pulmonary vasoconstriction is also called the **Euler–Liljestrand mechanism** (Ulf von Euler and Göran Liljestrand, 1946). The O₂-sensitive channels are voltage-gated K⁺ (Kv) channels of the pulmonary artery smooth muscle; the Ca²⁺ channels opened are L-type voltage-gated channels. In the fetus it keeps pulmonary resistance high; at the first breath alveolar PO₂ rises, the vessels relax and pulmonary resistance falls.
[^14]: In systemic arterioles hypoxia opens ATP-sensitive K⁺ channels (hyperpolarisation → relaxation) and releases local vasodilators (adenosine, NO, lactate, H⁺) — metabolic autoregulation of the coronary, renal and cerebral beds.
[^ety-ventilation]: **ventilation** — Latin *ventus*, "wind" → *ventilare*, "to fan, to winnow" + *-ation*, the process → the process of moving air in and out. **Differentiate:** *ventilation* (bulk air movement) · *respiration* (gas exchange — external at the lung, internal at the tissue, cellular in mitochondria) · *perfusion* (blood flow).
[^ety-alveolus]: **alveolus / alveolar** — Latin *alveus*, "a hollow, a trough" + *-olus*, small → a small hollow; plural *alveoli*. The same word names the tooth socket (*alveolar* bone) — context decides.
[^ety-perfusion]: **perfusion** — Latin *per-*, "through" + *fundere*, "to pour" + *-ion*, the process → pouring through; blood flow through a capillary bed. **Differentiate:** *perfusion* (flow through) · *infusion* (pouring in, e.g. a drip) · *effusion* (pouring out into a cavity) · *diffusion* (spreading apart).
[^ety-nitrogen]: **nitrogen** — Greek *nitron*, "native soda, saltpetre" + *-genēs*, "producing" → saltpetre-maker (named by Chaptal, 1790). It is inert in the body, which is why it is used as the marker gas in Fowler's method.
[^ety-oxygen]: **oxygen** — Greek *oxys*, "sharp, acid" + *-genēs*, "producing" → acid-maker; named by Antoine Lavoisier (1777), who wrongly believed all acids contained it.
[^ety-inspiration]: **inspiration** — Latin *in-*, "into" + *spirare*, "to breathe" + *-ation*, the process → breathing in. **Differentiate:** *inspiration* (in) · *expiration* (out — *ex-*) · *respiration* (*re-* again — breathing over and over; also gas exchange) · *aspiration* (*ad-* towards — drawing something into the airway).
[^ety-dilution]: **dilution** — Latin *di-* (*dis-*), "apart" + *luere*, "to wash" + *-ion* → washing apart, thinning out; here water vapour "thins" the O₂ in the inspired air. **Differentiate:** *dilution* (less concentrated) · *dilation* (*dis-* + *latus*, "wide" — widening of a vessel).
[^ety-respiratory]: **respiratory** — Latin *re-*, "again" + *spirare*, "to breathe" + *-atory*, "relating to" → relating to breathing again and again.
[^ety-atmosphere]: **atmosphere / atmospheric** — Greek *atmos*, "vapour, steam" + *sphaira*, "ball, globe" → the ball of vapour around the earth; one atmosphere = 760 mmHg at sea level.
[^ety-gradient]: **gradient** — Latin *gradi*, "to step, to walk" (*gradus*, a step) → a step-down from one value to another; the A–a gradient is the step-down in PO₂ from alveolus to artery.
[^ety-syndrome]: **syndrome** — Greek *syn-*, "together" + *dromos*, "a running" → things that run together, a set of signs occurring together. RDS = respiratory distress syndrome (in adults, ARDS). **Differentiate:** *syndrome* (a recognisable cluster) · *disease* (a defined cause and pathology) · *sign* (seen by the doctor) · *symptom* (felt by the patient).
[^ety-barometric]: **barometric** — Greek *baros*, "weight" + *metron*, "measure" + *-ic* → measuring the weight of the air; barometric pressure = atmospheric pressure (760 mmHg at sea level, lower at altitude).
[^ety-tension]: **tension (gas tension)** — Latin *tendere*, "to stretch" + *-ion* → stretching; in respiratory physiology "O₂ tension" means the **partial pressure** of O₂ dissolved in a liquid. **Differentiate:** *tension* (partial pressure, mmHg) · *content* (ml O₂/100 ml blood) · *saturation* (% of Hb bound).
[^ety-expiration]: **expiration** — Latin *ex-*, "out" + *spirare*, "to breathe" + *-ation* → breathing out. The same word means dying ("breathing one's last") and the end date of something.
[^ety-anatomical]: **anatomical** — Greek *ana-*, "up, throughout" + *tomē*, "a cutting" → cutting up (dissection) → relating to structure. *Anatomical* dead space = space set by the structure of the airways, not by disease.
[^ety-fowler]: **Fowler's method** — Ward S. Fowler, American physiologist, who in 1948 described measuring the respiratory dead space from the nitrogen concentration of a single expired breath after one breath of 100 % O₂.
[^ety-plateau]: **plateau** — French, "a flat tray, a tableland" (Old French *platel*, from *plat*, "flat") → the flat part of a curve; the alveolar plateau is phase III, where the N₂ concentration hardly changes.
[^ety-dependent]: **dependent** — Latin *de-*, "down from" + *pendere*, "to hang" → hanging down; the *dependent part* of an organ is its lowest part under gravity (the base in the upright lung, the back when lying supine). Same root as *pendulum* and *appendix*.
[^ety-residual]: **residual** — Latin *re-*, "back" + *sidere*, "to sit, settle" → what sits behind, the remainder; residual volume = air left in the lung after a maximal expiration.
[^ety-transition]: **transition** — Latin *trans-*, "across" + *ire*, "to go" + *-ition* → going across; the transition phase (II) of Fowler's curve is where expired gas changes from dead-space air to alveolar air.
[^ety-weibel]: **Weibel model** — Ewald R. Weibel (1929–2019), Swiss anatomist, whose *Morphometry of the Human Lung* (1963) numbered the airways as 23 generations of dichotomous branching from the trachea (0) to the alveolar sacs (23).
[^ety-trachea]: **trachea** — Greek *tracheia (artēria)*, "rough (air-pipe)" — rough because of its cartilage rings, to distinguish it from the smooth *artēria* (arteries were once thought to carry air).
[^ety-bronchus]: **bronchus / bronchiole** — Greek *bronchos*, "windpipe, throat" → bronchus (plural *bronchi*); + Latin diminutive *-iole* → *bronchiole*, a small bronchus (< 1 mm, no cartilage).
[^ety-pathological]: **pathological** — Greek *pathos*, "suffering, disease" + *logos*, "study" + *-ical* → relating to disease. **Differentiate:** *pathological* (caused by disease) · *physiological* (normal function) · *pathognomonic* (a sign specific to one disease).
[^ety-physiological]: **physiological** — Greek *physis*, "nature" + *logos*, "study" + *-ical* → relating to the normal workings of nature (the body). *Physiological dead space* is "the dead space that function sees" — every ventilated space without exchange, whatever its cause.
[^ety-bohr]: **Bohr's equation** — Christian Bohr (1855–1911), Danish physiologist at Copenhagen, who published the dead-space equation in 1891 and described the Bohr effect (CO₂/H⁺ lowering Hb's O₂ affinity) in 1904; father of the physicist Niels Bohr.
[^ety-compression]: **compression** — Latin *com-*, "together" + *premere*, "to press" + *-ion* → pressing together; in zone I the alveolar pressure presses the capillary walls together. **Differentiate:** *compression* (squeezed from outside) · *constriction* (narrowed by its own muscle) · *obstruction* (blocked from inside).
[^ety-intermittent]: **intermittent** — Latin *inter-*, "between" + *mittere*, "to send, let go" → letting go at intervals; flow that stops and starts. **Differentiate:** *intermittent* (on–off) · *continuous* (Latin *con-* + *tenere*, "to hold together" — never stops) · *pulsatile* (rises and falls but never stops).
[^ety-artery]: **artery / arterial** — Greek *artēria*, originally "windpipe" (from *aeirein*, "to raise" or *aēr*, "air"); ancient anatomists found arteries empty after death and thought they carried air. The **P_a** of this chapter is pulmonary arterial pressure.
[^ety-vein]: **vein / venous** — Latin *vena*, "a blood vessel, a channel"; *venous* = of the veins. In the pulmonary circuit the **veins** carry oxygenated blood and the **arteries** deoxygenated blood — the reverse of the systemic circuit.
[^ety-pulmonary]: **pulmonary** — Latin *pulmo*, "lung" + *-arius*, "relating to" → relating to the lungs. The Greek equivalent is *pneumōn* (pneumonia). **Differentiate:** *pulmonary* (lung) · *pulmonic* (the pulmonary valve, as in pulmonic stenosis).
[^ety-circulation]: **circulation** — Latin *circulus*, "a small ring" (diminutive of *circus*) + *-ation* → going round in a ring; William Harvey (1628) proved the blood circulates. **Pulmonary** (right heart → lungs → left heart) vs **systemic** (left heart → body → right heart).
[^ety-ventricle]: **ventricle** — Latin *ventriculus*, "little belly" (diminutive of *venter*, belly) → a small cavity; the right ventricle pumps the pulmonary circulation, the left the systemic. Same word for the brain ventricles.
[^ety-distensible]: **distensible** — Latin *dis-*, "apart" + *tendere*, "to stretch" + *-ible*, "able to be" → able to be stretched apart. **Differentiate:** *distensibility* (fractional change in volume per unit pressure) · *compliance* (absolute change in volume per unit pressure = distensibility × volume) · *elasticity* (tendency to spring back — the opposite of compliance).
[^ety-vasoconstriction]: **vasoconstriction** — Latin *vas*, "vessel" + *con-*, "together" + *stringere*, "to draw tight" + *-ion* → drawing a vessel tight. **Differentiate:** *vasoconstriction* (lumen narrowed) · *vasodilation* (*dis-* + *latus*, "wide" — lumen widened) · *vasospasm* (sudden excessive constriction).
[^ety-hypoxia]: **hypoxia** — Greek *hypo-*, "under" + *oxy-* (from oxygen) + *-ia*, a condition → a condition of too little O₂. **Differentiate:** *hypoxia* (low O₂ at the tissue or alveolus) · *hypoxaemia* (*-aemia*, "in the blood" — low PaO₂) · *anoxia* (*an-*, "without" — no O₂) · *asphyxia* (low O₂ **and** high CO₂).
[^ety-depolarization]: **depolarization** — Latin *de-*, "removal, down from" + Greek *polos*, "pole, axis" + *-ization*, "the process of making" → removing the polarity (the negative inside) of a membrane. **Differentiate:** *depolarisation* (inside less negative) · *repolarisation* (*re-*, back to the resting value) · *hyperpolarisation* (*hyper-*, more negative than rest).
[^ety-systemic]: **systemic** — Greek *systēma*, "an organised whole" (*syn-*, "together" + *histanai*, "to set") + *-ic* → relating to the whole body; the systemic circulation supplies all organs except the gas-exchanging lung.
[^suf-ation]: **-ation / -ition / -ion** — the process or result of an action: ventilation, circulation, inspiration, expiration, compression, dilution, transition, vasoconstriction. Don't confuse with **-osis** a condition or state (fibrosis) · **-ia** a condition (hypoxia).
[^suf-olus]: **-olus / -ulus / -ole / -ule** — small (Latin diminutive): alveolus (small hollow), arteriole, venule, bronchiole, ventriculus. Don't confuse with **-ium** a structure or layer (endothelium) · **-oma** a tumour.
[^pre-per]: **per-** — through, thoroughly: perfusion, permeable, percutaneous. Don't confuse with **peri-** around (pericardium) · **pre-** before · **para-** beside.
[^suf-gen]: **-gen / -genic** — producing, giving rise to: nitrogen, oxygen, pathogen, erythrogenic. Don't confuse with **-genesis** the process of formation (angiogenesis) · **-gnosis** knowledge (diagnosis).
[^pre-in]: **in- (im-, il-)** — into, in: inspiration, inspired, infusion, influx. Don't confuse with the other **in-** "not" (incompetent, insoluble) · **intra-** within · **inter-** between.
[^pre-di]: **di- / dis- / dif-** — apart, away, in different directions: dilution, distensible, diffusion, dissociation. Don't confuse with Greek **di-** two (dioxide, diphosphoglycerate) · **dia-** through (diaphragm) · **dys-** bad, difficult (dyspnoea).
[^suf-ar]: **-ar / -ary / -al** — relating to: alveolar, pulmonary, arterial, residual. Don't confuse with **-ia** a condition · **-ity** a quality (capacity).
[^pre-re]: **re-** — back, again: respiratory, residual, recruitment, reflex. Don't confuse with **retro-** backwards, behind (retroperitoneal) · **pre-** before.
[^pre-syn]: **syn- / sym-** — together, with: syndrome, systemic (*sy-* before *s*), synapse. Don't confuse with **sin-** (Latin, left) · **semi-** half.
[^pre-baro]: **baro-** — weight, pressure: barometric, baroreceptor, barotrauma. Don't confuse with **brady-** slow · **bari-** heavy (bariatric — same root, used for body weight).
[^pre-ex]: **ex- (e-, ef-)** — out of: expiration, expired, effusion, exchange. Don't confuse with **exo-** outside (Greek: exocrine) · **extra-** beyond, outside (extrapulmonary).
[^pre-ana]: **ana-** — up, throughout, again: anatomical (cutting up), anabolism (building up), anaphylaxis. Don't confuse with **an- / a-** without (anoxia, apnoea) · **ante-** before · **anti-** against.
[^pre-de]: **de-** — down from, removal, reversal: dependent (hanging down), depolarisation (removing polarity), deoxygenated, decompression. Don't confuse with **di- / dis-** apart · **dia-** through.
[^pre-trans]: **trans-** — across, through: transition, transport, transection, transmural. Don't confuse with **inter-** between · **per-** through (thoroughly) · **dia-** through (Greek).
[^suf-ole]: **-iole / -ole / -ule** — small: bronchiole, arteriole, venule. Don't confuse with **-ol** an alcohol (cholesterol, glycerol) · **-ole** in chemistry (imidazole — a ring compound).
[^suf-logy]: **-logy / -logical** — the study of, relating to: pathological, physiological, pathology, cytology. Don't confuse with **-logue** speech, discourse (dialogue) · **-nomy** law, arrangement (anatomy is *-tomy*, a cutting).
[^pre-con]: **con- / com- / co-** — together, with, thoroughly: compression, constriction, continuous, compliance, content. Don't confuse with **contra-** against (contraindication) · **counter-** against (countercurrent).
[^pre-inter]: **inter-** — between, among: intermittent, interstitial, intercostal. Don't confuse with **intra-** within (intrapleural) · **infra-** below (infraclavicular).
[^suf-ary]: **-ary / -arius** — relating to, connected with: pulmonary, coronary, capillary, ciliary. Don't confuse with **-arium** a place for (aquarium, sanatorium) · **-ory** relating to an action (respiratory, circulatory).
[^suf-ible]: **-ible / -able** — able to be: distensible, compressible, reversible, permeable. Don't confuse with **-ility** the noun of the same quality (distensibility, permeability) · **-ile** relating to (febrile, contractile).
[^pre-vaso]: **vaso-** — vessel (Latin *vas*): vasoconstriction, vasodilation, vasopressin, vasa vasorum. Don't confuse with **vas deferens** (the duct that carries sperm — same root, a "vessel" that carries away) · **angio-** vessel (Greek synonym: angiogenesis).
[^pre-hypo]: **hypo-** — under, below, deficient: hypoxia, hypoxaemia, hypoventilation, hypotension. Don't confuse with **hyper-** over, excessive (hyperventilation) · **hypno-** sleep · **sub- / infra-** below (Latin equivalents).
[^suf-ia]: **-ia** — a condition or state: hypoxia, anoxia, ischaemia, anaemia. Don't confuse with **-iasis** a disease process or infestation (lithiasis) · **-aemia** a condition of the blood (hypoxaemia).
