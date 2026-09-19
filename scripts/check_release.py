#!/usr/bin/env python3
"""Release check — run before every deploy:  python3 scripts/check_release.py

Checks selected published figures and release invariants against the dataset,
docs, Mirror bundle, public extracts, share-card manifest and homepage loader.
It does not validate scientific assumptions or replace browser checks. Exit code 1 on any failure.
Uses the Python stdlib and Node; reads repo files only. Node is required to execute
the Mirror's deep-link resolver and the homepage's historical-share functions.

Written 2026-09-19 after an audit found the homepage drawing 1990 workforce
shares for every later year, a published replacement formula that did not
produce the published numbers, and counts that had drifted across five files.
Hardened the same day after an independent reviewer showed 21 ways the first
version could pass while something was wrong. The archived fit worksheet is
included to reproduce its arithmetic, not to authenticate its source mappings.
"""
import collections, csv, hashlib, json, math, pathlib, re, shutil, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
fails, passes, skipped = [], 0, []

def check(label, ok, detail=""):
    global passes
    if ok: passes += 1
    else: fails.append(f"{label}" + (f" — {detail}" if detail else ""))

def text(rel):
    try: return (ROOT / rel).read_text()
    except Exception as e:
        check(f"read {rel}", False, str(e)); return ""

def load_json(rel, strip_js=False):
    try:
        t = (ROOT / rel).read_text()
        if strip_js: t = t[t.index("=") + 1:].strip().rstrip(";")
        return json.loads(t)
    except Exception as e:
        check(f"parse {rel}", False, f"{type(e).__name__}: {e}"); return None

def finish():
    note = f"  ({len(skipped)} skipped: {'; '.join(skipped)})" if skipped else ""
    print(f"release check: {passes} passed, {len(fails)} failed{note}")
    for f in fails: print("  FAIL ·", f)
    sys.exit(1 if fails else 0)

ds = load_json("ai_reach_v5.0.json")
bundle = load_json("mirror/mirror_data.js", strip_js=True)
idx = load_json("data/occupations_index.json")
og = load_json("mirror/og/manifest.json")
if not all(isinstance(x, dict) for x in (ds, bundle, idx, og)): finish()

md, occ, labor = ds["metadata"], ds["occupations"], ds["labor"]
ds_sha = hashlib.sha256((ROOT / "ai_reach_v5.0.json").read_bytes()).hexdigest()
by_code = {str(o["isco_code"]): o for o in occ}
strip_tags = lambda s: re.sub(r"<[^>]+>", "", s)
js_round = lambda x: math.floor(x + 0.5)
fold = lambda s: re.sub(r"[^a-z0-9]+", " ", str(s).lower()).strip()

# ── 1. declared counts equal the arrays they describe ─────────────────────────
for field, n in [("occupation_count", len(occ)), ("labor_record_count", len(labor)),
                 ("technology_event_count", len(ds["technology_events"])), ("source_count", len(ds["sources"]))]:
    check(f"metadata.{field} == array length", md.get(field) == n, f"{md.get(field)} vs {n}")
modern = {o["territory_id"] for o in occ}
check("metadata.territory_count == territories that carry occupations", md.get("territory_count") == len(modern), f"{md.get('territory_count')} vs {len(modern)}")
check("territory_replaceability covers exactly the modern territories", {r["territory_id"] for r in ds["territory_replaceability"]} == modern)
check("historical_aggregate_count == territory_metadata − modern", md.get("historical_aggregate_count") == len(ds["territory_metadata"]) - len(modern))
tasks = [len(o["task_decomposition"]) for o in occ]; T, S, E = sum(tasks), len(ds["sources"]), len(ds["technology_events"])
check("metadata.task_short.covers matches the task total", (md.get("task_short") or {}).get("covers") == f"{T}/{T}", str((md.get("task_short") or {}).get("covers")))

