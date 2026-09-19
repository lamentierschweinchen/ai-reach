/* Execute the homepage's actual lookup/aggregation functions against its dataset.
   No browser, network or dependencies. Also called by check_release.py. */
const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert');
const root=path.resolve(__dirname,'..'),h=fs.readFileSync(root+'/index.html','utf8'),data=JSON.parse(fs.readFileSync(root+'/ai_reach_v5.0.json','utf8'));
const section=(a,b)=>{const i=h.indexOf(a),j=h.indexOf(b,i);assert(i>=0&&j>i,`Missing source section ${a}`);return h.slice(i,j);};
const code=section('function buildLookupTables()','// ═══════════════════════════════════════════════════════════════\n// CONSTANTS')+
 section('const TERRITORIES =','const ERAS =')+section('const MACRO_SHAPES =','// ═══════════════════════════════════════════════════════════════\n// STATE')+
 section('function interp(','// Occupation score interpolation');
const ctx={V2:{...data,replaceability:data.territory_replaceability},laborLookup:{},laborProjected:{},macroLookup:{},workforceLookup:{},replLookup:{},replProjected:{},occupationsByTerritory:{},scenario:'moderate'};vm.createContext(ctx);
vm.runInContext(code+`;buildLookupTables(); this.parts = y => TERRITORIES.map(t=>getShareForId(t.id,y)*emergenceProgress(t.id,y)).concat(MACRO_SHAPES.map(m=>getShareForId(m.id,y)));`,ctx);
for(let y=1800;y<=2041;y+=.25){const total=ctx.parts(y).reduce((a,b)=>a+b,0);assert(Math.abs(total-100)<.1,`${y}: displayed partition ${total}`);}
for(const r of data.labor.filter(r=>r.year===2025)){for(const y of [2025,2026,2041])assert.equal(ctx.getShareForId(r.territory_id,y),r.global_workforce_share_pct);}
/* display cadence: shares are drawn at decade points + the newest year and the 1950 cross-section is skipped; totals stay annual */
const rec=(t,y)=>data.labor.find(r=>r.territory_id===t&&r.year===y&&r.data_type!=='modelled').global_workforce_share_pct,lin=(a,b,f)=>a+(b-a)*f,near=(a,b)=>Math.abs(a-b)<1e-9;
for(const t of data.labor.filter(r=>r.year===2025).map(r=>r.territory_id)){
 for(const y of [1870,1940,1960,1990,2000,2010,2020,2025])assert(near(ctx.getShareForId(t,y),rec(t,y)),`${t} ${y}: a drawn point must equal its record`);
 assert(near(ctx.getShareForId(t,1950),lin(rec(t,1940),rec(t,1960),.5)),`${t}: the 1950 cross-section must not be drawn`);
 assert(near(ctx.getShareForId(t,2011),lin(rec(t,2010),rec(t,2020),.1)),`${t}: 2011 must be drawn from the 2010 and 2020 points`);
 assert(near(ctx.getShareForId(t,2023),lin(rec(t,2020),rec(t,2025),.6)),`${t}: 2023 must be drawn from the 2020 and 2025 points`);
}
const total=y=>data.labor.filter(r=>r.year===y&&['historical','historical_macro','interpolated','derived_from_occupation'].includes(r.data_type)).reduce((s,r)=>s+r.global_workers_millions,0);
for(const y of [1950,2011,2024])assert(Math.abs(ctx.getWorkforce(y)-total(y))<1e-8,`${y}: workforce totals stay annual`);
for(let y=1981;y<=1989;y++)assert(Math.abs(ctx.getWorkforce(y)-(total(1980)+(total(1990)-total(1980))*(y-1980)/10))<1e-8);
assert(Math.abs(ctx.getShareForId('macro_services',1940)-29.315)<1e-8);
assert.equal(ctx.getShareForId('macro_industry',1903),0);assert.equal(ctx.getShareForId('macro_services',1983),0);
assert(!h.includes('getTerritoryShare(t, Math.max(1950, currentYear))'),'Panel must use the selected year');
assert(h.includes('areaShare: share * morphProgress')&&h.includes('s.areaShare / totalShare'),'Sizes must use the partition');
console.log('homepage: 965 quarterly partitions; modern endpoint holds; decade-point cadence; 1981–89 workforce; macro transitions passed');
