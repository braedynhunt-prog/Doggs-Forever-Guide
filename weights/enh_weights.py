"""
Kill-speed stat-weight model for a levelling 2H Enhancement Dwarf Shaman in WoW Forever.

Everything is a marginal derivative of "mobs killed per hour" in a steady-state grind loop
(fight -> walk/loot -> fight ... -> drink when the pool is empty), normalised so that
1 melee attack power = 1.0.

Inputs and their provenance are listed next to each constant.  Anything tagged UNCERTAIN is
carried as a parameter so the sensitivity pass can flex it.
"""
from __future__ import annotations
import json, math, copy, sys
from dataclasses import dataclass, field

# ---------------------------------------------------------------------------------------
# 1. Base character
# ---------------------------------------------------------------------------------------
# Shaman class base stats (race-neutral) from wowsims/sod core/stats.go: L25/40/60, and the
# vanilla level-1 line (Orc shaman 24/17/23/18/25 minus Orc offsets +3/-3/+2/-3/+3).
# Str Agi Sta Int Spi
CLASS_BASE = {1: (21, 20, 21, 21, 22), 25: (41, 31, 45, 43, 47), 40: (58, 40, 63, 61, 67), 60: (85, 55, 95, 90, 100)}
DWARF_OFFSET = (2, -4, 3, -1, -1)   # wowsims/sod RaceOffsets

def _quad_through(p0, p1, p2):
    (x0, y0), (x1, y1), (x2, y2) = p0, p1, p2
    # Lagrange quadratic
    def f(x):
        return (y0 * (x - x1) * (x - x2) / ((x0 - x1) * (x0 - x2))
                + y1 * (x - x0) * (x - x2) / ((x1 - x0) * (x1 - x2))
                + y2 * (x - x0) * (x - x1) / ((x2 - x0) * (x2 - x1)))
    return f

def base_stats(level: int):
    out = []
    for i in range(5):
        f = _quad_through((1, CLASS_BASE[1][i]), (25, CLASS_BASE[25][i]), (40, CLASS_BASE[40][i]))
        out.append(f(level) + DWARF_OFFSET[i])
    return dict(zip(("str", "agi", "sta", "int", "spi"), out))

# Shaman base mana by level: wowsims/sod gives 505 @25, 975 @40, 1255 @50, 1520 @60.  Level 1 ~ 55
# (vanilla).  Quadratic through 1/25/40.  UNCERTAIN at 10-20 by maybe +-15%.
_mana_f = _quad_through((1, 55), (25, 505), (40, 975))
def base_mana(level):  return max(50.0, _mana_f(level))
# Shaman base health: sod 257 @25, 610 @40, 1280 @60; level 1 ~ 50.
_hp_f = _quad_through((1, 50), (25, 257), (40, 610))
def base_health(level): return max(40.0, _hp_f(level))

# Agility -> melee crit.  8 Nov 2026: Forever client PlayerExpectedStat table (build 1.60.1.70862) via
# foreverdb.net/stats/shaman, verified on the character sheet at L21 (9.6% = 0.46 base + 39 Agi / 9.4 + 5% TS).
# Was vmangos/XPOff/wowsims anchors (4.6 @1, 7.7 @19, 10.3 @25), 10-15% too generous below 25.
_AGI_PER_CRIT = [(1, 6.1), (5, 6.7), (10, 7.3), (15, 8.2), (20, 9.4), (25, 10.3), (30, 11.5), (40, 13.95), (60, 19.7)]
def agi_per_crit(level):
    for (l0, v0), (l1, v1) in zip(_AGI_PER_CRIT, _AGI_PER_CRIT[1:]):
        if l0 <= level <= l1:
            return v0 + (v1 - v0) * (level - l0) / (l1 - l0)
    return 19.7
# Intellect -> spell crit: same client table (Int per 1%: 7.8 @1, 10.4 @10, 14.8 @15, 19.3 @20, 23.7 @25, 28.2 @30,
# 59.2 @60), verified at L21 (9.55% = 2.3 base + 45 Int / 20.0 + 5% TS).
_INT_CRIT = [(1, 1 / 7.8), (10, 1 / 10.4), (15, 1 / 14.8), (20, 1 / 19.3), (25, 1 / 23.7), (30, 1 / 28.2), (60, 1 / 59.2)]
def crit_per_int(level):
    for (l0, v0), (l1, v1) in zip(_INT_CRIT, _INT_CRIT[1:]):
        if l0 <= level <= l1:
            return v0 + (v1 - v0) * (level - l0) / (l1 - l0)
    return 0.0169
