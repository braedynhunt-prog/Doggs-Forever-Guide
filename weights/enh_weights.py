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
# 11 Nov 2026: replaced by the client's per-level table (foreverdb.net/stats/shaman, PlayerExpectedStat, build
# 1.60.1.70888; the quadratic read 180 / 272 / 381 / 646 at 10 / 15 / 20 / 30 against 175 / 260 / 370 / 665). Base mana
# enters the printed pool and fights-per-drink, and Stormstrike's cost (8% of base mana); kills/hour without Stormstrike
# do not depend on it.
_BASE_MANA = [55, 61, 68, 91, 100, 110, 121, 133, 161, 175, 190, 206, 223, 241, 260, 280, 301, 323, 346, 370,
              395, 421, 448, 476, 505, 535, 566, 598, 631, 665, 699, 733, 767, 786, 820, 854, 888, 922, 941, 975,
              1009, 1028, 1062, 1096, 1115, 1149, 1183, 1202, 1236, 1255, 1289, 1323, 1342, 1376, 1395, 1414, 1448, 1467, 1501, 1520]
def base_mana(level):  return float(_BASE_MANA[max(1, min(60, int(level))) - 1])
# Shaman base health: sod 257 @25, 610 @40, 1280 @60; level 1 ~ 50.
_hp_f = _quad_through((1, 50), (25, 257), (40, 610))
def base_health(level): return max(40.0, _hp_f(level))

# Agility -> melee crit.  8 Nov 2026: Forever client PlayerExpectedStat table (build 1.60.1.70862) via
# foreverdb.net/stats/shaman, verified on the character sheet at L21 (9.6% = 0.46 base + 39 Agi / 9.4 + 5% TS).
# Was vmangos/XPOff/wowsims anchors (4.6 @1, 7.7 @19, 10.3 @25), 10-15% too generous below 25.
# 11 Nov 2026: re-read at build 1.60.1.70888 (rows unchanged); 35 and 40 added for the level-40 band (40 was 13.95).
_AGI_PER_CRIT = [(1, 6.1), (5, 6.7), (10, 7.3), (15, 8.2), (20, 9.4), (25, 10.3), (30, 11.5), (35, 12.7), (40, 13.9), (60, 19.7)]
def agi_per_crit(level):
    for (l0, v0), (l1, v1) in zip(_AGI_PER_CRIT, _AGI_PER_CRIT[1:]):
        if l0 <= level <= l1:
            return v0 + (v1 - v0) * (level - l0) / (l1 - l0)
    return 19.7
# Intellect -> spell crit: same client table (Int per 1%: 7.8 @1, 10.4 @10, 14.8 @15, 19.3 @20, 23.7 @25, 28.2 @30,
# 59.2 @60), verified at L21 (9.55% = 2.3 base + 45 Int / 20.0 + 5% TS).
# 11 Nov 2026: 35 (33.0) and 40 (38.2) added; the 30-60 interpolation gave 34.2 at 40.
_INT_CRIT = [(1, 1 / 7.8), (10, 1 / 10.4), (15, 1 / 14.8), (20, 1 / 19.3), (25, 1 / 23.7), (30, 1 / 28.2), (35, 1 / 33.0),
             (40, 1 / 38.2), (60, 1 / 59.2)]
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
# 11 Nov 2026: Wowhead Forever spell pages give the passive aura each rank applies (15568: 88, 15569: 129, 16311: 211 AP)
# = the floor column, and the cast tooltips are rendered for a level-60 viewer (118 / 194 / 355) = the max column. So the
# AP does scale with level; how fast inside a rank is still the convention below. The level-34 rank was (211, 260): the
# 260 was a guess, the tooltip says 355.
ROCKBITER = [(1, 29, 50), (8, 58, 79), (16, 88, 118), (24, 129, 194), (34, 211, 355)]
def rockbiter_ap(level, frac=None):
    ranks = [r for r in ROCKBITER if r[0] <= level]
    lvl, lo, hi = ranks[-1]
    nxt = [r[0] for r in ROCKBITER if r[0] > lvl]
    span = (nxt[0] - lvl) if nxt else 10
    f = (level - lvl) / span if frac is None else frac
    return lo + (hi - lo) * min(1.0, max(0.0, f))

