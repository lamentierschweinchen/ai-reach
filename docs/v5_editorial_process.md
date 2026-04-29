# Large Labor Model v5.0 — Editorial Process Record

**Build window:** 2026-04-11 → 2026-04-19. **Reviewer:** Lukas (project owner). **Architect:** Claude Opus 4.6 / 4.7 instances across phases, with scorers/forecasters/auditors from Opus 4.6, Opus 4.7 (1M context), GPT 5.3 Codex, GPT 5.4 Codex, GPT 5.2 Codex Max, Sonnet 4.6, and Antigravity. **Purpose:** painstaking record for future v5.1 / v6 review — specifically, a full accounting of Phase 11 emergency interventions.

---

## Context and scope

### Why a v5 rebuild was needed

The dataset that powers largelabormodel.com shipped as v3.2 in prior versions. v3.2 had inherited a mix of data-quality issues from v3.0:

- **~200 wrong ISCO codes.** Occupation meanings correctly identified but attached to wrong codes (v3.2 "Chief Executives" at ISCO 1111, but 1111 is Legislators; "Physicists and Astronomers" at 2112, but 2112 is Meteorologists).
- **89 fabricated codes** — codes that don't exist in ISCO-08 (e.g., 2171 "Urban and Traffic Planners", 2213 "Surgeons" — real codes are 2164 and 2212-surgeon). Only ~13% of v3.2 occupations had both a correct code and a canonical title.
- **Template-filled common titles.** Many occupations carried patterns like "[name] specialist/professional/operator" from a templated fill, not sourced.
- **Opaque sourcing in places.** Some fields had no audit trail.
- **Flattened-out Thinking & Leading territory** — eroded by territory moves; framing no longer internally coherent.

The reviewer's call: don't patch v3.2; rebuild v5 ground-up, with v3.2 as post-hoc sanity check only. v4 had been attempted as an incremental fix and failed — its primary failure was template slop on barrier notes (39% of v4 notes contained recurring stock phrases keyed to barrier type). v4's failure informed v5's anti-fabrication rigor.

### What v3.2 was and wasn't

v3.2 was good at editorial curation (display names, territory assignments, employment weights, the spirit of barrier notes) and bad at underlying data (ISCO codes, common titles, task decomposition, capability anchoring). v5 preserves v3.2's editorial substrate — occupation meaning as the preservation anchor — while rebuilding every data-grounded field.

### Scope of v5

