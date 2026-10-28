---
title: Synaptic Transmission and Neurotransmitters
aliases: [Synapse, EPSP and IPSP, Presynaptic inhibition, Neurotransmitter classes, Dopamine pathways, NMDA receptor]
rank: 14
status: not-started
topic: Physiology
subtopic: Central Nervous System
chapter: 14
pages: "68–73"
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
source: "Physiology main notes (Marrow 8) — Synaptic Transmission and Neurotransmitters, pp. 68–73 (sections: Synaptic Transmission 00:00:48 · Neurotransmitters (NT) 00:24:00)"
mindmap: "[[Synaptic Transmission and Neurotransmitters — Mind Map]]"
index: "[[Physiology — Index]]"
review_day_2: false
review_day_4: false
review_day_7: false
review_day_10: false
review_day_15: false
---
# 🔌 Synaptic Transmission and Neurotransmitters

> [!abstract] Core Definition
> A **synapse**[^ety-synapse][^pre-syn] is the junction where one neuron passes its signal to the next cell — **electrically** through gap junctions (fast) or **chemically** through a **neurotransmitter**[^ety-neurotransmitter][^pre-neuro][^pre-trans] (slow). The chapter answers:
> - ✅ How is the signal passed and turned into a **postsynaptic potential** (EPSP / IPSP) that must **summate** to reach threshold?
> - ✅ How is transmission **regulated** — facilitation vs pre-, post- and feedback inhibition?
> - ✅ Which **neurotransmitter** — class I ACh · class II biogenic amines · class III amino acids · class IV gases — works where, on which receptor, and what disease follows when it fails?

---

## 🧠 Mental Model — A Postal Service Between Neurons

An **electrical synapse** is a door left open between two rooms — the message walks straight through (fast, no delay). A **chemical synapse** is a postal service: the sender packs the message into vesicles (stored NT), Ca²⁺ is the stamp that lets the post office (SNARE proteins) release the parcel, the parcel crosses the street (synaptic cleft), and the receiver signs for it at a receptor — either opening the door at once (ionotropic, fast) or passing it to an assistant who acts later (metabotropic, slow). The receiver acts only when enough letters pile up (summation → threshold).

```
AP arrives → Ca²⁺ enters → SNARE exocytosis → NT crosses cleft → receptor
   ionotropic  (nicotinic, AMPA/NMDA, GABA-A, 5-HT3) → FAST PSP
   metabotropic (muscarinic, D1–D5, most 5-HT)        → SLOW PSP (≈ 500 ms)
EPSP (Na⁺/Ca²⁺ in, ↓K⁺ out) ↔ IPSP (Cl⁻ in, ↑K⁺ out) → SUMMATION → threshold → AP
CLASS I  ACh · CLASS II NE, DA, 5-HT, histamine · CLASS III glutamate (+), GABA (−), glycine (±) · CLASS IV NO, CO
```

---

## 🔗 Synaptic Transmission

### Types

| | **1. Electrical mode** | **2. Neurotransmitters (NT)** |
|---|---|---|
| **Mediated by** | **Gap junctions (connexin**[^ety-connexin][^pre-con] **protein)** | **Chemicals** (eg: ACh released from the presynaptic end onto the postsynaptic end) |
| **Speed** | **Fast mode** | **Slow mode** |

![[Synaptic Transmission and Neurotransmitters - electrical and chemical synapse.png]]
*Types of synaptic transmission — 1. electrical mode: action potentials pass straight through gap junctions (connexin protein) — fast; 2. chemical mode: ACh released from the presynaptic[^pre-pre] end (motor axon) crosses the synaptic cleft to the postsynaptic[^pre-post] end (muscle endplate) — slow (cropped from the handwritten page).*

🧠 In the electrical mode current flows directly from cell to cell, so there is no delay; in the chemical mode the transmitter has to be released, diffuse and bind, which costs time (the synaptic delay).[^1]

### Structure

![[Synaptic Transmission and Neurotransmitters - structure of a chemical synapse.png]]
*Structure of a synapse — presynaptic neuron with stored NT, synaptic cleft, postsynaptic neuron with receptors; release of NT → NT–receptor binding (cropped from the handwritten page).*

- **Presynaptic neuron** — holds the **stored NT** in vesicles.
- **Synaptic cleft** — the gap the NT crosses.
- **Postsynaptic neuron** — carries the **NT receptors**.

```
Release of NT
      ↓
NT receptor binding
      ↓
Postsynaptic potential / end plate potential  (= LOCAL potential)
      ↓
Undergoes summation
      ↓
Crosses threshold
      ↓
Action potential generated
```

🧠 A postsynaptic potential[^ety-potential] is a **local** (graded) potential — it is small and fades with distance, so one alone rarely fires the neuron; many must add up (**summation**[^ety-summation]) to push the membrane to **threshold**[^ety-threshold].[^2]

> [!note] Note — Types of synapse
> - **Axon – axon.**
> - **Axon – somatic.**
> - **Axon – dendritic**[^ety-dendrite].[^3]

### Post Synaptic Potentials (PSP)

| | **Excitatory**[^ety-excitatory][^pre-ex] **PSP — Fast EPSP** | **Excitatory PSP — Slow EPSP** | **Inhibitory**[^ety-inhibitory][^pre-in] **PSP — Fast IPSP** | **Inhibitory PSP — Slow IPSP** |
|---|---|---|---|---|
| **Ion movement (image)** | **Na⁺ and Ca²⁺ in** → inside +++ | **K⁺ (decrease efflux)** → inside +++ | **Cl⁻ in, K⁺ out** → inside − − − | **K⁺ (increase efflux)** → inside − − − |
| **Example** | **Glutamate, acetylcholine** | **Autonomic ganglia, cardiac muscle, smooth muscle** | **GABA** | — |
| **Latency** | — | **500 ms** | — | **500 ms** |

![[Synaptic Transmission and Neurotransmitters - fast and slow EPSP and IPSP.png]]
*Postsynaptic potentials — fast EPSP (Na⁺ and Ca²⁺ in), slow EPSP (↓ K⁺ efflux), fast IPSP (Cl⁻ in, K⁺ out), slow IPSP (↑ K⁺ efflux) (cropped from the handwritten page).*

🧠 Excitation = making the inside **less negative** (cations in, or keeping K⁺ in); inhibition = making the inside **more negative** (Cl⁻ in, or letting more K⁺ out). Fast ones use ion-channel receptors; slow ones go through G proteins, hence the ~500 ms latency.[^4]

### Regulation

| **Facilitation**[^ety-facilitation][^suf-ation] | **Inhibition** |
|---|---|
| Ca²⁺ channel on presynaptic membrane → channel open for long time → **↑↑↑ Ca²⁺ release** → **↑ neurotransmitter release** → **synaptic facilitation** | **1. Postsynaptic inhibition** — AKA **GABA-mediated inhibition** · **2. Presynaptic inhibition** — AKA **lateral inhibition (in retina)**[^ety-retina] · **3. Feedback inhibition** — **Renshaw**[^ety-renshaw] **cell (α motor interneuron**[^pre-inter]**)** → α motor neuron (through glycine) |

**Facilitation:**

```
Ca²⁺ channel on presynaptic membrane
        ↓
Channel open for long time
        ↓
↑↑↑ Ca²⁺ release
        ↓
↑ neurotransmitter release
        ↓
Synaptic facilitation
```

![[Synaptic Transmission and Neurotransmitters - synaptic facilitation.png]]
*Synaptic facilitation — Ca²⁺ entering the presynaptic terminal releases more NT onto the postsynaptic neuron (cropped from the handwritten page).*

**Inhibition (synaptic inhibition):**

1. **Postsynaptic inhibition** — the presynaptic neuron releases **GABA** onto the postsynaptic neuron (−) → AKA **GABA-mediated inhibition**.
2. **Presynaptic inhibition** — an inhibitory (−) **interneuron** acts on the presynaptic terminal, so less transmitter reaches the postsynaptic neuron → AKA **lateral inhibition (in retina)**.
3. **Feedback inhibition** — the **Renshaw cell (α motor interneuron)** inhibits the **α motor neuron (through glycine)** that excited it.[^5]

![[Synaptic Transmission and Neurotransmitters - types of synaptic inhibition.png]]
*Synaptic inhibition — 1. postsynaptic (GABA-mediated) inhibition; 2. presynaptic inhibition via an inhibitory interneuron (lateral inhibition in the retina); 3. feedback inhibition of the α motor neuron by the Renshaw cell through glycine (cropped from the handwritten page).*

