// Paste/run in the browser console (or Claude's built-in browser javascript tool) on a
// https://www.wowhead.com/forever/zone=<id> page.  Returns the quest Listview as a TSV block
// that tooling/ingest_zone_tsv.py understands:
//   ZONE<TAB>/forever/zone=<id>/<slug>
//   id level reqlevel xp side category category2 type reqclass reqrace status money itemchoices itemrewards name
// Wowhead blocks scripted fetches (202 challenge page / CloudFront 403) but renders fine in a real browser.
// Pulling ~14 zones back-to-back trips a CloudFront 403 rate limit for a few minutes - pace it.
(() => {
  const h = document.documentElement.outerHTML;
  const i = h.indexOf("new Listview({template: 'quest', id: 'quests'");
  if (i < 0) return 'NOT READY ' + location.pathname + ' ' + document.title;
  const d = h.indexOf('data: [', i);
  let depth = 0, j = d + 6, inStr = false, esc = false;
  for (; j < h.length; j++) {
    const c = h[j];
    if (inStr) { if (esc) esc = false; else if (c === '\\') esc = true; else if (c === '"') inStr = false; continue; }
    if (c === '"') inStr = true; else if (c === '[') depth++; else if (c === ']') { depth--; if (depth === 0) break; }
  }
  const data = JSON.parse(h.slice(d + 6, j + 1));
  const ids = a => (a || []).map(x => Array.isArray(x) ? x[0] : x).join(',');
  return 'ZONE\t' + location.pathname + '\n' + data.map(q => [q.id, q.level, q.reqlevel, q.xp == null ? '' : q.xp,
    q.side == null ? '' : q.side, q.category, q.category2, q.type == null ? '' : q.type, q.reqclass || 0, q.reqrace || 0,
    (q.envChange || {}).status || '', q.money || 0, ids(q.itemchoices), ids(q.itemrewards), q.name].join('\t')).join('\n');
})()
