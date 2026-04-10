# AI Reach — Data Architecture Overview

**Version:** 2.5 · **Date:** 2026-03-29 · **Repo:** `lamentierschweinchen/ai-reach`

---

## What This Is

A canvas-based labor visualization spanning 1800–2041 that tracks how AI/automation reaches across 13 occupational territories. The entire frontend is a single `index.html` (2,290 lines) loading a single JSON dataset (`ai_reach_v2.5.json`, 1.5 MB). No build step, no framework.

---

## 1. Dataset Schema

### Top-Level Keys

```
ai_reach_v2.5.json
├── metadata                   # Version info, changelogs, record counts
├── labor[]                    # 426 records — workforce distribution by territory/year
├── replaceability[]           # 535 records — AI replaceability scores by territory/year
├── occupations[]              # 389 records — individual jobs with ISCO codes
├── technology_events[]        # 57 records — timeline milestones (1764–2041)
├── territory_metadata{}       # 15 entries — panel copy for all territories + macros
└── historical_occupations{}   # 3 entries — pre-disaggregation occupation groups
```

### 1.1 `labor[]` — Workforce Distribution

Each record = one territory at one year. Historical data (1800–2026) plus three scenario projections (2027–2041).

```json
{
  "year": 2020,
  "territory_id": "care_health",
  "territory": "Care & Health",
  "isic_sections": ["Q"],
  "global_workers_millions": 121.0,
  "global_workforce_share_pct": 3.8,
  "share_of_employed_pct": 3.8,
  "data_quality": "HIGH",
  "granularity": "territory",
  "data_type": "historical",
  "scenario": null,
  "notes": "...",
  "source_ids": ["G045", "G046"]
}
```

| Field | Values | Notes |
|-------|--------|-------|
| `data_type` | `historical`, `historical_macro`, `interpolated`, `projected` | Projected records always have a `scenario` |
| `scenario` | `null`, `conservative`, `moderate`, `accelerated` | Only set when `data_type === "projected"` |
| `data_quality` | `LOW`, `MEDIUM`, `HIGH` | Pre-1900 is mostly LOW |
| `granularity` | `macro`, `territory`, `interpolated`, `projected` | Macro = pre-disaggregation 3-sector model |

**Coverage by era:**

| Period | Territories Present |
|--------|-------------------|
| 1800–1899 | `land_sea`, `macro_industry`, `macro_services` (3-sector model) |
| 1900–1949 | + `making_things`, `building_things`, `moving_things`, `governing_protecting` |
| 1950–1959 | + `buying_selling` |
| 1960–1969 | + `care_health`, `learning_teaching` |
| 1970–1979 | + `money_data` |
| 1980–2026 | + `feeding_hosting`, `maintaining_fixing`, `making_meaning`, `thinking_leading` (all 13) |
| 2027–2041 | All 13 territories × 3 scenarios. No macros. |

### 1.2 `replaceability[]` — AI Replaceability Scores

Territory-level scores (0–100). Not per-occupation — those are derived from these.

```json
{
  "year": 2026,
  "territory_id": "making_things",
  "replaceability_score": 72,
  "score_basis": "OBSERVED",
  "primary_barrier": "ECONOMIC",
  "barrier_types": ["ECONOMIC"],
  "benchmark_anchor": "Xiaomi runs lights-out factories...",
  "key_barrier_note": "Global average decades behind frontier...",
  "scenario": null,
  "source_ids": ["G014"]
}
```

| Period | Records | Notes |
|--------|---------|-------|
| 1970–2026 | 1 per territory per year | `score_basis: "OBSERVED"`, no scenario |
| 2027–2041 | 1 per territory per year per scenario | `score_basis: "DERIVED"`, scenario required |

**Barrier types:** `ECONOMIC`, `REGULATORY`, `TECHNICAL`, `HUMAN_PREFERENCE`

### 1.3 `occupations[]` — Individual Jobs

389 ISCO-coded occupations, each assigned to exactly one territory.

```json
{
  "isco_code": "2512",
  "occupation_name": "Software Developers",
  "display_name": "Software Developers",
  "common_titles": ["software engineer", "programmer", "coder", "SWE", ...],
  "territory_id": "money_data",
  "territory": "Money & Data",
  "replaceability_2026": 89,
  "replaceability_2030_conservative": 91,
  "replaceability_2030_moderate": 93,
  "replaceability_2030_accelerated": 96,
  "primary_barrier": "TECHNICAL",
  "key_barrier_note": "...",
  "benchmark_anchor_2026": "...",
  "displacement_2026_moderate": 12.5,
  "displacement_2030_moderate": 35.0,
  "display_in_territory": true
}
```

**Key fields for the data pipeline:**