# Windfury Weapon (11 Nov 2026): each landed hit has a 20% chance of 2 extra attacks with +N melee AP. Passive auras 8233
# (R1, level 30) +46 AP and 8236 (R2, level 40) +119 AP; cast tooltips 8232 / 8235 at a level-60 viewer +104 / +221. Same
# floor/max reading and within-rank convention as Rockbiter. Elemental Weapons adds 13/27/40% to this AP (WCLBox, build
# 1.60.1.70888). R3 (50) max 315, R4 (60) max 433: floors not read yet.
WINDFURY = [(30, 46, 104), (40, 119, 221)]
WINDFURY_PROC = 0.20
def windfury_ap(level, frac=None):
    ranks = [r for r in WINDFURY if r[0] <= level]
    if not ranks: return 0.0
    lvl, lo, hi = ranks[-1]
    nxt = [r[0] for r in WINDFURY if r[0] > lvl]
    span = (nxt[0] - lvl) if nxt else 10
    f = (level - lvl) / span if frac is None else frac
    return lo + (hi - lo) * min(1.0, max(0.0, f))

# Earth Shock (Forever, build 1.60.1.70755 of 3 Nov 2026 raised every rank to about Classic; WCLBox, read 8 Nov):
# R1 L4 21-24 dmg 30 mana, R2 L8 38-41/50, R3 L14 69-74/85, R4 L24 131-140/145.  6 s CD.  In game at L21: R3 71-76
# (a little within-rank level scaling, realPointsPerLevel 0.9).  Beta values were 18/33/49/81.
# 11 Nov 2026: R5 L36 241-256/240 (Wowhead Forever spell 10412: SP mod 0.386), R6 L48 380-402/345 (nether tooltips).
EARTH_SHOCK = [(4, 22.5, 30, 0.154), (8, 39.5, 50, 0.212), (14, 71.5, 85, 0.299), (24, 135.5, 145, 0.386),
               (36, 248.5, 240, 0.386), (48, 391.0, 345, 0.386)]
def earth_shock(level):
    r = [r for r in EARTH_SHOCK if r[0] <= level][-1]
    return dict(dmg=r[1], mana=r[2], coef=r[3])   # coef = vanilla per-rank SP coefficient; Wowhead Forever gives 0.386 at top rank

# Lightning Shield (Forever, WCLBox build 1.60.1.70862, read 8 Nov 2026): per-orb R1 L8 13, R2 L16 24, R3 L24 40,
# R4 L32 64 (Classic 13/29/51/80); mana 45/80/125/180.  3 orbs, SP coef 0.33/orb (UNCERTAIN).
# 11 Nov 2026: R5 L40 96/240, R6 L48 134/305 (nether tooltips 8134, 10431).
LIGHTNING_SHIELD = [(8, 13, 45), (16, 24, 80), (24, 40, 125), (32, 64, 180), (40, 96, 240), (48, 134, 305)]
def lightning_shield(level):
    r = [r for r in LIGHTNING_SHIELD if r[0] <= level]
    if not r: return dict(dmg=0, mana=0)
    return dict(dmg=r[-1][1], mana=r[-1][2])

# Healing Wave efficiency (HP healed per mana): Forever R3 127-150/80, R4 246-289/155, R5 329-382/200 = 1.73-1.78 (WCLBox, 8 Nov 2026).
HEAL_HP_PER_MANA = 1.75
# 11 Nov 2026: R6 L32 465-536/265 = 1.89, R7 L40 656-753/340 = 2.07, R8 L48 929-1062/440 = 2.26 (WCLBox, build 70888).
def heal_hp_per_mana(level):
    if level >= 48: return 2.26
    if level >= 40: return 2.07
    if level >= 32: return 1.89
    return HEAL_HP_PER_MANA