480 occupations × 13 modern territories × 3 historical groupings × 635 labor records × 4,818 inline task decompositions (after Phase 11 audits, down from Phase 4's 5,655) × 77 timeline events × three-scenario 2026–2041 projections.

---

## The 11-phase build pipeline

Each phase produced a canonical deliverable, a reviewer-signed checkpoint, and archived intermediate outputs. The build advanced only after reviewer sign-off.

| Phase | Output | Quality gate | Outcome |
|:---|:---|:---|:---|
| 0 | Schema lock + spec | JSON Schema Draft 2020-12 validation | PASS 2026-04-15 |
| 1 | ISCO-08 canonical reference (436 unit groups + 10 approved custom codes) | Byte-match against freshly-downloaded ILO CSV; IHE FHIR cross-check on 27 civilian samples | PASS 2026-04-15 |
| 2 | Occupation master (480 occupations) | 3 independent scorers + reconciler; 87.3% unanimous agreement; 112/112 PRESERVE_V32 baseline-match | PASS 2026-04-16 |
| 3 | Labor records (635 records, occupation-up methodology after attempt 1 archived) | Territory-assignment audit; structural verification 20/20 spot-checks; armed-forces patch | PASS 2026-04-16 |
| 4 | Task decompositions (5,655 tasks after 3-way reconciliation) | Vector distribution in target; preservation check; anti-fabrication post-flight | PASS with residual issues 2026-04-17 |
| 5 | Replaceability 2026 (481 records + low/high bounds + barriers) | Blind calibrator + 3 scorers + reconciler; median-rule for wide disagreements | PASS 2026-04-17 |
| 6 | Replacement formula (conversion × lag × era × barrier multipliers) | Fit against 7 historical cases + 28-occupation Anthropic Economic Index cross-section; R² 0.85+ | PASS 2026-04-17 |
| 7 | Capability trajectories + occupation projections 2026 → 2041 | 2 forecasters + reconciler; double-counting barrier fix applied; three-scenario merge rule | PASS 2026-04-18 |
| 8 | Common titles + barrier notes | 3 retrieval sources + reconciler + template sweeper; targeted 189-note rewrite after v1's 39% template slop detected | PASS 2026-04-18 |
| 9 | Timeline events (77 events, 1769–2026) | Adversarial 20-event stratified verifier sample; 3 edits applied, zero fabrications | PASS 2026-04-18 |
| 10 | Adversarial validation | Isolated validator with zero builder context; 25 structural/content/editorial/source checks | PASS 2026-04-18 (102 attention-flagged candidates for Phase 11) |
| 11 | Editorial sign-off + release | Reviewer walk-through + five emergency interventions | PASS 2026-04-19 |

---

## Checkpoint-by-checkpoint journey

### Checkpoint 1 — ISCO-08 reference (2026-04-15)

**What Phase 1 produced.** 436 canonicalized ISCO-08 unit groups with titles, definitions, ISIC Rev.4 hints, and major / sub-major / minor hierarchy. A whitelist of 10 proposed custom codes.

**What reviewer caught.** Sub-major 51 (Personal service workers) had blanket ISIC hint "I (Accommodation and Food Service)" applied to all 17 unit groups, but only 4 actually belong to Section I. The other 13 span Sections S, T, N, P, H. Fixed inline. The XDEVOPS_SRE whitelist proposal had a parent/split mismatch (parent 2523 but reasoning said 2512); normalized to 2512. Verifier flagged undocumented apostrophe normalization; extended `conventions_note`.

**Principles established.** Inline corrections at checkpoint are acceptable when evidence is clear; full reruns are for systemic issues. Residual risk logging is mandatory (the ILO PDF was not independently re-fetched; that gap was noted with mitigation documented).

**Rework triggered.** None. Whitelist: 3 ADD top-level X codes (`XDATA_SCI`, `XCONTMOD`, `XCYBERSEC`), 6 SPLITs (`2512-ml`, `2512-devops`, `3153-uas`, `9621-gig`, `2166-ux`, `2523-cloud`), 1 REJECT (`XPROMPT_ENG`).

### Checkpoint 2 — Occupation inventory + territory mapping (2026-04-16)

**What Phase 2 produced.** 480 occupations across 13 territories, reconciled from a 3-scorer territory assignment (Claude / Codex / Antigravity) + reconciler. 87.3% unanimous agreement; 112/112 PRESERVE_V32 baseline-match; only 1 unanimous override of v3.2 (9621-gig → Moving Things).

**What reviewer caught.** 35 Phase 2d flags resolved individually (20 confirms, 14 moves, 1 split). 5 gap DEFERs: 4 kept (1113 Traditional chiefs, 5161 Astrologers, 6224 Hunters and trappers, 9332 Animal-drawn-vehicle drivers), 1 rejected (7319 Handicraft NEC). 37 specialized splits: 35 accepted, 2 rejected. Reviewer overrode architect's rec to reject 2261-orthodontist and 2512-mobile (both kept on credentialing / career-track grounds). T&L redefined with a 178-character description: "Organization-wide leadership, cross-functional knowledge work, and the administrative support surrounding them — deciding what the organization does and coordinating how it runs." Reviewer overrode architect's rec on 4419 Clerical support NEC → Money & Data.

**Principles established.** **Defensibility over count targets** — the 480–520 occupation range is a sanity bracket, not a constraint. Decisions on merits, not to hit numbers. T&L redefinition staged, not applied, to prevent sandbox-data drift mid-phase.

### Checkpoint 3 — Labor data rebuild (2026-04-16)

**What Phase 3 produced.** 635 labor records spanning 1800–2025 using an occupation-up methodology.

**Journey.** Attempt 1 used ISIC-down methodology with editorial split ratios for historical data; two independent runs produced 40–60% variance for 5 territories. Too much uncertainty for Phase 5 to score against. Architect re-scoped and archived attempt 1 (`phase3_attempt1_isic_down/`), rebuilt with deterministic occupation-up aggregation using Phase 2's occupation → territory map.

**Reviewer decisions.** 5163 Undertakers kept in Care & Health (end-of-life care continuum). 5164 Pet groomers split into bare 5164 (pets → C&H) + new 5164-livestock (farm animals → L&S) → 481 total. Clerks cluster distributed: 4110 + 4120 → M&D; 4416 / 3341 / 3343 / 3343-executive stayed in T&L (HR sub-cluster). Armed-forces patch merged: 38 World Bank MS.MIL.TOTL.P1 records (1988–2025) added to G&P.

**Principles established.** **v3.2 firewall — v3.2 is NEVER an authority, only post-hoc sanity check.** v3.2 files are quarantined out of each phase's active inputs; verifiers operate under no-v3.2-comparisons rules. The attempt-1 re-scope made this concrete: the first attempt had to be thrown away because editorial split ratios had implicitly made v3.2's territory boundaries the authority.

### Checkpoint 4 — Task decomposition (2026-04-17)

**What Phase 4 produced.** 480 occupations × 5,655 tasks (mean 11.76/occupation), 3-way reconciled across: (1) v2 context-bound reclassification (Opus 4.7), (2) v3 Codex GPT 5.4 adversarial reduction from 22+ tasks to 10–15, (3) Opus 4.6 context-free classifier (blind to occupation context). 3-way reconciliation: unanimous 34.4%, majority 49.8%, three-way-split 15.8% (defaulted to Codex v3 pass, flagged).

**Journey.** v1 rule-based classifier catastrophically broke vector distribution (Phi_U at 43.8%, P_A at 0.2%). Targeted Opus 4.7 reclassifier (v2) fixed it. Codex adversarial + context-free then caught context bias. Post-reconciliation G&P S_E demotion applied (124 tasks → C_G; 5 revivals).

**What reviewer caught / architect flagged.** Vector distribution partially off target: C_R 19.0% (target 25–35%) slightly low, C_G 36.4% (target 20–30%) slightly high. 4 of 6 vectors in target range. 895 three-way-split tasks flagged for Phase 11 editorial review. 209 majority-qualified cases (context-free dissent with HIGH confidence). G&P S_E over-corrected to 1.4%.

**Principles established.** **Architect priors are expectations, not canon.** Target ranges are priors. If specialized instances produce values outside the range but well-argued, data-grounded, and coherent, those values are acceptable. **Phase 4 task-classification ceiling is real.** Three independent classifiers converged on 84.2% of tasks; the 15.8% remaining represent genuine ambiguity that no automated approach resolved. Phase 5 should include sensitivity analysis rather than re-running classification.

**Rework triggered inside the phase.** Two full reruns within Phase 4 (v1 broken; v2 calibration fix; v3 adversarial reduction). Gemini Instance C's first attempt was rejected for template fabrication (completed 5–10× faster than budget; catastrophic Phi_U over-application).

### Checkpoint 5 — Replaceability 2026 scoring (2026-04-17)

**What Phase 5 produced.** 481 records with `replaceability_2026` + low/high bounds + primary_barrier + score_basis + confidence, reconciled from 3 independent scorers: Scorer A (Opus 4.7) mean 57.8, Scorer B (GPT 5.4 Codex) mean 55.2, Scorer C (GPT 5.3 Codex, rerun after Gemini first attempt rejected for fabrication) mean 42.9. Reconciler (Opus 4.7) used median-based resolution for wide cases (70 tight + 99 moderate + 125 significant + 187 wide); final mean 54.9, median 61. Calibrator (Opus 4.7 max, blind): C_R 0.87, C_G 0.62, P_A 0.78, Phi_S 0.60, Phi_U 0.15, S_E 0.42.

**Editorial decisions.** All 312 reconciler-flagged disagreements accepted as-is. Gemini observed-coverage data reframed as Phase 6 input, not Phase 5 adjudication ground truth. No retroactive making_meaning adjustments — median rule already discounts Opus-A's creative optimism; wide low/high bounds carry honest uncertainty.

**Principle first framed here (refined at C7, CORRECTED at Phase 11).** **Replaceability ≠ Replacement.** Phase 5 scorers applied barrier discounts for all four types under a "if swapped today, would it work?" test; Phase 6 would model adoption lag separately. *This framing was later corrected at Phase 11 — see Intervention A below.*

### Checkpoint 6 — Replacement formula (2026-04-17)

**What Phase 6 produced.** Calibrated replacement formula `displacement(t) = (conversion × Δreplaceability + lag(t) × pending) × barrier_multiplier`, fit against 7 historical cases + the 28-occupation 2026 Anthropic Economic Index cross-section. Parameters: conversion 0.30 (v3.2 0.333); lag 2026/2030/2035/2040/2041 = 7/18/30/42/44% (v3.2 5/28/48/58/60%); era-stratified `already_absorbed` pre-2015 0.30 / 2015–2022 0.15 / post-2022 LLM 0.05; barrier multipliers NONE 1.20× / ECONOMIC 1.00× / HUMAN_PREFERENCE 0.70× / REGULATORY 0.50× / HUMANOID_DEPENDENT 0.15× (HUMAN_PREFERENCE and REGULATORY later strengthened at Phase 11). Empirical validation: R² 0.61 plain → 0.85+ with barrier as categorical predictor.

**Reviewer's editorial stance.** "Conservative-lag doesn't worry me; capability frontier is primary pressure." v5 projects 6.9–15.7 pp lower displacement than v3.2 at 2041 across all 13 territories — accepted. **Principle reinforced.** Terminal year is 2041 (= 2026 + 15). Never 2040.

### Checkpoint 7 — Capability trajectories + projections (2026-04-18)

**What Phase 7 produced.** Capability trajectories 2026–2041 for all 6 vectors + 481 per-occupation projections at 2030/2035/2040/2041. Pipeline: Forecaster A (Opus 4.7) + Forecaster B (GPT 5.4 Codex) + Reconciler (Opus 4.7).

**Two mid-pass corrections.**
1. **Double-counting barrier fix.** The original brief had ECONOMIC softening to 0.5× and HUMANOID_DEPENDENT to 0.4× by 2041. This double-counted: HUMANOID_DEPENDENT is already captured in the Phi_U trajectory rising 0.15 → 0.66; ECONOMIC is captured in capability-adoption curves. Fix: HUMANOID_DEPENDENT and ECONOMIC set to 1.0× (no independent softening over time). REGULATORY 0.9× and HUMAN_PREFERENCE 0.7× retained. v1 archived.
2. **Three-scenario merge rule.** The original reconciler averaged `A_mid + B_mid`, pulling canonical mid toward Forecaster B's aggressive reading. Corrected to `canonical_mid = min(A_mid, B_mid)` — mid = tempered, high = accelerated (B's mid becomes canonical high anchor). v2 archived.

