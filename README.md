# Large Labor Model

An interactive research and art project mapping AI's technical capability to replace human labor — from the first point at which global employment can be measured to the furthest point at which it can be reasonably projected.

**largelabormodel.com**

Created by Lukas Seel and Enya Trenholm-Jensen. Open source. March 2026.

---

## What it is

The Large Labor Model traces human labor across 13 territories of work from 1800 to 2041. It maps two things:

**Labor shares** — how many people work in each territory, globally, based on ILO data.

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
| Care & Health | Q | Human health and social work |
| Learning & Teaching | P | Education |
| Making Meaning | R | Arts, media, creative industries |
| Governing & Protecting | O | Public administration, defense |
| Feeding & Hosting | I | Accommodation, food service |
| Maintaining & Fixing | D, E, S | Utilities, repair, personal services |
| Thinking & Leading | M, N | Professional, scientific, technical, management |

---

## Dataset

**Current version:** 2.10 (March 2026)

| Layer | Records | Coverage |
|---|---|---|
| Labor shares | 608 | 1800–2041, moderate scenario |
| Replaceability scores | 327 | 1970–2041, moderate scenario |
| Occupations | 388 | ISCO-08 4-digit, searchable |
| Technology events | 57 | 1764–2041 |

**Source architecture:**
- ILOSTAT modeled estimates (primary, 1991–2025)
- GGDC 10-Sector Database (pre-1991, splice-adjusted to ILOSTAT classification)
- World Bank WDI (secondary validation)
- Displacement formula with documented parameters (2026–2041 projections)

The **moderate scenario** is displayed. Conservative and accelerated scenarios were computed during development and are archived separately for potential future use.

The full methodology is available at largelabormodel.com and in `Large_Labor_Model_Methodology_v2.10.md`.

---

## How it works

The visualization is a single `index.html` loading a single JSON dataset. No build step, no framework. Canvas-rendered. Deployed on Vercel.

**To run locally:**
```
git clone https://github.com/lamentierschweinchen/ai-reach.git
cd ai-reach
# Open index.html in a browser, or:
python -m http.server 8000
# Then visit http://localhost:8000
```

---

## Contributing

This is an open source project. Corrections, extensions, and challenges are welcome.

**To correct a score:** Reference the specific territory, year, and scenario. State the current score. Provide evidence — a commercially available product that raises it, or the absence of one that should lower it.

**To challenge the displacement model:** The lag schedule and conversion rate are the most consequential parameters. Sector-specific technology adoption data that suggests a different absorption curve would directly improve the model.

See the methodology document for the full contribution framework.

---

## License

Open source. Dataset, methodology, and visualization code available for reuse, adaptation, and critique.

---

*Large Labor Model. Grounded in the landscape of early 2026 — a moment when AI capabilities have made extraordinary leaps that most research has not yet caught up with.*
