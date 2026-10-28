---
title: Diffusion and Transport of Gases
aliases: [Gas diffusion, DLCO, Oxygen dissociation curve, Bohr effect, Haldane effect, Chloride shift, CO2 transport]
rank: 31
status: not-started
topic: Physiology
subtopic: Respiratory System
chapter: 31
pages: "139–141"
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
source: "Physiology main notes (Marrow 8) — Diffusion and Transport of Gases, pp. 139–141 (sections: Diffusion of Gases 00:01:30 · Transport of Gases 00:17:30)"
mindmap: "[[Diffusion and Transport of Gases — Mind Map]]"
index: "[[Physiology — Index]]"
review_day_2: false
review_day_4: false
review_day_7: false
review_day_10: false
review_day_15: false
---
# 🫧 Diffusion and Transport of Gases

> [!abstract] Core Definition
> Gases cross the **respiratory membrane** by **simple diffusion**[^ety-diffusion][^pre-di] — passive, no ATP, down a pressure gradient, within the **0.75 s** a red cell spends in the alveolar capillary. Once in the blood, **O₂ rides mainly on haemoglobin (97 %)** and **CO₂ travels mainly as bicarbonate (70 %)**. Everything in the chapter answers:
> - ✅ **What speeds or slows diffusion?** → **Fick's law** (area, gradient, solubility ↑; thickness, particle size ↓) — measured by **DLCO (25 ml/min/mmHg)**
> - ✅ **How does Hb load O₂ in the lung and drop it in the tissue?** → the **sigmoid O₂–Hb dissociation curve** (P50 **27 mmHg**), **left shift in lungs / right shift in tissues** (**Haldane** and **Bohr** effects, **2,3-DPG**)
> - ✅ **How is CO₂ carried back?** → **carbonic anhydrase → HCO₃⁻ → chloride shift (Hamburger phenomenon)**; 4 ml CO₂ per 100 ml blood

---

## 🧠 Mental Model — A Four-Seat Taxi That Picks Up in the Lung and Drops Off in the Tissue

Haemoglobin is a taxi with **four seats** for O₂. The first passenger has to force the stiff door open (**tight form**); after that the doors swing open easily (**relaxed form**) — so the taxi fills quickly once it starts. In the **lung** (lots of O₂, little CO₂/H⁺) the taxi grips its passengers (**left shift**); in the **tissue** (little O₂, lots of CO₂, H⁺, heat and 2,3-DPG) it lets them go (**right shift**). CO₂ goes home the other way, mostly converted to bicarbonate:

```
ALVEOLUS ──(diffusion, ≤ 0.75 s, Fick's law)──► PLASMA ──► RBC
O2  : 3 % dissolved (sets PO2)  +  97 % on Hb (1.34 ml/g)  → Hb raises O2 carriage 70×
LUNG   : high PO2, low CO2/H+  → LEFT shift  → Hb grabs O2, drops CO2   (HALDANE effect)
TISSUE : low PO2, high CO2/H+, ↑ 2,3-DPG, heat → RIGHT shift → Hb drops O2   (BOHR effect)
CO2 : tissue → RBC → CO2 + H2O ─carbonic anhydrase→ H2CO3 → H+ (buffered by Hb) + HCO3− (70 %, out to plasma)
                       Cl− comes in (CHLORIDE SHIFT) → water follows → venous RBC swells (Hct +3 %)
      + 30 % as carbamino-Hb · CO2 curve: 48 → 52 ml/100 ml = 4 ml delivered per 100 ml blood
```

---

## 🫁 Diffusion of Gases

- **Transit time of blood in alveolar capillaries: 0.75 sec.**
- Therefore **diffusion should take place in ≤ 0.75 sec.**[^1]
- **Simple diffusion: doesn't require ATP (passive**[^ety-passive] **process).**

![[Diffusion and Transport of Gases - respiratory membrane.png]]
*Respiratory membrane (Rm) — between the alveolus (high O₂) and the red cell (high CO₂) lie the respiratory membrane and the plasma; O₂ diffuses alveolus → RBC, CO₂ diffuses RBC → alveolus (cropped from the handwritten page).*

🧠 The **respiratory membrane**[^ety-membrane] is everything a gas molecule must cross between alveolar air and haemoglobin — very thin and very large, which is why diffusion is fast enough.[^2]

Rotate the gas-exchange organs in 3D — the respiratory membrane lines the alveoli of both lungs, fed by the pulmonary arteries and drained by the pulmonary veins:

```anatomed
# lungs and pulmonary vessels — retype a name with the plugin's autocomplete if it shows as "unmatched"
parts: right lung, left lung, trachea, right main bronchus, left main bronchus, pulmonary trunk, right pulmonary artery, left pulmonary artery, pulmonary veins, heart
detail: related
title: Lungs — where the respiratory membrane lies
```

### Factors affecting diffusion (Fick's law)[^ety-fick]

| Directly proportional | Inversely proportional |
|---|---|
| **Concentration**[^ety-concentration][^pre-con] **gradient** (high → low) | **Thickness of respiratory membrane** |
| **Surface area of respiratory membrane** | **Size of particle** |
| **Lipid solubility of gas** | — |

```latex
\text{Rate of diffusion} \propto \frac{\text{Surface area} \times \text{Concentration gradient} \times \text{Lipid solubility}}{\text{Thickness of membrane} \times \text{Size of particle}}
```

### Applied aspect

| Step | Emphysema[^ety-emphysema][^pre-en] | Pulmonary fibrosis[^ety-fibrosis][^suf-osis] |
|---|---|---|
| **Start** | **α₁ antitrypsin**[^ety-antitrypsin][^pre-anti] **deficiency** | **Fibrosis** |
| **↓** | **↑ trypsin activity (protease**[^suf-ase]**)** | **↑ thickness of Rm** |
| **↓** | **↑ destruction of Rm** | — |
| **↓** | **↓ membrane surface area** | — |
| **End result** | **↓ diffusion of gases** | **↓ diffusion of gases** |

```
Emphysema:  α1 antitrypsin deficiency → ↑ trypsin activity (protease) → ↑ destruction of Rm → ↓ surface area ─┐
                                                                                                               ├→ ↓ DIFFUSION OF GASES
Pulmonary fibrosis:  fibrosis → ↑ thickness of Rm ─────────────────────────────────────────────────────────────┘
```

- In emphysema the **area** term of Fick's law falls; in fibrosis the **thickness** term rises — both reduce diffusion.[^3]

![[Diffusion and Transport of Gases - emphysema distended alveoli.png]]
*Cut surface of an emphysematous lung — **distended alveoli**: walls destroyed, airspaces merged into large holes, so the surface for diffusion is lost (cropped from the handwritten page).*

### DLCO

- **Test to assess diffusion capacity of lung using carbon monoxide**[^ety-monoxide][^pre-mono] **(CO).**
- **CO: ↑ affinity**[^ety-affinity][^pre-ad] **to Hb (210 × O₂ affinity).**
- **Normal value: 25 ml/min/mmHg.**[^4]
- **Conditions affecting DLCO:**

| ↑ DLCO (d/t ↑ blood flow) | ↓ DLCO |
|---|---|
| 1. **Exercise** (physiological) | 1. **Anemia**[^ety-anaemia][^pre-an][^suf-aemia] (d/t ↓ blood flow) |
| 2. **Polycythemia**[^ety-polycythaemia][^pre-poly] | 2. **Emphysema** (↓ area of Rm) |
| 3. **Pulmonary hemorrhage**[^ety-haemorrhage][^suf-rrhage] | 3. **Pulmonary fibrosis** (↑ thickness of Rm) |

