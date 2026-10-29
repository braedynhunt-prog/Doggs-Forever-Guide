#!/usr/bin/env python3
r"""Data checks for the Forever Guidelime files (the flow check is check_guide.py; both read guidelib.py).

Modules (python tooling\verify.py [--all] [--module questnpc,tar,gates] [--update-baseline] [--chain Dwarf]):
  questnpc  every [QA]/[QT] line's [TAR] is the quest's starter / finisher in tooling/qdb/quest.json
  tar       every [TAR] exists in npc.json with the written name, and the line's [G x,y Zone] is within 3 units of a DB spawn
            (first [TAR] on the line; later ones only need to be within 15, they are "next to" the first)
  gates     skill-gated steps (recipes, trainer ranks, Camping 101) come after the steps that provide the skill
            (tooling/skill_gates.json: providers = learn / cook-to-N / fish-to-N / Journeyman; gates = min skill, mode)
Lines on the Dwarf Shaman route only (the Human / Hunter lines are unmaintained since 27 Oct 2026).

Findings are "module  file:line  message". tooling/verify_baseline.txt holds the accepted ones: the default run prints
only findings that are not in it and exits 1 when there are any; --all prints everything grouped by module;
--update-baseline rewrites the baseline from the current run.
"""
import os, sys, re, json, math, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import guidelib as gl

HERE = os.path.dirname(os.path.abspath(__file__))
BASELINE = os.path.join(HERE, 'verify_baseline.txt')
GATES = os.path.join(HERE, 'skill_gates.json')
NEAR, NEAR_SECOND = 3.0, 15.0

def route_lines(chain='Dwarf'):
    """(file, ln, line, band) for every step on the chain, skipping other races' and Hunter-only lines."""
    for f in gl.chain_files(chain):
        txt = gl.read(f); ga = gl.chapter_ga(txt); band = gl.chapter_band(txt)
        for ln, line in gl.steps(txt):
            if not gl.on_chain(line, ga, chain): continue
            m = gl.A_TAG.search(line)
            if m and 'Hunter' in m.group(1) and 'Shaman' not in m.group(1): continue
            yield f, ln, line, band

def fmt_ids(ids, name):
    return ', '.join(f'{i} {name(i) or "?"}' for i in ids)

# ---------------------------------------------------------------- questnpc
def check_questnpc(lines):
    out = []
    for f, ln, line, band in lines:
        tars = gl.tars(line)
        for code, qid, title in gl.quest_tags(line):
            if code not in ('QA', 'QT'): continue
            ends = gl.qends(qid) if code == 'QT' else gl.qstarts(qid)
            what = 'finisher' if code == 'QT' else 'starter'
            if ends is None:
                out.append((f, ln, f'[{code}{qid}] {gl.qname(qid)}: quest not in the Forever DB (not checkable)')); continue
            npcs = ends['npc']; objs = ends['object']; items = ends.get('item', [])
            if tars:
                if any(t in npcs for t, _ in tars): continue
                if not npcs and (objs or items):
                    kind = 'object ' + fmt_ids(objs, gl.object_name) if objs else 'item ' + ', '.join(map(str, items))
                    out.append((f, ln, f'[{code}{qid}] {gl.qname(qid)}: {what} in the DB is {kind}; line has [TAR{tars[0][0]} {tars[0][1]}] (fine if the TAR is just the nearby NPC)'))
                elif not npcs:
                    out.append((f, ln, f'[{code}{qid}] {gl.qname(qid)}: DB lists no {what} at all; line has [TAR{tars[0][0]} {tars[0][1]}]'))
                else:
                    out.append((f, ln, f'[{code}{qid}] {gl.qname(qid)}: line has {", ".join(f"[TAR{t} {n}]" for t, n in tars)}; DB {what}: {fmt_ids(npcs, gl.npc_name)}'))
            else:
                if npcs:
                    out.append((f, ln, f'[{code}{qid}] {gl.qname(qid)}: no [TAR] on the line; DB {what}: {fmt_ids(npcs, gl.npc_name)}'))
    return out

# ---------------------------------------------------------------- tar
def check_tar(lines):
    out = []
    for f, ln, line, band in lines:
        tars = gl.tars(line)
        if not tars: continue
        gs = gl.gotos(line)
        for i, (nid, nm) in enumerate(tars):
            dbname = gl.npc_name(nid)
            if dbname is None:
                out.append((f, ln, f'[TAR{nid} {nm}] not in the Forever DB')); continue
            if dbname != nm:
                out.append((f, ln, f'[TAR{nid}] is "{dbname}" in the DB, line says "{nm}"'))
            if not gs: continue
            gx, gy, gz = gs[0]
            if gz not in gl.ZID:
                out.append((f, ln, f'[G{gx},{gy} {gz}]: zone has no map id in guidelib.ZID')); continue
            pts = gl.npc_spawns(nid, gl.ZID[gz])
            if not pts:
                zones = gl.npc_zones(nid)
                where = f'spawns in zones {zones}' if zones else 'no spawn data in the DB at all'
                out.append((f, ln, f'{nm} ({nid}) has no spawn in {gz} ({where})')); continue
            best = min(pts, key=lambda p: math.hypot(p[0] - gx, p[1] - gy))
            d = math.hypot(best[0] - gx, best[1] - gy)
            lim = NEAR if i == 0 else NEAR_SECOND
            if d > lim:
                tag = '' if i == 0 else ' (secondary TAR, 15-unit limit)'
                out.append((f, ln, f'{nm} [G{gx},{gy}] is {d:.1f} from the nearest spawn {best[0]:.1f},{best[1]:.1f}{tag}'))
    return out

