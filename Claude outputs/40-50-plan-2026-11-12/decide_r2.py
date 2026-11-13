"""Apply RULES.md rules 2, 3, 11, 12, 13 to the round-2 pool and print a verdict per quest.

Usage: python decide_r2.py <repo root> <pool dir> [pulled pages .tsv ...]
Reads <pool dir>/_pool.json (pool_r2.py), data/drop_rates.json, the newest weights/tooltips file, and any pulled-page
files (ITEM / QUEST / NPC lines from the browser). Writes <pool dir>/_decisions.tsv and _review.txt.

Verdicts: PLAIN | DUN-normal | DUN-grind | GROUP? (elite or group outside a dungeon: optional only for a scored upgrade) |
OPT? (drop 30-60%: optional only for an upgrade or when the route's kills cover it) | RATE? (no rate yet) | HOLD (side
unknown / needs a look) | LINK (0 XP chain step a kept quest needs) | OUT <reason>.
"""
import sys, os, re, json, glob, collections
ROOT, PD = sys.argv[1], sys.argv[2]
P = {int(k): v for k, v in json.load(open(os.path.join(PD, '_pool.json'), encoding='utf-8')).items()}
DR = json.load(open(os.path.join(ROOT, 'data', 'drop_rates.json'), encoding='utf-8'))['items']
WLq = json.load(open(os.path.join(ROOT, 'data', 'wowhead_quest_links.json'), encoding='utf-8'))['quests']
ITEMS, QPAGES, NPAGES = {}, {}, {}
QDB = json.load(open(os.path.join(ROOT, 'tooling', 'qdb', 'quest.json'), encoding='utf-8'))
NDB = json.load(open(os.path.join(ROOT, 'tooling', 'qdb', 'npc.json'), encoding='utf-8'))
def qdb_side(qid):
    r = QDB.get(str(qid))
    if not r: return None
    races = r[5] if len(r) > 5 else None
    if races:
        a, h = races & 77, races & 178
        return 'Alliance' if a and not h else 'Horde' if h and not a else 'Both'
    fr = [NDB.get(str(n), [None] * 13)[12] for n in ((r[1] or [[]])[0] or []) + ((r[2] or [[]])[0] or [])]
    fr = [x for x in fr if x]
    if fr and all(x == 'H' for x in fr): return 'Horde'
    if fr and all('A' in x for x in fr): return 'Both' if any(x == 'AH' for x in fr) else 'Alliance'
    return None
for fn in sys.argv[3:]:
    for line in open(fn, encoding='utf-8'):
        p = line.rstrip('\n').split('\t')
        if len(p) < 3: continue
        try: d = json.loads(p[2])
        except Exception: continue
        {'ITEM': ITEMS, 'QUEST': QPAGES, 'NPC': NPAGES}.get(p[0], {})[int(p[1])] = d
ELITE_WORDS = ('Elite', 'Rare Elite', 'Boss')
def npc_class(i):
    d = NPAGES.get(i)
    if not d: return None
    m = re.search(r'Classification: ([A-Za-z ]+)', d.get('facts', ''))
    return m.group(1).strip() if m else 'Normal'
def side_of(qid):
    d = QPAGES.get(qid)
    if d:
        f = d.get('facts', '')
        m = re.search(r'Side: (?:\[span[^\]]*\])?(Alliance|Horde|Both)', f)
        if m: return m.group(1)
        return 'none listed'
    e = WLq.get(str(qid))
    return e.get('side') if e else None
def item_rate(it):
    """(rate %, how) for a mob-only objective item: per-item page pull first, then drop_rates.json, then the tooltip rate."""
    d = ITEMS.get(it['id'])
    if d and not d.get('missing'):
        rows = [r for r in d.get('npcs', []) if (r.get('outof') or 0) > 0]
        if rows:
            tc, to = sum(r['count'] for r in rows), sum(r['outof'] for r in rows)
            best = max(rows, key=lambda r: r['count'] / r['outof'])
            return round(100 * tc / to, 1), f"{len(rows)} droppers, best {best['name']} {100 * best['count'] / best['outof']:.0f}% of {best['outof']}"
    e = DR.get(str(it['id']))
    if e and e.get('overall_pct') is not None: return e['overall_pct'], 'drop_rates.json 11 Nov'
    if it.get('rate') is not None: return it['rate'], 'tooltip'
    return None, 'no rate'
