"""Protection warrior (1H + shield, levelling 1-30) gear weights for the Forever warrior variant.

Reasoning-only weights (no kill-speed model behind them yet): docs/forever-prot-stat-weights.md explains each number.
AP-equivalent, attack power = 1. Read by weights/profiles.py (profile 'prot'); score_items.parse() supplies the item
dicts (armor, defense, block, blockpct, dodge, parry, hit, crit added to the parser on 1 Nov 2026).

  CENTRAL       1H weapon dps 6, ranged dps 1, Str 2, AP 1, Sta 1.5, Agi 0.9, Armor 0.03/pt, Defense 1.5/pt,
                Block value 0.5, Block chance 3/%, Dodge 4/%, Parry 4/%, hit 6/%, crit 4/%, expertise 2/pt,
                Int / Spirit / spell power 0
  CONSERVATIVE  the same with Sta 1.0, Defense 1.0, Armor 0.02 (less credit for survival stats while solo levelling)
"""

CENTRAL = dict(wdps=6.0, rdps=1.0, str=2.0, ap=1.0, sta=1.5, agi=0.9, armor=0.03, defense=1.5, block=0.5, blockpct=3.0,
               dodge=4.0, parry=4.0, hit=6.0, crit=4.0, exp=2.0, int=0.0, spi=0.0, sp=0.0)
CONSERVATIVE = dict(CENTRAL, sta=1.0, defense=1.0, armor=0.02)

ONE_HAND_CLASSES = ('Axe', 'Mace', 'Sword', 'Dagger', 'Fist Weapon')
RANGED_CLASSES = ('Bow', 'Gun', 'Crossbow')
SECONDARY = 'ranged (pull slot)'


def usable(it):
    """(usable, note) for a Protection warrior at 1-30: mail at any level, leather, cloth only as a cloak, shields,
    1H axe/mace/sword/dagger/fist, ranged (bow/gun/crossbow/thrown) as a low-value pull slot; never a 2H."""
    slot, cls = it.get('slot'), it.get('cls')
    if it.get('thrown'):
        return True, SECONDARY
    if slot is None:
        return False, 'not equipment'
    if slot in ('Shirt', 'Tabard'):
        return False, 'cosmetic'
    if slot == 'Two-Hand':
        return False, '2H (1H + shield build)'
    if cls == 'Plate':
        return False, 'plate (40+)'
    if cls == 'Cloth' and slot != 'Back':
        return False, 'cloth'
    if slot == 'Held In Off-hand':
        return False, 'held in off-hand (shield slot)'
    if slot == 'Ranged':
        if cls in RANGED_CLASSES:
            return True, SECONDARY
        return False, '%s (warrior cannot use)' % (cls or 'ranged').lower()
    if slot == 'Off Hand':
        if cls == 'Shield':
            return True, 'shield'
        return False, 'off-hand weapon (shield build)'
    if slot in ('Main Hand', 'One-Hand'):
        if cls in ONE_HAND_CLASSES:
            return True, '1H'
        return False, '%s (not a 1H weapon)' % (cls or 'weapon').lower()
    return True, ''


def score(it, w):
    g = it.get
    s = (w['str'] * g('str', 0) + w['agi'] * g('agi', 0) + w['sta'] * g('sta', 0) + w['int'] * g('int', 0)
         + w['spi'] * g('spi', 0) + w['ap'] * g('ap', 0) + w['sp'] * g('sp', 0) + w['exp'] * g('exp', 0)
         + w['armor'] * g('armor', 0) + w['defense'] * g('defense', 0) + w['block'] * g('block', 0)
         + w['blockpct'] * g('blockpct', 0) + w['dodge'] * g('dodge', 0) + w['parry'] * g('parry', 0)
         + w['hit'] * g('hit', 0) + w['crit'] * g('crit', 0))
    if g('slot') in ('Main Hand', 'One-Hand'):
        s += w['wdps'] * g('wdps', 0.0)
    elif g('slot') == 'Ranged' or g('thrown'):
        s += w['rdps'] * g('wdps', 0.0)
    return s
