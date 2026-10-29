#!/usr/bin/env python3
"""Dump full atlas detail for new/updated quests: objectives with entity coords, comments, item stats."""
import json, sys, re
import os
BASE = os.environ.get('FOREVER_ATLAS', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
ATLAS = os.path.join(BASE, 'data')
quests = {int(k): v for k, v in json.load(open(f'{ATLAS}/quests.json')).items()}
ents = json.load(open(f'{ATLAS}/entities.json'))

def ent_locs(kind, eid, limit=3):
    e = ents.get(f'{kind}:{eid}')
    if not e: return 'NOT FETCHED'
    out = []
    for zid, arr in (e.get('mapper') or {}).items():
        for a in arr:
            c = a.get('coords') or []
            if c:
                pts = ', '.join(f"{x:.1f},{y:.1f}" for x, y in c[:limit])
                out.append(f"{a.get('uiMapName') or zid}: {pts}" + (f" (+{a.get('count', len(c)) - min(limit, len(c))} more)" if a.get('count', len(c)) > limit else ''))
    g = e.get('g') or {}
    lv = ''
    if g.get('minlevel'): lv = f" L{g.get('minlevel')}-{g.get('maxlevel')}" + (' ELITE' if g.get('classification') == 1 else (' RARE' if g.get('classification') in (2, 4) else ''))
    return (e.get('name') or '?') + lv + ' @ ' + ('; '.join(out) if out else 'no coords')

def equip_str(eq):
    if not eq: return ''
    parts = []
    slot = eq.get('slotbak')
    SL = {1: 'Head', 2: 'Neck', 3: 'Shoulder', 4: 'Shirt', 5: 'Chest', 6: 'Waist', 7: 'Legs', 8: 'Feet', 9: 'Wrist', 10: 'Hands', 11: 'Ring', 12: 'Trinket', 13: '1H', 14: 'Shield', 15: 'Ranged', 16: 'Back', 17: '2H', 18: 'Bag', 21: 'MH', 22: 'OH', 23: 'Held', 25: 'Thrown', 26: 'Ranged', 28: 'Relic'}
    if slot: parts.append(SL.get(slot, f'slot{slot}'))
    if eq.get('dps'): parts.append(f"{eq.get('dmgmin1')}-{eq.get('dmgmax1')} spd {eq.get('speed')} = {eq['dps']} dps")
    if eq.get('armor'): parts.append(f"{eq['armor']} armor")
    for k, n in (('agi', 'agi'), ('str', 'str'), ('sta', 'sta'), ('int', 'int'), ('spi', 'spi'), ('atkpwr', 'AP'), ('splpwr', 'SP'), ('mlecritstrkpct', 'crit%'), ('hitrtng', 'hit'), ('block', 'block')):
        if eq.get(k): parts.append(f"+{eq[k]} {n}")
    if eq.get('reqlevel'): parts.append(f"req {eq['reqlevel']}")
    return ' | '.join(parts)

def show(qid):
    q = quests.get(qid)
    if not q: print(qid, 'not in atlas'); return
    g = q.get('g', {}); info = q.get('info', {})
    print(f"=== {qid} {q.get('name')}  L{g.get('level')}/req{g.get('reqlevel')} xp {g.get('xp')} side {g.get('side')} type {info.get('type','')} reqs {info.get('reqs','')}")
    for k in ('start', 'end'):
        for e in info.get(k, []): print(f"  {k}: {e['name']} [{e['kind']} {e['id']}] -> {ent_locs(e['kind'], e['id'])}")
    print('  objective:', (q.get('objective_text') or '').replace('\n', ' ')[:300])
    for o in q.get('objectives', []):
        loc = ent_locs(o['kind'], o['eid']) if o.get('kind') in ('npc', 'object') else ''
        print(f"    - {o['qty']} x {o['text'][:60]} [{o.get('kind')} {o.get('eid')}] {loc}")
    if q.get('series'): print('  series:', ' > '.join(f"{s['n']}:{s['id']}{'*' if s.get('current') else ''}" for s in q['series']))
    for iid, it in (q.get('items') or {}).items():
        print(f"  item {iid}: {it.get('name')} q{it.get('quality')} {equip_str(it.get('equip'))}")
    for c in q.get('comments', [])[:3]: print('  comment:', c.replace('\n', ' ')[:300])
    if g.get('envChange', {}).get('lines'): print('  changes:', ' | '.join(g['envChange']['lines']))
    d = q.get('description')
    if d: print('  desc:', d.replace('\n', ' ')[:400])
    print()

if __name__ == '__main__':
    for a in sys.argv[1:]: show(int(a))
