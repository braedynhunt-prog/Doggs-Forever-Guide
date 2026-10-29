"""Leatherworking 1-150 path + Totemic mats + skinning-yield estimate for WoW Forever.
Run: python3 -I lwcalc.py   (writes lw_calc.json next to this file; report is built by report.py)"""
import json, math, os, re, ast
from collections import defaultdict, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
LW = os.path.join(HERE, '..', 'lw')
ATLAS = "/mnt/user-data/uploads/WoW Forever Atlas"

R = json.load(open(os.path.join(LW, 'lw_recipes_forever.json'), encoding='utf-8'))
SP = json.load(open(os.path.join(LW, 'skill_page_items.json'), encoding='utf-8'))
SRC = json.load(open(os.path.join(LW, 'leather_sources_forever.json'), encoding='utf-8'))
QDB = json.load(open(os.path.join(ATLAS, 'tooling', 'qdb', 'item.json'), encoding='utf-8'))

spells = [s for s in R['spells'] if s.get('creates') and s.get('colors')]
by_id = {s['id']: s for s in spells}
by_name = {}
for s in spells:
    by_name.setdefault(s['name'], s)


def iname(i):
    v = QDB.get(str(i))
    return v[0] if v and v[0] else f'item {i}'


# ---------- skill-up model ----------
def chance(sp, skill):
    o, y, g, gr = sp['colors']
    s = math.floor(skill + 1e-9)
    if gr <= y:          # [0,N,N,N]: grey as soon as learned -> no skill-up
        return 0.0 if s >= gr else 1.0
    if s < y:
        return 1.0
    return max(0.0, (gr - s) / (gr - y))


def avail(sp):
    o = sp['colors'][0]
    if o > 0:
        return o
    if sp['status'] == 'new':
        return sp['learnedat']
    return 1                  # classic starter recipe (Light Armor Kit, Handstitched ...)


# ---------- weights (Light-Leather equivalents) used ONLY to choose filler ----------
W = {2318: 1.0, 783: 15.0, 2319: 2.5, 4232: 40.0, 4234: 12.5,
     4289: 0.1, 2320: 0.1, 2321: 0.2, 4340: 0.3, 2324: 0.3, 2605: 0.5, 4291: 0.5, 2325: 0.3}
VENDOR = {4289, 2320, 2321, 4340, 2324, 2605, 4291, 2325, 3371}
SKINNED = {2318, 783, 2319, 4232, 4234}
NEWREAG = {249427, 249410}
INTER = {4231: 3816, 4233: 3817, 4246: 3763, 4243: 3761, 2313: 2165, 4265: 3780}
EXCLUDE_FILLER = {2881, 20648, 20649}


def expand(sp, skill, w=None):
    """raw cost, expected points, list of sub-crafts (inline intermediates) for one craft"""
    w = w or W
    cost, pts, subs = 0.0, chance(sp, skill), []
    for it, n in sp['reagents']:
        if it in INTER:
            sub = by_id[INTER[it]]
            for _ in range(n):
                c2, p2, s2 = expand(sub, skill, w)
                cost += c2; pts += p2; subs += s2 + [sub['id']]
        elif it in w:
            cost += w[it] * n
        else:
            return None, None, None
    return cost, pts, subs


fillers = []
for s in spells:
    src = s.get('source') or []
    starter = (not src) and s['colors'][0] == 0 and s['status'] != 'new'
    if s['id'] in EXCLUDE_FILLER or not (6 in src or starter):
        continue
    if s['status'] == 'new' and 6 not in src:
        continue
    c, p, _ = expand(s, avail(s))
    if c is None:
        continue
    fillers.append(s)

