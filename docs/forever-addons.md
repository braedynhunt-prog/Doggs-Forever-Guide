# Forever addons

What to install in the Forever client for Braedyn's shaman, after checking what the base game and Leatrix already do. Checked 1 Nov 2026 against CurseForge file pages and the Forever guide sites named at the bottom. Forever launches 4 Nov 2026 (client 1.60.1, addon interface 16001). No Forever client is installed on the PC yet, so nothing here is installed.

Install only files tagged Forever on CurseForge (the app's Forever flavor). Old Classic Era files are not guaranteed to load.

## Forever's addon rules
Forever uses the modern client's rules: addons can display combat values (health, threat, cooldowns) but cannot read them to make decisions ("secret values"). WeakAuras has no Forever build and does not work. Anything that reacts to combat data is limited to what Blizzard exposes as trackable buffs and debuffs.

## Built into the base game (no addon)
- Damage meter: Options > Advanced Options > Enable Damage Meter, placed in Edit Mode. Details is therefore optional.
- Cooldown Manager (off by default; Shaman not yet named among the tested classes, weapon imbues are a known gap), Click Casting, Edit Mode.
- Swing timer: one guide says there is an option, the other says Blizzard only said it may come. Unverified.
- NOT built in: a threat meter (not announced as of 4 Oct 2026), dungeon boss timers, standing-in-fire alerts, AH price tooltips.

## Covered by Leatrix (install both, Forever builds 1.60.25, 21 Oct 2026)
- Leatrix Plus: minimap button bag ("Enhance minimap": put addon buttons in one bag), sell junk + auto repair at vendors (one Automation option), free bag slots, vendor prices. All off by default; configure with /ltp.
  - Vendor price on item tooltips away from a vendor: the Forever page lists "vendor prices" but does not say where. The Classic build shows them on tooltips. Test in game.
  - Leatrix Plus does NOT do AH prices, threat, damage or bags-full advice.
- Leatrix Maps: player and cursor coordinates, unexplored areas, dungeon/flight point icons. Nothing to do with vendors, tooltips or other addons' minimap buttons.

## Install list
1. **Guidelime** (Forever flavor, v6.008+) + `Guidelime_ForeverShaman` + the **Questie** Forever bundle. The guide assumes all three.
2. **Leatrix Plus** and **Leatrix Maps** (above).
3. **DBM**, three packages, all with Forever files dated 26 Oct 2026:
   - DBM - Deadly Boss Mods (core, 12.1.18)
   - DBM - Dungeons, Delves, Challenges & Events (DBM-Dungeons-r269): 5-player dungeons, world events, holiday events, Darkmoon Faire
   - DBM - SoD and Vanilla (DBM-Vanilla_SoD-r834): all Vanilla raids, plus BFD/Gnomeregan/Sunken Temple
   - Not confirmed from the CurseForge pages: Vanilla world bosses (Azuregos, Kazzak; a DBM-Azeroth folder exists in the GitHub mirror) and timers for Forever's own new raids (raids open 9 Dec 2026; expect updates then).
4. **GTFO** (6.12.2, 16 Oct 2026, one zip covers Retail and Forever): audible alert when standing in fire or other harmful ground effects, plus an AFK-attacked alert. On the modern API it can only alert on mechanics that apply a trackable debuff, so some ground effects will be silent. DBM warns for scripted boss abilities only; it is not a generic standing-in-fire alert. Test GTFO in a dungeon early.
5. **Auctionator** (Forever build): AH plus auction and vendor prices on item tooltips. Covers the tooltip-price slot and feeds LootOptimizer.
6. **LootOptimizer Forever**: when bags are full, one-click swap of the loot with the cheapest bag item (vendor value x stack, or AH value via Auctionator); "make room now" option; protects profession mats. New (late Oct 2026), lightly tested. Alternative with no automation: Loot Triage.
7. **RareScanner** (RareScanner_FOREVER_1.60.1): rare spawn alerts.
8. **Pawn** (2.14.0 Forever flavor): default scales are the Classic Era ones, so import the scale below.
9. Optional, dungeons only: a threat meter. Forever Threat (looks like the built-in damage meter) or ForeverThreat (Omen-style). Addons cannot read a mob's full threat list on Forever.
10. **Shortest Path Forever**: directions in the objective tracker across walking, known flights, boats, tram, portals, for anywhere the guide does not route (the guide itself carries every flight, boat and tram step for 1-30). Days old as of 1 Nov 2026, unverified. Alternative: Mapzeroth (draws the route on the map). TomTom is only a straight-line arrow, no routing.
11. **Plater Nameplates** (Plater-v662, 28 Oct 2026, Forever tagged on the project page): nameplates. Nothing on its page about Forever limits, but the "secret values" rule means any script that reads health or threat to recolour plates may not work; stock profile first.
12. **What's Training? (Forever)** by Zerkaa (1.1.0, 22 Sep 2026): spellbook button listing trainable spells and prices, spell lists checked against Forever trainers; spells no trainer sells go in a "Not sold by the trainer" section. Beta quirk noted on its page: settings do not persist across logins. The older Fusionpit "What's Training?" also lists Forever support; take the Zerkaa one first.
13. **GatherMate2** + **GatherMate2 Data Wowhead classic**, for Mining nodes from the start. Status 1 Nov 2026: the data addon has a Forever-tagged file (v2026-10-17; no fishing pools, "no data on wowhead for fishing nodes"). GatherMate2 itself has NO Forever-tagged file on either CurseForge project: the Retail project lists Forever as a flavor and its description mentions a "NodesVanilla" namespace "for the older names used in Forever and Classic", but its only file is Retail 1.52.3 (17 Aug); the Classic project (1.47.11, 29 Jul) does not list Forever at all. Install the Retail GatherMate2 with the data addon and test; GatherPath Forever (draws a loop through recorded nodes) says it works with GatherMate2 on Forever, which suggests the Retail build loads. Unverified.
14. **Better Fishing** (file 66, 21 Oct 2026, Forever tagged): one keybind casts and then hooks the bobber via soft targeting, optional right-double-click cast, "Enhanced Sound" option. 9 KB, no dependencies. Worth it: the route has fishing stops to 130+ skill and this halves the clicking. Its page's range caveat names Classic Era/TBC/Mists, not Forever; if the keybind hook misses far bobbers, switch on double-click. Companion the author suggests: Speedy AutoLoot (the base game's auto-loot option should do).
15. **Prat 3.0** (3.9.113, 14 Oct 2026, Forever tagged in Recent Files): chat (timestamps, class colours, URL copy, channel sticky). No Forever-specific notes on its page.
16. **Road To Sixty** (CurseForge road-to-sixty, by Hotdoghands, 1.18.0 of 1 Nov 2026; project lists Forever 1.60.1, Classic Era and TBC Anniversary): records the character's path from 1 to 60 and replays it on the world map (up to 32x), with per-level gear, level-up summaries and a Stats tab; /rts, /rts map, /rts stats. Free companion app and wiki at roadtosixty.online for syncing between PCs. Its page says "Install it before you start": nothing is recorded retroactively, so it goes in before the first login on 4 Nov. Recent files are tagged Classic/TBC rather than Forever; whether 1.18.0 loads on Forever is an in-game test. Similar, not installing: Journey Tracker (journeytracker.dev, 0.6.15): stats export and rankings rather than a map replay.