V = {}
def base(q):
    f = q['flags']; qid = q['id']
    if 'SIDE?' in f:
        s = side_of(qid)
        if s == 'Horde': return 'OUT', 'Horde (Wowhead quest page)'
        if s not in ('Alliance', 'Both'):
            s2 = qdb_side(qid)
            if s2 == 'Horde': return 'OUT', 'Horde (QuestieDB race mask / giver faction)'
            if s2 not in ('Alliance', 'Both'): return 'HOLD', f'side not stated on Wowhead ({s}) or in the DB'
    if 'RAID' in f or 'PVP' in f or 'EVENT' in f: return 'OUT', 'raid / pvp / event'
    if 'SHAMAN' in f: return 'HOLD', 'class quest: place by hand'
    if 'NOSTART' in f:
        d = QPAGES.get(qid)
        if not d or not re.search(r'Start: ', d.get('facts', '')): return 'HOLD', 'no starter in the DB or on the Wowhead quest page'
    rates = []
    for it in q['items']:
        if it['mobs'] and not it['objects'] and not it['vendors']:
            r, how = item_rate(it); rates.append((r, how, it))
    dun = 'DUNGEON' in f
    if dun:
        if any(r is None for r, _, _ in rates): return 'DUN-rate?', '; '.join(f"{it['name']} {how}" for r, how, it in rates if r is None)
        low = [(r, it) for r, _, it in rates if r < 60]
        if low and all(len(it['mobs']) == 1 for r, it in low):
            return 'DUN-boss', 'held by one mob or boss; Wowhead reads ' + '; '.join(f"{it['name']} {r}%" for r, it in low) + ' over all kills, quest or not'
        if low: return 'DUN-grind', '; '.join(f"{it['name']} {r}% from {len(it['mobs'])} mob types" for r, it in low)
        return 'DUN-normal', ''
    elite = 'ELITE' in f
    typed = 'GROUP' in f and not elite
    for k in q['kills']:
        c = npc_class(k['id'])
        if c in ELITE_WORDS: elite = True
    for r, how, it in rates:
        cs = [npc_class(m) for m in it['mobs']]
        if cs and all(c in ELITE_WORDS for c in cs): elite = True
        rows = [x for x in (ITEMS.get(it['id'], {}).get('npcs') or DR.get(str(it['id']), {}).get('npcs') or []) if (x.get('outof') or 0) > 0]
        if rows and all(x.get('classification') in (1, 2, 3) or x.get('elite') for x in rows): elite = True
    if elite: return 'GROUP?', 'elite target outside a dungeon'
    if typed and (q['kills'] or rates): return 'GROUP?', 'typed Group on Wowhead; targets carry no elite rank in the data'
    if not q['xp'] and 'NOXP' in f: return 'NOXP', 'no XP on Wowhead'
    if q.get('skill'): return 'HOLD', f"needs skill {q['skill']}"
    if q.get('rep'): return 'HOLD', f"needs reputation {q['rep']}"
    if rates:
        if any(r is None for r, _, _ in rates): return 'RATE?', '; '.join(f"{it['name']} [{it['id']}] {len(it['mobs'])} mobs" for r, how, it in rates if r is None)
        r, how, it = min(rates, key=lambda x: x[0])
        need = it.get('count')
        txt = f"{it['name']} {r}% ({how})" + (f", {need} needed, ~{round(need / (r / 100))} kills" if need and r else '')
        if r >= 60: return 'PLAIN', txt
        if r >= 30: return 'OPT?', txt
        return 'OUT', 'drop under 30%: ' + txt
    return 'PLAIN', ''
for qid, q in P.items(): V[qid] = base(q)
AUTO = dict(V)
OVR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'overrides_r2.tsv')
if os.path.exists(OVR):
    for line in open(OVR, encoding='utf-8'):
        p = line.rstrip(chr(10)).split(chr(9))
        if len(p) == 3 and not line.startswith('#') and p[0].isdigit():
            if int(p[0]) in V: V[int(p[0])] = (p[1], p[2])
            else: print('override for a quest that is not in the pool:', p[0])
changed = True
while changed:                      # chain closure: a quest behind an OUT quest is out
    changed = False
    for qid, q in P.items():
        if V[qid][0] == 'OUT': continue
        dead = lambda p: (p in P and V[p][0] in ('OUT', 'JUDGE-OUT'))
        gone = [p for p in q.get('pre_all', []) if dead(p)]
        one = q.get('pre_one', [])
        if one and all(dead(p) for p in one): gone += one
        if gone:
            V[qid] = ('OUT', f"chain behind {gone[0]} {P[gone[0]]['name']} ({V[gone[0]][1][:40]})"); changed = True
changed = True
while changed:                      # a quest behind a "your call" or "round 3" quest waits with it
    changed = False
    for qid, q in P.items():
        if V[qid][0] in ('OUT', 'JUDGE-OUT', 'ASK', 'LATER', 'COND'): continue
        for tag in ('ASK', 'LATER', 'COND'):
            hit = [p for p in q.get('pre_all', []) if p in P and V[p][0] == tag]
            one = q.get('pre_one', [])
            if one and all(p in P and V[p][0] == tag for p in one): hit += one
            if hit:
                word = {'ASK': 'your call', 'LATER': 'left for round 3', 'COND': 'conditional'}[tag]
                V[qid] = (tag, f"behind {hit[0]} {P[hit[0]]['name']}, which is {word}"); changed = True; break