# ── 2. display names are unique (a collision hides an occupation in search) ───
for label, names in [("dataset display_name", [o["display_name"] for o in occ]), ("mirror bundle name", [o["name"] for o in bundle["occupations"]])]:
    dup = [n for n, c in collections.Counter(x.strip().lower() for x in names).items() if c > 1]
    check(f"{label}s unique", not dup, f"duplicates: {dup}")

# ── 3. derivatives were regenerated from THIS dataset — stamps AND content ────
check("mirror bundle built from this dataset (sha256)", bundle["meta"].get("source_sha256") == ds_sha)
check("occupations_index.json built from this dataset (sha256)", (idx.get("source_sha256") or (idx.get("meta") or {}).get("source_sha256")) == ds_sha)
ix = {str(o.get("isco_code")): o for o in idx.get("occupations", [])}
check("occupations_index.json: one record per occupation, names and scores equal the dataset",
      set(ix) == set(by_code) and all(ix[c].get("name") == o["display_name"] and ix[c].get("replaceability_2026") == o["replaceability_2026"] for c, o in by_code.items()))
index_fields = {"name": "display_name", "replaceability_2041": "replaceability_2041_moderate",
                "displacement_2026": "displacement_2026_moderate", "displacement_2041": "displacement_2041_moderate"}
for k in ("isco_code", "territory_id", "employment_weight_pct", "primary_barrier", "replaceability_2026",
          "replaceability_2026_low", "replaceability_2026_high", "replaceability_2041_low", "replaceability_2041_high"):
    index_fields[k] = k
check("occupation index: every exported field matches, with no duplicate or missing rows",
      len(idx.get("occupations", [])) == len(occ) and set(ix) == set(by_code) and
      all(all(ix[c].get(k) == o.get(src) for k, src in index_fields.items()) and
          ix[c].get("task_count") == len(o["task_decomposition"]) for c, o in by_code.items()))
try:
    rows = list(csv.DictReader((ROOT / "data/task_tables.csv").open()))
except Exception as e:
    rows = []; check("read data/task_tables.csv", False, str(e))
csv_names = {}
for r in rows: csv_names.setdefault(r["isco_code"], set()).add(r["occupation"])
check(f"task_tables.csv has one row per task ({T})", len(rows) == T, f"{len(rows)} rows")
check("task_tables.csv occupation names equal the dataset", set(csv_names) == set(by_code) and all(v == {by_code[c]["display_name"]} for c, v in csv_names.items()))
per = collections.Counter(r["isco_code"] for r in rows)
check("task_tables.csv task counts per occupation equal the dataset", all(per[c] == len(o["task_decomposition"]) for c, o in by_code.items()))

CT = bundle["capability_trajectory"]; VEC = ["C_R", "C_G", "P_A", "Phi_S", "Phi_U", "S_E"]
expected_csv = []
for o in occ:
    for t in o["task_decomposition"]:
        credit = round(1 / (1 + math.exp(-8 * (CT[t["vector"]]["2026"]["mid"] - t["difficulty_threshold"]))), 3)
        expected_csv.append(dict(isco_code=str(o["isco_code"]), occupation=o["display_name"], task=t["task_name"],
                                 vector=t["vector"], difficulty_threshold=str(t["difficulty_threshold"]),
                                 time_weight_pct=str(t["time_weight_pct"]), machine_credit_2026=str(credit)))
check("task CSV: every task and numeric cell equals the canonical inputs", rows == expected_csv)
def reach(o, year="2026"):
    tw = sum(t["weight"] for t in o["tasks"])
    return sum(t["weight"] / (1 + math.exp(-8 * (CT[t["vector"]][year]["mid"] - t["diff"]))) for t in o["tasks"]) / tw