TOTEMIC_ORDER = ['Belt', 'Gloves', 'Armor', 'Boots', 'Hood', 'Pants', 'Tunic', 'Leggings', 'Helm']
TOT = {p: by_name[f'Totemic Leather {p}'] for p in TOTEMIC_ORDER}
BRAWL_NAMES = {'Belt': "Brawler's Leather Belt", 'Gloves': "Brawler's Leather Gloves", 'Armor': "Brawler's Leather Armor",
               'Boots': "Brawler's Leather Boots", 'Hood': "Brawler's Leather Hood", 'Pants': "Brawler's Leather Pants",
               'Tunic': "Brawler's Leather Tunic", 'Leggings': "Brawler's Leather Legguards", 'Helm': "Brawler's Leather Helm"}


def simulate(target, pieces, w=None):
    w = w or W
    fstock = defaultdict(int)   # intermediates made as filler (e.g. Fine Leather Belt) - reused by later recipes
    need = defaultdict(int)
    for p in pieces:
        for it, n in TOT[p]['reagents']:
            if it in (4231, 4233):
                need[it] += n
    quota = {4231: need[4231], 4233: need[4233]}
    stock = defaultdict(int)
    s = 1.0
    done = set()
    actions = []
    actions_note = []

    def do(sp, forced, use_stock):
        nonlocal s
        start = s
        subs = []
        for it, n in sp['reagents']:
            if it in INTER:
                for _ in range(n):
                    if use_stock and stock[it] > 0:
                        stock[it] -= 1
                        continue
                    if fstock[it] > 0:
                        fstock[it] -= 1
                        actions_note.append(it)
                        continue
                    sub = by_id[INTER[it]]
                    # nested intermediates (e.g. none deeper than 1 level here)
                    s += chance(sub, s)
                    subs.append(sub['id'])
        g = chance(sp, s)
        s += g
        actions.append({'id': sp['id'], 'name': sp['name'], 'start': start, 'end': s, 'gain': s - start,
                        'subs': subs, 'forced': forced})
        if sp['creates'][0] in (4231, 4233) and forced == 'quota':
            stock[sp['creates'][0]] += 1
        elif forced == 'filler' and sp['creates'][0] in INTER:
            fstock[sp['creates'][0]] += 1

    guard = 0
    while True:
        guard += 1
        assert guard < 5000
        fl = math.floor(s + 1e-9)
        pend = [p for p in pieces if p not in done and avail(TOT[p]) <= fl]
        if pend:
            p = pend[0]
            do(TOT[p], 'totemic', True)
            done.add(p)
            continue
        if fl >= target and all(p in done for p in pieces):
            break
        if quota[4231] > 0 and fl >= 30:
            quota[4231] -= 1; do(by_id[3816], 'quota', False); continue
        if quota[4233] > 0 and fl >= 75:
            quota[4233] -= 1; do(by_id[3817], 'quota', False); continue
        if fl >= target:
            # waiting for a Totemic piece whose skill is above target: cannot happen with our targets
            break
        best = None
        for f in fillers:
            if avail(f) > fl:
                continue
            c, p_, _ = expand(f, s, w)
            if p_ <= 0:
                continue
            key = c / p_
            if best is None or key < best[0] - 1e-9:
                best = (key, f)
        do(best[1], 'filler', False)
    return actions, dict(stock), quota, {iname(k): v for k, v in fstock.items()}, len(actions_note)


def group(actions):
    segs = []
    for a in actions:
        if segs and segs[-1]['id'] == a['id'] and segs[-1]['forced'] == a['forced']:
            sg = segs[-1]
            sg['crafts'] += 1; sg['end'] = a['end']; sg['subs'] += a['subs']
        else:
            segs.append({'id': a['id'], 'name': a['name'], 'forced': a['forced'], 'start': a['start'],
                         'end': a['end'], 'crafts': 1, 'subs': list(a['subs'])})
    for sg in segs:
        sp = by_id[sg['id']]
        sg['colors'] = sp['colors']
        sg['source'] = sp.get('source')
        sg['reagents'] = [[it, n, iname(it)] for it, n in sp['reagents']]
        sg['sub_counts'] = {by_id[x]['name']: sg['subs'].count(x) for x in set(sg['subs'])}
        sg['total_reagents'] = {iname(it): n * sg['crafts'] for it, n in sp['reagents']}
        del sg['subs']
    return segs


