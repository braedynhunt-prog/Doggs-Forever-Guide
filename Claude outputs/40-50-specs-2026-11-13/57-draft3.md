# Spec 57 - Ironforge: the round's hand-ins (13 Nov 2026, written by the main session)

Written against `docs/40-50-plan-2026-11-12.md`, second revision, section "### 57 Ironforge: the round's hand-ins". Facts checked 13 Nov against `tooling/qdb` 1.0.16 (quest rows [1], [2], [7], [11], [12], [21]; `python tooling/loc.py`), `data/zone_*.json` through `python tooling/qinfo.py`, `tooling/trainer_costs.json` (12 Nov), `tooling/client/1.60.1.70938/TaxiNodes.csv` and `TaxiPath.csv`, and Braedyn's leveling sheet (`docs/forever-shaman-leveling-sheet.html`, rows 46 / 48 / 50).

## 1. Header
- File `57_Ironforge.lua`, group "Forever Shaman 30-60". `[N 48-49 Ironforge]`. No `[NX]`: the last chapter of round 2 (round 3 adds it later, as chapter 41 gets its `[NX]` to 42 in this round).
- `[GA Alliance]`; class lines `[A Shaman]`.
- Description (suggested): "The round's last stop: the Explorers' League hand-ins for Uldum and Tymor, the training rows you have not bought, and what round 3 starts with."
- Level on entry 48.4, on exit 48.6 on required quest XP at the 65% share (route_xp.py); with required levels enforced the round ends at about 47.9. The chapter itself has no fight and no level gate.
- **Level-check line (first `[OC]`)**: "This chapter needs no level: three hand-ins and the trainer. Buy the rows your level opens (46, 48, 50)."

## 2. Entry state
- Stands at Marshal's Refuge at the end of chapter 56 (flight point taken there). Hearth: Gadgetzan (chapter 56 binds there; the DB has no innkeeper in Un'Goro).
- Carried in, required: 2977 Return to Ironforge (accepted at the Stone Watcher of Norgannon in chapter 53, after 2954), 3461 Return to Tymor with Tymor's Drawing Kit (accepted from Pilot Xiggs Fuselighter on his island in Azshara, chapter 55).
- Carried in, optional: 7070 Shadowshard Fragments if the ten fragments dropped in Maraudon (chapter 54); the round-3 carries (below).

## 3. Travel and hearth
- Marshal's Refuge -> Gadgetzan (TaxiPath 452 / 453, cost field 730 = 7s 30c) -> Theramore (path 201, 6s 30c). Gadgetzan's flight point is taken in chapter 46; Theramore's is known from round 1.
- Theramore: the optional 7070 hand-in at Archmage Tervosh [4967], Dustwallow 66.4,49.3, then the boat to Menethil Harbor (pier as in round 1; unverified).
- Menethil Harbor -> Ironforge (path 17, 3s 30c).
- Bind at Ironforge on arrival ([S] at Innkeeper Firebrew [5111], 18.1,51.5, position from the chapter 52 spec): round 3 starts from here.
- The chapter and the round end in Ironforge.