b_by = {o["isco"]: o for o in bundle["occupations"]}
check("bundle has exactly one record for every canonical occupation", len(bundle["occupations"]) == len(occ) and set(b_by) == set(by_code))
bundle_bad = []
for c, o in by_code.items():
    b = b_by.get(c, {})
    expected_tasks = [dict(name=t["task_name"], short=t.get("task_short"), vector=t["vector"],
                           diff=t["difficulty_threshold"], weight=t["time_weight_pct"]) for t in o["task_decomposition"]]
    expected = dict(tasks=expected_tasks, territory_id=o["territory_id"], employment_weight_pct=o["employment_weight_pct"],
                    barrier=o["primary_barrier"], barrier_note=o.get("key_barrier_note"))
    for y in (2026, 2030, 2035, 2040):
        expected[f"r{y}"] = o[f"replaceability_{y}" + ("" if y == 2026 else "_moderate")]
        expected[f"disp{y}"] = o[f"displacement_{y}_moderate"]
    if any(b.get(k) != v for k, v in expected.items()): bundle_bad.append(c)
check("bundle task inputs, scores, weights and barriers equal the dataset", not bundle_bad, str(bundle_bad[:5]))
bad_og = [k for k in b_by if k not in og or og[k].get("n") != b_by[k]["name"] or og[k].get("r") != js_round(100 * reach(b_by[k]))]
check("OG manifest: every occupation present, name and % equal the bundle's task math", not bad_og and len(og) == len(b_by), f"{len(bad_og)} wrong, e.g. {bad_og[:4]}")
check("bundle task math reproduces the dataset's 2026 scores", all(abs(round(100 * reach(b_by[c]), 1) - o["replaceability_2026"]) <= 0.1001 for c, o in by_code.items()))

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

# ── 5. the homepage admits every share-bearing record type — and USES the set ─
index_html = text("index.html")
m = re.search(r"LABOR_SHARE_TYPES\s*=\s*new Set\(\[([^\]]*)\]\)", index_html)
if m:
    admitted = set(re.findall(r"'([^']+)'", m.group(1)))
else:  # legacy form: if (rec.data_type === 'a' || rec.data_type === 'b' …) { … laborLookup
    legacy = re.search(r"if \(((?:rec\.data_type === '[^']+'(?: \|\| )?)+)\) \{\s*// For macro categories", index_html)
    admitted = set(re.findall(r"'([^']+)'", legacy.group(1))) if legacy else set()
present = {r["data_type"] for r in labor}
check("index.html declares LABOR_SHARE_TYPES", bool(m))
check("index.html uses LABOR_SHARE_TYPES for BOTH the share lookup and the workforce totals",
      len(re.findall(r"LABOR_SHARE_TYPES\.has\(rec\.data_type\)", index_html)) >= 2 and "rec.data_type === 'historical' ||" not in index_html)
check("no labor data_type is silently dropped by the homepage", present <= admitted | NON_SHARE_TYPES, f"unhandled: {sorted(present - admitted - NON_SHARE_TYPES)}")
check("the homepage never admits an additive patch as a share", not (admitted & NON_SHARE_TYPES), f"{sorted(admitted & NON_SHARE_TYPES)}")
newest = max(r["year"] for r in labor if r["data_type"] not in NON_SHARE_TYPES)
have = {r["territory_id"] for r in labor if r["year"] == newest and r["data_type"] in admitted}
check(f"the homepage admits a {newest} share for every modern territory", modern <= have, f"missing {len(modern - have)} of {len(modern)}")

# ── 6. the documented replacement formula reproduces the stored fields ────────
rf = md["replacement_formula_v5"]
metadata_equation = "displacement_y = 100 * ( conversion_rate * max(0, r_y - r_2026)/100 + lag_schedule[y] * barrier_multipliers[primary_barrier] * (r_2026/100) * (1 - already_absorbed_era[era]) ), rounded to 0.1"
check("metadata equation states the calculation being checked", rf.get("equation", "").startswith(metadata_equation))
def era(b): return "post_2022" if b == "NONE" else ("y2015_2022" if b in ("REGULATORY", "HUMAN_PREFERENCE") else "pre_2015")
CHK = {2026: "replaceability_2026", 2030: "replaceability_2030_moderate", 2035: "replaceability_2035_moderate",
       2040: "replaceability_2040_moderate", 2041: "replaceability_2041_moderate"}