def raw_totals(actions):
    tot = defaultdict(int)
    produced = defaultdict(int)
    consumed = defaultdict(int)
    for a in actions:
        sp = by_id[a['id']]
        for it, n in sp['reagents']:
            if it in INTER:
                consumed[it] += n
            else:
                tot[it] += n
        produced[sp['creates'][0]] += 1
        for sid in a['subs']:
            sub = by_id[sid]
            for it, n in sub['reagents']:
                tot[it] += n
            # sub-crafts are consumed straight away by their parent (already counted in consumed)
            produced[sub['creates'][0]] += 1
    inter_balance = {iname(i): produced[i] - consumed[i] for i in INTER if produced[i] or consumed[i]}
    return dict(tot), inter_balance


def cat_totals(tot):
    out = OrderedDict()
    for label, ids in (('skinned', SKINNED), ('vendor', VENDOR), ('new_forever', NEWREAG)):
        out[label] = OrderedDict((f'{iname(i)} ({i})', tot[i]) for i in sorted(tot, key=lambda i: -tot[i]) if i in ids)
    other = {f'{iname(i)} ({i})': tot[i] for i in tot if i not in SKINNED | VENDOR | NEWREAG}
    if other:
        out['other'] = other
    return out


PIECES_125 = ['Belt', 'Gloves', 'Armor', 'Boots', 'Hood', 'Pants', 'Tunic', 'Leggings']
PIECES_150 = PIECES_125 + ['Helm']
res = {}
W_HEAVY = dict(W); W_HEAVY[4234] = 3.0   # once skinning level-30+ mobs, Heavy Leather is a main drop
for label, target, pieces, w in (('to125', 125, PIECES_125, W), ('to150', 150, PIECES_150, W_HEAVY),
                                 ('to150_mlonly', 150, PIECES_150, W)):
    acts, stock, quota, fst, reused = simulate(target, pieces, w)
    tot, bal = raw_totals(acts)
    res[label] = {'target': target, 'pieces': pieces, 'final_skill': acts[-1]['end'], 'n_crafts': len(acts),
                  'n_subcrafts': sum(len(a['subs']) for a in acts), 'segments': group(acts),
                  'raw_totals': {str(k): v for k, v in tot.items()}, 'by_category': cat_totals(tot),
                  'intermediate_balance': bal, 'leftover_stock': {iname(k): v for k, v in stock.items()},
                  'leftover_filler_products': fst, 'filler_products_reused': reused}

# Totemic-only mats (pieces themselves, with CLH/CMH expanded to hide+salt)
def piece_raw(pieces):
    t = defaultdict(int)
    for p in pieces:
        for it, n in TOT[p]['reagents']:
            if it == 4231:
                t[783] += n; t[4289] += n
            elif it == 4233:
                t[4232] += n; t[4289] += n
            else:
                t[it] += n
    return dict(t)

res['totemic_pieces_raw_125'] = {f'{iname(k)} ({k})': v for k, v in piece_raw(PIECES_125).items()}
res['totemic_pieces_raw_150'] = {f'{iname(k)} ({k})': v for k, v in piece_raw(PIECES_150).items()}
res['totemic_pieces_raw_craftable6'] = {f'{iname(k)} ({k})': v for k, v in piece_raw(['Belt', 'Gloves', 'Boots', 'Hood', 'Tunic', 'Leggings']).items()}

# ---------- B: set tables ----------
rec_items = {r['name']: r for r in SP['recipeItems']}
crafted = {c['spell']: c for c in SP['crafted']}