needed = set()                      # 0-XP steps and pre-chain steps that a kept quest needs
KEEP = ('PLAIN', 'DUN-normal', 'DUN-boss', 'DUN-grind')
def mark(qid):
    for p in P[qid].get('pre_all', []) + P[qid].get('pre_one', [])[:1]:
        if p in P and p not in needed: needed.add(p); mark(p)
for qid in P:
    if V[qid][0] in ('PLAIN', 'DUN-normal', 'DUN-boss', 'DUN-grind'): mark(qid)
for qid, q in P.items():
    if V[qid][0] == 'NOXP': V[qid] = ('LINK', 'chain step, no XP') if qid in needed else ('OUT', 'no XP, nothing kept behind it')
    if 'PRECHAIN' in q['flags'] and qid not in needed and V[qid][0] != 'OUT': V[qid] = ('OUT', 'below the bracket and nothing kept behind it')
# reward scores
sys.path.insert(0, os.path.join(ROOT, 'weights'))
import score_items as si
from profiles import PROFILES
central = PROFILES['enh'].weights(40)[0]
tips = {}
for fn in sorted(glob.glob(os.path.join(ROOT, 'weights', 'tooltips', '*.json'))):
    for name, rec in json.load(open(fn, encoding='utf-8')).items():
        if isinstance(rec, dict) and rec.get('id'): tips[int(rec['id'])] = (name, rec)
def scored(iid):
    t = tips.get(iid)
    if not t: return None
    try:
        it = si.parse(t[0], t[1])
        if not it: return None
        return {'name': t[0], 'slot': it.get('slot') or '?', 'ok': si.usable(it, 44)[0], 'score': round(si.score(it, central), 1), 'stats': si.fmt_stats(it), 'cls': it.get('cls') or ''}
    except Exception: return None
def best_reward(q):
    rs = [(s['score'], s) for s in (scored(i) for i in q['rew']) if s and s['ok'] and s['slot'] != '?']
    return max(rs, key=lambda x: x[0])[1] if rs else None
order = ['PLAIN', 'LINK', 'DUN-normal', 'DUN-boss', 'DUN-grind', 'GROUP-OPT', 'GATE', 'COND', 'ASK', 'LATER', 'R1FIX', 'JUDGE-OUT', 'RATE?', 'OPT?', 'GROUP?', 'HOLD', 'OUT']
with open(os.path.join(PD, '_decisions.tsv'), 'w', encoding='utf-8', newline='\n') as f:
    for qid, q in sorted(P.items(), key=lambda kv: (str(kv[1]['cat']), kv[1]['rq'], kv[1]['lv'], kv[0])):
        b = best_reward(q)
        f.write('\t'.join(map(str, [q['cat'], qid, q['name'], q['lv'], q['rq'], q['xp'], q['money'], V[qid][0], V[qid][1], ' '.join(q['flags']), q['maxlv'],
                                    f"{b['slot']} {b['score']} {b['name']} ({b['stats']})" if b else ''])) + '\n')
cats = collections.defaultdict(lambda: collections.defaultdict(lambda: [0, 0]))
for qid, q in P.items():
    c = cats[q['cat']][V[qid][0]]; c[0] += 1; c[1] += q['xp']
print(f"{'cat':>6} | " + ' | '.join(f"{o:>11}" for o in order))
tot = collections.defaultdict(lambda: [0, 0])
for cat, d in sorted(cats.items(), key=lambda kv: -sum(v[1] for k, v in kv[1].items() if k != 'OUT')):
    print(f"{str(cat):>6} | " + ' | '.join(f"{d[o][0]:3d} {d[o][1] // 1000:6d}k" if d[o][0] else ' ' * 11 for o in order))
    for o in order: tot[o][0] += d[o][0]; tot[o][1] += d[o][1]
print(f"{'all':>6} | " + ' | '.join(f"{tot[o][0]:3d} {tot[o][1] // 1000:6d}k" for o in order))
with open(os.path.join(PD, '_review.txt'), 'w', encoding='utf-8', newline='\n') as f:
    for o in ('RATE?', 'DUN-rate?', 'OPT?', 'GROUP?', 'HOLD', 'ASK', 'COND', 'GATE', 'GROUP-OPT', 'LATER'):
        f.write(f"\n== {o}\n")
        for qid, q in sorted(P.items(), key=lambda kv: (str(kv[1]['cat']), kv[0])):
            if V[qid][0] != o: continue
            b = best_reward(q)
            f.write(f"{q['cat']} {qid} {q['name']} L{q['lv']} req{q['rq']} xp {q['xp']} | {V[qid][1]}" + (f" | best reward: {b['slot']} {b['score']} {b['name']} [{b['cls']}] {b['stats']}" if b else '') + '\n')
print('pulled pages read: items', len(ITEMS), 'quests', len(QPAGES), 'npcs', len(NPAGES))
