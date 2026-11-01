#!/usr/bin/env python3
"""Hunter (levels 1-20, solo levelling, pet tanks) gear scoring for the Forever Alliance guide.

Reuses the tooltip parser from score_items.py (the ~180 Forever tooltips scraped on 24 Sep) and adds the
reward items of the guide's new/updated Forever quests straight from the atlas (data/quests.json 'items').

Weights (AP-equivalent, ranged attack power = 1), reasoning in claude/forever-guide/README.md:
  ranged weapon dps 14  (14 RAP = 1 dps of auto shot; the ranged weapon IS the class)
  Agi 2.4               (2 RAP + 1 melee AP + ~1% crit per ~20 Agi at these levels, and the pet inherits 100% crit)
  AP 1.0 (generic and ranged), melee AP 0.05, Str 0.05
  Sta 0.35              (pet gets 2 HP per Sta; the hunter rarely takes hits solo)
  Int 0.5, Spi 0.35     (Serpent Sting/Arcane Shot/Mend Pet mana; drinking is downtime)
  melee weapon dps 1.0  (stat stick; Raptor Strike only when something reaches you)
  spell power 0
Hunters use leather (mail at 40), bows/guns/crossbows, axes/swords/daggers/polearms/staves/fist weapons; no maces, shields, wands.
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from score_items import parse, fmt_stats, TOOLTIPS

BASE = os.environ.get('FOREVER_ATLAS', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
W = dict(rwdps=14.0, mwdps=1.0, agi=2.4, ap=1.0, str=0.05, sta=0.35, int=0.5, spi=0.35, sp=0.0)
SLOTBAK = {1:'Head',2:'Neck',3:'Shoulder',4:'Shirt',5:'Chest',6:'Waist',7:'Legs',8:'Feet',9:'Wrist',10:'Hands',11:'Finger',12:'Trinket',
           13:'One-Hand',14:'Off Hand',15:'Ranged',16:'Back',17:'Two-Hand',20:'Chest',21:'Main Hand',22:'Off Hand',23:'Held In Off-hand',25:'Thrown',26:'Ranged',28:'Relic'}

def from_atlas(quest_ids):
    """Reward items of the guide's Forever quests (atlas rows carry Wowhead 'equip' stats)."""
    Wq = json.load(open(os.path.join(BASE, 'data', 'quests.json'), encoding='utf-8'))
    out = []
    for q in quest_ids:
        v = Wq.get(str(q))
        if not v: continue
        for iid, it in (v.get('items') or {}).items():
            e = it.get('equip') or {}
            if 'slotbak' not in e: continue
            rec = dict(name=it['name'], id=int(iid), quest=q, str=e.get('str',0), agi=e.get('agi',0), sta=e.get('sta',0), int=e.get('int',0),
                       spi=e.get('spi',0), ap=e.get('atkpwr',0) or e.get('rgdatkpwr',0), sp=e.get('spldmg',0), exp=0,
                       wdps=float(e.get('dps',0) or 0), slot=SLOTBAK.get(e['slotbak'], str(e['slotbak'])), cls=None, req=e.get('reqlevel',0), ilvl=e.get('level',0))
            if e.get('rgddps'): rec['cls'] = 'Ranged'
            if e.get('armor') is not None and e.get('subclass') is not None: pass
            out.append(rec)
    return out

def usable(it):
    slot, cls = it['slot'], it['cls']
    if slot is None: return False, 'not equipment'
    if slot in ('Shirt', 'Tabard', 'Trinket', 'Relic'): return False, 'cosmetic/none'
    if cls == 'Mail': return False, 'mail (40+)'
    if cls in ('Plate', 'Shield', 'Wand', 'Mace'): return False, f'{cls.lower()} (hunter cannot use)'
    if slot in ('Off Hand', 'Held In Off-hand'): return False, 'off-hand (no shield/held item)'
    if slot == 'Thrown': return False, 'thrown (use a gun/bow)'
    return True, ''

def score(it):
    s = W['agi']*it['agi'] + W['ap']*it['ap'] + W['str']*it['str'] + W['sta']*it['sta'] + W['int']*it['int'] + W['spi']*it['spi'] + W['sp']*it['sp']
    if it['slot'] == 'Ranged' or it['cls'] in ('Bow', 'Gun', 'Crossbow', 'Ranged'):
        s += W['rwdps'] * it['wdps']
    elif it['slot'] in ('Two-Hand', 'Main Hand', 'One-Hand'):
        s += W['mwdps'] * it['wdps']
    return s