🧠 *Why CO?* CO binds Hb so avidly that the blood never "fills up" with it during a test — its uptake is limited only by how fast it can **diffuse** across the membrane, which is exactly what we want to measure. Anything that adds Hb for CO to bind (more red cells, blood in the alveoli, more capillaries opened in exercise) raises DLCO; anything that removes Hb, area or thinness lowers it.[^5]

> [!note] Note
> **Diffusion of CO₂ (20 times solubility of O₂) > O₂.**[^6]

🎬 **Watch:** [Diffusion across the respiratory membrane — Fick's law (YouTube search)](https://www.youtube.com/results?search_query=fick%27s+law+diffusion+respiratory+membrane) · [DLCO explained (YouTube search)](https://www.youtube.com/results?search_query=DLCO+diffusing+capacity+explained) · [Emphysema vs pulmonary fibrosis diffusion (YouTube search)](https://www.youtube.com/results?search_query=emphysema+vs+pulmonary+fibrosis+DLCO)

---

## 🚚 Transport of Gases

### Form of transport

#### O₂

| Plasma — **dissolved form: 3 %** | Hemoglobin[^ety-haemoglobin][^pre-haem] — **combined form: 97 %** |
|---|---|
| **Carries 3 % of O₂.** | **Carries 97 % of O₂.** |
| **Determines pO₂.** | **1 g Hb → 1.34 ml O₂/100 ml of blood.**[^7] |
| — | **↑ O₂ transport by 70 times.** |

🧠 Only the **dissolved** O₂ exerts a partial pressure, so it alone sets PO₂ — but it is tiny. Haemoglobin is the "sponge" that soaks up O₂ according to that PO₂ and so lets blood carry about 70 times more.

#### CO₂

| Bicarbonate[^ety-bicarbonate][^pre-bi] — **70 %** | Hemoglobin — **30 %** |
|---|---|
| **Major form of transport** | **CO₂ + Hb → carbamino**[^ety-carbamino] **Hb**[^8] |

### O₂ dissociation curves

#### O₂–Hb dissociation[^ety-dissociation][^pre-dis] curve

![[Diffusion and Transport of Gases - O2-Hb dissociation curve.png]]
*O₂–Hb dissociation curve — **sigmoid**; **plateau at PO₂ 100 mmHg as Hb is fully saturated**; **P50: 50 % of Hb saturated at PO₂ of 27 mmHg**; **L shift (P50 ↓)** and **R shift (P50 ↑)** curves on either side of the normal one (cropped from the handwritten page; the white band is where a watermark was removed).*

> [!example]- 🎨 Image prompt — O₂–Hb dissociation curve with left and right shifts
> "Clean medical textbook graph, white background. X-axis 'Oxygen partial pressure (mmHg)' 0–120, y-axis 'Haemoglobin oxygen saturation (%)' 0–100. Three sigmoid curves: a dark 'Normal' curve with P50 marked by dashed lines at 27 mmHg / 50 %; a pale green 'L shift (P50 ↓)' curve to its left; a brown 'R shift (P50 ↑)' curve to its right. A dashed vertical line at 100 mmHg labelled 'Plateau at PO₂ 100 mmHg — Hb fully saturated'. Labels: 'Sigmoid curve', 'P50: 50 % of Hb saturated at PO₂ of 27 mmHg'. No other text, no watermark."

- **Plateau**[^ety-plateau] **at pO₂ 100 mmHg** as **Hb is fully saturated**[^ety-saturation].
- **P50: 50 % of Hb saturated at pO₂ of 27 mmHg.**
- **L shift → P50 ↓** (Hb holds O₂ tighter) · **R shift → P50 ↑** (Hb lets O₂ go).

> [!info] **Sigmoid**[^ety-sigmoid][^suf-oid] **curve: 1 Hb molecule binds to 4 O₂ molecules**
> The shape is S-shaped because of **cooperative**[^ety-cooperative][^pre-co] **binding kinetics**[^ety-kinetics]:

```
1st O2 ── difficult binding ──► Hb (TIGHT form)
                                     │
2nd O2 ── easy ─┐                    ▼
3rd O2 ── easy ─┼──────────────► Hb (RELAXED form)
4th O2 ── easy ─┘
          = COOPERATIVE BINDING KINETICS
```

- **1st O₂ — difficult binding → Hb (tight form).**
- **2nd, 3rd, 4th O₂ — easy → Hb (relaxed form).**
- → **Cooperative binding kinetics.**[^9]

#### Shifts

| | **L shift (in lungs)** | **R shift (in tissues)** |
|---|---|---|
| **Effects** | O₂ → **binding / loading** → Hb | Hb → **release / unloading** → O₂ |
| | **↑ affinity of O₂ to Hb → loading of O₂ → unloading of CO₂** = **Haldane effect**[^ety-haldane] | **↓ affinity to Hb, release of O₂** = **Bohr effect**[^ety-bohr] |
| **Metabolic changes** | **↓ CO₂ (hypocarbia**[^ety-carbia][^pre-hypo]**), ↓ H⁺ (alkalosis**[^ety-alkalosis]**)** | **↓ O₂ (hypoxia**[^ety-hypoxia][^suf-ia]**) → ↑ CO₂ (hypercarbia**[^pre-hyper]**) → ↑ H⁺ (acidosis**[^ety-acidosis]**)** |
| **Causes** | 1. **Total Hb** → ↓ affinity to 2,3 DPG[^10] | 1. **Hypoxia → anaerobic**[^ety-anaerobic] **glycolysis**[^ety-glycolysis][^pre-glyco][^suf-lysis] **→ ↑ 2,3 diphosphoglycerate**[^ety-dpg] **(2,3-DPG) → binds to Hb (β chain) → O₂ release** |
| | 2. **CO poisoning** | 2. **Thyroid**[^ety-thyroid][^suf-oid] **hormones → ↑ metabolism**[^ety-metabolism][^suf-ism] |
| | 3. **Stored blood** } ↓ glycolysis → **↓ 2,3 DPG** | 3. **Exercise** |
| | 4. **Chronic hypoxia** } ↓ glycolysis → **↓ 2,3 DPG**[^11] | 4. **High altitude** |

🧠 *Read the shifts by place:* in the **lung** the blood has just lost CO₂ and H⁺, so Hb's affinity rises and it **loads** O₂ — and as O₂ binds, Hb lets go of its CO₂ (**Haldane**). In the **tissue** CO₂, H⁺, heat and 2,3-DPG are high, so affinity falls and Hb **unloads** O₂ where it is needed (**Bohr**).[^12]

> [!note] Note
> **Citrate-phosphate-dextrose-adenine (CPDA) → less fall in 2,3 DPG → used for blood storage.**[^13]

#### O₂–myoglobin dissociation curve

- **O₂ storage in muscles.**
- **1 myoglobin**[^ety-myoglobin][^pre-myo] **molecule binds to 1 O₂ molecule (1 : 1): no cooperativity.**
- Shape: **rectangular hyperbola**[^ety-hyperbola].

![[Diffusion and Transport of Gases - myoglobin vs haemoglobin dissociation curves.png]]
*Myoglobin (Mb) vs fetal (HbF) and adult (HbA) haemoglobin — myoglobin's curve is a **rectangular hyperbola** far to the left (P50 ≈ 2 mmHg); HbF (P50 ≈ 19) lies left of HbA (P50 ≈ 27) (cropped from the handwritten page).*

