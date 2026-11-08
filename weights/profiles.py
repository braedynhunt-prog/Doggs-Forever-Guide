"""Gear-weight profiles for the guide tooling (registry; added 1 Nov 2026 for the generator-built warrior variant).

PROFILES = {'enh': ENH, 'prot': PROT, 'feral': FERAL}. Each profile gives:
  weights(band)     -> (central, conservative) weight dicts for a level band (BANDS 10/15/20/25/30)
  usable(item)      -> (bool, note) on a score_items.parse() item dict
  score(item, w)    -> AP-equivalent score
  secondary         usable() note that marks a secondary slot: such items count as "best" only when nothing else is
                    usable (enh: the 1H shield set; prot: the ranged pull slot)
  client_usable     tooling/client Item.csv (ClassID, SubclassID) -> (label, allowed InventoryTypes or None), the
                    filter tooling/dungeon_loot.py applies before tooltips are read
  slot_suffix       client label -> text appended to its slot/type in dungeon_loot ("(shield set)" for enh 1H)
  slot_group        score_items slot -> comparison group for dungeon_loot's baseline
  describe(item)    short item wording for gear lines, e.g. "mail hands +5 Str +5 Sta, Def +3"
  nothing_text      wording when a quest offers nothing usable ("nothing for a warrior - vendor")
  class_tag         the Guidelime [A ...] word for the class's gear lines

'enh' wraps the 2H Enhancement shaman behaviour exactly as score_items.py / dungeon_loot.py / gear_calls.py had it
(level-20 sets copied from score_items.main(), other bands take Int/Agi from enh_weights; no mace term since 1 Nov
2026). 'prot' is weights/prot_weights.py (reasoning-only weights, docs/forever-prot-stat-weights.md). 'feral' (added
2 Nov 2026 for the druid variant) is weights/feral_weights.py: bear weights for bands 10/15, cat for 20/25/30
(reasoning-only, docs/forever-feral-stat-weights.md).
"""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import score_items  # noqa: E402
import prot_weights  # noqa: E402
import feral_weights  # noqa: E402

BANDS = (10, 15, 20, 25, 30)


def nearest_band(level):
    return min(BANDS, key=lambda b: (abs(b - level), -b))


# ---------------------------------------------------------------- enh (2H Enhancement shaman)
# Copied verbatim from score_items.main() (level-20 band; no mace term since 1 Nov 2026).
# 3 Nov 2026: Int 1.05 -> 1.55 (Mental Dexterity 50/100/150% of Int, was 33/67/100%; source: Blizzard dev notes 3 Nov)
# 8 Nov 2026: Spirit 1.0 -> 2.5, SP 1.5 -> 2.0, Int 1.55 -> 1.65, Agi 0.85 -> 0.8 after the character-sheet readings
# (regen 1.25 x Spirit per 5 s, Int-independent; client crit tables; Earth Shock ranks of the 3 Nov build) - the
# one-shock-per-fight case of the model; conservative = Lightning Shield only. docs/audit-2026-11-08.md.
ENH_W20_CENTRAL = dict(wdps=14.0, str=2.0, ap=1.0, int=1.65, agi=0.8, spi=2.5, sta=0.0, sp=2.0, exp=3.0)
ENH_W20_CONSERVATIVE = dict(wdps=14.0, str=2.0, ap=1.0, int=1.65, agi=0.8, spi=1.5, sta=0.0, sp=1.0, exp=1.0)

_enh_cache = {}


def enh_band_weights():
    """{band: (central, conservative)}. 20 = score_items' sets; the other bands = those with model Int/Agi for the band."""
    if not _enh_cache:
        from enh_weights import band_scenarios, weights as model_weights
        out = {20: (ENH_W20_CENTRAL, ENH_W20_CONSERVATIVE)}
        scen = band_scenarios()
        for b in BANDS:
            if b == 20:
                continue
            m, _ = model_weights(scen[b])
            over = {k: round(m[k], 2) for k in ('int', 'agi')}
            out[b] = (dict(ENH_W20_CENTRAL, **over), dict(ENH_W20_CONSERVATIVE, **over))
        _enh_cache.update(out)
    return dict(_enh_cache)