# Agility -> dodge: XPOff 0.13%/agi @19; ~20 agi per 1% at 60.  Same shape as crit, close enough.
def dodge_per_agi(level): return 1.0 / agi_per_crit(level)

BASE_MELEE_CRIT = 0.46     # 8 Nov 2026: character sheet at L21 (was 1.7, vmangos / wowsims); server-side, not in the client
BASE_SPELL_CRIT = 2.3      # wowsims/sod
MELEE_AP_BASE = lambda level, strength: 2 * level + 2 * strength - 20   # vmangos StatSystem.cpp (shaman)

# ---------------------------------------------------------------------------------------
# 2. Forever spell numbers (foreverdiff.com client diff, Wowhead Forever tooltips)
# ---------------------------------------------------------------------------------------
# Rockbiter AP: foreverdiff shows the value at the rank's training level (R1 29, R2 58, R3 88, R4 129),
# Wowhead shows the tooltip max (R1 50, R2 79, R3 118, R4 194).  Assumed to grow linearly with level
# inside the rank (vanilla behaviour) -- UNCERTAIN, bounded by the two numbers.
ROCKBITER = [(1, 29, 50), (8, 58, 79), (16, 88, 118), (24, 129, 194), (34, 211, 260)]
def rockbiter_ap(level, frac=None):
    ranks = [r for r in ROCKBITER if r[0] <= level]
    lvl, lo, hi = ranks[-1]
    nxt = [r[0] for r in ROCKBITER if r[0] > lvl]
    span = (nxt[0] - lvl) if nxt else 10
    f = (level - lvl) / span if frac is None else frac
    return lo + (hi - lo) * min(1.0, max(0.0, f))

# Earth Shock (Forever, build 1.60.1.70755 of 3 Nov 2026 raised every rank to about Classic; WCLBox, read 8 Nov):
# R1 L4 21-24 dmg 30 mana, R2 L8 38-41/50, R3 L14 69-74/85, R4 L24 131-140/145.  6 s CD.  In game at L21: R3 71-76
# (a little within-rank level scaling, realPointsPerLevel 0.9).  Beta values were 18/33/49/81.
EARTH_SHOCK = [(4, 22.5, 30, 0.154), (8, 39.5, 50, 0.212), (14, 71.5, 85, 0.299), (24, 135.5, 145, 0.386)]
def earth_shock(level):
    r = [r for r in EARTH_SHOCK if r[0] <= level][-1]
    return dict(dmg=r[1], mana=r[2], coef=r[3])   # coef = vanilla per-rank SP coefficient; Wowhead Forever gives 0.386 at top rank

# Lightning Shield (Forever, WCLBox build 1.60.1.70862, read 8 Nov 2026): per-orb R1 L8 13, R2 L16 24, R3 L24 40,
# R4 L32 64 (Classic 13/29/51/80); mana 45/80/125/180.  3 orbs, SP coef 0.33/orb (UNCERTAIN).
LIGHTNING_SHIELD = [(8, 13, 45), (16, 24, 80), (24, 40, 125), (32, 64, 180)]
def lightning_shield(level):
    r = [r for r in LIGHTNING_SHIELD if r[0] <= level]
    if not r: return dict(dmg=0, mana=0)
    return dict(dmg=r[-1][1], mana=r[-1][2])

# Healing Wave efficiency (HP healed per mana): Forever R3 127-150/80, R4 246-289/155, R5 329-382/200 = 1.73-1.78 (WCLBox, 8 Nov 2026).
HEAL_HP_PER_MANA = 1.75

# Expertise: Forever client = rating, 10 rating per 1% at 60 (wowsims/forever #34).  Below 60 the
# TBC/Wrath rating curve is assumed: rating-per-1% = base60 * (L-8)/52 for 10<=L<=60.  UNCERTAIN.
def expertise_pct_per_rating(level, model="tbc"):
    if model == "tbc":
        return 1.0 / (10.0 * max(2, level - 8) / 52.0)
    if model == "flat60":            # no level scaling at all: 0.1% per rating everywhere
        return 0.1
    if model == "point":             # "+6 expertise" = 6 points at 0.25% each, TBC style
        return 0.25
    raise ValueError(model)

