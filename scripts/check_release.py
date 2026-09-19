#!/usr/bin/env python3
"""Release check — run before every deploy:  python3 scripts/check_release.py

Every figure the docs state is derived here from the dataset and compared with
what the docs, the Mirror bundle, the public extracts and the homepage loader
actually say. Exit code 1 on any failure. Stdlib only; reads repo files only.

Written 2026-09-19 after an audit found the homepage drawing 1990 workforce
shares for every later year, a published replacement formula that did not
produce the published numbers, and counts that had drifted across five files.
"""
import hashlib, json, pathlib, re, sys, collections

ROOT = pathlib.Path(__file__).resolve().parents[1]
fails, passes = [], 0

def check(label, ok, detail=""):
    global passes
    if ok: passes += 1
    else: fails.append(f"{label}" + (f" — {detail}" if detail else ""))

def text(rel): return (ROOT / rel).read_text()

DS_PATH = ROOT / "ai_reach_v5.0.json"
ds = json.loads(DS_PATH.read_text())
md, occ, labor = ds["metadata"], ds["occupations"], ds["labor"]
ds_sha = hashlib.sha256(DS_PATH.read_bytes()).hexdigest()
_b = text("mirror/mirror_data.js"); bundle = json.loads(_b[_b.index("=") + 1:].strip().rstrip(";"))

# ── 1. declared counts equal the arrays they describe ─────────────────────────
for field, n in [("occupation_count", len(occ)), ("labor_record_count", len(labor)),
                 ("technology_event_count", len(ds["technology_events"])), ("source_count", len(ds["sources"]))]:
    check(f"metadata.{field} == array length", md.get(field) == n, f"{md.get(field)} vs {n}")
modern = {o["territory_id"] for o in occ}
check("metadata.territory_count == territories that carry occupations", md.get("territory_count") == len(modern), f"{md.get('territory_count')} vs {len(modern)}")
check("territory_replaceability covers exactly the modern territories", {r["territory_id"] for r in ds["territory_replaceability"]} == modern)
check("historical_aggregate_count == territory_metadata − modern", md.get("historical_aggregate_count") == len(ds["territory_metadata"]) - len(modern),
      f"{md.get('historical_aggregate_count')} vs {len(ds['territory_metadata']) - len(modern)}")

# ── 2. display names are unique (a collision hides an occupation in search) ───
for label, names in [("dataset display_name", [o["display_name"] for o in occ]), ("mirror bundle name", [o["name"] for o in bundle["occupations"]])]:
    dup = [n for n, c in collections.Counter(x.strip().lower() for x in names).items() if c > 1]
    check(f"{label}s unique", not dup, f"duplicates: {dup}")

# ── 3. derivatives were regenerated from THIS dataset ──────────────────────────
check("mirror bundle built from this dataset (sha256)", bundle["meta"].get("source_sha256") == ds_sha)
idx = json.loads(text("data/occupations_index.json"))
idx_sha = idx.get("source_sha256") or (idx.get("meta") or {}).get("source_sha256")
check("data/occupations_index.json built from this dataset (sha256)", idx_sha == ds_sha)
og = json.loads(text("mirror/og/manifest.json"))
bn = {o["isco"]: o["name"] for o in bundle["occupations"]}
stale = [k for k, v in og.items() if bn.get(k) != v["n"]]
check("OG manifest names match the bundle", not stale and len(og) == len(bn), f"stale: {stale[:5]}")

# ── 4. workforce shares are shares ─────────────────────────────────────────────
NON_SHARE_TYPES = {"modelled", "projected"}      # additive patches / legacy scenario rows — never whole-territory shares
by_year = collections.defaultdict(list)
for r in labor:
    if r["data_type"] not in NON_SHARE_TYPES: by_year[r["year"]].append(r)
