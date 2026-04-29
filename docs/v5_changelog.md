# Large Labor Model v5.0 — Changelog

**Released:** 2026-04-19 (Phase 12 historical backfill + late fixes applied 2026-04-20)
**Previous version:** v3.2

---

## Headline changes

- **Historical backfill 1970 → 2014 (Phase 12, added 2026-04-20).** v5.0 now ships 585 new `territory_replaceability` records covering 1970–2014, produced by a dedicated Phase 12 pipeline: two parallel honest-deployment research instances (GPT-5.4 + Claude Opus 4.7) reconstructed the 1970–2025 capability-vector trajectory with URL-cited milestone anchors; programmatic reconciliation applied honest-deployment discipline (`mid = min(A_mid, B_mid)`); per-occupation replaceability computed via logistic crossover against current task decompositions; employment-weighted per territory. Fixes a late-caught regression where the canvas displayed 0% replaceability for every territory before 2015.
- **Ground-up rebuild, not a patch.** Every scoring column in v5 was recomputed from a new Phase 4 task decomposition, a dual-recalibrated 2026 capability vector, and an empirically fit replacement formula. v3.2 served only as post-hoc sanity check; never staged as input to any v5 phase.
- **Canonical ISCO-08 codes for all 480 occupations.** v3.2 had inherited ~200 wrong ISCO codes and 89 fabricated codes from v3.0 (e.g., "Chief Executives" at 1111 — the real 1111 is Legislators; "Physicists and Astronomers" at 2112 — the real 2112 is Meteorologists). v5 re-anchors every entry to the ILO ISCO-08 hierarchy, with specialised splits (e.g., `2512-ml`, `2261-orthodontist`) using a documented parent + suffix convention.
- **Replaceability and Replacement are now cleanly separated.** Replaceability (the 2026 score) answers "if swapped to an autonomous system today, does it work? — tech × economics × availability." Replacement (the displacement curves) answers "how fast does that capability translate into actual workforce displacement?" Regulatory and human-preference frictions live in the Phase 6 replacement model, not in the replaceability score. The distinction was corrected in Phase 11 after a review-caught conflation (see §2.6b in the editorial process record).
- **Post-recalibration 2026 capability vectors.** After two independent Phase 11 recalibrators (Claude Opus 4.7 and GPT 5.4) applied a benchmark-to-deployment honest lens, 2026 capability values were lowered: **C_R 0.87 → 0.76, C_G 0.62 → 0.57, P_A 0.78 → 0.75, Phi_S 0.60 → 0.46, Phi_U 0.15 (held), S_E 0.42 → 0.35**. Ordering preserved. The shipping snapshot is stored in `metadata.capability_vectors_2026_snapshot`.
- **Three-scenario framing.** Every occupation has low/mid/high bands for 2026 and for 2030/2035/2040/2041. Mid is the moderate, displayed default. Low is conservative; high is accelerated.

---

## Coverage

| Record type | v3.2 | v5.0 |
|---|---:|---:|
| Occupations | 388 | **480** |
| Labor records (territory × year) | 608 | **635** |
| Technology timeline events | 57 | **77** |
| Territory × year replaceability entries | 327 | **936** (585 historical 1970–2014 + 351 modern 2015–2041) |
| Historical macro groupings | 3 | **3** |
| Modern territories | 13 | **13** |
| Inline task decompositions | — | **4,818 tasks across 480 occupations** |
| Displayed occupations (curated) | 104 | **104** (13 territories × 8) |

Task decompositions are a v5-only addition — v3.2 had none. The inlined 4,818 tasks (mean 10.0 per occupation, range 2–14 after Audit 3 removals) each carry a capability vector, difficulty threshold, time weight, and source-id citations. Phase 4 originally produced 5,655 tasks; Phase 11 audits removed 825 scrape artifacts / wrong-occupation imports across four intervention passes. The 423-record `metadata.source_count` is the unique-by-registry-key count; the inline `sources[]` array has 6,686 task-level and labor-level references for per-entry provenance.