# Talents added 11 Nov 2026 (WCLBox talent page, build 1.60.1.70888; Wowhead Forever spell pages):
#   ss     Stormstrike (tier 4, 15 points): 150% normalized weapon damage (2H: AP x 3.3 / 14), 6 s cooldown, 8% of base
#          mana, +20% on the next Earth Shock
#   iss    Improved Stormstrike 0-2: 50 / 100% chance per Stormstrike of 50% mana regeneration while casting for 15 s
#          (spell 1223031: base value 20, rank curve 50 / 100); the dodge/parry cooldown reset is not modelled
#   flurry 0-5: +6% attack speed per rank for the 3 swings after a melee crit
#   ant    Anticipation 0-3: +2% dodge per rank
#   tf     Tidal Focus 0-5 (Restoration): +1% hit and -1% healing-spell mana per rank (hit applied to melee only)
#   mind   Mindfulness 0-3 (Restoration): 17 / 33 / 50% mana regeneration while casting
#   ils    Improved Lightning Shield 0-3: +5% Lightning Shield damage per rank
#   mq     Mental Quickness 0-2: spell damage +15% of Intellect per rank
TALENT_KEYS = ("ts", "md", "sf", "ew", "ak", "ss", "iss", "flurry", "ant", "tf", "mind", "ils", "mq")
ISS_CHANCE = {0: 0.0, 1: 0.5, 2: 1.0}
MINDFULNESS = {0: 0.0, 1: 0.17, 2: 0.33, 3: 0.50}
FLURRY_PER_RANK = 0.06
SS_COOLDOWN = 6.0
SS_NORMALIZED_SPEED = 3.3

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
                                                   # + ss, iss, flurry, ant, tf, mind, ils, mq: see TALENT_KEYS
    imbue: str = "rockbiter"                       # "rockbiter" | "windfury" (11 Nov 2026)
    ss_item_bonus: float = 0.0                     # Rage of the Storm: 0.10 (Equip: +10% Stormstrike damage)
    iss_chance: float = None                       # override Improved Stormstrike's chance per rank (tooltip base reads 20%)
    regen_stack: bool = False                      # True: Improved Stormstrike and Mindfulness casting regen add up (cap 100%)
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
    rockbiter_frac: float = None                   # override within-rank scaling (Rockbiter and Windfury AP alike)
    heal_fraction_floor: float = 0.0
    policy_shocks: object = "max"                  # "max" = one every 6 s, or an integer n per fight (1 = pull only)
    policy_ls: bool = True                         # keep Lightning Shield up
    spirit_regen_scale: float = 1.0                # 1.0 = Forever as read on the sheet 8 Nov 2026 (1.25 x Spirit per 5 s)

    def drink(self):
        if self.drink_rate is not None: return self.drink_rate
        # Refreshing Spring Water 145/18s (L5), Ice Cold Milk 420/21s (L15). 11 Nov 2026 (Forever tooltips): Sweet Nectar
        # 1345/27s (L25; was "Moonberry 1344/30s"), Moonberry Juice 1915/30s (L35), Morning Glory Dew 2821/30s (L45).
        if self.level >= 45: return 2821 / 30
        if self.level >= 35: return 1915 / 30
        if self.level >= 25: return 1345 / 27
        if self.level >= 15: return 420 / 21
        return 145 / 18

    def food(self):
        if self.food_hp is not None: return self.food_hp
        if self.level >= 45: return 2065   # Homemade Cherry Pie (Forever tooltip, 11 Nov 2026)
        if self.level >= 35: return 1338   # Cured Ham Steak / Fine Aged Cheddar (Forever: requires 35)
        if self.level >= 15: return 234    # Freshly Baked Bread etc (Forever tooltips: 234 over 21 s)
        return 59                          # Tough Jerky 59 over 18 s (level 5 food)


