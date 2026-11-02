#!/usr/bin/env python3
r"""For every line with a [TARid ...] and a [G x,y Zone], compare the [G] with the NPC's nearest Forever-DB spawn.
python3 tooling\tarcheck.py [guide\Guidelime_ForeverShaman\08_RuinsOfLordaeron.lua ...]   (no arguments = every chapter; prints lines off by > 3 units, or with no spawn)
No arguments: the chapters of guidelib.ADDON (the Alliance folder unless FOREVER_GUIDE names another addon folder)."""
import json, re, sys, os, math
BASE = os.environ.get('FOREVER_ATLAS', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
N = json.load(open(os.path.join(BASE, 'tooling', 'qdb', 'npc.json'), encoding='utf-8'))
ZID = {'Dun Morogh': 1, 'Loch Modan': 38, 'Ironforge': 1537, 'Westfall': 40, 'Elwynn Forest': 12, 'Stormwind City': 1519, 'Redridge Mountains': 44,
       'Duskwood': 10, 'Wetlands': 11, 'Darkshore': 148, 'Teldrassil': 141, 'Darnassus': 1657, 'Hillsbrad Foothills': 267, 'Silverpine Forest': 130,
       'Ashenvale': 331, 'Alterac Mountains': 36, 'Arathi Highlands': 45, 'Stranglethorn Vale': 33, 'Stonetalon Mountains': 406, 'The Barrens': 17,
       'Tirisfal Glades': 85, 'Dustwallow Marsh': 15, 'Badlands': 3, 'Zephras Isle': 16593, 'Moonglade': 493}
import glob
# 28 Oct 2026: with no arguments, check every chapter in the addon folder (CLAUDE.md says to run it bare after [G] edits)
# 1 Nov 2026: the addon folder is guidelib.ADDON (FOREVER_GUIDE overrides it, e.g. a variant's output folder)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import guidelib as gl
FILES = sys.argv[1:] or sorted(glob.glob(os.path.join(gl.ADDON, '[0-9]*.lua')))
for fn in FILES:
    for i, ln in enumerate(open(fn, encoding='utf-8'), 1):
        tars = re.findall(r'\[TAR(\d+) ([^\]]*)\]', ln)
        gs = re.findall(r'\[G([\d.]+),([\d.]+) ([^\]]+)\]', ln)
        if not tars or not gs: continue
        gx, gy, gz = float(gs[0][0]), float(gs[0][1]), gs[0][2].strip()
        if gz not in ZID: print(f"{os.path.basename(fn)}:{i}: unknown zone name '{gz}'"); continue
        for nid, nm in tars:
            n = N.get(nid)
            if not n: print(f"{os.path.basename(fn)}:{i}: npc {nid} {nm} not in DB"); continue
            if (n[0] or '') != nm: print(f"{os.path.basename(fn)}:{i}: npc {nid} is '{n[0]}' in the DB, line says '{nm}'")
            sp = (n[6] or {}) if isinstance(n[6], dict) else {}
            pts = [p for p in sp.get(str(ZID[gz]), []) if p and p[0] is not None and p[0] >= 0]
            if not pts:
                zones = [z for z, v in sp.items() if any(p and p[0] is not None and p[0] >= 0 for p in v)]
                print(f"{os.path.basename(fn)}:{i}: {nm} has no spawn in {gz} (spawns in zones {zones})"); continue
            d = min(math.hypot(p[0] - gx, p[1] - gy) for p in pts)
            if d > 3:
                best = min(pts, key=lambda p: math.hypot(p[0] - gx, p[1] - gy))
                print(f"{os.path.basename(fn)}:{i}: {nm} [G{gx},{gy}] is {d:.1f} from nearest spawn {best[0]:.1f},{best[1]:.1f}")
