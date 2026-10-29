#!/usr/bin/env python3
"""Spawn helper: python3 loc.py "Crag Boar" "Rockjaw Trogg" 1125 obj:"Shimmerweed Basket" ...
Prints per-zone centroid and spread of Questie spawns for NPCs (by name or id) and objects (obj:name)."""
import json, sys, statistics
import os
BASE = os.environ.get('FOREVER_ATLAS', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
N = json.load(open(os.path.join(BASE, 'tooling', 'qdb', 'npc.json'), encoding='utf-8')); O = json.load(open(os.path.join(BASE, 'tooling', 'qdb', 'object.json'), encoding='utf-8'))
ZN = {1: 'Dun Morogh', 38: 'Loch Modan', 1537: 'Ironforge', 40: 'Westfall', 12: 'Elwynn Forest', 1519: 'Stormwind City', 44: 'Redridge Mountains', 10: 'Duskwood', 11: 'Wetlands', 148: 'Darkshore', 1581: 'The Deadmines', 717: 'The Stockade'}
def summarize(name, sp, extra=''):
    for z, pts in (sp or {}).items():
        pts = [p for p in pts if p and p[0] >= 0]
        if not pts: continue
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        print(f"  {name}{extra} @ {ZN.get(int(z), z)}: centre {statistics.mean(xs):.1f},{statistics.mean(ys):.1f}  range x {min(xs):.0f}-{max(xs):.0f} y {min(ys):.0f}-{max(ys):.0f}  n={len(pts)}" + (f"  first {pts[0][0]:.1f},{pts[0][1]:.1f}" if len(pts) <= 3 else ''))
for a in sys.argv[1:]:
    if a.startswith('obj:'):
        nm = a[4:]
        for k, v in O.items():
            if v[0] == nm: summarize(f"object {nm} [{k}]", v[3])
    elif a.isdigit():
        v = N.get(a)
        if v: summarize(f"{v[0]} [{a}]", v[6], f" L{v[3]}-{v[4]}" + (' ELITE' if v[5] == 1 else ' RARE' if v[5] == 2 else ''))
    else:
        for k, v in N.items():
            if v[0] == a: summarize(f"{a} [{k}]", v[6], f" L{v[3]}-{v[4]}" + (' ELITE' if v[5] == 1 else ' RARE' if v[5] == 2 else ''))