### Territory counts

| Territory | v3.2 | v5.0 | Δ |
|---|---:|---:|---:|
| Making Things | 45 | 75 | +30 |
| Money & Data | 43 | 57 | +14 |
| Care & Health | 40 | 56 | +16 |
| Land & Sea | 31 | 40 | +9 |
| Making Meaning | 34 | 37 | +3 |
| Building Things | 25 | 34 | +9 |
| Maintaining & Fixing | 30 | 34 | +4 |
| Governing & Protecting | 26 | 31 | +5 |
| Moving Things | 32 | 31 | −1 |
| Feeding & Hosting | 24 | 26 | +2 |
| Buying & Selling | 24 | 22 | −2 |
| Learning & Teaching | 23 | 22 | −1 |
| Thinking & Leading | 11 | 16 | +5 |

Thinking & Leading was redefined at Checkpoint 2 ("Organization-wide leadership, cross-functional knowledge work, and the administrative support surrounding them — deciding what the organization does and coordinating how it runs"). General office clerks (4110) and secretaries (4120) moved into Money & Data at Checkpoint 3; the HR / executive-support sub-cluster stayed in T&L.

---

## Methodological changes

### New fields on every occupation

- `task_decomposition[]` — the ordered list of tasks with per-task `vector`, `difficulty_threshold`, `time_weight_pct`, and `source_ids`.
- `replaceability_2026_low` and `replaceability_2026_high` — scorer-disagreement bands preserved from Phase 5 reconciliation (mean spread 38.8 pp, median 34 pp; wider on creative / unstructured-physical work where honest uncertainty is larger).
- `replaceability_2030_moderate` and `replaceability_2040_moderate` for the projection anchors (the full dataset carries 2030/2035/2040/2041 values with low/mid/high).
- `editorial_justification` (mandatory) — short free-text tying each occupation-level decision to the editorial principle it applies.
- `confidence` and `confidence_reason` — qualitative tags per occupation.
- `projection_note_2030` — narrative note supporting the 2030 anchor where non-trivial.

### Retained from v3.2 schema

`isco_code`, `occupation_name`, `display_name`, `territory_id`, `common_titles`, `primary_barrier`, `barrier_types`, `benchmark_anchor_2026`, `key_barrier_note`, `notes`, `employment_weight_pct`, `global_estimated_employment`, and the `displacement_{2026,2030,2035,2040}_moderate` series.

### Schema amendments applied during Phase 10 assembly

Five patch rounds were required to bring the release candidate to zero validation failures. The substantive schema adjustments: `display_name` maxLength raised from 25 to 35 (to accommodate titles like "Early Childhood Educators"); `barrier_types` and `primary_barrier` enums now include `NONE`; `technology_events` entries allow `access_date`, `citation`, `source_url`, `v32_status`, and `verifier_note`; occupations optionally carry an `isco_verification_note`.

---

## Scoring changes

### Aggregate shifts vs v3.2

Across all 293 occupations whose ISCO codes match in both datasets:

- **Mean replaceability_2026:** v3.2 58.63 → v5 44.34 (**−14.29 pp** on matched subset).
- **Mean displacement_2040 (moderate):** v3.2 37.70 → v5 27.03 (**−10.67 pp** on matched subset).

