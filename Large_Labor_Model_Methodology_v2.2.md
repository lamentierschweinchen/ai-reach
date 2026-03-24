# Large Labor Model — Methodology

**Version 2.2 — March 2026**

This document describes how the Large Labor Model dataset was produced. It is written so that someone with no prior knowledge of the project can understand how every number in the dataset was derived, what assumptions were made, and where the model is weakest. It is the single reference for anyone who wants to challenge, extend, or build on this work.

---

## 1. What this project measures

The Large Labor Model maps two things across time:

**Labor shares** — how many people work in each category of human activity, globally, from 1800 to 2041.

**Replaceability** — when AI or robotics becomes technically capable of performing the core tasks of each category, scored 0–100.

These are separate measurements. Replaceability tracks the technical frontier. Labor shares track the actual economy. The gap between the two — between what AI *can* do and what has actually *changed* in the labor market — is not a flaw in the model. It is one of the most important things the model shows.

### 1.1 Replaceability defined

A replaceability score answers one question: **can the best commercially available AI or robotics perform the core tasks of this role?**

The threshold is commercial availability — a product you can buy. A prototype in a lab does not raise the score. Geographic variation in deployment, economic viability at average scale, regulatory permission, and social preference do not affect the score. All of these are recorded separately as barrier annotations.

This means a territory can score 90 (almost fully replaceable) while employment in that territory has barely changed. That is not a contradiction — it is the replaceability/replacement distinction at work.

### 1.2 Replacement defined

Replacement is when workers actually lose jobs. This lags replaceability by months to decades, depending on capital costs, regulation, institutional inertia, social preference, and political will.

The displacement model (Section 5) converts replaceability into projected employment change. The labor share data tracks actual historical employment. Together they show: here is what AI can technically do, and here is what has actually happened to jobs. The distance between those two lines is the project's central provocation.

---

## 2. Territory definitions

Human work is organized into 13 territories. Each maps to one or more sections of the International Standard Industrial Classification (ISIC Rev. 4). The territory names are editorial — designed to be legible to a general audience rather than to an economist. The ISIC mapping ensures that every territory corresponds to a standard, internationally comparable definition of economic activity.

| Territory | What it covers | ISIC Sections |
|---|---|---|
| Land & Sea | Agriculture, forestry, fishing, mining, quarrying | A, B |
| Making Things | Manufacturing | C |
| Building Things | Construction | F |
| Moving Things | Transport, logistics, warehousing | H |
| Buying & Selling | Retail and wholesale trade | G |
| Money & Data | Finance, insurance, real estate, information | J, K, L |
| Care & Health | Human health and social work | Q |
| Learning & Teaching | Education | P |
| Making Meaning | Arts, media, creative industries | R |
| Governing & Protecting | Public administration, defense | O |
| Feeding & Hosting | Accommodation, food service | I |
| Maintaining & Fixing | Utilities, repair, personal services | D, E, S |
| Thinking & Leading | Professional, scientific, technical, management | M, N |

The territory groupings are an editorial layer over the native ISIC classification. The underlying data is keyed to ISIC sections so that regrouping territories does not require re-collecting data.

---

## 3. Data sources and quality

### 3.1 Labor share data

The labor share layer covers 1800–2025 (historical) and 2026–2041 (projected).

**1800–1870 (LOW quality):** Employment shares reconstructed from Bairoch (1988), cross-checked against Mitchell (2003) and Cambridge Group occupational reconstructions. Global workforce totals derived from Maddison Project population estimates combined with estimated labor force participation rates. Only three macro sectors are distinguishable at this resolution: agriculture (Land & Sea), industry (macro_industry), and services (macro_services). These are editorial reconstructions, not observed data.

**1900–1970 (MEDIUM quality):** Progressive disaggregation as census data and national accounts support more granular sectoral estimates. Transition from three macro sectors to the full 13-territory resolution occurs between 1950 and 1991, with the exact year depending on data availability for each territory. Primary sources: Mitchell (2003), ILO historical estimates, GGDC 10-Sector Database.