bad_years = []
for y, recs in by_year.items():
    s = sum(r["global_workforce_share_pct"] for r in recs); w = sum(r["global_workers_millions"] or 0 for r in recs)
    gap = max(abs(100 * (r["global_workers_millions"] or 0) / w - r["global_workforce_share_pct"]) for r in recs) if w else 0
    if abs(s - 100) > 0.5 or gap > 0.5: bad_years.append((y, round(s, 2), round(gap, 2)))
check("every year's workforce shares sum to 100 and agree with worker counts", not bad_years, f"{sorted(bad_years)[:4]}")

# ── 5. the homepage admits every share-bearing record type ────────────────────
index_html = text("index.html")
m = re.search(r"LABOR_SHARE_TYPES\s*=\s*new Set\(\[([^\]]*)\]\)", index_html)
if m:
    admitted = set(re.findall(r"'([^']+)'", m.group(1)))
else:  # legacy form: if (rec.data_type === 'a' || rec.data_type === 'b' ...) { … laborLookup
    legacy = re.search(r"if \(((?:rec\.data_type === '[^']+'(?: \|\| )?)+)\) \{\s*// For macro categories", index_html)
    admitted = set(re.findall(r"'([^']+)'", legacy.group(1))) if legacy else set()
present = {r["data_type"] for r in labor}
check("index.html declares LABOR_SHARE_TYPES", bool(m))
check("no labor data_type is silently dropped by the homepage", present <= admitted | NON_SHARE_TYPES, f"unhandled: {sorted(present - admitted - NON_SHARE_TYPES)}")
newest = max(r["year"] for r in labor if r["data_type"] not in NON_SHARE_TYPES)
have = {r["territory_id"] for r in labor if r["year"] == newest and r["data_type"] in admitted}
check(f"the homepage admits a {newest} share for every modern territory", modern <= have, f"missing {len(modern - have)} of {len(modern)}")

# ── 6. the documented replacement formula reproduces the stored fields ────────
rf = md["replacement_formula_v5"]
def era(b): return "post_2022" if b == "NONE" else ("y2015_2022" if b in ("REGULATORY", "HUMAN_PREFERENCE") else "pre_2015")
CHK = {2026: "replaceability_2026", 2030: "replaceability_2030_moderate", 2035: "replaceability_2035_moderate",
       2040: "replaceability_2040_moderate", 2041: "replaceability_2041_moderate"}
n_chk = n_bad = 0
for o in occ:
    r26, b = o["replaceability_2026"], o.get("primary_barrier", "NONE")
    for y, rfld in CHK.items():
        stored, ry = o.get(f"displacement_{y}_moderate"), o.get(rfld)
        if stored is None or ry is None: continue
        n_chk += 1
        got = round((rf["conversion_rate"] * max(0, ry - r26) / 100
                     + rf["lag_schedule"][str(y)] * rf["barrier_multipliers"].get(b, 1.0) * r26 / 100 * (1 - rf["already_absorbed_era"][era(b)])) * 100, 1)
        n_bad += abs(got - stored) > 0.1001
check(f"metadata.replacement_formula_v5 reproduces all {n_chk} stored displacement values", n_bad == 0 and n_chk == len(occ) * 5, f"{n_bad} differ")

# ── 7. published capability tables match the trajectory at printed precision ──
CT = bundle["capability_trajectory"]; VEC = ["C_R", "C_G", "P_A", "Phi_S", "Phi_U", "S_E"]
def cells_html(h):
    for row in re.findall(r"<tr>((?:<td[^>]*>[^<]*</td>){7})</tr>", h):
        c = re.findall(r"<td[^>]*>([^<]*)</td>", row)
        if c[0].strip().isdigit() and c[0].strip() in CT["C_R"]: yield [x.strip() for x in c]
def cells_md(t):
    for line in t.splitlines():
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) == 7 and c[0].isdigit() and c[0] in CT["C_R"]: yield c
for rel, rows in [("methodology-full.html", list(cells_html(text("methodology-full.html")))), ("docs/v5_methodology.md", list(cells_md(text("docs/v5_methodology.md"))))]:
    wrong = [(c[0], v, val) for c in rows for val, v in zip(c[1:], VEC)
             if abs(round(CT[v][c[0]]["mid"], len(val.split(".")[1]) if "." in val else 0) - float(val)) > 1e-9]
    check(f"{rel}: capability table matches the trajectory ({len(rows)} rows)", rows and not wrong, f"{wrong[:4]}")

