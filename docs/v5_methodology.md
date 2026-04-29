# Large Labor Model v5.0 — Methodology

**Version:** 5.0
**Published:** 2026-04-19 (updated 2026-04-20)
**Horizon:** 1970 → 2041 (historical backfill + forward projection)

---

## Overview

Large Labor Model v5 is a structured estimate of how AI and robotics capability translates into labor replaceability and workforce replacement across 480 occupations, 13 modern territories, and 3 historical macro groupings. It covers the 2026 → 2041 horizon — fifteen years from its reference date — and presents three scenarios (conservative, moderate, accelerated) for every occupation.

The model answers two questions that the build pipeline keeps strictly separate:

1. **Replaceability.** If you tried to swap this occupation to an autonomous AI or robotics system today, would it work? This is a task-by-task capability comparison: what fraction of the occupation's weighted task profile can a deployed system handle with production reliability?
2. **Replacement.** How fast does that replaceability translate into actual workforce displacement? This is a dynamic question about adoption lag, regulatory gates, preference inertia, capital cycles, and institutional drag.

Separating these two questions was the load-bearing editorial decision of v5 and is the first thing a reader should know. A high replaceability score does not mean imminent displacement; a low displacement curve does not mean capability has not arrived.

The model is explicitly a structured reasoning exercise, not a prediction. Every number ships with an audit trail to specific benchmarks, historical cases, and sourced decisions — but the numbers are deliberately coarse because the underlying physical and economic systems are coarse. The honest output is a map of where capability sits today, where it is plausibly headed by 2041, and how fast that translates into workforce change.

---

## Replaceability ≠ Replacement — the load-bearing distinction

This distinction was refined repeatedly over the v5 build and corrected in a Phase 11 review that caught a framing slip. The clean framing is:

**Replaceability = tech capability × economic viability × commercial availability.** A high score means:
- the technology exists and works on the occupation's tasks,
- the unit economics are plausible (a humanoid at $30/hour against a gig worker at $15/hour will fail this test), and
- a product or service is commercially available to deploy.

Replaceability says nothing about whether regulation permits it, whether customers will accept it, or how fast adoption happens.

**Replacement = adoption-lag frictions.** Given a replaceability score (what works today), how fast does actual workforce displacement track it? Regulatory gates, preference inertia, capital cycles, named-human statutory mandates, malpractice liability, and institutional drag all live here.

### Canonical examples