| Field | Constraint | Purpose |
|-------|-----------|---------|
| `display_name` | Max 25 chars | Shown on canvas diamonds and side panel |
| `display_in_territory` | Exactly 8 `true` per territory | Which occupations render as sub-shape diamonds |
| `common_titles` | Array of strings | Powers search (deduplicated by highest score) |
| `replaceability_2026` | 0–100 integer | Base score, always present |
| `replaceability_2030_{scenario}` | 0–100 integer | Projection; code falls back to 2026 if missing |
| `displacement_*` | Float (%) | Present but **not rendered** in current UI |

### 1.4 `technology_events[]` — Timeline Milestones

57 events from 1764 to 2041.

```json
{
  "year": 2024,
  "event_name": "Xiaomi Lights-Out Smartphone Factory",
  "era": "Generative AI Era",
  "primary_territory_id": "making_things",
  "secondary_territory_ids": [],
  "impact_type": "DEPLOYMENT",
  "impact_description": "Xiaomi launches an 81,000 square meter...",
  "confidence": "HIGH"
}
```

| Field | Values |
|-------|--------|
| `year` | Can be fractional (2022.5 = July 2022) |
| `impact_type` | `INVENTION`, `DEPLOYMENT`, `BENCHMARK` |
| `confidence` | `HIGH`, `MEDIUM`, `LOW` |

**Filtering for timeline dots:** Only HIGH confidence + structural types (INVENTION/DEPLOYMENT/BENCHMARK). Pre-2022: max 1 per year. Post-2022: max 2 per year (positioned at year+0.0 and year+0.5).

**Toast display:** Shows year + event name only. `impact_description` is loaded but hidden via CSS (`display: none`).

### 1.5 `territory_metadata{}` — Panel Copy

15 entries (13 modern territories + 2 macros). Replaces hardcoded descriptions.

```json
{
  "money_data": {
    "display_name": "Money & Data",
    "isic": "J, K, L",
    "description": "Finance, insurance, information technology, and data — where money moves and information is processed.",
    "panel_note": null
  },
  "macro_services": {
    "display_name": "Services",
    "isic": "Various",
    "description": "Services workforce before territory disaggregation...",
    "panel_note": "Services disaggregates gradually: Governing & Protecting splits off at 1900...",
    "applicable_years": { "start": 1800, "end": 1949 }
  }
}
```

`panel_note` is optional — only present on `land_sea`, `macro_industry`, `macro_services`.

### 1.6 `historical_occupations{}` — Pre-Disaggregation Groups

3 entries for the macro-era view. Each contains exactly 8 occupations.

```json
{
  "macro_industry": {
    "description": "Industrial workforce before territory disaggregation",
    "applicable_years": { "start": 1800, "end": 1899 },
    "note": "From 1900, macro_industry splits into Making Things...",
    "occupations": [
      {
        "display_name": "Textile Workers",
        "approximate_share_pct": 26,
        "replaceability_score": 0
      },
      ...
    ]
  }
}
```

| Entry | Years | Notes |
|-------|-------|-------|
| `macro_industry` | 1800–1899 | Splits into Making Things, Building Things, Moving Things at 1900 |
| `macro_services` | 1800–1949 | Gradually disaggregates: Gov at 1900, Buying at 1950, etc. through 1980 |
| `land_sea` | 1800–1899 | Real territory from 1800, but uses historical occupation set pre-1900 |

**Critical rule:** `approximate_share_pct` drives diamond **size** only. It is never displayed as text. `replaceability_score` is always 0 for historical occupations.

---

## 2. Data Loading Pipeline

`loadData()` (line 586) fetches the JSON into global `V2`, then `buildLookupTables()` (line 593) transforms it into six lookup structures:

### Lookup Tables Built

```
V2.labor           →  laborLookup[territory_id][year] = share_pct       (historical)
                   →  laborProjected[scenario][territory_id][year]       (2027+)
                   →  workforceLookup[year] = total_millions             (summed)
                   →  macroLookup[macro_id][year] = share_pct            (3-sector)

V2.replaceability  →  replLookup[territory_id][year] = score             (1970–2026)
                   →  replProjected[scenario][territory_id][year]        (2027–2041)

V2.occupations     →  occupationsByTerritory[territory_id] = [all occs]  (sorted by score desc)
                   →  displayOccupations[territory_id] = [8 occs]        (display_in_territory=true)
                   →  JOB_SEARCH_DATA = [{job, territory, score, ...}]   (deduplicated titles)

V2.historical_occupations  →  historicalOccupations = V2.historical_occupations  (direct ref)

V2.technology_events  →  ALL_EVENTS = [mapped events]                    (all 57)
                      →  MILESTONES = [filtered subset]                  (for timeline dots)
```

### Workforce Total Computation

Per-year sum of all non-overlapping labor records (avoids double-counting macro + child territories). Stored in `workforceLookup[year]`.

