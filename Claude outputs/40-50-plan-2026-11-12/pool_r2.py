"""Round-2 (42-50) candidate pool: every Alliance-usable quest of quest level LO..HI that chapters 00-41 do not tag,
with the facts the rules need, one file per Wowhead category (zone) plus the lists of what still has to be pulled.

Usage: python pool_r2.py <repo root> <out dir> [LO HI]
Sources: data/zone_*.json (Wowhead Forever), tooling/qdb (QuestieDB), data/drop_rates.json, data/wowhead_quest_links.json,
weights/tooltips/*.json (newest wins), the chapter files (ids already used).
Row layout used (0-indexed): quest [1] startedBy [2] finishedBy [3] reqLevel [4] level [5] races [6] classes [9] objectives
[11] preQuestGroup [12] preQuestSingle [15] exclusiveTo [16] zoneOrSort [17] requiredSkill [18] requiredMinRep [21] next;
npc [0] name [3] min [4] max level [5] rank [6] spawns; object [0] name [3] spawns; item [0] name [1] npc drops [2] object drops [13] vendors.
"""
import sys, os, re, json, glob, collections
ROOT, OUT = sys.argv[1], sys.argv[2]
LO, HI = (int(sys.argv[3]), int(sys.argv[4])) if len(sys.argv) > 4 else (39, 52)
os.makedirs(OUT, exist_ok=True)
ld = lambda p: json.load(open(os.path.join(ROOT, p), encoding='utf-8'))
Q, N, O, I = ld('tooling/qdb/quest.json'), ld('tooling/qdb/npc.json'), ld('tooling/qdb/object.json'), ld('tooling/qdb/item.json')
DR = ld('data/drop_rates.json')['items']
WL = ld('data/wowhead_quest_links.json')['quests']
TT = {}
for fn in sorted(glob.glob(os.path.join(ROOT, 'weights', 'tooltips', '*.json'))):
    for name, rec in json.load(open(fn, encoding='utf-8')).items():
        if isinstance(rec, dict) and rec.get('id'): TT[int(rec['id'])] = (name, rec.get('tooltip', ''))
used = {}
for fn in sorted(glob.glob(os.path.join(ROOT, 'guide', 'Guidelime_ForeverShaman', '*.lua'))):
    b = os.path.basename(fn).split('_')[0]
    for m in re.finditer(r'\[Q[AT](\d+)', open(fn, encoding='utf-8').read()): used.setdefault(int(m.group(1)), b)
W, slug = {}, {}
for fn in sorted(glob.glob(os.path.join(ROOT, 'data', 'zone_*.json'))):
    z = json.load(open(fn, encoding='utf-8')); slug[z['id']] = z.get('slug') or str(z['id'])
    for q in z['quests']:
        if z.get('_browser_refresh') and q.get('_browser') != z['_browser_refresh']: continue   # a row Wowhead no longer lists on this zone page
        o = W.get(q['id'])
        if o is None or (q.get('_browser') or '') > (o.get('_browser') or ''): W[q['id']] = q
g = lambda r, c: r[c] if r and c < len(r) else None
ZN = {int(k): v for k, v in {3: 'Badlands', 4: 'Blasted Lands', 8: 'Swamp of Sorrows', 15: 'Dustwallow', 16: 'Azshara', 17: 'Barrens', 33: 'Stranglethorn', 36: 'Alterac',
      38: 'Loch Modan', 40: 'Westfall', 45: 'Arathi', 46: 'Burning Steppes', 47: 'Hinterlands', 51: 'Searing Gorge', 331: 'Ashenvale', 357: 'Feralas', 361: 'Felwood',
      400: 'Thousand Needles', 405: 'Desolace', 440: 'Tanaris', 490: "Un'Goro", 1337: 'Uldaman', 1176: "Zul'Farrak", 1477: 'Sunken Temple', 2100: 'Maraudon',
      1519: 'Stormwind', 1537: 'Ironforge', 1657: 'Darnassus', 16591: 'Riverglades', 16842: "Krol'dok", 16620: 'Alcaz', 16651: "Shen'dralas", 721: 'Gnomeregan',
      618: 'Winterspring', 28: 'W Plaguelands', 139: 'E Plaguelands', 1: 'Dun Morogh', 10: 'Duskwood', 11: 'Wetlands', 12: 'Elwynn', 44: 'Redridge', 85: 'Tirisfal',
      267: 'Hillsbrad', 148: 'Darkshore', 141: 'Teldrassil', 493: 'Moonglade', 1584: 'BRD', 722: 'RFD', 796: 'SM', 16560: 'Dalaran', 16554: 'Blackmaw Hold'}.items()}
def zname(z):
    try: z = int(z)
    except Exception: return str(z)
    return ZN.get(z) or slug.get(z) or str(z)