🧠 With one haem and one O₂, there is nothing to cooperate with — so the curve rises steeply and flattens early (hyperbola, not S). Myoglobin keeps its O₂ until muscle PO₂ is very low, which makes it a **reserve** store rather than a transporter.

### CO₂ dissociation

#### Mechanism

![[Diffusion and Transport of Gases - CO2 transport and chloride shift.png]]
*CO₂ transport in venous blood — CO₂ from the tissue (PCO₂ 45 mmHg) diffuses through interstitial fluid and plasma into the RBC; carbonic anhydrase makes H₂CO₃ → H⁺ + HCO₃⁻; H⁺ is buffered by Hb, HCO₃⁻ leaves through the anion exchanger (70 %) in exchange for Cl⁻ (chloride shift / Hamburger phenomenon); Cl⁻ and water enter, the RBC swells (cropped from the handwritten page).*

```
Tissue (PCO2 = 45 mmHg) → CO2 → interstitial fluid → plasma → RBC
                                                               │
  Hb + CO2 → carbamino Hb                         CO2 + H2O
                                                      │ carbonic anhydrase
                                                    H2CO3 (carbonic acid)
                                                   ┌──┴──┐
                 Hb buffers ───────────────────►  H+    HCO3− ──(anion exchanger)──► plasma HCO3− ↑↑ (70 %)
                                                          Cl− ◄──(Cl− shift = Hamburger phenomenon)── plasma Cl−
  Cl− osmotically active → H2O enters → RBC swells → ↑ haematocrit / PCV of venous blood by 3 %
```

- In the **RBC**: **CO₂ + H₂O —carbonic anhydrase**[^ety-anhydrase][^suf-ase]**→ H₂CO₃ (carbonic acid) → H⁺ + HCO₃⁻.**
- **H⁺ → buffered**[^ety-buffer] **by Hb** (Hb also takes CO₂ directly → **carbamino Hb**).
- **HCO₃⁻ → plasma via the anion exchanger → HCO₃⁻ ↑↑ (70 %).**
- **Cl⁻ moves into the RBC in exchange — Cl⁻ shift (Hamburger**[^ety-hamburger] **phenomenon).**
- **Cl⁻ is osmotically**[^ety-osmosis] **active → H₂O follows → RBC swells → ↑ hematocrit**[^ety-haematocrit][^suf-crit] **/ packed cell volume of venous blood by 3 %.**
- Partial pressures on the figure: **tissue PCO₂ = 45 mmHg**, **plasma PCO₂ = 40 mmHg**.[^14]

#### CO₂ dissociation curve

![[Diffusion and Transport of Gases - CO2 dissociation curve.png]]
*CO₂ dissociation curve — volume of CO₂ in blood rises almost linearly with PCO₂: **48 ml** at PaCO₂ **40 mmHg**, **52 ml** at PvCO₂ **45 mmHg** → **4 ml CO₂ transported / 100 ml of blood** (cropped from the handwritten page).*

| | PCO₂ | CO₂ content |
|---|---|---|
| **Arterial** (PaCO₂) | **40 mmHg** | **48 ml / 100 ml** |
| **Venous** (PvCO₂) | **45 mmHg** | **52 ml / 100 ml** |
| **Difference** | 5 mmHg | **4 ml CO₂ transported / 100 ml of blood** |

🧠 Unlike the O₂ curve, the CO₂ curve has **no plateau** in the physiological range — more PCO₂ always means more CO₂ carried. That is why hyperventilation can wash CO₂ out (but cannot load more O₂ onto saturated Hb).[^15]