## Not installing (redundant with the above)
Details (built-in damage meter), MinimapButtonButton / Minimap Button: Forever (Leatrix bag), ForeverForge / ForeverPlusPlus / Auto Forever (Leatrix sells junk and repairs), GearQuest Forever (Pawn + our scale), TomTom (Guidelime arrow), paid route addons (RestedXP, Journey, Zygor), Baganator/Bagnon unless the default bags annoy him.

## In-game test list
Struck 2 Nov 2026 after reading the installed .toc/Lua files and the project pages (docs/audit-2026-11-02.md): Pawn stat names (HitRating/CritRating/ExpertiseRating, and 2.14.1 ships Forever default scales), DBM-Party-Forever covers the four new dungeons, GatherMate2 1.52.3-11 (22 Oct) and RoadToSixty 1.18.0 are Forever builds, Questie 12.4.0 + QuestieDB 1.0.10 and Guidelime 6.015 are current. GTFO's Forever spell files are empty stubs, so it will not fire in Classic dungeons: known gap, not a test. Leatrix Plus has no passive sell-price tooltip; use its "Show info cards" keybind or Auctionator.
- Cooldown Manager works for Shaman spells.
- DBM-Azeroth (world bosses; its toc lists no 16001) fires on Forever; DBM timers for Forever's new raids after 9 Dec.
- Better Fishing keybind hooks the bobber at full cast range.
- Road To Sixty starts recording on the first login (install before it).