# ── 8. the docs state the numbers the data has ────────────────────────────────
tasks = [len(o["task_decomposition"]) for o in occ]; T, S, E = sum(tasks), len(ds["sources"]), len(ds["technology_events"])
ev_years = [e["year"] for e in ds["technology_events"]]
lab_years = [r["year"] for r in labor if r["data_type"] not in NON_SHARE_TYPES]
readme = text("README.md")
for needle in [f"| {T:,} | {min(tasks)}–{max(tasks)} tasks per occupation", f"| Sources | {S:,} |", f"| Technology events | {E} | {int(min(ev_years))}–{int(max(ev_years))} |",
               f"| Labor shares | {len(labor)} | {min(lab_years)}–{max(lab_years)}", f"| Occupations (per-occupation scores) | {len(occ)} |", f"**{len(modern)} territories of work**"]:
    check(f"README states: {needle[:48]}…", needle in readme)
check("/about states task totals", f"({min(tasks)}–{max(tasks)} tasks per occupation, {T:,} total across {len(occ)} occupations)" in text("methodology.html"))
llms = text("llms.txt")
check("llms.txt states task and source totals", f"{T:,}" in llms and f"{S:,}" in llms)
check("llms.txt documents the deep link by ISCO code", "job=<ISCO-08 code>" in llms)
cff = text("CITATION.cff")
check("CITATION.cff: dataset licence is CC-BY-4.0 (SPDX), not MIT", bool(re.search(r"^license: CC-BY-4\.0$", cff, re.M)) and not re.search(r"^license: MIT$", cff, re.M))
check("CITATION.cff: preferred-citation.type is a valid reference type ('data')", bool(re.search(r"preferred-citation:\n\s+type: data\n", cff)))
check(f"CITATION.cff abstract says {len(modern)} territories", f"across {len(modern)} territories of work" in cff)
mults = rf["barrier_multipliers"]
html_full = text("methodology-full.html")
check("methodology-full prints the shipped barrier multipliers",
      "<br>".join(f"{k}: {mults[k]:.2f}" for k in ["NONE", "ECONOMIC", "HUMAN_PREFERENCE", "REGULATORY", "HUMANOID_DEPENDENT"]) in html_full)
mdoc = text("docs/v5_methodology.md")
check("v5_methodology.md prints the shipped barrier multipliers", all(f"{k}: {mults[k]:.2f} ×" in mdoc for k in ["HUMAN_PREFERENCE", "REGULATORY"]))

# ── 9. examples satisfy the threshold they illustrate ─────────────────────────
ex = re.search(r"score below 10 — humanoid-dependent physical roles \(([^)]*)\)", html_full)
if ex:
    for w in [x.strip() for x in ex.group(1).split(",")]:
        hit = [o for o in occ if o["display_name"].lower().startswith(w.lower().rstrip("s"))]
        check(f"'below 10' example '{w}' scores below 10", hit and all(o["replaceability_2026"] < 10 for o in hit), f"{[(o['display_name'], o['replaceability_2026']) for o in hit]}")
else:
    check("methodology-full names below-10 examples", False, "sentence not found")

# ── 10. deep links never default silently ─────────────────────────────────────
for rel in ["mirror/desktop.html", "mirror/mobile.html"]:
    h = text(rel)
    check(f"{rel}: ?job= resolves names and surfaces misses", "function resolveJobParam" in h and "_jobMiss" in h and "?_want:'2221'" not in h)

print(f"release check: {passes} passed, {len(fails)} failed   (dataset sha256 {ds_sha[:12]}…)")
for f in fails: print("  FAIL ·", f)
sys.exit(1 if fails else 0)
