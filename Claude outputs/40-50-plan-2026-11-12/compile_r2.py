"""Compile the 12 Nov 2026 Wowhead page pull (ITEM / QUEST / NPC lines) into the repo's data files.

  data/drop_rates.json            item pages (dropped-by count/outof) + single-dropper tooltip Drop Chance for the round-2 pool
  data/wowhead_quest_links.json   quick-facts rows for the quests QuestieDB leaves unlinked or Wowhead lists without a side
  tooling/trainer_costs.json      the 26 trainer / vendor pages, re-pulled
Usage: python compile_r2.py <repo root> <pages.tsv> <pool dir> <date>
"""
import sys, os, re, json
ROOT, PAGES, PD, TODAY = sys.argv[1:5]
ITEMS, QUESTS, NPCS = {}, {}, {}
for line in open(PAGES, encoding='utf-8'):
    p = line.rstrip('\n').split('\t', 2)
    if len(p) == 3: {'ITEM': ITEMS, 'QUEST': QUESTS, 'NPC': NPCS}[p[0]][p[1]] = json.loads(p[2])
Q = json.load(open(os.path.join(ROOT, 'tooling/qdb/quest.json'), encoding='utf-8'))
I = json.load(open(os.path.join(ROOT, 'tooling/qdb/item.json'), encoding='utf-8'))
owner = {}
for qid, r in Q.items():
    if r[9] and len(r[9]) > 2 and r[9][2]:
        for it in r[9][2]: owner.setdefault(str(it[0]), []).append(int(qid))

# ---- drop rates
path = os.path.join(ROOT, 'data', 'drop_rates.json')
D = json.load(open(path, encoding='utf-8'))
before = dict(D['items'])
n_new = n_upd = 0
for iid, d in ITEMS.items():
    rec = {'name': (I.get(iid) or [d['title'].split(' - ')[0]])[0], 'quests': owner.get(iid, []),
           'source': f'wowhead.com/forever/item page, dropped-by listview (count/outof), {TODAY}'}
    rows = [{'id': r['id'], 'name': r['name'], 'count': r['count'], 'outof': r['outof']} | ({'elite': True} if r.get('classification') in (1, 2, 3) else {})
            for r in d.get('npcs', []) if (r.get('outof') or 0) > 0]
    tc, to = sum(r['count'] for r in rows), sum(r['outof'] for r in rows)
    rec['npcs'] = rows; rec['overall_pct'] = round(100 * tc / to, 1) if to else None
    if d.get('objects'): rec['objects'] = d['objects']
    if not rows and not d.get('objects'): rec['note'] = 'NO DROPPED-BY' if d.get('nodrop') else 'dropped-by rows carry no sample'
    if iid in D['items']: n_upd += 1
    else: n_new += 1
    D['items'][iid] = rec
tips = json.load(open(os.path.join(ROOT, 'weights', 'tooltips', TODAY + '.json'), encoding='utf-8'))
pool = json.load(open(os.path.join(PD, '_pool.json'), encoding='utf-8'))
want = {str(it['id']) for q in pool.values() for it in q['items'] if it['mobs'] and not it['objects'] and not it['vendors']}
n_tip = 0
for name, rec in tips.items():
    if not isinstance(rec, dict): continue
    iid = str(rec.get('id'))
    m = re.search(r'Drop Chance:?\s*([\d.]+)%', rec.get('tooltip', ''))
    if m and iid in want and iid not in ITEMS:
        db = re.search(r'Dropped by:? ([^|]+)', rec['tooltip'])
        new = {'name': name, 'quests': owner.get(iid, []), 'source': f'nether.wowhead.com/forever/tooltip (single dropper), {TODAY}',
               'dropped_by': db.group(1).strip() if db else None, 'overall_pct': float(m.group(1))}
        if D['items'].get(iid) != new: n_tip += 1
        D['items'][iid] = new
if 'round-2' not in D['_source']:
    D['_source'] += f' {TODAY}: the quest items of the round-2 (42-50) candidates were added or re-pulled the same way; each row\'s "source" carries its own pull date, and rows still dated 11 Nov were not re-pulled.'
D['items'] = dict(sorted(D['items'].items(), key=lambda kv: int(kv[0])))
json.dump(D, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'drop_rates: {len(before)} -> {len(D["items"])} items; item pages new {n_new}, re-pulled {n_upd}; tooltip rows written {n_tip}')
moved = []
for iid in ITEMS:
    a, b = before.get(iid, {}).get('overall_pct'), D['items'][iid].get('overall_pct')
    if a is not None and b is not None and abs(a - b) >= 3: moved.append(f"{iid} {D['items'][iid]['name']} {a} -> {b}")
print('   re-pulled rates that moved 3+ points:', moved or 'none')

# ---- quest links
path = os.path.join(ROOT, 'data', 'wowhead_quest_links.json')
L = json.load(open(path, encoding='utf-8'))
def render(L):
    out = ['{', ' "_source": ' + json.dumps(L['_source'], ensure_ascii=False) + ',', ' "pulled": ' + json.dumps(L['pulled']) + ',', ' "quests": {']
    ks = sorted(L['quests'], key=int)
    for i, k in enumerate(ks): out.append(f'  "{k}": ' + json.dumps(L['quests'][k], ensure_ascii=False) + (',' if i < len(ks) - 1 else ''))
    return '\n'.join(out + [' }', '}']) + '\n'
same = render(L) == open(path, encoding='utf-8').read()
print('quest links: round trip of the existing file is byte-identical:', same)
def ends(f, word):
    m = re.search(word + r': (.*?)\[/li\]', f)
    return [t[0] + i for t, i in re.findall(r'/forever/(npc|object|item)=(\d+)', m.group(1))] if m else []