## Pawn scale for 2H Enhancement (from `forever-enh-stat-weights.md`, recommended 15-20 set)

Weights: weapon DPS 14, Str 2, AP 1, Int 1.15 (13 Nov 2026: Mental Dexterity is 100% of Int again since the 12 Nov hotfix; it was 1.65 at 150%; docs/audit-2026-11-13.md), Agi 0.8 (0.6 at 15), Spirit 2.5, Sta 0.25 floor, spell damage 2.0, expertise 7 per 1%, +1% hit or crit 6. (8 Nov 2026: Spirit 1.0 -> 2.5, spell damage 1.5 -> 2.0, Int 1.55 -> 1.65, Agi 0.85 -> 0.8 from the level-21 character sheet: mana regen is 1.25 x Spirit per 5 s with no Int term; docs/audit-2026-11-08.md.) Stat names verified 4 Nov 2026 against Pawn 2.14.1 (TooltipParsing.lua, Localization.lua) and live Forever tooltips: hit is "Improves your chance to hit by 0.4%" -> HitRating in percent; crit "Improves your chance to get a critical strike by 1.0%" -> CritRating in percent; expertise has its own Forever regex, "Reduces chance to be Dodged or Parried by 0.6%" -> ExpertiseRating in percent (so the weight is per 1%, not per rating point: the model priced 6 points = 2.6% at 18, about 7 per 1%); spell damage lines -> SpellDamage. Pawn merges melee and spell hit/crit weights on Forever, and the import starts from an empty scale (no template weights, 2H upgrades not hidden). Whether the expertise percent shown changes with level is still an in-game check. The weapon DPS weight assumes Rockbiter; redo at 30 when Windfury makes speed matter. Pawn keeps scales in the account SavedVariables, so paste this in Pawn > Scale > Import after the first login.

```
( Pawn: v1: "Forever 2H Enh 15-20": Class=Shaman, Spec=Enhancement, Dps=14, Strength=2, Ap=1, Intellect=1.15, Agility=0.8, Spirit=2.5, Stamina=0.25, SpellDamage=2, ExpertiseRating=7, HitRating=6, CritRating=6 )
```

## Sources (checked 1 Nov 2026)
CurseForge pages: leatrix-plus (file 9275554), leatrix-maps, deadly-boss-mods (file 9335631), deadly-boss-mods-dbm-dungeons (file 9335679), dbm-vanilla (file 9336008), gtfo (file 9208630), lootoptimizer-forever, loot-triage, rarescanner, pawn, auctionator, road-to-sixty (file 9391639, checked 2 Nov 2026), journeytracker.dev (2 Nov 2026). Guides: wowforever.be/guides/built-in-ui-tools, wofwforever.com built-in UI setup (4 Oct), wowforeverinfo.com/guides/addons (23 Oct), Blizzard forum thread "Threat Meter" (Forever beta).