def disp(o, y, mult):
    r26, b = o["replaceability_2026"], o.get("primary_barrier", "NONE")
    return round((rf["conversion_rate"] * max(0, o[CHK[y]] - r26) / 100
                  + rf["lag_schedule"][str(y)] * mult.get(b, 1.0) * r26 / 100 * (1 - rf["already_absorbed_era"][era(b)])) * 100, 1)
n_chk = n_bad = 0
for o in occ:
    for y in CHK:
        stored = o.get(f"displacement_{y}_moderate")
        if stored is None or o.get(CHK[y]) is None: continue
        n_chk += 1; n_bad += abs(disp(o, y, rf["barrier_multipliers"]) - stored) > 0.1001
check(f"metadata.replacement_formula_v5 reproduces all {n_chk} stored displacement values", n_bad == 0 and n_chk == len(occ) * 5, f"{n_bad} differ")

# ── 7. published capability tables match the trajectory at printed precision ──
def table_rows(cells_iter):
    out = []
    for c in cells_iter:
        c = [strip_tags(x).replace("*", "").strip() for x in c]
        if len(c) == 7 and c[0].isdigit() and c[0] in CT["C_R"]: out.append(c)
    return out
html_full = text("methodology-full.html"); mdoc = text("docs/v5_methodology.md")
html_rows = table_rows(re.findall(r"<td[^>]*>(.*?)</td>", r, re.S) for r in re.findall(r"<tr[^>]*>(.*?)</tr>", html_full, re.S))
md_rows = table_rows(l.strip().strip("|").split("|") for l in mdoc.splitlines() if l.strip().startswith("|"))
for rel, rws, need in [("methodology-full.html", html_rows, 10), ("docs/v5_methodology.md", md_rows, 7)]:
    wrong = [(c[0], v, val) for c in rws for val, v in zip(c[1:], VEC)
             if abs(round(CT[v][c[0]]["mid"], len(val.split(".")[1]) if "." in val else 0) - float(val)) > 1e-9]
    yrs = {c[0] for c in rws}
    check(f"{rel}: capability table complete ({len(rws)} rows ≥ {need}, incl. 2025 and 2026)", len(rws) >= need and {"2025", "2026"} <= yrs, f"years: {sorted(yrs)}")
    check(f"{rel}: every capability cell matches the trajectory", not wrong, f"{wrong[:4]}")

# ── 8. the docs state the numbers the data has ────────────────────────────────
ev_years = [e["year"] for e in ds["technology_events"]]
lab_years = [r["year"] for r in labor if r["data_type"] not in NON_SHARE_TYPES]
codes = [str(o["isco_code"]) for o in occ]
plain = [c for c in codes if re.fullmatch(r"\d{4}", c)]; split = [c for c in codes if re.fullmatch(r"\d{4}-.+", c)]
other = [c for c in codes if c not in plain and c not in split]
tr = ds["territory_replaceability"]; displayed = sum(1 for o in occ if o.get("display_in_territory"))
hist = sum(len(v.get("occupations", [])) for v in (ds.get("historical_occupations") or {}).values())
readme = text("README.md")
for needle in [f"| {T:,} | {min(tasks)}–{max(tasks)} tasks per occupation", f"| Sources | {S:,} |", f"| Technology events | {E} | {int(min(ev_years))}–{int(max(ev_years))} |",
               f"| Labor shares | {len(labor)} | {min(lab_years)}–{max(lab_years)}", f"| Occupations (per-occupation scores) | {len(occ)} | {len(plain)} plain ISCO-08 4-digit codes + {len(split)} specialised splits across {len({c.split('-')[0] for c in split})} base codes",
               f"+ {len(other)} occupations with no ISCO-08 equivalent", f"| Replaceability scores (territory-level) | {len(tr)} |", f"| Displayed occupations (canvas) | {displayed} |",
               f"| Historical occupations | {hist} |", f"**{len(modern)} territories of work**"]:
    check(f"README states: {needle[:52]}…", needle in readme)
