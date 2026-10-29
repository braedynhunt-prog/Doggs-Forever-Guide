#!/usr/bin/env python3
r"""Quest fact sheet from QuestieDB Forever (tooling\qdb) + Wowhead XP (data\zone_*.json).
  python3 tooling\qinfo.py 95250 377 ...          one block per quest id
  python3 tooling\qinfo.py zone:717 zone:16611    every Alliance-usable quest filed under that zoneOrSort
  python3 tooling\qinfo.py name:"Stockade"        quests whose name contains the text
Options: -s (short, one line per quest)."""
import json, sys, os, glob, statistics
BASE = os.environ.get('FOREVER_ATLAS', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
QDB = os.path.join(BASE, 'tooling', 'qdb')
Q = json.load(open(os.path.join(QDB, 'quest.json'), encoding='utf-8'))
N = json.load(open(os.path.join(QDB, 'npc.json'), encoding='utf-8'))
O = json.load(open(os.path.join(QDB, 'object.json'), encoding='utf-8'))
IT = json.load(open(os.path.join(QDB, 'item.json'), encoding='utf-8'))
ZN = {1: 'Dun Morogh', 38: 'Loch Modan', 1537: 'Ironforge', 40: 'Westfall', 12: 'Elwynn Forest', 1519: 'Stormwind City',
      44: 'Redridge Mountains', 10: 'Duskwood', 11: 'Wetlands', 148: 'Darkshore', 141: 'Teldrassil', 1657: 'Darnassus',
      1581: 'The Deadmines', 717: 'The Stockade', 16919: 'The Hall of Thanes', 16611: 'Ruins of Lordaeron', 16732: 'Excavation Site',
      85: 'Tirisfal Glades', 267: 'Hillsbrad Foothills', 130: 'Silverpine Forest', 331: 'Ashenvale', 36: 'Alterac Mountains',
      45: 'Arathi Highlands', 33: 'Stranglethorn Vale', 406: 'Stonetalon Mountains', 400: 'Thousand Needles', 3: 'Badlands',
      719: 'Blackfathom Deeps', 209: 'Shadowfang Keep', 721: 'Gnomeregan', 491: 'Razorfen Kraul', 17: 'The Barrens', 15: 'Dustwallow',
      16544: 'City of Dalaran', 16591: 'Ruins of Lordaeron(?)', 1497: 'Undercity', 1637: 'Orgrimmar', 1638: 'Thunder Bluff', 14: 'Durotar', 215: 'Mulgore'}
XP = {}; WH = {}
for f in glob.glob(os.path.join(BASE, 'data', 'zone_*.json')):
    for q in json.load(open(f, encoding='utf-8')).get('quests', []):
        if q.get('xp') not in (None, '') and q['id'] not in XP: XP[q['id']] = q['xp']
        WH.setdefault(q['id'], q)
def f(row, i):
    return row[i - 1] if row and len(row) >= i else None
def npc_loc(nid):
    n = N.get(str(nid))
    if not n: return f'npc {nid}?'
    sp = f(n, 7) or {}
    locs = []
    for z, pts in (sp.items() if isinstance(sp, dict) else []):
        pts = [p for p in pts if p and p[0] is not None and p[0] >= 0]
        if pts:
            xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
            locs.append(f"{ZN.get(int(z), z)} {statistics.mean(xs):.1f},{statistics.mean(ys):.1f}" + (f" (n={len(pts)}, x{min(xs):.0f}-{max(xs):.0f} y{min(ys):.0f}-{max(ys):.0f})" if len(pts) > 1 else ''))
    lv = f"L{f(n,4)}-{f(n,5)}" if f(n, 4) else ''
    rank = {1: ' ELITE', 2: ' RARE', 4: ' RARE-ELITE'}.get(f(n, 6) or 0, '')
    return f"[{nid}] {f(n,1)} {lv}{rank} @ " + ('; '.join(locs) if locs else 'instance/no spawn')
def obj_loc(oid):
    o = O.get(str(oid))
    if not o: return f'object {oid}?'
    sp = f(o, 4) or {}
    locs = []
    for z, pts in (sp.items() if isinstance(sp, dict) else []):
        pts = [p for p in pts if p and p[0] is not None and p[0] >= 0]
        if pts:
            xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
            locs.append(f"{ZN.get(int(z), z)} {statistics.mean(xs):.1f},{statistics.mean(ys):.1f}" + (f" (n={len(pts)})" if len(pts) > 1 else ''))
    return f"obj[{oid}] {f(o,1)} @ " + ('; '.join(locs) if locs else 'instance/no spawn')
def item_name(iid):
    it = IT.get(str(iid)); return f"item[{iid}] {f(it,1) if it else '?'}"
def races(mask):
    if not mask: return 'any'
    m = mask & 0xFFFF
    r = [n for b, n in ((1, 'Human'), (2, 'Orc'), (4, 'Dwarf'), (8, 'NightElf'), (16, 'Undead'), (32, 'Tauren'), (64, 'Gnome'), (128, 'Troll')) if m & b]
    return ','.join(r)
def classes(mask):
    if not mask: return ''
    return ','.join(n for b, n in ((1, 'Warrior'), (2, 'Paladin'), (4, 'Hunter'), (8, 'Rogue'), (16, 'Priest'), (64, 'Shaman'), (128, 'Mage'), (256, 'Warlock'), (1024, 'Druid')) if mask & b)
def alliance_ok(row):
    m = f(row, 6)
    return (not m) or (m & 77)
def show(qid, short=False):
    row = Q.get(str(qid))
    if not row: print(f"{qid}: not in Forever DB"); return
    name = f(row, 1); xp = XP.get(qid, '?'); wh = WH.get(qid, {})
    st = f(row, 2) or []; en = f(row, 3) or []
    g = lambda a, i: (a[i] or []) if isinstance(a, list) and len(a) > i else []
    starters = [npc_loc(n) for n in g(st, 0)] + [obj_loc(o) for o in g(st, 1)] + [item_name(i) for i in g(st, 2)]
    enders = [npc_loc(n) for n in g(en, 0)] + [obj_loc(o) for o in g(en, 1)]
    pre1 = f(row, 13) or []; preg = f(row, 12) or []; nxt = f(row, 22); excl = f(row, 16) or []
    head = f"{qid} {name} | req {f(row,4)} L{f(row,5)} | xp {xp} | {races(f(row,6))} {classes(f(row,7))} | sort {ZN.get(f(row,17), f(row,17))} | wh:{wh.get('envChange',{}).get('status','-')}"
    if short: print(head); return
    print(head)
    print(f"  start: {' | '.join(starters) or '?'}")
    print(f"  end:   {' | '.join(enders) or '?'}")
    if pre1 or preg or nxt or excl:
        print(f"  pre(any): {pre1}  pre(all): {preg}  next: {nxt}  exclusive: {excl}")
    obj = f(row, 10) or []
    obj = obj if isinstance(obj, list) else []
    if len(obj) > 0 and obj[0]:
        for o in obj[0]: print(f"  kill: {npc_loc(o[0])} x{o[2] if len(o)>2 else ''} {('- ' + o[1]) if len(o)>1 and o[1] else ''}")
    if len(obj) > 1 and obj[1]:
        for o in obj[1]: print(f"  use:  {obj_loc(o[0])} x{o[2] if len(o)>2 else ''}")
    if len(obj) > 2 and obj[2]:
        for o in obj[2]:
            it = IT.get(str(o[0])); drops = (f(it, 2) or []) if it else []; odrops = (f(it, 3) or []) if it else []
            src = '; '.join([npc_loc(d) for d in drops[:4]] + [obj_loc(d) for d in odrops[:3]])
            print(f"  item: {item_name(o[0])} x{o[2] if len(o)>2 else ''}  from: {src or '?'}")
    txt = f(row, 8)
    if txt: print(f"  text: {' '.join(txt) if isinstance(txt, list) else txt}")
    si = f(row, 11)
    if si: print(f"  source item: {item_name(si)}")
    rew = wh.get('itemchoices') or []; rr = wh.get('itemrewards') or []
    if rew or rr: print(f"  rewards: choice {[item_name(r[0]) for r in rew]} fixed {[item_name(r[0]) for r in rr]}")
args = sys.argv[1:]; short = '-s' in args; args = [a for a in args if a != '-s']
for a in args:
    if a.startswith('zone:'):
        z = int(a[5:])
        ids = sorted(int(k) for k, v in Q.items() if f(v, 17) == z and alliance_ok(v))
        print(f"== zoneOrSort {z} {ZN.get(z, '')}: {len(ids)} Alliance-usable quests")
        for q in ids: show(q, short=True)
    elif a.startswith('name:'):
        s = a[5:].lower()
        for k, v in Q.items():
            if s in (f(v, 1) or '').lower(): show(int(k), short=True)
    else:
        show(int(a), short=short); print()
