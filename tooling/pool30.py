#!/usr/bin/env python3
r"""Compact 20-30 candidate pool per zoneOrSort: Alliance class-free quests (req<=30), minus the ones our 00-07 chapters turn in.
python3 tooling\pool30.py 1519 38 11 ... > compare\pool_20-30.txt"""
import json, sys, os, re, glob, statistics
sys.argv += ['-s']
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'qinfo.py')).read().split("args = sys.argv[1:]")[0])
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import guidelib as gl
GUIDE = gl.ADDON   # 1 Nov 2026: FOREVER_GUIDE can point at another addon folder
done = set()
for fn in glob.glob(os.path.join(GUIDE, '0*.lua')):
    if os.path.basename(fn).startswith('08'): continue
    for m in re.finditer(r'\[QT(\d+)', open(fn, encoding='utf-8').read()): done.add(int(m.group(1)))
def loc1(s):  # strip to "name @ zone x,y"
    return re.sub(r'\s*\(n=\d+[^)]*\)', '', s)
# 9 Nov 2026: an optional "L<minReq>-<maxReq>" argument sets the required-level window (default L0-30, quest level <= maxReq + 5),
# e.g.  python tooling\pool30.py L28-40 405 16591 33   for the 30-40 pools.
LO, HI = 0, 30
for a in sys.argv[1:]:
    m = re.fullmatch(r'L(\d+)-(\d+)', a)
    if m: LO, HI = int(m.group(1)), int(m.group(2))
for z in [int(a) for a in sys.argv[1:] if a.isdigit()]:
    ids = sorted(int(k) for k, v in Q.items() if f(v, 17) == z and alliance_ok(v) and not f(v, 7) and LO <= (f(v, 4) or 0) <= HI and (f(v,5) or 0) <= HI + 5)
    print(f"\n==== zoneOrSort {z} {ZN.get(z,'')}: {len(ids)} quests")
    for qid in ids:
        row = Q[str(qid)]
        st = f(row, 2) or []; en = f(row, 3) or []
        g = lambda a, i: (a[i] or []) if isinstance(a, list) and len(a) > i else []
        starters = [loc1(npc_loc(n)) for n in g(st, 0)] + [loc1(obj_loc(o)) for o in g(st, 1)] + [item_name(i) for i in g(st, 2)]
        enders = [loc1(npc_loc(n)) for n in g(en, 0)] + [loc1(obj_loc(o)) for o in g(en, 1)]
        pre1 = f(row, 13) or []; preg = f(row, 12) or []; nxt = f(row, 22)
        flag = 'DONE ' if qid in done else ''
        wh = WH.get(qid, {})
        print(f"{flag}{qid} {f(row,1)} | req{f(row,4)} L{f(row,5)} xp {XP.get(qid,'?')} {wh.get('envChange',{}).get('status','-')} | from {' / '.join(starters) or '?'} | to {' / '.join(enders) or '?'}" + (f" | pre {pre1 or preg}" if (pre1 or preg) else '') + (f" | next {nxt}" if nxt else ''))