def piece_row(sp):
    c = crafted.get(sp['id'], {})
    pat = rec_items.get('Pattern: ' + sp['name'])
    q = QDB.get(str(pat['id'])) if pat else None
    return {'name': sp['name'], 'spell': sp['id'], 'item': sp['creates'][0], 'reqlevel': c.get('reqlevel'),
            'ilvl': c.get('ilvl'), 'armor': c.get('armor'), 'learnedat': sp['learnedat'], 'colors': sp['colors'],
            'spell_source': sp.get('source'),
            'reagents': [[it, n, iname(it)] for it, n in sp['reagents']],
            'pattern': ({'id': pat['id'], 'skill': pat['skill'], 'source': pat.get('source'), 'level': pat.get('level'),
                         'qdb_vendors': (q[13] if q else None), 'qdb_npcDrops': (q[1] if q else None)} if pat else None),
            'item_qdb_npcDrops': (QDB.get(str(sp['creates'][0])) or [None, None])[1]}

res['totemic_table'] = [piece_row(TOT[p]) for p in TOTEMIC_ORDER]
res['brawler_table'] = [piece_row(by_name[BRAWL_NAMES[p]]) for p in TOTEMIC_ORDER]
res['totemic_other_slots'] = [s['name'] for s in spells if s['name'].startswith('Totemic') and not any(s['name'].endswith(p) for p in TOTEMIC_ORDER)]

# ---------- D/E ----------
acid = {p: dict((it, n) for it, n in TOT[p]['reagents']).get(249410, 0) for p in TOTEMIC_ORDER}
prist = {p: dict((it, n) for it, n in TOT[p]['reagents']).get(249427, 0) for p in TOTEMIC_ORDER}
res['acid_per_piece'] = acid
res['pristine_per_piece'] = prist
acid_sp = SRC['249410']['created-by-spell'][0]
res['acid_recipe'] = {'spell': acid_sp['id'], 'skill': acid_sp['skill'], 'learnedat': acid_sp['learnedat'],
                      'colors': acid_sp['colors'], 'reagents': [[i, n, iname(i)] for i, n in acid_sp['reagents']],
                      'pyrite_objectDrops': QDB['249391'][2], 'vial_vendor_count': len(QDB['3371'][13] or [])}
P = SRC['249427']
res['pristine'] = {
    'skinned_from': [{k: r.get(k) for k in ('id', 'name', 'min', 'max', 'count', 'outof', 'fcount', 'foutof', 'pctstack')} for r in P['skinned-from']],
    'dropped_by_n': len(P['dropped-by']),
    'dropped_by_sum_count': sum(r['count'] for r in P['dropped-by']),
    'dropped_by_sum_outof': sum(r['outof'] for r in P['dropped-by']),
    'dropped_by_sum_fcount': sum(r['fcount'] for r in P['dropped-by']),
    'dropped_by_top': [{k: r.get(k) for k in ('id', 'name', 'min', 'max', 'count', 'outof', 'pctstack')} for r in sorted(P['dropped-by'], key=lambda r: -r['count'])[:10]],
    'comments': [{'date': c['date'][:10], 'rating': c['rating'], 'body': c['body']} for c in P['comments']],
    'qdb_npcDrops_count': len(QDB['249427'][1] or []),
}


# ---------- F: skinning yields by mob-level band ----------
def avgstack(ps):
    if not ps:
        return 1.0
    d = ast.literal_eval(ps)
    tot = sum(d.values())
    return sum(k * v for k, v in d.items()) / tot


def band(lvl):
    return '<=10' if lvl <= 10 else '11-15' if lvl <= 15 else '16-20' if lvl <= 20 else '21-25' if lvl <= 25 else '26-30' if lvl <= 31 else '31+'


bands = ['<=10', '11-15', '16-20', '21-25', '26-30', '31+']
rates = {b: {} for b in bands}
for item in ('2318', '783', '2319', '4232'):
    acc = defaultdict(lambda: [0, 0, 0.0])
    for r in SRC[item]['skinned-from']:
        if 'min' not in r:
            continue
        # skip named/rare rows with tiny samples
        if r['outof'] < 1000:
            continue
        b = band(r['min'])
        a = acc[b]
        a[0] += r['count']; a[1] += r['outof']; a[2] += r['count'] * avgstack(r['pctstack'])
    for b in bands:
        if acc[b][1]:
            rates[b][item] = {'p': acc[b][0] / acc[b][1], 'avgstack': acc[b][2] / acc[b][0],
                              'per_skin': acc[b][2] / acc[b][1], 'n_skins_sample': acc[b][1]}