def kills_per_hour(s: Scenario, verbose=False):
    L = s.level
    b = base_stats(L)
    g = {k: s.gear.get(k, 0.0) for k in ("str", "agi", "sta", "int", "spi", "ap", "sp", "exp", "hitpct", "critpct")}
    t = {k: s.talents.get(k, 0) for k in TALENT_KEYS}

    Str, Agi, Sta, Int, Spi = (b["str"] + g["str"], b["agi"] + g["agi"], b["sta"] + g["sta"],
                               b["int"] + g["int"], b["spi"] + g["spi"])
    Int *= 1 + 0.02 * t["ak"]      # Ancestral Knowledge, +2% Int per rank (2/5 at 18-19 in the sheet's talent order)

    # --- melee ---
    wf = s.imbue == "windfury"
    rb = 0.0 if wf else rockbiter_ap(L, s.rockbiter_frac) * (1 + 0.0667 * t["ew"])
    # 3 Nov 2026: Blizzard dev notes, Mental Dexterity 50/100/150% of Int (was 33/67/100%)
    ap = MELEE_AP_BASE(L, Str) + g["ap"] + rb + Int * (0.5 * t["md"])
    crit = BASE_MELEE_CRIT + Agi / agi_per_crit(L) + t["ts"] + (1.0 if s.mace else 0.0) + g["critpct"]
    crit -= 1.0 * max(0, s.mob_level_delta)   # crit suppression 1%/level (magey)
    d = s.mob_level_delta
    miss = max(0.0, 5.0 + 0.5 * max(0, d) - g["hitpct"] - t["tf"])   # 2H vs same level 5%, +0.5%/level to +2; Tidal Focus
    exp_pct = g["exp"] * expertise_pct_per_rating(L, s.expertise_model)
    dodge = max(0.0, 5.0 + 0.5 * max(0, d) - exp_pct)
    parry = 0.0 if s.from_behind else max(0.0, 5.0 + 0.5 * max(0, d) - exp_pct)
    glance = 10.0 + 10.0 * max(0, d)
    glance_dmg = {0: 0.95, 1: 0.95, 2: 0.85, 3: 0.65}.get(max(0, d), 0.65)
    crit = max(0.0, min(crit, 100 - miss - dodge - parry - glance))
    p_hit = (100 - miss - dodge - parry - glance - crit) / 100
    mult = p_hit + (crit / 100) * 2.0 + (glance / 100) * glance_dmg
    white_dps = (s.weapon_dps + ap / 14.0) * mult
    # 11 Nov 2026. Flurry: a swing is hasted when any of the previous 3 swings crit. Windfury: expected extra damage per
    # landed hit = 20% x 2 attacks, each a white swing with the rank's AP added; the extra attacks do not proc again.
    haste = 1.0 + FLURRY_PER_RANK * t["flurry"] * (1 - (1 - crit / 100) ** 3)
    white_dps = white_dps * haste
    p_land = (100 - miss - dodge - parry) / 100
    swing = s.weapon_dps * s.weapon_speed + ap * s.weapon_speed / 14.0
    wf_extra = wf_dps = wf_ap = 0.0
    if wf:
        wf_ap = windfury_ap(L, s.rockbiter_frac) * (1 + 0.1333 * t["ew"])
        wf_extra = WINDFURY_PROC * 2 * (swing + wf_ap * s.weapon_speed / 14.0) * mult
        wf_dps = haste / s.weapon_speed * p_land * wf_extra
    white_dps = white_dps + wf_dps
    # Stormstrike: yellow strike (no glancing), can proc Windfury.
    ss_dmg = ss_cost = 0.0
    if t["ss"]:
        y_mult = (100 - miss - dodge - parry + crit) / 100
        ss_dmg = (1.5 * (s.weapon_dps * s.weapon_speed + ap * SS_NORMALIZED_SPEED / 14.0) * (1 + s.ss_item_bonus) * y_mult
                  + p_land * wf_extra)
        ss_cost = 0.08 * base_mana(L)

    # --- spells ---
    es = earth_shock(L)
    spell_crit = BASE_SPELL_CRIT + Int * crit_per_int(L) + t["ts"] + (1.0 if s.mace else 0.0)
    spell_hit = 0.97 - 0.01 * max(0, d)
    sp = g["sp"] + 0.15 * t["mq"] * Int          # Mental Quickness
    es_dmg = (es["dmg"] + sp * es["coef"] * s.shock_coef_scale) * (1 + 0.5 * spell_crit / 100) * spell_hit
    es_cost = es["mana"] * (0.55 if t["sf"] else 1.0)
    ls = lightning_shield(L)
    ls_on = s.policy_ls and ls["dmg"] > 0
    ls_dmg_per_fight = (3 * (ls["dmg"] + sp * s.ls_coef) * (1 + 0.5 * spell_crit / 100) * (1 + 0.05 * t["ils"])) if ls_on else 0.0
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
        # Stormstrike: one in the first cooldown window, then one per 6 s (mean of floor(T/6) + 1 = T/6 + 0.5); every
        # shock after the pull shock lands inside a Stormstrike debuff (+20%).
        n_ss = (T / SS_COOLDOWN + 0.5) if t["ss"] else 0.0
        ss_shock = (0.2 * es_dmg * max(0.0, shocks - 1.0)) if t["ss"] else 0.0
        dmg_fight = white_dps * T + shocks * es_dmg + ls_dmg_per_fight + n_ss * ss_dmg + ss_shock
        T = T * mob_hp / dmg_fight
    shocks = (T + 6.0) / 6.0 if s.policy_shocks == "max" else min(float(s.policy_shocks), (T + 6.0) / 6.0)
    n_ss = (T / SS_COOLDOWN + 0.5) if t["ss"] else 0.0

    # --- mana / health economy ---
    mana_fight = shocks * es_cost + ls_cost + n_ss * ss_cost   # LS recast every fight (3 orbs used)
    pool = base_mana(L) + 20 + max(0.0, Int - 20) * 15.0
    # 8 Nov 2026, character sheet at L21: 51 mana per 5 s at 41 Spirit, unchanged when Int went 45 -> 42, no Spirit gear
    # to vary.  Fits 1.25 x Spirit per 5 s = 0.25 mana/s per Spirit with no base term (vanilla 17 + Spi/5 per tick would
    # have read 63).  A level term cannot be excluded from one level; re-read at the same Spirit a few levels on.
    spirit_regen = 0.25 * Spi * s.spirit_regen_scale   # mana per second outside the 5-s rule
    regen_walk = spirit_regen * max(0.0, s.walk_seconds - 5.0)   # last shock lands mid-fight; be conservative
    # 11 Nov 2026: regeneration while casting (the fight plus the 5-second tail). Improved Stormstrike's 15 s buff sees
    # about 2.5 Stormstrikes, so its uptime is 1 - (1 - chance)^2.5; Mindfulness is permanent. Central case: they do not
    # stack (the larger wins); regen_stack adds them.
    iss_ch = (ISS_CHANCE[t["iss"]] if s.iss_chance is None else (s.iss_chance if t["iss"] else 0.0)) if t["ss"] else 0.0
    cast_a, cast_b = 0.5 * (1 - (1 - iss_ch) ** 2.5), MINDFULNESS[t["mind"]]
    cast_regen = min(1.0, cast_a + cast_b) if s.regen_stack else max(cast_a, cast_b)
    regen_fight = spirit_regen * cast_regen * (T + min(5.0, s.walk_seconds))
    hp = base_health(L) + 20 + max(0.0, Sta - 20) * 10.0
    dodge_me = min(30.0, Agi * dodge_per_agi(L) + 2.0 * t["ant"]) / 100   # Anticipation
    incoming = s.mob_dps_per_level * L * (1 - dodge_me) * T
    hp_regen_walk = (0.11 * Spi + 7) / 2.0 * s.walk_seconds

    # Steady-state grind: every fight's net HP loss is eventually healed with mana (Healing Wave, ~1.8 HP per
    # mana), every point of mana spent is eventually drunk back at (drink + Spirit) mana/s.  Pool size and
    # max HP therefore do not enter the steady state at all -- only regen, mana efficiency and damage do.
    # (Food is ignored: it is only free while you are drinking anyway, and modelling that couples pool size
    # to meal frequency, a second-order effect that swamped the numbers in an earlier version.)
    loss = max(0.0, incoming - hp_regen_walk)              # HP lost per fight net of walking regen
    heal_mana = loss / heal_hp_per_mana(L) * (1 - 0.01 * t["tf"])   # mana per fight to heal it back (Tidal Focus)
    net_mana = mana_fight + heal_mana - regen_walk - regen_fight   # per fight, >0 means the pool drains
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
                    drink_time=drink_time, loss=loss, buffer=buffer, imbue=s.imbue, haste=haste, wf_dps=wf_dps, wf_ap=wf_ap,
                    n_ss=n_ss, ss_dmg=ss_dmg, regen_fight=regen_fight, net_mana=net_mana, miss=miss,
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
# 11 Nov 2026: the talents of Braedyn's levelling sheet at each band (docs/forever-shaman-leveling-sheet.html; legal on
# Forever's tree per wowsims/forever shaman.json and WCLBox): 10-14 Thundering Strikes, 15-17 Mental Dexterity, 18-19
# Ancestral Knowledge 2, 20 Shamanistic Focus, 21-23 Elemental Weapons, 24 Anticipation 1, 25 Stormstrike, 26-27 Improved
# Ghost Wolf, 28-29 Flurry 2, 30-31 Improved Stormstrike, 32 Spirit Weapons, 33-37 Tidal Focus, 38-40 Mindfulness.
# Improved Ghost Wolf and Spirit Weapons have no term in the model.
SHEET_TALENTS = {
    25: dict(md=3, ts=5, sf=1, ak=2, ew=3, ant=1, ss=1),
    30: dict(md=3, ts=5, sf=1, ak=2, ew=3, ant=1, ss=1, flurry=2, iss=1),
    40: dict(md=3, ts=5, sf=1, ak=2, ew=3, ant=1, ss=1, flurry=2, iss=2, tf=5, mind=3),
}
# Level-40 gear from the 30-60 route plan's picks (weights/tooltips/2026-11-11.json): Wild Headdress, Prisoner Handwraps,
# Apprentice Sorcerer's Slacks, Doomsayer's Robe, Wingborne Boots, Coldwater Ring, Arathi Armbands, Violet Sash, Chainlink
# Towel, Explorers' League Commendation. No shoulders or second ring (the plan names none).
GEAR_40 = dict(str=7, agi=5, sta=20, int=35, spi=85, sp=53)
# Live tooltips 11 Nov 2026. Rage of the Storm 280604: 102-154, speed 3.60, +16 Str +15 Sta, Equip +10% Stormstrike damage
# (the 28 Oct reading was 3.20 speed, +15 Sta +12 Int). Bonebiter 6830: 105-159, speed 3.40, +20 Str +10 Sta.
WEAPONS_40 = {
    "Rage of the Storm": dict(weapon_dps=35.56, weapon_speed=3.6, gear=dict(str=16, sta=15), ss_item_bonus=0.10),
    "Bonebiter": dict(weapon_dps=38.82, weapon_speed=3.4, gear=dict(str=20, sta=10), ss_item_bonus=0.0),
}