check("/about states task totals", f"({min(tasks)}–{max(tasks)} tasks per occupation, {T:,} total across {len(occ)} occupations)" in text("methodology.html"))
llms = text("llms.txt")
check("llms.txt states task and source totals", f"{T:,}" in llms and f"{S:,}" in llms)
check("llms.txt says thirteen territories, never fifteen", "thirteen territories" in llms and "fifteen" not in llms.lower())
check("llms.txt documents the deep link by ISCO code", "job=<ISCO-08 code>" in llms)
mb = (ROOT / "ai_reach_v5.0.json").stat().st_size / 1e6
sz = re.search(r"~\s*([\d.]+)\s*MB", llms)
check("llms.txt states the dataset's size within 10%", bool(sz) and abs(float(sz.group(1)) - mb) / mb <= 0.10, f"says {sz.group(1) if sz else '?'} MB, file is {mb:.1f} MB")
cff = text("CITATION.cff")
check("CITATION.cff: root type is dataset", bool(re.search(r"^type: dataset$", cff, re.M)))
check("CITATION.cff: dataset licence is CC-BY-4.0 (SPDX), not MIT", bool(re.search(r"^license: CC-BY-4\.0$", cff, re.M)) and not re.search(r"^license: MIT$", cff, re.M))
check("CITATION.cff: preferred-citation.type is a valid reference type ('data')", bool(re.search(r"preferred-citation:\n\s+type: data\n", cff)))
check(f"CITATION.cff abstract says {len(modern)} territories", f"across {len(modern)} territories of work" in cff)
check("citation identifies this dataset revision in both citation blocks",
      cff.count(f'version: "{md.get("citation_version")}"') == 2 and 'date-released: "2026-09-19"' in cff)

mults = rf["barrier_multipliers"]; ORDER = ["NONE", "ECONOMIC", "HUMAN_PREFERENCE", "REGULATORY", "HUMANOID_DEPENDENT"]
check("methodology-full prints the shipped barrier multipliers", "<br>".join(f"{k}: {mults[k]:.2f}" for k in ORDER) in html_full)
check("methodology-full prints the shipped lag schedule", "<br>".join(f"{y}: {round(100 * v)}%" for y, v in rf["lag_schedule"].items()) in html_full)
check("methodology-full prints the shipped conversion rate", f'<td>conversion_rate</td><td class="mono">{rf["conversion_rate"]:.2f}</td>' in html_full)
ab = rf["already_absorbed_era"]
check("methodology-full prints the shipped absorbed fractions", f"{ab['pre_2015']:.2f} pre-2015, {ab['y2015_2022']:.2f} for 2015–2022, {ab['post_2022']:.2f} post-2022" in html_full)
EQ1, EQ2 = "conversion_rate × max(0, replaceability_t − replaceability_2026)", "pending = replaceability_2026 × (1 − already_absorbed"
check("methodology-full prints the shipped equation", EQ1 in html_full and "lag(t) × barrier_multiplier(primary_barrier) × pending" in html_full and EQ2 in html_full)
check("v5_methodology.md prints the shipped equation and era rule", EQ1 in mdoc and "lag(t) × barrier_multiplier × pending" in mdoc and "NONE → post-2022" in mdoc)
check("Markdown prints the shipped conversion and lag parameters",
      f'conversion_rate = {rf["conversion_rate"]:.2f}' in mdoc and
      all(f'{round(100*v)}% in {y}' in mdoc for y,v in rf["lag_schedule"].items()))
check("current scoring descriptions consistently use logistic credit",
      'strict threshold used for near-term projections' not in mdoc and
      'continuous capability credit' in text('methodology.html'))
check("v5_methodology.md prints the shipped barrier multipliers, in prose and in the taxonomy table",
      all(f"{k}: {mults[k]:.2f} ×" in mdoc for k in ("HUMAN_PREFERENCE", "REGULATORY")) and all(f"Lag multiplier {mults[k]:.2f} ×" in mdoc for k in ("HUMAN_PREFERENCE", "REGULATORY")))