# Assumption for <=10 (not in the data): Light Leather ~0.35/skin + Ruined Leather Scraps (~1.5/skin, 3 -> 1 LL) = ~0.85 LL-equivalent
rates['<=10'] = {'2318': {'p': None, 'avgstack': None, 'per_skin': 0.85, 'n_skins_sample': 0, 'assumed': True},
                 '783': {'p': 0, 'avgstack': 1, 'per_skin': 0.0, 'n_skins_sample': 0, 'assumed': True}}
# 21-25 Light Leather: only 2 rows (Vicious Gray Bear 22, Starving Mountain Lion 23); Light Hide stops ~20
res['skin_rates'] = rates

# beast kill steps (from beast_lines.json, counts read by hand; collect steps = items / assumed drop rate)
# (chapter, target, explicit_kills_estimate, mob_level, basis)
STEPS = [
    ('01a', 'Ragged Young Wolf', 13, 2, '8 Tough Wolf Meat / ~0.6'),
    ('01a', 'Small Crag Boar', 12, 4, 'Kill 12'),
    ('01a', 'Snow Leopard Prowler', 1, 6, 'named'),
    ('01b', 'Crag Boar', 12, 6, '6 Crag Boar Rib + 4 Chunk of Boar Meat / ~0.8'),
    ('01b', 'Young Black Bear', 3, 6, '2 Thick Bear Fur / ~0.7'),
    ('01b', 'Ice Claw Bear', 6, 8, 'Kill 6'),
    ('01b', 'Elder Crag Boar', 8, 8, 'Kill 8'),
    ('01b', 'Snow Leopard', 8, 8, 'Kill 8'),
    ('01b', 'Young Wendigo / Wendigo', 12, 8, '8 Wendigo Manes / ~0.65'),
    ('01b', 'Frosthowl', 1, 9, 'named yeti'),
    ('01b', 'Vagash', 1, 11, 'named'),
    ('01b', 'Snow Leopard (Pristine Leopard Pelts)', 15, 8, '6 pelts, "low drop rate" ~0.4'),
    ('01b', 'Mangeclaw', 1, 11, 'named'),
    ('02', 'Mountain Buzzard', 6, 13, 'Kill 6'),
    ('02', 'Loch Crocolisk', 10, 14, '5 meat + 6 skins, ~0.6 each from same kills'),
    ('02', 'Daggerfang', 1, 15, 'named'),
    ('04', 'Elder Mountain Boar', 5, 16, 'Kill 5'),
    ('05', 'Young Fleshripper', 5, 12, '3 Stringy Vulture Meat / ~0.6'),
    ('05', 'Young Goretusk', 14, 12, '8 Goretusk Livers / ~0.6 (snouts from same kills)'),
    ('06', 'Great Goretusk', 8, 16, '5 snouts / ~0.6'),
    ('06', 'Dire Condor', 8, 18, '5 Tough Condor Meat / ~0.6'),
    ('09', 'Young Wetlands Crocolisk', 7, 21, '4 Young Crocolisk Skins / ~0.6'),
    ('11', 'Den Mother', 1, 18, 'named'),
    ('16', 'Bellygrub', 1, 24, 'named'),
    ('17', 'Nightbane Vile Fang / Tainted One', 10, 29, 'kill quest 222 (count not in guide text; ~10)'),
    ('18', 'Giant Wetlands Crocolisk', 15, 25, 'guide: "budget ~15 kills"'),
    ('18', 'Mottled Raptor + Mottled Screecher', 20, 23, 'Ormer 294: 10 + 10 (Classic counts)'),
    ('18', 'Mottled Scytheclaw + Mottled Razormaw', 20, 26, 'Ormer 295: 10 + 10 (Classic counts)'),
    ('18', 'Sarltooth', 1, 28, 'named'),
    ('19', 'Crimson/Red/Lost/Flamesnorting Whelps', 16, 25, '8 Pristine Crimson Scales / ~0.5'),
    ('19', 'Highland Razormaw', 15, 27, '10 Razormaw Incisors / ~0.65'),
    ('19', 'Carnage', 1, 28, 'named elite'),
    ('22', 'Mottled Scytheclaw / Razormaw', 6, 26, 'on the way down'),
    ('23', 'Snapjaw', 15, 30, '10 Turtle Meat / ~0.65'),
    ('23', 'Cave Yeti', 15, 30, '10 Yeti Fur / ~0.65'),
]
# dungeon / incidental beasts not written as kill steps
DUNGEON_EXTRA = [('13', 'BFD Aku\'mai Snapjaws / Fishers (trash)', 8, 24), ('26', 'RFK Kraul Bats / Raging Agam\'ar / boars (trash)', 15, 30)]
INCIDENTAL = 0.5     # +50% beasts killed in passing (adds, travel, packs) on top of the written steps