🎬 **Watch:** [Synaptic transmission — EPSP, IPSP and summation (YouTube search)](https://www.youtube.com/results?search_query=synaptic+transmission+EPSP+IPSP+summation+physiology) · [Presynaptic vs postsynaptic inhibition, Renshaw cell (YouTube search)](https://www.youtube.com/results?search_query=presynaptic+postsynaptic+inhibition+renshaw+cell)

---

## 🧪 Neurotransmitters (NT)

- **1st neurotransmitter discovered: Acetylcholine.**[^6]

### Criteria for NT

1. **NT synthesised & stored in presynaptic neuron.**
2. **NT released into synapse.**
3. **Post-synaptic neuron receptor** (it must act on one).[^7]

![[Synaptic Transmission and Neurotransmitters - criteria for a neurotransmitter.png]]
*Criteria for a neurotransmitter — 1. synthesised and stored in the presynaptic neuron, 2. released into the synapse, 3. acts on a postsynaptic receptor (cropped from the handwritten page).*

### Classification

| **Class I** | **Class II** | **Class III** | **Class IV** |
|---|---|---|---|
| **Eg: Acetylcholine** | **Biogenic**[^ety-biogenic][^pre-bio][^suf-genic] **amines**[^ety-amine] (eg: dopamine, norepinephrine, serotonin) | **Amino acids** (eg: glutamate, GABA, glycine) | **Gases** (eg: nitric oxide, carbon monoxide[^pre-mono]) |

![[Synaptic Transmission and Neurotransmitters - classes of neurotransmitters.png]]
*Classification of neurotransmitters — class I acetylcholine, class II biogenic amines (dopamine → norepinephrine by dopamine β-hydroxylase), class III amino acids, class IV gases (nitric oxide) (cropped from the handwritten page).*

---

### Class I — Acetylcholine[^ety-acetylcholine]

#### ACh release

- **Acetylcholine release: exocytosis**[^ety-exocytosis][^pre-exo][^suf-osis] **by SNARE**[^ety-snare] **proteins & Ca²⁺.**

| SNARE protein | Where | Role |
|---|---|---|
| **SNAP-25** | Membrane | Docking (target) protein |
| **Syntaxin**[^ety-syntaxin] | Membrane | Docking (target) protein |
| **Synaptobrevin** | Vesicle | Pairs with syntaxin + SNAP-25 |
| **Synaptotagmin** | Vesicle | **Ca²⁺ sensor** |

```
Ca²⁺ enters → synaptotagmin (Ca²⁺ sensor) → vesicle SNAREs zip with membrane SNAREs → ACh release

Botulinum toxin degrades the SNAREs
        ↓
No release of ACh
        ↓
Flaccid paralysis
```

![[Synaptic Transmission and Neurotransmitters - SNARE proteins and botulinum toxin.png]]
*ACh release by exocytosis — SNAP-25 and syntaxin on the membrane, synaptobrevin on the vesicle, synaptotagmin as the Ca²⁺ sensor; botulinum[^ety-botulinum] toxin[^ety-toxin] degrades the SNAREs → no ACh release → flaccid[^ety-flaccid] paralysis[^ety-paralysis][^pre-para][^suf-lysis] (cropped from the handwritten page).*[^8]

#### Receptors

| Receptor | Type | Speed |
|---|---|---|
| **1. Nicotinic**[^ety-nicotinic] **ACh receptor** | **Ion channel: ionotrope**[^ety-ionotropic][^suf-tropic] | **Fast transmission** |
| **2. Muscarinic**[^ety-muscarinic] **ACh receptor** | **G protein-coupled receptor: metabotropic**[^pre-meta] | **Slow transmission** |

![[Synaptic Transmission and Neurotransmitters - nicotinic and muscarinic receptors.png]]
*Acetylcholine receptors — 1. nicotinic: an ion channel (ionotropic, fast transmission); 2. muscarinic: a seven-pass G-protein-coupled receptor (metabotropic, slow transmission) (cropped from the handwritten page).*[^9]

#### Location and function of acetylcholine

| Location | Function |
|---|---|
| **1. Neuromuscular junction** | **Muscle contraction** |
| **2. Nucleus basalis of Meynert**[^ety-meynert] | **Reduced level in Alzheimer's**[^ety-alzheimer] |
| **3. REM**[^ety-rem] **ON neurons** | **Sleep** |
| **4. Sweat glands** | **Sympathetic cholinergic**[^suf-ergic] **neurons** |

🧠 ACh is the one transmitter of the sympathetic system that breaks the "sympathetic = NE" rule: sweat glands are supplied by sympathetic nerves that release ACh.[^10]

---

### Class II — Biogenic amines

#### Norepinephrine[^ety-norepinephrine][^pre-epi]

- **Synthesised from dopamine.**
- **Location: Locus coeruleus**[^ety-locus-coeruleus].
- **Function: Promote wakefulness.**[^11]

```
Norepinephrine released (locus coeruleus)
        ↓
Widespread brain area activation
        ↓
Awake / arousal state attained
```

![[Synaptic Transmission and Neurotransmitters - norepinephrine from locus coeruleus.png]]
*Norepinephrine released from the locus coeruleus in the brainstem → widespread brain activation → awake / arousal state (cropped from the handwritten page).*

#### Dopamine[^ety-dopamine]

**Pathways:**

| | **Nigrostriatal**[^ety-nigrostriatal] | **Mesolimbic**[^ety-mesolimbic][^pre-meso] | **Mesocortical** | **Tuberoinfundibular**[^ety-tuberoinfundibular] |
|---|---|---|---|---|
| **Location** | **Basal ganglia (substantia nigra)** | **Ventral tegmental area**[^ety-tegmental], **nucleus accumbens**[^ety-accumbens] | **Prefrontal cortex** | Hypothalamus → pituitary stalk → anterior pituitary (figure) |
| **Function** | **Motor movement** | **Reward pathway; Addiction** | **Motivation; Emotional regulation; Decision making; Memory** | **Inhibit release of prolactin**[^ety-prolactin][^pre-pro] |
| **Applied aspect** | **↓ level of dopamine: bradykinesia**[^ety-bradykinesia][^pre-brady][^suf-kinesia] **in Parkinson's disease**[^ety-parkinson] | **Abnormal dopamine pathway at nucleus accumbens: addiction** | — | **Dopamine: physiologic inhibition of prolactin** |

![[Synaptic Transmission and Neurotransmitters - tuberoinfundibular pathway.png]]
*Tuberoinfundibular pathway — hypothalamus → pituitary stalk → anterior pituitary, where dopamine inhibits prolactin (cropped from the handwritten page).*

- **Receptors: D1, D2, D3, D4, D5: G-protein-coupled receptors (GPCR).**[^12]

Rotate the transmitter map — the nuclei that make each amine and where they project:

```anatomed
# neurotransmitter nuclei and targets — retype a name with the plugin's autocomplete if it shows as "unmatched"
parts: substantia nigra, caudate nucleus, putamen, nucleus accumbens, ventral tegmental area, prefrontal cortex, hypothalamus, pituitary gland, locus coeruleus, raphe nuclei, hippocampus, subthalamic nucleus, area postrema, pineal gland
detail: related
title: Transmitter nuclei — dopamine, NE, serotonin, histamine, glutamate
```

#### Serotonin[^ety-serotonin]

**Released from:**

| Location | Function |
|---|---|
| **Brain** (raphe nuclei[^ety-raphe]) | **Awake state** |
| **GIT** | **Regulate peristalsis**[^ety-peristalsis][^pre-peri] |
| **Platelets** | **Aggregation** |

![[Synaptic Transmission and Neurotransmitters - serotonin sources.png]]
*Serotonin is released from the brain (raphe nuclei → awake state), the GIT (regulates peristalsis) and platelets (aggregation) (cropped from the handwritten page).*[^13]

**Receptors: 5-hydroxytryptamine**[^ety-hydroxytryptamine][^pre-hydroxy] **receptors: 5-HT1 to 5-HT7.**

| Receptor | Type | Location | Function |
|---|---|---|---|
| **5-HT2a** | GPCR | **Platelet** | **Platelet aggregation** |
| **5-HT2c** | GPCR | **GIT** | **↓ food intake (regulate satiety**[^ety-satiety]**)** |
| **5-HT4** | GPCR | **GIT** | **Peristalsis** |
| **5-HT6, 7** | GPCR | **Limbic system** | — |
| **5-HT3** | **Ionotropic receptor** | **Area postrema**[^ety-area-postrema][^pre-post] | **Vomiting** |

🧠 5-HT3 is the odd one out — the only serotonin receptor that is an ion channel; it sits in the vomiting centre's chemoreceptor zone, which is why its blockers stop chemotherapy vomiting.[^14]

#### Histamine[^ety-histamine]

**Released from:**

| | **Brain** | **Stomach** |
|---|---|---|
| **Location** | **Posterior hypothalamus**[^ety-hypothalamus][^pre-hypo] (pituitary gland and pineal[^ety-pineal] gland shown for orientation) | **Parietal**[^ety-parietal] **cell (HCl)** |
| **Function** | **Promote wakefulness** | **↑ Acid production** |

![[Synaptic Transmission and Neurotransmitters - histamine sources.png]]
*Histamine is released from the posterior hypothalamus (promotes wakefulness; pituitary and pineal glands labelled for orientation) and acts in the stomach on the parietal cell (→ ↑ HCl) (cropped from the handwritten page).*[^15]

---

### Class III — Amino acid

#### Glutamate[^ety-glutamate][^suf-ate]

- **Major excitatory neurotransmitter.**

**Released from:**

| Location | Function |
|---|---|
| **Hippocampus**[^ety-hippocampus], **subthalamic**[^pre-sub] **nucleus** | **Memory** |
| **A-delta fibres** | **Fast pain** |

**Receptors:**

```
Glutamate ──(+)──► AMPA (Na⁺ channel) ──► Na⁺ in (DEPOLARIZATION)
                                                │
                                                ▼
                         Removes Mg²⁺ block & activates Ca²⁺ channel
                                                │
Glycine + NMDA ─► activates receptor ─────────► NMDA (Ca²⁺ channel)
for glutamate                                   ▲
                    Mg²⁺ blocks NMDA receptor (physiological) at rest
```

![[Synaptic Transmission and Neurotransmitters - AMPA and NMDA receptors.png]]
*Glutamate receptors — glutamate opens AMPA (Na⁺ in → depolarisation[^ety-depolarisation][^pre-de]), which removes the Mg²⁺ block of NMDA and activates its Ca²⁺ channel; glycine + glutamate activate NMDA; Mg²⁺ blocks NMDA physiologically at rest (cropped from the handwritten page).*

- **AMPA**[^ety-ampa] opens first (fast Na⁺ entry); **NMDA**[^ety-nmda] opens only when **glutamate + glycine** are bound **and** the membrane is already depolarised to expel **Mg²⁺** — a "coincidence detector".[^16]

**Clinical aspect — Excitotoxicity**[^ety-excitotoxicity]:

```
Excitotoxicity — seen in amyotrophic lateral sclerosis (ALS)
MOA: ↑ Ca²⁺ influx
        ↓
Cell death
Rx: Riluzole (NMDA blocker)
```

- Seen in **amyotrophic lateral sclerosis**[^ety-als][^pre-a][^suf-trophic] **(ALS)**; **Rx: Riluzole (NMDA blocker)**.[^17]

> [!note] Note
> **Subthalamic nucleus: only excitatory nucleus of basal ganglia.**[^18]

#### GABA[^ety-gaba]

- **Major inhibitory neurotransmitter.**
- **Location: Basal ganglia → caudate**[^ety-caudate] **& putamen**[^ety-putamen] **(striatum**[^ety-striatum]**).**
- **Function: Inhibit involuntary movements.**
- **MOA: Acts in hyperpolarization**[^ety-hyperpolarisation][^pre-hyper] **phase of action potential.**
- **Applied aspect:**

```
Loss of GABA in striatum
        ↓
Huntington's chorea (involuntary movement)
```

- **Huntington's**[^ety-huntington] **chorea**[^ety-chorea] (involuntary movement).

![[Synaptic Transmission and Neurotransmitters - GABA hyperpolarisation.png]]
*GABA acts in the hyperpolarisation phase — it pushes the membrane from −70 towards −90 mV (interior of cell more negative), further from the −55 mV threshold (cropped from the handwritten page).*

> [!note] Note
> **GABA is inhibitory by enhancing hyperpolarization.**[^19]

#### Glycine[^ety-glycine]

- **Function: Both excitatory & inhibitory.**
- **Location: α motor neuron.**
- **MOA: Feedback inhibition / Renshaw cell inhibition.**

![[Synaptic Transmission and Neurotransmitters - Renshaw cell feedback inhibition.png]]
*Glycine and the Renshaw cell — feedback inhibition of the α motor neuron supplying skeletal muscle; the box "Antagonist of glycine" marks where strychnine acts (cropped from the handwritten page).*

**Clinical aspect:**

```
Strychnine                              Tetanospasmin
    ↓                                        ↓
Inhibits the release of glycine         Inhibits the release of GABA
            ╲                              ╱
             ▼                            ▼
                 Causes SPASTIC PARALYSIS
(d/t uninhibited stimulation of α motor neurons → sustained contractions)
```

- **Strychnine**[^ety-strychnine] and **tetanospasmin**[^ety-tetanospasmin][^suf-spasm] both remove the brake on the α motor neuron → **spastic**[^ety-spastic] **paralysis** (d/t uninhibited stimulation of α motor neurons → sustained contractions).[^20]

---

### Class IV — Gases

#### Nitric oxide[^ety-nitric-oxide][^suf-ide]

- **Source: Arginine**[^ety-arginine].
- **Location: Hippocampus.**
- **MOA:**
  - **Requires cGMP for all action.**
  - **↑ glutamate release from presynaptic neuron.**
- **Function: Learning and memory.**[^21]

#### Carbon monoxide

- **Source:**

```
         Heme oxygenase 2
Heme  ─────────────────────►  CO
```

- **Heme**[^ety-heme] **oxygenase**[^ety-oxygenase][^suf-ase] **2** converts heme to CO.
- **Function:**
  - **Olfaction**[^ety-olfaction].
  - **Pain transmission.**
  - **Learning and memory.**[^22]

🎬 **Watch:** [Neurotransmitters — classification and receptors (YouTube search)](https://www.youtube.com/results?search_query=neurotransmitters+classification+receptors+physiology+lecture) · [Dopamine pathways — nigrostriatal, mesolimbic, mesocortical, tuberoinfundibular (YouTube search)](https://www.youtube.com/results?search_query=dopamine+pathways+nigrostriatal+mesolimbic+mesocortical+tuberoinfundibular) · [NMDA and AMPA receptors, excitotoxicity (YouTube search)](https://www.youtube.com/results?search_query=NMDA+AMPA+receptor+magnesium+block+excitotoxicity)

---

## Core Dictum & Pattern Recognition

> [!check]+ **🎯 Core Dictum - The Unifying Principle**
>
> **A synapse is a decision point, not a wire.** The presynaptic side decides *how much* transmitter is released (Ca²⁺ entry → SNAREs; more Ca²⁺ = facilitation, less = presynaptic inhibition; toxins that cut SNAREs stop it entirely). The postsynaptic side decides *what it means*: the receptor type, not the transmitter, sets fast vs slow (ionotropic vs metabotropic) and excitatory vs inhibitory (cations in vs Cl⁻ in / K⁺ out). Only when the local potentials **summate to threshold** does the next neuron fire.
>
> Each disease in this chapter is a broken decision: too little transmitter (dopamine in Parkinson's, ACh in Alzheimer's, GABA in Huntington's), too much excitation (glutamate excitotoxicity in ALS), or loss of the brake (strychnine, tetanospasmin → spastic paralysis; botulinum → no release → flaccid paralysis).

> [!example]+ **📊 Clinical Pattern Recognition**
>
> Understanding how the condition progresses through stages helps you recognize it at different phases and predict outcomes.
>
> **Stage 1 - Normal Physiology:**
> Ca²⁺-triggered SNARE exocytosis releases NT; fast EPSPs (glutamate, ACh) and fast IPSPs (GABA, glycine) are balanced; Renshaw feedback and presynaptic inhibition trim motor output; dopamine pathways grade movement, reward and prolactin; Mg²⁺ keeps NMDA closed at rest.
>
> **Stage 2 - Compensated/Early Pathology:**
> Neurons begin to fail but remaining terminals release more transmitter and receptors up-regulate: Parkinson's is silent until most nigral dopamine neurons are lost; cholinergic loss in the nucleus basalis begins years before dementia; excess glutamate is still buffered by uptake.
>
> **Stage 3 - Decompensated/Overt Disease:**
> Clinical syndromes appear: bradykinesia (nigrostriatal dopamine ↓), memory loss (ACh ↓, Alzheimer's), chorea (striatal GABA ↓, Huntington's), progressive motor neuron death (glutamate excitotoxicity, ALS), flaccid paralysis (botulinum — no ACh release), spastic paralysis and opisthotonus (strychnine, tetanospasmin — loss of glycine/GABA inhibition), hyperprolactinaemia (loss of tuberoinfundibular dopamine).
>
> **Progression Timeline:**
> Normal → toxin / degeneration / receptor block → compensation (↑ release, receptor up-regulation) → transmitter deficit or excess unmasked → specific neurological syndrome
>
> **Why This Matters Clinically:**
> Therapy replaces or mimics the missing transmitter (levodopa, cholinesterase inhibitors), blocks the excess (riluzole, 5-HT3 blockers for vomiting, D2 blockers), or neutralises the toxin (antitoxin, benzodiazepines to restore GABA tone in tetanus).

> [!warning]+ **🔍 Diagnostic Buzzwords & Pattern Recognition**
>
> These are the key terms, phrases, and clinical patterns that should immediately trigger specific diagnoses in your mind. When you see these in a clinical vignette or real patient, you should think of the associated condition instantly.
>
> **Buzzwords by Condition:**
>
> **Electrical synapse:** "Gap junctions", "connexin", "fast mode", "no delay" → electrical transmission.
>
> **Botulism:** "Canned food", "descending flaccid paralysis", "SNARE degraded", "no ACh release" → botulinum toxin.
>
> **Tetanus / strychnine:** "Spastic paralysis", "opisthotonus", "Renshaw cell", "glycine", "GABA release blocked" → loss of spinal inhibition.
>
> **Alzheimer's:** "Nucleus basalis of Meynert", "↓ ACh" → cholinergic deficit.
>
> **Parkinson's:** "Substantia nigra", "nigrostriatal", "bradykinesia", "↓ dopamine" → Parkinson's disease.
>
> **Huntington's:** "Loss of GABA in striatum (caudate, putamen)", "chorea" → Huntington's disease.
>
> **ALS:** "Excitotoxicity", "↑ Ca²⁺ influx", "riluzole" → glutamate toxicity in motor neuron disease.
>
> **Vomiting centre:** "5-HT3", "ionotropic", "area postrema" → chemoreceptor trigger zone (ondansetron target).
>
> **Wakefulness transmitters:** "Locus coeruleus (NE)", "raphe (5-HT)", "posterior hypothalamus (histamine)" → arousal systems.
>
> **Visual/Imaging Buzzwords:**
> Four small synapse pictures with Na⁺/Ca²⁺ in vs K⁺ out vs Cl⁻ in = EPSP/IPSP table; a receptor plugged by a Mg²⁺ ball = NMDA; seven-loop serpentine receptor = GPCR (muscarinic, dopamine); a star-shaped interneuron feeding back on a motor neuron = Renshaw cell.
>
> **Severity Indicators:**
> Fast PSPs act within milliseconds; slow PSPs have ~500 ms latency. Facilitation is graded by Ca²⁺ — ↑↑↑ Ca²⁺ = ↑ release.

> [!danger]+ **⚠️ Common Traps & Pitfalls**
>
> These are the mistakes that students and clinicians commonly make with this topic. Being aware of these traps helps you avoid diagnostic errors and answer tricky exam questions correctly.
>
> **Trap 1: Botulinum vs tetanus toxin**
>
> **What students think:** Both toxins cause the same (spastic) paralysis because both cut SNAREs.
>
> **Why this is wrong:** Both are zinc proteases that cleave SNAREs, but botulinum acts at the **neuromuscular junction** (no ACh release → **flaccid** paralysis), while tetanospasmin travels to the **spinal cord** and stops release of **inhibitory** transmitters (glycine/GABA) from Renshaw/inhibitory interneurons → **spastic** paralysis.
>
> **How to avoid this trap:** Ask "which synapse loses its transmitter?" — excitatory (NMJ) → flaccid; inhibitory (cord) → spastic.
>
> **Trap 2: "Glycine is purely inhibitory"**
>
> **What students think:** Glycine only inhibits (Renshaw cell).
>
> **Why this is wrong:** The page says glycine is **both** excitatory and inhibitory: it is the inhibitory transmitter of Renshaw cells (Cl⁻ channel), but it is also the obligatory **co-agonist** of the excitatory NMDA receptor ("glycine + NMDA → activates receptor for glutamate").
>
> **How to avoid this trap:** Glycine alone = brake (spinal cord); glycine + glutamate on NMDA = accelerator (hippocampus).
>
> **Trap 3: Presynaptic vs postsynaptic inhibition**
>
> **What students think:** Both hyperpolarise the postsynaptic neuron.
>
> **Why this is wrong:** Postsynaptic inhibition (GABA-mediated) produces an IPSP in the postsynaptic cell and lowers its response to *every* input. Presynaptic inhibition acts through an interneuron on one presynaptic terminal, reducing Ca²⁺ entry and NT release from *that input only*, leaving the postsynaptic membrane unchanged.
>
> **How to avoid this trap:** Pre = less letter posted; post = receiver less willing to read anything.
>
> **Trap 4: The odd serotonin receptor**
>
> **What students think:** All 5-HT receptors are GPCRs (as the page lists 5-HT2a, 2c, 4, 6, 7).
>
> **Why this is wrong:** **5-HT3 is ionotropic** — a ligand-gated cation channel in the area postrema → vomiting. That is the receptor ondansetron blocks.
>
> **How to avoid this trap:** "3 = the third class of receptor in the table that is not G-protein — the ion channel."
>
> **Trap 5: Excitatory nucleus of the basal ganglia**
>
> **What students think:** All basal-ganglia output is inhibitory GABA, so all nuclei are inhibitory.
>
> **Why this is wrong:** The **subthalamic nucleus is the only excitatory (glutamatergic) nucleus** of the basal ganglia — it releases glutamate (memory, with the hippocampus, on the page). Its lesion gives hemiballismus.
>
> **How to avoid this trap:** "Sub-thalamic = sole glutamate" — the exception in a GABA circuit.

> [!tip]+ **🔗 Related Concepts & Cross-Topic Connections**
>
> Understanding how this topic connects to other areas of medicine deepens your knowledge and helps you see the bigger picture. These connections also help you answer integrated questions on exams.
>
> **Related Topic 1: [[Characteristics of Nerve Fibres]]**
> The action potential that arrives at the terminal, local vs propagated potentials and A-delta fibres (fast pain, glutamate) come from here.
>
> **Related Topic 2: [[Skeletal Muscles]]**
> The neuromuscular junction — ACh, nicotinic receptors, end plate potential, botulinum toxin — is the best-studied chemical synapse.
>
> **Related Topic 3: [[Cerebellum and Basal Ganglia]]**
> Nigrostriatal dopamine, striatal GABA, the excitatory subthalamic nucleus, Parkinson's and Huntington's disease.
>
> **Related Topic 4: [[Spinal Reflexes]]**
> Renshaw cell feedback inhibition, reciprocal inhibition and the effects of strychnine and tetanus on the motor neuron pool.
>
> **Related Topic 5: [[EEG and Sleep]]**
> REM-on cholinergic neurons and the arousal systems — NE (locus coeruleus), 5-HT (raphe), histamine (posterior hypothalamus).
>
> **Related Topic 6: [[Sensory Receptors]]**
> Glutamate (fast pain, Aδ) and substance P (slow pain, C fibres) at the first sensory synapse; presynaptic inhibition in the gate control theory.
>
> **Clinical Integration:**
> Antiparkinsonian drugs, antipsychotics (D2 block → hyperprolactinaemia, extrapyramidal effects), cholinesterase inhibitors in Alzheimer's, riluzole in ALS, ondansetron in chemotherapy vomiting, antihistamine drowsiness, and toxicology (botulism, tetanus, strychnine) all apply this chapter.
>
> **Exam Integration:**
> Expect: the first NT discovered, the Ca²⁺ sensor of exocytosis (synaptotagmin), what botulinum degrades, ionotropic vs metabotropic receptors, slow EPSP latency, lateral inhibition in the retina, the dopamine pathway that inhibits prolactin, the only ionotropic 5-HT receptor, Mg²⁺ block of NMDA, the only excitatory nucleus of the basal ganglia, and the transmitter lost in Huntington's.

---

## 🏆 Pearls (High-Yield Summary)

> [!success] Must-Know Pearls
> 1. Synaptic transmission: **electrical (gap junctions, connexin) — fast**; **chemical (NT) — slow**.
> 2. NT release → receptor binding → **postsynaptic / end plate potential (local)** → **summation** → threshold → AP. Synapses: axo-axonic, axo-somatic, axo-dendritic.
> 3. **Fast EPSP** Na⁺/Ca²⁺ in (glutamate, ACh); **slow EPSP** ↓ K⁺ efflux (autonomic ganglia, cardiac, smooth muscle; **500 ms**); **fast IPSP** Cl⁻ in (GABA); **slow IPSP** ↑ K⁺ efflux (500 ms).
> 4. **Facilitation**: Ca²⁺ channel open longer → ↑↑↑ Ca²⁺ → ↑ NT release.
> 5. Inhibition: **postsynaptic (GABA-mediated)**, **presynaptic (= lateral inhibition in retina)**, **feedback (Renshaw cell → α motor neuron, glycine)**.
> 6. **First NT discovered: acetylcholine**; criteria — synthesised & stored presynaptically, released, acts on a postsynaptic receptor.
> 7. Classes: **I ACh · II biogenic amines (DA, NE, 5-HT) · III amino acids (glutamate, GABA, glycine) · IV gases (NO, CO)**.
> 8. ACh release = **exocytosis by SNAREs + Ca²⁺** (SNAP-25, syntaxin, synaptobrevin; **synaptotagmin = Ca²⁺ sensor**); **botulinum degrades SNAREs → no ACh → flaccid paralysis**.
> 9. **Nicotinic = ionotropic (fast); muscarinic = GPCR, metabotropic (slow)**. ACh: NMJ, **nucleus basalis of Meynert (↓ in Alzheimer's)**, REM-on neurons, **sweat glands (sympathetic cholinergic)**.
> 10. **NE**: from dopamine, **locus coeruleus**, wakefulness. Dopamine: **nigrostriatal** (movement; ↓ → Parkinson's bradykinesia), **mesolimbic** (reward, addiction), **mesocortical** (motivation, decisions, memory), **tuberoinfundibular** (inhibits prolactin); D1–D5 all GPCR.
> 11. Serotonin: brain (awake), GIT (peristalsis), platelets (aggregation); **5-HT2a platelets, 5-HT2c satiety, 5-HT4 peristalsis, 5-HT3 ionotropic — area postrema — vomiting**. Histamine: **posterior hypothalamus (wakefulness)**, parietal cell (↑ HCl).
> 12. **Glutamate = major excitatory NT** (hippocampus, subthalamic nucleus — memory; Aδ — fast pain); **AMPA → Na⁺ → depolarisation → removes Mg²⁺ block of NMDA**; glycine co-activates NMDA; **excitotoxicity → ALS → riluzole**; **subthalamic nucleus = only excitatory BG nucleus**.
> 13. **GABA = major inhibitory NT** (caudate & putamen); enhances hyperpolarisation; **loss in striatum → Huntington's chorea**. **Glycine** — both excitatory & inhibitory; Renshaw feedback inhibition; **strychnine (glycine) and tetanospasmin (GABA) → spastic paralysis**.
> 14. **NO** — from arginine, hippocampus, needs cGMP, ↑ glutamate release → learning & memory. **CO** — heme → (heme oxygenase 2) → CO → olfaction, pain, memory.

---

## 🔁 One-Line Recall

```
ELECTRICAL (gap jn, connexin) = fast · CHEMICAL (NT) = slow · release → binding → PSP (local) → summation → AP
EPSP fast Na⁺/Ca²⁺ (glu, ACh) · slow ↓K⁺ (ganglia, heart, smooth; 500 ms) · IPSP fast Cl⁻ (GABA) · slow ↑K⁺
FACILITATION ↑Ca²⁺ · INHIBITION post (GABA) / pre (lateral, retina) / feedback (Renshaw, glycine)
CLASS I ACh (SNARE + Ca²⁺; botulinum → flaccid) · nicotinic ionotropic / muscarinic GPCR · Meynert ↓ Alzheimer's
CLASS II NE locus coeruleus · DA nigrostriatal (Parkinson) / mesolimbic / mesocortical / TIF (⊣ prolactin) · 5-HT3 ionotropic vomiting · histamine post. hypothalamus
CLASS III glutamate (+) AMPA → Mg²⁺ off NMDA → ALS riluzole · GABA (−) striatum → Huntington · glycine ± Renshaw → strychnine/tetanus spastic
CLASS IV NO (arginine, cGMP, memory) · CO (heme oxygenase 2, smell, pain, memory)
```

---

## 🎬 Video Library

| What to watch | Link |
|---|---|
| Synaptic transmission — EPSP, IPSP and summation (YouTube search) | https://www.youtube.com/results?search_query=synaptic+transmission+EPSP+IPSP+summation+physiology |
| Presynaptic vs postsynaptic inhibition, Renshaw cell (YouTube search) | https://www.youtube.com/results?search_query=presynaptic+postsynaptic+inhibition+renshaw+cell |
| Neurotransmitters — classification and receptors (YouTube search) | https://www.youtube.com/results?search_query=neurotransmitters+classification+receptors+physiology+lecture |
| Dopamine pathways (YouTube search) | https://www.youtube.com/results?search_query=dopamine+pathways+nigrostriatal+mesolimbic+mesocortical+tuberoinfundibular |
| NMDA and AMPA receptors, excitotoxicity (YouTube search) | https://www.youtube.com/results?search_query=NMDA+AMPA+receptor+magnesium+block+excitotoxicity |

---

## 🖼 Infographic Prompt — One-Page Summary

> [!abstract]- 🎨 Prompt for an image generator (copy everything inside)
> "Design a single-page, portrait A4 medical study infographic titled **'SYNAPTIC TRANSMISSION AND NEUROTRANSMITTERS'** for a postgraduate physiology exam. Flat-vector textbook style, off-white background; colour code: green = excitatory, red = inhibitory, yellow = Ca²⁺, blue = receptors, purple = toxins and drugs. Thin icons, crisp legible text, generous white space. Eight panels in a 2 × 4 grid:
>
> **Panel 1 — 'Types & structure'.** Left: two cells joined by gap junctions 'electrical — connexin — fast'. Right: a chemical synapse with stored NT vesicles, synaptic cleft and receptors, 'chemical — NT — slow'. A vertical flow: 'release of NT → receptor binding → postsynaptic / end plate potential (local) → summation → threshold → action potential'. Three tags: 'axo-axonic, axo-somatic, axo-dendritic'.
>
> **Panel 2 — 'Postsynaptic potentials'.** A 4-column mini-table: fast EPSP (Na⁺, Ca²⁺ in; glutamate, ACh), slow EPSP (↓ K⁺ efflux; autonomic ganglia, cardiac, smooth muscle; 500 ms), fast IPSP (Cl⁻ in; GABA), slow IPSP (↑ K⁺ efflux; 500 ms).
>
> **Panel 3 — 'Regulation'.** Facilitation flow 'Ca²⁺ channel open long → ↑↑↑ Ca²⁺ → ↑ NT release'. Three inhibition sketches: 'postsynaptic — GABA-mediated', 'presynaptic — via (−) interneuron — lateral inhibition (retina)', 'feedback — Renshaw cell → α motor neuron (glycine)'.
>
> **Panel 4 — 'Neurotransmitter basics'.** 'First NT discovered: acetylcholine'; three criteria arrows on a synapse; a four-column class bar 'I ACh · II biogenic amines (DA, NE, 5-HT) · III amino acids (glutamate, GABA, glycine) · IV gases (NO, CO)'.
>
> **Panel 5 — 'Class I — acetylcholine'.** SNARE sketch: SNAP-25 and syntaxin on membrane, synaptobrevin on vesicle, synaptotagmin 'Ca²⁺ sensor'; a purple scissors 'botulinum toxin degrades SNAREs → no ACh → flaccid paralysis'. Receptor icons 'nicotinic — ion channel — fast' vs 'muscarinic — GPCR — slow'. Location list: NMJ (contraction), nucleus basalis of Meynert (↓ in Alzheimer's), REM-on neurons (sleep), sweat glands (sympathetic cholinergic).
>
> **Panel 6 — 'Class II — biogenic amines'.** Brain sagittal outline: locus coeruleus 'NE → wakefulness'; four dopamine arrows 'nigrostriatal — movement — ↓ in Parkinson's (bradykinesia)', 'mesolimbic — reward, addiction (nucleus accumbens)', 'mesocortical — motivation, emotion, decisions, memory', 'tuberoinfundibular — inhibits prolactin'; 'D1–D5 = GPCR'. Serotonin: brain (awake), GIT (peristalsis), platelets (aggregation); receptor strip '5-HT2a platelet aggregation · 5-HT2c ↓ food intake · 5-HT4 peristalsis · 5-HT6,7 limbic · 5-HT3 ionotropic — area postrema — vomiting'. Histamine: posterior hypothalamus (wakefulness), parietal cell (↑ HCl).
>
> **Panel 7 — 'Class III — amino acids'.** AMPA and NMDA side by side with a Mg²⁺ plug: 'glutamate → AMPA → Na⁺ → depolarisation → removes Mg²⁺ → NMDA Ca²⁺; glycine co-activates'; 'glutamate — hippocampus & subthalamic nucleus (memory), Aδ (fast pain)'; 'excitotoxicity → ↑ Ca²⁺ → cell death → ALS → riluzole'; 'subthalamic nucleus = only excitatory BG nucleus'. GABA: 'major inhibitory — caudate & putamen — inhibits involuntary movement — enhances hyperpolarisation (−70 → −90) — loss → Huntington's chorea'. Glycine: Renshaw loop, 'strychnine and tetanospasmin → spastic paralysis'.
>
> **Panel 8 — 'Class IV — gases'.** 'NO — from arginine — hippocampus — cGMP — ↑ glutamate release — learning & memory'; 'CO — heme → heme oxygenase 2 → CO — olfaction, pain, memory'.
>
> Footer strip: 'Pre-side decides how much; post-side receptor decides fast/slow and excite/inhibit; summation decides firing'. No watermark, no photographs, illustration quality."

---

## 📚 References

- Physiology main notes (Marrow 8) — *Synaptic Transmission and Neurotransmitters*, pp. 68–73
- Guyton & Hall Textbook of Medical Physiology — Organization of the nervous system; basic functions of synapses and transmitter substances
- Ganong's Review of Medical Physiology — Synaptic and junctional transmission; neurotransmitters and neuromodulators
- `Synaptic Transmission and Neurotransmitters - ….png` files in `attachments/` are crops of the handwritten pages

[^1]: Electrical synapses conduct in both directions with essentially no delay (heart, smooth muscle, some CNS neurons such as the inferior olive and retina); chemical synapses conduct one way only and have a minimal synaptic delay of about 0.5 ms (Guyton) — the time for Ca²⁺ entry, exocytosis, diffusion and receptor binding.
[^2]: The end plate potential at the neuromuscular junction is large enough to fire the muscle every time (a "safety factor"), whereas a single CNS EPSP is only ~0.5–1 mV; dozens must add up — spatially (many synapses at once) or temporally (rapid firing of one synapse) — at the axon initial segment to reach threshold.
[^3]: Axo-dendritic synapses are the most numerous; axo-axonic synapses are the anatomical basis of presynaptic inhibition.
[^4]: Ganong: slow EPSPs and IPSPs (autonomic ganglia, cardiac and smooth muscle, cortical neurons) have a latency of about 100–500 ms and last several seconds; they are mediated by G-protein-coupled receptors — e.g. muscarinic M1 closing K⁺ channels (slow EPSP) or GABA-B opening K⁺ channels (slow IPSP). The page's slow IPSP example cell is blank and is left blank.
[^5]: Presynaptic inhibition: an axo-axonic GABA-ergic interneuron reduces Ca²⁺ entry into one presynaptic terminal → less transmitter released from that input only. Lateral inhibition in the retina (horizontal and amacrine cells) sharpens contrast; textbooks treat it as surround inhibition built from such inhibitory interneurons. Renshaw cells are excited by ACh from the α motor neuron's recurrent collateral and release glycine back onto it and its neighbours.
[^6]: Otto Loewi (1921) showed that stimulating a frog's vagus released a substance ("Vagusstoff") that slowed a second heart; Henry Dale identified it as acetylcholine. They shared the 1936 Nobel Prize.
[^7]: Fuller textbook criteria also require a mechanism that removes or inactivates the substance (enzyme, reuptake) and that applying it artificially mimics the natural effect. NO and CO break the classical rules — they are not stored in vesicles and diffuse freely.
[^8]: Botulinum toxins A and E cleave SNAP-25, C cleaves syntaxin (and SNAP-25), B, D, F and G cleave synaptobrevin (VAMP); tetanus toxin also cleaves synaptobrevin but in spinal inhibitory interneurons. Botulism gives a descending, symmetrical flaccid paralysis with cranial-nerve palsies first.
[^9]: The muscle nicotinic receptor is a pentamer (2 α, β, δ, ε) forming a non-selective cation channel. Muscarinic receptors M1–M5: M1, M3, M5 couple to Gq; M2, M4 to Gi.
[^10]: Sympathetic cholinergic fibres to sweat glands act on muscarinic (M3) receptors — atropine poisoning therefore produces hot, dry skin.
[^11]: Synthesis chain: tyrosine → (tyrosine hydroxylase, rate-limiting) → DOPA → (DOPA decarboxylase) → dopamine → (dopamine β-hydroxylase, inside vesicles; ascorbic acid as cofactor — shown in the page's class II structures) → norepinephrine → (PNMT, adrenal medulla) → epinephrine.
[^12]: D1-like receptors (D1, D5) couple to Gs (↑ cAMP); D2-like (D2, D3, D4) to Gi (↓ cAMP). Lactotrophs carry D2 receptors — D2-blocking antipsychotics cause hyperprolactinaemia, and D2 block in the nigrostriatal pathway causes extrapyramidal side effects. Mesolimbic overactivity is linked to the positive symptoms of schizophrenia, mesocortical underactivity to the negative symptoms.
[^13]: About 90 % of the body's serotonin is made by enterochromaffin cells of the gut; platelets do not synthesise it but take it up from plasma and release it when they aggregate. In the brain it comes from the raphe nuclei of the brainstem.
[^14]: Ondansetron and granisetron block 5-HT3 receptors in the area postrema (chemoreceptor trigger zone) and on vagal afferents. Prucalopride (5-HT4 agonist) is a prokinetic; triptans act on 5-HT1B/1D receptors (5-HT1 is on the page only as the first of the family).
[^15]: Brain histamine comes from the tuberomammillary nucleus of the posterior hypothalamus — sedating first-generation H1 antihistamines cross the blood–brain barrier. In the stomach, histamine is released by enterochromaffin-like (ECL) cells and acts on H2 receptors of the parietal cell, which secretes HCl; the page labels the parietal cell.
[^16]: NMDA receptor activation therefore needs three things: glutamate, glycine (or D-serine) as co-agonist, and depolarisation (via AMPA) to expel Mg²⁺. The resulting Ca²⁺ entry triggers long-term potentiation — the cellular basis of memory in the hippocampus.
[^17]: Riluzole is usually described as reducing presynaptic glutamate release and blocking voltage-gated Na⁺ channels, with some non-competitive inhibition of NMDA responses; the page's label "NMDA blocker" is kept. It prolongs survival in ALS modestly.
[^18]: All other basal-ganglia nuclei (striatum, globus pallidus, substantia nigra pars reticulata) use GABA; a lesion of the subthalamic nucleus causes contralateral hemiballismus ([[Cerebellum and Basal Ganglia]]).
[^19]: GABA-A receptors are Cl⁻ channels (enhanced by benzodiazepines and barbiturates); GABA-B receptors are GPCRs that open K⁺ channels (baclofen). Huntington's disease is an autosomal dominant CAG-repeat disorder (*HTT*, chromosome 4) that destroys the GABA-ergic medium spiny neurons of the caudate first.
[^20]: Standard pharmacology: **strychnine** is a competitive **antagonist of the glycine receptor** (it blocks glycine's action rather than its release — the page's figure itself labels it "antagonist of glycine"); **tetanospasmin** blocks the **release of both glycine and GABA** from spinal inhibitory interneurons. Either way the α motor neurons lose their brake.
[^21]: NO is made from L-arginine by Ca²⁺–calmodulin-dependent neuronal NO synthase; it diffuses back from the postsynaptic to the presynaptic neuron (a retrograde messenger), activates soluble guanylyl cyclase → cGMP, and increases glutamate release — part of long-term potentiation in the hippocampus.
[^22]: Heme oxygenase splits heme into biliverdin, Fe²⁺ and CO; HO-2 is the constitutive (neuronal) form and HO-1 the inducible (stress) form. Like NO, CO activates guanylyl cyclase.
[^ety-synapse]: **synapse** — Greek *syn-*, "together" + *haptein*, "to fasten, clasp" → *synapsis*, "a clasping together"; coined by Charles Sherrington (1897) for the junction between neurons. **Differentiate:** *synapse* (neuron → cell junction) · *synapsis* (pairing of homologous chromosomes in meiosis) · *gap junction* (electrical synapse).
[^ety-neurotransmitter]: **neurotransmitter** — Greek *neuron*, "nerve" + Latin *trans-*, "across" + *mittere*, "to send" + *-er*, agent → the chemical that sends the signal across the synapse. **Differentiate:** *neurotransmitter* (acts across one synapse, fast) · *neuromodulator* (alters how a synapse responds) · *neurohormone* (released into blood — ADH, oxytocin).
[^ety-connexin]: **connexin** — Latin *connexus*, "joined together" (*con-* + *nectere*, "to bind") + *-in*, a protein → the joining protein of gap junctions; six form a connexon (half-channel).
[^ety-potential]: **potential** — Latin *potentia*, "power" (from *posse*, "to be able") → stored electrical power; a voltage difference across a membrane. **Differentiate:** *local / graded potential* (EPSP, IPSP, end plate potential — size varies, decays, summates) · *action potential* (all-or-none, propagated, cannot summate).
[^ety-summation]: **summation** — Latin *summa*, "total" + *-ation* → the process of adding up. **Differentiate:** *spatial summation* (many synapses firing at once) · *temporal summation* (one synapse firing repeatedly in quick succession).
[^ety-threshold]: **threshold** — Old English *therscold*, "the sill of a doorway" (the board you step over) → the membrane potential (≈ −55 mV in a neuron) that must be crossed for an AP to fire.
[^ety-dendrite]: **dendrite** — Greek *dendron*, "tree" + *-ites*, "of the nature of" → the tree-like branches of a neuron that receive synapses. **Differentiate:** *dendrite* (receives) · *axon* (*axōn*, axle — sends) · *soma* (*sōma*, body — integrates).
[^ety-excitatory]: **excitatory** — Latin *ex-*, "out" + *citare*, "to set in motion, call" + *-atory*, "tending to" → tending to call out a response; an excitatory PSP moves the membrane towards threshold (depolarises).
[^ety-inhibitory]: **inhibitory** — Latin *in-*, "in, upon" + *habere*, "to hold" → *inhibere*, "to hold back, restrain" + *-ory* → restraining; an inhibitory PSP moves the membrane away from threshold (hyperpolarises or clamps it).
[^ety-facilitation]: **facilitation** — Latin *facilis*, "easy to do" (from *facere*, "to do") + *-ation* → the process of making easier; more transmitter per impulse, so the next neuron fires more easily. **Differentiate:** *facilitation* (presynaptic ↑ release, short-term) · *potentiation* (long-term ↑ response, LTP) · *summation* (adding PSPs).
[^ety-retina]: **retina** — Medieval Latin, probably from *rete*, "net" → the net-like inner layer of the eye (its network of vessels) where lateral inhibition sharpens edges.
[^ety-renshaw]: **Renshaw cell** — Birdsey Renshaw (1911–1948), American neurophysiologist, who described in 1941 the recurrent inhibition of motor neurons by small spinal interneurons, later named Renshaw cells.
[^ety-biogenic]: **biogenic** — Greek *bios*, "life" + *-genēs*, "born, produced" + *-ic* → produced by living organisms; *biogenic amines* are amines made in the body by decarboxylating amino acids (tyrosine → DA, NE; tryptophan → 5-HT; histidine → histamine).
[^ety-amine]: **amine** — from *ammonia* (named after the temple of Ammon in Libya, where ammonium salts were collected) + *-ine* → a compound in which a hydrogen of ammonia is replaced by a carbon group; *monoamines* (DA, NE, 5-HT, histamine) have one amine group.
[^ety-acetylcholine]: **acetylcholine** — *acetyl* (Latin *acetum*, "vinegar") + *choline* (Greek *cholē*, "bile", where choline was first isolated) → the acetic ester of choline. **Differentiate:** *cholinergic* (uses ACh) · *cholinesterase* (breaks it down) · *anticholinergic* (blocks it — atropine).
[^ety-exocytosis]: **exocytosis** — Greek *exō*, "outside" + *kytos*, "a hollow, cell" + *-osis*, "process" → the process of moving out of the cell: the vesicle fuses with the membrane and empties its contents outside. **Differentiate:** *exocytosis* (out) · *endocytosis* (in) · *transcytosis* (across).
[^ety-snare]: **SNARE** — acronym: **S**oluble **N**SF **A**ttachment protein **RE**ceptor (NSF = N-ethylmaleimide-sensitive factor); a deliberate pun on *snare*, "a trap" — the proteins snare the vesicle to the membrane. *v-SNARE* on the vesicle (synaptobrevin), *t-SNAREs* on the target membrane (syntaxin, SNAP-25).
[^ety-syntaxin]: **syntaxin / synaptobrevin / synaptotagmin** — *syntaxin* from Greek *syntaxis*, "arrangement together"; *synaptobrevin* from *synapse* + Latin *brevis*, "short" (a short vesicle protein); *synaptotagmin* from *synapse* + Greek *tagma*, "something arranged, a unit". All three name SNARE-complex proteins of the synaptic terminal.
[^ety-botulinum]: **botulinum** — Latin *botulus*, "sausage" → named from sausage poisoning (*botulism*) described by Justinus Kerner in Germany in the 1820s; *Clostridium botulinum* produces the most potent known toxin.
[^ety-toxin]: **toxin** — Greek *toxikon (pharmakon)*, "(poison) for arrows" (from *toxon*, "bow") + *-in* → a poison of biological origin. **Differentiate:** *toxin* (biological) · *toxicant* (synthetic poison) · *venom* (toxin injected by an animal).
[^ety-flaccid]: **flaccid** — Latin *flaccidus*, "flabby, drooping" (from *flaccus*, "flap-eared") → limp with lost tone. **Differentiate:** *flaccid* paralysis (lower motor neuron / NMJ — botulinum) · *spastic* paralysis (loss of inhibition / upper motor neuron — tetanus, strychnine).
[^ety-paralysis]: **paralysis** — Greek *para-*, "beside, abnormally" + *lyein*, "to loosen" + *-sis*, process → *paralysis*, "a loosening on one side, disabling" → loss of voluntary movement. **Differentiate:** *paralysis / -plegia* (complete loss) · *paresis* (partial weakness) · *palsy* (old French form of paralysis).
[^ety-nicotinic]: **nicotinic** — from **nicotine**, named after Jean Nicot (1530–1600), French ambassador to Portugal who sent tobacco to Paris in 1560 + *-ic* → the ACh receptor that nicotine stimulates (NMJ, autonomic ganglia).
[^ety-ionotropic]: **ionotropic / metabotropic** — Greek *ion*, "going" (a charged particle that moves) + *tropos*, "turning, acting on" → a receptor that acts on an ion channel (it *is* the channel) — fast; *meta-*, "change" + *bolē* (metabolism) + *tropos* → a receptor acting through metabolic second messengers (G protein) — slow.
[^ety-muscarinic]: **muscarinic** — from **muscarine**, an alkaloid of the fly agaric mushroom *Amanita muscaria* (Latin *musca*, "fly" — it was used to kill flies) + *-ic* → the ACh receptor muscarine stimulates (heart, glands, smooth muscle).
[^ety-meynert]: **nucleus basalis of Meynert** — Theodor Meynert (1833–1892), German–Austrian neuropathologist in Vienna, who described this basal forebrain nucleus (1872); *basalis*, "of the base" — the main cholinergic source for the cortex.
[^ety-alzheimer]: **Alzheimer's disease** — Alois Alzheimer (1864–1915), German psychiatrist, who in 1906 described plaques and neurofibrillary tangles in the brain of a 51-year-old woman (Auguste D.) with progressive dementia.
[^ety-rem]: **REM** — acronym: **R**apid **E**ye **M**ovement sleep (Aserinsky and Kleitman, 1953) — the dreaming stage switched on by cholinergic "REM-on" neurons of the pons.
[^ety-norepinephrine]: **norepinephrine** — *nor-* (German *N ohne Radikal*, "nitrogen without a radical": no N-methyl group) + Greek *epi-*, "upon" + *nephros*, "kidney" + *-ine* → the de-methylated hormone of the gland upon the kidney; Latin synonym *noradrenaline*.
[^ety-locus-coeruleus]: **locus coeruleus** — Latin *locus*, "place" + *caeruleus*, "sky-blue, dark blue" → "the blue place": a pigmented (neuromelanin) nucleus in the dorsal pons, the brain's main NE source.
[^ety-dopamine]: **dopamine** — acronym-word from **D**ihydr**o**xy**p**henyl-ethyl**amine** → the catecholamine made from L-DOPA; precursor of NE and a transmitter in its own right.
[^ety-nigrostriatal]: **nigrostriatal** — Latin *niger*, "black" (*substantia nigra*, the black substance — neuromelanin) + *striatum*, "streaked" + *-al* → the pathway from the black substance to the streaked body (caudate + putamen).
[^ety-mesolimbic]: **mesolimbic / mesocortical** — Greek *mesos*, "middle" (the *mesencephalon*, midbrain) + Latin *limbus*, "border, edge" (the limbic lobe borders the brainstem) / *cortex*, "bark, outer layer" → pathways from the midbrain to the limbic system and to the cortex.
[^ety-tuberoinfundibular]: **tuberoinfundibular** — Latin *tuber*, "a swelling, lump" (*tuber cinereum* of the hypothalamus) + *infundibulum*, "a funnel" (*in-* + *fundere*, to pour — the pituitary stalk) + *-ar* → from the hypothalamic tuber down the funnel to the pituitary.
[^ety-tegmental]: **tegmental** — Latin *tegmentum*, "a covering" (from *tegere*, "to cover") + *-al* → the "covering" floor of the midbrain over the cerebral peduncles; the ventral tegmental area (VTA) holds the mesolimbic/mesocortical dopamine neurons.
[^ety-accumbens]: **nucleus accumbens** — Latin *accumbere*, "to lie beside, recline" → the nucleus lying against the septum; the brain's reward centre.
[^ety-prolactin]: **prolactin** — Latin *pro-*, "for, promoting" + *lac, lactis*, "milk" + *-in* → the hormone promoting milk; the only anterior pituitary hormone under predominantly inhibitory (dopamine) control.
[^ety-bradykinesia]: **bradykinesia** — Greek *bradys*, "slow" + *kinēsis*, "movement" + *-ia*, condition → slowness of movement. **Differentiate:** *bradykinesia* (slow) · *hypokinesia* (reduced amplitude) · *akinesia* (absence / difficulty initiating) · *dyskinesia* (abnormal involuntary movement).
[^ety-parkinson]: **Parkinson's disease** — James Parkinson (1755–1824), English surgeon-apothecary, who described "the shaking palsy" (*paralysis agitans*) in his 1817 *Essay on the Shaking Palsy*; Charcot named it after him.
[^ety-serotonin]: **serotonin** — Latin *serum* (the clear fluid of clotted blood) + Greek *tonos*, "tension, tone" + *-in* → the substance in serum that raises vascular tone; named by Rapport, Green and Page (1948). Chemical name 5-hydroxytryptamine.
[^ety-raphe]: **raphe** — Greek *rhaphē*, "a seam, suture" → the midline "seam" of the brainstem where the serotonergic raphe nuclei lie. Same word in *raphe of the scrotum, palate*.
[^ety-peristalsis]: **peristalsis** — Greek *peri-*, "around" + *stellein*, "to place, compress" → *peristaltikos*, "clasping and compressing around" → the wave of circular contraction that pushes gut contents forward. **Differentiate:** *peristalsis* (propulsive) · *segmentation* (mixing) · *antiperistalsis* (reverse — vomiting).
[^ety-hydroxytryptamine]: **5-hydroxytryptamine** — *hydroxy* (OH group; Greek *hydōr*, water + *oxy*, oxygen) at position 5 + *tryptamine* (from *tryptophan*: Greek *tryptein*, "to rub, wear down" — it was found in tryptic digests of protein — + *phainein*, "to show") + *amine* → serotonin's chemical name.
[^ety-satiety]: **satiety** — Latin *satietas*, from *satis*, "enough" → the state of having had enough food; 5-HT2c activation in the hypothalamus increases satiety and reduces food intake.
[^ety-area-postrema]: **area postrema** — Latin *area*, "an open space" + *postrema*, "hindmost, last" → the hindmost area at the bottom of the fourth ventricle; outside the blood–brain barrier, it is the chemoreceptor trigger zone for vomiting.
[^ety-histamine]: **histamine** — Greek *histos*, "tissue" + *amine* → the amine found in tissues (formed from histidine); first isolated from ergot and tissues by Dale and Laidlaw (1910).
[^ety-hypothalamus]: **hypothalamus** — Greek *hypo-*, "below" + *thalamos*, "inner chamber" → the region below the thalamus; its posterior part (tuberomammillary nucleus) holds the brain's histamine neurons.
[^ety-pineal]: **pineal** — Latin *pinea*, "pine cone" + *-al* → the pine-cone–shaped gland that secretes melatonin.
[^ety-parietal]: **parietal** — Latin *paries, parietis*, "wall" + *-al* → of the wall; *parietal cells* sit in the walls of the gastric glands and secrete HCl and intrinsic factor. **Differentiate:** *parietal cell* (stomach) · *parietal bone / lobe* (side "walls" of the skull/brain) · *parietal pleura* (lining the chest wall).
[^ety-glutamate]: **glutamate** — Latin *gluten*, "glue" (glutamic acid was first isolated from wheat gluten by Ritthausen, 1866) + *-amic* + *-ate*, salt → the salt of glutamic acid; the brain's main excitatory transmitter.
[^ety-hippocampus]: **hippocampus** — Greek *hippos*, "horse" + *kampos*, "sea monster" → "sea horse", for its curled shape in coronal section; the memory-forming structure of the medial temporal lobe.
[^ety-depolarisation]: **depolarisation** — Latin *de-*, "away, reversal" + *polaris*, "of the poles" + *-isation*, "making" → the process of removing the membrane's polarity (inside becomes less negative). **Differentiate:** *depolarisation* (towards 0) · *repolarisation* (back to resting) · *hyperpolarisation* (more negative than resting).
[^ety-ampa]: **AMPA** — acronym: **α**-**a**mino-3-hydroxy-5-**m**ethyl-4-isoxazole**p**ropionic **a**cid — the synthetic agonist after which this fast glutamate receptor (Na⁺/K⁺ channel) is named.
[^ety-nmda]: **NMDA** — acronym: **N**-**m**ethyl-**D**-**a**spartate — the synthetic agonist after which this glutamate receptor (Ca²⁺-permeable, Mg²⁺-blocked) is named.
[^ety-excitotoxicity]: **excitotoxicity** — Latin *excitare*, "to rouse" + Greek *toxikon*, "poison" + *-icity*, "state" → poisoning by over-excitation; coined by John Olney (1969) for neuron death caused by excess glutamate → Ca²⁺ overload.
[^ety-als]: **amyotrophic lateral sclerosis** — Greek *a-*, "without" + *mys*, "muscle" + *trophē*, "nourishment" + *-ic* → muscle without nourishment (wasting, from LMN loss); *lateral*, the lateral columns of the cord (corticospinal tract, UMN loss); *sclerosis* (Greek *sklērōsis*, hardening) — the scarred columns. Described by Jean-Martin Charcot (1869); also called Lou Gehrig disease.
[^ety-gaba]: **GABA** — acronym: **γ**-**A**mino**B**utyric **A**cid; *butyric* from Latin *butyrum*, "butter" (butyric acid smells of rancid butter); *gamma* — the amino group sits on the third (γ) carbon.
[^ety-caudate]: **caudate** — Latin *cauda*, "tail" + *-ate* → the tailed nucleus, curving with a long tail beside the lateral ventricle.
[^ety-putamen]: **putamen** — Latin, "husk, shell, clipping" (from *putare*, "to prune") → the outer shell of the lentiform nucleus.
[^ety-striatum]: **striatum** — Latin *striatus*, "streaked" → the caudate and putamen together, streaked by grey bridges crossing the internal capsule.
[^ety-hyperpolarisation]: **hyperpolarisation** — Greek *hyper-*, "over, beyond" + *polaris* + *-isation* → making the membrane more polarised (more negative inside) than at rest, as GABA and glycine do via Cl⁻ entry or K⁺ exit.
[^ety-huntington]: **Huntington's disease** — George Huntington (1850–1916), American physician from Long Island, who described hereditary chorea in 1872 in his paper "On Chorea".
[^ety-chorea]: **chorea** — Greek *choreia*, "a dance" (as in *choreography*) → brief, irregular, flowing involuntary movements like dancing. **Differentiate:** *chorea* (dance-like, distal — striatum) · *ballismus* (*ballein*, to throw — wild flinging, proximal — subthalamic nucleus) · *athetosis* (*athetos*, not fixed — slow writhing).
[^ety-glycine]: **glycine** — Greek *glykys*, "sweet" + *-ine* → the sweet-tasting amino acid (the simplest one); inhibitory transmitter of the spinal cord and co-agonist of NMDA. Not a sugar despite *glyco-*.
[^ety-strychnine]: **strychnine** — Greek *strychnos*, a name for nightshade-type plants, given to *Strychnos nux-vomica* (the poison nut tree) + *-ine* → the alkaloid from its seeds; isolated by Pelletier and Caventou (1818); a glycine-receptor antagonist.
[^ety-tetanospasmin]: **tetanospasmin** — Greek *tetanos*, "taut, stretched" + *spasmos*, "convulsion" + *-in* → the spasm-making toxin of *Clostridium tetani*; a zinc protease that cleaves synaptobrevin in spinal inhibitory interneurons.
[^ety-spastic]: **spastic** — Greek *spastikos*, "drawing, pulling" (from *span*, "to pull") → stiff with increased tone that resists passive movement (velocity-dependent). **Differentiate:** *spasticity* (velocity-dependent, clasp-knife — UMN, loss of inhibition) · *rigidity* (uniform, lead-pipe or cogwheel — basal ganglia) · *spasm* (sudden involuntary contraction).
[^ety-nitric-oxide]: **nitric oxide** — Greek *nitron*, "native soda" (nitre) + *-ic* + *oxide* (Greek *oxys*, "sharp, acid" — oxygen was named as the "acid-maker") → NO, a gas made from arginine; originally discovered as endothelium-derived relaxing factor (Furchgott, Ignarro, Murad — Nobel 1998).
[^ety-arginine]: **arginine** — Latin *argentum*, "silver" + *-ine* → named (Schulze and Steiger, 1886) because it was first crystallised as its silver salt; the amino acid that NO synthase turns into NO + citrulline.
[^ety-heme]: **heme / haem** — Greek *haima*, "blood" → the iron–porphyrin ring of haemoglobin; heme oxygenase splits it to biliverdin, iron and CO.
[^ety-oxygenase]: **oxygenase** — *oxygen* (Greek *oxys*, "acid" + *-genēs*, "producing") + *-ase*, enzyme → an enzyme that inserts oxygen into a substrate. **Differentiate:** *oxygenase* (adds O₂ atoms) · *oxidase* (uses O₂ as electron acceptor) · *dehydrogenase* (removes hydrogen).
[^ety-olfaction]: **olfaction** — Latin *olfacere*, "to smell" (*olere*, "to give off a smell" + *facere*, "to make") + *-ion* → the sense of smell. **Differentiate:** *olfaction* (smell) · *gustation* (taste) · *anosmia* (*an-* + *osmē* — loss of smell).
[^pre-syn]: **syn- / sym-** — together, with: synapse, syntaxin, synaptobrevin, sympathetic. Don't confuse with **sin-** left (Latin *sinister*) · **semi-** half.
[^pre-neuro]: **neuro- / neur-** — nerve: neurotransmitter, neuron, neuromuscular. Don't confuse with **nephro-** kidney · **neo-** new.
[^pre-trans]: **trans-** — across, through, beyond: neurotransmitter, transmission, transcytosis, transduction. Don't confuse with **trans-** in chemistry (opposite sides) · **inter-** between · **dia-** through (Greek).
[^pre-con]: **con- / com- / co-** — together, with: connexin, conduction, co-agonist. Don't confuse with **contra-** against · **counter-** against.
[^pre-pre]: **pre-** — before, in front of: presynaptic, prefrontal, preganglionic. Don't confuse with **pro-** forward, for (prolactin) · **post-** after · **peri-** around.
[^pre-post]: **post-** — after, behind: postsynaptic, area postrema (hindmost), posterior. Don't confuse with **pre-** before · **para-** beside · **meta-** after/change (Greek).
[^pre-ex]: **ex- / e- / ef-** — out, out of: excitatory, exocytosis (Greek *exo*), efferent. Don't confuse with **exo-** outside (Greek) · **extra-** beyond · **ec-** out (ectopic).
[^pre-in]: **in- (upon, in)** — in, into, upon: inhibitory (*in-* + *habere*), innervation, influx. Don't confuse with **in- (not)** — involuntary, insensitive · **intra-** within · **infra-** below.
[^suf-ation]: **-ation / -ion** — the process or result: facilitation, transmission, olfaction, depolarisation. Don't confuse with **-osis** a condition or process (exocytosis, sclerosis) · **-ism** a state.
[^pre-inter]: **inter-** — between: interneuron, intercalated, interstitial. Don't confuse with **intra-** within · **infra-** below.
[^pre-bio]: **bio-** — life: biogenic, biology, biopsy. Don't confuse with **bi- / bis-** two (bilateral, bicarbonate) · **brady-** slow.
[^suf-genic]: **-genic / -genesis** — producing, produced by, origin: biogenic, neurogenic, myogenic, pathogenesis. Don't confuse with **-gen** a precursor (pepsinogen, allergen) · **-genous** born in (endogenous).
[^pre-mono]: **mono-** — one, single: carbon monoxide (one oxygen), monoamine, monocyte. Don't confuse with **mono-** vs **uni-** (Latin synonym) · **di-** two (dioxide) · **poly-** many.
[^pre-exo]: **exo-** — outside, outer: exocytosis, exocrine, exogenous. Don't confuse with **ecto-** outer layer (ectoderm) · **endo-** within (endocytosis) · **extra-** (Latin) outside.
[^suf-osis]: **-osis** — a process, condition or increase: exocytosis, sclerosis, fibrosis, leucocytosis. Don't confuse with **-itis** inflammation · **-iasis** an infestation (amoebiasis) · **-ation** a process (Latin).
[^pre-para]: **para-** — beside, abnormal, faulty: paralysis, parasympathetic, paraesthesia. Don't confuse with **peri-** around · **pre-** before.
[^suf-lysis]: **-lysis** — loosening, dissolving, breakdown: paralysis, glycolysis, haemolysis. Don't confuse with **-lytic** the adjective · **-plasty** repair · **-stasis** standstill.
[^suf-tropic]: **-tropic / -tropy** — turning towards, acting on: ionotropic, metabotropic, inotropic, gonadotropic. Don't confuse with **-trophic / -trophy** nourishing, growth (amyotrophic, hypertrophy, neurotrophic).
[^pre-meta]: **meta-** — change, after, beyond: metabotropic, metabolism, metastasis. Don't confuse with **meso-** middle · **para-** beside.
[^suf-ergic]: **-ergic** — working by means of a transmitter: cholinergic, adrenergic, dopaminergic, GABA-ergic, serotonergic. Don't confuse with **-ergy / ergo-** work, energy (synergy, ergometer) · **-urgy** working (surgery).
[^pre-epi]: **epi-** — upon, above, over: epinephrine, epidermis, epiglottis. Don't confuse with **endo-** within · **hypo-** below · **ecto-** outer.
[^pre-meso]: **meso-** — middle: mesolimbic, mesocortical, mesencephalon, mesoderm. Don't confuse with **meta-** change, after · **medio-** middle (Latin: mediolateral).
[^pre-pro]: **pro-** — before, forward, for, promoting: prolactin (for milk), prokinetic, prodrome. Don't confuse with **pre-** before (in time or place) · **post-** after.
[^pre-brady]: **brady-** — slow: bradykinesia, bradycardia, bradykinin. Don't confuse with **brachy-** short (brachydactyly) · **tachy-** fast.
[^suf-kinesia]: **-kinesia / -kinesis / -kinetic** — movement: bradykinesia, dyskinesia, akinesia, cytokinesis. Don't confuse with **-kinin** a peptide that moves (bradykinin — a vasoactive peptide) · **-kinase** an enzyme that transfers phosphate.
[^pre-peri]: **peri-** — around: peristalsis, pericardium, periaqueductal. Don't confuse with **para-** beside · **pre-** before · **epi-** upon.
[^pre-hydroxy]: **hydroxy- / hydro-** — the OH group / water: 5-hydroxytryptamine, hydroxylase, hydrolysis. Don't confuse with **hydro-** as fluid (hydrocephalus) · **hygro-** moisture · **hyper-** over.
[^pre-hypo]: **hypo-** — below, under, deficient: hypothalamus, hypokinesia, hypotension. Don't confuse with **hyper-** over · **hypno-** sleep.
[^suf-ate]: **-ate** — the salt or ester of an acid: glutamate, aspartate, lactate, phosphate. Don't confuse with **-ase** an enzyme · **-ite** a lower-oxygen salt (nitrite).
[^pre-sub]: **sub-** — under, below: subthalamic, subarachnoid, subcortical. Don't confuse with **supra-** above · **hypo-** below (Greek synonym) · **infra-** below.
[^pre-de]: **de-** — removal, reversal, down from: depolarisation, dephosphorylation, denervation. Don't confuse with **dis-** apart · **dys-** bad · **di-** two.
[^pre-a]: **a- / an-** — without, not: amyotrophic, akinesia, anosmia, analgesia. Don't confuse with **ana-** up, again · **ad- / a-** towards (ascend) · **ab-** away.
[^suf-trophic]: **-trophic / -trophy** — nourishment, growth: amyotrophic (muscle without nourishment → wasting), hypertrophy, neurotrophic. Don't confuse with **-tropic** turning, acting on (ionotropic) · **-atrophy** (*a-* + *trophē* — wasting).
[^pre-hyper]: **hyper-** — over, above, excessive: hyperpolarisation, hyperprolactinaemia, hyperalgesia. Don't confuse with **hypo-** under · **super- / supra-** above (Latin).
[^suf-spasm]: **-spasm** — an involuntary sudden contraction: tetanospasmin, vasospasm, laryngospasm. Don't confuse with **-plasm** formed material (cytoplasm) · **-stasis** standing still.
[^suf-ide]: **-ide** — a binary compound or anion: oxide, chloride, sulfide, peptide (from a similar ending). Don't confuse with **-ite / -ate** oxygen-containing salts (nitrite, nitrate) · **-oid** like (steroid).
[^suf-ase]: **-ase** — an enzyme: oxygenase, hydroxylase, cholinesterase, kinase. Don't confuse with **-ose** a sugar · **-ate** a salt.