prop = rf.get("phase11_proposed_not_applied") or {}
for rel, t in [("docs/v5_methodology.md", mdoc), ("methodology-full.html", html_full)]:
    stale = [f"{v} ×" for v in prop.values() if re.search(rf"(multiplier|:)\s*{re.escape(str(v))} ×", t)]
    check(f"{rel}: the never-applied Phase 11 multipliers are not presented as values", not stale, f"{stale}")
barriers = collections.Counter(o.get("primary_barrier") for o in occ)
check("v5_methodology.md barrier taxonomy counts equal the data", all(re.search(rf"\*\*{k}\*\*.*\| {barriers[k]} \|", mdoc) for k in ORDER), f"{dict(barriers)}")

# numbers the 2026-09-19 correction published, re-derived here
alt = dict(mults, **prop)
chg = [o for o in occ if abs(disp(o, 2041, alt) - o["displacement_2041_moderate"]) > 0.1001]
mean_now = sum(o["displacement_2041_moderate"] for o in occ) / len(occ); mean_alt = sum(disp(o, 2041, alt) for o in occ) / len(occ)
phrase = f"change {len(chg)} occupations at 2041 and move the mean from {mean_now:.1f} to {mean_alt:.1f}"
check(f"Phase 11 what-if as published ({len(chg)} occupations, {mean_now:.1f} → {mean_alt:.1f})", phrase in html_full and phrase in mdoc)
share = {r["territory_id"]: r["global_workforce_share_pct"] for r in labor if r["year"] == newest and r["data_type"] not in NON_SHARE_TYPES}
W = {str(o["isco_code"]): share[o["territory_id"]] * (o.get("employment_weight_pct") or 0) / 100 for o in occ}; SW = sum(W.values())
wm = lambda f: sum(W[str(o["isco_code"])] * o[f] for o in occ) / SW
check(f"world-weighted 2026 mean as published ({wm('replaceability_2026'):.1f})", f"<strong>{wm('replaceability_2026'):.1f} for 2026</strong>" in html_full)
check(f"world-weighted 2041 mean as published ({wm('replaceability_2041_moderate'):.1f})", f"across the world workforce it is {wm('replaceability_2041_moderate'):.1f}" in html_full)
clog = text("docs/v5_changelog.md")
ls = []
for y in (1800, 1830, 1860):
    recs = [r for r in labor if r["year"] == y and r["data_type"] == "historical_macro"]
    ls.append(100 * next(r for r in recs if r["territory_id"] == "land_sea")["global_workers_millions"] / sum(r["global_workers_millions"] for r in recs))
check("changelog states the normalised pre-1870 Land & Sea shares", " / ".join(f"{v:.1f}" for v in ls) in clog)

# ── 9. statements about score thresholds hold ─────────────────────────────────
n5 = sum(o["replaceability_2026"] <= 5 for o in occ); n10 = sum(o["replaceability_2026"] < 10 for o in occ)
check(f"methodology-full: '{n5} occupations score r26 ≤ 5 and {n10} score below 10'", f"{n5} occupations score r26 ≤ 5 and {n10} score below 10" in html_full)
ex = re.search(r"score below 10 — [^(]*\(([^)]*)\)", html_full)
check("methodology-full names below-10 examples", bool(ex))
for w in ([x.strip() for x in ex.group(1).split(",")] if ex else []):
    hit = [o for o in occ if o["display_name"].lower().startswith(w.lower().rstrip("s"))]
    check(f"'below 10' example '{w}' scores below 10", bool(hit) and all(o["replaceability_2026"] < 10 for o in hit), f"{[(o['display_name'], o['replaceability_2026']) for o in hit]}")
check("methodology-full names ISCO 9112 by its current display name", f'is now "{by_code["9112"]["display_name"]}"' in html_full)

