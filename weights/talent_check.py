"""Talent-order check for the 2H Enhancement levelling sheet (11 Nov 2026).

Runs the kill-speed model (enh_weights.py) at bands 25 / 30 / 40 with the talents of Braedyn's levelling sheet
(docs/forever-shaman-leveling-sheet.html) and with five alternative orders, at the kill-speed optimum policy, on the
band's own gear, weapon and Rockbiter. Prints kills/hour per build, then what each talent of the sheet is worth at 40
(kills/hour lost when it is removed) and three sensitivity rows.

Every build is legal on Forever's tree (wowsims/forever ui/sim/talents/trees/shaman.json, WCLBox talent page, build
1.60.1.70888): Stormstrike and Flurry are tier 4 (15 Enhancement points; Flurry needs Mental Dexterity 3/3), Improved
Stormstrike tier 5 (20 points, needs Stormstrike), Tidal Focus Restoration tier 1, Mindfulness Restoration tier 2.

Not in the model, so worth nothing here: Improved Ghost Wolf (travel time between quest hubs), Spirit Weapons (parry),
Toughness (Stamina), Guardian Totems. Read the table with that in mind: a build that skips Improved Ghost Wolf looks
better here than it plays.

    python weights/talent_check.py
"""
import copy
from enh_weights import band_scenarios, optimum, SHEET_TALENTS

BASE25 = dict(md=3, ts=5, sf=1, ak=2, ew=3, ant=1, ss=1)            # 16 points, the sheet at 25
BUILDS = [
    ("A  sheet as written",
     "24 Anticipation, 25 Stormstrike, 26-27 Imp. Ghost Wolf, 28-29 Flurry 2, 30-31 Imp. Stormstrike, 32 Spirit Weapons, "
     "33-37 Tidal Focus, 38-40 Mindfulness",
     {25: SHEET_TALENTS[25], 30: SHEET_TALENTS[30], 40: SHEET_TALENTS[40]}),
    ("B  Flurry 5/5 first",
     "24 Ancestral Knowledge 3 (no Anticipation), 25 Stormstrike, 26-30 Flurry 5, 31-32 Imp. Stormstrike, 33-37 Tidal "
     "Focus, 38-40 Mindfulness (no Imp. Ghost Wolf, no Spirit Weapons)",
     {25: dict(md=3, ts=5, sf=1, ak=3, ew=3, ss=1),
      30: dict(md=3, ts=5, sf=1, ak=3, ew=3, ss=1, flurry=5),
      40: dict(md=3, ts=5, sf=1, ak=3, ew=3, ss=1, flurry=5, iss=2, tf=5, mind=3)}),
    ("C  Enhancement only to 40",
     "the sheet to 32, then 33-35 Flurry 5, 36-37 Mental Quickness 2, 38-40 Imp. Lightning Shield 3 (no Restoration)",
     {25: SHEET_TALENTS[25], 30: SHEET_TALENTS[30],
      40: dict(BASE25, flurry=5, iss=2, mq=2, ils=3)}),
    ("D  Tidal Focus straight after Stormstrike",
     "26-30 Tidal Focus 5, 31-34 Flurry 4, 35-36 Imp. Stormstrike, 37 Flurry 5, 38-40 Mindfulness (no Imp. Ghost Wolf, "
     "no Spirit Weapons)",
     {25: SHEET_TALENTS[25], 30: dict(BASE25, tf=5), 40: dict(BASE25, flurry=5, iss=2, tf=5, mind=3)}),
    ("E  Flurry instead of Imp. Ghost Wolf",
     "26-29 Flurry 4, 30-31 Imp. Stormstrike, 32 Flurry 5, 33-37 Tidal Focus, 38-40 Mindfulness (no Spirit Weapons)",
     {25: SHEET_TALENTS[25], 30: dict(BASE25, flurry=4, iss=1), 40: dict(BASE25, flurry=5, iss=2, tf=5, mind=3)}),
    ("F  sheet, Flurry 5/5 instead of Mindfulness",
     "the sheet to 37 (Tidal Focus 5), then 38-40 Flurry 5 (Improved Stormstrike 2/2 already gives the casting regeneration)",
     {25: SHEET_TALENTS[25], 30: SHEET_TALENTS[30], 40: dict(BASE25, flurry=5, iss=2, tf=5)}),
]
POINTS = {25: 16, 30: 21, 40: 31}
UNMODELLED = {"A": {25: 0, 30: 2, 40: 3}, "B": {25: 0, 30: 0, 40: 0}, "C": {25: 0, 30: 2, 40: 3},
              "D": {25: 0, 30: 0, 40: 0}, "E": {25: 0, 30: 0, 40: 0}, "F": {25: 0, 30: 2, 40: 3}}   # Imp. Ghost Wolf 2, Spirit Weapons 1