**Principle established (§2.8 in the architect HANDOFF).** **Reasoned model, not biased model** — the model depends on reasoning validated adversarially. Reviewer hunches are not canon absent specific evidence. But "it's a model, not a prediction" is not license to produce fantasy numbers. Failure mode logged: architect had loaded reviewer's AGI-soon framing into Phase 7 mid trajectory via "preserve aggressive scenarios" brief language; corrected via explicit three-scenario merge rule.

### Checkpoint 8 — Barrier notes + common titles (2026-04-18)

**What Phase 8 produced.** 480 occupations × 4–8 canonical titles (3,838 unique; O*NET Sonnet 4.6 / BLS GPT 5.4 / live LinkedIn GPT 5.3). 481 barrier notes (254 with deep-linked evidence URLs across 101 unique domains).

**Journey — v1 failure and recovery.** The v1 barrier editor produced **189 of 481 notes (39%) as templated slop** — stock phrases keyed to barrier type when v3.2's framing disagreed with Phase 5's primary_barrier. Caught via opening-phrase clustering (56), near-duplicate detection (26), missing-evidence audit (140, overlapping). Targeted 189-note rerun with banned-openings + mandatory evidence + 0.80 near-dup threshold: 100% evidence coverage, 0 violations across 4,319 scanned fields.