# ---------------------------------------------------------------- gates
def check_gates(lines):
    cfg = json.load(open(GATES, encoding='utf-8'))
    state = {s: {'learned': False, 'cap': 0, 'target': 0, 'where': None} for s in cfg['skills']}
    out = []
    for f, ln, line, band in lines:
        # a step is one unit: what it provides (learn, fish-to-N, a rank) counts for the gates on the same line
        for p in cfg['providers']:
            if p['match'] not in line: continue
            st = state[p['skill']]
            if p.get('learn'):
                st['learned'] = True; st['cap'] = max(st['cap'], 75); st['target'] = max(st['target'], 1)
            if p.get('target'):
                st['target'] = max(st['target'], p['target']); st['where'] = f'{os.path.basename(f)}:{ln}'
            if p.get('rank'):
                st['cap'] = max(st['cap'], p['rank'])
        # gates apply to actionable steps only: [OC] lines are notes (plans, gear calls, labels) and may name a recipe
        # or trainer long before the route reaches it. Providers on [OC] lines still count (the targets live in notes).
        for g in (cfg['gates'] if not line.startswith('[OC]') else ()):
            if g['match'] not in line: continue
            st = state[g['skill']]; skill = g['skill']; need = g['min']; mode = g['mode']
            cond = bool(re.search(r'\bif (you|Cooking|Fishing|First Aid|Skinning|Mining)\b', line)) or 'if you' in line
            soft = ' [conditional step]' if cond else ''
            src = '' if 'Classic' not in g['source'] and 'unverified' not in g['source'] else ' [gate value unverified on Forever]'
            if not st['learned']:
                out.append((f, ln, f'{g["match"]} needs {skill} {need} but the route has not learned {skill} yet{soft}{src}')); continue
            if mode in ('rank', 'target') and st['cap'] < need:
                out.append((f, ln, f'{g["match"]} needs {skill} {need}; the last rank on the route caps {skill} at {st["cap"]}{soft}{src}'))
            if mode == 'target' and st['target'] < need:
                w = f' (last target: {skill} {st["target"]} at {st["where"]})' if st['where'] else f' (no {skill} target stated yet)'
                out.append((f, ln, f'{g["match"]} needs {skill} {need}; the route has only asked for {skill} {st["target"]} so far{w}{soft}{src}'))
            if g.get('level') and band[1] < g['level']:
                out.append((f, ln, f'{g["match"]} needs level {g["level"]}; the chapter tops out at {band[1]}{soft}{src}'))
    return out

MODULES = {'questnpc': check_questnpc, 'tar': check_tar, 'gates': check_gates}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--all', action='store_true', help='print every finding grouped by module, not just the new ones')
    ap.add_argument('--module', default=','.join(MODULES), help='comma list of modules to run')
    ap.add_argument('--update-baseline', action='store_true', help='write the current findings as the accepted baseline')
    ap.add_argument('--chain', default='Dwarf')
    a = ap.parse_args()
    lines = list(route_lines(a.chain))
    findings = []   # (module, file, ln, msg)
    for mod in a.module.split(','):
        for f, ln, msg in MODULES[mod](lines):
            findings.append((mod, os.path.basename(f), ln, msg))
    keys = [f'{m}  {f}:{ln}  {msg}' for m, f, ln, msg in findings]
    if a.update_baseline:
        open(BASELINE, 'w', encoding='utf-8', newline='\n').write('\n'.join(keys) + ('\n' if keys else ''))
        print(f'baseline written: {len(keys)} findings -> {os.path.relpath(BASELINE)}'); return 0
    base = set(open(BASELINE, encoding='utf-8').read().splitlines()) if os.path.exists(BASELINE) else set()
    if a.all:
        for mod in a.module.split(','):
            rows = [k for k, (m, *_rest) in zip(keys, findings) if m == mod]
            print(f'== {mod}: {len(rows)} ==')
            for k in rows: print(('    ' if k in base else 'NEW ') + k)
        print(f'\n{len(lines)} route lines; {len(keys)} findings, {sum(k not in base for k in keys)} not in the baseline')
        return 0
    new = [k for k in keys if k not in base]
    gone = [k for k in base if k not in set(keys)]
    for k in new: print('NEW ' + k)
    print(f'{len(keys)} findings ({len(new)} new, {len(gone)} baseline lines no longer produced)')
    return 1 if new else 0

if __name__ == '__main__':
    sys.exit(main())
