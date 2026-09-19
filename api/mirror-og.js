'use strict';
/* ============================================================================
   /api/mirror-og — serves /mirror.

   Same device-router shell as mirror/index.html (router script that preserves
   ?job=/#hash and forwards to /mirror/mobile or /mirror/desktop; noscript
   link; favicon; canonical), but with per-job Open Graph / Twitter meta when
   ?job=<isco or exact display name> resolves in mirror/og/manifest.json. Unknown or absent
   job falls back to the exact same generic meta mirror/index.html has today
   (og-mirror.png).

   No npm dependencies — only Node core (`url`) and the manifest JSON, which
   is required directly (it's tiny: {isco: {n, r}}, not the full data bundle).
   ========================================================================== */

const { URL } = require('url');
const manifest = require('../mirror/og/manifest.json');

const SITE = 'https://largelabormodel.com';
const GENERIC_OG_IMAGE = `${SITE}/mirror/og-mirror.png`;
const GENERIC_OG_IMAGE_ALT = 'The Mirror — how much of your job AI can technically do, across 480 jobs from 1970 to 2041.';
const SITE_DESCRIPTION = 'How much of your job can AI technically do? Look up any of 480 occupations — replaceability, not replacement.';

function escapeHTML(s) {
  return String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
}

/* ?job= accepts an ISCO code or an exact display name ("nurse"). Names that more
   than one occupation shares are left unresolved — a share card must never guess. */
const own = (o, k) => Object.prototype.hasOwnProperty.call(o, k);   // `?job=constructor` must not reach Object.prototype
const norm = s => String(s).toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();   // same folding as the Mirror pages
const CODE_INDEX = Object.create(null);
for (const isco of Object.keys(manifest)) CODE_INDEX[isco.toLowerCase()] = isco;
function nameIndex(pairs) {           // name -> isco, dropping any name more than one occupation shares
  const idx = Object.create(null), dup = new Set();
  for (const [name, isco] of pairs) { const k = norm(name); if (!k) continue; if (k in idx && idx[k] !== isco) dup.add(k); else idx[k] = isco; }
  for (const k of dup) delete idx[k];
  return idx;
}
const NAME_TO_ISCO = nameIndex(Object.entries(manifest).map(([isco, e]) => [e.n, isco]));
let DATASET_NAMES = null;             // the dataset's own (plural) display names — loaded only when the fast paths miss
function datasetNames() {
  if (DATASET_NAMES) return DATASET_NAMES;
  try {
    const idx = require('../data/occupations_index.json');
    DATASET_NAMES = nameIndex((idx.occupations || []).map(o => [o.name, String(o.isco_code)]).filter(([, c]) => own(manifest, c)));
  } catch (_) { DATASET_NAMES = Object.create(null); }
  return DATASET_NAMES;
}
function resolveJob(job) {
  if (!job) return null;
  const raw = String(job).trim();
  if (own(manifest, raw)) return raw;
  const byCode = CODE_INDEX[raw.toLowerCase()]; if (byCode) return byCode;
  const q = norm(raw); if (!q) return null;
  return NAME_TO_ISCO[q] || datasetNames()[q] || null;
}

/** Builds the <head> meta block — generic or per-job — as a string. */
function buildMeta(rawJob) {
  const job = resolveJob(rawJob);
  const entry = job && own(manifest, job) ? manifest[job] : null;

  if (!entry) {
    // Unknown/absent job: the existing generic meta, byte-for-byte as in mirror/index.html.
    return `<meta property="og:type" content="website">
<meta property="og:site_name" content="Large Labor Model">
<meta property="og:title" content="The Mirror · Large Labor Model">
<meta property="og:description" content="${escapeHTML(SITE_DESCRIPTION)}">
<meta property="og:url" content="${SITE}/mirror">
<meta property="og:image" content="${GENERIC_OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="${escapeHTML(GENERIC_OG_IMAGE_ALT)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="The Mirror · Large Labor Model">
<meta name="twitter:description" content="How much of your job can AI technically do? 480 jobs · replaceability, not replacement.">
<meta name="twitter:image" content="${GENERIC_OG_IMAGE}">
<meta name="twitter:image:alt" content="The Mirror — technical replaceability across 480 jobs.">`;
  }

  const { n: name, r: reach } = entry;
  const title = `${name} — ${reach}% technical replaceability`;
  const image = `${SITE}/mirror/og/${job}.png`;
  const imageAlt = `${name}: ${reach}% technical replaceability in 2026 — The Mirror, Large Labor Model.`;
  const url = `${SITE}/mirror?job=${encodeURIComponent(job)}`;

  return `<meta property="og:type" content="website">
<meta property="og:site_name" content="Large Labor Model">
<meta property="og:title" content="${escapeHTML(title)}">
<meta property="og:description" content="${escapeHTML(SITE_DESCRIPTION)}">
<meta property="og:url" content="${url}">
<meta property="og:image" content="${image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="${escapeHTML(imageAlt)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${escapeHTML(title)}">
<meta name="twitter:description" content="${escapeHTML(SITE_DESCRIPTION)}">
<meta name="twitter:image" content="${image}">
<meta name="twitter:image:alt" content="${escapeHTML(imageAlt)}">`;
}

/** The full document. Router script, noscript, favicon and canonical are
 *  verbatim from mirror/index.html and never change with ?job=. */
function renderHTML(job) {
  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>The Mirror · Large Labor Model</title>
<meta name="description" content="Technical replaceability of your job — a companion to the Large Labor Model.">
<link rel="canonical" href="${SITE}/mirror">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
${buildMeta(job)}
<style>html,body{margin:0;background:#efeae0;}</style>
<script>
  // Route to the device-appropriate build, preserving any ?job= / #section deep link.
  (function () {
    var small = window.matchMedia('(max-width: 820px)').matches
      || /Mobi|Android|iPhone|iPod|iPad/i.test(navigator.userAgent);
    // absolute base + extensionless (cleanUrls) so resolution never depends on a trailing slash
    var base = location.pathname.replace(/\\/(index)?$/, '') || '/mirror';
    var target = base + (small ? '/mobile' : '/desktop') + location.search + location.hash;
    location.replace(target);
  })();
</script>
</head>
<body>
<noscript style="font-family:Georgia,serif;padding:40px;max-width:640px;margin:0 auto;color:#1c1a17">
  The Mirror needs JavaScript. <a href="/mirror/desktop">Continue →</a>
</noscript>
</body>
</html>
`;
}

module.exports = (req, res) => {
  let job = null;
  try {
    const u = new URL(req.url, `http://${req.headers.host || 'localhost'}`);
    job = u.searchParams.get('job');
  } catch (_) {
    job = null;
  }

  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/html; charset=utf-8');
  res.setHeader('Cache-Control', 'public, s-maxage=86400, stale-while-revalidate=604800');
  res.end(renderHTML(job));
};