def scenario_40(weapon="Rage of the Storm", imbue="rockbiter", talents=None):
    w = WEAPONS_40[weapon]
    gear = dict(GEAR_40)
    for k, v in w["gear"].items():
        gear[k] = gear.get(k, 0) + v
    return Scenario(level=40, weapon_dps=w["weapon_dps"], weapon_speed=w["weapon_speed"], gear=gear,
                    talents=dict(SHEET_TALENTS[40] if talents is None else talents), imbue=imbue,
                    ss_item_bonus=w["ss_item_bonus"])

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
        # Gear sums from weights/tooltips/2026-11-01.json. 11 Nov 2026: talents now the sheet's (25: Elemental Weapons 3,
        # Anticipation 1, Stormstrike; 30: + Flurry 2, Improved Stormstrike 1); they were md 3 ts 5 sf 1 ak 2 (+ ew 3 at 30).
        25: Scenario(level=25, weapon_dps=19.71, weapon_speed=3.5,
                     gear=dict(str=25, agi=22, sta=10, int=8, spi=15, ap=18, sp=5),  # Smite's, Defias Armor/Belt, Gold-flecked, Deepgrave,
                     talents=dict(SHEET_TALENTS[25])),                                # Loch Walkers, Bravo's, Spiritwraith, both rings, Choker
        30: Scenario(level=30, weapon_dps=22.88, weapon_speed=3.3,
                     gear=dict(str=26, agi=12, sta=30, int=8, spi=19, ap=18, sp=25),  # Twilight Maul, Defender's Helm, Naga Gloves, Bands of
                     talents=dict(SHEET_TALENTS[30])),                                # Serra'kis, Thresher Cape + the rest of the 25 set
        # 11 Nov 2026: level 40, Rage of the Storm + Rockbiter (the model's pick, see the tables this file prints).
        40: scenario_40(),
    }