**Principle established.** **Editorial "realignment" workflows are the highest-risk fabrication vector.** Any future brief that realigns existing text against new classifications MUST bake in banned-opening phrase list from pre-scan, mandatory evidence URL per rewrite, stricter 0.80 near-dup threshold. Do not add anti-template rigor on rerun; bake it into the initial brief.

### Checkpoint 9 — Timeline events (2026-04-18)

**What Phase 9 produced.** 77 events (1769–2026), all with deep-linked source URL + access date + citation. 38 v3.2 events preserved, 16 edited, 3 removed (unverifiable), 23 new 2024–2026 added. Adversarial 20-stratified-sample verifier: 17 verified, 3 edit_recommended, 0 fabricated. Three inline edits (1798 Whitney source URL; 1953 SABRE year → 1957; 2019 China robot density figure replaced with IFR-verified 2020 246/10k).

### Checkpoint 10 — Adversarial validation (2026-04-18)

**What Phase 10 produced.** Isolated GPT 5.4 validator with zero builder context. All 25 structural / content / editorial / source checks PASS. 102 attention-flagged candidates for Phase 11 editorial review (not failures) — 88 HUMANOID_DEPENDENT × r26 < 30 candidates (Service Station Staff the canonical case), 14 REGULATORY × r41 ≥ 95 candidates. **Assembly journey:** initial assembled dataset had 15,484 validation failure instances from assembly bugs (not data quality); six rounds of in-place patches (metadata fields, schema enum, sources schema, `display_name` maxLength 25→35, display-name shortening, ISCO 3135 padding) brought it to zero.

### Checkpoint 11 — Editorial sign-off (2026-04-19)

**What Phase 11 was supposed to be.** Reviewer reads v5_changelog (auto-generated by a summary instance), spot-checks 5–10 random occupations for internal consistency, resolves the 102 attention-flagged candidates, stages to `dev-largelabormodel.vercel.app`, approves, deploys to production. Plan budgeted 1–2 hours.

**What Phase 11 actually became.** Five emergency interventions plus a full 13-territory adversarial deep review. Phase 11 ran from 2026-04-18 into 2026-04-19 and was the most substantive editorial phase of the entire build.

Described in detail below.

---

## Key editorial principles established during v5

Load-bearing rules, in operational order:

**Process principles.** (1) **Phase-by-phase prompt writing.** Prompts for Phase N+1 are written ONLY after Phase N's checkpoint passes — each phase's prompt needs the prior phase's real output. (2) **v3.2 firewall.** v3.2 is never an authority, only post-hoc sanity check; files quarantined out of each phase's active inputs. (3) **Defensibility over count targets.** Count ranges are sanity brackets, not hard constraints. (4) **Architect priors are expectations, not canon.** Well-argued out-of-range values are acceptable. (5) **Adversarial multi-model pattern.** Independent models in fully separate sessions; expect 72–87% unanimous agreement as healthy (higher suggests contamination, lower suggests ambiguous brief). (6) **Anti-fabrication post-flight.** Check domain diversity, template phrases, bare-homepage URLs, meta-language, completion time (added after Gemini Instance C's template-fabricated Phase 4 attempt).

**Editorial principles.** (7) **Replaceability ≠ Replacement (load-bearing).** Replaceability = tech × economics × availability. Replacement = regulatory + preference + lag. Refined at C5/C7, CORRECTED at Phase 11 (Intervention A). (8) **Reasoned model, not biased model.** Reviewer hunches ≠ canon without specific evidence; "it's a model, not a prediction" is not license to produce fantasy numbers.

**Recovery principles.** (9) **Editorial "realignment" workflows = highest fabrication risk** — bake in banned-opening lists, mandatory evidence URLs, stricter near-dup thresholds up front. (10) **Preserve v2/v1 archives on every reconciliation.** Auditable archives at `phase4/reconciler_v1_pre_reclassification/`, `phase4/attempt3_*`, `phase7/deliverables/*.v1_doublecounted.bak`, and pre-intervention `deliverables/ai_reach_v5.0.pre_*.json.bak`.

---

## Phase 11 emergency interventions (the most detailed section)

Phase 11 was expected to be editorial sign-off + release. Instead it surfaced five deep issues — A through E — and then a sixth intervention (the Audit 3 territorial deep-review round) after a reviewer sanity-check caught further issues in nearly every occupation sampled. The interventions were run by the reviewer's decision and the architect's execution, with adversarial audits from independent instances. Without these interventions, v5 would have shipped with material quality issues.

### Intervention A — Replaceability ≠ Replacement framing correction

**What went wrong.** The §2.6b framing as written at Checkpoint 7 bundled regulatory and preference into replaceability via a "would swap today work?" test, discounting r26 scores for regulatory gates and preference collapse. The shipping methodology defines replaceability narrowly (tech × economics × availability). Under the narrow definition, "Lawyers r26 = 41 AND r41 = 100" is incoherent — regulation both gates today AND dissolves by 2041. Under the correct framing, "Lawyers r26 ≈ 78 (capability) AND displacement_2041 ≈ 20% (regulation keeps the gap open)" is honest. The reviewer caught the conflation during Phase 11 review.

**What was done.** Phase 5 r26 scores were re-computed to pure task-math for the 162 occupations carrying REGULATORY or HUMAN_PREFERENCE discounts (69 REGULATORY + 93 HUMAN_PREFERENCE). Those barrier types moved cleanly to the Phase 6 lag-multiplier side. ECONOMIC and HUMANOID_DEPENDENT stayed replaceability-side (capability / economics gates, not regulatory / preference). Phase 6 multipliers strengthened proportionally to preserve the Anthropic Economic Index empirical anchor: HUMAN_PREFERENCE 0.70× → 0.562×; REGULATORY 0.50× → 0.405×. The two axes are now cleanly separated without changing the displacement fit.

**Why this matters.** The viz tells two stories (replaceability + displacement); if the scores bundled regulatory and preference into the first, neither could be told honestly.

### Intervention B — Four-instance adversarial task audit (Audit 1)

**What went wrong.** Checkpoint 4 shipped 5,655 tasks with two residual issues: 895 three-way-split tasks defaulted to Codex v3 without human adjudication, and systematic vector mis-classifications in the craft / physical / embodied-performance cluster. The architect's Checkpoint 4 recommendation — "include sensitivity analysis at Phase 5" — didn't catch the scrape artifacts at all.

Phase 11 launched a four-instance adversarial audit. Upper half (240 occupations / 2,793 tasks): Instance A (Opus 4.7) 350 flags, Instance B (GPT 5.4) 674 flags. Lower half (241 occupations / 2,823 tasks): Instance C (Opus 4.7) 333 flags, Instance D (GPT 5.4) 623 flags. Each instance operated blind to the other three.

**What the audits caught.** Four patterns, each with ~10+ occupations affected:

- **Scrape contamination — the largest failure mode** (~9.5% of upper-half tasks, ~11.8% of lower-half). Families: ISCO taxonomic descriptors ("This unit group covers..."), ISCO fragments split mid-description, cybersecurity curriculum boilerplate appearing verbatim across 10+ unrelated occupations, WHO/NHS navigation, AWS/SageMaker marketing contaminating non-ML occupations, Deloitte consulting promo text, a "Product Designer Reflow California" careers-page footer duplicated across unrelated occupations, and cross-domain contamination (pottery tasks in 7315 Glass makers; coroner tasks in 3353 Government social benefits; DJ tasks in 5161 Astrologers; aircraft-ground-handling tasks in 9332 animal-drawn-vehicle drivers). Contamination concentrated in tail task indices 8–13, consistent with a search-then-scrape pipeline that failed to extract only prose-in-list format.
- **Embodied performance mis-coded as C_G.** Singing (2652), instruments, acting (2655), acrobatics (2659), athletic competition (3421), modelling (5241), hands-on cooking/bartending — all tagged C_G 0.60. The calibrator places embodied performance under Phi_U (0.15); these tasks were being counted replaceable under C_G when they shouldn't have been.
- **Hand-crafted making mis-coded as C_G or P_A.** Sculpting, hand-painting, engraving, weaving, jewellery, pottery. Physical work in unstructured settings, incorrectly tagged cognitive or factory-structured.
- **Air traffic control as Phi_S** (3154, all 12 tasks). ATC is the calibrator's canonical S_E example; reclassified S_E.

**How reconciliation resolved the flags.** Cross-instance 2-model agreement (A+B on upper; C+D on lower) was the acceptance bar. **461 scrape artifacts** accepted for removal. **87 vector reclassifications** accepted. **24 difficulty recalibrations** (within 0.10 agreement) accepted. Solo flags NOT applied (sampling showed ~20–30% false-positive rate on single-instance flags).

**Task count after Intervention B:** 5,194 (from 5,655).

### Intervention C — Focused GPT audit on high-r26 occupations (Audit 2)

**What went wrong.** Audit 1 focused on the Phi_U-vs-C_G confusion pattern (Musicians case). A separate check on high-r26 occupations — where the scoring concern is "this r26 looks implausibly high" — needed its own pass.

Phase 11 launched a focused GPT audit scoped to 156 high-r26 occupations and 1,658 tasks.

**What it caught.** **272 vector reclassifications + 21 difficulty recalibrations** across 278 findings. Systematic patterns: retail / public-facing sales (5223, 9520, 5243) treated as C_R when the task text described body-at-counter work → Phi_U; field-service route work (9623 meter readers, vending collectors) hidden as routine records → Phi_S for the route + Phi_U for site repair; driving instruction (5165) as C_G with "students under actual driving conditions" → student-in-loop Phi_S/Phi_U; early childhood education (2342) as C_G with "tools and equipment, prevent injuries, motor skills, playground" → Phi_U; foundry/craft over-structured as P_A ("molten metal, hand tools, open dies") → Phi_U; prison governors (1349-prison) as C_G → S_E; chef work (3434) as C_R / C_G → Phi_U (hands-on) and S_E (kitchen operations).

**Most common vector movements:** C_R → Phi_U (78), C_G → Phi_U (61), C_R → P_A (29), P_A → Phi_U (27), C_G → S_E (25).

**Downstream consequence.** Intervention C drove the largest per-occupation r26 movers in the v3.2 → v5 diff: Metal moulders 85 → 8, Shop Salespersons 87 → 30 (moved again later by Audit 3), Air traffic controllers 70 → 18.

### Intervention D — Capability vector recalibration

**What went wrong.** Phase 5's blind calibration produced benchmark-dense, well-justified 2026 capability values. But the reviewer's concern at the pre-ship checkpoint was specific: benchmarks systematically over-state production capability, and Phase 5 did not apply sufficient discount for four known benchmark-to-deployment divergences:
1. Remote-operator safety nets backing demo-scale autonomous systems (Waymo fleet response, Amazon warehouse human backstops).
2. LLM confident-failure modes in production (~10–15% confidently-wrong outputs on real-world queries).
3. Agentic brittleness — multi-step agents degrade on long horizons (Devin/Composer production ~50% vs GAIA 0.75).
4. Narrow operational-design domains (Waymo's 5 metros, Figure's single BMW plant) that do not transfer to the full workforce.

**What was done.** Two independent recalibrators — Claude Opus 4.7 (1M context) and GPT 5.4 — each ran a benchmark-to-deployment honest lens, blind to each other's output, using the same Phase 5 benchmark citations as fixed input. The question they were asked: what does each benchmark number translate to in production-reliability terms?

**Convergence was tight.**

| Vector | Phase 5 | Opus recalib | GPT recalib | Shipped | Δ vs Phase 5 |
|:---|---:|---:|---:|---:|---:|
| C_R | 0.87 | 0.75 | 0.76 | **0.76** | −0.11 |
| C_G | 0.62 | 0.55 | 0.58 | **0.57** | −0.05 |
| P_A | 0.78 | 0.73 | 0.78 | **0.75** | −0.03 |
| Phi_S | 0.60 | 0.45 | 0.46 | **0.46** | −0.14 |
| Phi_U | 0.15 | 0.15 | 0.15 | **0.15** | 0.00 |
| S_E | 0.42 | 0.35 | 0.34 | **0.35** | −0.07 |

Both recalibrators landed within ±0.03 of each other on every vector. The shipping set takes the blended midpoint.

**Per-vector reasoning (condensed).** C_R (0.76): AEI shows top occupations reach ~75% observed coverage; 10–15% confident-failure rate caps unsupervised substitution. C_G (0.57): 2026 legal / consulting / medical deployment is augmentation, not replacement. P_A (0.75): IFR counts are actual installations; small adjustment for global-weighted density. Phi_S (0.46, largest correction): remote-operator backstops on every robotaxi deployment; Waymo's 5 metros don't transfer; Amazon Vulcan asks humans to tag in ~25%. Phi_U (0.15): defended unchanged — no scaled commercial deployment for home-care, surgery, plumbing, firefighting. S_E (0.35): Devin/Composer ~50% production completion vs GAIA 0.75; zero multi-stakeholder autonomous deployment; ARC-AGI-3 at 0.004.

**Cross-vector sanity.** Orderings preserved: C_R > P_A > C_G > Phi_S > S_E > Phi_U. All deltas ≤ 0. Largest Phi_S (−0.14). Post-recalibration values recorded in `metadata.capability_vectors_2026_snapshot`. Phase 11 applied a parallel shift through Phase 7 trajectories; 2041 mid-band anchors stayed aggressive because capability curves saturate past task thresholds — honest task-math, not calibration artifact.

### Intervention E — Twenty-occupation sanity check with Lukas + dataset-wide sweep

**What went wrong.** Interventions A through D addressed systemic issues identified from the outside (reviewer concerns + architect-audited corpora). A final pre-ship sanity check surfaced a different class of problem: per-occupation data defects that had not been caught by any systematic filter because they were idiosyncratic.

**What was done.** The reviewer walked through 20 occupations in a batch-by-batch review. Per-occupation findings:
- **Task-level corrections (12+).** Scrape artifacts still remaining after Audit 1's threshold, ISCO definitions mislabelled as tasks, sentence fragments, wrong vector assignments on specific tasks. Each found and applied inline.
- **Wrong barrier notes.** Example surfaced: Insurance Salespeople (3321) carrying a trades-style barrier note — clear wrong-occupation metadata. Corrected inline.
- **Dataset-wide sweep triggered by the sanity check.** The batch review identified residual scrape-pattern strings that hadn't appeared in Audit 1's regex catalog. A targeted sweep caught **12 more scrape / descriptive entries across 11 additional occupations**, removed with pre/post validation.

**Why this intervention matters.** Audits 1 and 2 caught classes of error that recur across the corpus. Intervention E caught the residue — idiosyncratic contamination that only human editorial reading surfaces. The broader lesson is that adversarial automation is necessary but not sufficient; a final human editorial pass catches things the automated audits miss.

### Audit 3 — Territorial deep-review round (13 auditors + 2 adversarial QC)

**What went wrong.** Intervention E concluded with the reviewer's observation that interventions to date had improved the dataset but had not been deep enough on per-territory domain expertise — "the task-level calibration shows no sophisticated understanding of how difficult some of these tasks are for machines and robots respectively." The architect launched a 13-territory deep-review pass in response.

**Setup.** One auditor per modern territory (16–75 occupations each). Each auditor was web-enabled with a brief to spend 30–60 minutes on domain research before reviewing tasks — what occupations actually do in 2026, where AI/robotics is deployed, deployment evidence (Waymo, Figure, UiPath, Cursor, Hadrian X, SAM100, Chef Robotics, Lely, BeeHero). Seven Opus 4.7 auditors, six GPT-5 Codex.

**Outputs.** **1,166 findings**: 299 removes / 736 vector changes / 470 difficulty changes (with overlap) + 60 barrier-note issues. Flag rate ranged from 0.126 (making_meaning, Opus) to 0.393 (buying_selling, GPT) — a 3× spread split cleanly along model lines (every Opus auditor below 21%; every GPT auditor at 24%+). The same model-driven aggressiveness pattern observed in Audit 1, at higher absolute rates because the per-territory brief drove deeper engagement.

**Adversarial QC.** Two reviewers (Opus 4.7 + GPT) cross-checked the 13 territorial findings via stratified sampling — not re-auditing from scratch. Approve rate ~94% in samples (audits defensible). Reject rate ~2% on over-reach (`maintaining_fixing 7421[6]` Phi_S → C_R for ground-support test equipment under-weighted the physical-setup component). Land_sea and maintaining_fixing auditors submitted all findings as HIGH confidence — over-confident for batches that size. Care_health had 76 vector findings with empty `difficulty_rationale` on implicit second-order difficulty changes. QC identified ~18 missed issues — fragments and contamination even the deep review didn't catch.

**Applied with QC filtering:** 7 QC-rejected findings dropped; 78 empty-rationale difficulty changes skipped (vector applied alone); 2 "difficulty → 0.00" learning_teaching findings re-interpreted as REMOVE; 15 QC-identified missed issues applied additively (2641 and 2641-copywriter fragment removes, blueprint-reading Phi_U → C_G propagation, cross-occupation contamination removal on 3256-ems and 8142). **Net applied: 729 vector reclassifications, 557 difficulty recalibrations, 299 task removals.** Task count: 5,155 → 4,830.

**Strongest single finding.** Air Traffic Controllers (3154): 11 of 12 tasks mis-categorized as Phi_S when ATC is the framework's canonical S_E example. That finding alone re-anchored a display occupation from r26 = 70 (v3.2) to r26 = 22 (v5 current).

**Barrier-note contamination caught at the metadata layer.** 60 barrier-note issues flagged; at least 50 were unambiguous wrong-occupation copy-pastes — 2164 Urban Planners had an architect's "professional seal" note; 3118 Draughtspersons (CAD work) was tagged HUMANOID_DEPENDENT with a humanoid-manipulation note; 5161 Astrologers had a pet-groomer note; 3431 Photographers had a financial-advisor fiduciary note. Evidence that the upstream barrier-note generator was pooling across occupations. Queued for v5.1 rather than auto-substituted.

---

## Why these interventions matter

Each intervention caught a systemic issue that could have shipped undetected. **A** caught an editorial conflation that would have made the methodology page internally inconsistent with the shipping scores. **B** caught scrape artifacts and vector mis-classifications that Phase 4's 3-way reconciliation (84.2% agreement) had buried in the 15.8% residual — plus contamination sitting below the anti-fabrication gates. **C** caught a different systemic error — physical/embodied work mis-vectored as cognitive — that the first audit under-sampled. **D** caught the benchmark-vs-deployment gap that Phase 5's blind calibration under-discounted; two independent instances converged within ±0.03 on every vector, which is strong evidence the gap is real. **E** caught idiosyncratic contamination that recurs-across-corpus filters miss. **Audit 3** caught per-territory domain subtlety — ATC as S_E not Phi_S, blueprint-reading as C_G not Phi_U, embedded industry context (Sweetgreen Infinite Kitchens, Chef Robotics 100M servings, Lely 50K robots) that only 30–60 minutes of domain research surfaces.

**The pattern across all six.** Systemic quality issues that each would have escaped if any earlier phase had been the final gate. Phase 4 anti-fabrication gates caught template slop but not plausible-looking scrape artifacts. Phase 5 scorers applied the calibrator definitions but could not audit the input task decompositions. Phase 10's adversarial validator had structural and content checks but not task-level vector audits. The multi-audit + dual-recalibrator + deep-review pattern at Phase 11 was the last-mile safety net. This is the reason the project uses adversarial multi-instance separation: single-model agreement is cheap; cross-model + cross-lens agreement at each stage is the safety net — and the Phase 11 interventions demonstrate that even that safety net needs multiple editorial-judgment passes at the final stage, because systemic issues hide in the space between checks.

---

## Shape of the final dataset

**Distribution.** Mean r26 = 45.01 (v3.2 was 58.24). 25 occupations at r26 = 100 (clerical + fully-automated industrial). r40 mid: 88.1% at 100, 5.2% at 90–99, 3.5% at 80–89. Mean displacement_2040_moderate = 27.27 (v3.2 was 37.97). Mean r26 low/high spread 38.8 pp, median 34 pp (wider on creative and unstructured-physical work where honest uncertainty is larger).

**Territory means (r26 mid).** Highest: Making Things 68.7, Money & Data 68.5, Buying & Selling 63.7, Learning & Teaching 54.5. Lowest: Land & Sea 21.9, Building Things 23.0, Maintaining & Fixing 23.3. The ordering reflects Phase 4 task distribution × recalibrated capability vectors: cognitive-heavy territories score higher in 2026, physical/embodied territories lower.

**What r26 = 100 means.** The 25 occupations at r26 = 100 are mostly clerical + fully-automated industrial: glass & ceramics plant ops (8181), sewing machine operators (8153), packing and bottling machine operators (8183), metal finishing / plating (8122), paper and plastic products operators (8142/8143), statistical and payroll clerks (4312/4313), data entry clerks (4132), filing clerks (4415), general office clerks (4110), secretaries (4120), bank tellers (4211), hotel receptionists (4224), government licensing officials (3354), plant controllers (3133/3134). The interpretation is "under 2026 capability, the task math says these occupations' work profiles can be handled" — not "these jobs vanish tomorrow." Displacement is the workforce-implications column.

**r40 saturation under moderate.** 424/480 occupations reach replaceability 100 by 2041 mid. This is honest task-math under capability saturation, not a projection artifact. Displacement carries the variance: 9.3% to 47.9% across occupations, mean 27.27%. The 47.9% high end is NONE-barrier routine-cognitive work; the 9.3% low end is REGULATORY / HUMANOID_DEPENDENT-barrier occupations where the lag multiplier keeps most work with licensed humans or gates displacement on humanoid readiness.

---

## Known limitations acknowledged in the final ship

From `editorial_overrides_queue.md` plus process concerns surfaced across the six Phase 11 interventions:

1. **ISCO 5245 Service Station Staff** — r26 = 44 with HUMANOID_DEPENDENT barrier, but self-service fuel pumping is universal outside NJ/OR. Low score appears to be a Phase 4 task-decomposition artifact; proposed override r26 → ~88 with REGULATORY barrier. Deferred to v5.1.
2. **REGULATORY-barrier occupations with r41 ≥ 95** (Lawyers, Senior Government Officials, Judges). Licensing regimes unlikely to fully dissolve by 2041. The multiplicative barrier model probably needs a floor component for regulatory frictions. Deferred to v5.1.
3. **Residual scrape artifacts below audit consensus.** Audits 1 and 3 used 2-model consensus as the acceptance bar; below-threshold contamination probably remains.
4. **Phase 4 task-classification ceiling.** 15.8% three-way-split tasks were defaulted to Codex v3 without human adjudication. Audits 2 and 3 sampled; exhaustive per-split human adjudication was not performed.
5. **Barrier-note wrong-occupation contamination.** Audit 3's 60 barrier-note issues are queued but not rewritten inline (avoiding a second template-slop-risk rewrite round).
6. **Within-vector heterogeneity persists.** C_G, Phi_S, S_E each cover wide internal distributions. A v6 vector split would add precision.
7. **Benchmark-to-deployment lens evolves.** Production reliability data for humanoid robotics, agentic systems, and autonomous vehicles is still developing; values may shift in v5.1/v6.
8. **G&P hybrid data model.** ILOSTAT occupation-up for majors 1–9 + WB/IISS for major 0. G&P 2023 ~70M is below the ISIC-O benchmark of ~206M — expected under occupation-up, as v5 routes non-military public admin work to other territories (health ministry → C&H, education ministry → L&T).
9. **Audit 3 over-confidence signals.** Land_sea and maintaining_fixing auditors marked all findings HIGH-confidence; the architect's apply script preserved the HIGH/MEDIUM distinction via per-finding spot-checks rather than downgrading labels.

---

## What future versions should address

Highest-value v6 improvements, derived from the Phase 11 process:

1. **Phase 4 re-run with stronger anti-scrape guardrails.** Blocklist of known-bad strings from the Phase 11 audits; tail-position stricter plausibility checks (indices 8–13, where cross-domain contamination clustered); cross-domain dedup (flag task text recurring across 3+ unrelated occupations); ISCO-descriptor detection.
2. **Calibrator brief default: benchmark-to-deployment honest lens.** Bake in from day one: for each benchmark citation, (a) AI-only or AI + human-operator composite? (b) full vector or narrow slice? (c) fraction of the target workforce in the deployment ODD?
3. **Floor-adjusted barrier model for REGULATORY.** The multiplicative form produces counterintuitive results at high r26 × REGULATORY (lawyers r41 = 100). Add a floor: hard minimum retained human share that doesn't soften further with capability.
4. **Vector split for C_G, Phi_S, S_E.** Each covers too-wide a distribution. Candidate splits: C_G specialist-QA vs novel-reasoning; Phi_S structured-ODD vs long-tail; S_E coding-agent vs multi-stakeholder orchestration.
5. **Phase 11-scale audit built into Phase 4 CI.** The four-instance adversarial + focused-audit + territorial-deep-review pattern should be a standard Phase 4 step, not an emergency Phase 11 intervention. Include per-task human adjudication budget for the three-way-split residual.
6. **Service-station kiosks as a reference case.** Low r26 + HUMANOID_DEPENDENT + real-world widespread self-service = candidate for reclassification to P_A or Phi_S. Test this pattern explicitly; same for parking attendants, toll collectors, ticket sellers.
7. **Barrier-note generation rigor parity with Phase 8 v2.** Audit 3's 60 barrier-note issues (pet-groomer note on Astrologers, architect note on Urban Planners) show the v1 editor's wrong-occupation failure mode was not fully contained by the targeted rerun. v6 should apply the banned-openings + mandatory-evidence + 0.80 near-dup discipline to ALL barrier notes from the first pass.
8. **Residual-risk logging standardized.** Phase 1 modelled this well; not every phase adopted. v6 should standardize: every checkpoint ends with a "residual risks not closed" table plus a go/no-go on whether to close before release.
9. **Differentiate auditor-model aggressiveness.** Audit 3 showed a clean 3× flag-rate split between Opus (conservative) and GPT (aggressive) auditors. Future briefs should include calibration examples spanning the conservative/aggressive axis.

---

*End of editorial process record. Total build window 2026-04-11 → 2026-04-19. Total Phase 11 window 2026-04-18 → 2026-04-19, containing five emergency interventions (A through E) plus the 13-territory Audit 3 deep-review round with adversarial QC. Release date 2026-04-19.*