# Item.csv ClassID / SubclassID -> label. A tuple value restricts the row to those InventoryTypes
# (2 neck, 11 finger, 12 trinket, 16 cloak). Anything not listed is dropped.
ENH_USABLE = {
    (2, 0):  ('1H axe', None),
    (2, 1):  ('2H axe', None),
    (2, 4):  ('1H mace', None),
    (2, 5):  ('2H mace', None),
    (2, 10): ('staff', None),
    (2, 13): ('fist weapon', None),
    (2, 15): ('dagger', None),
    (4, 2):  ('leather', None),
    (4, 1):  ('cloth', (16,)),            # cloth only as a cloak
    (4, 0):  ('misc', (2, 11, 12)),       # neck, ring, trinket
}
PROT_USABLE = {
    (2, 0):  ('1H axe', None),
    (2, 4):  ('1H mace', None),
    (2, 7):  ('1H sword', None),
    (2, 13): ('fist weapon', None),
    (2, 15): ('dagger', None),
    (2, 2):  ('bow', None),
    (2, 3):  ('gun', None),
    (2, 18): ('crossbow', None),
    (2, 16): ('thrown', None),
    (4, 3):  ('mail', None),
    (4, 2):  ('leather', None),
    (4, 6):  ('shield', None),
    (4, 1):  ('cloth', (16,)),            # cloth only as a cloak
    (4, 0):  ('misc', (2, 11, 12)),       # neck, ring, trinket
}
# 2 Nov 2026: feral druid - cloth and leather in every slot, staves, 1H/2H maces, daggers, fist weapons, held-in-off-hand
# items (misc, InventoryType 23) and idols (armor subclass 8, InventoryType 28). No mail, shields or ranged weapons.
FERAL_USABLE = {
    (2, 4):  ('1H mace', None),
    (2, 5):  ('2H mace', None),
    (2, 10): ('staff', None),
    (2, 13): ('fist weapon', None),
    (2, 15): ('dagger', None),
    (4, 2):  ('leather', None),
    (4, 1):  ('cloth', None),
    (4, 0):  ('misc', (2, 11, 12, 23)),   # neck, ring, trinket, held in off-hand
    (4, 8):  ('idol', (28,)),
}

SLOT_WORD = {'Head': 'head', 'Neck': 'neck', 'Shoulder': 'shoulders', 'Back': 'cloak', 'Chest': 'chest', 'Wrist': 'wrist',
             'Hands': 'hands', 'Waist': 'waist', 'Legs': 'legs', 'Feet': 'feet', 'Finger': 'ring', 'Trinket': 'trinket'}
WEAPON_WORD = {'Axe': 'axe', 'Mace': 'mace', 'Sword': 'sword', 'Dagger': 'dagger', 'Fist Weapon': 'fist weapon',
               'Staff': 'staff', 'Polearm': 'polearm', 'Bow': 'bow', 'Gun': 'gun', 'Crossbow': 'crossbow', 'Wand': 'wand'}
PRIMARY = (('str', 'Str'), ('agi', 'Agi'), ('sta', 'Sta'), ('int', 'Int'), ('spi', 'Spi'), ('ap', 'AP'), ('sp', 'SP'))


def _num(v):
    return ('%g' % v) if isinstance(v, float) else str(v)