def with_imbue(sc, imbue, frac=None):
    s2 = copy.deepcopy(sc); s2.imbue = imbue; s2.rockbiter_frac = frac
    return s2

def optimum(sc):
    """(kills/hour, verbose dict) at the kill-speed optimum policy."""
    k, n, ls = best_policy(sc)
    s2 = copy.deepcopy(sc); s2.policy_shocks, s2.policy_ls = n, ls
    return k, kills_per_hour(s2, verbose=True)

def compare_row(label, sc):
    k, v = optimum(sc)
    return (f"   {label:46s} kills/h {k:6.1f}  fight {v['T']:4.1f}s  white {v['white_dps']:5.1f} (Windfury {v['wf_dps']:4.1f})  "
            f"AP {v['ap']:4.0f}  Stormstrike {v['ss_dmg']:3.0f} x{v['n_ss']:.1f}  ES {v['es_dmg']:3.0f} x{v['shocks']:.1f}")

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
    bands = band_scenarios()
    print("\n##### imbue: Rockbiter vs Windfury on the band's scenario (kill-speed optimum policy) #####")
    print("   growth = how far the imbue's AP has grown inside its rank: model = linear to the next rank, floor = the passive")
    print("   aura's base value, max = the level-60 tooltip value")
    for lvl in (30, 40):
        for imbue in ("rockbiter", "windfury"):
            for frac, lab in ((None, "model"), (0.0, "floor"), (1.0, "max")):
                print(compare_row(f"L{lvl} {imbue:9s} growth {lab}", with_imbue(bands[lvl], imbue, frac)))
    print("\n##### level 40 weapon: Rage of the Storm vs Bonebiter (sheet talents, kill-speed optimum policy) #####")
    for imbue in ("rockbiter", "windfury"):
        for weapon in WEAPONS_40:
            print(compare_row(f"{weapon} + {imbue}", scenario_40(weapon, imbue)))
            no_ss = dict(SHEET_TALENTS[40], ss=0, iss=0)
            print(compare_row(f"{weapon} + {imbue}, no Stormstrike", scenario_40(weapon, imbue, no_ss)))
    print("\n##### level 40 weights by weapon and imbue (AP = 1, kill-speed optimum policy) #####")
    for imbue in ("rockbiter", "windfury"):
        for weapon in WEAPONS_40:
            w, kph = weights(scenario_40(weapon, imbue))
            print(f"   {weapon + ' + ' + imbue:30s} " + "  ".join(f"{k}={w[k]:.2f}" for k in ["wdps", "str", "int", "agi", "spi", "sp", "exp", "hitpct", "critpct"]))