# ---------------------------------------------------------------------------------------
# 3. The scenario
# ---------------------------------------------------------------------------------------
@dataclass
class Scenario:
    level: int
    weapon_dps: float
    weapon_speed: float
    gear: dict = field(default_factory=dict)      # str agi sta int spi ap sp exp hitpct critpct
    talents: dict = field(default_factory=dict)   # ts (0-5), md (0-3), sf (0/1), ew (0-3), ak (0-5, +2% Int per rank)
    mace: bool = False                             # 17 Oct 2026: Dwarf Mace Specialization removed from Forever (Earth Fury);
                                                   # True only in sensitivity.py's "mace spec restored" case
    from_behind: bool = False
    mob_level_delta: int = 0                       # mob level minus player level
    # environment
    walk_seconds: float = 9.0                      # loot + walk between mobs
    mob_hp_per_level: tuple = (1.1, 9.0)           # HP = a*L^2 + b*L  (UNCERTAIN)
    mob_dps_per_level: float = 0.7                 # incoming DPS after armour (UNCERTAIN)
    drink_rate: float = None                       # mana/s from the drink; default by level
    food_hp: float = None                          # HP restored during a drink break by eating in parallel
    shock_coef_scale: float = 1.0                  # multiply the vanilla SP coefficient (Forever unknown)
    ls_coef: float = 0.33
    expertise_model: str = "tbc"
    rockbiter_frac: float = None                   # override within-rank scaling
    heal_fraction_floor: float = 0.0
    policy_shocks: object = "max"                  # "max" = one every 6 s, or an integer n per fight (1 = pull only)
    policy_ls: bool = True                         # keep Lightning Shield up
    spirit_regen_scale: float = 1.0                # 1.0 = Forever as read on the sheet 8 Nov 2026 (1.25 x Spirit per 5 s)

    def drink(self):
        if self.drink_rate is not None: return self.drink_rate
        # Refreshing Spring Water 145/18s (L5), Ice Cold Milk 420/21s (L15), Moonberry 1344/30s (L25)
        if self.level >= 25: return 1344 / 30
        if self.level >= 15: return 420 / 21
        return 145 / 18

    def food(self):
        if self.food_hp is not None: return self.food_hp
        if self.level >= 15: return 234    # Freshly Baked Bread etc (Forever tooltips: 234 over 21 s)
        return 59                          # Tough Jerky 59 over 18 s (level 5 food)


