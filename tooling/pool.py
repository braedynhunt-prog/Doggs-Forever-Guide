#!/usr/bin/env python3
"""Merge the Wowhead Forever atlas (zone lists + new/updated quest detail + entity coords)
with Questie's Classic DB (unchanged quests) into one quest pool per zone."""
import json, re, sys
import os
BASE = os.environ.get('FOREVER_ATLAS', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from collections import defaultdict

ATLAS = os.path.join(BASE, 'data')
Q = json.load(open('qdb/quest.json')); N = json.load(open('qdb/npc.json'))
O = json.load(open('qdb/object.json')); IT = json.load(open('qdb/item.json'))
quests = {int(k): v for k, v in json.load(open(f'{ATLAS}/quests.json')).items()}
ents = json.load(open(f'{ATLAS}/entities.json'))
zones_meta = {z['id']: z for z in json.load(open('/mnt/user-data/uploads/WoW Forever Atlas/zones.json'))} if False else {}

# Questie zone ids -> names (AreaTable) for the ones we use
ZN = {1: 'Dun Morogh', 38: 'Loch Modan', 1537: 'Ironforge', 40: 'Westfall', 12: 'Elwynn Forest', 1519: 'Stormwind City',
      44: 'Redridge Mountains', 10: 'Duskwood', 11: 'Wetlands', 148: 'Darkshore', 141: 'Teldrassil', 1657: 'Darnassus',
      1581: 'The Deadmines', 717: 'The Stockade', 16919: 'The Hall of Thanes', 16611: 'Ruins of Lordaeron',
      85: 'Tirisfal Glades', 14: 'Durotar', 215: 'Mulgore', 267: 'Hillsbrad Foothills', 130: 'Silverpine Forest',
      331: 'Ashenvale', 36: 'Alterac Mountains', 45: 'Arathi Highlands', 33: 'Stranglethorn Vale', 406: 'Stonetalon Mountains',
      400: 'Thousand Needles', 3: 'Badlands', 8: 'Swamp of Sorrows', 47: 'The Hinterlands', 51: 'Searing Gorge', 405: 'Desolace'}
ALLIANCE_RACES = 77  # Human 1 + Dwarf 4 + NightElf 8 + Gnome 64
DWARF = 4
CLASS_BITS = {1: 'Warrior', 2: 'Paladin', 4: 'Hunter', 8: 'Rogue', 16: 'Priest', 64: 'Shaman', 128: 'Mage', 256: 'Warlock', 1024: 'Druid'}
SHAMAN = 64

def classes_of(mask):
    if not mask: return None
    return [n for b, n in CLASS_BITS.items() if mask & b]

def npc_loc(nid):
    r = N.get(str(nid))
    if not r: return None, None
    sp = r[6] or {}
    out = []
    for z, coords in sp.items():
        if coords and coords[0] and coords[0][0] >= 0:
            out.append((int(z), coords[0][0], coords[0][1], len(coords)))
    return r[0], out

def obj_loc(oid):
    r = O.get(str(oid))
    if not r: return None, None
    sp = r[3] or {}
    out = []
    for z, coords in sp.items():
        if coords and coords[0] and coords[0][0] >= 0:
            out.append((int(z), coords[0][0], coords[0][1], len(coords)))
    return r[0], out

def fmt_locs(locs, limit=2):
    if not locs: return 'no coords'
    return '; '.join(f"{ZN.get(z, z)} {x:.1f},{y:.1f}" + (f" (+{n-1})" if n > 1 else '') for z, x, y, n in locs[:limit])

def wh_ent_loc(kind, eid):
    e = ents.get(f'{kind}:{eid}')
    if not e: return None
    out = []
    for zid, arr in (e.get('mapper') or {}).items():
        for a in arr:
            c = a.get('coords') or []
            if c: out.append((int(zid), c[0][0], c[0][1], a.get('count', len(c)), a.get('uiMapName')))
    return out

def fmt_wh(locs, limit=2):
    if not locs: return 'no coords yet'
    return '; '.join(f"{nm or z} {x:.1f},{y:.1f}" + (f" (+{n-1})" if n and n > 1 else '') for z, x, y, n, nm in locs[:limit])

def questie_row(qid):
    r = Q.get(str(qid))
    if not r: return None
    r = list(r) + [None] * (40 - len(r))
    d = {'name': r[0], 'reqlevel': r[3], 'level': r[4], 'races': r[5], 'classes': classes_of(r[6]),
         'objtext': r[7], 'objectives': r[9], 'sourceItem': r[10], 'preGroup': r[11], 'preSingle': r[12],
         'childQuests': r[13], 'inGroupWith': r[14], 'exclusiveTo': r[15], 'zoneOrSort': r[16],
         'nextInChain': r[21], 'flags': r[22], 'special': r[23], 'parent': r[24], 'breadcrumbFor': r[26],
         'breadcrumbs': r[27], 'reqSkill': r[17], 'reqMaxLevel': r[31], 'availUntil': r[32]}
    st = r[1] or []; fn = r[2] or []
    starts = []
    for nid in (st[0] if len(st) > 0 and st[0] else []): starts.append(('npc', nid) + npc_loc(nid))
    for oid in (st[1] if len(st) > 1 and st[1] else []): starts.append(('object', oid) + obj_loc(oid))
    for iid in (st[2] if len(st) > 2 and st[2] else []):
        it = IT.get(str(iid)); starts.append(('item', iid, it[0] if it else f'item {iid}', None))
    ends = []
    for nid in (fn[0] if len(fn) > 0 and fn[0] else []): ends.append(('npc', nid) + npc_loc(nid))
    for oid in (fn[1] if len(fn) > 1 and fn[1] else []): ends.append(('object', oid) + obj_loc(oid))
    d['starts'] = starts; d['ends'] = ends
    return d

def load_zone(zid):
    return json.load(open(f'{ATLAS}/zone_{zid}.json'))

def pool_for(zid):
    z = load_zone(zid)
    rows = []
    for r in z['quests']:
        qid = r['id']; st = r.get('envChange', {}).get('status')
        side = r.get('side')
        # side: 1 A, 2 H, 3 both; None unspecified
        if side == 2: continue
        row = {'id': qid, 'name': r['name'], 'level': r.get('level'), 'reqlevel': r.get('reqlevel'), 'xp': r.get('xp'),
               'side': {1: 'A', 2: 'H', 3: 'AH'}.get(side, '?'), 'status': st, 'reqclass': r.get('reqclass'),
               'category': r.get('category'), 'itemchoices': [i[0] for i in r.get('itemchoices', [])],
               'itemrewards': [i[0] for i in r.get('itemrewards', [])], 'zone': zid}
        qr = questie_row(qid)
        row['questie'] = qr
        if qr:
            # faction/race filter from Questie: races bitmask; 0 = all
            races = qr['races'] or 0
            if races and not (races & DWARF): row['not_dwarf'] = True
            if races and not (races & ALLIANCE_RACES): row['horde_only'] = True
        wq = quests.get(qid)
        row['wh'] = wq
        rows.append(row)
    return z, rows

def describe(row, shaman_only=False):
    q = row; qr = q['questie']; wq = q['wh']
    lvl = q['level']; req = q['reqlevel']; xp = q['xp']
    cls = q.get('reqclass')
    if isinstance(cls, int): cls = '/'.join(classes_of(cls) or []) or ''
    elif qr and qr['classes']: cls = '/'.join(qr['classes'])
    cls = cls or ''
    typ = (wq or {}).get('info', {}).get('type', '') or ''
    st = q['status']
    # starts
    if wq and (wq['info'].get('start') or wq['info'].get('end')):
        s = '; '.join(f"{e['name']} ({fmt_wh(wh_ent_loc(e['kind'], e['id']))})" for e in wq['info']['start']) or '-'
        e_ = '; '.join(f"{e['name']} ({fmt_wh(wh_ent_loc(e['kind'], e['id']))})" for e in wq['info']['end']) or '-'
    elif qr:
        s = '; '.join(f"{nm} ({fmt_locs(loc)})" if kind != 'item' else f"[item] {nm}" for kind, i, nm, loc in qr['starts']) or '-'
        e_ = '; '.join(f"{nm} ({fmt_locs(loc)})" for kind, i, nm, loc in qr['ends']) or '-'
    else:
        s = e_ = '?'
    pre = ''
    if qr:
        if qr['preSingle']: pre += f" pre(any):{qr['preSingle']}"
        if qr['preGroup']: pre += f" pre(all):{qr['preGroup']}"
        if qr['nextInChain']: pre += f" next:{qr['nextInChain']}"
        if qr['exclusiveTo']: pre += f" excl:{qr['exclusiveTo']}"
        if qr['breadcrumbFor']: pre += f" breadcrumbFor:{qr['breadcrumbFor']}"
        if qr['special'] and qr['special'] & 1: pre += ' REPEATABLE'
        if qr['flags'] and qr['flags'] & 1: pre += ' (stay-alive)'
    ser = ''
    if wq and wq.get('series'):
        ser = ' series ' + '/'.join(f"{x['n']}:{x['id']}" for x in wq['series'])
    obj = ''
    if wq and wq.get('objective_text'): obj = wq['objective_text'][:110]
    elif qr and qr['objtext']: obj = (qr['objtext'][0] if qr['objtext'] else '')[:110]
    chg = ' | '.join((wq or {}).get('g', {}).get('envChange', {}).get('lines', [])) if wq else ''
    rew = ''
    if wq and wq.get('items'):
        rew = ', '.join(f"{v['name']}" for v in wq['items'].values() if v.get('name'))
    elif q['itemchoices'] or q['itemrewards']:
        rew = ', '.join(IT[str(i)][0] if str(i) in IT else str(i) for i in (q['itemchoices'] + q['itemrewards']))
    flag = ''
    if q.get('horde_only'): flag += ' HORDE-ONLY'
    elif q.get('not_dwarf'): flag += ' NOT-DWARF'
    return (f"{q['id']:>6} [{st[:3]}] L{lvl or '?'}/req{req or '?'} {xp or 0:>5}xp {q['side']:<2} {(cls or ''):<8} {typ:<8} {q['name']}{flag}\n"
            f"        start: {s}\n        end:   {e_}\n        obj:   {obj}{pre}{ser}\n" + (f"        rew:   {rew}\n" if rew else '') + (f"        chg:   {chg}\n" if chg else ''))

if __name__ == '__main__':
    zids = [int(x) for x in sys.argv[1:]] or [1]
    for zid in zids:
        z, rows = pool_for(zid)
        rows.sort(key=lambda r: ((r['level'] or 0), r['id']))
        tot = defaultdict(int)
        print(f"\n######## {ZN.get(zid, zid)} ({zid}) — {len(rows)} Alliance-usable quests")
        for r in rows:
            if r.get('horde_only') or r.get('not_dwarf'): continue
            if (r['reqlevel'] or 0) > 22 or (r['level'] or 0) > 27: continue
            qr = r['questie']
            if qr and qr['special'] and qr['special'] & 1: continue
            if r['name'].startswith(('Darkmoon', 'Carnival', 'Winter', 'Stolen Winter', 'A Smokywood', 'Metzen', 'Great-father', 'Greatfather', 'Treats for', 'Camping 101')):
                if not r['name'].startswith('Camping 101'): continue
            print(describe(r))