**1991–2025 (HIGH quality):** Full 13-territory resolution. Primary source: ILOSTAT modelled estimates (November 2024 vintage for most records). These are econometric model outputs produced by the ILO, not raw survey data, but they represent the international standard for globally comparable labor market statistics. Coverage: 189 countries.

**Quality flags:** Every labor record carries a data_quality field (LOW, MEDIUM, or HIGH) indicating the reliability of the underlying source material.

**Missing data:** Null values remain null. The dataset does not fabricate data for periods or territories where no reliable source exists.

**Sum constraint:** Labor shares sum to 100% at every historical year. This is enforced by proportional normalization where raw sources produce sums that deviate from 100%.

**Known issue — ILO vintage drift:** The dataset uses the November 2024 vintage of ILO modelled estimates for most 2024–2025 figures. The ILO's November 2025 vintage (published in the Employment and Social Trends 2026 report, January 2026) places 2025 global employment at approximately 3,599 million — 49 million (1.4%) above this dataset's 3,550 million. The gap is partly driven by the ILO's revised treatment of India's Periodic Labour Force Survey data. This drift does not affect the model's internal consistency but means the conservative baseline sits slightly below current ILO consensus.

### 3.2 Replaceability data

The replaceability layer covers 1970–2026 (historical, no scenario) and 2027–2041 (projected, three scenarios).

**1970–2014:** Retrospective calibration anchored to known technology milestones. Scores are low (typically 0–15) and reflect narrow subtask automation only. These values establish the baseline from which the acceleration becomes visible.

**2015–2026:** Benchmark-anchored scoring. Each territory's score at each year is tied to a specific commercial capability milestone (e.g., Waymo commercial operations for Moving Things, SWE-bench performance for Thinking & Leading, Xiaomi dark factory for Making Things). The 2026 scores serve as the baseline for all projections and are locked.

**2027–2041:** Projected under three scenarios (see Section 4). Anchor years: 2027, 2028, 2029, 2030, 2032, 2035, 2040, 2041. The visualization interpolates linearly between anchor points.

**Scoring scale:**

| Score | Meaning | Example |
|---|---|---|
| ~5 | Narrow subtask automation; role not substitutable | Single-task construction robot (2015) |
| ~25 | AI handles specific bounded tasks; majority beyond frontier | Agricultural GPS auto-steer + drone spraying (2020) |
| ~50 | Frontier AI capable of most core functions; not all | Radiology AI matching human accuracy (2024) |
| ~75 | Capable of full role with minimal human involvement | SWE-bench 71.7%; AI writes 30–50% of production code (2024) |
| ~90+ | Complete technical substitution possible at frontier | Xiaomi zero-worker smartphone factory (2024) |

**Methodology constraints:**

- Monotonicity: scores are non-decreasing within each territory-scenario. AI capability does not regress.
- Cross-scenario ordering: accelerated ≥ moderate ≥ conservative at every anchor year.
- Both constraints are validated programmatically. The current dataset has zero violations.

### 3.3 Occupation data

405 occupations mapped to ISCO-08 4-digit codes, each assigned to one territory. Every occupation carries a 2026 replaceability score and 2030 projections under all three scenarios.

Occupation scores were derived from a combination of benchmark research and model training knowledge. The scoring basis for individual occupations is not independently verifiable to the same standard as territory-level scores. This is a known limitation. The occupation layer exists primarily for the public-facing "find your job" feature and should be understood as indicative rather than definitive.

### 3.4 Technology events

57 milestone events from 1764 to 2026, each assigned to a primary territory. These serve as annotation markers on the timeline, not as inputs to the model. A maximum of two events per year are displayed.