def kills_per_hour(s: Scenario, verbose=False):
    L = s.level
    b = base_stats(L)
    g = {k: s.gear.get(k, 0.0) for k in ("str", "agi", "sta", "int", "spi", "ap", "sp", "exp", "hitpct", "critpct")}
    t = {k: s.talents.get(k, 0) for k in ("ts", "md", "sf", "ew", "ak")}

    Str, Agi, Sta, Int, Spi = (b["str"] + g["str"], b["agi"] + g["agi"], b["sta"] + g["sta"],
                               b["int"] + g["int"], b["spi"] + g["spi"])
    Int *= 1 + 0.02 * t["ak"]      # Ancestral Knowledge, +2% Int per rank (2/5 at 18-19 in the sheet's talent order)

    # --- melee ---
    rb = rockbiter_ap(L, s.rockbiter_frac) * (1 + 0.0667 * t["ew"])
    # 3 Nov 2026: Blizzard dev notes, Mental Dexterity 50/100/150% of Int (was 33/67/100%)
    ap = MELEE_AP_BASE(L, Str) + g["ap"] + rb + Int * (0.5 * t["md"])
    crit = BASE_MELEE_CRIT + Agi / agi_per_crit(L) + t["ts"] + (1.0 if s.mace else 0.0) + g["critpct"]
    crit -= 1.0 * max(0, s.mob_level_delta)   # crit suppression 1%/level (magey)
    d = s.mob_level_delta
    miss = max(0.0, 5.0 + 0.5 * max(0, d) - g["hitpct"])          # 2H vs same level 5%, +0.5%/level to +2
    exp_pct = g["exp"] * expertise_pct_per_rating(L, s.expertise_model)
    dodge = max(0.0, 5.0 + 0.5 * max(0, d) - exp_pct)
    parry = 0.0 if s.from_behind else max(0.0, 5.0 + 0.5 * max(0, d) - exp_pct)
    glance = 10.0 + 10.0 * max(0, d)
    glance_dmg = {0: 0.95, 1: 0.95, 2: 0.85, 3: 0.65}.get(max(0, d), 0.65)
    crit = max(0.0, min(crit, 100 - miss - dodge - parry - glance))
    p_hit = (100 - miss - dodge - parry - glance - crit) / 100
    mult = p_hit + (crit / 100) * 2.0 + (glance / 100) * glance_dmg
    white_dps = (s.weapon_dps + ap / 14.0) * mult

    # --- spells ---
    es = earth_shock(L)
    spell_crit = BASE_SPELL_CRIT + Int * crit_per_int(L) + t["ts"] + (1.0 if s.mace else 0.0)
    spell_hit = 0.97 - 0.01 * max(0, d)
    es_dmg = (es["dmg"] + g["sp"] * es["coef"] * s.shock_coef_scale) * (1 + 0.5 * spell_crit / 100) * spell_hit
    es_cost = es["mana"] * (0.55 if t["sf"] else 1.0)
    ls = lightning_shield(L)
    ls_on = s.policy_ls and ls["dmg"] > 0
    ls_dmg_per_fight = (3 * (ls["dmg"] + g["sp"] * s.ls_coef) * (1 + 0.5 * spell_crit / 100)) if ls_on else 0.0
    ls_cost = (ls["mana"] * (0.55 if t["sf"] else 1.0)) if ls_on else 0.0

    # --- fight ---
    a, bcoef = s.mob_hp_per_level
    mob_hp = a * L ** 2 + bcoef * L
    # shocks: one on pull, then every 6 s -> continuous approximation (T+6)/6, self-consistent solve
    T = mob_hp / (white_dps + es_dmg / 6.0 + 1e-9)
    for _ in range(30):
        shocks = (T + 6.0) / 6.0 if s.policy_shocks == "max" else float(s.policy_shocks)
        if s.policy_shocks != "max":
            shocks = min(shocks, (T + 6.0) / 6.0)
        dmg_fight = white_dps * T + shocks * es_dmg + ls_dmg_per_fight
        T = T * mob_hp / dmg_fight
    shocks = (T + 6.0) / 6.0 if s.policy_shocks == "max" else min(float(s.policy_shocks), (T + 6.0) / 6.0)

    # --- mana / health economy ---
    mana_fight = shocks * es_cost + ls_cost                 # LS recast every fight (3 orbs used)
    pool = base_mana(L) + 20 + max(0.0, Int - 20) * 15.0
    # 8 Nov 2026, character sheet at L21: 51 mana per 5 s at 41 Spirit, unchanged when Int went 45 -> 42, no Spirit gear
    # to vary.  Fits 1.25 x Spirit per 5 s = 0.25 mana/s per Spirit with no base term (vanilla 17 + Spi/5 per tick would
    # have read 63).  A level term cannot be excluded from one level; re-read at the same Spirit a few levels on.
    spirit_regen = 0.25 * Spi * s.spirit_regen_scale   # mana per second outside the 5-s rule
    regen_walk = spirit_regen * max(0.0, s.walk_seconds - 5.0)   # last shock lands mid-fight; be conservative
    hp = base_health(L) + 20 + max(0.0, Sta - 20) * 10.0
    dodge_me = min(30.0, Agi * dodge_per_agi(L)) / 100
    incoming = s.mob_dps_per_level * L * (1 - dodge_me) * T
    hp_regen_walk = (0.11 * Spi + 7) / 2.0 * s.walk_seconds

    # Steady-state grind: every fight's net HP loss is eventually healed with mana (Healing Wave, ~1.8 HP per
    # mana), every point of mana spent is eventually drunk back at (drink + Spirit) mana/s.  Pool size and
    # max HP therefore do not enter the steady state at all -- only regen, mana efficiency and damage do.
    # (Food is ignored: it is only free while you are drinking anyway, and modelling that couples pool size
    # to meal frequency, a second-order effect that swamped the numbers in an earlier version.)
    loss = max(0.0, incoming - hp_regen_walk)              # HP lost per fight net of walking regen
    heal_mana = loss / HEAL_HP_PER_MANA                    # mana per fight to heal it back
    net_mana = mana_fight + heal_mana - regen_walk         # per fight, >0 means the pool drains
    heal_mana_cycle = heal_mana
    avail = pool - es_cost * 1.5
    k = avail / net_mana if net_mana > 0 else 1e9          # fights per drink (reported only)
    drink_per_fight = max(0.0, net_mana) / (s.drink() + spirit_regen)
    drink_time = drink_per_fight * min(k, 1e6)
    cycle = min(k, 1e6) * (T + s.walk_seconds + drink_per_fight)
    kph = 3600 / (T + s.walk_seconds + drink_per_fight)
    buffer = 0.65 * hp
    if verbose:
        return dict(kph=kph, T=T, white_dps=white_dps, ap=ap, crit=crit, es_dmg=es_dmg, shocks=shocks,
                    mana_fight=mana_fight, pool=pool, k=k, spirit_regen=spirit_regen, mob_hp=mob_hp,
                    hp=hp, incoming=incoming, heal_mana_cycle=heal_mana_cycle, mult=mult,
                    Str=Str, Agi=Agi, Sta=Sta, Int=Int, Spi=Spi, rockbiter=rb, spell_crit=spell_crit,
                    drink_time=drink_time, loss=loss, buffer=buffer,
                    cycle_fight_share=(k * (T + s.walk_seconds)) / cycle)
    return kph