Across the full v5 population, mean r26 is **45.01** (v3.2's full-population mean was 58.24) and mean displacement_2040 (mid) is **27.27** (v3.2 was 37.97). Two effects drive the r26 drop: (a) the Phase 11 recalibration lowered 2026 capability values on every vector except Phi_U, and (b) four Phase 11 audit rounds removed scrape artifacts and reclassified physical/embodied tasks that had been mis-coded as cognitive in Phase 4.

### Territory-level r26 means (v5, mid)

| Territory | r26 mean | r40 mean (mod) |
|---|---:|---:|
| Making Things | 68.7 | 99.9 |
| Money & Data | 68.5 | 100.0 |
| Buying & Selling | 63.7 | 100.0 |
| Learning & Teaching | 54.5 | 99.7 |
| Governing & Protecting | 44.5 | 94.8 |
| Thinking & Leading | 40.8 | 100.0 |
| Making Meaning | 39.0 | 95.5 |
| Feeding & Hosting | 37.7 | 99.5 |
| Moving Things | 35.9 | 98.2 |
| Care & Health | 35.3 | 93.3 |
| Maintaining & Fixing | 23.3 | 98.9 |
| Building Things | 23.0 | 99.4 |
| Land & Sea | 21.9 | 99.2 |

The r40-mid surface is aggressive: 88.1% of occupations reach replaceability 100 by 2041 under the moderate scenario; only 3.1% remain below 80. This is honest task-math: once capability trajectories saturate past Phase 4 per-task difficulty thresholds, per-task replaceability saturates too. The variance at 2041 is carried by displacement, not by r40. Mid-scenario displacement_2040 ranges from 9.3% to 47.9% with a mean of 27.27%.

### Top 20 individual movers (matched occupations, |Δ r26| largest)

| ISCO | Occupation | v3.2 r26 | v5 r26 | Δ |
|---|---|---:|---:|---:|
| 9112 | Cleaners and helpers | 81 | 0 | −81 |
| 7211 | Metal moulders and coremakers | 85 | 8 | −77 |
| 9611 | Garbage and recycling collectors | 72 | 3 | −69 |
| 2653 | Dancers and choreographers | 69 | 0 | −69 |
| 6210 | Forestry workers | 66 | 0 | −66 |
| 9122 | Vehicle cleaners | 67 | 1 | −66 |
| 8311 | Locomotive engine drivers | 74 | 10 | −64 |
| 9213 | Mixed crop and livestock labourers | 63 | 0 | −63 |
| 6111 | Field crop and vegetable growers | 63 | 1 | −62 |
| 7119 | Building-frame and trades workers | 62 | 0 | −62 |
| 3131 | Power production plant operators | 17 | 78 | +61 |
| 7312 | Musical instrument makers | 68 | 8 | −60 |
| 6221 | Aquaculture workers | 59 | 0 | −59 |
| 1223 | R&D managers | 75 | 16 | −59 |
| 6121 | Livestock and dairy producers | 59 | 0 | −59 |
| 6224 | Hunters and trappers | 58 | 0 | −58 |
| 5241 | Fashion and other models | 58 | 0 | −58 |
| 1113 | Traditional chiefs | 58 | 0 | −58 |
| 7321 | Pre-press technicians | 37 | 94 | +57 |
| 3255 | Physiotherapy techs and assistants | 77 | 21 | −56 |

The direction of the largest drops reflects two Phase 11 patterns. First, embodied-craft, performance, and unstructured-field work that v3.2 scored as cognitive-replaceable was re-vectored to Phi_U (0.15) once audits caught the mis-coding (dancers, models, metal moulders, musical-instrument makers, foresters, farm labourers). Second, physical occupations carrying the `HUMANOID_DEPENDENT` barrier now consistently reflect the deployment absence — in 2026, there is no scaled humanoid for cleaners, vehicle cleaners, farm workers, hunters, or chiefs. The largest upward movers are structured-industrial operators (3131 power plants, 7321 pre-press) and teachers at the cognitive-codifiable end (2353 language teachers), where Phase 4 decomposition better captures the automatable core.

---

## Barrier taxonomy changes

### Enum

`NONE` is a v5 addition to both `primary_barrier` and `barrier_types`. v3.2 had only 2 occupations with no explicit barrier; v5 has 42 — cases where no structural barrier blocks deployment and only adoption-diffusion time gates it.

### Distribution

| Barrier | v3.2 | v5.0 |
|---|---:|---:|
| HUMAN_PREFERENCE | 170 | 93 |
| HUMANOID_DEPENDENT | 99 | 123 |
| ECONOMIC | 65 | 154 |
| REGULATORY | 52 | 69 |
| NONE | 2 | 42 |

The sizeable v3.2 → v5 shifts are driven by the corrected Replaceability ≠ Replacement framing (see the editorial process record). Many v3.2 HUMAN_PREFERENCE assignments were really ECONOMIC (unit economics break the swap today), and NONE cases that v3.2 buried under HUMAN_PREFERENCE defaults are now surfaced honestly.

---

## Projection structure changes

- **Three-scenario framing** replaces v3.2's single central projection. Low = conservative; mid = `min(A_mid, B_mid)` across two Phase 7 forecasters (the tempered read, the default displayed); high = the accelerated read anchored on the more aggressive forecaster's mid.
- **2030 anchors for every occupation,** computed directly from task-decomposition × capability-trajectory × barrier, then reconciled.
- **Terminal year 2041** (= 2026 + 15). v3.2 terminated at 2040. v5's 2041 anchor is canonical and the 2040 values are retained for continuity with v3.2 readers.
- **Capability trajectories published.** `metadata.capability_trajectories_summary` shows the year-by-year mid-band trajectory for each of the six vectors (2026, 2030, 2035, 2041). This summary preserves the Phase 7 mid trajectory values as projection inputs; the 2026 snapshot in `capability_vectors_2026_snapshot` records the post-recalibration starting values used for scoring.

---

## Formula changes (replacement lag)

v3.2 → v5 parameter diff:

| Parameter | v3.2 | v5.0 |
|---|:---|:---|
| Conversion rate | 0.333 | **0.30** |
| Lag schedule 2026 / 2030 / 2035 / 2040 / 2041 | 5 / 28 / 48 / 58 / 60 % | **7 / 18 / 30 / 42 / 44 %** |
| `already_absorbed` | uniform 0.15 | **era-stratified:** pre-2015 0.30 / 2015–2022 0.15 / post-2022 LLM 0.05 |
| NONE barrier multiplier | (implicit 1.0) | **1.20 ×** |
| ECONOMIC | (implicit 1.0) | **1.00 ×** |
| HUMAN_PREFERENCE | (implicit 1.0) | **0.562 ×** (Phase 11 strengthened from Phase 6's 0.70) |
| REGULATORY | (implicit 1.0) | **0.405 ×** (Phase 11 strengthened from Phase 6's 0.50) |
| HUMANOID_DEPENDENT | (implicit 1.0) | **0.15 ×** |

Barrier-type stratification was validated empirically at Phase 6: cross-section R² jumps from 0.61 (plain conversion × lag) to 0.85+ when barrier type is included as a categorical predictor. The Phase 11 recalibration strengthened HUMAN_PREFERENCE and REGULATORY proportionally to preserve empirical fit against the Anthropic Economic Index observed-coverage anchor after Phase 5 r26 scores were rescored to pure task-math. Historical-case anchors (telephone operators 1920–2023, bank tellers, travel agents, cashiers, translators, CSRs, bookkeeping clerks) constrain the lag schedule.

---

## Display curation

104 occupations carry `display_in_territory = true` (13 modern territories × 8 each), matching v3.2's display density. The curation was locked at Phase 11 (`decisions.json`) after reviewer-directed swaps to improve editorial representation.

### Display name overrides applied

- 7126 "Plumbers and pipe fitters" → **Plumbers** (Building Things)
- 7311 "Precision-instrument makers and repairers" → **Precision Instrument Makers** (Making Things)
- 0310 "Armed forces occupations, other ranks" → **Soldiers** (Governing & Protecting)

### Notable swaps from v3.2 display selection

- **Making Things:** Mechanical Engineers dropped in favour of Robotics Engineers (`2149-robotics`). CNC Operators and Potters (7314) added.
- **Thinking & Leading:** Sociologists dropped (too similar to Humanities Academics). Kept Mathematicians, HR Specialists, Chief Executives, Policy Professionals, Humanities Academics, Economists, Physicists.
- **Governing & Protecting:** Military Officers (0110) swapped for Soldiers (0310, ~44% of G&P employment vs ~13% for officers; more iconic). Tax Inspectors retained over Customs Officers per reviewer: "automated borders are already a thing; AI auditing tax returns is the scary one."
- **Care & Health:** Child Care Workers added (previously no representation for the ~13% employed in child care).
- **Land & Sea:** Farm Workers and Horticulturalists replaced by Vegetable Growers (26.80% of L&S employment), Offshore Oil Workers (rigs/offshore signal), and Earth Scientists (scientific-layer representation).
- **Feeding & Hosting:** Waiters dropped (redundant with Kitchen Helpers + Cooks). Added Catering Managers and Bookmakers / Croupiers (gaming/non-restaurant).
- **Making Meaning:** Authors and Screenwriters added — the canonical "is AI replacing writers?" role, distinct from Journalists.
- **Learning & Teaching:** Driving Instructors added (out-of-classroom teaching context).
- **Maintaining & Fixing:** Watchmakers and Clock Repairers added (artisan/craft signal).
- **Money & Data:** Securities Traders dropped (weak outlier; four other finance roles cover the space).

---

## What's preserved from v3.2

v3.2's hand-curated editorial substrate was the most valuable inheritance. v5 preserves:

- **Occupation meaning as the preservation anchor.** Where v3.2 had attached a wrong ISCO code to a correctly identified occupation, Phase 2a reassigned the code while keeping v3.2's display name, territory assignment, employment weight baseline, and the spirit of the barrier note. 112 of 112 `PRESERVE_V32` cases held their territory across Phase 2d reconciliation.
- **Territory framework.** Thirteen modern territories plus three historical macro groupings. v5 refined T&L's definition and moved a handful of occupations between territories but did not add or remove any territory.
- **Display density convention.** Eight displays per modern territory, 3 historical groupings × 8 each for 1800–1950 curation.
- **Timeline events structure.** v5 preserved 38 v3.2 events verbatim, edited 16 (year or description corrections), removed 3 unverifiable entries, and added 23 new 2024–2026 events (AlphaFold 3, Claude 3.5 Sonnet, Claude Computer Use, Devin AI, EU AI Act, Anthropic Economic Index, etc.).
- **Barrier notes where they were still strong.** 125 v3.2 notes preserved unchanged at Phase 8; 158 light-edited; 189 got targeted rewrites with mandatory evidence URLs after a template-slop detection pass.

---

## Known limitations

- **Editorial overrides queued but not applied.** Phase 11 surfaced two evidence-backed concerns that are documented but not baked into v5.0:
  - *ISCO 5245 Service Station Staff* (r26 = 44, `primary_barrier = HUMANOID_DEPENDENT`). Self-service pumping is already universal across most of the world; the low r26 appears to be a Phase 4 task-decomposition artifact (tasks coded as Phi_U when they should be P_A or Phi_S). Proposed override: r26 → ~88, primary_barrier → REGULATORY.
  - *REGULATORY-barrier occupations with r41 ≥ 95* (Lawyers at r41=100, Senior Government Officials at 99, Patent Attorneys, Legislators, Litigation Attorneys). Projections imply near-full replaceability despite regulatory floors (bar exam, named-human mandates). The multiplicative barrier model probably needs a floor component for these cases.

  Both are deferred to post-launch editorial work or v5.1.

- **High r40-mid shape.** Under the moderate scenario, mean replaceability at 2040 is 84.6 across 480 occupations and 25% score ≥ 90. The logistic crossover (k=8) ceiling is asymptotic, so no occupation reaches exactly 100 — the maximum is around 98. Most occupations sit in the 80–95 band by 2040; this still pushes editorial weight onto the displacement column where the variance lives. Readers should interpret 2040 workforce implications via displacement (mean 24%, range 9–47%) rather than via r40 alone — replaceability above 90 means "most of the task profile crosses the capability threshold"; displacement at 24% is what tells you what the workforce actually looks like.

- **Residual scrape artifacts below the audit bar.** The Phase 11 audit bar was consistently 2-model agreement (Audits 1 and 3 both used adversarial QC). Below-threshold contamination likely remains. A v6 re-run of Phase 4 with tightened anti-scrape guardrails is recommended.

- **Benchmark-vs-deployment calibration evolves.** The post-recalibration 2026 capability values trim Phase 5's benchmark-anchored set toward observed deployment reliability. This is our best honest read as of April 2026; production reliability data for humanoid robotics, agentic coding, and autonomous vehicles is still developing and values may need further adjustment in v5.1 or v6.

- **Within-vector heterogeneity.** C_G (specialist QA to novel reasoning), Phi_S (robotaxis to heavy equipment), and S_E (coding agents to incident command) each cover wide internal distributions. Single-point values average over heterogeneity; the bounds carry some of the uncertainty but a v6 split of these vectors would add precision.

- **Phase 6 barrier-model form.** Multiplicative barrier multipliers work well across most of the distribution but produce counterintuitive results at high r26 × REGULATORY (lawyers at r41 = 100). A floor-adjusted barrier model for regulatory frictions is a likely v6 change.

- **Task-classification ceiling persists.** Phase 4's three-way reconciliation achieved 84.2% agreement; the 15.8% split cases were defaulted to the Codex adversarial pass and flagged. The Phase 11 audits re-examined a large subset (notably high-r26 physical occupations via Audit 2 and every task in every territory via Audit 3) but exhaustive per-split human adjudication was out of scope.

- **Historical backfill uses current task decompositions + weights.** Phase 12 produces honest historical capability values but applies them against today's occupation task lists and within-territory employment weights. The number reads as "what share of today's labor would have been technically replaceable at that year's capability" — not "what share of 1985's actual labor force." Reconstructing historical occupation composition at the 481-occupation granularity is deferred to a future version.

---

## Post-launch editorial polish (2026-04-21)

Two parallel review instances surfaced quality issues, applied after reviewer sign-off:

- **Phase 14 legibility sweep** — 33 display renames covering truncated labels, ambiguous bare-adjective displays, and three display-vs-ISCO mismatches. Examples: ISCO 2230 "Traditional & Complementary" → "Traditional & Complementary Medicine"; ISCO 4413 "Coding" → "Coding & Proofing Clerks" (it had been reading as software coding); ISCO 7234 "Aircraft Engine Mechanics" → "Bicycle Repairers" (the official ISCO 7234 scope; aircraft mechanics already exist separately at 7232); ISCO 2635 "Religious Professionals" → "Social Workers & Counsellors" (caught during Phase 15 review — 2635 is officially Social work and counselling; 2636 is the actual religious-professionals occupation).
- **Phase 15 common-titles enrichment** — 11 occupations updated to fill search gaps. Crypto/blockchain titles added to ISCO 3311 (cryptocurrency trader, digital asset trader, crypto market maker), 2512 (blockchain engineer, smart contract developer, solidity developer), and 2413 (on-chain analyst, crypto analyst). Yoga / Pilates / barre / wellness coaching titles added to ISCO 3423. Modern AI roles (prompt engineer, AI researcher, MLOps engineer, LLM engineer, AI safety researcher) replacing generic titles on ISCO 2512-ml. Three previously-broken arrays (2431-social, 3153-uas, 2512-ml) had been carrying contamination from unrelated occupations and are now correct.
- **MLM/waiter contamination dedup** — the `direct sales coach`, `independent beauty consultant`, `independent distributor`, `independent sales associate/representative`, `door-to-door sales trainer` cluster was contaminating four occupations where it didn't belong (ISCO 5211 Market Salespersons, 5212 Food Truck Operators, 9520 Street Vendors, 5221 Shopkeepers). Stripped from all four; preserved on ISCO 5243 (Door-to-door Salespersons) where the cluster is correct. ISCO 5212 also had five waiter-titles (food server, kitchen runner, etc.) belonging to ISCO 5131 — also stripped. Affected occupations now have thin titles flagged for v5.1 web-verified enrichment at `metadata.deferred_to_v5_1`.
- **ISCO 1219 territory move + display rename.** "Hospitality Directors" → "Admin Services Directors" + reassigned from feeding_hosting to thinking_leading. Rationale: ISCO 1219 official scope is "Business services and administration managers not elsewhere classified" — corporate admin/services directors, not hospitality industry executives, which already exist separately at ISCO 1411 (Hotel Managers) and 1412 (Restaurant Managers). The v5 functional-manager principle says functional managers go with their function. Within-territory employment weights renormalized in both territories using `global_estimated_employment` as ground truth — both feeding_hosting and thinking_leading still sum to 100.000% post-move. 1219's weight in thinking_leading: 18.19% (substantial chunk of admin-services managers globally; previously diluted at 2.99% inside larger feeding_hosting).
- **ISCO 3422-personal dropped.** Off-by-one specialized split: personal training officially sits in ISCO 3423, not 3422. The split had zero employment_weight (didn't drive territory aggregates) so removal had no aggregate impact. ISCO 3423 is now the canonical home for personal trainers, yoga, Pilates, group fitness, and wellness coaches. **Occupation count: 481 → 480.**
- **End-to-end recompute** of replaceability + displacement + territory aggregates against the modified inputs. Phase 10 validator: PASS, 0 critical failures.

Deferred to v5.1 (recorded at `metadata.deferred_to_v5_1`):
- ISCO 5211 / 5212 / 9520 thin-titles after MLM/waiter dedup (need Phase 15.x web-verified enrichment)
- Proposed specialized split ISCO 2422-compliance for AML/KYC/financial-crime officers (≥50K US LinkedIn postings, distinct task profile)

---

## Late-cycle fixes (2026-04-20)

After the initial 2026-04-19 release, a spot-check surfaced a set of small-but-real issues that were fixed on the dev branch before production deploy:

- **Stale capability trajectories summary in dataset metadata.** `metadata.capability_trajectories_summary` was carrying pre-parallel-shift Phase 7 values (C_R 2041 0.98 rather than 0.87, etc.). The block was regenerated from the post-shift `phase7/reconciler/capability_trajectories_2026_2041.json` and a traceability note was added.
- **Methodology doc cited the same stale 2041 anchors.** The v5_methodology.md paragraphs for 2041 mid and high anchors were patched to cite post-shift values, with a note pointing to the `*_phase7_original` fields in the trajectory file for traceability.
- **`metadata.scenarios_shipped` flag added.** v5.0 ships the moderate (mid) scenario as the editorially-reviewed display; low and high bands are structural only (produced deterministically from Phase 7 low/high trajectories; not reviewed occupation-by-occupation). The flag encodes this disclosure for downstream consumers.
- **Common-titles contamination cleanup.** A cross-occupation contamination pattern (the strings "caddymaster", "community life director", "aquatics supervisor", "bar and restaurant manager", etc.) was present in 7 ISCO 5xxx service-sector occupations. Titles stripped and 6 occupations augmented with domain-correct replacements (ISCO 3423, 5113, 5141, 5142, 5164, 5311, 5322).
- **Business-development coverage.** ISCO 3322 Commercial Sales Representatives common_titles were updated to include modern BD-track titles (account executive, business development representative, business development associate, sales development representative).
- **UI schema-compat shim.** `index.html` was updated with a one-line alias (`V2.replaceability ?? V2.territory_replaceability`) so the v5.0 rename of the territory-level replaceability array doesn't break the canvas. Both v3.2 and v5 schemas now render with the same front-end code.

---

*Large Labor Model v5.0 is the work of a reviewer-directed build pipeline that treated every prior version as sanity-check only. The editorial principles, phase-by-phase process, and Phase 11 emergency interventions are documented in the companion files [v5_methodology.md](v5_methodology.md) (public methodology page) and [v5_editorial_process.md](v5_editorial_process.md) (full post-mortem of the build journey).*