Events were selected for labor relevance — moments when a technology became commercially available and changed or threatened to change how work is done. Culturally famous milestones (Turing's paper, ENIAC, the founding of Google) are included only when they correspond to a change in the commercial capability frontier, not for historical significance alone.

### 3.5 Source hierarchy

The dataset contains 414 source records. The source hierarchy for labor data is:

1. ILO ILOSTAT modelled estimates (primary for 1991–2025)
2. World Bank World Development Indicators (cross-check)
3. GGDC 10-Sector Database (historical disaggregation)
4. Bairoch (1988), Mitchell (2003), Cambridge Group (pre-1870 reconstructions)
5. Maddison Project Database (population and GDP only — not employment)

For replaceability scores, sources are primarily benchmark datasets (SWE-bench, METR, IFR robot density), commercial deployment data (company reports, earnings calls, industry databases), and academic research (Frey & Osborne, Eloundou et al., Gmyrek et al., Anthropic Economic Index).

---

## 4. Scenarios

Three capability trajectories model how fast the technical frontier advances. These are not labor market scenarios — they do not model policy responses, capital investment cycles, or social adaptation. They model only how quickly AI and robotics becomes technically capable of performing human work.

### 4.1 Conservative

AI capability growth continues but decelerates from 2025 rates. Benchmark improvement reverts toward 2019–2022 pace by 2027. Physical manipulation advances slowly. The frontier reaches human-level performance on most cognitive tasks by 2030.

In the displacement model, the conservative scenario applies no AI-driven workforce reduction. It represents the ILO consensus employment baseline — where employment would go if AI displacement did not occur. Employment grows slowly, driven by population growth and structural economic change.

### 4.2 Moderate

The METR 4-month capability doubling rate continues through 2028, then stabilizes. Frontier AI reaches human-level performance on most cognitive tasks by 2027–2028. Commercially available robotics crosses dexterity thresholds for most structured physical environments by 2029–2030.

This is the display scenario. The visualization shows the moderate projection only.

### 4.3 Accelerated

Capability improvement accelerates beyond 2025 levels. Frontier AI reaches AGI-adjacent performance by 2027. Commercially available robotics crosses thresholds for unstructured physical environments by 2028. By 2030, the only remaining technical frontiers are direct physical contact with humans and genuinely novel creative output.

---

## 5. The displacement model

The displacement model converts replaceability scores into projected employment changes. It answers: given that AI can technically do X, how many jobs actually disappear?

### 5.1 The formula

For each territory T, year Y, and scenario S:

```
total_reduction = delta_repl_term + lag_term

delta_repl_term = conv_rate(S) × max(0, repl(T, Y, S) − repl_2026(T)) / 100

lag_term = lag_release(S, Y) × pending(T) / 100

pending(T) = repl_2026(T) × 0.85

workers(T, Y, S) = consensus_workers(T, Y) × (1 − total_reduction)
```

Where:
- `repl(T, Y, S)` is the replaceability score for territory T at year Y under scenario S
- `repl_2026(T)` is the locked 2026 baseline score (no scenario)
- `consensus_workers(T, Y)` is the conservative (ILO consensus) workforce projection
- `conv_rate(S)` is the scenario-specific conversion rate
- `lag_release(S, Y)` is the scenario-specific lag absorption at year Y
- `pending(T)` is the backlog of existing capability not yet absorbed (85% of the 2026 score)

### 5.2 What the two terms mean

**The delta replaceability term** captures new capability arriving after 2026. Each new point of replaceability is converted into displacement at the scenario's conversion rate. If Money & Data goes from 78 (2026) to 94 (2030 moderate), that is 16 new points. One-third of 16 is approximately 5.3 — meaning about 5.3% of that territory's workforce is displaced by post-2026 capability gains.

**The lag term** captures the backlog. In 2026, a substantial amount of technical capability already exists that has not yet been absorbed into actual job losses. Radiology AI works, but radiologists still have jobs. The lag term says: this backlog gets absorbed over time, on a schedule. The 0.85 multiplier means 85% of the 2026 score is treated as pending absorption — the remaining 15% is assumed to have already been absorbed into the pre-2026 employment baseline.

### 5.3 Parameters

**Conversion rates** (what fraction of each new replaceability point becomes an actual job loss):

| Scenario | Rate |
|---|---|
| Conservative | No displacement applied. The conservative scenario is the ILO consensus baseline — it represents where employment would go if AI displacement did not occur. The displacement formula is not run on this scenario. |
| Moderate | 1/3 (0.333). One-third of new capability becomes displacement. |
| Accelerated | 0.60. Three-fifths of new capability becomes displacement. |

**Lag release schedule** (what fraction of the 2026 capability backlog has been absorbed by each year). These values apply to the moderate and accelerated scenarios only. The conservative scenario does not use the displacement formula.

| Year | Moderate | Accelerated |
|---|---|---|
| 2026 | 5% | 12% |
| 2030 | 28% | 55% |
| 2035 | 48% | 75% |
| 2040 | 58% | 85% |
| 2041 | 60% | 87% |

The lag schedule decelerates: the gaps between anchor points are +23pp (2026–2030), +20pp (2030–2035), +10pp (2035–2040), +2pp (2040–2041) for the moderate scenario. This reflects the assumption that the easiest-to-displace roles are absorbed first, and the remaining backlog becomes progressively harder to convert into actual displacement.

### 5.4 Headline outputs

| Year | Conservative | Moderate | Accelerated |
|---|---|---|---|
| 2026 | 3,551M | 3,417M | 3,151M |
| 2030 | 3,606M | 2,946M | 2,134M |
| 2035 | 3,700M | 2,580M | 1,692M |
| 2040 | 3,800M | 2,427M | 1,470M |
| 2041 | 3,820M | 2,395M | 1,426M |

The moderate scenario shows a 30% workforce decline from 2026 to 2041.

### 5.5 What the model does not do

**No reinstatement effects.** The model does not create new jobs in response to AI-driven productivity gains. Workers displaced by the displacement formula exit the employed workforce and are not redistributed. This is a deliberate editorial choice reflecting the project's assessment that the ceiling on human AI-supervisor roles is structurally low, mass reskilling has no historical precedent at the speed required, and the project's purpose is to show the full scale of displacement pressure before institutional responses are considered.

**No within-territory redistribution.** Workers displaced from one territory are not moved to another. Each territory's displacement is computed independently.

**No policy modeling.** Regulatory responses, UBI, retraining programs, and changes to labor law are not modeled. These are the subject of the political conversation the project aims to provoke, not inputs to the model.

### 5.6 Sensitivity

The lag release schedule is the single most consequential free parameter in the model. Small changes produce large changes in output:

- Moderate lag at 2040 = 58% → total workforce 2,427M (29% decline from conservative)
- Moderate lag at 2040 = 30% → total workforce approximately 2,760M (18% decline)
- Moderate lag at 2040 = 80% → total workforce approximately 2,120M (38% decline)

The conversion rate is the second most sensitive parameter. Changing moderate from 1/3 to 1/4 reduces the 2040 decline by approximately 3–4 percentage points.

The lag schedule is modeled, not empirically measured. It reflects the project's assessment of institutional absorption speed based on historical technology adoption patterns. It is not a prediction. Alternative schedules would produce materially different projections.

---

## 6. The production pipeline

The dataset was produced through an 8-phase pipeline using multiple AI model instances in an adversarial research-and-reconciliation architecture. Each phase used two independent research models (typically one Claude instance and one Gemini instance) that produced outputs without seeing each other's work. A third model instance served as editor/reconciler, adjudicating disagreements based on evidence quality and methodology compliance. All phases were subsequently validated by Claude (Opus 4.6), which served as the final editorial layer — checking internal consistency, cross-scenario ordering, monotonicity, formula correctness, and evidence grounding. Manual review by the project lead covered structural decisions, editorial judgment, and spot-checking of individual records, but did not independently verify every source citation.

### 6.1 Phases

| Phase | Content | Research models | Reconciler | Final editor |
|---|---|---|---|---|
| 1 | Historical labor shares 1800–2024 | Claude + Gemini | GPT | Claude (Opus 4.6) |
| 2 | Labor projections 2025–2040 | Gemini + GPT | Claude | Claude (Opus 4.6) |
| 3 | Territory replaceability 2015–2026 | Claude + GPT | Gemini | Claude (Opus 4.6) |
| 4A/B | Occupation replaceability (405 occupations) | Claude + GPT | Gemini | Claude (Opus 4.6) |
| 5 | Replaceability projections 2027–2040 | Claude + Gemini | GPT | Claude (Opus 4.6) |
| 6 | Technology events timeline | Claude + Gemini | GPT | Claude (Opus 4.6) |
| 7 | Manual integration + source deduplication | — | — | Manual + Claude (Opus 4.6) |
| 8 | Final validation | — | — | Automated + manual |

Automated validation checks: monotonicity (all territory-scenario trajectories non-decreasing), cross-scenario ordering (accelerated ≥ moderate ≥ conservative at every anchor year), labor share summation (100% at every anchor year), and displacement formula consistency. Manual validation caught errors that automated checks cannot — most notably a phantom parameter value (conservative conversion rate listed as 0.30 but never applied) that persisted through multiple automated validation passes.

### 6.2 How reconciliation worked

When the two research models agreed within 5 points, the reconciler typically accepted the average or the more specifically benchmarked value. When they disagreed by 6–10 points, the reconciler chose the model with stronger benchmark evidence. When they disagreed by more than 10 points, the reconciler averaged but flagged the record for manual review.

The largest single disagreement in the dataset was Land & Sea at 2030 moderate: Claude scored 71, Gemini scored 44. The reconciled value is 58 (midpoint). This 27-point gap reflects genuine uncertainty about agricultural robotics timelines and is the widest in the entire dataset.

Cognitive territories showed tight agreement (1–5 points) across all years. Physical territories showed systematic disagreement (16–27 points) at 2030, narrowing to 7–12 points by 2040. The disagreement is concentrated on one question: how fast will humanoid robots cross commercial availability thresholds for physical labor? As of Q1 2026, the evidence favors the more conservative projections — Unitree has shipped approximately 15,000 units globally, primarily as research platforms, and Tesla Optimus remains in the R&D phase.

### 6.3 Post-production revisions (v2.2)

Following the initial reconciliation, a targeted evidence review in March 2026 revised two territories:

**Building Things (moderate):** 2028–2032 scores lowered by 1–3 points. Basis: MEP trades (plumbing, electrical, HVAC) represent 30–40% of construction labor and have zero commercially available robotic solutions. The Zacua/Hilti 2026 Construction Robotics Report places construction robotics spend at less than 0.03% of global construction expenditure.

**Feeding & Hosting (moderate):** 2027–2032 scores lowered by 5–8 points. Basis: The leading kitchen automation robot (Flippy) has approximately 14 active commercial installations. The leading validated success (Sweetgreen Infinite Kitchen) operates at 12 locations and still requires roughly half the normal staff. No general cooking robot, hotel room-cleaning robot, or humanoid hospitality worker is commercially deployed anywhere.

---

## 7. 2026 replaceability baselines

These are the locked baseline scores from which all projections depart. Each score is briefly justified below.

| Territory | 2026 Score | Justification |
|---|---|---|
| Making Things | 86 | Xiaomi zero-worker factory (81K sqm, 24/7); China 470 robots per 10K manufacturing workers. High-capital frontier is essentially fully automatable. Global average lower due to legacy equipment. |
| Money & Data | 78 | Frontier AI performs most financial analysis, document processing, compliance review, and data management at professional level. Complex multi-party judgment and novel legal structures remain. |
| Thinking & Leading | 72 | SWE-bench 71.7% (2024); AI writes 30–50% of code at frontier companies. Professional services (consulting, management, legal research) substantially automatable. Senior architecture and novel system design remain. |
| Making Meaning | 72 | Generative AI produces professional-quality text, image, video, and music. Commercial deployment in advertising, content production, design. Genuinely novel creative output and aesthetic judgment remain. |
| Care & Health | 62 | 873 FDA-cleared AI radiology tools. AI matches human diagnostic accuracy on many imaging tasks. Telehealth AI operational. Fine physical manipulation, novel diagnosis, and therapeutic relationship remain. |
| Buying & Selling | 62 | E-commerce AI, automated customer service, inventory optimization, dynamic pricing all commercially deployed. Complex negotiation and relationship sales remain. |
| Moving Things | 52 | Waymo commercial robotaxi in multiple cities. Amazon 1M+ warehouse robots. Autonomous trucking in pilot. Last-mile in unstructured environments and adverse conditions remain. |
| Land & Sea | 48 | GPS auto-steer, drone spraying, autonomous grain harvesting commercially deployed. Precision weeding lasers operational. Fruit harvesting in early commercial. Unstructured terrain, biological variability, and the global South's minimal mechanization anchor the score. |
| Building Things | 46 | Construction drones (45–67% contractor adoption), rebar robots, 3D concrete printing scaling. MEP trades (plumbing, electrical, HVAC) at zero robotic automation. Unstructured environments, multi-trade coordination unsolved. |
| Governing & Protecting | 41 | AI surveillance, predictive policing, document automation in government. Military autonomous systems in deployment. Democratic accountability, judgment in novel situations, and physical enforcement remain deeply human. |
| Feeding & Hosting | 34 | Digital ordering/payment mature. Restaurant delivery robots (160K+ units globally). Basic food assembly automation (Sweetgreen). No general cooking, room-cleaning, or complex hospitality service robots deployed. |
| Maintaining & Fixing | 32 | Industrial inspection platforms (Boston Dynamics Spot, pipe crawlers, utility drones) commercially deployed. SCADA/IoT for process monitoring. Zero commercial robotic solutions for physical repair (HVAC, plumbing, electrical). |
| Learning & Teaching | 18 | AI tutoring systems (Khan Academy + GPT-4) operational. Automated grading for structured assessments. Embodied presence, real-time social adaptation, and the developmental relationship remain far from any technical solution. |

---

## 8. Timeline and endpoint rationale

### 8.1 Start: 1800

1800 is not the start of industrialization — the Industrial Revolution began in Britain decades earlier, and manufacturing overtook agriculture in England around 1740 (Cambridge Group). 1800 is the earliest date at which a defensible estimate of global labor distribution can be constructed from the available historical sources (Bairoch 1988). The pre-1850 data is LOW quality and covers only three macro sectors. It exists in the visualization to provide the "before" baseline that the project's argument depends on: a world in which the overwhelming majority of human labor was agricultural.

### 8.2 Baseline: 2026

2026 is the present year. Replaceability scores at 2026 are anchored to commercially available technology as of Q1 2026. All projections depart from this baseline. The 2026 scores are locked and not subject to scenario variation.

### 8.3 End: 2041

2041 = 2026 + 15 years. Fifteen years represents the outer boundary at which the model's core assumptions — capability trajectories, lag absorption rates, and structural economic parameters — can be reasonably grounded in observable evidence and historical analogues. Beyond this horizon, the compounding uncertainty in all parameters would make the model's outputs indistinguishable from speculation.

The date 1800–2041 is also an aesthetic choice. A timeline ending at a round number (2040) reads as arbitrary. 2041 reads as deliberate — a signal that the endpoint was chosen, not defaulted to.

### 8.4 Known boundary artifacts

The 2025–2026 boundary is a methodological seam where backward-calibrated historical data meets forward-calibrated projections. Some territories show apparent plateaus at this boundary (e.g., Land & Sea holding at 48 for both 2025 and 2026). These are artifacts of the calibration methodology, not genuine capability stalls.

---

## 9. Known limitations

### 9.1 The conservative baseline has drifted from ILO consensus

The dataset's conservative scenario uses the November 2024 vintage of ILO modelled estimates. The ILO's November 2025 vintage (published January 2026 in Employment and Social Trends 2026) places 2025 global employment approximately 49 million higher. The conservative baseline is therefore slightly below current ILO consensus. The percentage-based displacement calculations are minimally affected, but absolute workforce numbers in all scenarios are correspondingly low by approximately 1.4%.

### 9.2 Pre-1870 data is editorial

The 12 records covering 1800–1870 are reconstructions from secondary historical sources, not observed labor statistics. They provide directional shape (agriculture declining, industry rising) but should not be treated as precise measurements.

### 9.3 The 2019–2020 replaceability discontinuity

Care & Health and Money & Data both show +16 point jumps from 2019 to 2020 — the largest single-year movements in the dataset. These reflect the simultaneous arrival of GPT-3 (the first commercially available general-purpose language model, June 2020) and pandemic-driven acceleration of digital health and financial services. The jumps are annotated in the dataset but represent a calibration choice that reasonable analysts might score differently.

### 9.4 Physical territory projection uncertainty

The five physical-labor territories (Land & Sea, Building Things, Moving Things, Feeding & Hosting, Maintaining & Fixing) carry wider uncertainty bands than cognitive territories. The two independent research models agreed within 1–5 points on cognitive territories at 2030 but disagreed by 16–27 points on physical territories. The central question — how fast will humanoid robots cross from research platforms to productive commercial tools — remains genuinely unresolved as of Q1 2026.

### 9.5 Occupation scores lack independent verification

The 405 occupation-level scores are derived from a combination of benchmark research and AI training knowledge. Many carry a "MEDIUM — Derived from training knowledge" basis. These scores have not been independently validated by domain experts in each occupation. They are provided as indicative estimates, not as peer-reviewed assessments.

### 9.6 No reinstatement or redistribution

The displacement model models job loss only, not job creation. This is its most challengeable assumption. Every economist will ask where the reinstatement effect is. The answer is: it is deliberately excluded. See Section 5.5 for the rationale. Readers should understand that actual employment outcomes depend on policy responses and economic restructuring that this model does not attempt to predict.

---

## 10. How to contribute

This is an open-source project. Contributions are welcome. Here is what a good contribution looks like.

### 10.1 Correcting a score

Point at a specific record: territory, year, scenario. State the current score. Provide the evidence that the score is wrong — a commercially available product that raises it, or the absence of a commercially available product that should lower it. Propose a replacement score with justification.

The standard is: can you explain this number? If you can explain why the current number is wrong and your replacement is right, referencing specific commercial evidence, that is a valid correction.

### 10.2 Extending the occupation layer

The occupation layer covers 405 ISCO-08 4-digit occupations. There are approximately 430 total. Adding missing occupations follows the same scoring methodology: assign a territory, assess the 2026 replaceability based on commercially available technology, and project 2030 scores under the three scenarios.

### 10.3 Adding a territory

The current 13-territory grouping is editorial. If you have evidence that a subdivision would be more accurate — for example, splitting Land & Sea into agriculture and mining, which have very different automation trajectories — the contribution would include the proposed ISIC mapping, the historical labor share data for both new territories, and replaceability scores from 2015 forward.

### 10.4 Challenging the displacement model

The displacement model's parameters (conversion rates, lag schedule) are the most consequential assumptions in the project. If you have evidence that the lag schedule is too fast or too slow — for example, sector-specific data on technology adoption rates that suggests a different absorption curve — that evidence would directly improve the model. The sensitivity analysis in Section 5.6 shows how much the outputs change with different parameter values.

### 10.5 What format

Corrections and extensions should reference the dataset's native structure: territory_id, year, scenario, replaceability_score, source_ids. The canonical dataset is a JSON file. Territory groupings are a separate editorial layer over native ISIC/ISCO classification keys.

---

## 11. Changelog

### v2.2 (March 2026)

- Timeline extended from 2040 to 2041 (78 new records: 39 replaceability + 39 labor)
- Feeding & Hosting moderate 2027–2032: scores lowered by 5–8 points (evidence review)
- Feeding & Hosting conservative 2027–2029: adjusted to maintain cross-scenario ordering
- Building Things moderate 2028–2032: scores lowered by 1–3 points (evidence review)
- Technology event "Tesla Optimus Gen 3 Begins Mass Production" revised to reflect Q1 2026 evidence (pilot production, not mass production)
- Technology events reduced from 96 to 57 (duplicates, product-catalog entries, and culturally famous but labor-irrelevant milestones removed)
- Pre-1870 source attribution corrected from Maddison to Bairoch/Mitchell/Cambridge Group
- Care & Health and Money & Data 2020 replaceability jumps annotated
- ILO Employment and Social Trends 2026 added as source
- Lag schedule and conversion rate documentation corrected to match implemented values

### v2.1 (February 2026)

- Initial public dataset
- 496 replaceability records, 387 labor records, 405 occupations, 96 technology events, 410 sources
- Three scenarios (conservative, moderate, accelerated)
- Timeline: 1800–2040

---

## 12. Citation

If referencing this dataset or methodology:

Large Labor Model, v2.2. Dataset and methodology. March 2026. largelabormodel.com.

The project is open source. The dataset, this methodology, and the visualization code are available for reuse, adaptation, and critique under the terms specified at the project website.
