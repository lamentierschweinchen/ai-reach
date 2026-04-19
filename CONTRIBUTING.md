# Contributing to Large Labor Model

Thanks for taking the time to engage with this project. The Large Labor Model is open source by design — every number is an invitation to refine, challenge, or extend the work. This document describes the kinds of contributions we welcome and how to make them.

---

## What we're looking for

The most valuable contributions are **specific, evidence-backed corrections** to the dataset. The model is grounded in early 2026; AI capabilities and labor data are moving fast, and contributions that pull a specific score in a defensible direction are exactly what we want.

We welcome:

- **Score corrections** with cited evidence
- **Methodology critiques** that identify weak assumptions
- **Source additions** — peer-reviewed or industry data we've missed
- **Occupation territory reassignments** — when the editorial categorization gets a job clearly wrong
- **Display name fixes** — typos, awkward phrasing, gendered language
- **Bug reports** for the visualization
- **Translation** of core copy into other languages (open an issue first to coordinate)

We are **not** looking for:

- "AI will/won't take jobs" essays — the model deliberately separates technical capability from labor displacement
- Predictions or forecasts beyond the methodology's documented scenarios
- Cosmetic preferences without a usability rationale
- Adding a new feature without first opening an issue to discuss

---

## Score corrections — the structured ask

A good score correction includes all of the following:

1. **Territory** (e.g., Care & Health) **and year** (e.g., 2026)
2. **Current score** as it appears in `ai_reach_v5.0.json`
3. **Proposed score** and direction (raise / lower / hold)
4. **Evidence**: a commercially available AI/robotic system that performs the territory's core tasks (raises) or the absence of one that should lower the current score
5. **Source link**: paper, product page, earnings call, benchmark result, deployment report

The standard for evidence is **commercial availability**, not lab demos. A research paper showing 95% accuracy on a benchmark does not raise a score. A product you can buy — or a deployment with documented headcount impact — does.

### Example of a well-formed correction

> **Territory:** Moving Things
> **Year:** 2026
> **Current score:** 56
> **Proposed:** 62
> **Evidence:** Waymo crossed 200,000 paid driverless trips per week in March 2026 (Waymo Q1 2026 update), with safety metrics meeting their published threshold for unsupervised operation in three additional metro areas. Cumulative unsupervised miles now exceed 50 million.
> **Source:** https://waymo.com/blog/2026/03/q1-update

---

## How to submit a contribution

### Small fixes (typos, wrong display names, broken links)

Open a pull request directly. Reference the file and line. Keep the diff minimal.

### Score corrections, source additions, methodology questions

Open an issue using the **Score correction** template. We will discuss in the issue, then either you or a project lead will open the PR.

### Bigger structural changes (new territories, schema changes, scoring framework changes)

Open an issue first — these need a design conversation before code changes. The schema is consumed by the visualization in `index.html`, so structural changes have downstream effects.

---

## How the dataset is built

The canonical dataset is `ai_reach_v5.0.json` at the repository root. The full methodology — every assumption, every parameter, the source hierarchy, the changelog — lives in `methodology-full.html`. Read both before proposing structural changes.

### Editorial principles (v5)

Two principles shape how occupations are placed into territories:

1. **Nature of work, not industry sector.** A barber's work is personal care, so barbers belong to Care & Health regardless of whether they work in a salon (retail) or a hotel (hospitality). A car mechanic's work is repair, so mechanics belong to Maintaining & Fixing regardless of whether they work for a manufacturer or a dealership.

2. **Functional managers go with their function.** A Finance Manager belongs to Money & Data, not Thinking & Leading. Thinking & Leading is reserved for organizational generalists (CEOs, consultants), pure knowledge workers (mathematicians, sociologists), and people functions (HR).

### Display selection

Each of the 13 modern territories displays 8 occupations (104 total). The selection balances workforce weight against iconic representation: the largest occupations are always included, but slots are also reserved for roles that define the territory in the public imagination (Surgeons, Architects, Veterinarians) even when their headcount is small. The remaining occupations stay in the dataset and remain searchable.

---

## Code contributions

The visualization is intentionally minimal: a single `index.html` (~2,700 lines) loading a single JSON file. No build step, no framework, no dependencies. Canvas-rendered.

### Local development

```bash
git clone https://github.com/lamentierschweinchen/ai-reach.git
cd ai-reach
python3 -m http.server 8000
# Visit http://localhost:8000
```

### Style notes

- Plain JavaScript, no transpilation
- ES2020+ features are fine (target is modern browsers)
- Match the existing code style — section headers, hyphenated comments, terse variable names
- Test on both desktop and mobile (375px viewport)
- iOS Safari has known canvas quirks — check the existing iOS workarounds before adding more

---

## Code of conduct

Be kind. Engage with the work, not with the people making it. Assume good faith. The model is provisional by design; disagreements about scores or methodology should be argued with evidence, not personal stake.

Conduct that violates GitHub's [Community Guidelines](https://docs.github.com/en/site-policy/github-terms/github-community-guidelines) will be moderated.

---

## Questions?

- For data and methodology questions: open a discussion or an issue
- For project direction and collaboration: see the contact information in the methodology page

The project is grounded in early 2026 — a moment when AI capabilities have made extraordinary leaps that most research has not yet caught up with. Helping the model catch up is the work.