### Search Index

`JOB_SEARCH_DATA` is built from all 389 occupations' `display_name`, `occupation_name`, and `common_titles`. Titles are lowercased and deduplicated — if two occupations share a title, the one with higher `replaceability_2026` wins. Search UI filters by substring, prioritizes prefix matches, shows top 8 results.

---

## 3. Territory System

### 13 Modern Territories

| ID | Name | ISIC | Color | Emerges |
|----|------|------|-------|---------|
| `land_sea` | Land & Sea | A, B | #004D1A | 1800 |
| `making_things` | Making Things | C | #FF6600 | 1900 |
| `building_things` | Building Things | F | #FF3D00 | 1900 |
| `moving_things` | Moving Things | H | #00A36C | 1900 |
| `governing_protecting` | Governing & Protecting | O | #A100FF | 1900 |
| `buying_selling` | Buying & Selling | G | #FFD700 | 1950 |
| `care_health` | Care & Health | Q | #E60073 | 1960 |
| `learning_teaching` | Learning & Teaching | P | #00E5FF | 1960 |
| `money_data` | Money & Data | J, K, L | #0033CC | 1970 |
| `feeding_hosting` | Feeding & Hosting | I | #C28A00 | 1980 |
| `maintaining_fixing` | Maintaining & Fixing | D, E, S | #39FF14 | 1980 |
| `making_meaning` | Making Meaning | R | #FF99CC | 1980 |
| `thinking_leading` | Thinking & Leading | M, N | #7B1FA2 | 1980 |

### 2 Macro Shapes (Pre-Disaggregation)

| ID | Name | Children | Dissolves |
|----|------|----------|-----------|
| `macro_industry` | Industry | making_things, building_things | 1900 |
| `macro_services` | Services | buying_selling, money_data, care_health, learning_teaching, feeding_hosting, maintaining_fixing, making_meaning, thinking_leading, moving_things, governing_protecting | 1980 |

**Note:** `moving_things` and `governing_protecting` are children of Services, not Industry.

### Progressive Disaggregation

The 3-sector model (Land & Sea, Industry, Services) is the only view in 1800. Territories emerge at their "Emerges" year with a ±3 year morph window (smooth interpolation of position, size, and opacity from parent macro to independent shape).

**1800–1899:** 3 shapes (land_sea + 2 macros)
**1900–1949:** land_sea + 4 independent + macro_services
**1950–1979:** Gradual Services breakup
**1980+:** All 13 independent territories, no macros

---

## 4. Replaceability Model

### How Scores Work

**Territory-level scores** (from `replaceability[]`): 0 = no AI capability, 100 = fully replaceable. These are the headline numbers shown on each territory shape.

**Occupation-level scores** (from `occupations[]`): Each occupation has a base `replaceability_2026` score. At runtime, this is **scaled by the territory's current reach** at whatever year the user is viewing:

```
displayed_score = occupation.replaceability_2026 × (territory_reach_at_year / territory_reach_at_2026)
```

So an occupation at 50% in a territory at 20% reach (in 2020) displays as ~14%. The same occupation at the same territory in 2026 (reach = 36%) would display 50%.

### Three Scenarios (2027–2041)

| Scenario | Assumption |
|----------|------------|
| `conservative` | Regulatory friction, slow capital deployment, historical adoption pace |
| `moderate` | Status quo trajectory, expected regulation, typical investment |
| `accelerated` | Rapid adoption, light regulation, breakthrough in humanoid cost curve |

Currently hardcoded to `moderate` (line 920: `let scenario = 'moderate'`). No UI toggle exists yet.

### Interpolation

All scores between known data points use linear interpolation via `interp()`. Outside the data range, values are clamped to the nearest endpoint (flat extrapolation).

---

## 5. Data Consumption — How the Renderer Uses Data

### Per-Frame Rendering

For each territory at `currentYear`:
1. `getTerritoryReach(t, year)` → interpolated replaceability score (0–100)
2. `getTerritoryShare(t, year)` → interpolated labor share (0–100%)
3. Shape size scaled by labor share, color intensity by reach

### Zoomed View (Diamond Sub-Shapes)

`getSubShapes(territoryId, currentYear)` decides what to render:

| Condition | Source | Diamond Label | Diamond Size |
|-----------|--------|--------------|--------------|
| Macro territory, or land_sea pre-1900 | `historicalOccupations[id]` | Name only | Proportional to `approximate_share_pct` |
| Modern territory post-emergence | `displayOccupations[id]` (8 curated) | Name + score% | Based on replaceability score |

### Side Panel