🎬 **Watch:** [Oxygen–haemoglobin dissociation curve and shifts (YouTube search)](https://www.youtube.com/results?search_query=oxygen+hemoglobin+dissociation+curve+shift+bohr+haldane) · [CO₂ transport and the chloride shift (YouTube search)](https://www.youtube.com/results?search_query=carbon+dioxide+transport+chloride+shift+hamburger) · [Myoglobin vs haemoglobin — cooperative binding (YouTube search)](https://www.youtube.com/results?search_query=myoglobin+vs+hemoglobin+cooperative+binding)

---

## Core Dictum & Pattern Recognition

> [!check]+ **🎯 Core Dictum - The Unifying Principle**
>
> Gas exchange is two problems solved by two tricks. **Getting across** is pure physics — Fick's law: the gradient, area and solubility push gas through, the thickness and size hold it back, and it must finish within 0.75 s; DLCO measures how well it does. **Getting carried** is chemistry: Hb's **cooperative** binding makes an S-shaped curve whose **flat top** keeps blood saturated even if alveolar PO₂ dips, and whose **steep middle** releases large amounts of O₂ for small falls in tissue PO₂. The curve slides **left in the lungs** (load O₂, drop CO₂ — Haldane) and **right in the tissues** (drop O₂ — Bohr, 2,3-DPG).
>
> CO₂ is far more soluble and mostly travels as **bicarbonate**, made inside the red cell by **carbonic anhydrase** and exported in exchange for chloride — a system that doubles as the blood's main buffer and has **no plateau**, so ventilation can always remove more CO₂.

> [!example]+ **📊 Clinical Pattern Recognition**
>
> Understanding how the condition progresses through stages helps you recognize it at different phases and predict outcomes.
>
> **Stage 1 - Normal Physiology:**
> O₂ equilibrates in the first third of the 0.75 s transit; PaO₂ 100 gives ~97 % saturation on the plateau. DLCO ~25 ml/min/mmHg. Tissues unload O₂ down to a venous PO₂ of 40 (P50 27); CO₂ content rises from 48 to 52 ml/100 ml and returns to the lungs, 70 % as bicarbonate.
>
> **Stage 2 - Compensated/Early Pathology:**
> Early emphysema (lost area) or interstitial fibrosis (thick membrane) lowers DLCO, but at rest the diffusion reserve still lets O₂ equilibrate before the end of the capillary; PaO₂ is normal at rest and falls only on exercise, when transit time shortens. Chronic hypoxia and altitude raise 2,3-DPG and shift the curve right to improve unloading.
>
> **Stage 3 - Decompensated/Overt Disease:**
> Severe emphysema or fibrosis leaves too little area or too thick a membrane: O₂ cannot equilibrate even at rest — hypoxaemia with low DLCO and exertional desaturation. CO poisoning blocks Hb and shifts the curve left, so O₂ content and unloading collapse while PaO₂ looks normal. Massive transfusion of old stored blood (low 2,3-DPG) temporarily reduces O₂ unloading.
>
> **Progression Timeline:**
> Normal diffusion → membrane loss / thickening → low DLCO with exercise desaturation → resting hypoxaemia → right shift (↑ 2,3-DPG) and polycythaemia as compensation → respiratory failure
>
> **Why This Matters Clinically:**
> DLCO separates lung diseases with similar spirometry (emphysema ↓ vs asthma normal or ↑; fibrosis ↓ vs obesity normal); the dissociation curve explains why SpO₂ stays high until PaO₂ falls below ~60, why CO poisoning is deadly with a normal PaO₂, and why stored blood is collected in CPDA.

> [!warning]+ **🔍 Diagnostic Buzzwords & Pattern Recognition**
>
> These are the key terms, phrases, and clinical patterns that should immediately trigger specific diagnoses in your mind. When you see these in a clinical vignette or real patient, you should think of the associated condition instantly.
>
> **Buzzwords by Condition:**
>
> **Emphysema:** "α₁-antitrypsin deficiency", "protease", "destruction of respiratory membrane", "distended alveoli", "↓ DLCO" → loss of surface area; panacinar disease of the lower lobes in a young non-smoker.
>
> **Pulmonary fibrosis:** "↑ thickness of Rm", "↓ DLCO", "exertional desaturation" → diffusion limited by thickness.
>
> **↑ DLCO:** "exercise", "polycythaemia", "pulmonary (alveolar) haemorrhage" → more Hb or more capillary blood for CO to bind.
>
> **Haldane effect:** "O₂ binding displaces CO₂", "in lungs", "left shift" → loading O₂ unloads CO₂.
>
> **Bohr effect:** "↑ CO₂ / H⁺ lowers affinity", "in tissues", "right shift" → release of O₂.
>
> **2,3-DPG:** "anaerobic glycolysis", "binds β chain", "high altitude", "stored blood ↓", "CPDA" → the main long-term regulator of P50.
>
> **Chloride shift:** "Hamburger phenomenon", "anion exchanger", "RBC swells", "venous haematocrit 3 % higher" → bicarbonate export from the red cell.
>
> **Myoglobin:** "1 : 1", "no cooperativity", "rectangular hyperbola", "O₂ storage in muscle" → curve far to the left.
>
> **Visual/Imaging Buzzwords:**
> S-shaped curve = Hb (cooperative); hyperbola = myoglobin; curve to the left = HbF, CO, alkalosis, cold, ↓ 2,3-DPG; curve to the right = ↑ CO₂, acid, ↑ 2,3-DPG, exercise, heat, thyroid hormone, altitude.
>
> **Severity Indicators:**
> DLCO below ~60–75 % of predicted is clinically reduced; P50 27 mmHg is normal — lower = left shift, higher = right shift. Venous PO₂ 40 with 75 % saturation means normal unloading.

> [!danger]+ **⚠️ Common Traps & Pitfalls**
>
> These are the mistakes that students and clinicians commonly make with this topic. Being aware of these traps helps you avoid diagnostic errors and answer tricky exam questions correctly.
>
> **Trap 1: "Hb-bound O₂ determines PO₂"**
>
> **What students think:** Because 97 % of O₂ is on Hb, Hb sets the PO₂.
>
> **Why this is wrong:** Partial pressure is exerted only by gas **dissolved** in plasma (3 %). Hb-bound O₂ is "hidden" from the electrode. That is why anaemia or CO poisoning can leave PaO₂ normal while O₂ **content** falls drastically.
>
> **How to avoid this trap:** "Dissolved sets the pressure; Hb sets the content."
>
> **Trap 2: Mixing up Bohr and Haldane**
>
> **What students think:** Both describe CO₂ affecting O₂ binding.
>
> **Why this is wrong:** **Bohr** = CO₂/H⁺ change Hb's affinity for **O₂** (right shift, **tissues**). **Haldane** = O₂ changes Hb's affinity for **CO₂** (O₂ binding drives CO₂ off, **lungs**). They are mirror images of the same allosteric change.
>
> **How to avoid this trap:** "**B**ohr in the **B**ody tissues drops O₂; **H**aldane at the **H**ead of the airways (lungs) dumps CO₂."
>
> **Trap 3: Thinking a left shift is always good because Hb holds more O₂**
>
> **What students think:** HbF, CO and stored blood "improve" oxygenation by raising affinity.
>
> **Why this is wrong:** Higher affinity helps loading only where PO₂ is low (the placenta for HbF). For the tissues, a left-shifted curve means Hb refuses to unload. CO adds a second blow by occupying binding sites — so CO poisoning is the worst of both.
>
> **How to avoid this trap:** "Left = Lungs Load; Right = Release to tissues."
>
> **Trap 4: Calling anaemia a diffusion defect**
>
> **What students think:** DLCO falls in anaemia because the membrane is damaged.
>
> **Why this is wrong:** The membrane is normal; there is simply less Hb in the capillaries to take up CO, so measured uptake falls (the page says "d/t ↓ blood flow"). The reverse — polycythaemia, alveolar haemorrhage — raises DLCO. DLCO must be corrected for Hb.
>
> **How to avoid this trap:** Ask "membrane problem or blood problem?" before interpreting DLCO.
>
> **Trap 5: Forgetting the direction of the chloride shift**
>
> **What students think:** Chloride leaves the red cell in the tissues.
>
> **Why this is wrong:** In tissue capillaries HCO₃⁻ is made inside the RBC and **leaves**; to keep electrical neutrality Cl⁻ **enters** (and water follows, so venous RBCs swell — venous haematocrit 3 % higher). In the lungs the process reverses.
>
> **How to avoid this trap:** "Bicarbonate out, chloride in — in the tissues."

> [!tip]+ **🔗 Related Concepts & Cross-Topic Connections**
>
> Understanding how this topic connects to other areas of medicine deepens your knowledge and helps you see the bigger picture. These connections also help you answer integrated questions on exams.
>
> **Related Topic 1: [[Alveolar Ventilation and Pulmonary Circulation]]**
> Sets the alveolar PO₂ (100) and PCO₂ (40) that drive diffusion, and the respiratory membrane in the respiratory zone.
>
> **Related Topic 2: [[Ventilation Perfusion Ratio]]**
> The flat top of the O₂ curve explains why high-V/Q units cannot compensate for low-V/Q units, while the linear CO₂ curve explains why CO₂ can be blown off.
>
> **Related Topic 3: [[Chemical Regulation of Respiration]]**
> The types of hypoxia (anaemic, CO poisoning, histotoxic) are read directly off O₂ transport, and the peripheral chemoreceptors sense the dissolved O₂ that sets PO₂.
>
> **Related Topic 4: [[Environmental Physiology]]**
> At altitude, ↑ 2,3-DPG shifts the curve right and polycythaemia raises O₂ content — acclimatisation is applied O₂ transport.
>
> **Related Topic 5: [[Acid Base Balance]]**
> The carbonic anhydrase reaction and bicarbonate buffer of this chapter are the core of the Henderson–Hasselbalch equation.
>
> **Related Topic 6: [[Hematopoiesis and Blood Groups]]**
> Haemoglobin, HbF, polycythaemia, anaemia and blood storage (CPDA) live there.
>
> **Clinical Integration:**
> DLCO in pulmonary function testing, pulse-oximetry limits (the plateau), CO poisoning, transfusion of stored blood, and the bicarbonate buffer in metabolic and respiratory acid–base disorders all apply this chapter.
>
> **Exam Integration:**
> Expect P50 = 27 mmHg, DLCO normal 25 ml/min/mmHg, CO affinity 210×, CO₂ diffuses 20× faster, O₂ 3 % dissolved / 97 % Hb, CO₂ 70 % bicarbonate, 1.34 ml O₂/g Hb, causes of left vs right shift, Bohr vs Haldane, the chloride shift and the 4 ml CO₂ per 100 ml blood.

---

## 🏆 Pearls (High-Yield Summary)

> [!success] Must-Know Pearls
> 1. Capillary **transit time 0.75 s**; diffusion is **simple, passive (no ATP)**.
> 2. **Fick's law** — ∝ **concentration gradient, surface area, lipid solubility**; ∝ 1/**thickness of Rm, size of particle**.
> 3. **Emphysema** (α₁-antitrypsin deficiency → protease → ↓ area) and **pulmonary fibrosis** (↑ thickness) both **↓ diffusion**.
> 4. **DLCO** uses CO (**210 × O₂ affinity**); normal **25 ml/min/mmHg**; **↑** exercise, polycythaemia, pulmonary haemorrhage; **↓** anaemia, emphysema, fibrosis.
> 5. **CO₂ diffuses 20 times** faster than O₂ (solubility).
> 6. O₂: **3 % dissolved (determines PO₂)**, **97 % on Hb**; **1 g Hb carries 1.34 ml O₂**; Hb **↑ O₂ transport 70 times**.
> 7. CO₂: **bicarbonate 70 % (major)**, **Hb 30 % as carbamino-Hb**.
> 8. O₂–Hb curve **sigmoid** (1 Hb : 4 O₂, **cooperative binding** — tight → relaxed); **plateau at PO₂ 100**; **P50 = 27 mmHg**.
> 9. **L shift (lungs, P50 ↓) = Haldane effect** (loading O₂ unloads CO₂) — hypocarbia, alkalosis; HbF, **CO poisoning, stored blood**, ↓ 2,3-DPG.
> 10. **R shift (tissues, P50 ↑) = Bohr effect** — hypoxia → **anaerobic glycolysis → ↑ 2,3-DPG (binds β chain)**, **thyroid hormones, exercise, high altitude**; hypercarbia, acidosis.
> 11. **CPDA** → less fall in 2,3-DPG → used for blood storage.
> 12. **Myoglobin 1 : 1, no cooperativity → rectangular hyperbola**; O₂ storage in muscle.
> 13. **Carbonic anhydrase** → H₂CO₃ → H⁺ (buffered by Hb) + HCO₃⁻ (out via anion exchanger) ⇄ **Cl⁻ in = chloride shift (Hamburger phenomenon)** → RBC swells → **venous Hct ↑ 3 %**.
> 14. **CO₂ curve:** 48 ml (PaCO₂ 40) → 52 ml (PvCO₂ 45) = **4 ml CO₂/100 ml blood**.

---

## 🔁 One-Line Recall

```
DIFFUSION: passive, ≤ 0.75 s · Fick: area × gradient × solubility / thickness × size · CO2 20× faster than O2
APPLIED: emphysema (α1-AT ↓ → protease → ↓ area) · fibrosis (↑ thickness) → ↓ diffusion
DLCO 25 ml/min/mmHg (CO 210×) · ↑ exercise, polycythaemia, alveolar bleed · ↓ anaemia, emphysema, fibrosis
O2: 3 % dissolved (sets PO2) + 97 % Hb (1.34 ml/g, 70×) · CO2: 70 % HCO3− + 30 % carbamino-Hb
O2–Hb: sigmoid, cooperative (tight → relaxed), plateau 100, P50 27 · LEFT = lungs = Haldane · RIGHT = tissues = Bohr, 2,3-DPG
MYOGLOBIN: 1:1, hyperbola, store · CO2: CA → HCO3− out, Cl− in (Hamburger) → Hct +3 % · 48 → 52 ml = 4 ml/100 ml
```

---

## 🎬 Video Library

| What to watch | Link |
|---|---|
| Fick's law and diffusion across the respiratory membrane (YouTube search) | https://www.youtube.com/results?search_query=fick%27s+law+diffusion+respiratory+membrane |
| DLCO — diffusing capacity explained (YouTube search) | https://www.youtube.com/results?search_query=DLCO+diffusing+capacity+explained |
| Oxygen–haemoglobin dissociation curve, Bohr and Haldane effects (YouTube search) | https://www.youtube.com/results?search_query=oxygen+hemoglobin+dissociation+curve+shift+bohr+haldane |
| CO₂ transport and the chloride shift (YouTube search) | https://www.youtube.com/results?search_query=carbon+dioxide+transport+chloride+shift+hamburger |

---

## 🖼 Infographic Prompt — One-Page Summary

> [!abstract]- 🎨 Prompt for an image generator (copy everything inside)
> "Design a single-page, portrait A4 medical study infographic titled **'DIFFUSION AND TRANSPORT OF GASES'** for a postgraduate physiology exam. Flat-vector textbook style, off-white background; colour code: blue = O₂, orange = CO₂, red = haemoglobin / red cells, grey = membrane and disease, green = normal values. Thin icons, crisp legible text, generous white space. Four panels in a 2 × 2 grid:
>
> **Panel 1 — 'Diffusion of gases'.** A diagram of alveolus → respiratory membrane (Rm) → plasma → RBC with a blue arrow 'High O₂ → RBC' and an orange arrow 'High CO₂ → alveolus'; captions 'Transit time 0.75 s — diffusion in ≤ 0.75 s', 'Simple diffusion, no ATP (passive)'. A two-column Fick's-law box: 'Directly ∝: concentration gradient, surface area, lipid solubility' / 'Inversely ∝: thickness of Rm, size of particle'. Two mini flow-charts: 'Emphysema: α₁-antitrypsin deficiency → ↑ protease → ↑ destruction of Rm → ↓ area → ↓ diffusion' with a small distended-alveoli lung image; 'Pulmonary fibrosis → ↑ thickness of Rm → ↓ diffusion'.
>
> **Panel 2 — 'DLCO'.** A gauge reading '25 ml/min/mmHg'; 'CO affinity to Hb 210 × O₂'. Two columns: '↑ DLCO (↑ blood flow): exercise, polycythaemia, pulmonary haemorrhage' / '↓ DLCO: anaemia, emphysema (↓ area), pulmonary fibrosis (↑ thickness)'. Footnote 'CO₂ diffuses 20 × O₂ (solubility)'.
>
> **Panel 3 — 'O₂ transport & dissociation curves'.** Two bars: 'Dissolved 3 % — determines PO₂' and 'Hb 97 % — 1 g Hb carries 1.34 ml O₂; ↑ O₂ transport 70 ×'. A sigmoid O₂–Hb curve with P50 27 mmHg, plateau at 100 mmHg, a left-shift (P50 ↓) and a right-shift (P50 ↑) curve. A four-seat haemoglobin icon 'tight → relaxed: cooperative binding'. A two-column shift table: 'L shift in lungs — loading — Haldane effect — ↓ CO₂, ↓ H⁺ — HbF, CO poisoning, stored blood, ↓ 2,3-DPG' / 'R shift in tissues — unloading — Bohr effect — hypoxia → anaerobic glycolysis → ↑ 2,3-DPG (β chain), thyroid hormone, exercise, high altitude'. Small box 'CPDA → less fall in 2,3-DPG → blood storage'. A small myoglobin hyperbola 'Mb 1 : 1, no cooperativity, O₂ store in muscle'.
>
> **Panel 4 — 'CO₂ transport'.** CO₂ forms: '70 % bicarbonate (major)', '30 % carbamino-Hb'. A red-cell diagram: tissue PCO₂ 45 → CO₂ into RBC → 'CO₂ + H₂O —carbonic anhydrase→ H₂CO₃ → H⁺ (buffered by Hb) + HCO₃⁻ → out via anion exchanger'; 'Cl⁻ in = chloride shift (Hamburger phenomenon) → water in → RBC swells → venous haematocrit +3 %'. A linear CO₂ dissociation curve: '48 ml at PaCO₂ 40 → 52 ml at PvCO₂ 45 = 4 ml CO₂ per 100 ml blood'.
>
> Footer strip: 'P50 27 · DLCO 25 · 3 % vs 97 % · 70 % HCO₃⁻ · Left = Lungs (Haldane) · Right = tissues (Bohr)'. No watermark, no photographs, illustration quality."

---

## 📚 References

- Physiology main notes (Marrow 8) — *Diffusion and Transport of Gases*, pp. 139–141
- Guyton & Hall Textbook of Medical Physiology — Principles of gas exchange; diffusion of O₂ and CO₂ through the respiratory membrane; Transport of O₂ and CO₂ in blood and tissue fluids
- Ganong's Review of Medical Physiology — Gas transport and pH
- West JB — *Respiratory Physiology: The Essentials* — Diffusion; Gas transport by the blood
- `Diffusion and Transport of Gases - ….png` files in `attachments/` are crops of the handwritten pages

[^1]: At rest O₂ reaches equilibrium with alveolar gas in about the first third of the capillary (~0.25 s), so there is a large reserve. In heavy exercise the transit time can fall to ~0.25 s — still just enough in a healthy lung, but not in a thickened or reduced membrane, which is why diffusion defects show up first on exercise.
[^2]: The respiratory membrane has six layers — the fluid/surfactant lining, alveolar epithelium, epithelial basement membrane, interstitial space, capillary basement membrane and capillary endothelium — about 0.2–0.6 µm thick (average ~0.5 µm) over a total area of ~70 m² in an adult (Guyton).
[^3]: α₁-antitrypsin, made in the liver, chiefly inhibits **neutrophil elastase**; its lack lets elastase destroy alveolar walls (panacinar emphysema, worst in the lower lobes, in young patients). The page writes "trypsin activity (protease)" — the enzyme mainly responsible is elastase, though the inhibitor is named for its action on trypsin. Smoking causes centriacinar emphysema of the upper lobes.
[^4]: Guyton gives a resting diffusing capacity for O₂ of about 21 ml/min/mmHg and for CO about 17 ml/min/mmHg in a young man; most PFT laboratories quote normal DLCO about 20–30 (≈ 25) ml/min/mmHg. CO's affinity for Hb is usually given as 200–250 times that of O₂ (the page's 210 is the classic figure).
[^5]: More precisely, DLCO depends on Hb concentration: polycythaemia adds Hb (↑), anaemia removes it (↓ — the page attributes this to "↓ blood flow"), and in alveolar haemorrhage free Hb in the airspaces binds CO (↑). Exercise opens extra capillaries (recruitment), raising both area and capillary blood volume. Reported DLCO is corrected for the patient's Hb.
[^6]: CO₂ is about 20–24 times more soluble than O₂ in water; its slightly larger molecular weight barely slows it, so its diffusion coefficient is ~20 times that of O₂. Hence CO₂ retention almost never results from a diffusion defect — hypoxaemia appears long before hypercapnia.
[^7]: The 1.34 ml is per **gram** of Hb (Hüfner's constant, 1.34–1.39 ml O₂/g). With Hb 15 g/100 ml blood, fully saturated Hb carries ~20 ml O₂/100 ml (≈ 19.5 ml at 97 %), against only 0.3 ml dissolved (0.003 ml/100 ml/mmHg × 100 mmHg) — roughly 65–70 times more, the page's "70 times".
[^8]: Standard textbooks split CO₂ transport as about **70 % bicarbonate, 23 % carbamino compounds (with Hb and plasma proteins) and 7 % dissolved**; the page groups dissolved and carbamino CO₂ as the Hb 30 %.
[^9]: The two forms are the **T (tense)** state — low O₂ affinity, held by salt bridges and stabilised by 2,3-DPG, H⁺ and CO₂ — and the **R (relaxed)** state, ~500 times higher affinity. Binding of each O₂ makes the next easier (allosteric cooperativity; Hill coefficient ≈ 2.8).
[^10]: ⚠ The page reads "Total Hb → ↓ affinity to 2,3 DPG". The standard cause is **fetal Hb (HbF, α₂γ₂)**: its γ chains bind 2,3-DPG poorly, so HbF has a higher O₂ affinity (P50 ~19 mmHg) and a left-shifted curve — what lets the fetus take O₂ from maternal blood. "Total" is most likely a slip for "Fetal".
[^11]: ⚠ The page lists **chronic hypoxia** among left-shift causes with ↓ glycolysis → ↓ 2,3-DPG, but in the same table lists hypoxia and high altitude as **right**-shift causes via ↑ 2,3-DPG. Standard texts agree with the second: chronic hypoxia (altitude, anaemia, COPD) raises 2,3-DPG and shifts the curve right. Stored blood is the true example of falling 2,3-DPG. Other left-shift causes: alkalosis, ↓ PCO₂, hypothermia, methaemoglobin.
[^12]: Right-shift causes are often remembered as **"CADET, face Right"** — **C**O₂, **A**cid (H⁺), 2,3-**D**PG, **E**xercise, **T**emperature (heat). Left-shift causes are the opposites plus HbF, CO and methaemoglobin.
[^13]: In stored blood 2,3-DPG falls steadily because red-cell glycolysis slows; it falls faster in the older ACD (acid-citrate-dextrose) solution than in CPD/CPDA, where phosphate and adenine support glycolysis and ATP. Transfused red cells regenerate 2,3-DPG within about 24 hours.
[^14]: Within a tissue capillary the plasma PCO₂ rises from the arterial 40 mmHg to the venous ~45 mmHg as CO₂ diffuses in from the tissue (PCO₂ ~45–46). The anion exchanger is **band 3 protein (AE1)**; carbonic anhydrase (a zinc enzyme, found in RBCs in 1933) speeds the CO₂ + H₂O reaction about 5000-fold.
[^15]: Guyton's values: arterial blood carries ~48 ml CO₂/100 ml at PCO₂ 40, venous ~52 ml at PCO₂ 45 — so each 100 ml of blood delivers ~4 ml CO₂ to the lungs, 200 ml/min at a cardiac output of 5 L. The respiratory exchange ratio then follows: 200 ml CO₂ out ÷ 250 ml O₂ in = 0.8.
[^ety-diffusion]: **diffusion** — Latin *dis-*, "apart, in different directions" + *fundere*, "to pour" + *-ion*, the process → pouring out in all directions; net movement of molecules from high to low concentration by their own random motion. **Differentiate:** *diffusion* (passive, down a gradient) · *active transport* (against a gradient, needs ATP) · *osmosis* (diffusion of **water** across a semipermeable membrane) · *perfusion* (bulk blood flow).
[^ety-passive]: **passive** — Latin *pati*, "to suffer, endure" + *-ive* → undergoing rather than doing; a passive process uses no metabolic energy (ATP). **Differentiate:** *passive* (simple and facilitated diffusion) · *active* (primary — uses ATP directly; secondary — uses an ion gradient).
[^ety-membrane]: **membrane** — Latin *membrana*, "a skin, parchment" (from *membrum*, a limb) → a thin sheet covering or separating; the respiratory membrane is the sheet between air and blood.
[^ety-fick]: **Fick's law** — Adolf Eugen Fick (1829–1901), German physiologist, who stated the law of diffusion in 1855 and later (1870) the Fick principle for measuring cardiac output.
[^ety-concentration]: **concentration** — Latin *con-*, "together" + *centrum*, "centre" + *-ation* → bringing to a common centre; the amount of a substance per unit volume. A *gradient* (*gradi*, "to step") is the step-down from high to low concentration that drives diffusion.
[^ety-emphysema]: **emphysema** — Greek *en-* (*em-* before *ph*), "in" + *physan*, "to blow, inflate" + *-ma*, the result → something blown up; permanent enlargement of airspaces distal to the terminal bronchiole with destruction of their walls. **Differentiate:** *emphysema* (walls destroyed) · *overinflation* (walls intact, e.g. asthma) · *subcutaneous emphysema* (air in the skin).
[^ety-fibrosis]: **fibrosis** — Latin *fibra*, "a fibre, filament" + Greek *-osis*, a condition → a condition of excess fibrous tissue; scarring that thickens the interstitium.
[^ety-antitrypsin]: **α₁-antitrypsin** — Greek *anti-*, "against" + *trypsin* (Greek *tripsis*, "rubbing", as it was first got by rubbing pancreas with glycerine; + *-in*, a substance) → a substance against trypsin; the α₁ marks its band on serum protein electrophoresis. A serine-protease inhibitor (serpin) whose main target is neutrophil elastase.
[^ety-monoxide]: **monoxide** — Greek *monos*, "single" + *oxide* (from *oxys*, "acid", via oxygen) → a compound with a single oxygen atom (CO). Compare *dioxide* (*di-*, two — CO₂).
[^ety-affinity]: **affinity** — Latin *ad-* (*af-*), "to, towards" + *finis*, "boundary" + *-ity* → bordering on, closeness; in chemistry the attraction of a molecule for its ligand. High affinity = binds readily and lets go reluctantly (left shift).
[^ety-anaemia]: **anaemia / anemia** — Greek *an-*, "without" + *haima*, "blood" + *-ia*, condition → "bloodlessness"; a fall in Hb concentration. **Differentiate:** *anaemia* (↓ Hb) · *hypoxaemia* (↓ PaO₂) · *hypovolaemia* (↓ blood volume) · *polycythaemia* (↑ red cells).
[^ety-polycythaemia]: **polycythaemia** — Greek *polys*, "many" + *kytos*, "a hollow vessel, cell" + *haima*, "blood" + *-ia* → too many cells in the blood. **Differentiate:** *polycythaemia vera* (primary marrow disorder) · *secondary* polycythaemia (↑ EPO — altitude, COPD) · *relative* (↓ plasma volume).
[^ety-haemorrhage]: **haemorrhage** — Greek *haima*, "blood" + *rhēgnynai*, "to burst forth" → blood bursting out of a vessel. **Differentiate:** *-rrhage* (bursting) · *-rrhoea* (flow) · *-rrhaphy* (suturing) · *-rrhexis* (rupture).
[^ety-haemoglobin]: **haemoglobin** — Greek *haima*, "blood" + Latin *globus*, "ball" + *-in*, a protein → the globular protein of blood (contracted from *haematoglobulin*); four globin chains, each with a haem (Fe²⁺ porphyrin) that binds one O₂.
[^ety-bicarbonate]: **bicarbonate** — Latin *bi-*, "two, double" + *carbo*, "coal, charcoal" + *-ate*, a salt → the "double carbonate" (HCO₃⁻ has twice the carbonic acid per base of carbonate CO₃²⁻). Also called hydrogen carbonate.
[^ety-carbamino]: **carbamino** — *carb(on)* + *amino* (from *ammonia*, Greek *Ammōn*, the god near whose Libyan temple ammonium salts were found) → CO₂ joined to an amino (–NH₂) group of the globin chain: Hb–NH₂ + CO₂ → Hb–NH–COOH. Not to be confused with *carboxy*haemoglobin (CO bound to haem).
[^ety-dissociation]: **dissociation** — Latin *dis-*, "apart" + *sociare*, "to join, unite" (*socius*, companion) + *-ation* → separating companions; here O₂ coming off Hb. **Differentiate:** *dissociation* (separating a bound pair) · *dissolution* (dissolving) · *dissipation* (scattering away).
[^ety-plateau]: **plateau** — French, "flat tray, tableland" (from *plat*, "flat") → the flat upper part of the O₂–Hb curve above PO₂ ~70 mmHg, where saturation barely changes.
[^ety-saturation]: **saturation** — Latin *satur*, "full, sated" + *-ation* → filling to the full; O₂ saturation = % of Hb binding sites occupied. **Differentiate:** *saturation* (%) · *content* (ml O₂/100 ml) · *tension* (partial pressure, mmHg).
[^ety-sigmoid]: **sigmoid** — Greek *sigma*, the letter Σ (in its curved form ς, "S") + *-oeidēs*, "like" → S-shaped; the same word names the S-shaped sigmoid colon.
[^ety-cooperative]: **cooperative / cooperativity** — Latin *co-*, "together" + *operari*, "to work" + *-ive* → working together; in biochemistry, binding at one site changes the affinity of the others. **Differentiate:** *positive cooperativity* (Hb — each O₂ eases the next) · *no cooperativity* (myoglobin — single site) · *allosteric* (*allos*, other + *stereos*, solid/shape — a change of shape at one site affecting another).
[^ety-kinetics]: **kinetics** — Greek *kinēsis*, "movement" (*kinein*, "to move") + *-ics*, the study of → the study of how fast and in what pattern reactions proceed.
[^ety-haldane]: **Haldane effect** — John Scott Haldane (1860–1936), Scottish physiologist at Oxford, who with Christiansen and Douglas (1914) showed that oxygenation of blood lowers its CO₂-carrying capacity. He also studied CO poisoning and high-altitude physiology.
[^ety-bohr]: **Bohr effect** — Christian Bohr (1855–1911), Danish physiologist, who with August Krogh and Karl Hasselbalch (1904) showed that CO₂ lowers haemoglobin's O₂ affinity; father of the physicist Niels Bohr.
[^ety-carbia]: **hypocarbia / hypercarbia (hypo- / hypercapnia)** — Greek *hypo-*, "under" / *hyper-*, "over" + Latin *carbo*, "coal" (CO₂) + *-ia*, condition → too little / too much CO₂ in the blood. *-capnia* uses Greek *kapnos*, "smoke" — the same meaning.
[^ety-alkalosis]: **alkalosis** — Arabic *al-qaly*, "the calcined ashes" (of saltwort, rich in soda) + Greek *-osis*, a condition → a condition of too much base (blood pH > 7.45). **Differentiate:** *alkalosis* (process) · *alkalaemia* (the high blood pH itself).
[^ety-hypoxia]: **hypoxia** — Greek *hypo-*, "under" + *oxy-* (oxygen) + *-ia*, condition → too little O₂. **Differentiate:** *hypoxia* (tissue) · *hypoxaemia* (blood PaO₂) · *anoxia* (none).
[^ety-acidosis]: **acidosis** — Latin *acidus*, "sour" + Greek *-osis*, a condition → a condition of too much acid (pH < 7.35). **Differentiate:** *acidosis* (process) · *acidaemia* (the low blood pH itself).
[^ety-anaerobic]: **anaerobic** — Greek *an-*, "without" + *aēr*, "air" + *bios*, "life" + *-ic* → living (working) without air/O₂; anaerobic glycolysis ends in lactate. **Differentiate:** *aerobic* (with O₂ — Krebs cycle, oxidative phosphorylation).
[^ety-glycolysis]: **glycolysis** — Greek *glykys*, "sweet" (sugar) + *lysis*, "loosening, splitting" → splitting of sugar; glucose → pyruvate. In red cells a side-branch (the Rapoport–Luebering shunt) makes 2,3-DPG.
[^ety-dpg]: **2,3-diphosphoglycerate (2,3-DPG / 2,3-BPG)** — Greek *di-*, "two" + *phosphate* (*phōs*, "light" + *pherein*, "to carry" — phosphorus glows) + *glycerate* (*glykeros*, "sweet") → glycerate carrying two phosphates, on carbons 2 and 3. It binds the β chains in the central cavity of deoxy-Hb and stabilises the T state.
[^ety-thyroid]: **thyroid** — Greek *thyreos*, "an oblong door-shaped shield" + *-eidēs*, "like" → shield-shaped (the thyroid cartilage, then the gland beside it). Thyroid hormones raise 2,3-DPG and metabolic rate.
[^ety-metabolism]: **metabolism** — Greek *meta-*, "change" + *ballein*, "to throw" + *-ism*, process → *metabolē*, "change"; the sum of the body's chemical changes. **Differentiate:** *anabolism* (*ana-*, up — building) · *catabolism* (*kata-*, down — breaking down).
[^ety-myoglobin]: **myoglobin** — Greek *mys* (*myo-*), "muscle" (literally "mouse", from the look of a moving muscle under the skin) + *globin* → the globin of muscle; a single chain with one haem.
[^ety-hyperbola]: **hyperbola** — Greek *hyper-*, "over, beyond" + *ballein*, "to throw" → "a throwing beyond" (the conic section whose angle exceeds that of the cone's side); a *rectangular* hyperbola is the shape of a simple 1 : 1 binding curve.
[^ety-anhydrase]: **carbonic anhydrase** — *carbonic* (Latin *carbo*, coal) + Greek *an-*, "without" + *hydōr*, "water" + *-ase*, an enzyme → the enzyme that removes water from carbonic acid (and adds it to CO₂ — it works both ways).
[^ety-buffer]: **buffer** — Old French *buffe*, "a blow" → something that softens a blow; a chemical buffer limits the change in pH when acid or base is added (Hb is the main non-bicarbonate buffer of blood).
[^ety-hamburger]: **Hamburger phenomenon** — Hartog Jakob Hamburger (1859–1924), Dutch physiologist at Groningen, who described in the 1890s the exchange of chloride between red cells and plasma as blood takes up CO₂ — the chloride shift.
[^ety-osmosis]: **osmosis / osmotically** — Greek *ōsmos*, "a push, thrust" + *-osis* → the push of water across a membrane towards the side with more solute particles. Cl⁻ entering the RBC adds particles, so water follows.
[^ety-haematocrit]: **haematocrit** — Greek *haima*, "blood" + *kritēs*, "a judge" (*krinein*, "to separate, judge") → blood-separator; the % of blood volume occupied by red cells after centrifuging (= packed cell volume, PCV).
[^pre-di]: **di- / dis- / dif-** — apart, in different directions: diffusion, dissociation, distensible. Don't confuse with Greek **di-** two (diphosphoglycerate, dioxide) · **dia-** through (diaphragm) · **dys-** bad, difficult (dyspnoea).
[^pre-con]: **con- / com- / co-** — together, with: concentration, compliance, cooperative, combined. Don't confuse with **contra-** against · **counter-** opposite (countercurrent).
[^pre-en]: **en- / em- (Greek)** — in, into: emphysema (blown in), embolism, encephalon. Don't confuse with **endo-** within · **ex- / ec-** out of · **an- / a-** without.
[^suf-osis]: **-osis** — a condition, usually abnormal: fibrosis, alkalosis, acidosis, osmosis (here a process). Don't confuse with **-itis** inflammation · **-iasis** disease due to an agent · **-ation** a process.
[^pre-anti]: **anti-** — against, opposing: antitrypsin, anticoagulant, antibody. Don't confuse with **ante-** before (antenatal) · **an- / a-** without.
[^suf-ase]: **-ase** — an enzyme: protease, carbonic anhydrase, elastase, lipase. Don't confuse with **-ose** a sugar (glucose, dextrose) · **-ate** a salt or ion (bicarbonate, glycerate).
[^pre-mono]: **mono-** — one, single: monoxide, monosaccharide, monocyte. Don't confuse with **mon-** in Greek *mōn* · **uni-** one (Latin synonym) · **di-** two · **poly-** many.
[^pre-ad]: **ad- (af-, ac-, ag-)** — to, towards: affinity, afferent, adhesion. Don't confuse with **ab-** away from · **a- / an-** without.
[^pre-an]: **an- / a-** — without, not: anaemia, anaerobic, anhydrase, anoxia, apnoea. Don't confuse with **ana-** up, again (anabolism) · **ante-** before · **anti-** against.
[^suf-aemia]: **-aemia / -emia** — a condition of the blood: anaemia, polycythaemia, hypoxaemia, uraemia. Don't confuse with **-ia** any condition (hypoxia) · **haemo- / haemato-** blood as a prefix.
[^pre-poly]: **poly-** — many, much: polycythaemia, polyuria, polypeptide. Don't confuse with **pleo-** more (pleomorphic) · **oligo-** few · **multi-** many (Latin synonym).
[^suf-rrhage]: **-rrhage / -rrhagia** — bursting forth, heavy bleeding: haemorrhage, menorrhagia. Don't confuse with **-rrhoea** flow · **-rrhaphy** suturing · **-rrhexis** rupture.
[^pre-haem]: **haem- / haemo- / haemato- (hem-)** — blood: haemoglobin, haemorrhage, haematocrit. Don't confuse with **hemi-** half (hemiplegia) · **hepat-** liver.
[^pre-bi]: **bi-** — two, twice, double: bicarbonate, bilateral, biconcave. Don't confuse with **bio-** life (anaerobic) · Greek **di-** two (dioxide).
[^pre-dis]: **dis-** — apart, away, reversal: dissociation, dissolve, distal. Don't confuse with **dys-** bad, difficult · **di-** two.
[^suf-oid]: **-oid** — like, resembling: sigmoid (S-like), thyroid (shield-like), adenoid, opioid. Don't confuse with **-ode** a way, path (electrode) · **-oma** tumour.
[^pre-co]: **co-** — together, jointly: cooperative, coenzyme, coagulation. Don't confuse with **contra-** against · **counter-** opposite.
[^pre-hypo]: **hypo-** — under, below, deficient: hypocarbia, hypoxia, hypothermia. Don't confuse with **hyper-** over · **hypno-** sleep.
[^suf-ia]: **-ia** — a condition: hypoxia, hypocarbia, anaemia. Don't confuse with **-iasis** a disease from an agent · **-ium** a structure.
[^pre-hyper]: **hyper-** — over, excessive: hypercarbia, hyperventilation, hyperbola (thrown beyond). Don't confuse with **hypo-** under · **supra- / super-** above (Latin).
[^pre-glyco]: **glyco- / gluco-** — sweet, sugar: glycolysis, glycogen, glucose. Don't confuse with **glyc-** in *glycine* (an amino acid, also "sweet") · **gly-** in *glycerol* (sweet alcohol) — same root, different molecules.
[^suf-lysis]: **-lysis** — loosening, splitting, breakdown: glycolysis, haemolysis, thrombolysis. Don't confuse with **-lytic** the adjective (haemolytic) · **-plasty** reshaping · **-poiesis** making.
[^suf-ism]: **-ism** — a process or state: metabolism, embolism, hyperthyroidism. Don't confuse with **-ist** a person · **-osis** a diseased condition.
[^pre-myo]: **myo- / my-** — muscle: myoglobin, myocardium, myopathy. Don't confuse with **myco-** fungus (Mycobacterium) · **myelo-** marrow, spinal cord · **myx-** mucus.
[^suf-crit]: **-crit** — separator, judge (Greek *kritēs*): haematocrit, leucocrit. Don't confuse with **-crine** secreting (endocrine — from *krinein*, the same root) · **-cyte** a cell.