def where(sp):
    if not sp: return 'no spawn'
    z = max(sp, key=lambda k: len(sp[k])); pts = sp[z]
    return f"{zname(z)} {sum(p[0] for p in pts) / len(pts):.1f},{sum(p[1] for p in pts) / len(pts):.1f}" + (f" ({len(pts)})" if len(pts) > 1 else '')
RK = {None: '', 0: '', 1: ' ELITE', 2: ' RARE-ELITE', 3: ' BOSS', 4: ' RARE'}
def npc(i):
    r = N.get(str(i))
    if not r: return f'npc{i}?'
    lv = f"{g(r, 3)}-{g(r, 4)}" if g(r, 3) != g(r, 4) else f"{g(r, 3)}"
    return f"{r[0]} [{i}] L{lv}{RK.get(g(r, 5), ' rank' + str(g(r, 5)))} @ {where(g(r, 6))}"
def obj(i):
    r = O.get(str(i))
    return f"obj {r[0]} [{i}] @ {where(g(r, 3))}" if r else f'obj{i}?'
def ends(col):
    out = []
    if isinstance(col, list):
        out += [npc(x) for x in (g(col, 0) or [])] + [obj(x) for x in (g(col, 1) or [])]
        out += [f"item {g(I.get(str(x)), 0)} [{x}]" for x in (g(col, 2) or [])]
    return out
def wl(qid, key):
    e = WL.get(str(qid))
    if not e: return []
    out = []
    for t in e.get(key) or []:
        out.append((npc(t[1:]) if t[0] == 'n' else obj(t[1:]) if t[0] == 'o' else 'item ' + t[1:]) + ' (Wowhead)')
    return out
def rate(iid):
    e = DR.get(str(iid))
    if e and e.get('overall_pct') is not None: return e['overall_pct']
    t = TT.get(int(iid))
    if t:
        m = re.search(r'Drop Chance:?\s*([\d.]+)%', t[1])
        if m: return float(m.group(1))
    return None
unlocks = collections.defaultdict(list)
for k, r in Q.items():
    for c in (11, 12):
        for p in (g(r, c) or []):
            for pp in (p if isinstance(p, list) else [p]): unlocks[abs(int(pp))].append(int(k))
