# Evidence Ledger — 2026 H2

**Standing evidence base for the Large Labor Model (largelabormodel.com).**
Compiled: **2026-08-15**. All URLs retrieved/accessed 2026-08-15 unless noted.
Purpose: the curated, dated registry that the **Q1 2027 annual recalibration** starts from. This is forward infrastructure — it records readings and tripwires; it does not re-audit the 2026 anchors (set April 2026; August 15, 2026 defensibility audit: all six HOLD).

## How to read this ledger

- **Vectors**: C_R (routine cognitive), C_G (generative cognitive), P_A (physical automation), Phi_S (selective physical / structured), Phi_U (unstructured physical), S_E (system engineering / orchestration). All are production-reliability quantities under the honest-deployment lens (discount benchmark performance for operator backstops, narrow domains, confident failure, pilot-vs-scale gaps).
- **[VERIFIED]** = the number was retrieved on the compile date from the named source page (primary org page, leaderboard, official data file, or a full-text fetch of a named article).
- **[REPORTED]** = retrieved on the compile date but only via a single secondary source or a search-result snippet; treat as provisional until re-verified.
- **[INTERNAL]** = pre-2026 training knowledge used **only for historical series points**, never for a latest reading; re-verify before load-bearing use.
- **Tripwire** = the one concrete reading that should trigger re-opening an anchor at (or before) the Q1 2027 recalibration. It is the only forward-looking line per family.
- Where sources disagree, the discrepancy is recorded rather than resolved.

## Family index

| # | Family | Informs | Latest headline reading (date) |
|---|--------|---------|-------------------------------|
| F1 | METR time horizons | S_E, C_G | 50% horizon ≈ 17.4 h, Claude Mythos Preview early ckpt (2026-04) |
| F2 | GDPval / GDPval-AA | C_G | Leader Elo 1,849 vs human 1,000 (2026-07/08) |
| F3 | SWE-bench Pro | C_R, C_G | 61.5% public set, Muse Spark 1.1 (2026-08 board) |
| F4 | OSWorld computer use | C_R | 85–86% vs human baseline 72.36% (2026-06/08) |
| F5 | Anthropic Economic Index | replacement calibration | API directive share 38.1%→29.4% (Nov'25→Feb'26) |
| F6 | IFR World Robotics | P_A | 542,000 installs 2024; stock 4.664 M (rel. 2025-09) |
| F7 | Robotaxi & driverless | Phi_S | Waymo ≈500 k paid rides/wk (2026-03; ~same 2026-07) |
| F8 | Commercial humanoid fleet | Phi_U | Milestones verified; audited unit counts: none published |
| F9 | Frontier model releases | C_G, C_R | Claude 5 family GA 2026-06-09; GPT-5.6 2026-07-09; Grok 4.6 2026-08-12 |
| F10 | Enterprise adoption cross-sections | replacement calibration, C_R | BTOS national AI use 19.8% (2026-05-03) |
| F11 | Remote Labor Index (added) | C_G, replacement calibration | 15.8% automation rate, Fable 5 (2026-07) |
| F12 | Warehouse & logistics fleets (added) | P_A, Phi_S | Amazon >1 M robots cumulative; Symbotic backlog >$5 B (2026) |

---

## F1. METR long-horizon task benchmark (time-horizon series)

**Measures:** the human-expert task duration at which a frontier agent succeeds with 50% (and 80%) reliability on diverse software/agentic tasks. **Informs: S_E, C_G.**

**Latest readings** — from METR's canonical Time Horizon 1.1 data file `benchmark_results_1_1.yaml` (raw values in seconds; unit cross-checked against published figures: o3 = 7,184 s ≈ 120 min vs METR's published 121 min; Claude 3.7 Sonnet = 3,623 s ≈ 60 min vs published ~59–60 min):

- **Claude Mythos Preview (early checkpoint, 2026-04-07): 62,687 s ≈ 17.4 h** — current frontier point in the file. [VERIFIED] https://metr.org/assets/benchmark_results_1_1.yaml
- **Claude Opus 4.6 (2026-02-05): 43,128 s ≈ 12.0 h** — highest generally-available model in the file. [VERIFIED] (same file)
- Gemini 3.1 Pro (2026-02-19): ≈ 6.4 h; GPT-5.4 (2026-03-05): ≈ 5.7 h; GPT-5.3-Codex (2026-02-05): ≈ 5.8 h. [VERIFIED] (same file)
- Doubling time: ≈ 7 months long-run (196-day hybrid TH1.0/1.1 trend); **131 days for post-2023 models under TH1.1** ("20% more rapid" than previously measured). [VERIFIED] https://metr.org/blog/2026-1-29-time-horizon-1-1/
- Landing page last updated 2026-05-08; TH1.1 = 228 tasks on Inspect framework (up from 170 on Vivaria). [VERIFIED] https://metr.org/time-horizons/ ; methodology sensitivity discussion (regularization fix) [REPORTED] https://metr.substack.com/p/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results

**Series (50% horizon, TH1.1 file, all [VERIFIED] from the YAML):**