STATS = ["ap", "str", "agi", "int", "spi", "sta", "sp", "exp", "hitpct", "critpct"]

def best_policy(s: Scenario):
    """Pick the shock count / Lightning Shield usage that maximises kills per hour."""
    best = None
    for n in ["max", 3, 2, 1]:
        for ls in (True, False):
            s2 = copy.deepcopy(s); s2.policy_shocks = n; s2.policy_ls = ls
            k = kills_per_hour(s2)
            if best is None or k > best[0] + 1e-9:
                best = (k, n, ls)
    return best

def weights(s: Scenario, h=2.0, optimise_policy=True):
    """Marginal kills/hour per point of each stat, normalised to AP = 1."""
    if optimise_policy:
        _, n, ls = best_policy(s)
        s = copy.deepcopy(s); s.policy_shocks = n; s.policy_ls = ls
    base = kills_per_hour(s)
    out = {}
    for st in STATS:
        s2 = copy.deepcopy(s); s2.gear[st] = s2.gear.get(st, 0.0) + h
        out[st] = (kills_per_hour(s2) - base) / h
    # weapon dps
    s2 = copy.deepcopy(s); s2.weapon_dps += 0.5
    out["wdps"] = (kills_per_hour(s2) - base) / 0.5
    # mace spec bonus: 0 since 17 Oct 2026 (Dwarf Mace Specialization removed); only computed when a scenario
    # restores the spec (sensitivity.py "mace spec restored")
    if s.mace:
        s2 = copy.deepcopy(s); s2.mace = False
        out["mace_bonus"] = base - kills_per_hour(s2)
    else:
        out["mace_bonus"] = 0.0
    ap = out["ap"]
    res = {k: v / ap for k, v in out.items()}
    res["_policy"] = (s.policy_shocks, s.policy_ls)
    return res, base