CHAPTERS = ['01a', '01b'] + [f'{i:02d}' for i in range(2, 27)]


def yields(upto, incidental=INCIDENTAL):
    idx = CHAPTERS.index(upto)
    sel = set(CHAPTERS[:idx + 1])
    tot = defaultdict(float)
    kills = 0
    for ch, t, k, lvl, _ in STEPS + [(a, b, c, d, '') for a, b, c, d in DUNGEON_EXTRA]:
        if ch not in sel:
            continue
        k2 = k * (1 + incidental)
        kills += k2
        for item, rr in rates[band(lvl)].items():
            tot[item] += k2 * rr['per_skin']
    return kills, {iname(int(k)): round(v, 1) for k, v in tot.items()}, dict(tot)


res['route_steps'] = STEPS
res['route_dungeon_extra'] = DUNGEON_EXTRA
res['route_yields'] = {}
for ch in ('07', '14', '26'):
    for inc in (0.0, 0.5, 1.0):
        k, named, raw = yields(ch, inc)
        res['route_yields'][f'ch{ch}_inc{int(inc*100)}'] = {'beast_kills': round(k), 'yield': named,
                                                            'raw': {k2: round(v, 1) for k2, v in raw.items()}}
per_ch = []
for ch in CHAPTERS:
    sel = [s for s in STEPS if s[0] == ch] + [(a, b, c, d, '') for a, b, c, d in DUNGEON_EXTRA if a == ch]
    per_ch.append((ch, sum(s[2] for s in sel)))
res['route_kills_per_chapter_explicit'] = per_ch

json.dump(res, open(os.path.join(HERE, 'lw_calc.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)

# quick console summary
for label in ('to125', 'to150', 'to150_mlonly'):
    r = res[label]
    print('=====', label, 'final', round(r['final_skill'], 2), 'crafts', r['n_crafts'], 'subcrafts', r['n_subcrafts'])
    for sg in r['segments']:
        print(f"  {math.floor(sg['start']):>3}-{math.floor(sg['end']):>3} {sg['crafts']:>3}x {sg['name']:<32} {sg['forced']:<8} {sg['colors']} subs={sg['sub_counts']}")
    print('  totals', json.dumps(r['by_category']))
    print('  balance', r['intermediate_balance'], 'stock', r['leftover_stock'], r['leftover_filler_products'], r['filler_products_reused'])
print(json.dumps(res['skin_rates'], indent=0)[:3000])
for k, v in res['route_yields'].items():
    print(k, v['beast_kills'], v['yield'])
print(res['acid_per_piece'], sum(res['acid_per_piece'].values()))
print(res['pristine_per_piece'], sum(res['pristine_per_piece'].values()))
print(res['totemic_other_slots'])
