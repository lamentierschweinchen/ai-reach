# AI Reach — When Does AI Reach Your Profession?

An interactive research and art project mapping artificial intelligence's progression into human professions across time. One question, answered with precision and honesty.

**Open Source · February 2026**

---

## What It Is

AI Reach tracks **replaceability** — when AI and robotics become technically and economically capable of performing a role — across 13 human labor territories, from 1800 to 2040.

It is not a forecast. It is a model: one interpretation of a fast-moving reality, designed to be visual, honest, and useful to people trying to understand what is happening to work.

> *"When does AI reach your profession?"*

This is an open source and collaborative project — between humans, between machines, across countries and compute.

---

## The Core Distinction

| REPLACEABILITY | REPLACEMENT |
|---|---|
| When AI/robotics becomes technically and economically capable of performing a role. **This is what AI Reach models.** | When workers actually lose jobs. This lags replaceability by years or decades due to deployment friction. **Labor share data tracks this.** |

The gap between replaceability and replacement is the **deployment lag** — caused by regulation, capital cost, institutional inertia, union resistance, and social preference.

---

## The 13 Territories

Work is grouped into 13 human-readable territories mapped to ISIC/ISCO international labor classifications:

| Territory | What It Covers | ISIC |
|---|---|---|
| Land & Sea | Agriculture, forestry, fishing | A, B |
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

*Territory taxonomy is editorial — designed for comprehension, not taxonomic purity — and subject to revision.*

---

## Replaceability Estimates (Early 2026)

| Territory | Now (2026) | 2030 | Key Barrier |
|---|---|---|---|
| Making Things (manufacturing, high-cap) | 80–90% | ~95% | Maintenance, edge cases |
| Money & Data (finance, admin, legal) | 70–80% | 85–90% | Regulatory, liability |
| Thinking & Leading (software coding) | 65–75% | 85–90% | Senior judgment, architecture |
| Care & Health (radiology, admin) | 55–65% | 75–80% | Legal liability, credentialing |
| Building Things (construction tasks) | 40–55% | 70–80% | Unstructured environments |
| Moving Things (logistics, transport) | 40–55% | 70–80% | Last mile, regulation |
| Making Things (global average) | 30–40% | 60–70% | Capital deployment lag |
| Maintaining & Fixing (physical services) | 15–25% | 45–60% | Humanoid cost curve |
| Learning & Teaching | 10–20% | 25–35% | Human preference, trust |

*These are working estimates, not final scores. Figures represent technical and economic replaceability — not actual job losses.*

---

## Why This Exists

Four things this project wants to say:

1. **Labor may be becoming obsolete — and that has no precedent.** If AI and automation make human labor structurally unnecessary as the primary mechanism for distributing economic value, the questions that follow are enormous. The project raises them without pretending to answer them.

2. **Most people do not know what AI can actually do.** In 2026, a large portion of white collar work is effectively replaceable or already being replaced. Autonomous vehicles are on roads. Lights-out factories are running. Humanoid robots have entered commercial deployment. The public debate has not caught up. This project is one attempt to close that gap.

3. **This is not alarmism — it is a political and economic reality that deserves serious attention.** The implications touch every labor market, every welfare system, every education policy, every political economy.

4. **This is a model, not a verdict.** Every number, every boundary, every projection is an invitation to engage, refine, and improve — not a claim of authority.

---

## The Rate of Progress

**The single most important finding:** METR research (2025) shows AI task time-horizon is doubling every 7 months (2019–2025), accelerating to every 4 months in 2024–2025. Cost-adjusted performance is improving ~10x per year.

- SWE-bench (real-world software engineering): 4.4% → 71.7% in one year (2023–2024)
- GPQA (graduate-level reasoning): +48.9 percentage points in one year
- GPT-4-level capability: $30/M tokens (2023) → under $1/M (2025)
- Xiaomi's 81,000 sq meter smartphone factory: fully dark, 24/7, zero workers (launched 2024)
- Entry-level job postings: down 15–67% depending on sector

---

## Data Architecture

Two parallel data layers, kept separate to prevent taxonomy churn from forcing re-collection:

**Layer 1: Labor Shares** (`labor_shares_raw.json`)
- Tracks actual employment shares — the replacement side of the ledger
- Native keys: ISIC Rev.4 sections (A–U) and ISCO-08 major groups (0–9)
- Sources: World Bank WDI, ILOSTAT modeled estimates, historical reconstructions
- Coverage: 1800–2040 (sparse pre-1991, systematic 1991+, projected 2024+)
- Null is honest — missing data stays null, not fabricated or smoothed

**Layer 2: Replaceability Index** *(in development)*
- Tracks capability frontier — the replaceability side of the ledger
- Scores by territory, 2020–2040, annual resolution
- Sources: METR time horizon data, benchmark trajectories, robotics deployment economics

### Projection Scenarios

| Scenario | Description |
|---|---|
| Conservative | Follows WEF/McKinsey consensus. Moderate displacement, large reabsorption. |
| Moderate | Accelerated timeline. Some permanent displacement. |
| Accelerated | Displaced band peaks ~11% by 2035, then partially recovers. |
| Structural (thesis) | Displacement rate permanently exceeds absorption rate post-2028 through 2040. |

---

## Working Principles

- **Null is honest.** Missing data stays null, never fabricated or smoothed.
- **Distinguish replaceability from replacement from deployment.** These are three different things.
- **Exposure ≠ replaceability.** "40% of jobs exposed to AI" is not a replaceability score.
- **The physical presence shield is eroding.** Pre-2024 models should not be treated as definitive on physical work.
- **Be analytical but accessible.** The audience is intelligent non-specialists capable of engaging with this material seriously.

---

## Status

This project is early. Throughout, a distinction is maintained between what is **settled** (treat as fixed) and what is **in development** (working decisions subject to change). The concept of the territories and the core distinction between replaceability and replacement are settled. Specific taxonomy, scoring methodology, and parameter values are not.

---

## Contributing

Open source and collaborative by design. Models are meant to be expanded, altered, and questioned. Pull requests welcome.

---

*Grounded in the landscape of early 2026 — a moment when AI capabilities have made extraordinary leaps that most research has not yet caught up with.*
