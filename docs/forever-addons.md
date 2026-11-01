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
1. **Guidelime** (Forever flavor, v6.008+) + `Guidelime_ForeverAlliance` + the **Questie** Forever bundle. The guide assumes all three.
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

## Not installing (redundant with the above)
Details (built-in damage meter), MinimapButtonButton / Minimap Button: Forever (Leatrix bag), ForeverForge / ForeverPlusPlus / Auto Forever (Leatrix sells junk and repairs), GearQuest Forever (Pawn + our scale), TomTom (Guidelime arrow), paid route addons (RestedXP, Journey, Zygor), Baganator/Bagnon unless the default bags annoy him.

## In-game test list
- Leatrix Plus vendor price shows on tooltips away from a vendor.
- GTFO fires on at least one dungeon ground effect (Deadmines or Wailing Caverns).
- Pawn's Weights tab shows hit, crit and expertise after importing the scale (stat names unverified).
- Cooldown Manager works for Shaman spells.
- DBM-Vanilla covers world bosses; DBM timers for Forever's new raids after 9 Dec.

## Pawn scale for 2H Enhancement (from `forever-enh-stat-weights.md`, recommended 15-20 set)

Weights: weapon DPS 14, Str 2, AP 1, Int 1.05, Agi 0.85 (0.6 at 15), Spirit 1.0, Sta 0.25 floor, spell damage 1.5, expertise 3, +1% hit or crit 6. Pawn stat names below are from Pawn's Classic build and the hit/crit/expertise names are unverified against the Forever item parser. The weapon DPS weight assumes Rockbiter; redo at 30 when Windfury makes speed matter.

```
( Pawn: v1: "Forever 2H Enh 15-20": Class=Shaman, Spec=Enhancement, Dps=14, Strength=2, Ap=1, Intellect=1.05, Agility=0.85, Spirit=1, Stamina=0.25, SpellDamage=1.5, ExpertiseRating=3, HitRating=6, CritRating=6 )
```

## Sources (checked 1 Nov 2026)
CurseForge pages: leatrix-plus (file 9275554), leatrix-maps, deadly-boss-mods (file 9335631), deadly-boss-mods-dbm-dungeons (file 9335679), dbm-vanilla (file 9336008), gtfo (file 9208630), lootoptimizer-forever, loot-triage, rarescanner, pawn, auctionator. Guides: wowforever.be/guides/built-in-ui-tools, wofwforever.com built-in UI setup (4 Oct), wowforeverinfo.com/guides/addons (23 Oct), Blizzard forum thread "Threat Meter" (Forever beta).