WT = {1: 'GROUP', 41: 'PVP', 62: 'RAID', 81: 'DUNGEON', 82: 'EVENT', 83: 'LEGENDARY', 84: 'ESCORT', 85: 'HEROIC'}
need_multi, need_single, need_rew, need_links, need_npc = {}, {}, set(), {}, {}
all_multi = {}
SKIPCAT = {16651, 721, -121, -264, -201, -304, -324, -364, -365, -1001, -221, -82, -641, 3358, 3277, 16606, 25, 348, 702}   # Shen'dralas (ruled out 11 Nov), Gnomeregan raid rows, other professions, events, battlegrounds
byzone = collections.defaultdict(list)
queue = [qid for qid, w in W.items() if LO <= (w.get('level') or 0) <= HI and (w.get('reqlevel') or 0) <= 50]
seenq, prechain, POOL = set(queue), set(), {}
while queue:
    qid = queue.pop(0); w = W[qid]
    lv, rq = w.get('level') or 0, w.get('reqlevel') or 0
    if w.get('side') == 2 or qid in used: continue
    r = Q.get(str(qid))
    nm = w.get('name') or ''
    if '<' in nm or 'REUSE' in nm or 'DEPRECATED' in nm.upper(): continue      # placeholder rows Wowhead still lists
    if r is None and 77000 <= qid < 86000: continue                            # Season of Discovery ids, not in the Forever DB
    if w.get('category') in SKIPCAT and qid not in prechain: continue
    cls = w.get('reqclass') or 0
    if cls and not (cls & 64): continue
    races = g(r, 5)
    if races and not (races & 4): continue          # Dwarf bit
    flags = []
    if qid in prechain: flags.append('PRECHAIN')
    if cls: flags.append('SHAMAN')
    if w.get('side') not in (1, 3): flags.append('SIDE?')
    if not w.get('xp'): flags.append('NOXP')
    wt = w.get('type')
    if wt: flags.append(WT.get(wt, f'TYPE{wt}'))
    dungeon = wt in (81, 62)
    st = ends(g(r, 1)) or wl(qid, 'start'); en = ends(g(r, 2)) or wl(qid, 'end')
    if r is None: flags.append('NOTINQDB')
    if not st: flags.append('NOSTART')
    if not en: flags.append('NOEND')
    if (r is None or not st or not en or 'SIDE?' in flags) and str(qid) not in WL: need_links[qid] = w.get('name')
    objs = g(r, 9) or []
    kills, items, oo, maxlv, elite = [], [], [], 0, False
    item_rows, kill_rows = [], []
    for c in (g(objs, 0) or []) + ((g(objs, 4) or [None])[0] or [] if isinstance(g(objs, 4), list) and g(objs, 4) and isinstance(g(objs, 4)[0], list) else []):
        cid = c[0] if isinstance(c, list) else c
        if not isinstance(cid, int): continue
        nr = N.get(str(cid)); kills.append(npc(cid))
        kill_rows.append({'id': cid, 'name': g(nr, 0), 'min': g(nr, 3), 'max': g(nr, 4), 'rank': g(nr, 5), 'spawns': sum(len(v) for v in (g(nr, 6) or {}).values())})
        if nr:
            maxlv = max(maxlv, g(nr, 4) or 0)
            if g(nr, 5) in (1, 2, 3): elite = True
            if cid > 200000 and g(nr, 5) is None: need_npc[cid] = nr[0]
            if g(nr, 3) is None: need_npc[cid] = nr[0]
    for o in (g(objs, 1) or []):
        oid = o[0] if isinstance(o, list) else o
        if isinstance(oid, int): oo.append(obj(oid))
    drop = False
    for it in (g(objs, 2) or []):
        iid = it[0] if isinstance(it, list) else it
        if not isinstance(iid, int): continue
        ir = I.get(str(iid)); nd = (g(ir, 1) or []); od = (g(ir, 2) or []); vd = (g(ir, 13) or [])
        rt = rate(iid)
        src = []
        if nd:
            lvls = [g(N.get(str(d)), 4) or 0 for d in nd]; maxlv = max([maxlv] + lvls)
            el = [d for d in nd if g(N.get(str(d)), 5) in (1, 2, 3)]
            if el and len(el) == len(nd): elite = True
            src.append(f"{len(nd)} mobs ({', '.join((g(N.get(str(d)), 0) or '?') for d in nd[:3])}{'...' if len(nd) > 3 else ''}){' all-elite' if el and len(el) == len(nd) else ''}")
            for d in nd:
                nr = N.get(str(d))
                if nr and d > 200000 and g(nr, 5) is None and len(nd) <= 3: need_npc[d] = nr[0]
        if od: src.append(f"{len(od)} objects ({(g(O.get(str(od[0])), 0) or '?')})")
        if vd: src.append('vendor')
        if nd and not od and not vd:
            drop = True
            if len(nd) > 1: all_multi[iid] = g(ir, 0)
            if rt is None: (need_multi if len(nd) > 1 else need_single)[iid] = g(ir, 0)
        item_rows.append({'id': iid, 'name': g(ir, 0), 'count': (it[2] if isinstance(it, list) and len(it) > 2 else None), 'mobs': nd, 'objects': od, 'vendors': bool(vd), 'rate': rt,
                          'mob_ranks': [g(N.get(str(d)), 5) for d in nd], 'mob_max': max([g(N.get(str(d)), 4) or 0 for d in nd] or [0])})
        items.append(f"{g(ir, 0) or iid} [{iid}] <- {'; '.join(src) or 'no source in qdb'}" + (f" RATE {rt}%" if rt is not None else (' RATE ?' if nd and not od and not vd else '')))
    if drop: flags.append('DROP')
    if elite and not dungeon: flags.append('ELITE')
    if g(r, 17): flags.append(f"SKILL{g(r, 17)}")
    if g(r, 18): flags.append(f"REP{g(r, 18)}")
    pre = [p for c in (11, 12) for p in (g(r, c) or [])]
    flat = [abs(int(x)) for p in pre for x in (p if isinstance(p, list) else [p])]
    prs = []
    for p in flat:
        pw = W.get(p, {})
        state = f"done {used[p]}" if p in used else ('HORDE' if pw.get('side') == 2 else f"L{pw.get('level')} req{pw.get('reqlevel')}" if pw else 'no Wowhead row')
        prs.append(f"{p} {g(Q.get(str(p)), 0)} ({state})")
    for p in flat:
        if p not in used and p in W and p not in seenq: seenq.add(p); prechain.add(p); queue.append(p)
    rew = [x[0] for x in (w.get('itemchoices') or []) + (w.get('itemrewards') or [])]
    for x in rew:
        if x not in TT: need_rew.add(x)
    line = f"{qid} {w.get('name')} | L{lv} req{rq} | xp {w.get('xp')} money {w.get('money') or 0} | {' '.join(flags) or '-'}"
    det = [f"   from: {' / '.join(st) or '?'}", f"   to:   {' / '.join(en) or '?'}"]
    if prs: det.append('   pre:  ' + ' ; '.join(prs))
    if g(r, 15): det.append(f"   exclusive to: {g(r, 15)}")
    nx = [u for u in unlocks.get(qid, []) if u in W and W[u].get('side') != 2]
    if nx: det.append('   unlocks: ' + ', '.join(f"{u} {W[u].get('name')} (L{W[u].get('level')} xp {W[u].get('xp')})" for u in nx[:6]))
    if kills: det.append('   kill: ' + ' ; '.join(kills[:6]))
    if oo: det.append('   objects: ' + ' ; '.join(oo[:4]))
    if items: det.append('   items: ' + ' ; '.join(items[:6]))
    txt = g(r, 7)
    if txt and not kills and not items and not oo: det.append('   text: ' + ' '.join(txt if isinstance(txt, list) else [str(txt)])[:230])
    if rew: det.append('   rewards: ' + ', '.join(f"{TT[x][0]} [{x}]" if x in TT else f"[{x}] no tooltip" for x in rew))
    cat = w.get('category')
    POOL[qid] = {'id': qid, 'name': w.get('name'), 'cat': cat, 'lv': lv, 'rq': rq, 'xp': w.get('xp') or 0, 'money': w.get('money') or 0, 'flags': flags,
                 'pre': flat, 'pre_all': [abs(int(x)) for p in (g(r, 11) or []) for x in (p if isinstance(p, list) else [p])], 'pre_one': [abs(int(x)) for p in (g(r, 12) or []) for x in (p if isinstance(p, list) else [p])], 'skill': g(r, 17), 'rep': g(r, 18), 'excl': g(r, 15), 'next': g(r, 21), 'unlocks': nx, 'maxlv': maxlv, 'rew': rew, 'choices': [x[0] for x in (w.get('itemchoices') or [])],
                 'items': item_rows, 'kills': kill_rows, 'start': st, 'end': en, 'side': w.get('side'), 'wtype': wt}
    byzone[cat].append({'id': qid, 'lv': lv, 'rq': rq, 'xp': w.get('xp') or 0, 'flags': flags, 'maxlv': maxlv, 'text': line + (f" | mobs to {maxlv}" if maxlv else '') + '\n' + '\n'.join(det)})