def main():
    import glob
    guide_dir = os.path.join(BASE, 'guide', 'Guidelime_ForeverShaman')   # pinned 1 Nov 2026 (the Hunter lines live only there)
    qids = set()
    for f in glob.glob(os.path.join(guide_dir, '0*.lua')):
        for m in re.finditer(r'\[Q[ACT](\d+)', open(f, encoding='utf-8').read()): qids.add(int(m.group(1)))
    data = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), TOOLTIPS), encoding='utf-8'))
    items = [parse(n, r) for n, r in data.items()]
    seen = {it['name'] for it in items}
    for it in from_atlas(qids):
        if it['name'] not in seen: items.append(it); seen.add(it['name'])
    items += [dict(name="Brawler's Leather Belt (LW 12)", id=None, quest=None, str=4, agi=4, sta=3, int=0, spi=0, ap=0, sp=0, exp=0, wdps=0, slot='Waist', cls='Leather', req=12, ilvl=0),
              dict(name="Brawler's Leather Gloves (LW 15)", id=None, quest=None, str=4, agi=4, sta=3, int=0, spi=0, ap=0, sp=0, exp=0, wdps=0, slot='Hands', cls='Leather', req=15, ilvl=0),
              dict(name="Brawler's Leather Armor (LW 15)", id=None, quest=None, str=5, agi=7, sta=3, int=0, spi=3, ap=0, sp=0, exp=0, wdps=0, slot='Chest', cls='Leather', req=15, ilvl=0),
              dict(name="Brawler's Leather Boots (LW 17)", id=None, quest=None, str=5, agi=5, sta=4, int=0, spi=0, ap=0, sp=0, exp=0, wdps=0, slot='Feet', cls='Leather', req=17, ilvl=0),
              dict(name="Brawler's Leather Pants (LW 20)", id=None, quest=None, str=6, agi=9, sta=4, int=0, spi=4, ap=0, sp=0, exp=0, wdps=0, slot='Legs', cls='Leather', req=20, ilvl=0),
              dict(name="Brawler's Leather Hood (LW 20)", id=None, quest=None, str=0, agi=8, sta=10, int=0, spi=0, ap=0, sp=0, exp=0, wdps=0, slot='Head', cls='Leather', req=20, ilvl=0),
              dict(name="Duty Bound Leggings (Ruins of Lordaeron)", id=None, quest=None, str=0, agi=6, sta=9, int=0, spi=0, ap=12, sp=0, exp=0, wdps=0, slot='Legs', cls='Leather', req=15, ilvl=0)]
    byq = {}
    for it in items:
        if it['quest']: byq.setdefault(it['quest'], []).append(it)
    print('HUNTER WEIGHTS (RAP = 1):', ' '.join(f'{k}={v}' for k, v in W.items()))
    print('\nPER-QUEST REWARD RANKING (quests in the guide with at least one hunter-usable reward)')
    for q in sorted(byq):
        rows = byq[q]
        if not any(usable(r)[0] for r in rows): continue
        print(f'\nquest {q}')
        for r in sorted(rows, key=lambda r: -score(r)):
            u, note = usable(r)
            print(f"   {score(r):6.1f}   {r['name']:36s} {str(r['slot']):12s} {str(r['cls'] or ''):8s} {fmt_stats(r)}{'' if u else '  ['+note+']'}  req{r['req']}")
    print('\nSLOT BY SLOT, hunter-usable, req <= 20')
    for sl in ['Ranged', 'Two-Hand', 'Main Hand', 'One-Hand', 'Head', 'Neck', 'Shoulder', 'Back', 'Chest', 'Wrist', 'Hands', 'Waist', 'Legs', 'Feet', 'Finger']:
        rows = [r for r in items if (r['slot'] == sl or (sl == 'Ranged' and r['cls'] in ('Bow','Gun','Crossbow'))) and usable(r)[0] and r['req'] <= 20 and score(r) > 0]
        rows.sort(key=lambda r: -score(r))
        if not rows: continue
        print(f'\n{sl}:')
        for r in rows[:8]:
            src = f"q{r['quest']}" if r['quest'] else ('craft/RoL' if r['id'] is None else 'drop')
            print(f"   {score(r):6.1f}  {r['name']:40s} {str(r['cls'] or ''):8s} {fmt_stats(r):42s} {src}  req{r['req']}")

if __name__ == '__main__':
    main()