| Date | Model | 50% horizon |
|------|-------|-------------|
| 2024-06 | Claude 3.5 Sonnet | ≈ 11.4 min |
| 2024-12 | o1 | ≈ 38.8 min |
| 2025-02 | Claude 3.7 Sonnet | ≈ 60 min |
| 2025-04 | o3 | ≈ 2.0 h |
| 2025-08 | GPT-5 | ≈ 3.4 h |
| 2025-11 | Claude Opus 4.5 | ≈ 4.9 h |
| 2025-12 | GPT-5.2 | ≈ 5.9 h |
| 2026-02 | Claude Opus 4.6 | ≈ 12.0 h |
| 2026-04 | Claude Mythos Preview (early) | ≈ 17.4 h |

(GPT-4 ≈ 5 min in 2023 per the original paper, https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/ [INTERNAL — paper value, not re-extracted].) Note: **no published horizon yet for the current GA frontier (Claude Fable 5 / Opus 5, GPT-5.6)** — file ends at the April 2026 preview checkpoint. Adjacent: METR Frontier Risk Report, Feb–Mar 2026 window, published 2026-05-19: https://metr.org/blog/2026-05-19-frontier-risk-report/ [VERIFIED as existing; values not extracted].

**Reliability caveat:** 50%-reliability horizons on clean, auto-scorable software tasks; only 5 of 31 long tasks have measured human baselines, results are sensitive to task composition and regularization choices, and 80%-reliability horizons (the deployment-relevant number) are materially shorter than the 50% headline.

**Tripwire:** a **generally available** model posts a TH1.1 50% horizon ≥ 40 h (one work-week) — or two consecutive frontier points imply a sustained doubling time < 4 months → re-open S_E (and C_G high).

---

## F2. GDPval / GDPval-AA (real-work deliverables vs human experts)

**Measures:** blind expert/judge preference for AI-produced real occupational deliverables (documents, spreadsheets, slides, CAD, media) vs human professionals; GDPval-AA is Artificial Analysis's independently run agentic version scored as Elo with **human experts anchored at 1,000**. **Informs: C_G.**

**Latest readings (GDPval-AA v2, snapshot current to Jul 2026 with some Aug 2026 entries; 220 tasks, agentic environments with shell + web):** [VERIFIED] https://artificialanalysis.ai/evaluations/gdpval-aa

- **Claude Opus 5 (adaptive reasoning, max effort): 1,849 Elo** (leader)
- Claude Opus 5 (xhigh): 1,817 · Grok 4.6 (high): 1,746 · **Claude Fable 5 (max, Opus 4.8 fallback): 1,739** · **Qwen3.8 Max: 1,737** (top open-weights-lineage entry; weights not yet shipped — see F9) · GPT-5.6 Sol (max): 1,725 · Qwen3.8 2.4T A95B: 1,720
- Elo 1,849 vs 1,000 ⇒ the leader's deliverable is preferred over the human expert's in the large majority of blind pairings (Elo-implied ≈ 99%; judge = LLM, see caveat).
- A search-snapshot from Aug 2026 shows slightly different values (Opus 5 1,861; Fable 5 1,747; GPT-5.6 Sol 1,736) — board moves between snapshots. [REPORTED] https://airank.dev/benchmarks/gdpval-aa-elo

**Series:**
- 2025-09-25 — GDPval launch (OpenAI; 44 occupations, 1,320 tasks, blinded expert grading): best model **Claude Opus 4.1 ≈ 47.6–49% wins+ties vs experts; GPT-5-high ≈ 40.6%** — secondary sources differ by a point or two; OpenAI's page returned HTTP 403 on compile date. [REPORTED] https://eu.36kr.com/en/p/3482873494740096 ; https://techcrunch.com/2025/09/25/openai-says-gpt-5-stacks-up-to-humans-in-a-wide-range-of-jobs/ ; paper https://arxiv.org/abs/2510.04374
- 2025-12/2026-01 — Claude Opus 4.8 reported as GDPval-AA leader over GPT-5.5. [REPORTED] https://officechai.com/ai/claude-opus-4-8-beats-gpt-5-5-on-gdpval-aa-benchmark-for-real-world-tasks/
- 2026-07/08 — leader 1,849 [VERIFIED above]. Adjacent instrument: **AA-Briefcase** (Artificial Analysis private long-horizon agentic knowledge-work Elo) — Grok 4.6 debuts at 1,577, behind Claude Opus 5. [REPORTED] https://datanorth.ai/news/xai-releases-grok-4-6

**Reliability caveat:** one-shot deliverables graded by preference (v2 judge is an LLM), with no client iteration, accountability, or consequence-of-error — preference-Elo above 1,000 is not evidence the work could ship unattended (contrast F11: same genre of work, 15.8% end-to-end acceptance).

**Tripwire:** GDPval-AA leader ≥ 1,900 Elo **held by a generally available model**, or an actually-downloadable open-weights model within 50 Elo of the leader → re-open C_G mid/high (and the commercial-availability term).

---

## F3. SWE-bench Pro (standardized agentic coding)

**Measures:** resolved rate on contamination-guarded, harder real-repo software engineering tasks under Scale's standardized harness (public set: 731 instances; Go/Python/JS/TS). **Informs: C_R, C_G.**

**Latest readings (Scale public leaderboard):** [VERIFIED] https://labs.scale.com/leaderboard/swe_bench_pro_public

