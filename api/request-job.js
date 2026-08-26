'use strict';
/* ============================================================================
   /api/request-job — "couldn't find my job" intake from the Mirror.

   POST {q, closest, page}. Appends the request as a comment on a rolling
   GitHub issue ("Job requests — The Mirror") when JOB_REQUESTS_GH_TOKEN is
   set; otherwise logs only. Always 200 {ok:true} to the client — the intake
   must never break the search UI. No PII stored: query text only, @-tokens
   redacted. No npm dependencies (Node 18+ global fetch).
   ========================================================================== */

const REPO = 'lamentierschweinchen/ai-reach';
const ISSUE_TITLE = 'Job requests — The Mirror';
const LABEL = 'job-requests';

let issueCache = null; // survives warm invocations

function clean(s, max) {
  if (typeof s !== 'string') return '';
  return s.replace(/[\u0000-\u001f\u007f]/g, ' ')
          .replace(/\S*@\S*/g, '[redacted]')
          .replace(/`/g, "'")
          .replace(/\s+/g, ' ').trim().slice(0, max);
}

async function gh(token, method, path, payload) {
  const r = await fetch(`https://api.github.com${path}`, {
    method,
    headers: {
      'Authorization': `Bearer ${token}`,
      'Accept': 'application/vnd.github+json',
      'User-Agent': 'mirror-job-requests',
      ...(payload ? { 'Content-Type': 'application/json' } : {}),
    },
    body: payload ? JSON.stringify(payload) : undefined,
  });
  if (!r.ok) throw new Error(`${method} ${path} -> ${r.status}`);
  return r.json();
}

async function fileRequest(token, q, closest, page) {
  if (issueCache === null) {
    const open = await gh(token, 'GET', `/repos/${REPO}/issues?state=open&per_page=100`);
    const found = open.find(i => i.title === ISSUE_TITLE && !i.pull_request);
    issueCache = found ? found.number
      : (await gh(token, 'POST', `/repos/${REPO}/issues`, {
          title: ISSUE_TITLE,
          labels: [LABEL],
          body: 'Occupation titles people looked for in the Mirror and did not find. '
              + 'Filed automatically by /api/request-job. Triage: extend common_titles '
              + 'for semantic gaps; consider new occupations for real ones.',
        })).number;
  }
  const line = `\`${q}\`` + (closest ? ` — closest shown: \`${closest}\`` : ' — no suggestion')
             + ` · ${page} · ${new Date().toISOString().slice(0, 10)}`;
  await gh(token, 'POST', `/repos/${REPO}/issues/${issueCache}/comments`, { body: line });
}

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') { res.statusCode = 405; return res.end('POST only'); }
  const b = req.body || {};
  if (b.hp) { res.statusCode = 200; return res.end(JSON.stringify({ ok: true })); } // honeypot
  const q = clean(b.q, 80);
  const closest = clean(b.closest, 80);
  const page = b.page === 'mobile' ? 'mobile' : 'desktop';
  if (q.length < 2) { res.statusCode = 400; return res.end(JSON.stringify({ ok: false })); }
  console.log('job-request', JSON.stringify({ q, closest, page }));
  let mode = 'logged';
  const token = process.env.JOB_REQUESTS_GH_TOKEN;
  if (token) {
    try { await fileRequest(token, q, closest, page); mode = 'filed'; }
    catch (e) { console.error('job-request GH error:', e.message); issueCache = null; }
  }
  res.statusCode = 200;
  res.setHeader('Content-Type', 'application/json');
  res.end(JSON.stringify({ ok: true, mode }));
};