- **Lawyers (2611) in 2041.** Replaceability is high: the cognitive capability is saturating, and legal-tech products exist and work. Displacement is much lower because bar licensing, courtroom mandates, malpractice liability, and client preference keep a meaningful share of work with licensed humans. The honest read is "capability arrived; replacement hasn't."
- **Robo-baristas.** Replaceability is high (they work when deployed; novelty even drives traffic). Replacement is low (almost no cafés have them). The Phase 6 curve models the catch-up as hardware cost falls, acceptance grows, and ordering-screen precedent (McDonald's) compounds.
- **Gig-delivery humanoids in 2026.** Replaceability is *low* — a humanoid at $30/hour doesn't work against a gig rider at $15/hour. The unit economics break the swap. This is not a regulatory or preference gate; it's an economics gate, and it correctly lives on the replaceability side.

### What lives where (v5 rule)

Replaceability-side discounts (count against r26):
- **Capability gap** — the AI/robotics system literally cannot perform the tasks.
- **Economic viability** — unit economics break the business.
- **Commercial availability** — no product or service to buy for this task.

Replacement-side drags (Phase 6 lag multipliers, not Phase 5 scores):
- **Regulatory** — licensing, statute, malpractice, named-human mandates.
- **Human preference** — customer rejection of AI substitute even when tech and economics allow.

Phase 11 corrected a looser framing that had bundled regulatory and preference into replaceability via a coarse "would swap today work?" test. Under the corrected framing, 162 occupations carrying REGULATORY or HUMAN_PREFERENCE barriers had their Phase 5 r26 scores re-computed to pure task-math; the Phase 6 HUMAN_PREFERENCE and REGULATORY multipliers were strengthened proportionally (0.70 → 0.562 and 0.50 → 0.405) so that the replacement projections stayed aligned with the Anthropic Economic Index empirical anchor.

---

## The 6 capability vectors

Every task carries one of six capability vectors. Each vector has a 2026 reference value (the fraction of that vector's tasks that deployed systems can reliably handle today) and a difficulty threshold per task (the minimum vector value at which a system could perform that task). A task is counted replaceable when `capability[task.vector] ≥ task.difficulty_threshold`. Occupation-level replaceability is the time-weighted share of tasks whose vector × difficulty threshold is crossed.

### Vector definitions and 2026 values

| Vector | Full name | 2026 value | Benchmark anchoring |
|:---|:---|---:|:---|
| **C_R** | Routine Cognitive | **0.76** | Codifiable, rule-based cognitive work: documentation, form processing, first-pass coding, routine customer-service drafts, routine medical coding. Anchored to SWE-bench Pro (decontaminated, 0.52), Anthropic Economic Index observed coverage (~75% for top NONE-barrier roles like programmers, customer service, bookkeepers), and enterprise back-office adoption. Held below 0.80 because 10–15% confident-failure rates cap unsupervised labor substitution. |
| **C_G** | Generative Cognitive | **0.57** | Open-ended professional judgment and creation: specialist analysis, strategy, diagnosis, senior advising, novel design. Benchmarks span GPQA Diamond (0.94 on specialist QA) through HLE (0.45) and ARC-AGI-3 (0.004, on frontier novel reasoning). Production pattern in legal, consulting, medical is augmentation, not replacement. |
| **P_A** | Physical Automation | **0.75** | Structured, repeatable industrial automation in engineered environments. Anchored to IFR World Robotics 2025 (542,000 new installations in 2024; 4.66M operational robots globally). Frontier density (Korea ~1,220 robots/10K workers) does not represent the global workforce (China 166, Western Europe 267, North America 204). |
| **Phi_S** | Selective Physical | **0.46** | Sensor-based, route-based, or structured physical operation in selected operational design domains. Anchored to Waymo (~500K weekly rides in 5 metros), Aurora/Kodiak (specific highway corridors), Amazon Vulcan (~75% item coverage with human tag-in), Tesla FSD (supervised). Remote-operator backstops and narrow ODDs preclude unsupervised replacement for the median Phi_S worker. |
| **Phi_U** | Unstructured Physical | **0.15** | Embodied physical work in unstructured real-world environments: plumbing in customer homes, surgery, hair styling, home care, firefighting, rescue, variable-terrain farm work, craft by hand, live performance (singing, dancing, acting). Anchored to the absence of scaled commercial deployment. Surgical robots remain surgeon-directed; home-care humanoids are not at scale; emergency environments are far outside production reliability. |
| **S_E** | System Engineering | **0.35** | Socio-technical orchestration of multi-stakeholder systems: enterprise architecture, incident command, air traffic control, platform operations, cross-organizational coordination. Anchored to METR time-horizon benchmarks (rapid progress but clean-task bias), Devin/Composer production completion (~50% vs GAIA 0.75), ARC-AGI-3 (0.004 on novel interactive systems). No multi-stakeholder autonomous deployment exists in 2026. |

### Post-recalibration context

The six 2026 values above are the Phase 11 post-recalibration set. Phase 5's original blind calibration produced higher 2026 values (C_R 0.87, C_G 0.62, P_A 0.78, Phi_S 0.60, Phi_U 0.15, S_E 0.42) on the basis of benchmark saturation. Phase 11's recalibration ran two independent instances — Claude Opus 4.7 and GPT 5.4 — each under the same brief: re-interpret each benchmark citation as a production-reliability number, discounting for remote-operator backstops, confident-failure rates, narrow operational-design domains, and agentic brittleness. Both instances converged within ±0.03 on every vector. The shipping set takes the blended midpoint. Ordering is preserved across the recalibration: C_R > P_A > C_G > Phi_S > S_E > Phi_U.

Phi_U is defended unchanged at 0.15 because it was already at the conservative floor in Phase 5, and no 2026 deployment evidence moves it. The largest correction is Phi_S (−0.14) — this is the vector where benchmark and demonstration evidence most over-states production capability under honest-deployment accounting.

### 2041 anchors under the moderate scenario

The Phase 7 capability trajectories (mid-band anchors used for projection, after the Phase 11 parallel shift that propagated the recalibrated 2026 values through the trajectory) are: C_R 0.87, C_G 0.86, P_A 0.92, Phi_S 0.76, Phi_U 0.66, S_E 0.78. These are the year-2041 values under the moderate scenario in `metadata.capability_trajectories_summary`. Phi_U carries the widest bands across scenarios (2041 low 0.29, 2041 high 0.995), reflecting honest humanoid-deployment uncertainty. The original pre-shift Phase 7 mid values (C_R 0.98, C_G 0.91, P_A 0.95, Phi_S 0.90, S_E 0.85) are retained in the trajectory file under `*_phase7_original` fields for traceability.

---

## Three-scenario framework

Every occupation carries low / mid / high bands for the 2026 score and for each 2030 / 2035 / 2040 / 2041 anchor:

- **Low (conservative).** Slower capability trajectory, stronger barrier drag, tempered task-math.
- **Mid (moderate) — the default displayed view.** Computed as `min(A_mid, B_mid)` across two independent Phase 7 forecasters, then parallel-shifted by the Phase 11 recalibration delta so that the 2026 anchor matches the recalibrated starting value. 2041 mid anchors (post-shift): C_R 0.87, C_G 0.86, P_A 0.92, Phi_S 0.76, Phi_U 0.66, S_E 0.78.
- **High (accelerated).** Faster capability, weaker barriers, aggressive task-math. Anchored on the more aggressive forecaster's mid reading (also post-shift). 2041 high anchors: C_R 0.91, C_G 0.95, P_A 1.00, Phi_S 0.88, Phi_U 0.995, S_E 0.93.

The three-scenario discipline was established at Checkpoint 7 after an early reconciler averaged `A_mid + B_mid`, contaminating the mid band with whichever forecaster happened to be more aggressive. The `min` rule for mid is the reconciliation contract: mid is the *tempered* read, not the average. Scenario preference never leaks into the central case.

Occupation-level bands are computed deterministically. Each task's vector × difficulty threshold is compared against the scenario's capability-vector value for that year; the time-weighted share of crossed thresholds is the replaceability score for that scenario/year.

---

## Replacement formula

v5 uses a single structured formula to convert replaceability into displacement over time:

```
displacement(t) = (conversion_rate × (replaceability_t − replaceability_2026)
                   + lag(t) × pending)
                 × barrier_multiplier
```

where `pending = replaceability_2026 × (1 − already_absorbed_era)`.

Parameters:

- **`conversion_rate = 0.30`** (bounds 0.22–0.38). The fraction of replaceable capability that actually converts to displacement in a mature-lag regime. v3.2 used 0.333; v5 tightened slightly based on historical-case fit.
- **`lag(t)`** is a piecewise schedule: 7% in 2026, 18% in 2030, 30% in 2035, 42% in 2040, 44% in 2041. v3.2's schedule was materially faster (5 / 28 / 48 / 58 / 60 %). v5's schedule is the honest read after fitting seven historical automation cases (telephone operators 1920–2023, bank tellers, travel agents, cashiers, translators, customer service reps, bookkeeping clerks).
- **`barrier_multiplier`** stratifies displacement by barrier type:
  - NONE: 1.20 × — no barrier; adoption is slightly faster than baseline.
  - ECONOMIC: 1.00 × — baseline.
  - HUMAN_PREFERENCE: 0.562 × — customers resist even when tech and economics allow.
  - REGULATORY: 0.405 × — licensing and statute keep the gap open.
  - HUMANOID_DEPENDENT: 0.15 × — humanoid readiness is the rate limit.

  The HUMAN_PREFERENCE and REGULATORY multipliers were strengthened from Phase 6's original values (0.70 and 0.50) during Phase 11 to preserve empirical fit against the Anthropic Economic Index cross-section after Phase 5 r26 scores were rescored to pure task-math. Barrier-type stratification was validated empirically: cross-section R² rises from 0.61 (plain conversion × lag) to 0.85+ when barrier type is a categorical predictor.

- **`already_absorbed_era`** stratifies by capability-era tag:
  - Pre-2015 (ATMs, online booking, ERP, calculators): 0.30 — 20+ years of diffusion already priced in.
  - 2015–2022 (neural machine translation, early chatbots, RPA): 0.15.
  - Post-2022 LLM-native: 0.05 — ~3 years of diffusion is still early.

  v3.2 used a uniform 0.15. Historical cases (telephone operators at Δt = 93 years reaching 0.99 absorbed; bank tellers at Δt = 39 years reaching ~0.50) falsify the uniform assumption; v5 stratifies explicitly.

Parameters were fit against the 7 historical cases and the 28-occupation cross-section from the Anthropic Economic Index (Massenkoff & McCrory, March 2026). Historical-case R² under the fitted formula is 0.85+; plain (no-barrier, uniform-absorbed) R² is 0.61.

---

## Barrier taxonomy

The `primary_barrier` enum has five values. Under the corrected Replaceability ≠ Replacement framing:

| Barrier | Side | Meaning | Count (v5) |
|:---|:---|:---|---:|
| **NONE** | — | No structural barrier. Only diffusion time. | 42 |
| **ECONOMIC** | **Replaceability-side** | Unit economics break the swap today. Affects r26 directly. | 154 |
| **HUMANOID_DEPENDENT** | **Replaceability-side** | Product or service not commercially available for the physical task (humanoid hardware gap). Affects r26 directly via Phi_U capability. | 123 |
| **HUMAN_PREFERENCE** | **Replacement-side** | Customers reject the AI substitute even when tech and economics allow. Lag multiplier 0.562 ×. | 93 |
| **REGULATORY** | **Replacement-side** | Licensing, statute, named-human mandates, malpractice liability. Lag multiplier 0.405 ×. | 69 |

Occupations may carry multiple `barrier_types` in the secondary enum; `primary_barrier` captures the dominant constraint.

The v3.2 → v5 distribution shifted substantially (HUMAN_PREFERENCE 170 → 93; ECONOMIC 65 → 154; NONE 2 → 42). Many v3.2 HUMAN_PREFERENCE defaults were really ECONOMIC (unit-economics failures), and many NONE cases that v3.2 buried under preference are now explicit. This was a consequence of tighter Phase 5 / Phase 11 editorial definitions, not a scoring artifact.

---

## Horizon rationale

The terminal year is **2041** (= 2026 + 15). Fifteen years out is far enough for capability curves to bend and for adoption lag to compound, but close enough that 2026 benchmark and deployment anchors still constrain the projection meaningfully. v3.2 used 2040 as a terminal year; v5 shifts to 2041 to preserve the clean "+ 15 from reference date" convention.

All projection anchors (2030, 2035, 2040, 2041) come with low/mid/high bands. 2041 is the primary horizon anchor; 2040 is retained for continuity with v3.2 readers and because many third-party comparisons use a 2040 target date.

The lower bound of the territory-level replaceability series is **1970** following the Phase 12 historical backfill (see next section). Before 1970, the dataset carries sector-level labor composition (via `historical_occupations` macro groupings) but not capability-vector-derived territory replaceability scores. Pre-1970 capability evidence is too thin (industrial robot density pre-1993 is estimated, not measured; digital-computing business deployment is a mostly-qualitative narrative) to support per-territory numbers with the same discipline as 1970+.

---

## Historical backfill (Phase 12, 1970 → 2014)

v5.0 ships a full 1970–2014 capability-vector trajectory and derived territory replaceability records. The trajectory was produced by two parallel honest-deployment research instances (GPT-5.4 + Claude Opus 4.7), each researching 15–25 milestone years with URL-cited anchors and producing low/mid/high values per vector per year. The two outputs were reconciled under the same discipline as Phase 7: `mid = min(A_mid, B_mid)`, `low = min(A_low, B_low)`, `high = max(A_high, B_high)` capped at 0.85 pre-2015, monotonicity enforced going forward.

Milestone anchors include: first commercial ATMs (1967–1970), CNC + microprocessor commercialization (1972–1975), VisiCalc / Lotus 1-2-3 (1979–1983), ERP precursors (SAP R/3 1992), IFR industrial-robot data series (1993), commercial web (1995), Deep Blue (1997), Google Translate (2006), Kiva / Amazon Robotics acquisition (2012), Watson Jeopardy (2011), Kubernetes + RPA (2014), AlexNet (2012), Waymo commercial launch (Dec 2018), Transformer paper (2017), GPT-2/3/ChatGPT/GPT-4 (2019–2023), Amazon Sequoia/Proteus (2023), humanoid pilots (2024).

Key reconciled trajectory values (mid band):

| Year | C_R  | C_G  | P_A  | Phi_S | Phi_U | S_E  |
|------|------|------|------|-------|-------|------|
| 1970 | 0.07 | 0.005| 0.10 | 0.005 | 0.02  | 0.005|
| 1985 | 0.16 | 0.009| 0.25 | 0.02  | 0.02  | 0.011|
| 2000 | 0.36 | 0.02 | 0.42 | 0.05  | 0.03  | 0.05 |
| 2010 | 0.47 | 0.04 | 0.51 | 0.07  | 0.04  | 0.09 |
| 2020 | 0.59 | 0.08 | 0.65 | 0.21  | 0.06  | 0.18 |
| 2025 | 0.74 | 0.56 | 0.74 | 0.44  | 0.14  | 0.33 |
| 2026 | 0.76 | 0.57 | 0.75 | 0.46  | 0.15  | 0.35 |

The trajectory shows:
- C_R and P_A rise steadily across the whole period (ATM + spreadsheet + ERP + SaaS + RPA for C_R; industrial robot stock growth for P_A).
- Phi_S is near-zero until the Waymo commercial launch in late 2018.
- S_E is near-zero pre-2010, rises with cloud + orchestration, sharp late rise with agentic coding (2023+).
- C_G is near-zero for most of 1970–2020; the entire rise from ~0.05 to 0.57 happens between 2017 (Transformer paper) and 2026.
- Phi_U stays near zero throughout — humanoid hardware is still in pilots.

Ordering through the historical period (C_R ≥ P_A > Phi_S ≈ S_E > C_G > Phi_U) reverses in the 2020s as C_G overtakes S_E, then Phi_S, consistent with the LLM-transformer era shift.

**Crossover function.** Historical per-occupation replaceability is computed via logistic crossover — `1 / (1 + exp(-8 · (capability − difficulty)))` — rather than the strict threshold used for near-term projections. This gives partial credit as capability approaches task-difficulty thresholds, which is the right behaviour when capability is low (the strict-threshold model collapses to zero across most occupations at 1970's capability values, which would be false). The logistic form matches the emergent-automation intuition: POS systems gave real-if-partial cashier replaceability in 2005 even though the C_R capability was below full task thresholds.

**Territory aggregation.** For each year, territory replaceability is the employment-weighted mean of in-territory occupation replaceabilities, using current (2026) employment weights within territory. This is an editorial decision: we don't have occupation-level employment weights back to 1970 at the 481-occupation granularity (ILOSTAT began in 1991), and reconstructing historical occupation weights would be a separate research project. The current framing is: "what share of today's labor composition, within each territory, would have been technically replaceable at each historical year's capability values?"

**Comparison to v3.2.** Phase 12 backfill generally produces higher historical values than v3.2's (e.g., Buying & Selling 2014 at 47% vs v3.2's 7%; Making Things 2014 at 31% vs v3.2's 15%). The gap is driven by Phase 12 applying the same task-math discipline used for 2026+ scoring, whereas v3.2's historical scoring was more conservative by construction. Both can be defended; v5's numbers are more internally consistent with the model's own mechanics.

**Calibration caveat — replaceability vs. replacement.** The 1985 Money & Data value at 4.4% and 2010 Buying & Selling value at 41% are both "replaceability" numbers, not "what actually happened" numbers. Real 1985 back-office displacement and real 2010 retail cashier displacement were both smaller because barriers (cost, preference, regulation) bind. The model's core distinction applies retrospectively as well as prospectively.

---

## Data sources

Primary sources backing the v5 build:

- **ILO ISCO-08 (International Standard Classification of Occupations, 2008 revision).** Canonical occupation codes and definitions. ILO PDF (2009-07-09 final) + ILO CSV (hash-matched) + IHE FHIR CodeSystem cross-check. Source for all 436 unit groups + 10 approved v5 custom / split codes.
- **O*NET (US Department of Labor).** Task statements and common occupational titles via SOC → ISCO crosswalk. 15,575 raw tasks from Phase 4 Instance A.
- **BLS (Bureau of Labor Statistics)** — OES (Occupational Employment Statistics) and OOH (Occupational Outlook Handbook). 11,234 raw tasks from Phase 4 Instance B.
- **Live LinkedIn guest-search scrapes (2025–2026)** for current job-title nomenclature — Phase 8 common titles (2,968 titles).
- **ILOSTAT EMP_TEMP_SEX_OCU_NB family** for 1991–2025 occupation-level global employment. Phase 3 occupation-up methodology.
- **GGDC 10-Sector Database** for 1870–1990 sector-level historical reconstruction. Phase 3.
- **World Bank MS.MIL.TOTL.P1 (IISS Military Balance)** for 1988–2025 armed forces coverage. ILOSTAT modelled-global does not publish ISCO major group 0; the WB/IISS series closes the gap for Governing & Protecting.
- **Bairoch + Maddison reconstructions** for 1800–1869 macro aggregates.
- **Anthropic Economic Index (Massenkoff & McCrory, March 2026).** 28-occupation cross-section of theoretical-vs-observed AI coverage; primary Phase 6 calibration anchor and Phase 11 cross-check for the capability recalibration.
- **METR time-horizon benchmarks** for agentic task completion. Phase 5 / 11 calibration input.
- **IFR World Robotics 2025.** Installed industrial robot stock and density. Phase 5 / 11 P_A calibration.
- **Humanoid pilot data (Figure 02 at BMW, Tesla Optimus, Amazon Vulcan).** Phase 5 / 11 Phi_S + Phi_U calibration (used to bound upside, not drive central estimates).
- **Epoch AI, GPQA, HLE, SWE-bench Verified / Pro, ARC-AGI-3.** Benchmark landscape for the six capability vectors.

A full source registry is inlined in the dataset at `sources[]`. Each labor record, each occupation, and each task carries `source_ids[]` pointing to registry entries with `id`, `type`, `title`, `reliability`, `authority`, and `citation`.

---

## Known limitations

This is a structured estimate, not a forecast. The honest statement of what the model cannot do:

1. **Point estimates over heterogeneous distributions.** C_G spans first-draft copywriting to frontier diagnosis. Phi_S spans robotaxis to rural mail to heavy equipment. S_E spans coding agents to multi-stakeholder incident command. A single 2026 value per vector averages over this; the bounds carry some of the uncertainty but a v6 vector split is a likely improvement.

2. **Benchmark-vs-deployment gap.** Benchmarks measure frontier capability on clean tasks; deployment measures production reliability on messy real labor. Phase 11's recalibration was an explicit attempt to close this gap via an honest-deployment lens, but production reliability data for humanoid robotics, agentic systems, and autonomous vehicles is still developing and values may shift in v5.1/v6.

3. **High 2040-mid shape.** Under the moderate scenario, mean replaceability across 480 occupations reaches 84.6 at 2040 and 25% of occupations score ≥90. The logistic crossover (k=8) ceiling is asymptotic — no occupation hits exactly 100; the maximum is around 98. Most occupations sit in the 80–95 band by 2040, so the model still pushes interpretive weight onto the displacement column where the variance lives. The honest reader uses displacement (mean 24% in 2040-mid, range 9–47%) to understand workforce implications, not replaceability alone.

4. **Phase 6 barrier-model form.** Multiplicative barrier multipliers work across most of the distribution but produce counterintuitive results at high r26 × REGULATORY (lawyers at r41 = 100). A floor-adjusted barrier model for regulatory frictions is a likely v6 change; in v5.0, these cases sit in the editorial-overrides queue.

5. **Residual scrape artifacts in task decomposition.** Four Phase 11 audit rounds removed 825 artifacts in aggregate (Audit 1 461 removals; Audit 2 none structural; intervention E a dozen more; Audit 3 299). Residual contamination below the 2-model consensus bar likely exists. A v6 Phase 4 re-run with tightened anti-scrape guardrails is recommended.

6. **Phase 4 task-classification ceiling.** Three-way reconciliation (v2 context-bound + v3 adversarial + context-free) achieved 84.2% agreement. The remaining 15.8% (895 cases) represent genuine ambiguity; Phase 11's focused Audit 2 re-examined high-r26 physical occupations and Audit 3 re-examined every task in every territory, but exhaustive per-task human adjudication remains out of scope for a 10K-task automated classification.

7. **Global-weighted P_A is lower than the frontier.** Industrial-robot density in Korea (~1,220 per 10K workers) is 7× China's (166), 5× Western Europe's (267), and 6× North America's (204). P_A at 0.75 averages across the global workforce, not the frontier economy. A single global value trades off against locale-specific precision.

8. **HUMANOID_DEPENDENT capability gap is uncertain.** The 2041 Phi_U mid at 0.66 assumes humanoid hardware matures from 0.15 in 2026. Low-band (0.29) is the conservative honest read; high-band (0.99) is the aggressive deployment read. The central value encodes substantial forecaster uncertainty.

9. **Editorial overrides pending for v5.0.** Two evidence-backed concerns (ISCO 5245 Service Station Staff; REGULATORY-barrier occupations with r41 ≥ 95) are documented but not applied to v5.0. They are v5.1 / post-launch editorial work.

10. **Historical reconstructions are coarse.** 1800–1869 labor data relies on Bairoch/Maddison macro aggregates; 1870–1990 relies on GGDC 10-sector + data-driven ISIC → territory allocation. Only 1991+ is occupation-level ILOSTAT. Territory-level totals for pre-1991 years are honest but not precise.

11. **Low/high scenario bands are structural, not editorially reviewed.** v5.0 ships the moderate (mid) scenario as the reviewed display. Low and high band values are preserved per occupation for audit-trail purposes, but are produced deterministically from Phase 7's capability-trajectory low/high curves applied against Phase 4 task difficulties — they were not reviewed occupation-by-occupation. This produces editorially-implausible shapes in thin-margin cases (e.g., preschool educators' r30_high jumps from 8 to 100 when Phi_U high = 0.67 crosses Phi_U task thresholds of 0.55-0.60). Re-examination of the low/high bands is a v5.1 deliverable; for now, reader attention should stay on the moderate band. `metadata.scenarios_shipped` encodes this disclosure.

12. **Historical backfill uses current task decompositions and current within-territory employment weights.** Phase 12 produces honest historical capability values; it applies them against today's occupation task lists, weighted by today's in-territory employment shares. This gives "what share of today's labor would have been technically replaceable at that year's capability" — not "what share of 1985's actual labor force was technically replaceable by 1985 technology." Reconstructing historical occupation-level task compositions and employment weights at the 481-occupation granularity would require a separate research project (ILOSTAT's occupation series begins only in 1991). This is a known editorial caveat for the historical series, documented at `metadata.phase12_historical_backfill`.

13. **Pre-1970 has no territory replaceability series.** Capability evidence pre-1970 is too thin (industrial robot density pre-1993 is estimated, digital-computing business deployment is mostly-qualitative) to support per-territory numbers with the same discipline as 1970+. Pre-1970 shows labor composition via `historical_occupations` macro aggregates (land_sea / macro_industry / macro_services) but no territory-level replaceability scores. The UI renders historical composition in the period.

---

## Versioning and reproducibility

v5.0 is built by an 11-phase pipeline. Each phase has a canonical output, a reviewer-signed checkpoint, and archived inputs/outputs for audit:

- **Phase 0:** Schema lock + spec (`v5_schema.json`, Draft 2020-12).
- **Phase 1:** ISCO-08 canonical reference (436 unit groups + 10 approved custom codes).
- **Phase 2:** Occupation inventory + territory mapping (480 occupations locked).
- **Phase 3:** Labor data rebuild with occupation-up methodology (635 records, 1800–2025).
- **Phase 4:** Task decomposition (3-way reconciled).
- **Phase 5:** Replaceability 2026 scoring (blind calibrator + 3 scorers + reconciler).
- **Phase 6:** Replacement formula calibration (7 historical cases + 28-occupation cross-section).
- **Phase 7:** Capability trajectories 2026 → 2041 (2 forecasters + reconciler, three-scenario framing).
- **Phase 8:** Barrier notes + common titles (3-source merge + targeted anti-template rerun).
- **Phase 9:** Timeline events audit (researcher + verifier).
- **Phase 10:** Adversarial validation (isolated instance).
- **Phase 11:** Editorial sign-off + release, with emergency interventions documented in [v5_editorial_process.md](v5_editorial_process.md).
- **Phase 12:** Historical capability-vector backfill 1970 → 2014 (2 parallel honest-deployment research instances — GPT-5.4 + Claude Opus 4.7 — + programmatic reconciliation + era-weighted territory aggregation).
- **Phase 13:** Independent formula-coherence verification (Codex GPT-5.4). Reproduced every per-occupation and per-territory replaceability, displacement, and dispersion value from scratch against the documented logistic formula. Reached max_abs_diff = 0.0 across all fields after the 2025 → 2026 trajectory seam was harmonized and the r35 / r40 band fields were added. Caught the spec/implementation divergence that the earlier Phase 10 validator didn't check.

Every phase checkpoint signoff is preserved. A rollback path to v3.2 exists as the previous published version. Intermediate v5 artifacts (calibrator JSON, scorer outputs, reconciler outputs, validator reports) are preserved under `v5-build/phase{N}/` in the build repo.

The reproducibility story is: same schema + same inputs + same calibrator/scorer/reconciler briefs = a dataset reproducible within the scorer-model variance documented at each checkpoint. We do not claim bit-identical reproducibility across model versions; we claim process transparency and principled calibration.

---

## Editorial principles (load-bearing rules followed throughout)

The four principles baked into `metadata.editorial_principles`:

1. **Replaceability = "if swapped today, would it work?" — capability × commercial availability × barrier frictions.**
2. **Replacement = actual displacement with lag (Phase 6 formula).**
3. **Three scenarios: low = conservative, mid = moderate (displayed), high = accelerated.**
4. **Terminal year 2041 (= 2026 + 15).**

Additional operating rules that shaped the build but aren't encoded in the shipped metadata — the v3.2 firewall, defensibility over count targets, phase-by-phase prompt writing, adversarial multi-model pattern, and the "reasoned model, not biased model" rule — are documented in the editorial process record.

---

*For the full post-mortem of the v5 build journey, including the Phase 11 emergency interventions that materially reshaped the shipping dataset, see [v5_editorial_process.md](v5_editorial_process.md).*