- **Muse Spark 1.1: 61.50%** (leader, marked NEW) · GPT-5.4 (xHigh): 59.10% · Muse Spark: 55.00% · Claude Opus 4.6 (thinking): 51.90% · Gemini 3.1 Pro (thinking): 46.10% · Claude Opus 4.5: 45.89% · Claude Sonnet 4.5: 43.60% · GPT-5 (2025-08-07, high): 41.78%
- Commercial (private) set: Claude Opus 4.6 reported at 47.1%. [REPORTED] https://codeant.ai/blogs/swe-bench-scores
- Vendor-reported SWE-bench-Pro-style numbers run far higher (Claude Fable 5 / Mythos 5 80.3%, Opus 5 79.2%, as of 2026-08-06 aggregates) — **~19-point spread vs the standardized harness**; treat vendor numbers as a different instrument. [REPORTED] https://codingfleet.com/blog/swe-bench-pro-leaderboard-2026/
- Adjacent (open-weights, shared-harness agentic coding): Terminal-Bench 2.1 — DeepSeek V4 Flash 0731: 82.7 vs GLM 5.2: 81.0; DeepSWE — 54.4 vs 46.2. [VERIFIED] https://a2aprotocol.ai/insights/qwen-38-max-vs-glm-52-vs-kimi-k3-vs-deepseek-v4-flash

**Series (public set, Scale harness):**
- 2025-09 launch: best models ≈ 23% (GPT-5 23.3%, Claude Opus 4.1 ≈ 23%). [INTERNAL — launch coverage; note the same GPT-5 checkpoint now posts 41.78% on the current board, i.e. harness/scaffold updates moved historical scores]
- 2026-02: Opus 4.6 51.9% [VERIFIED above] → 2026-08 board: 61.5% leader [VERIFIED above].

**Reliability caveat:** resolved-rate on self-contained issues with green-test oracles — no ambiguous requirements, code review, or production blast radius, and scores are strongly harness-sensitive (same model varies up to ~20 points across scaffolds).

**Tripwire:** ≥ 75% on Scale's standardized public set by a generally available model (or ≥ 65% on the commercial set) → re-open C_R mid/high and C_G mid.

---

## F4. OSWorld / computer-use reliability

**Measures:** end-to-end success on 369 real desktop/web tasks (file management, multi-app workflows, real applications, terminal) — OSWorld-Verified = standardized re-runs. Human baseline 72.36%. **Informs: C_R.**

**Latest readings:** [VERIFIED] https://leaderboard.steel.dev/leaderboards/osworld/

- **Claude Mythos Preview: 85.4%** · **Claude Mythos 5: 85.0%** · **Claude Fable 5: 85.0%** (Jun 2026, OSWorld-Verified) · Claude Opus 4.8: 83.4% (May 2026) · Claude Sonnet 5: 81.2% · Claude Sonnet 4.6: 78.5% · OSAgent (TheAGI Co.): 76.26% (Oct 2025, self-reported) · GPT-5.4: 75.0% (Mar 2026, self-reported)
- **Qwen3.8 Max reported at 86.1%** atop an Aug-14-2026 snapshot of OSWorld-Verified. [REPORTED] https://benchlm.ai/benchmarks/osworld-verified
- Frontier is now **12–14 points above the published human baseline** (72.36%).

**Series:** 2024 launch: best agents ≈ 12% (paper) [INTERNAL] · Claude Sonnet 4.5: 61.4% (2025-09) [VERIFIED, same board] · Claude Opus 4.5: 66.3% (2025-11) [VERIFIED, same board] · Claude Sonnet 4.6: 72.5% at release (2026-02) [REPORTED] https://coasty.ai/blog/osworld-benchmark-2026-computer-use-results · 85–86% (2026-06/08) [VERIFIED above].

**Reliability caveat:** short, well-specified tasks in sandboxed VMs with programmatic checkers — "above human baseline" here does not include interruption recovery, credential/permission friction, ambiguous instructions, or the long-tail app zoo of real enterprise desktops.

**Tripwire:** ≥ 95% OSWorld-Verified, **or** any credible enterprise study showing > 90% unattended completion of multi-app back-office workflows at production scale → re-open C_R mid/high.

---

## F5. Anthropic Economic Index (Cadences + Learning Curves)

**Measures:** how Claude is actually used across the economy (privacy-preserving conversation classification): automation (directive + feedback loop) vs augmentation (validation + task iteration + learning), task mix, concentration. **Informs: replacement-formula calibration (automation-share term).**

**Latest readings:**

- **"Learning curves"** (published 2026-03-24; data Feb 5–12, 2026 vs Nov 2025): **1P API directive share fell 38.1% → 29.4% (−8.7 pp)**; feedback-loop 11.7% → 12.1%; text states automation "decreased sharply" in 1P API while **augmentation on Claude.ai increased slightly** (chart labels ≈ 55% augmentation both periods); top-10 tasks = 19% of Claude.ai traffic (down from 24% in Nov); Management-occupation tasks 3% → 5%. Emerging ≥2x-growth automated workflows: business sales & outreach automation; automated trading & market ops. [VERIFIED — PDF text extraction] https://humanreadiness.org/pdfs/learning-curves.pdf (mirror of https://www.anthropic.com/research/economic-index-march-2026-report)
- **"Cadences"** (June-2026 report; artifacts chapter data Apr 10 – Jun 10, 2026): no single platform-wide automation share published; work share and Claude Code share both positively correlate with automation, Claude Code sessions are on average more automated than chat or Cowork; most common artifacts: explanations 17%, documents/reports 15%, guidance 11%. AEI Survey instrument launched Apr 2026. [VERIFIED] https://www.anthropic.com/research/economic-index-june-2026-report

