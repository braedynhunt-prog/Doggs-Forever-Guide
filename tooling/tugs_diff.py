#!/usr/bin/env python3
r"""Compare TUGs' Forever Alliance Guidelime route with our Guidelime_ForeverShaman guide.

Usage:  python3 tooling\tugs_diff.py <GuideLime_TUGs_Forever folder> [outdir]
Reads the atlas (data\quests.json + zone_*.json), Questie's Classic DB (tooling\qdb\quest.json) and
tooling\extra_quests.json (rows fetched from Wowhead for quests the atlas lacks; see wh_quests.py).
Writes <outdir>\tugs_vs_ours.tsv, tugs_20-35.tsv, tugs_diff_summary.md and unknown_quests.txt.
"""
import re, json, os, sys, glob, csv
from collections import OrderedDict, defaultdict

BASE = os.environ.get('FOREVER_ATLAS', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
OURS = os.path.join(BASE, 'guide', 'Guidelime_ForeverShaman')
TUGS = sys.argv[1]
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(BASE, 'compare')
os.makedirs(OUT, exist_ok=True)

Q = json.load(open(os.path.join(BASE, 'tooling', 'qdb', 'quest.json'), encoding='utf-8'))
WQ = {int(k): v for k, v in json.load(open(os.path.join(BASE, 'data', 'quests.json'), encoding='utf-8')).items()}
_extra = os.path.join(BASE, 'tooling', 'extra_quests.json')
EXTRA = {int(k): v for k, v in json.load(open(_extra, encoding='utf-8')).items()} if os.path.exists(_extra) else {}
ZONES = {z['id']: z['name'] for z in json.load(open(os.path.join(BASE, 'zones.json'), encoding='utf-8'))}
ZONES.update({1: 'Dun Morogh', 12: 'Elwynn Forest', 38: 'Loch Modan', 40: 'Westfall', 44: 'Redridge Mountains', 10: 'Duskwood',
              11: 'Wetlands', 148: 'Darkshore', 141: 'Teldrassil', 331: 'Ashenvale', 1537: 'Ironforge', 1519: 'Stormwind City',
              718: 'Wailing Caverns', 719: 'Blackfathom Deeps', 721: 'Gnomeregan', 717: 'The Stockade', 36: 'Alterac Mountains',
              45: 'Arathi Highlands', 33: 'Stranglethorn Vale', 267: 'Hillsbrad Foothills', 400: 'Thousand Needles',
              406: 'Stonetalon Mountains', 1657: 'Darnassus', 209: 'Shadowfang Keep', 491: 'Razorfen Kraul', 796: 'Scarlet Monastery',
              16919: 'The Hall of Thanes', 16611: 'Ruins of Lordaeron', 16544: 'Zephras Isle', 1581: 'The Deadmines', 85: 'Tirisfal Glades',
              14: 'Durotar', 17: 'The Barrens', 215: 'Mulgore', 3: 'Badlands', 8: 'Swamp of Sorrows', 15: 'Dustwallow Marsh',
              357: 'Feralas', 440: 'Tanaris', 47: 'The Hinterlands', 51: 'Searing Gorge', 405: 'Desolace', 490: "Un'Goro Crater",
              361: 'Felwood', 618: 'Winterspring', 28: 'Western Plaguelands', 139: 'Eastern Plaguelands', 46: 'Burning Steppes',
              4: 'Blasted Lands', 1377: 'Silithus', 16: 'Azshara', 130: 'Silverpine Forest', 2100: 'Maraudon', 1477: 'Sunken Temple',
              1176: "Zul'Farrak", 978: "Zul'Farrak", 1337: 'Uldaman', 1583: 'Blackrock Spire', 1584: 'Blackrock Depths',
              16560: 'Excavation Site: Wetlands', 16562: 'City of Dalaran', 16593: 'Shen\'dralas', 16632: 'The Riverglades', 16732: 'Mount Hyjal', 17191: 'The Drowned City'})
# zone rows (lightweight quest info incl. xp) + quest->zone map
ZQ = {}; QZ = defaultdict(list)
for zf in sorted(glob.glob(os.path.join(BASE, 'data', 'zone_*.json'))):
    z = json.load(open(zf, encoding='utf-8'))
    for q in z.get('quests', []):
        QZ[q['id']].append(z['id'])
        ZQ.setdefault(q['id'], q)

TAG = re.compile(r'\[([A-Z]+)\s*([^\]]*)\]')
RACES = {'dwarf': 'Dwarf', 'gnome': 'Gnome', 'human': 'Human', 'nightelf': 'Night Elf', 'night elf': 'Night Elf', 'skyborne': 'Skyborne'}
CLASSES = {'warrior', 'paladin', 'hunter', 'rogue', 'priest', 'shaman', 'mage', 'warlock', 'druid'}
RACE_BIT = {'Human': 1, 'Dwarf': 4, 'Night Elf': 8, 'Gnome': 64}
CLASS_BIT = {'Warrior': 1, 'Paladin': 2, 'Hunter': 4, 'Rogue': 8, 'Priest': 16, 'Shaman': 64, 'Mage': 128, 'Warlock': 256, 'Druid': 1024}

def restrict(text):
    races, classes = set(), set()
    for m in re.finditer(r'\[(?:A|GA) ([^\]]+)\]', text):
        for part in m.group(1).split(','):
            p = part.strip().lower()
            if p in RACES: races.add(RACES[p])
            elif p in CLASSES: classes.add(p.capitalize())
    return races, classes

def applies(r, race, cls):
    races, classes = r
    return (not races or race in races) and (not classes or cls in classes)

def rstr(r):
    races, classes = r
    return ','.join(sorted(races) + sorted(classes))

def parse_guide(path):
    txt = open(path, encoding='utf-8', errors='replace').read()
    body = txt.split('[[', 1)[1].rsplit(']]', 1)[0]
    name = re.search(r'^\[N\s*([^\]]*)\]', body, re.M)
    nx = re.search(r'^\[NX\s*([^\]]*)\]', body, re.M)
    ga = re.search(r'^\[GA ([^\]]+)\]', body, re.M)
    ga_r = restrict(ga.group(0)) if ga else (set(), set())
    events = []
    for ln, line in enumerate(body.split('\n'), 2):
        if not line.strip(): continue
        optional = bool(re.search(r'\[OC?\]', line))
        lr = restrict(line)
        r = (lr[0] or ga_r[0], lr[1] or ga_r[1])
        for m in TAG.finditer(line):
            code, payload = m.group(1), m.group(2).strip()
            if code in ('QA', 'QC', 'QT', 'QS'):
                mm = re.match(r'(\d+)', payload)
                if mm:
                    events.append(dict(file=os.path.splitext(os.path.basename(path))[0], ln=ln, code=code, qid=int(mm.group(1)),
                                       opt=optional, r=r, text=re.sub(r'\s+', ' ', line.strip())[:140]))
    return (name.group(1).strip() if name else '?', nx.group(1).strip() if nx else '', events)

def qinfo(qid):
    d = dict(id=qid, name='?', level='', req='', xp='', status='', zone='', side='', src='')
    zr = ZQ.get(qid)
    if zr:
        d.update(name=zr.get('name', '?'), level=zr.get('level', ''), req=zr.get('reqlevel', ''), xp=zr.get('xp', ''),
                 status=(zr.get('envChange') or {}).get('status', ''), side={1: 'A', 2: 'H', 3: 'both'}.get(zr.get('side'), ''), src='atlas')
        d['zone'] = ' / '.join(ZONES.get(z, str(z)) for z in QZ[qid])
    w = WQ.get(qid) or EXTRA.get(qid)
    if w:
        g = w.get('g') or {}
        if d['name'] in ('?', ''): d['name'] = w.get('name') or g.get('name') or '?'
        for k, gk in (('level', 'level'), ('req', 'reqlevel'), ('xp', 'xp')):
            if d[k] in ('', None) and g.get(gk) is not None: d[k] = g[gk]
        if not d['status']: d['status'] = (g.get('envChange') or {}).get('status', '')
        if not d['side']: d['side'] = {1: 'A', 2: 'H', 3: 'both'}.get(g.get('side'), '')
        if not d['zone'] and g.get('category'): d['zone'] = ZONES.get(g['category'], str(g['category']))
        if not d['src']: d['src'] = 'atlas' if qid in WQ else 'wowhead'
    r = Q.get(str(qid))
    if r:
        r = list(r) + [None] * 40
        if d['name'] in ('?', ''): d['name'] = r[0]
        if d['req'] in ('', None): d['req'] = r[3]
        if d['level'] in ('', None): d['level'] = r[4]
        if not d['zone'] and r[16] and r[16] > 0: d['zone'] = ZONES.get(r[16], str(r[16]))
        if not d['status']: d['status'] = 'classic'
        if not d['src']: d['src'] = 'questie'
        races = r[5] or 0; classes = r[6] or 0
        if races and not races & 77: d['side'] = d['side'] or 'H'
        d['qclass'] = ','.join(c for c, b in CLASS_BIT.items() if classes & b) if classes else ''
        d['qrace'] = ','.join(c for c, b in RACE_BIT.items() if races & b) if races and races != 77 else ''
    else:
        d['qclass'] = ''; d['qrace'] = ''
    if not d['src']: d['status'] = 'UNKNOWN'; d['src'] = '-'
    return d

# ---- chapters -------------------------------------------------------------------
TD = os.path.join(TUGS, 'TUGs', 'Alliance')
TUGS_DWARF = ['1-6 Coldridge Valley', '6-9 Dun Morogh', '9-11 Dun Morogh&Loch Modan', '11-14 Darkshore', '14-15 Westfall',
              '15-16 Halls of Thanes', '16-18 Loch Modan', '18-20 Darkshore']
TUGS_HUMAN = ['1-6 Northshire', '6-9 Elwynn Forest'] + TUGS_DWARF[2:]
TUGS_LATER = ['20-22 Ruins of Lordaeron&Deadmines', '22-23 Redridge Mountains', '23-24 Ashenvale', '24-25 Duskwood', '25-26 Stockades',
              '26-27 Redridge Mountains', '27-28 Ashenvale', '28-29 Blackfathom Depths', '29-30 Wetlands', '30-31 Duskwood', '31-32 Wetlands',
              '32-33 Excavation Site', '32-33 Stranglethorn Vale', '33-34 Gnomeregan', '34-35 Ashenvale']
tugs = OrderedDict()
for ch in TUGS_HUMAN[:2] + TUGS_DWARF + TUGS_LATER:
    tugs[ch] = parse_guide(os.path.join(TD, ch + '.lua'))
ours = OrderedDict()
for f in sorted(glob.glob(os.path.join(OURS, '[0-9]*.lua'))):
    k = os.path.splitext(os.path.basename(f))[0]
    ours[k] = parse_guide(f)

PERSONAS = [('Dwarf', 'Shaman'), ('Dwarf', 'Hunter'), ('Human', 'Hunter')]
OUR_CH = {'Dwarf': [k for k in ours if not k.startswith('00')], 'Human': [k for k in ours if not k.startswith('01')]}
TUGS_CH = {'Dwarf': TUGS_DWARF, 'Human': TUGS_HUMAN}

def collect(chapters, src, race, cls):
    """accepted: qid -> first chapter; turned: set; skipped: set (persona-filtered)."""
    acc, turned, skipped, order = OrderedDict(), set(), set(), []
    for ch in chapters:
        for e in src[ch][2]:
            if not applies(e['r'], race, cls): continue
            if e['code'] == 'QA' and e['qid'] not in acc: acc[e['qid']] = (ch, e)
            elif e['code'] == 'QT': turned.add(e['qid'])
            elif e['code'] == 'QS': skipped.add(e['qid'])
    return acc, turned, skipped

def xp_of(ids):
    tot, unknown = 0, 0
    for q in ids:
        x = qinfo(q)['xp']
        if x in ('', None): unknown += 1
        else: tot += int(x)
    return tot, unknown

# ---- main diff (per persona) ------------------------------------------------------
summary = []
unknown_ids = set()
all_rows = {}
for race, cls in PERSONAS:
    t_acc, t_turn, t_skip = collect(TUGS_CH[race], tugs, race, cls)
    o_acc, o_turn, o_skip = collect(OUR_CH[race], ours, race, cls)
    l_acc, l_turn, l_skip = collect(TUGS_LATER, tugs, race, cls)
    T, O = set(t_acc), set(o_acc)
    both, tonly, oonly = T & O, T - O, O - T
    txp = xp_of([q for q in T if q in t_turn]); oxp = xp_of([q for q in O if q in o_turn])
    tnew = sum(1 for q in T if qinfo(q)['status'] in ('new',)); onew = sum(1 for q in O if qinfo(q)['status'] in ('new',))
    tupd = sum(1 for q in T if qinfo(q)['status'] == 'updated'); oupd = sum(1 for q in O if qinfo(q)['status'] == 'updated')
    summary.append(dict(persona=f'{race} {cls}', tugs_acc=len(T), tugs_turn=len(T & t_turn), tugs_xp=txp[0], tugs_xp_unknown=txp[1], tugs_new=tnew, tugs_upd=tupd,
                        ours_acc=len(O), ours_turn=len(O & o_turn), ours_xp=oxp[0], ours_xp_unknown=oxp[1], ours_new=onew, ours_upd=oupd,
                        both=len(both), tugs_only=len(tonly), ours_only=len(oonly),
                        tugs_only_xp=xp_of(tonly)[0], ours_only_xp=xp_of(oonly)[0],
                        ours_only_tugs_later=sum(1 for q in oonly if q in l_acc)))
    for q in T | O:
        i = qinfo(q)
        if i['status'] == 'UNKNOWN' or i['xp'] in ('', None): unknown_ids.add(q)
        row = all_rows.setdefault(q, dict(qid=q, name=i['name'], zone=i['zone'], level=i['level'], req=i['req'], xp=i['xp'], status=i['status'],
                                          side=i['side'], qclass=i['qclass'], qrace=i['qrace'], src=i['src']))
        key = f'{race[0]}{cls[0]}'
        if q in t_acc: row[f'tugs_{key}'] = t_acc[q][0] + (' [O]' if t_acc[q][1]['opt'] else '') + (f" [A {rstr(t_acc[q][1]['r'])}]" if rstr(t_acc[q][1]['r']) else '')
        if q in o_acc: row[f'ours_{key}'] = o_acc[q][0] + (' [O]' if o_acc[q][1]['opt'] else '') + (f" [A {rstr(o_acc[q][1]['r'])}]" if rstr(o_acc[q][1]['r']) else '')
        if q in l_acc: row['tugs_later'] = l_acc[q][0]
        if q in t_skip or q in o_skip: row['skipped'] = ('tugs ' if q in t_skip else '') + ('ours' if q in o_skip else '')
        if q in T and q not in t_turn: row['tugs_no_turnin'] = 'x'
        if q in O and q not in o_turn: row['ours_no_turnin'] = 'x'

# bucket by the main persona (Dwarf Shaman) for the TSV ordering
def bucket(row):
    t, o = row.get('tugs_DS'), row.get('ours_DS')
    if t and o: return 'both'
    if t: return 'tugs-only'
    if o: return 'ours-only' + (' (TUGs later: %s)' % row['tugs_later'] if row.get('tugs_later') else '')
    return 'hunter/human-only step'
cols = ['bucket', 'qid', 'name', 'zone', 'level', 'req', 'xp', 'status', 'side', 'qclass', 'qrace', 'src',
        'tugs_DS', 'ours_DS', 'tugs_DH', 'ours_DH', 'tugs_HH', 'ours_HH', 'tugs_later', 'skipped', 'tugs_no_turnin', 'ours_no_turnin']
chapter_order = {ch: i for i, ch in enumerate(list(tugs.keys()) + list(ours.keys()))}
def sort_key(r):
    ref = (r.get('tugs_DS') or r.get('tugs_DH') or r.get('tugs_HH') or r.get('ours_DS') or r.get('ours_DH') or r.get('ours_HH') or '').split(' [')[0]
    return (bucket(r), chapter_order.get(ref, 99), r['zone'], r['level'] if isinstance(r['level'], int) else 99, r['qid'])
with open(os.path.join(OUT, 'tugs_vs_ours.tsv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=cols, delimiter='\t', extrasaction='ignore')
    w.writeheader()
    for r in sorted(all_rows.values(), key=sort_key):
        r['bucket'] = bucket(r); w.writerow(r)

# ---- TUGs 20-35 listing (Dwarf Shaman persona + class-free) ---------------------------------
with open(os.path.join(OUT, 'tugs_20-35.tsv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh, delimiter='\t')
    w.writerow(['chapter', 'order', 'qid', 'name', 'zone', 'level', 'req', 'xp', 'status', 'side', 'restrict', 'optional', 'in_ours_1-20', 'turned_in_same_chain'])
    later_rows = []
    chapter_stats = []
    o_all = set(q for k in ours for e in ours[k][2] if e['code'] == 'QA' for q in [e['qid']])
    for ch in TUGS_LATER:
        acc = OrderedDict(); turned = set(); n_restricted = 0
        for e in tugs[ch][2]:
            if e['code'] == 'QA':
                if not applies(e['r'], 'Dwarf', 'Shaman'):
                    n_restricted += 1; continue
                acc.setdefault(e['qid'], e)
            elif e['code'] == 'QT': turned.add(e['qid'])
        chain_turned = set(e['qid'] for c in TUGS_LATER for e in tugs[c][2] if e['code'] == 'QT')
        xp, unk = xp_of(acc)
        new = sum(1 for q in acc if qinfo(q)['status'] == 'new'); upd = sum(1 for q in acc if qinfo(q)['status'] == 'updated')
        unknown_ids.update(q for q in acc if qinfo(q)['status'] == 'UNKNOWN' or qinfo(q)['xp'] in ('', None))
        zones = defaultdict(int)
        for q in acc: zones[qinfo(q)['zone'].split(' / ')[0] or '?'] += 1
        chapter_stats.append(dict(chapter=ch, nx=tugs[ch][1], quests=len(acc), xp=xp, xp_unknown=unk, new=new, updated=upd, other_class_steps=n_restricted,
                                  zones=', '.join(f'{z} {n}' for z, n in sorted(zones.items(), key=lambda t: -t[1])), lines=len(tugs[ch][2])))
        for i, (q, e) in enumerate(acc.items(), 1):
            inf = qinfo(q)
            w.writerow([ch, i, q, inf['name'], inf['zone'], inf['level'], inf['req'], inf['xp'], inf['status'], inf['side'], rstr(e['r']), 'O' if e['opt'] else '',
                        'yes' if q in o_all else '', 'yes' if q in chain_turned else 'NO'])

# ---- summary markdown ---------------------------------------------------------------
L = []
L.append('# TUGs Forever 1.12 (file of 14 Oct 2026) vs Guidelime_ForeverShaman (25 Sep 2026)\n')
L.append('## Chapter chains\n')
L.append('TUGs Dwarf: ' + ' -> '.join(TUGS_DWARF) + '\n')
L.append('TUGs Human: ' + ' -> '.join(TUGS_HUMAN) + '\n')
L.append('TUGs 20-35: ' + ' -> '.join(TUGS_LATER) + '\n')
L.append('Ours Dwarf: ' + ' -> '.join(OUR_CH['Dwarf']) + '\n')
L.append('Ours Human: ' + ' -> '.join(OUR_CH['Human']) + '\n')
L.append('\nTUGs [NX] next-chapter links: ' + '; '.join(f"{ch} -> {tugs[ch][1] or '(none)'}" for ch in tugs) + '\n')
L.append('\n## Totals per persona (quests accepted in 1-20; XP = quests accepted and turned in, atlas/Wowhead XP at quest level)\n')
L.append('| persona | guide | accepted | turned in | XP | XP unknown | new Forever | updated | shared | only here | only-here XP |')
L.append('|---|---|---|---|---|---|---|---|---|---|---|')
for s in summary:
    L.append(f"| {s['persona']} | TUGs | {s['tugs_acc']} | {s['tugs_turn']} | {s['tugs_xp']} | {s['tugs_xp_unknown']} | {s['tugs_new']} | {s['tugs_upd']} | {s['both']} | {s['tugs_only']} | {s['tugs_only_xp']} |")
    L.append(f"| {s['persona']} | ours | {s['ours_acc']} | {s['ours_turn']} | {s['ours_xp']} | {s['ours_xp_unknown']} | {s['ours_new']} | {s['ours_upd']} | {s['both']} | {s['ours_only']} ({s['ours_only_tugs_later']} TUGs does later) | {s['ours_only_xp']} |")
L.append('\n## TUGs 20-35 chapters (Dwarf Shaman persona)\n')
L.append('| chapter | lines | quests | XP | XP unknown | new | updated | other-class pickups | zones |')
L.append('|---|---|---|---|---|---|---|---|---|')
for c in chapter_stats:
    L.append(f"| {c['chapter']} | {c['lines']} | {c['quests']} | {c['xp']} | {c['xp_unknown']} | {c['new']} | {c['updated']} | {c['other_class_steps']} | {c['zones']} |")
# lists
rows = sorted(all_rows.values(), key=sort_key)
def fmt(r): return f"- {r['qid']} {r['name']} ({r['zone'] or '?'}; L{r['level']} req {r['req']}; {r['xp'] or '?'} xp; {r['status']}{'; ' + r['qclass'] if r.get('qclass') else ''})"
L.append('\n## TUGs-only (Dwarf Shaman view), grouped by TUGs chapter\n')
cur = None
for r in rows:
    if bucket(r) != 'tugs-only': continue
    ch = r['tugs_DS'].split(' [')[0]
    if ch != cur: L.append(f'\n### {ch}\n'); cur = ch
    L.append(fmt(r) + (f"  <- {r['tugs_DS'][len(ch):].strip()}" if len(r['tugs_DS']) > len(ch) else ''))
L.append('\n## Ours-only (Dwarf Shaman view), grouped by our chapter\n')
cur = None
for r in rows:
    if not bucket(r).startswith('ours-only'): continue
    ch = r['ours_DS'].split(' [')[0]
    if ch != cur: L.append(f'\n### {ch}\n'); cur = ch
    L.append(fmt(r) + (f"  <- {r['ours_DS'][len(ch):].strip()}" if len(r['ours_DS']) > len(ch) else '') + (f"  [TUGs later: {r['tugs_later']}]" if r.get('tugs_later') else ''))
L.append('\n## Hunter-only differences (Dwarf Hunter view)\n')
for r in rows:
    t, o = r.get('tugs_DH'), r.get('ours_DH')
    if (bool(t) != bool(o)) and (r.get('tugs_DS') is None and r.get('ours_DS') is None or 'Hunter' in (t or '') or 'Hunter' in (o or '')):
        L.append(fmt(r) + f"  TUGs: {t or '-'} | ours: {o or '-'}")
L.append('\n## Quests with no XP / unknown to atlas+Questie (fetch with wh_quests.py)\n')
L.append(', '.join(str(q) for q in sorted(unknown_ids)) or 'none')
open(os.path.join(OUT, 'tugs_diff_summary.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
open(os.path.join(OUT, 'unknown_quests.txt'), 'w').write('\n'.join(str(q) for q in sorted(unknown_ids)) + '\n')
print('\n'.join(L))

# ---- per-chapter XP (Dwarf Shaman): XP credited to the chapter where the quest is turned in --------------------------
XP_TO_LEVEL = [0, 400, 900, 1400, 2100, 2800, 3600, 4500, 5400, 6500, 7600, 8700, 9800, 11000, 12300, 13600, 15000, 16400, 17800, 19300,
               20800, 22400, 24000, 25500, 27200, 28900, 30500, 32200, 33900, 35600, 37300]  # xp needed to leave level i (i=1..30)
def level_at(xp):
    lv, cum = 1, 0
    while lv < 60 and lv < len(XP_TO_LEVEL) and cum + XP_TO_LEVEL[lv] <= xp:
        cum += XP_TO_LEVEL[lv]; lv += 1
    return lv
def chapter_xp(chapters, src, race, cls):
    rows, cum = [], 0
    acc = set()
    for ch in chapters:
        n_acc = n_turn = xp = 0; new = 0
        for e in src[ch][2]:
            if not applies(e['r'], race, cls): continue
            if e['code'] == 'QA': acc.add(e['qid']); n_acc += 1
            elif e['code'] == 'QT':
                n_turn += 1; x = qinfo(e['qid'])['xp']; xp += int(x) if x not in ('', None) else 0
                if qinfo(e['qid'])['status'] == 'new': new += 1
        cum += xp
        rows.append((ch, n_acc, n_turn, new, xp, cum, level_at(cum)))
    return rows
L2 = ['\n## Quest XP per chapter (Dwarf Shaman; XP credited where the quest is turned in; level = reached on quest XP alone, no mob XP)\n',
      '| guide | chapter | pickups | turn-ins | new turn-ins | chapter XP | cumulative | level on quest XP alone |', '|---|---|---|---|---|---|---|---|']
for ch, a, t, n, x, c, lv in chapter_xp(TUGS_DWARF + TUGS_LATER[:9], tugs, 'Dwarf', 'Shaman'):
    L2.append(f'| TUGs | {ch} | {a} | {t} | {n} | {x} | {c} | {lv} |')
for ch, a, t, n, x, c, lv in chapter_xp(OUR_CH['Dwarf'], ours, 'Dwarf', 'Shaman'):
    L2.append(f'| ours | {ch} | {a} | {t} | {n} | {x} | {c} | {lv} |')
L2.append('\nXP to reach 20 = 159,100; to reach 30 = 440,100 (vanilla table).')
with open(os.path.join(OUT, 'tugs_diff_summary.md'), 'a', encoding='utf-8') as fh: fh.write('\n'.join(L2) + '\n')
print('\n'.join(L2))

