# Scenarios Archive — Conservative & Accelerated

**Date:** 2026-03-30
**Status:** Removed from production dataset v2.9. Archived for potential v2 site work (scenario toggle).

---

## Why they were removed

**Conservative** was the ILO consensus baseline with no displacement formula applied. It existed only as the input to the displacement calculation — `consensus_workers(T,Y)` in the formula. Its labor projections are the "what if AI displacement didn't happen" counterfactual. It was never displayed on the site. It served its purpose as an input and is archived with full data integrity.

**Accelerated** had three structural problems that were never resolved:
1. **Undocumented lag schedule.** The moderate lag (5/28/48/58/60%) is documented and formula-verified. The accelerated lag was reverse-engineered as approximately 25/60/81/92/87% but was never formally defined.
2. **Territory-variable 2026 entry points.** The 2026 accelerated starting values used per-territory lags ranging from 17% to 73%, instead of a uniform schedule. This was never documented or justified.
3. **2041 uptick anomaly.** Accelerated workers *increased* from 1,470M (2040) to 1,506M (2041) — the lag dropped from 92% to 87% while the conservative baseline grew. Workers rising in the final year of an "accelerated displacement" scenario is implausible.

These issues were documented starting in v2.6 but never fixed because the accelerated scenario was not displayed. Rather than ship data with known structural problems, we removed both non-displayed scenarios from the production file.

---

## What's in the archive

`scenarios_archive_v2.9.json` contains:

| Key | Records | Content |
|---|---|---|
| `conservative_labor` | 65 | 13 territories × 5 years (2026, 2030, 2035, 2040, 2041) |
| `accelerated_labor` | 65 | Same structure |
| `conservative_replaceability` | 104 | 13 territories × 8 years (2027–2041) |
| `accelerated_replaceability` | 104 | Same structure |

Total: 338 records.

The occupation-level scenario fields (`replaceability_2030_conservative`, `replaceability_2030_accelerated`, `displacement_*_accelerated`) were also removed from the production dataset.

---

## To restore for v2 site work

If building a scenario toggle for the v2 site:

1. **Conservative:** Data is structurally sound. Merge `conservative_labor` and `conservative_replaceability` back into the dataset arrays. Add the formula documentation: conservative applies NO displacement — its labor values ARE the ILO consensus projection directly.

2. **Accelerated:** Requires fixing before use. Specifically:
   - Define the lag schedule explicitly (recommend: 25/60/81/92/95% to fix the 2041 uptick)
   - Recompute 2026 entry points using the defined schedule uniformly (not per-territory)
   - Recompute all accelerated labor projections from the formula
   - Verify 2040→2041 monotonicity (workers should not increase)

3. **Occupation-level fields:** Would need to be recomputed or restored from v2.7 archive.

---

## Scenario parameters (for reference)

| Parameter | Conservative | Moderate | Accelerated |
|---|---|---|---|
| Conversion rate | None (no displacement) | 1/3 | 0.60 |
| Lag schedule | None | 5/28/48/58/60% | ~25/60/81/92/87% (undocumented) |
| Pre-absorption factor | None | 0.85 | 0.85 |
| Capability trajectory | WEF consensus deceleration | METR doubling through 2028 | AGI-adjacent by 2027 |
