# Spec 51 - Zul'Farrak (dungeon) (drafted 13 Nov 2026 against the second revision of the 40-50 plan)

Data used (all read 13 Nov 2026): `tooling/qdb` = QuestieDB Forever 1.0.16 (quest rows [1] [2] [3] [7] [9] [11] [12] [22] [26] [27]; npc rows [3] [4] [5] [6]; item rows [1]; object rows [3]) via `qinfo.py`, `loc.py` and scratch readers; `data/zone_1176.json`, `zone_440.json`, `zone_400.json` (Wowhead XP, money, itemchoices / itemrewards, side, reqlevel); `data/drop_rates.json`; `data/wowhead_quest_links.json` (96770 only); `data/browser/r2_pages3_2026-11-13.tsv` (QUEST 96770) and `r2_pages_2026-11-12.tsv` (ITEM 10660, 277112); `tooling/client/1.60.1.70938/TaxiNodes.csv`, `TaxiPath.csv`; `weights/tooltips/2026-11-12.json` scored with `score_items.parse/score` and `profiles.enh_band_weights()[40]` (the `--band 40` weights: wdps 14, Str 2, Int 1.69, Agi 1.12, Spi 2.5 / 1.5, SP 2.0 / 1.0); `nether.wowhead.com/forever/tooltip/item/<id>` fetched 13 Nov for Saltseer's Helm (279930, not in the dated file) and 40 Zul'Farrak boss drops (saved in this scratch folder as `boss_tips.json`, not in the repo); plan `docs/40-50-plan-2026-11-12.md` (second revision), route file `docs/40-50-route-2026-11-12.txt` (chapter 51 row: 3520 2865 2768 3527, opt 3042 2769 2770, zones 440 1176), `route_xp.py` output (51: 4 quests, 19,200 XP, 65s, 44.5 -> 44.7, "UNDER: wants 46"); pool `1176_ZulFarrak.txt`, `_decisions.tsv`, `overrides_r2.tsv`. Classic-only knowledge (room order, the stairs event, the mallet) is marked unverified.