`updatePanel(id)` pulls:
- Name, ISIC, description from `V2.territory_metadata[id]` (falls back to hardcoded TERRITORIES array)
- Replaceability from `getTerritoryReach()`
- Workforce from `getTerritoryShare()` × `getWorkforce(year)`
- Barrier text from the 2026 replaceability record's `primary_barrier` + `key_barrier_note`
- Job groups from either `historicalOccupations` or `displayOccupations`
- Mini projection chart drawing from 2000–2041

### Era Labels

```javascript
const ERAS = [
  { start: 1800, end: 1850, name: 'Pre-Industrial' },
  { start: 1850, end: 1913, name: 'First Industrial Revolution' },
  { start: 1913, end: 1945, name: 'Mass Production Era' },
  { start: 1945, end: 1980, name: 'Post-War Expansion' },
  { start: 1980, end: 2000, name: 'Digital Revolution' },
  { start: 2000, end: 2012, name: 'Information Age' },
  { start: 2012, end: 2022, name: 'Deep Learning Era' },
  { start: 2022, end: 2026, name: 'Generative AI Arrives' },
  { start: 2026, end: 2041, name: 'The Transition' }
];
```

---

## 6. Fallback Behavior

| Lookup | Missing Data | Fallback |
|--------|-------------|----------|
| `laborLookup[tid]` | No labor data for territory | Returns 0 |
| `replLookup[tid]` | No replaceability data | Returns 0 |
| `replProjected[scenario][tid]` | No projection | Returns 0 |
| `occ.replaceability_2030_{scenario}` | Missing scenario variant | Uses `replaceability_2026` |
| `V2.territory_metadata[id]` | No metadata entry | Falls back to TERRITORIES array fields |
| `displayOccupations[tid]` | Empty | Returns empty array (no diamonds) |
| `historicalOccupations[id]` | No historical data | Falls through to modern occupations |

---

## 7. Version History

| Version | Commit | Key Changes |
|---------|--------|-------------|
| v2.1 | 9121576 | Progressive disaggregation, pre-2015 replaceability, search dedup |
| v2.2 | 8a46e7a | Full dataset swap, new sources, ISCO re-mapping, methodology page |
| v2.3 | 12ae89e | 405→389 occupations (merged dupes), `display_name` + `display_in_territory` + `historical_occupations` added |
| v2.4 | e614e4a | ISCO label corrections (5131/5132), 5 territory moves, Care & Health + Feeding & Hosting display revisions |
| v2.5 | 6352ca4 | 47 territory reassignments, `territory_metadata` added, replaceability smoothing, event revisions, all display-8 reselected |

---

## 8. Data Update Checklist

When producing a new dataset version:

- [ ] All 13 territories have exactly 8 occupations with `display_in_territory: true`
- [ ] All 389 occupations have `territory_id`, `replaceability_2026`, `display_name` (≤25 chars)
- [ ] Labor records sum to ~100% per year (no double-counting macro + child)
- [ ] Replaceability records exist for all 13 territories × all years 1970–2026 (no scenario)
- [ ] Projected records exist for all 13 territories × 2027–2041 × 3 scenarios (both labor and replaceability)
- [ ] `conservative ≤ moderate ≤ accelerated` for all projected scores
- [ ] Historical occupations: 8 per set, `replaceability_score` = 0, `approximate_share_pct` sums roughly to 100
- [ ] `territory_metadata` has entries for all 13 territories + 2 macros
- [ ] Technology events have `year`, `event_name`, `impact_type`, `confidence`
- [ ] Changelog updated in `metadata`
- [ ] `search_terms` / `common_titles` cover expected user queries

### Deployment

```bash
# Place JSON in project root
cp ai_reach_vX.Y.json ai-reach/

# Update fetch URL in index.html line 587
# const resp = await fetch('ai_reach_vX.Y.json');

# Commit, push, deploy
git add ai_reach_vX.Y.json index.html
git commit -m "vX.Y: description"
git push origin main
npx vercel --prod
```

---

## 9. Constants Reference

| Constant | Value | Location |
|----------|-------|----------|
| `START_YEAR` | 1800 | line 780 |
| `END_YEAR` | 2041 | line 780 |
| `SPLIT_YEAR` | 2026 | line 780 (historical/projected boundary) |
| `MORPH_HALF_WIDTH` | 3 | line 895 (territory emergence transition window) |
| `scenario` | `'moderate'` | line 920 (hardcoded, no UI toggle yet) |

---

## 10. Not Yet Implemented

| Feature | Data Available | Status |
|---------|---------------|--------|
| Scenario toggle (conservative/moderate/accelerated) | Yes — all three scenarios in JSON | Global var exists, no UI |
| Displacement figures | Yes — `displacement_*` fields on occupations | Loaded but never rendered |
| `impact_description` on event toast | Yes — in technology_events | Loaded, hidden via CSS |
| Country-level labor breakdown | No | Global totals only |