def describe(it, w, feral=False):
    """'mail hands +5 Str +5 Sta, Def +3' / '1H mace 14.0 dps +3 Str' / 'shield 642 armor 13 block +8 Sta'.
    Stats with zero weight in w are left out (a warrior's line does not quote Intellect). feral=True (the feral
    profile) also quotes the form-only attack power ('+N AP in forms')."""
    slot, cls = it.get('slot'), it.get('cls')
    if it.get('thrown'):
        head = ['thrown', '%.1f dps' % it.get('wdps', 0.0)]
    elif slot == 'Off Hand' and cls == 'Shield':
        head = ['shield', '%d armor' % it.get('armor', 0)] + (['%d block' % it['block']] if it.get('block') else [])
    elif slot in ('Main Hand', 'One-Hand', 'Two-Hand', 'Off Hand', 'Ranged'):
        kind = WEAPON_WORD.get(cls, (cls or 'weapon').lower())
        pre = {'Two-Hand': '2H ', 'Main Hand': '1H ', 'One-Hand': '1H ', 'Off Hand': 'off-hand '}.get(slot, '')
        if kind in ('dagger', 'fist weapon', 'staff', 'polearm', 'bow', 'gun', 'crossbow', 'wand'):
            pre = 'off-hand ' if slot == 'Off Hand' else ''
        head = [pre + kind] + (['%.1f dps' % it['wdps']] if it.get('wdps') else [])
    elif slot == 'Relic':
        head = [(cls or 'relic').lower()]
    else:
        word = SLOT_WORD.get(slot, (slot or 'item').lower())
        head = [('%s %s' % (cls.lower(), word)) if cls else word]
    prim = ['+%d %s' % (it[k], lab) for k, lab in PRIMARY if it.get(k) and w.get(k, 0) > 0]
    if feral and it.get('feral_ap') and w.get('ap', 0) > 0:
        prim.append('+%d AP in forms' % it['feral_ap'])
    if it.get('exp') and w.get('exp', 0) > 0:
        prim.append('+%d Exp' % it['exp'])
    tank = []
    if it.get('defense') and w.get('defense', 0) > 0:
        tank.append('Def +%d' % it['defense'])
    if it.get('block') and w.get('block', 0) > 0 and not (slot == 'Off Hand' and cls == 'Shield'):
        tank.append('+%d block value' % it['block'])
    for k, lab in (('blockpct', 'block'), ('dodge', 'dodge'), ('parry', 'parry'), ('hit', 'hit'), ('crit', 'crit')):
        if it.get(k) and w.get(k, 0) > 0:
            tank.append('+%s%% %s' % (_num(it[k]), lab))
    s = ' '.join(head + prim)
    return s + (', ' + ', '.join(tank) if tank else '')


class Profile:
    def __init__(self, name, label, class_word, class_tag, usable, score, weights, secondary, client_usable,
                 slot_suffix, slot_group):
        self.name, self.label, self.class_word, self.class_tag = name, label, class_word, class_tag
        self.usable, self.score, self._weights, self.secondary = usable, score, weights, secondary
        self.client_usable, self.slot_suffix, self.slot_group = client_usable, slot_suffix, slot_group
        self.nothing_text = 'nothing for a %s - vendor' % class_word

    def weights(self, band):
        return self._weights()[band]

    def band_weights(self):
        return self._weights()

    def describe(self, it, band=20):
        if self.name == 'feral':
            return describe(it, self.weights(band)[0], feral=True)
        return describe(it, self.weights(band)[0])


ENH = Profile('enh', '2H Enhancement shaman', 'shaman', 'Shaman', score_items.usable, score_items.score, enh_band_weights,
              '1H (shield set only)', ENH_USABLE,
              {k: ' (shield set)' for k in ('1H axe', '1H mace', 'dagger', 'fist weapon')},
              {'Main Hand': '1H weapon (shield set)', 'One-Hand': '1H weapon (shield set)'})

PROT = Profile('prot', 'Protection warrior (1H + shield)', 'warrior', 'Warrior', prot_weights.usable, prot_weights.score,
               lambda: {b: (prot_weights.CENTRAL, prot_weights.CONSERVATIVE) for b in BANDS},
               prot_weights.SECONDARY, PROT_USABLE,
               {k: ' (pull slot)' for k in ('bow', 'gun', 'crossbow', 'thrown')},
               {'Main Hand': '1H weapon', 'One-Hand': '1H weapon'})

FERAL = Profile('feral', 'Feral druid (bear to 20, cat from 20)', 'druid', 'Druid', feral_weights.usable,
                feral_weights.score, feral_weights.band_weights, feral_weights.SECONDARY, FERAL_USABLE, {},
                {'Main Hand': '1H weapon', 'One-Hand': '1H weapon', 'Two-Hand': '2H weapon'})

PROFILES = {'enh': ENH, 'prot': PROT, 'feral': FERAL}


def get(name):
    if name not in PROFILES:
        raise SystemExit('unknown weights profile %r (known: %s)' % (name, ', '.join(sorted(PROFILES))))
    return PROFILES[name]