# The worksheet predates current task scores: verify only its stated, centred R².
try:
    fit = list(csv.DictReader((ROOT / "docs/fit_worksheet_2026-04-17.csv").open()))
    x = [float(r["phase5_replaceability"]) for r in fit]; y = [float(r["worksheet_coverage"]) for r in fit]
    xm, ym = sum(x)/len(x), sum(y)/len(y)
    slope = sum((a-xm)*(b-ym) for a,b in zip(x,y))/sum((a-xm)**2 for a in x)
    origin = sum(a*b for a,b in zip(x,y))/sum(a*a for a in x)
    fm = dict(NONE=.82, HUMAN_PREFERENCE=.47, REGULATORY=.38, HUMANOID_DEPENDENT=.05)
    predictions = [[ym+slope*(a-xm) for a in x], [origin*a for a in x],
                   [a*fm[r["barrier"]] for a,r in zip(x,fit)]]
    r2 = [1-sum((a-b)**2 for a,b in zip(y,p))/sum((a-ym)**2 for a in y) for p in predictions]
    check("archived worksheet reproduces the three stated centred R² values",
          len(fit) == 28 and [round(v,2) for v in r2] == [.61,.56,.78], str(r2))
except Exception as e:
    check("read and calculate archived fit worksheet", False, str(e))
check("current method distinguishes worksheet arithmetic from model validation",
      all('earlier Phase 5 scores' in t and 'not the displacement multipliers above' in t for t in (html_full, mdoc)))

# ── 10. deep links never default silently ─────────────────────────────────────
shim = text("api/mirror-og.js")
check("OG shim guards manifest lookups against prototype keys", "hasOwnProperty.call" in shim and "own(manifest, job)" in shim)
node = shutil.which("node")
for rel in ["mirror/desktop.html", "mirror/mobile.html"]:
    h = text(rel)
    fn = re.search(r"function resolveJobParam\(v\)\{.*?\n\}", h, re.S)
    check(f"{rel}: resolver present, Nurse only when no ?job= is given", bool(fn) and "let FOCAL_ISCO=_resolved||'2221'" in h and "if(_jobMiss){" in h and "?_want:'2221'" not in h)
    if not (fn and node):
        if not node: skipped.append(f"{rel} resolver execution (node not found)")
        continue
    nm = collections.Counter(fold(o["name"]) for o in bundle["occupations"])
    uniq = next(o for o in bundle["occupations"] if "-" in o["name"] and nm[fold(o["name"])] == 1)
    al = collections.defaultdict(set)
    for o in bundle["occupations"]:
        for t in o.get("common_titles") or []: al[fold(t)].add(o["isco"])
    amb = next(k for k, v in al.items() if len(v) > 1 and k not in nm)
    cases = {"2221": "2221", "nurse": "2221", "NURSE": "2221", "xdata_sci": "XDATA_SCI", uniq["name"]: uniq["isco"], amb: None, "zzzz-not-a-job": None, "": None}
    js = ("const DATA=JSON.parse(require('fs').readFileSync(process.argv[1],'utf8').replace(/^[^=]*=/,'').trim().replace(/;$/,''));\n"
          + fn.group(0) + "\nconst C=" + json.dumps(cases) + ";const bad=Object.entries(C).filter(([k,v])=>resolveJobParam(k)!==v).map(([k,v])=>k+'→'+resolveJobParam(k)+' (want '+v+')');"
          "console.log(JSON.stringify(bad));")
    try:
        out = subprocess.run([node, "-e", js, str(ROOT / "mirror/mirror_data.js")], capture_output=True, text=True, timeout=60)
        bad = json.loads(out.stdout.strip() or json.dumps(["no output: " + out.stderr.strip()[:80]]))
    except Exception as e:
        bad = [f"{type(e).__name__}: {e}"]
    check(f"{rel}: resolver executed — code, name, any-case, hyphenated name resolve; ambiguous alias and junk do not", not bad, f"{bad}")

if node:
    try:
        result = subprocess.run([node, str(ROOT / "scripts/check_homepage.cjs")], capture_output=True, text=True, timeout=30)
        check("homepage functions: historical partition, macro transitions and workforce regression", result.returncode == 0, result.stderr[-1000:])
    except Exception as e:
        check("homepage function execution", False, str(e))
else:
    check("node is required for homepage and resolver release checks", False)

finish()