**Series:** Dec 2024–Jan 2025 (first AEI report): ≈ 57% augmentation / 43% automation on Claude.ai [INTERNAL; echoed in secondary coverage] · Aug–Sep 2025 report: Claude.ai directive share ≈ 39% (up from ≈ 27%), API traffic much more automation-leaning [INTERNAL] · Feb 2026: API directive 29.4% [VERIFIED above] · Apr–Jun 2026: correlational readings only [VERIFIED above].

**Reliability caveat:** measures one vendor's traffic mix (composition shifts, new surfaces like Cowork/Claude Code, and enterprise-API opacity move the shares), and "directive conversation" ≠ completed unattended work product.

**Tripwire:** automation share (directive + feedback loop) exceeds 50% on Claude.ai in two consecutive AEI reports, **or** 1P API directive share reverses and clears 60% → re-open the replacement-formula automation-share calibration (and C_R mid).

---

## F6. IFR World Robotics (industrial robot installations / density)

**Measures:** audited global industrial-robot annual installations, operational stock, and robot density per 10,000 manufacturing employees. **Informs: P_A.**

**Latest readings (World Robotics 2025, released 2025-09-25 — 2024 data; next edition expected ~Sep 2026):** [VERIFIED] https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years

- **2024 installations: 542,000 units** (4th straight year > 500k; ~2x the level of 10 years prior)
- **Operational stock: 4,664,000 units (+9% YoY)**
- Regional: Asia 74% of new deployments · Europe 16% · Americas 9%; **China 295,000 units = 54% of world**
- IFR forecast: **575,000 installs in 2025 (+6%); 700,000-unit mark surpassed by 2028**
- Density (2024, release 2026-04-08): **world average 132 robots/10k employees**; Korea 1,220 · Singapore 818 · Germany 449 · Japan 446 · US 307 · China 166 (rank 22, +17% YoY, stock ≈ 2 M ≈ 4.5x Japan); Western Europe 267, North America 204, Asia 131. [VERIFIED] https://ifr.org/ifr-press-releases/news/robot-density-surges-in-europe-asia-and-americas

**Series (installations):** 2023: ≈ 541,000 [INTERNAL — WR2024] · 2024: 542,000 [VERIFIED] · 2025F: 575,000 [VERIFIED forecast]. Density figures are not reliably comparable across editions (employment-denominator revisions) — treat density as a within-edition cross-section, not a time series.

**Reliability caveat:** counts shipped/installed arms, not utilization or task breadth — a flat-to-slow installations series co-exists with rising capability per robot (vision, force control, easier programming), so this family bounds P_A's *scale* term more than its capability term.

**Tripwire:** annual installations > 700,000 before the 2028 forecast date, or operational stock > 6.0 M, or China density entering the global top 10 → re-open P_A mid (scale/diffusion term).

---

## F7. Robotaxi & driverless scale

**Measures:** paid, rider-only autonomous service volume and geographic/regulatory breadth — the cleanest live gauge of structured-environment physical autonomy at commercial scale. **Informs: Phi_S.**

**Latest readings:**

