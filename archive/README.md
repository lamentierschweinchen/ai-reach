# Archive

Historical files preserved for reference. **Not used by the live site.**

## Files

| File | What it is | When it was current |
|---|---|---|
| `ai_reach_v3.0.json` | Dataset v3.0 — first release of the 6-vector task decomposition model | April 2026 |
| `ai_reach_v3.1.json` | Dataset v3.1 — post-production R2030 floor enforcement | April 2026 |
| `Large_Labor_Model_Methodology_v2.10.md` | Standalone Markdown methodology document | March 2026 |
| `scenarios_archive_documentation.md` | Documentation of the conservative and accelerated scenarios that were removed in v2.9 | March 2026 |

## What's current

The canonical dataset and methodology live at the repository root:

- `ai_reach_v3.2.json` — current dataset
- `methodology-full.html` — current methodology (incorporates the full changelog)
- `index.html` — fetches `ai_reach_v3.2.json`

## Why these are kept

- **Reproducibility.** Anyone analyzing or citing earlier versions of the dataset (e.g., a paper that referenced v3.0 figures) can still find the exact file they used.
- **Audit trail.** The changelog in `methodology-full.html` references decisions made between versions; having the prior versions available makes those decisions verifiable.
- **Migration cost.** v3.0 → v3.2 has structural overlap; users who built on v3.0 don't need to rewrite everything to understand what changed.

If you're starting a new analysis or visualization, use the current files at the repository root.