def kph(level, talents, **over):
    sc = copy.deepcopy(band_scenarios()[level])
    sc.talents = dict(talents)
    for k, v in over.items():
        setattr(sc, k, v)
    return optimum(sc)[0]


def main():
    for name, order, t in BUILDS:
        for lvl in (25, 30, 40):
            spent = sum(t[lvl].values()) + UNMODELLED[name[0]][lvl]
            assert spent == POINTS[lvl], (name, lvl, spent)
    print("Talent check, kills/hour at the kill-speed optimum (band gear, Rockbiter; 40 = Rage of the Storm)")
    base = {lvl: kph(lvl, BUILDS[0][2][lvl]) for lvl in (25, 30, 40)}
    print(f"   {'build':44s} {'L25':>7s} {'L30':>7s} {'L40':>7s}   vs sheet at 30 / 40")
    for name, order, t in BUILDS:
        k = {lvl: kph(lvl, t[lvl]) for lvl in (25, 30, 40)}
        print(f"   {name:44s} {k[25]:7.1f} {k[30]:7.1f} {k[40]:7.1f}   {100 * (k[30] / base[30] - 1):+5.1f}% / {100 * (k[40] / base[40] - 1):+5.1f}%")
    print()
    for name, order, t in BUILDS:
        print(f"   {name}: {order}")

    print("\nWhat each talent of the sheet is worth at 40 (kills/hour lost when it is removed; sheet = %.1f)" % base[40])
    sheet = SHEET_TALENTS[40]
    for key, label in (("ts", "Thundering Strikes 5"), ("md", "Mental Dexterity 3"), ("ak", "Ancestral Knowledge 2"),
                       ("sf", "Shamanistic Focus"), ("ew", "Elemental Weapons 3"), ("ant", "Anticipation 1"),
                       ("ss", "Stormstrike (and Improved Stormstrike)"), ("iss", "Improved Stormstrike 2"),
                       ("flurry", "Flurry 2"), ("tf", "Tidal Focus 5"), ("mind", "Mindfulness 3")):
        t = dict(sheet)
        t[key] = 0
        if key == "ss":
            t["iss"] = 0
        k = kph(40, t)
        pts = sheet[key] + (sheet["iss"] if key == "ss" else 0)
        print(f"   {label:40s} {base[40] - k:6.1f} kills/h  ({(base[40] - k) / pts:5.1f} per point)")

    print("\nSensitivity at 40 (sheet talents)")
    print(f"   {'central':66s} {base[40]:6.1f}")
    print(f"   {'Improved Stormstrike and Mindfulness regeneration stack':66s} {kph(40, sheet, regen_stack=True):6.1f}")
    print(f"   {'Improved Stormstrike chance 20% (the tooltip base value)':66s} {kph(40, sheet, iss_chance=0.2):6.1f}")
    t = dict(sheet, mind=0)
    print(f"   {'no Mindfulness, Improved Stormstrike chance 20%':66s} {kph(40, t, iss_chance=0.2):6.1f}")
    print(f"   {'build C (Enhancement only), Improved Stormstrike chance 20%':66s} {kph(40, BUILDS[2][2][40], iss_chance=0.2):6.1f}")


if __name__ == "__main__":
    main()