HARD = ('GROUP', 'ELITE', 'DROP', 'DUNGEON', 'RAID', 'PVP', 'NOXP', 'SHAMAN', 'EVENT', 'LEGENDARY', 'HEROIC')
print(f"pool L{LO}-{HI}: {sum(len(v) for v in byzone.values())} quests, {sum(q['xp'] for v in byzone.values() for q in v):,} XP")
print(f"{'cat':>6} {'zone':18} {'n':>3} {'xp':>8} | {'clean n':>7} {'clean xp':>8} | drop  elite/grp  dungeon  nostart  side?")
rows = []
for cat, qs in byzone.items():
    qs.sort(key=lambda q: (q['rq'], q['lv'], q['id']))
    clean = [q for q in qs if not any(f in HARD or f.startswith('SKILL') or f.startswith('REP') for f in q['flags'])]
    c = lambda *fs: sum(1 for q in qs if any(f in q['flags'] for f in fs))
    rows.append((sum(q['xp'] for q in qs), f"{str(cat):>6} {zname(cat)[:18]:18} {len(qs):3d} {sum(q['xp'] for q in qs):8,} | {len(clean):7d} {sum(q['xp'] for q in clean):8,} | {c('DROP'):4d} {c('ELITE', 'GROUP'):9d} {c('DUNGEON', 'RAID'):8d} {c('NOSTART', 'NOEND', 'NOTINQDB'):8d} {c('SIDE?'):6d}"))
    open(os.path.join(OUT, f"{cat}_{re.sub(r'[^A-Za-z]', '', zname(cat))}.txt"), 'w', encoding='utf-8', newline='\n').write(
        f"# {zname(cat)} (category {cat}): {len(qs)} quests, {sum(q['xp'] for q in qs):,} XP; clean (no drop / elite / group / dungeon / skill flag) {len(clean)} quests {sum(q['xp'] for q in clean):,} XP\n\n" + '\n\n'.join(q['text'] for q in qs) + '\n')
for _, t in sorted(rows, reverse=True): print(t)
json.dump(POOL, open(os.path.join(OUT, '_pool.json'), 'w', encoding='utf-8'), ensure_ascii=False)
w = lambda name, d: open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='\n').write(''.join(f"{k}\t{v}\n" for k, v in sorted(d.items())))
w('_need_item_pages.tsv', need_multi); w('_all_multi_items.tsv', all_multi); w('_need_item_tooltips.tsv', need_single); w('_need_quest_pages.tsv', need_links); w('_need_npc_pages.tsv', need_npc)
open(os.path.join(OUT, '_need_reward_tooltips.txt'), 'w', newline='\n').write('\n'.join(str(x) for x in sorted(need_rew)) + '\n')
print(f"\nneeds: item pages (multi-dropper, no rate) {len(need_multi)}; item tooltips (single dropper, no rate) {len(need_single)}; reward tooltips {len(need_rew)}; quest pages {len(need_links)}; NPC pages (rank or level blank) {len(need_npc)}")
