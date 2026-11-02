"""Feral druid (bear 10-20, cat from 20; levelling 1-30) gear weights for the Forever druid variant.

Reasoning-only weights (no kill-speed model behind them yet). Verified (Blizzard's Forever class deep dive,
https://news.blizzard.com/en-us/article/24301515/world-of-warcraft-forever-class-deep-dives-hunter-and-druid): form
auto-attack dps equals the equipped weapon's dps (attack speed fixed per form), Rake and Swipe scale with attack power,
and Cat Form gives "+12 AP plus Agility". So weapon dps is weighted in every band at the Classic conversion (1 dps =
14 AP at a fixed speed; 10 in the conservative set). Unverified on Forever: Strength to AP in forms (2 per point
assumed, Classic), the feral attack power wording on gear, the per-form attack speeds, and the Forever feral talents
(Feral Charge, Primal Bite; Blizzard's deep dive). Staves and 2H maces get no bias over 1H maces, daggers and fist weapons
beyond their dps and stats. docs/forever-feral-stat-weights.md explains each number. AP-equivalent, attack power = 1.
Read by weights/profiles.py (profile 'feral'); score_items.parse() supplies the item dicts (feral_ap = "attack power
in Cat/Bear form" bonuses, counted here as AP; the enh and prot scorers never read that key).

  Bear (bands 10, 15)       CENTRAL       weapon dps 14, Str 2, Agi 1.2, Sta 1.5, AP 1, Armor 0.05/pt (Bear Form takes
                                          180% armor from items), Int 0.3, Spirit 0.2, crit 6/%, hit 8/%, rest 0
                            CONSERVATIVE  the same with weapon dps 10, Agi 1.0, Sta 1.2, crit 4, Armor 0.03
  Cat (bands 20, 25, 30)    CENTRAL       weapon dps 14, Str 2, Agi 1.6, AP 1, Sta 0.6, crit 8/%, hit 10/%, Int 0.2,
                                          Spirit 0.2, Armor 0, rest 0
                            CONSERVATIVE  the same with weapon dps 10, Agi 1.3, crit 5
"""

_ZERO = dict(wdps=0.0, rdps=0.0, str=0.0, ap=0.0, sta=0.0, agi=0.0, armor=0.0, defense=0.0, block=0.0, blockpct=0.0,
             dodge=0.0, parry=0.0, hit=0.0, crit=0.0, exp=0.0, int=0.0, spi=0.0, sp=0.0)

BEAR_CENTRAL = dict(_ZERO, wdps=14.0, str=2.0, agi=1.2, sta=1.5, ap=1.0, armor=0.05, int=0.3, spi=0.2, crit=6.0, hit=8.0)
BEAR_CONSERVATIVE = dict(BEAR_CENTRAL, wdps=10.0, agi=1.0, sta=1.2, crit=4.0, armor=0.03)

CAT_CENTRAL = dict(_ZERO, wdps=14.0, str=2.0, agi=1.6, ap=1.0, sta=0.6, crit=8.0, hit=10.0, int=0.2, spi=0.2)
CAT_CONSERVATIVE = dict(CAT_CENTRAL, wdps=10.0, agi=1.3, crit=5.0)

BEAR_BANDS = (10, 15)
CAT_BANDS = (20, 25, 30)

# a druid has no pull slot and no shield set: nothing is a secondary-only choice
SECONDARY = None

ONE_HAND_CLASSES = ('Mace', 'Dagger', 'Fist Weapon')
TWO_HAND_CLASSES = ('Staff', 'Mace')


def band_weights():
    """{band: (central, conservative)}: bear sets for 10 and 15, cat sets for 20, 25 and 30."""
    out = {b: (BEAR_CENTRAL, BEAR_CONSERVATIVE) for b in BEAR_BANDS}
    out.update({b: (CAT_CENTRAL, CAT_CONSERVATIVE) for b in CAT_BANDS})
    return out


def usable(it):
    """(usable, note) for a feral druid at 1-30: cloth and leather at any level, cloaks, neck/rings/trinkets, staves,
    1H and 2H maces, daggers, fist weapons, held-in-off-hand items and idols. No shields, mail, plate, off-hand weapons
    or ranged weapons (bow / gun / crossbow / wand / thrown)."""
    slot, cls = it.get('slot'), it.get('cls')
    if it.get('thrown'):
        return False, 'thrown (druid cannot use)'
    if slot is None:
        return False, 'not equipment'
    if slot in ('Shirt', 'Tabard'):
        return False, 'cosmetic'
    if cls in ('Mail', 'Plate'):
        return False, '%s (druid cannot use)' % cls.lower()
    if cls == 'Shield':
        return False, 'shield (druid cannot use)'
    if slot == 'Ranged':
        return False, '%s (druid cannot use)' % (cls or 'ranged').lower()
    if slot == 'Relic':
        if cls == 'Idol':
            return True, 'idol'
        return False, '%s (druid cannot use)' % (cls or 'relic').lower()
    if slot == 'Held In Off-hand':
        return True, 'held in off-hand'
    if slot == 'Off Hand':
        return False, 'off-hand weapon (druid cannot dual wield)'
    if slot in ('Main Hand', 'One-Hand'):
        if cls in ONE_HAND_CLASSES:
            return True, '1H'
        return False, '%s (druid cannot use)' % (cls or 'weapon').lower()
    if slot == 'Two-Hand':
        if cls in TWO_HAND_CLASSES:
            return True, '2H'
        return False, '%s (druid cannot use)' % (cls or 'weapon').lower()
    return True, ''


def score(it, w):
    g = it.get
    s = (w['str'] * g('str', 0) + w['agi'] * g('agi', 0) + w['sta'] * g('sta', 0) + w['int'] * g('int', 0)
         + w['spi'] * g('spi', 0) + w['ap'] * (g('ap', 0) + g('feral_ap', 0)) + w['sp'] * g('sp', 0)
         + w['exp'] * g('exp', 0) + w['armor'] * g('armor', 0) + w['defense'] * g('defense', 0)
         + w['block'] * g('block', 0) + w['blockpct'] * g('blockpct', 0) + w['dodge'] * g('dodge', 0)
         + w['parry'] * g('parry', 0) + w['hit'] * g('hit', 0) + w['crit'] * g('crit', 0))
    if g('slot') in ('Main Hand', 'One-Hand', 'Two-Hand'):
        s += w['wdps'] * g('wdps', 0.0)
    elif g('slot') == 'Ranged' or g('thrown'):
        s += w['rdps'] * g('wdps', 0.0)
    return s