- **Waymo: ≈ 500,000 paid rides/week (2026-03), 10 U.S. metros, fleet ≈ 3,067 (Dec 2025) — "tenfold in under two years" on a roughly flat fleet (utilization gains).** [VERIFIED] https://techcrunch.com/2026/03/27/waymo-skyrocketing-ridership-in-one-chart/
- 2026-07-08: still ≈ 500k rides/week; four more cities announced (San Diego, Las Vegas, Tampa, Denver); stated aim **1,000,000 rides/week before end of 2026**. [REPORTED] https://spacedaily.com/m-on-july-8-2026-waymo-announced-fully-driverless-taxis-for-four-more-american-cities-its-fleet-now-giving-about-half-a-million-rides-a-week-and-aiming-for-a-million-a-week-before-the-year-is-out/ ; target also per [REPORTED] https://www.forbes.com/sites/alanohnsman/2025/12/10/waymo-targets-1-million-robotaxi-rides-a-week/ and [VERIFIED] https://insideevs.com/news/788284/waymo-expansion-tesla-cities-2026/ (which adds: end-2025 ≈ 400k/week across six metros; ≥ 20 cities worldwide planned; London first international market)
- Freeway operations enabled Phoenix/SF/LA at up to 65 mph, Nov 2025. [REPORTED] search-verified multiple sources (e.g., https://www.hostextraordinaires.com/post/waymo-automated-rides-rollout-status-2026)
- **Aurora (driver-out trucking):** > 250,000 incident-free driverless miles since Apr 2025 launch; network tripled to **10 routes** across TX/NM/AZ (Dallas–Houston, Fort Worth–El Paso, El Paso–Phoenix, Fort Worth–Phoenix ~1,000 mi, Laredo–Dallas); target **200+ trucks by end-2026**; second-gen hardware intended to remove the partner-requested observer. [REPORTED] https://nationaltoday.com/us/tx/dallas/news/2026/03/05/aurora-innovation-touts-250k-incident-free-driverless-miles-targets-200-trucks-in-2026/ ; https://www.truckinginfo.com/news/aurora-adds-1000-mile-driverless-run-from-fort-worth-to-phoenix
- **Tesla robotaxi:** unsupervised (monitor-out, chase-car phase) began Austin 2026-01-22/23 with 1 vehicle → ~8 (Feb) → ~20–30 active (Jun 2026), 42–44 registered in TX; Austin-metro-wide map; small supervised deployments Dallas/Houston; 19% availability measured at 8 months in. [REPORTED] https://www.benzinga.com/markets/prediction-markets/26/06/53004232/tesla-removes-robotaxi-safety-monitors-and-widens-austin-map-but-fleet-shrinks-to-20-cars ; https://www.electrive.com/2026/06/02/tesla-robotaxi-fleet-in-texas-reaches-only-42-vehicles/ ; https://electrek.co/2026/02/16/tesla-robotaxi-status-check-8-months-in/ ; [VERIFIED] Tesla comparison figures in the insideevs piece above.

**Series (Waymo weekly paid rides):** 50k (May 2024) [VERIFIED, TechCrunch chart] · 100k (Aug 2024) [VERIFIED] https://techcrunch.com/2024/08/20/waymo-is-now-giving-100000-robotaxi-rides-week · 250k (Apr 2025) [INTERNAL] · ≈ 400k (end 2025) [VERIFIED, insideevs] · ≈ 500k (Mar–Jul 2026) [VERIFIED above].

**Reliability caveat:** geofenced ODDs with remote-assistance backstops and curated weather/road exposure; ride counts prove commercial reliability *inside the fence*, not generalization beyond it (and Tesla's "unsupervised" still runs chase-car/monitor hybrids at two-digit fleet scale).

**Tripwire:** Waymo sustains ≥ 1 M paid rides/week, or rider-only service operates in ≥ 25 U.S. metros across ≥ 3 operators, or Aurora exceeds 500 observer-free trucks in revenue service → re-open Phi_S mid/high.

---

## F8. Commercial humanoid fleet (verified productive units)

**Measures:** humanoids actually performing paid productive work at customer sites (not demos, not lab units). **Informs: Phi_U (with spillover to Phi_S for structured warehouse work).**

**Latest readings (as of Jul–Aug 2026):**

- **No vendor publishes audited deployed-unit counts. That absence is the reading.** The most complete tracker states unit counts are "largely proprietary" for every major vendor. [VERIFIED] https://humanoidapplications.com/humanoid-robot-deployment-report-real-world-milestones-industry-adoption-tracker-july-2026/
- **Figure:** ~40 Figure 03 units reported at BMW Spartanburg from late Jun 2026, after an 11-month Figure 02 pilot that contributed to production of 30,000+ BMW X3s; BMW "Center of Competence for Physical AI in Production" established; extension to Plant Leipzig from summer 2026. [REPORTED] https://www.solidmarketresearch.com/post/humanoid-robots-cross-the-pilot-threshold-where-factory-deployment-actually-stands-in-2026
- **Agility Robotics (Digit):** company claims **65,000+ operating hours across nine customer facilities** (GXO, Schaeffler, Toyota Motor Manufacturing Canada, Mercado Libre named); third-party installed-base estimate 40–150 units (central 75); RoboFab design capacity 10,000/yr. No published unit counts. [REPORTED] https://humanoid.guide/humanoid-deployments-in-2026-favor-figure-and-agility/ ; https://newmarketpitch.com/blogs/news/humanoid-robotics-digit-deployment-tracker
- **1X (NEO):** first consumer home deliveries began 2026-01-01 — only humanoid with confirmed consumer deliveries; $20,000 or $499/mo; teleoperation-assisted autonomy; unit counts undisclosed. [VERIFIED — tracker above; also REPORTED] https://www.travteks.com/blog/1x-neo-home-delivery/
- **Boston Dynamics (Atlas):** production Atlas unveiled CES 2026; operating at Hyundai Metaplant Application Center (Georgia) from 2026-02-01 on autonomous material handling; 2026 allocations committed (Hyundai RMAC + Google DeepMind); counts undisclosed. [VERIFIED — tracker above]
- **Unitree:** G1/H2/R1 mass shipments from early 2026 (G1 ≈ $16k) to labs, training centers, enterprise innovation units — R&D/education fleet, not productive-work deployment. [REPORTED] search-verified CES 2026 coverage
- **Tesla Optimus:** "multiple units" at internal facilities; no verified third-party deployment counts. [VERIFIED — tracker above]

**Series:** 2024: zero humanoids in sustained commercial productive work [INTERNAL] · 2025: single-site pilots (Figure 02 @ BMW; Digit @ GXO RaaS) [INTERNAL/REPORTED] · 2026 H1: first multi-site paid fleets, tens-of-units per site, first consumer home deliveries [readings above]. Best-evidence global productive fleet remains **low hundreds of units**.

**Reliability caveat:** every deployment is structured, curated, and teleop/exception-handled to an undisclosed degree — hours-in-operation and milestone press are vendor-controlled, so this family currently evidences Phi_U's *floor*, not its trajectory.

**Tripwire:** any audited/third-party-verified count of ≥ 5,000 humanoids in paid productive work globally, or a single customer site running ≥ 500 units in sustained operations → re-open Phi_U (and check Phi_S spillover).

---

## F9. Frontier model releases with deployment-relevant reliability claims

**Measures:** the capability/reliability frontier commercially purchasable (closed API) and freely available (open weights) — feeds C_G, C_R levels and the model's commercial-availability term. **Informs: C_G, C_R.**

**Latest readings — closed frontier (2026 H1–H2):**

- **Anthropic Claude 5 family:** **Claude Fable 5 GA 2026-06-09** (access suspended 2026-06-12, restored 2026-07-01); Claude Mythos 5 limited-release via Project Glasswing; 1M-token context, 128k output, $10/$50 per Mtok; adaptive thinking always on; **deployment-reliability infrastructure now productized: safety-classifier refusals returned as `stop_reason: "refusal"`, server-side fallback routing, fallback billing credit, task budgets, compaction, memory tool**. [VERIFIED] https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 ; announcement https://www.anthropic.com/news/claude-fable-5-mythos-5
- **Claude Opus 5 released 2026-07-24** — "near-Fable 5 intelligence at half the price," $5/$25 per Mtok, 1M context. [REPORTED] https://www.axios.com/2026/07/24/anthropic-releases-new-model-opus-5 ; https://github.blog/changelog/2026-07-24-claude-opus-5-is-now-available-in-github-copilot/
- **OpenAI GPT-5.6 released 2026-07-09** (previewed under restrictions 2026-06-26) — three tiers Luna/Terra/Sol; enterprise/coding/science/cyber positioning. [VERIFIED-secondary] https://en.wikipedia.org/wiki/GPT-5.6 ; https://openai.com/index/gpt-5-6/ ; https://www.cnbc.com/2026/07/08/openai-expanding-gpt-5point6-ai-model-release-ending-government-limits.html
- **Google:** Gemini 3 (2025-11-18); Gemini 3.1 Pro (2026-02-19, per METR file); Gemini 3.6 Flash + 3.5 Flash-Lite (2026-07-21) with **no 3.5/3.6 Pro** — flagship cadence paused pending "Gemini 4." [REPORTED] https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/
- **xAI Grok 4.6 released 2026-08-12:** AA Intelligence Index 61 (level with GPT-5.6 Sol, 1 pt behind Claude Fable 5); SWE-bench (Vals) 95.6%; AA-Briefcase debut Elo 1,577; 500k context; same 1.5T base as 4.5, gains from post-training. [REPORTED — multiple outlets] https://datanorth.ai/news/xai-releases-grok-4-6 ; https://felloai.com/grok-4-6/

**Latest readings — open weights (the commercial-availability term):** [VERIFIED] https://a2aprotocol.ai/insights/qwen-38-max-vs-glm-52-vs-kimi-k3-vs-deepseek-v4-flash

- **Kimi K3 — downloadable now** (2.8T MoE, MIT license, on Hugging Face since 2026-07-27): **AA Intelligence Index 57 = #4 of 189 overall** — i.e., open weights sit ~3–5 index points behind the closed leader (Fable 5 ≈ 60–62, GPT-5.6 Sol ≈ 59–61 depending on snapshot). SWE-bench Verified ~78% (independent table) vs 93.4% (Vals AI harness) — harness spread again.
- **GLM 5.2 — downloadable** (~744B, MIT): AA Index 51. **DeepSeek V4 Flash 0731** (284B/13B active): AA Index 50 at $0.14/$0.28 per Mtok; weights "in coming weeks" as of retrieval; DeepSeek-V4-Pro-Max reported 80.6% SWE-bench Verified (vendor). [REPORTED] https://www.morphllm.com/best-open-source-coding-model-2026
- **Qwen3.8 Max — API-only at retrieval** (2.4T/95B active; weights "promised" as of 2026-07-30): GDPval-AA 1,737 [VERIFIED, F2]; OSWorld-Verified 86.1% [REPORTED, F4] — a Chinese open-lineage model at/near the top of two deployment-relevant boards.
- **Meta/Llama: absent.** No Llama entry surfaced on any 2026 frontier leaderboard retrieved for this ledger (last major open release remains Llama 4, Apr 2025 [INTERNAL]) — the open-weights frontier is now Chinese-lab-led.

**Reliability caveat:** release-note capability claims are vendor-benchmarked at max effort/scaffold; the deployment-relevant signal here is infrastructure (refusal/fallback APIs, task budgets, effort control, 1M contexts) and price-per-capability collapse (Opus-5-class at $5/$25), not headline scores.

**Tripwire:** an actually-downloadable open-weights model reaches parity (within measurement noise) with the closed leader on ≥ 2 of F1–F4 simultaneously, or a closed GA release ships with a contractual unattended-operation SLA → re-open the commercial-availability term and C_G/C_R mid.

---

## F10. Enterprise adoption cross-sections

**Measures:** independently surveyed AI use in firms, plus production deployment rates in the two most instrumented niches (customer support, software engineering). **Informs: replacement calibration, C_R.**

**Latest readings — economy-wide (best methodology first):**

- **US Census BTOS: national AI use rate 19.8% of firms as of 2026-05-03** (Information 39.7%, Finance & Insurance 33.9%); Dec 2025–May 2026 range 17–20%, expected-use next 6 months 20–23%; ~1.2M-business sample frame, biweekly collection. [VERIFIED] https://www.census.gov/library/stories/2026/05/ai-use-businesses.html ; https://www.census.gov/newsroom/press-releases/2026/btos-apr-23.html ; Federal Reserve monitoring note (2026-04-03) [VERIFIED] https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-us-economy-20260403.html ; microdata working paper CES-WP-26-25 [VERIFIED] https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-25.html
- Series: ≈ 3.9% (Sep 2023) [INTERNAL] · ≈ 5–6% (2024) [INTERNAL] · ≈ 9% (mid-2025) [INTERNAL] · **17.3% (late 2025) → 19.8% (May 2026)** [VERIFIED above]. Adoption roughly doubled in ~9 months.

**Latest readings — contact centers (deflection/resolution):**

- Intercom **Fin: 76% average resolution across ~12,000 customers** (~1%/month improvement; top customers 80–84%) — vendor-reported. [REPORTED] https://fin.ai/learn/sierra-ai-pricing (vendor context) ; sector guide: ~two-thirds median, 70–75% strong, 80%+ best-in-class [REPORTED] https://www.lorikeetcx.ai/articles/best-ai-customer-support-software
- **Independent assessments place typical real resolution at 42–50%** vs vendor-cited ~71–76% — the honest-deployment discount made measurable. [REPORTED] https://www.thewitn.com/blog/ai-agent-pricing-in-2026-what-fin-sierra-decagon-and-agentforce-actually-charge
- Structural signal: **Salesforce definitive agreement to acquire Fin (Intercom's agent line) for ≈ $3.6B, 2026-06-15**; outcome-based pricing now standard ($0.50–$2.00/resolution across Quickchat/Fin/Zendesk/Agentforce). [VERIFIED-primary press title] https://www.salesforce.com/news/press-releases/2026/06/15/salesforce-signs-definitive-agreement-to-acquire-fin/
- Series: 2023–24 deflection typically 20–40% [INTERNAL] · 2025: Fin-class ~65% vendor-avg [INTERNAL] · 2026: 76% vendor / 42–50% independent [REPORTED above].

**Latest readings — agentic coding in production:**

- **57% of organizations report coding agents in production**; Cursor + GitHub Copilot + Claude Code ≈ 70%+ combined share. [REPORTED] https://sourceryintel.com/reports/the-state-of-ai-coding-agents-2026
- Google: **75% of new code AI-generated and engineer-approved (Apr 2026), up from ~50% late 2025**. [REPORTED] https://www.secondtalent.com/resources/how-much-software-written-by-ai/
- Enterprise codebase share: 61% AI-generated/assisted (CloudBees "State of Code Abundance" 2026) [REPORTED] https://www.cloudbees.com/blog/2026-state-of-code-abundance-report ; 51% of early-2026 GitHub commits AI-gen/assisted [REPORTED, same aggregate family] ; McKinsey: −46% time on routine coding across 4,500 devs / 150 enterprises [REPORTED]. Anthropic's own 2026 Agentic Coding Trends Report: https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf [VERIFIED as existing; not parsed].

**Reliability caveat:** the best-methodology reading (BTOS) measures *any* AI use, not job-level replacement; the niche readings are vendor-skewed (resolution-rate definitions vary, "AI-generated code" conflates autocomplete with agents), and the vendor-vs-independent gap in support (76% vs 42–50%) is the calibration constant to carry, not either number alone.

**Tripwire:** BTOS national use ≥ 35%, or an independent (non-vendor) multi-firm study showing ≥ 70% full-resolution in support or ≥ 50% of merged enterprise code authored end-to-end by agents → re-open replacement-formula calibration and C_R mid.

---

## F11. Remote Labor Index (ADDED FAMILY)

**Justification for addition:** RLI (Scale AI + Center for AI Safety) is the closest single instrument to the model's own definition — real paid freelance projects, end-to-end, judged "at least as good as the delivered human standard" by expert reviewers. It is the honest-deployment lens *as a benchmark*, and it directly disciplines the gap between F2's preference-Elo and shippable work. **Informs: C_G, replacement-formula calibration.**

**Latest readings (240 real projects — 3D/CAD, architecture, design, video, audio, data, web apps; 230 private + 10 public; 94.4% inter-rater agreement):** [VERIFIED] https://labs.scale.com/leaderboard/rli

- **Claude Fable 5: 15.80% automation rate** (current leader, marked NEW ⇒ Jul 2026 per coverage)
- Claude Opus 4.8: 8.33% · Codex GPT-5.5: 6.25% · Claude Opus 4.6 (Cowork): 4.17% · Manus 1.6 Max: 2.92% · GPT-5.2: 2.50% · Claude Sonnet 4.5: 2.08% · Gemini 2.5 Pro: 0.83%
- CAIS framing of the update: "a significant increase in digital labor automation." [REPORTED] https://safe.ai/blog/significant-increase-in-digital-labor-automation ; one secondary source quotes 16.1% — use the leaderboard's 15.8%. [REPORTED] https://blog.pebblous.ai/blog/remote-labor-index-automation/en/

**Series:** 2025-10 launch: best model 2.5% (paper: https://arxiv.org/abs/2510.26787) [VERIFIED-secondary] · ~2026-01: Opus 4.6-era ≈ 4.2% [VERIFIED, board] · ~2026 Q2: Opus 4.8 8.3% [VERIFIED, board] · 2026-07: **15.8%** [VERIFIED, board]. Frontier ≈ **6x in ~9 months**, roughly a doubling every 3–4 months.

**Reliability caveat:** projects are one-shot with full upfront specs and no client back-and-forth — real freelance work adds requirement discovery and revision loops — while 84% of deliverables still fail the acceptance bar, so this is simultaneously the most honest and the most pessimistic instrument in the ledger.

**Tripwire:** RLI automation rate ≥ 35% by any GA model (the level the current 3–4-month doubling would reach around Q1 2027 if it holds) → re-open C_G mid **and** the replacement-formula acceptance discount.

---

## F12. Warehouse & logistics automation fleets (ADDED FAMILY)

**Justification for addition:** IFR (F6) counts industrial arms and misses the mobile/ASRS fleets where structured-environment physical autonomy is actually scaling; Amazon and Symbotic are the load-bearing readings between P_A and Phi_S, and they move on quarterly (not annual) cadence. **Informs: P_A, Phi_S.**

**Latest readings:**

- **Amazon: > 1,000,000 robots deployed cumulatively since 2012**; active fleet reported as "over 500,000 across 185+ fulfillment centers" with seasonal scaling ~350k → 500k+ — cumulative-vs-active definitions conflict across sources; carry both. [REPORTED] https://standardbots.com/blog/warehouse-robotics-companies ; https://www.fool.com/investing/2026/07/29/amazons-warehouse-robot-army-keeps-growing-is-symb/ (the 1M cumulative milestone was first announced Jul 2025 [INTERNAL])
- **Symbotic:** acquired Walmart's Advanced Systems & Robotics division (Jan 2026, $200M) with Walmart simultaneously investing $520M to deploy across its distribution network; **backlog > $5B**; ARMS Innovation acquisition completed 2026-07-02. [REPORTED] https://www.fool.com/investing/2026/07/15/andy-jassys-amazon-is-throwing-billions-at-warehou/ ; search-verified Motley Fool/Yahoo coverage
- Context: Amazon continues multi-billion-dollar warehouse-robotics capex in 2026. [REPORTED, same sources]

**Series:** Amazon ~200k robots (2019) · ~520k (2022) · ~750k (2023) [all INTERNAL] · > 1M cumulative (Jul 2025) [INTERNAL, re-confirmed in 2026 coverage above] · active ~500k+ (2026) [REPORTED above].

**Reliability caveat:** these are the most structured environments in the physical economy (purpose-built facilities, fixed SKU flows) — scale here evidences P_A/Phi_S *at their easiest*, and headcount-per-facility effects, not fleet counts, are the replacement-relevant quantity.

**Tripwire:** a credible report of a large fulfillment network running majority-lights-out (picking + stowing + packing automated at network scale), or Amazon active fleet ≥ 1.5M, or Symbotic deployed-system count doubling year-over-year → re-open Phi_S mid (and P_A high).

---

## Gaps register (a gap is a finding)

1. **F1 METR:** no published time horizon for the current GA frontier (Claude Fable 5 / Opus 5, GPT-5.6, Grok 4.6) — canonical file ends at the 2026-04 Mythos Preview early checkpoint. Re-check `benchmark_results_1_1.yaml` before any recalibration use.
2. **F5 AEI:** no single platform-wide automation-share percentage published for the latest (Cadences, Apr–Jun 2026) window — only component figures and correlations. The Feb-2026 Learning Curves PDF carries the last hard split.
3. **F8 Humanoids:** zero audited deployed-unit counts from any vendor; every count in this family is a company claim or third-party estimate. Structural gap, unlikely to close before vendors face disclosure pressure.
4. **F2 GDPval:** OpenAI's original GDPval page returned HTTP 403 at compile; Sept-2025 baseline values rest on secondary retrievals (paper: arXiv:2510.04374 for re-verification).
5. **F6 IFR:** World Robotics 2026 (2025 data) not yet published at compile — expected ~Sep 2026; the 2025 "installations" reading is still an IFR forecast (575k). Density series not comparable across editions.
6. **F10 Enterprise:** no independent (non-vendor) large-N study of contact-center resolution rates retrieved — the 42–50% independent figure traces to one analyst source.

## Standing retrieval list (for the Q1 2027 pass)

Primary re-check URLs, in family order: metr.org/time-horizons + /assets/benchmark_results_1_1.yaml · artificialanalysis.ai/evaluations/gdpval-aa · labs.scale.com/leaderboard/swe_bench_pro_public · leaderboard.steel.dev/leaderboards/osworld (+ os-world.github.io) · anthropic.com/research (economic index series) · ifr.org/worldrobotics · waymo blog + TechCrunch AV desk · aurora.tech newsroom · humanoidapplications.com deployment tracker · platform.claude.com model docs + openai.com/index + ai.google.dev changelog + x.ai · census.gov BTOS + federalreserve.gov FEDS notes · labs.scale.com/leaderboard/rli · Amazon About/robotics + Symbotic IR.

*End of ledger. Compiled 2026-08-15; twelve families; every latest reading retrieved on compile date. The tripwire lines above are the only forward-looking statements in this document.*
