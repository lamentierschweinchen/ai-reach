# Large Labor Model

[![site](https://img.shields.io/badge/site-largelabormodel.com-2042E3?style=flat-square)](https://largelabormodel.com)
[![dataset](https://img.shields.io/badge/dataset-v3.2-1A5C2A?style=flat-square)](./ai_reach_v3.2.json)
[![code license](https://img.shields.io/badge/code-MIT-blue?style=flat-square)](./LICENSE)
[![data license](https://img.shields.io/badge/data-CC%20BY%204.0-orange?style=flat-square)](./LICENSE)

An interactive research and art project mapping AI's technical capability to replace human labor — from the first point at which global employment can be measured to the furthest point at which it can be reasonably projected.

**[largelabormodel.com](https://largelabormodel.com)**

Created by Lukas Seel and Enya Trenholm-Jensen. Open source. April 2026.

![Hero — 2041 view of all 13 modern territories with replaceability scores](docs/hero-2041.png)

---

## What it is

The Large Labor Model traces human labor across **15 territories of work** (13 modern + 2 historical aggregates) from 1800 to 2041. It maps two things:

**Labor shares** — how many people work in each territory, globally, based on ILO data and historical reconstructions.

**Replaceability** — when AI or robotics becomes technically capable of performing each territory's core tasks, scored 0–100 based on what is commercially available at the frontier.

The gap between what AI *can* do and what has actually changed in the labor market is the project's central provocation. A territory can score 90 while employment barely moves. That is not a flaw — it is the most important thing the visualization shows.

This is a model, not a prediction. Every number is an invitation to engage, refine, and challenge.

---

## The core distinction

**Replaceability** = can the best commercially available AI/robotics perform this role? Pure technical capability. Lab prototypes don't count. Deployment rates, economics, regulation, and social preference are recorded as barrier annotations — they do not suppress the score. *This is what the model measures.*

**Replacement** = when workers actually lose jobs. Lags replaceability by months to decades. *This is what labor share data tracks.*

---

## The 13 territories

| Territory | ISIC | What it covers |
|---|---|---|
| Land & Sea | A, B | Agriculture, forestry, fishing, mining |
| Making Things | C | Manufacturing |
| Building Things | F | Construction |
| Moving Things | H | Transport, logistics, warehousing |
| Buying & Selling | G | Retail and wholesale trade |
| Money & Data | J, K, L | Finance, insurance, information, real estate |
| Care & Health | Q | Human health and social work, personal care |
| Learning & Teaching | P | Education |
| Making Meaning | R | Arts, media, creative industries |
| Governing & Protecting | O | Public administration, defense |
| Feeding & Hosting | I | Accommodation, food service |
| Maintaining & Fixing | D, E, S | Utilities, repair, personal services |
| Thinking & Leading | M, N | Management, consulting, science, professional strategy |

Plus **2 historical aggregate territories** (Industry and Services) that cover the period before granular sectoral data was available — they disaggregate progressively into the 13 modern territories between 1900 and 1980.

### Editorial principles

Two principles shape how occupations are placed into territories:

1. **Nature of work, not industry sector.** A barber's work is personal care, so barbers belong to Care & Health regardless of whether they work in a salon (retail) or a hotel (hospitality). A car mechanic's work is repair, so mechanics belong to Maintaining & Fixing regardless of whether they work for a manufacturer or a dealership.

2. **Functional managers go with their function.** A Finance Manager belongs to Money & Data, not Thinking & Leading. Thinking & Leading is reserved for organizational generalists (Chief Executives, Management Consultants), pure knowledge workers (Mathematicians, Sociologists, Humanities Academics), and people functions (HR Specialists, Development Officers).

---

## Dataset

**Current version:** 3.2 (April 2026) — see [`methodology-full.html`](./methodology-full.html) for the full changelog.

| Layer | Records | Coverage |
|---|---|---|
| Labor shares | 608 | 1800–2041 |
| Replaceability scores (territory-level) | 327 | 1970–2041 |
| Occupations (per-occupation scores) | 388 | ISCO-08 4-digit, searchable |
| Displayed occupations (canvas) | 104 | 8 per modern territory |
| Technology events | 57 | 1764–2026 |
| Historical occupations | 24 | 8 per historical aggregate (3 categories) |
| Sources | 414 | Per-record citation |

**Source architecture:**
- **ILOSTAT** modeled estimates (primary, 1991–2025)
- **GGDC 10-Sector Database** (1870–1991, splice-adjusted to ILOSTAT classification)
- **Bairoch (1988), Mitchell (2003), Cambridge Group** (pre-1870 reconstructions)
- **World Bank WDI** (secondary validation)
- **Displacement formula** with documented parameters (2026–2041 projections)

### Replaceability scoring

- Scores tied to commercially available capability milestones (e.g., Waymo for Moving Things, SWE-bench for Thinking & Leading, Xiaomi dark factory for Making Things)
- Per-occupation scores derived from a **6-vector task decomposition model** (27,460 tasks across 388 occupations)
- Sources: METR time-horizon data, AI benchmark trajectories, SWE-bench, GPQA, IFR robot density, robotics capability research, commercial deployment data
- Per-occupation barrier tags: REGULATORY / ECONOMIC / HUMANOID_DEPENDENT / HUMAN_PREFERENCE

### Projection (2027–2041)

The visualization shows a single projection under a moderate capability trajectory. The displacement model converts capability gains into projected workforce reduction using a one-third conversion rate and a 15-year lag absorption schedule. See the full methodology for details and the most consequential parameters to challenge.

---

## How it works

The visualization is a single `index.html` loading a single JSON dataset. No build step, no framework, no dependencies. Canvas-rendered. Deployed on Vercel.

### Run locally

```bash
git clone https://github.com/lamentierschweinchen/ai-reach.git
cd ai-reach
python3 -m http.server 8000
# Visit http://localhost:8000
```

### File layout

```
ai-reach/
├── index.html              # Main visualization (~2,700 lines, canvas + DOM)
├── methodology.html        # Short methodology page (linked from the site)
├── methodology-full.html   # Full methodology + changelog
├── ai_reach_v3.2.json      # Current dataset (the only file index.html fetches)
├── DATA_ARCHITECTURE.md    # Schema and rendering pipeline reference
├── LICENSE                 # MIT (code) + CC BY 4.0 (data)
├── CONTRIBUTING.md         # How to propose corrections and additions
├── CITATION.cff            # Citation metadata
├── docs/
│   └── hero-2041.png       # Repo hero image (the 2041 view)
├── archive/                # Historical dataset versions
│   ├── ai_reach_v3.0.json
│   ├── ai_reach_v3.1.json
│   └── README.md
├── fonts/Inter-Variable.ttf
└── favicon.svg
```

---

## Contributing

Open source by design. Specific, evidence-backed corrections are exactly what we want. See [**CONTRIBUTING.md**](./CONTRIBUTING.md) for the full guide.

The short version:

- **Score correction**: Open an issue using the *Score correction* template. Include territory, year, current score, proposed score, and a link to the commercially available product or deployment that supports the change.
- **Bug report**: Use the *Bug report* template.
- **Methodology critique**: Open a discussion or an issue. Read [`methodology-full.html`](./methodology-full.html) first — most of the model's assumptions are documented there with notes on which are most worth challenging.

The standard for evidence is **commercial availability**, not lab demos. A research paper showing 95% accuracy on a benchmark does not raise a score. A product you can buy — or a documented deployment — does.

---

## Citation

```
Seel, L. & Trenholm-Jensen, E. (2026). Large Labor Model (v3.2) [Dataset].
https://largelabormodel.com
```

GitHub auto-generates a "Cite this repository" widget from [`CITATION.cff`](./CITATION.cff).

---

## License

- **Code** (`index.html`, `methodology.html`, `methodology-full.html`, all JavaScript): [MIT](./LICENSE)
- **Data** (`ai_reach_v3.2.json` and successor versions, methodology content): [CC BY 4.0](./LICENSE)
- **Inter typeface**: SIL Open Font License 1.1

You are free to share, adapt, and build on the dataset for any purpose, commercial or otherwise, with attribution.

---

*Large Labor Model is grounded in early 2026 — a moment when AI capabilities have made extraordinary leaps that most research has not yet caught up with. Helping the model catch up is the work.*