## 1. Header
- File: `51_ZulFarrak.lua`
- `[N 44-45 Zul'Farrak]` (required dungeon chapter: no `[O]` on the title)
- `[NX 44-46 Searing Gorge]` (chapter 52's `[N]` as the plan gives it; copy it exactly if 52's spec changes it)
- `[GA Alliance]`; class lines `[A Shaman]`. Group "Forever Shaman 30-60".
- Description: `[D Forever Shaman 30-60 (Braedyn)\\Zul'Farrak at 44-45: Feathermoon - Thalanaar - Gadgetzan by flight, bind at Gadgetzan, Screecher Spirits to Yeh'kinya at Steamwheedle Port for The Prophecy of Mosh'aru, one run through Zul'Farrak (the Mosh'aru tablets, the Divino-matic Rod, Scarab Shells, and the Tiara, Nekrum's Medallion and Zum'rah's head for the eastern trip), then the Gadgetzan and Steamwheedle hand-ins.]`
- Level on entry: 44.5 (route_xp); exit 44.7 on quest XP (plus the run's kill XP, not counted).
- **First line (level check)** `[OC]`: "This chapter wants level 46: no quest here needs more than level 40, but the quest bosses are 45-46 elite (Sergeant Bly 45; Theka the Martyr, Witch Doctor Zum'rah, Hydromancer Velratha, Nekrum Gutchewer 46) and the trash 43-47 elite; Shadowpriest Sezz'ziz is 47, Antu'sul and Chief Ukorz 48. You arrive at about 44.5, the low end: look for a group of 44-48, ideally with a tank of 46 or more. At 44-45 do the quest bosses; Antu'sul and Chief Ukorz hold no quest item and can be left if the group struggles. There is no conditional quest to do first: every required pickup is open at 40."

## 2. Entry state
- Where: Feathermoon Stronghold, at [TAR8019 Fyldren Moonfeather] 30.2,43.3 Feralas (Hippogryph Master; qdb npc 8019, one spawn), where chapter 50 ends. Hearth: Feathermoon (chapter 50's bind, per the prompt). Rebound to Gadgetzan in leg 1.
- Flight points assumed known: Feathermoon (chapter 47 or 50), Thalanaar (chapter 47 ends there), Gadgetzan (chapter 46 `[P Gadgetzan]` at Bera Stonehammer).
- Quests carried in (must be in the log):
  - **3520 Screecher Spirits**, complete (picked up at Yeh'kinya in chapter 46, done in Feralas in chapter 47).
  - **96770 The Witch Doctor's Head** (Archmage Lan'dalock 20735, Alterac 15.3,73.9, chapter 43).
  - **2991 Nekrum's Medallion** (Thadius Grimshade 8022, Blasted Lands 66.9,19.5, chapter 49, after 2990's hand-in).
  - **2846 Tiara of the Deep** (Tabetha 6546, Dustwallow 46.1,57.1, chapter 50).
  - Possibly **2865 Scarab Shells** (chapter 46 hands in 2864 Tran'rek, which offers it; if 46's spec takes it there, step 4 is skipped).
  - Conditional: **2769 The Brassbolts Brothers** only if it was taken from Klockmort Spannerspan (6169, Ironforge 67.9,46.1) on an Ironforge pass of chapter 48 or 49 (not this chapter's to place); **2770 Gahz'rilla** only if taken at Wizzle on an earlier pass (see D2).
  - Untouched here, carried through: 2972 Doling Justice, 4267 Rise of the Silithid, 2939 In Search of Knowledge (to Darnassus, chapter 55); 1475 Into The Temple of Atal'Hakkar and 624 Cortello's Riddle (round 3); 6610 Clamlette Surprise if chapter 46 took it at Cooking 225.
- Gear on entry (from round 1 and the round-2 table): two-hander Bigger Rock on Bigger Stick (chapter 43, if Mugg dropped the Eye) or Rage of the Storm / Bonebiter; head Saltseer's Helm (chapter 31) or Zorbin's Water Resistant Hat (chapter 50, conditional); legs Apprentice Sorcerer's Slacks (chapter 31); chest Doomsayer's Robe (39e) or Blackwater Tunic (49); hands Traveled Gloves (39).
- Training / professions: none due. No shaman trainer in Kalimdor on this route (Threads: stops in 43, 44, 48, 49, 52, 57). Artisan Cooking gate optional (step 6).

## 3. Travel and hearth
- In: at Fyldren Moonfeather fly Feathermoon -> Gadgetzan. TaxiPath 70938: 326 Feathermoon (node 41) -> Thalanaar (31), cost 430; 324 Thalanaar (31) -> Gadgetzan (39), cost 730 (raw copper: 11s 60c for both legs; the game routes through Thalanaar; whether the trainer-style 5% cut applies is the open test-list question). No direct Feathermoon - Gadgetzan path (node 41 links only to 26 Auberdine, 31 Thalanaar, 37 Nijel's Point, 73 Cenarion Hold).
- Gadgetzan: flight master [TAR7823 Bera Stonehammer] 51.0,29.3 Tanaris (L55 elite guard-type, Gryphon Master); innkeeper [TAR7733 Innkeeper Fizzgrimble] 52.5,27.9 Tanaris: **bind `[S Gadgetzan]`** (plan Threads: Gadgetzan for 51).
- Steamwheedle Port: no flight point (TaxiNodes has none); ride from Gadgetzan to Yeh'kinya 67.0,22.4 (about 16 map units; estimate).
- Zul'Farrak: the only Tanaris object near the dungeon is the **Meeting Stone** (object 178829) at **38.5,20.7 Tanaris**; the portal's position is not in the data (Classic: just north of the stone, unverified). Sandfury trolls outside are elite (Sandfury Hideskinner 42-43, Axe Thrower and Firecaller 43-44, qdb rank 1, x36-42 y20-24) and Warleader Krazzilak (8199, 45 rare elite, 38.8,21.7): stay on the path with the group. Ride Steamwheedle Port -> the Meeting Stone across north Tanaris (about 29 units; estimate, road unverified).
- Out: hearth (or Astral Recall) to Gadgetzan if off cooldown, otherwise ride (about 15 units, estimate). Gadgetzan hand-ins, Steamwheedle Port for 3527, back to Gadgetzan; the chapter ends at Bera Stonehammer, hearth Gadgetzan. Chapter 52 starts with the Gadgetzan - Theramore flight (paths 201 / 222).
- Optional only: Wizzle Brassbolts [4453] 78.1,77.1 Thousand Needles (Mirage Raceway), north of Gadgetzan by road (distance not in the data; unverified).

## 4. Route

### Leg 1 - Gadgetzan (flight in, bind, pickups)
1. At [TAR8019 Fyldren Moonfeather] `|cFFfff8a3Fly to [F Gadgetzan]|r` `[G30.2,43.3 Feralas]` (via Thalanaar).
2. At [TAR7733 Innkeeper Fizzgrimble] bind `[S Gadgetzan]` `[G52.5,27.9 Tanaris]`.
3. At [TAR7407 Chief Engineer Bilgewhizzle] `[QA2768 Divino-matic Rod]` (6,300 XP at the hand-in, no money; req 40, L47; no prerequisite: rows [11] [12] empty) `[G52.5,28.5 Tanaris]`. Objective: the Divino-matic Rod (item 8548) from Sergeant Bly. Label in the run.
4. If not in the log from chapter 46: at [TAR7876 Tran'rek] `[QA2865 Scarab Shells]` (3,900 XP + 65s at the hand-in; req 40, L45; rows [11] [12] empty; row [27] lists 2864 Tran'rek as its breadcrumb, which chapter 46 hands in) `[G51.6,26.8 Tanaris]`. Objective: 5 Uncracked Scarab Shells (item 9238; quest row [7] text, row [9] gives no count).
5. `[O]` At [TAR7804 Trenton Lighthammer] `[QA3042 Troll Temper]` (3,900 XP + 1g 95s at the hand-in; req 40, L45; no prerequisite) `[G51.4,28.8 Tanaris]`. Label: **grind / luck**: 20 Vials of Troll Temper (item 9523) at 15.6% over 16 troll and zombie types (drop_rates.json: Blood Drinker 393/2053, Witch Doctor 243/1369, Shadowhunter 214/1217, Shadowcaster 136/724, Zul'Farrak Zombie 159/832 ...) = about 128 kills; costs nothing to carry, never farmed, abandoned if short.
6. `[O]` Cooking 225 only (gate, rule 11: profession rank): at [TAR8125 Dirge Quikcleave] `[QT6610 Clamlette Surprise]` if held and complete, or `[QA6610 Clamlette Surprise]` (3,900 XP; req 35, L45; quest row [17] needs Cooking 225; 12 Giant Eggs, 10 Zesty Clam Meat, 20 Alterac Swiss) `[G52.6,28.1 Tanaris]`. Not counted (plan Threads: chapter 46, 51 or 53). If chapter 46's spec carries the line, the writer keeps one of the two.

### Leg 2 - Steamwheedle Port (Screecher Spirits first)
7. Ride north-east to Steamwheedle Port (about 16 units, estimate).
8. At [TAR8579 Yeh'kinya] `[QT3520 Screecher Spirits]` (3,750 XP, no money; req 40, L44) `[QA3527 The Prophecy of Mosh'aru]` (5,250 XP at the hand-in, no money; req 40, L47; prerequisite 3520, quest row [12] = [3520]) `[G67.0,22.4 Tanaris]`. Objective: the First Mosh'aru Tablet (10660) and the Second Mosh'aru Tablet (10661). (4787 The Ancient Egg, offered after 3527, is out: section 6.)

### Leg 3 (optional) - Wizzle Brassbolts, only if the group has the Mallet of Zul'Farrak
9. `[OC]` Gahz'rilla has to be summoned at the Gong of Zul'Farrak (object 141832, Zul'Farrak) with the Mallet of Zul'Farrak (item 9240): QuestieDB has the mallet with no source at all (item rows [1]-[3] empty). The DB has the Sacred Mallet (9241) as a drop of Qiaga the Keeper (7996, level 50 elite, Hinterlands 48.6,68.2, at the Altar of Zul); Classic turns it into the Mallet at the Altar of Zul (unverified on Forever). Qiaga is an elite outside a dungeon (rule 13), so the guide does not send him for it: Gahz'rilla only if someone in the group brings the mallet. Ask when the group forms; no mallet, skip this leg and every 2769 / 2770 line.
10. `[O]` Ride north out of Tanaris to the Mirage Raceway (Shimmering Flats; distance not in the data). At [TAR4453 Wizzle Brassbolts] `[QT2769 The Brassbolts Brothers]` (405 XP, no money; req 40, L46; only if carried from Ironforge) and `[QA2770 Gahz'rilla]` (7,100 XP + 75s at the hand-in; req 40, L50; rows [11] [12] empty, row [27] lists 2769 as its breadcrumb, so Wizzle should offer it without 2769 - unverified) `[G78.1,77.1 Thousand Needles]`. Ride back south to the Meeting Stone. (D2: if chapter 46's road pickup takes 2770 earlier, this pre-run ride goes.)

### Leg 4 - the run (one run, never a re-run; rule 2)
11. `|cFFFF0000GROUP 5|r` Ride to the Zul'Farrak Meeting Stone and enter with the group (portal north of the stone; position not in the data, unverified) `[G38.5,20.7 Tanaris]`.
12. `[OC]` label block (as 39e): one `[OC]` per quest with its label (below). Inside: no `[G]` (the DB has no positions in zone 1176: every spawn is [-1,-1]). Mobs (qdb npc rows with a 1176 spawn): trash 43-47 elite (Sandfury Shadowcaster 43-44, Zul'Farrak Zombie 43-44, Sandfury Cretin 43-45, Blood Drinker and Witch Doctor 44-45, Shadowhunter, Soul Eater, Guardian 45-46, Sandfury Executioner 46, Sul'lithuz Sandcrawler 45-47, Sul'lithuz Abomination 47; Zul'Farrak Dead Hero 45-46 and Scarab 44-46 not elite); rare elites Sandarr Dunereaver, Dustwraith, Zerillis 45; bosses Sergeant Bly 45, Theka the Martyr, Witch Doctor Zum'rah, Hydromancer Velratha, Gahz'rilla, Nekrum Gutchewer, Ruuzlu 46, Shadowpriest Sezz'ziz 47, Antu'sul and Chief Ukorz Sandscalp 48, all rank 1 (elite). Left out of the range: summoned Sul'lithuz Hatchling / Broodling (30-39, Antu'sul's adds in Classic), Delirious Ancient (222573, 52, zone id only, no spawn, no rank: a Forever NPC whose role is unknown), Elder Wildmane (60, festival) and Gahz'ranka (63, a Zul'Gurub boss misfiled in 1176).
13. Quests and their bosses (labels):
   - **2865 Scarab Shells** - **normal, collection**: 5 Uncracked Scarab Shells from Scarabs (7269, L44-46, not elite: npc row [5] empty), 36.15% (drop_rates.json, single dropper, 12 Nov) - budget about 14 scarabs. Where the scarabs are is not in the data (Classic: around Theka the Martyr; unverified). Kill line: "Kill [TAR7269 Scarab] for 5 Uncracked Scarab Shells [QC2865] (~36% - budget ~14 kills)". Short at the end of the run: abandon at step 16 (no re-run). See D1 for the label.
   - **3527 The Prophecy of Mosh'aru** - **normal on boss items, one kill each**: First Mosh'aru Tablet from Theka the Martyr (7272, 46 elite; Wowhead 21.8% = 81 of 372 kills over all kills, quest or not), Second Mosh'aru Tablet from Hydromancer Velratha (7795, 46 elite; 34.73%). Hold each with `[CI10660,1]` / `[CI10661,1]` (lesson: one of several items is held with [CI], not [QC id,index]).
   - **96770 The Witch Doctor's Head** (carried, counted in 52) - **normal on a boss item, one kill**: Zum'rah's Head (277112) from Witch Doctor Zum'rah (7271, 46 elite; Wowhead item page 72 of 256 = 28.1% over all kills). The item page also lists a second Zum'rah (220076, Wowhead classification elite, qdb rank empty, no spawn, no kill count); one kill of whichever stands there. Quest is Forever-only (patch 1.60.1, Wowhead page: Type Dungeon, Side Alliance, Sharable); objective read from quest row [7] ("Slay Witch Doctor Zum'rah and bring Zum'rah's Head") since row [9] holds only the item.
   - **2846 Tiara of the Deep** (carried, counted in 52) - **normal on a boss item, one kill**: Tiara of the Deep (9234) from Hydromancer Velratha (7795, 46 elite; 43.09%). Same kill as the Second Tablet.
   - **2768 Divino-matic Rod** - **normal on a boss item, one kill**: from Sergeant Bly (7604, 45 elite; 36.92%). Classic (unverified on Forever): Bly and his crew (Weegli Blastfuse 7607 43, Murta Grimgut 7608, Oro Eyegouge 7606, Raven 7605, all 44 elite in qdb) are caged on the pyramid; the Executioner's Key (8444, drop of the Sandfury Executioner 7274, 46 elite, per item row [1]) opens the cages, the stairs event follows (waves of trolls), and Bly's crew turn on the group afterwards; Bly drops the rod.
   - **2991 Nekrum's Medallion** (carried, counted in 52) - **normal on a boss item, one kill**: from Nekrum Gutchewer (7796, 46 elite; 11.68% over all kills). Classic: Nekrum comes down with Shadowpriest Sezz'ziz at the end of the stairs event (unverified). If it does not drop, 2992 The Divination (chapter 52, 1,050 XP) goes with it.
   - **3042 Troll Temper** `[O]` - **grind / luck** (step 5).
   - **2770 Gahz'rilla** `[O]` - **grind / luck**, only with the mallet: Gahz'rilla's Electrified Scale (8707) from Gahz'rilla (7273, 46 elite; 33.6%), summoned at the Gong of Zul'Farrak (object 141832). One kill only.
14. Suggested steps inside (writer: as 39e, no `[G]`): Scarab kill line; Theka `[CI10660,1]`; Zum'rah `[QC96770]`; Velratha `[QC2846]` + `[CI10661,1]`; `[O]` Gahz'rilla `[QC2770]`; the stairs event / Bly `[QC2768]`; Nekrum `[QC2991]`; `[O]` Troll Temper running line `[QC3042]`; boss order is the group's (Classic layout, unverified); `[OC]` boss-loot line (section 5).
15. `[OC]` Group notes: shareable per QuestieDB quest row [22] = 8 (the sharable flag): 2865, 2768, 3527, 3042, 2769, 2770, 2991, 2846; 96770 per its Wowhead page ("Sharable"); 3520 has no flag (and is handed in already).

### Leg 5 - out, abandons and hand-ins
16. After the last boss, for each quest whose item did not drop (one run, rule 2/3): `[QS2865]` (fewer than 5 shells), `[QS3527]` (a tablet missing), `[QS2768]`, `[QS3042]` (fewer than 20 vials), `[QS2770]`, and for the carried ones `[QS96770]`, `[QS2846]`, `[QS2991]` (chapter 52 then skips their hand-ins and 2992). Each as an `[O]` "no X: abandon" line, as 39e.
17. `|cFFfff8a3Hearth to [H Gadgetzan]|r` (or Astral Recall; if both are on cooldown, ride east to Gadgetzan, about 15 units).
18. At [TAR7407 Chief Engineer Bilgewhizzle] `[QT2768]` (6,300 XP; gear G1) `[G52.5,28.5 Tanaris]`.
19. At [TAR7876 Tran'rek] `[QT2865]` (3,900 XP + 65s) `[G51.6,26.8 Tanaris]`.
20. `[O]` At [TAR7804 Trenton Lighthammer] `[QT3042]` (3,900 XP + 1g 95s) if you have 20 vials `[G51.4,28.8 Tanaris]`.
21. Ride to Steamwheedle Port: at [TAR8579 Yeh'kinya] `[QT3527]` (5,250 XP) `[G67.0,22.4 Tanaris]`. 4787 is offered now: not taken (rule 4, no text).
22. `[O]` Only with the scale: ride north to [TAR4453 Wizzle Brassbolts] `[QT2770]` (7,100 XP + 75s; Carrot on a Stick) `[G78.1,77.1 Thousand Needles]`, then back to Gadgetzan.
23. Back to Gadgetzan; `[OC]` Check line (section 7); end at [TAR7823 Bera Stonehammer] 51.0,29.3 Tanaris (chapter 52 flies to Theramore from here).

## 5. Gear calls (band 40, mail wearable; central | conservative)
- **G1, 2768 Divino-matic Rod**: take the **Engineer's Guild Headpiece** (9534, leather head +22 Spi, +10 spell damage / +29 healing) **75.0 | 43.0** over Magister Cowl (270099, cloth head +18 SP) 36.0 | 18.0 and Masons Fraternity Ring (9533, +14 Agi +5 Sta) 15.7 | 15.7. It replaces Saltseer's Helm (279930, live tooltip 13 Nov: leather +12 Int +5 Spi +8 SP) 48.8 | 35.8 or Zorbin's Water Resistant Hat (19039) 43.7 | 35.7 if chapter 50 took it. The plan's table has it as the best head reward of the round.
- 3527, 2865, 3042, 3520, 2769: no item reward (zone JSON itemchoices / itemrewards empty). 2770: Carrot on a Stick (11122, trinket, mount speed; no stats, not scored).
- For chapter 52 (handed in there; repeated so the writers agree): 2846 Tiara of the Deep gives the Spellshifter Rod (9527, 2H staff 27.6 dps +6 Sta +17 Int +40 SP) 495.0 fixed - below every two-hander he holds (vendor), and a choice of Gemshale Pauldrons (plate, unusable) or Dank Shoulderpads (270098, leather +4 Agi +13 Sta) 4.5. 2991 and 96770 have no item reward.
- **Boss drops** (tooltips fetched 13 Nov from nether.wowhead.com/forever; not in the dated file; drop chance where the tooltip prints one; req = required level - he is 44 here):
  - **The Minotaur** (9481, 2H axe 42.66 dps, 3.20 speed, +8 Str +24 Sta, BoE, req 44; qdb item row [1]: Hydromancer Velratha only; no rate in the tooltip) **613.2**: on the linear score above Bigger Rock on Bigger Stick 604.5, Bonebiter 583.5 and Rage of the Storm 529.8. The 11 Nov kill-speed model put Rage's Stormstrike bonus at about the 3.3 dps gap to Bonebiter; The Minotaur's gap over Rage is 7.1 dps. Need it; very likely an upgrade (model not re-run here: Unsure U4).
  - **The Chief's Enforcer** (9477, 2H staff 43.53 dps, 3.40, chance on hit stun, BoP, **req 45**; Chief Ukorz 26.63%) 609.4: an upgrade at 45; keep it in the bags until then.
  - Jinxed Hoodoo Kilt (9474, leather legs +10 Int +19 Spi +8 SP, req 44; Sezz'ziz 21.81%) 80.4 | 53.4 over Apprentice Sorcerer's Slacks 73.7 | 48.7: small upgrade.
  - Gahz'rilla Scale Armor (9469, mail chest +10 Sta +16 Spi +11 SP, req 43; 32.39%) 62.0 | 35.0 over Doomsayer's Robe 57.0 | 33.0 and Blackwater Tunic 51.5 | 36.5: small upgrade (only with the mallet).
  - Embrace of the Lycan (9479, leather head +8 Str +16 Sta +5 Spi +32 AP, req 44; Chief Ukorz) 60.5 | 55.5: below the Engineer's Guild Headpiece on central weights (75.0), above it on conservative (43.0) - the guide follows central, as round 1.
  - Brainlash (6440, ring +10 Int +5 Spi +11 SP -10 Sta, BoE, req 43; Ruuzlu, Sandfury Executioner, Zerillis) 51.4 | 35.4: an upgrade on any ring of the round (Woodseed Hoop 28.9 is the best quest ring).
  - Not for him: Ripsaw, The Hand of Antu'sul (1H, shield set only), Eyegouger and Diabolic Skiver (polearms), Jang'thraze / Sang'thraze (swords), Zum'rah's Vexing Cane 560.4 and Witch Doctor's Cane 474.1 (below his two-handers), Jumanza Grips 23.8 (below Traveled Gloves 40.0), plate pieces. Random-enchantment items (Wolf Rider's Headgear, Gaea's Cloak, Bloodwoven Mask, Imposing Gloves) cannot be scored before they drop.

## 6. Out
- 4787 The Ancient Egg (5,900; offered by Yeh'kinya after 3527) - `_decisions.tsv` OUT: "the Ancient Egg (Hinterlands 57.6,86.8) is guarded by Hitah'ya the Keeper and Vilebranch Aman'zasi Guards (51 elite) - rule 13; it also needs The Prophecy of Mosh'aru". Silent.
- No other Zul'Farrak-category quest is out: 2864 is chapter 46's, 2861 chapter 50's, 96770 / 2846 / 2991 chapter 52's. The Tanaris and Thousand Needles quests belong to chapters 46 and 53.

## 7. End check
- Handed in here: 3520, 3527, 2768, 2865 (or abandoned when short); 3042 handed in or abandoned; 2769 / 2770 handed in, abandoned or never taken.
- Carried out to chapter 52 (complete, or abandoned at step 16 if the item did not drop): **2846 Tiara of the Deep** (Tabetha, Dustwallow 46.1,57.1), **2991 Nekrum's Medallion** (Thadius Grimshade, Blasted Lands 66.9,19.5; opens 2992), **96770 The Witch Doctor's Head** (Archmage Lan'dalock, Alterac 15.3,73.9).
- Carried on, untouched: 2972, 4267, 2939 (chapter 55); 1475, 624 (round 3); 6610 if taken and not complete (chapter 53).
- Hearth Gadgetzan; standing at Bera Stonehammer, Gadgetzan.

## 8. Totals
- Required (4): 3520 3,750; 2865 3,900 + 65s; 2768 6,300; 3527 5,250 = **19,200 XP, 65s** - equals the plan's row (4, 19,200, 65s).
- Optional / conditional: 3042 3,900 + 1g 95s (grind / luck); 2769 405 (conditional); 2770 7,100 + 75s (grind / luck, mallet) = **11,405 XP**, 2g 70s - equals the plan's 11,405.
- Done here, counted in chapter 52: 96770 5,050 + 1g 30s; 2846 6,050 + 65s; 2991 5,250 + 70s (16,350 XP).
- Not counted: 6610 Clamlette Surprise (gate, 3,900), the run's kill XP.

## 9. Unverified / in-game test list; Needs pull; Unsure
Test list:
- The Zul'Farrak portal beside the Meeting Stone (Tanaris 38.5,20.7) and the ride times Gadgetzan - Steamwheedle Port - the Meeting Stone.
- Where the Scarabs are and how many (the DB has no positions); whether 14 kills covers 5 shells with the quest.
- The stairs event on Forever: the Executioner's Key, the cages, Bly's crew turning hostile, Nekrum and Sezz'ziz arriving.
- Gahz'rilla: what summons it on Forever (Mallet of Zul'Farrak has no source in the DB).
- Whether Wizzle offers 2770 without 2769, and Tran'rek 2865 without 2864 (row [27] read as breadcrumbs).
- The two Witch Doctor Zum'rah ids (7271 / 220076): which one stands in the dungeon.
- Whether the flight Feathermoon - Gadgetzan costs the raw 11s 60c.
Needs pull: Wowhead NPC page 7269 Scarab (map: count and place); item pages 9481 The Minotaur and 9479 Embrace of the Lycan (drop rates; not in the tooltip); item page 9240 Mallet of Zul'Farrak (source).
Unsure:
- U1 Whether chapter 46's spec takes 2865 when it hands in 2864; step 4 is written "if not in the log".
- U2 Where 2770 is picked up (D2): a pre-run ride from Gadgetzan to the Mirage Raceway and back, twice, for a quest that needs a mallet nobody on the route can get. Chapter 46's road passes Wizzle; an `[O]` pickup there (and 2769's hand-in, if the Ironforge pickup were earlier) would remove leg 3. The main session decides; this spec is written for both.
- U3 2769's pickup is in Ironforge (Klockmort 67.9,46.1), on chapter 48's or 49's pass, not here; whether those specs carry an `[O]` line is not known.
- U4 The Minotaur vs Rage of the Storm / Bigger Rock on the kill-speed model (Stormstrike, speed 3.20 vs 3.60 / 3.40) was not run; the linear call says "need".
- U5 3520's objective: quest row [9] says 5 of npc 8612, the text says 3 screechers (chapter 47's concern; here it is handed in complete).

## 10. Deviations from the route plan
- **D1** 2865 Scarab Shells: the plan labels it "normal (boss item, one kill)" and `_decisions.tsv` says "held by one mob or boss". The data says a collection: 5 Uncracked Scarab Shells (quest row [7]) from Scarab 7269, level 44-46, not elite (npc row [5] empty), 36.15%: budget about 14 kills. It stays **normal** (a trash collection over 30%, answer 4; rule 3's ~25-kill line not reached) with the budget on the kill line and an abandon line if short. No change in count or XP.
- **D2** 2770 Gahz'rilla: the plan does not say where it is picked up. It starts only at Wizzle Brassbolts (Thousand Needles 78.1,77.1; quest row [1] = [[4453]]), so in this chapter it costs a ride before the run as well as after; the spec makes that ride conditional on a group mallet (leg 3). Optional XP unchanged.
- **D3** 2769 The Brassbolts Brothers: its pickup is in Ironforge (quest row [1] = [[6169]], Klockmort Spannerspan 67.9,46.1), in an earlier chapter; only its hand-in can fall here. Unchanged count.
- **D4** Added `[O]` gate line for 6610 Clamlette Surprise at Dirge (Cooking 225), as the Threads allow; not counted.
- Totals: no deviation.