## 4. Route
1. `[OC]` level-check line (section 1).
2. Fly Marshal's Refuge -> Gadgetzan -> Theramore (`[F]` steps; two flights).
3. `[O]` At [TAR4967 Archmage Tervosh], 66.4,49.3 Dustwallow Marsh: `[QT7070 Shadowshard Fragments]` (3,450 XP) - only if you hold the ten fragments; otherwise `[QS7070]` here (rule 9: grind / luck, one run, never a re-run).
4. Boat to Menethil Harbor, fly to Ironforge.
5. Bind: `[S Ironforge]` at the innkeeper.
6. At [TAR2916 Historian Karnik], 77.5,11.8 Ironforge: `[QT2977 Return to Ironforge]` (470 XP; prerequisite 2954, row [12]) and `[QA2964 A Future Task]` (next quest, row [21]).
7. At [TAR5387 High Explorer Magellas], 69.9,18.6 Ironforge: `[QT2964 A Future Task]` (4,700 XP; "Speak with High Explorer Magellas in Ironforge"). No follow-up in the DB (row [21] empty).
8. At [TAR8507 Tymor], 31.0,4.8 Ironforge: `[QT3461 Return to Tymor]` (7,600 XP + 2g 20s; prerequisite 3449, row [12]; "Return Tymor's Drawing Kit to him in Ironforge"). No follow-up in the DB.
9. `[A Shaman]` At [TAR258098 Eldrun Stormbreaker], 47.1,13.8 Ironforge, `[T]`: the rows not yet bought. Prices are Wowhead's raw values (trainer_costs.json, 12 Nov; whether the trainer shows 5% less is on the test list). The sheet's buys first:
   - Level 46 (2g each): **Mana Spring Totem 3** (sheet); later Frost Shock 3, Magma Totem 3; the row also has Chain Heal 2, Windwall Totem 2, Flametongue Weapon 5. Row 12g.
   - Level 48 (2g 20s each): **Earth Shock 6, Healing Wave 8, Flametongue Totem 3** (sheet); the row also has Chain Lightning 3, Stoneclaw Totem 5, Lightning Shield 6, Frostbrand Weapon 4, Ancestral Spirit 4, and Mana Tide Totem 3 at 16s. Row 17g 76s.
   - Level 50, only if he is 50 (2g 40s each): **Windfury Weapon 3, Lightning Bolt 9, Searing Totem 5** (sheet); later Healing Stream Totem 4; Riptide 2 at 2g 63s 15c. Row 12g 23s 15c.
   - Level 44 row if it is still open (1g 80s each; sheet: Lesser Healing Wave 4, Lightning Bolt 8).
10. `[O][A Shaman]` Ask Eldrun for a level-50 class quest, only at 50: the Classic ones (8410-8413) are Horde-side on Wowhead and no Alliance version is in the data. In-game check; no quest tag.
11. `[O]` profession ranks still open, each only at its skill: Artisan Skinning at [TAR6291 Balthus Stoneflayer] (5g, skill 200); the Artisan First Aid and Fishing starters (6625 at Nissa Firestone, 6609 at Grimnur Stonebrand) at skill 225 if never taken.
12. `[OC]` gold check from `python tooling/gold.py` once the chapters exist (plan Threads: quest money of the round 35g 53s against 57g 69s of training at raw values).
13. `[OC]` end Check (section 7).

## 5. Gear calls
None: 2977, 2964 and 3461 give no item choice (zone_1537.json itemchoices empty; 3461 pays 2g 20s). 7070's pendants (18.0 / 14.0) are below his neck (chapter 54 spec): vendor.

## 6. Out
Nothing of this stop is out. Not taken here on purpose: 2993 Return to the Hinterlands (Nethergarde, round 3), 3445 The Sunken Temple (Feathermoon, round 3).

## 7. End check
Log at the round's end, carried to round 3: 1475 Into The Temple of Atal'Hakkar (from Brohann Caskbelly, chapter 49), 624 Cortello's Riddle (the scroll, chapter 49), 7066 Seed of Life (Maraudon, hand-in at Moonglade), 3908 It's a Secret to Everybody (if Linken gave it; Winterspring), any OOX rescue he holds (Booty Bay), and whatever of Un'Goro's tiers his level had not opened (chapter 56 lists them by id). Hearth Ironforge.

## 8. Totals
3 required quests, 12,770 XP, 2g 20s; optional 0 XP in the plan's row (7070's 3,450 XP is counted in chapter 54's optional list). Equals the plan's XP table row for chapter 57.

## 9. Unverified / in-game test list, Needs pull, Unsure
- Test list: the Theramore - Menethil boat; the trainer's price (raw or 5% less); a level-50 shaman quest for the Alliance.
- Needs pull: nothing.
- Unsure: whether he still holds 7070 (chapter 54).

## 10. Deviations from the route plan
1. The optional 7070 hand-in at Theramore is added on the way (the chapter 54 spec found that Tervosh both gives and takes it, and this is the route's only Theramore pass after Maraudon). No change to the required list or totals.
2. A bind at Ironforge is added so round 3 starts there.