added = []
for qid, d in QUESTS.items():
    f = d['facts']
    lv = re.search(r'Level: (\d+)', f); rq = re.search(r'Requires level (\d+)', f); sd = re.search(r'Side: (?:\[span[^\]]*\])?([A-Za-z]+)', f)
    series = [int(x) if x != 'SELF' else int(qid) for x in d.get('series', [])]
    row = {'level': int(lv.group(1)) if lv else None, 'reqlevel': int(rq.group(1)) if rq else None, 'side': sd.group(1) if sd else None,
           'start': ends(f, 'Start'), 'end': ends(f, 'End'), 'series': [series] if series else [], 'pulled': TODAY}
    L['quests'][qid] = row; added.append(f"{qid} {d['title'].split(' - Quest')[0]}: side {row['side']} start {row['start']} end {row['end']}" + (f" series {series}" if series else ''))
if 'round-2' not in L['_source']:
    L['_source'] += f' {TODAY}: 19 quests of the round-2 (42-50) pool added the same way (rows carry "pulled"); the file\'s "pulled" stays the date of the oldest rows.'
if same: open(path, 'w', encoding='utf-8', newline='\n').write(render(L))
else: print('   NOT WRITTEN: layout differs, add the rows by hand')
for a in added: print('   ' + a)

# ---- trainers
path = os.path.join(ROOT, 'tooling', 'trainer_costs.json')
T = json.load(open(path, encoding='utf-8'))
def row(x):
    name, rank = x['name'], x.get('rank')
    if isinstance(rank, str):
        rank = rank.strip(); m = re.fullmatch(r'(?:Rank|Tier) (\d+)', rank)
        if m: rank = int(m.group(1))
        elif rank in ('Apprentice', 'Journeyman', 'Expert', 'Artisan', 'Master', 'Grand Master'):
            if not name.startswith(rank + ' '): name = rank + ' ' + name
            rank = None
        else: rank = None
    return {'id': x['id'], 'name': name, 'rank': rank, 'level': x.get('level') or x.get('learnedat'), 'cost': x.get('cost')}
js = lambda v: json.dumps(v, ensure_ascii=False)
def render_t(T):
    lines = ['{', ' ' + js('_source') + ': ' + js(T['_source']) + ',']
    items = sorted(((k, v) for k, v in T.items() if k != '_source'), key=lambda kv: (kv[0] != '258098', int(kv[0])))
    for i, (nid, v) in enumerate(items):
        lines.append(' ' + js(nid) + ': {"name": ' + js(v['name']) + ', "pulled": ' + js(v['pulled']) + ', "spells": [')
        for j, s in enumerate(v['spells']): lines.append('  ' + js(s) + (',' if j < len(v['spells']) - 1 else ''))
        if v.get('sells'):
            lines.append(' ], "sells": [')
            for j, s in enumerate(v['sells']): lines.append('  ' + js(s) + (',' if j < len(v['sells']) - 1 else ''))
        lines.append(' ]}' + (',' if i < len(items) - 1 else ''))
    return '\n'.join(lines + ['}']) + '\n'
same_t = render_t(T) == open(path, encoding='utf-8').read()
print('trainer costs: round trip of the existing file is byte-identical:', same_t)
chg = []
for nid in [k for k in T if k != '_source']:
    d = NPCS.get(nid)
    if not d: continue
    spells, seen = [], set()
    for x in d['spells']:
        s = row(x); k = (s['id'], s['name'], s['rank'])
        if k not in seen: seen.add(k); spells.append(s)
    sells = [x for x in d.get('sells', []) if x.get('cost') is not None]
    old = T[nid]
    okey = {(s['id'], s['name'], s['rank']): (s['level'], s['cost']) for s in old['spells']}; nkey = {(s['id'], s['name'], s['rank']): (s['level'], s['cost']) for s in spells}
    diff = [f"{k[1]} {okey.get(k)} -> {nkey.get(k)}" for k in sorted(set(okey) | set(nkey), key=str) if okey.get(k) != nkey.get(k)]
    osell = {x['id']: x['cost'] for x in old.get('sells', [])}; nsell = {x['id']: x['cost'] for x in sells}
    if osell != nsell: diff.append(f"sells {len(osell)} -> {len(nsell)} rows")
    if diff: chg.append(f"{nid} {old['name']}: {len(diff)} differences: " + '; '.join(diff[:6]))
    T[nid] = {'name': old['name'], 'pulled': TODAY, 'spells': spells, **({'sells': sells} if sells else {})}
if f'{TODAY}: re-pulled' not in T['_source']: T['_source'] += f' {TODAY}: re-pulled every trainer after client build 1.60.1.70938.'
if same_t: open(path, 'w', encoding='utf-8', newline='\n').write(render_t(T))
else: print('   NOT WRITTEN: layout differs')
print('   trainers with a changed row:', chg or 'none')

# ---- mob pages: level and classification for the working papers
print('mob pages:')
for nid, d in NPCS.items():
    if nid in T: continue
    f = d['facts']; lv = re.search(r'Level: ([\d\- ?]+)', f); cl = re.search(r'Classification: ([A-Za-z ]+)', f)
    mp = re.search(r'"count":(\d+),"coords":\[\[([\d.]+),([\d.]+)\].*?"uiMapName":"([^"]+)"', d.get('map', ''))
    print(f"   {nid} {d['title'].split(' - NPC')[0]} | level {lv.group(1).strip() if lv else '?'} | {cl.group(1).strip() if cl else 'Normal'} | " + (f"{mp.group(4)} {mp.group(2)},{mp.group(3)} ({mp.group(1)} points)" if mp else 'no map'))