# ---------------------------------------------------------------------------------------
# 4. Bands
# ---------------------------------------------------------------------------------------
def band_scenarios():
    return {
        10: Scenario(level=10, weapon_dps=8.33, weapon_speed=2.7,
                     gear=dict(str=1, spi=1),                                   # Coldridge Hammer, rest statless
                     talents=dict(md=1)),                                        # first point: Mental Dexterity
        15: Scenario(level=15, weapon_dps=11.21, weapon_speed=3.3,
                     gear=dict(str=3, agi=2, sta=8, int=2),                      # Mountaineer's Greataxe, Bingles' gloves, Robe of the Keeper
                     talents=dict(md=3, ts=3)),
        20: Scenario(level=20, weapon_dps=19.71, weapon_speed=3.5,
                     gear=dict(str=26, agi=24, sta=14, int=6, spi=16, ap=18),    # Smite's Hammer + the Deadmines/HoT set in the guide
                     talents=dict(md=3, ts=5, sf=1, ak=2)),
        # 1 Nov 2026: bands 25 and 30 added for the 23-31 chapters (Blackfathom, Stockade, Gnomeregan, Razorfen Kraul).
        # Gear sums from weights/tooltips/2026-11-01.json. Flurry (21-25) is not modelled (no haste term); the 30 band
        # adds Elemental Weapons 3/3 (26-28).
        25: Scenario(level=25, weapon_dps=19.71, weapon_speed=3.5,
                     gear=dict(str=25, agi=22, sta=10, int=8, spi=15, ap=18, sp=5),  # Smite's, Defias Armor/Belt, Gold-flecked, Deepgrave,
                     talents=dict(md=3, ts=5, sf=1, ak=2)),                           # Loch Walkers, Bravo's, Spiritwraith, both rings, Choker
        30: Scenario(level=30, weapon_dps=22.88, weapon_speed=3.3,
                     gear=dict(str=26, agi=12, sta=30, int=8, spi=19, ap=18, sp=25),  # Twilight Maul, Defender's Helm, Naga Gloves, Bands of
                     talents=dict(md=3, ts=5, sf=1, ew=3, ak=2)),                     # Serra'kis, Thresher Cape + the rest of the 25 set
    }

if __name__ == "__main__":
    for lvl, sc in band_scenarios().items():
        for pol in ("max", "best"):
            if pol == "max":
                w, kph = weights(sc, optimise_policy=False)
                v = kills_per_hour(sc, verbose=True)
                print(f"\n=== Level {lvl} === policy: shock every 6 s + Lightning Shield")
            else:
                w, kph = weights(sc, optimise_policy=True)
                s3 = copy.deepcopy(sc); s3.policy_shocks, s3.policy_ls = w["_policy"]
                v = kills_per_hour(s3, verbose=True)
                print(f"--- Level {lvl} --- policy: kill-speed optimum = shocks/fight {w['_policy'][0]}, Lightning Shield {w['_policy'][1]}")
            print(f"   kills/h {kph:.0f}  fight {v['T']:.1f}s  white dps {v['white_dps']:.1f}  AP {v['ap']:.0f} "
              f"(Rockbiter {v['rockbiter']:.0f})  crit {v['crit']:.1f}%  ES {v['es_dmg']:.0f} x{v['shocks']:.1f}/fight  "
              f"pool {v['pool']:.0f}  fights/drink {v['k']:.1f}  fight-share {v['cycle_fight_share']:.2f}  heal mana/cycle {v['heal_mana_cycle']:.0f}")
            print("   naked+gear: Str %.0f Agi %.0f Sta %.0f Int %.0f Spi %.0f" % (v['Str'], v['Agi'], v['Sta'], v['Int'], v['Spi']))
            print("   " + "  ".join(f"{k}={w[k]:.2f}" for k in ["wdps", "str", "ap", "int", "agi", "spi", "sta", "sp", "exp", "hitpct", "critpct", "mace_bonus"]))
    sys.exit(0)
    for lvl, sc in band_scenarios().items():
        w, kph = weights(sc)
        v = kills_per_hour(sc, verbose=True)
        print(f"\n=== Level {lvl} ===  kills/h {kph:.0f}  fight {v['T']:.1f}s  white dps {v['white_dps']:.1f}  AP {v['ap']:.0f} "
              f"(Rockbiter {v['rockbiter']:.0f})  crit {v['crit']:.1f}%  ES {v['es_dmg']:.0f} x{v['shocks']:.1f}/fight  "
              f"pool {v['pool']:.0f}  fights/drink {v['k']:.1f}  fight-share {v['cycle_fight_share']:.2f}  heal mana/cycle {v['heal_mana_cycle']:.0f}")
        print("   naked+gear: Str %.0f Agi %.0f Sta %.0f Int %.0f Spi %.0f" % (v['Str'], v['Agi'], v['Sta'], v['Int'], v['Spi']))
        print("   " + "  ".join(f"{k}={w[k]:.2f}" for k in ["wdps", "str", "ap", "int", "agi", "spi", "sta", "sp", "exp", "hitpct", "critpct", "mace_bonus"]))
