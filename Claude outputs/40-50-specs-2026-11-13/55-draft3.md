# Spec 55 - Darnassus and Azshara (13 Nov 2026, from docs/40-50-plan-2026-11-12.md second revision)

Data used (all read in this session, 13 Nov 2026): tooling/qdb 1.0.16 (quest/npc/object/item.json), data/zone_16.json, zone_357/440/1657 (Wowhead XP and money, browser rows 12 Nov), data/wowhead_quest_links.json (pulled 12-13 Nov), data/browser/r2_pages*.tsv, data/drop_rates.json, tooling/client/1.60.1.70938 TaxiNodes/TaxiPath, weights/tooltips/2026-11-12.json scored with weights/score_items.py functions at --band 40 (central [conservative]), nether.wowhead.com/forever quest and item tooltips (read 13 Nov, 1 request/s). Coordinates are QuestieDB Forever spawns unless marked.

## 1. Header
- File: `55_Azshara.lua`
- Title: `[N 46-48 Azshara]` ; next: `[NX 47-49 Un'Goro Crater]` (plan's chapter 56 title) ; `[GA Alliance]`
- Description: "Darnassus and Rut'theran hand-ins, then Azshara from Talrendis Point: Loh'atu, Berdun and Truesong at 45, Saria Fairmoon's chain, Ekkal and Kim'jael at 47."
- Level in 46.5 (plan), out 47.5. Wants level 47 (nine pickups need 47: 88821, 88884, 88917, 89037, 3601, 86746, 89038, 89053, 89470; quest row [3] / Wowhead reqlevel).

## 2. Entry state
- Stands at Nijel's Point (Desolace) or the Maraudon door (end of chapter 54). Hearth: Gadgetzan (chapter 54, per the coordinator; not re-read from [S] tags, which do not exist yet for 54).
- Quests carried in, all complete:
  - 2972 Doling Justice (Jer'kai's Signet Ring 9368), 4267 Rise of the Silithid (Raschal's Report 11466), 2939 In Search of Knowledge - from chapter 50 (settled by the coordinator).
  - 162 Rise of the Silithid (Insect Analysis Report 8594), 3022 Handle With Care (A Carefully-packed Crate 9507) - from chapter 53.
  - 3449 Arcane Runes - picked up from Tymor in chapter 52 with the Drawing Kit (10445); the Standard Issue Flare Gun (10444) is the reward of 3451 Signal for Pickup (chapter 52, required; item row [5] = 3451, 3483). The objectives are done in this chapter.
- Professions: Dragonscale Leatherworking gate (5141) at Leatherworking 225. No shaman trainer on this route (plan Threads: chapters 53-56 pass none; the 46 and 48 rows wait for chapter 57).

## 3. Travel and hearth
- Flights (TaxiPath 70938, cost in copper): Nijel's Point (37) - Auberdine (26) direct, 530 (5s 30c); Auberdine - Rut'theran (27) direct, 0; Rut'theran - Auberdine 0; Auberdine - Astranaar (28) direct, 330 (3s 30c). Known: [P Nijel's Point] 33_Desolace.lua:16, [P Auberdine] and [P Rut'theran Village] 11_Darkshore.lua:18/21 (and 11s), [P Astranaar] 11t/12_Ashenvale.lua:21, [P Theramore] 32_Dustwallow.lua:28.
- Flight masters: Baritanas Skyriver 6706 Desolace 64.7,10.5; Caylais Moonfeather 3841 Darkshore 36.3,45.6; Vesprystus 3838 Teldrassil 58.4,94.0; Daelyshia 4267 Ashenvale 34.4,48.0.
- Rut'theran - Darnassus: the portal (not in the data; position unverified). Walk back through it to Rut'theran.
- Astranaar to Talrendis Point: ride east through Ashenvale into Azshara (road not in the data: unverified; Loh'atu's quest text puts Talrendis "on the border of Ashenvale").
- Talrendis Point: flight master Jarrodenus 12577 (Hippogryph Master, A) Azshara 11.9,77.6 - [P Talrendis Point] on arrival (new; TaxiNodes 64). Innkeeper: Berdun Cliffbrew 240482 (subName Innkeeper, A) 12.6,77.4 - he is also the quest giver.
- Talrendis links (TaxiPath): Auberdine 730, Astranaar 330, Theramore 630, Ratchet 730, Everlook and Talonbranch Glade (both unknown). No direct Talrendis - Gadgetzan path: chapter 56's flight is Talrendis - Theramore (630) - Gadgetzan (730), routed through Theramore (Gadgetzan known from chapter 46).
- Bind: **[S Talrendis Point] at Berdun** on arrival. Reasons: the chapter returns to Talrendis three times (the level-45 hand-ins, Ill Tidings, the conditional Truesong quests) and ends on Pilot Xiggs's island at the far south-east (77.8,91.4), from where the hearth brings him straight to Truesong; Gadgetzan has no use inside this chapter and chapter 56 flies there anyway (two hops). Astral Recall uses the same bind (separate cooldown; 22_ExcavationSite.lua:69 trains it) and covers the second return. Chapter 56 must rebind at Gadgetzan or Marshal's Refuge (carry out).

## 4. Route

### Leg 0 - level check (first line, [OC])
"This chapter wants level 47: nine Azshara pickups need it (Making Contact, Saria Fairmoon's chain, Ekkal, Kim'jael). Darnassus and the level-45 Talrendis quests come first (about 47,500 quest XP), which should make 47 on its own. If you are still 46 when the Talrendis quests are handed in, kill Spitelash Warriors and Screamers (46-48) and Mosshoof Runners (45-47) west of the Ruins of Eldarath until 47 before you take Making Contact. Mobs past Talrendis run 48-55: Warlord Krellian at the Ruins of Eldarath is 55, the giants on the south coast are 52-55 elites."

### Leg 1 - Rut'theran Village (zone 141, Teldrassil)
1. Fly Nijel's Point - Auberdine [TAR6706 Baritanas Skyriver] [G64.7,10.5 Desolace], then Auberdine - Rut'theran [TAR3841 Caylais Moonfeather] [G36.3,45.6 Darkshore].
2. Turn in 2939 In Search of Knowledge - 420 XP, 0 money - Daryn Lightwind 7907, Teldrassil 55.4,92.2 (Rut'theran). Prereq none.
3. Accept 2940 Feralas: A History from the book object 142958 "Feralas: A History", Teldrassil 55.2,91.5 (pre 2939). Turn in 2940 at Daryn Lightwind 55.4,92.2 - 420 XP.
4. Accept 2941 The Borrower - Daryn Lightwind 55.4,92.2 (pre 2940; req 42). Carried to chapter 56 (Curgle Cranklehop 7763, Tanaris 52.4,26.9). Counted in 56. Not taken afterwards: 2943 Return to Troyas, 2944 The Super Snapper FX (follow it).
5. Turn in 3022 Handle With Care - 2,100 XP, 50s - Erelas Ambersky 7916, Teldrassil 55.5,92.0 (Rut'theran).

### Leg 2 - Darnassus (zone 1657), all three NPCs in the Temple of the Moon
6. Through the portal to Darnassus (unverified position).
7. Turn in 2972 Doling Justice - 5,250 XP, 0 money - Tyrande Whisperwind 7999, Darnassus 39.1,81.6. Choice: see Gear (G1). Not taken: 3841 An Orphan Looking For a Home (given by Kindal Moonweaver in Feralas; round 3).
8. Turn in 4267 Rise of the Silithid - 405 XP - and 162 Rise of the Silithid - 5,700 XP - both Gracina Spiritmight 7740, Darnassus 41.8,85.6. Not taken: 4493 March of the Silithid (req 50), 4510.
9. Accept 98096 Sisters In Duty - Sentinel Dalia Sunblade 8396, Darnassus 39.6,89.5. Wowhead side "None", reqlevel 45, QuestieDB race mask Alliance (Human, Dwarf, NightElf, Gnome); the giver is faction A in npc row [12]: plain.
10. Back through the portal; fly Rut'theran - Auberdine [TAR3838 Vesprystus] [G58.4,94.0 Teldrassil], Auberdine - Astranaar [TAR3841 Caylais Moonfeather] [G36.3,45.6 Darkshore].
11. Ride east to Talrendis Point (unverified road). [P Talrendis Point] at Jarrodenus 12577 [G11.9,77.6 Azshara]. [S] bind at Berdun Cliffbrew 240482 [G12.6,77.4 Azshara].

### Leg 3 - Talrendis Point pickups (zone 16; all req 45)
12. Turn in 98096 Sisters In Duty - 420 XP - Commander Truesong 239822, Azshara 11.8,78.4.
13. Accept 88807 Slay the Spitelash - Truesong 11.8,78.4.
14. Accept 5535 Spiritual Unrest and 5536 A Land Filled with Hatred - Loh'atu 11548, Azshara 11.4,78.2.
15. Accept 89001 Home on the Range, 89013 Gettin' Buzzed, 89228 Winter Frontier Fishery - Berdun Cliffbrew 240482, 12.6,77.4. 89013 gives Berdun's Pellet Gun (item 238501, no source in qdb; the quest text names it): [UI 238501] unverified.

### Leg 4 - north of Talrendis, mobs 45-47 (lowest first)
16. 5535 Spiritual Unrest (4,200 XP, 50s): kill 6 Highborne Apparition 6116 (L45-46, 11 spawns, 14-17,69-74) and 6 Highborne Lichling 6117 (L46-47, 10 spawns, 13-17,67-73) [G16.2,70.5 Azshara]. Counts from quest text (row [7]).
17. 89001 Home on the Range (4,400 XP, 0) - FILL, required: 5 Mosshoof Hide 238463 from Mosshoof Runner 8759 (L45-47, 29 spawns, 16-23,46-71, one at 12.7,75.3): 45% per mob (81 of 180, Wowhead item page 12 Nov; overall 29.2% includes Coursers) - "budget ~11 kills". Do not hunt the Coursers 8761 (L52-53, 27/190) or Stags 8760. Kill line: "Kill [TAR8759 Mosshoof Runner] for 5 Mosshoof Hide [QC89001] (~45% - budget ~11 kills)". Runners are spread along the whole west strip: kill them through legs 4-6.
18. 5536 A Land Filled with Hatred (4,200 XP, 70s): kill 6 Haldarr Satyr 6125 (L45-46), 2 Haldarr Trickster 6126 (L45-47), 2 Haldarr Felsworn 6127 (L46-47) at the Haldarr Encampment [G20.3,61.8 Azshara].
19. 88857 Saving a Sentinel (4,200 XP, 50s; req 45): accept from Sentinel Keldara Sunblade 222478 (L45) in the encampment, Azshara 20.6,61.9 (the Classic Keldara 8397, L43, also stands there: target 222478). Escort her out (objective text only; nothing in row [9]); hand-in Truesong. Not sharable (Wowhead).
20. 89013 Gettin' Buzzed (4,400 XP, 0): 5 Wild Honey 238503 from Honey Wasp 236028 (L47-49, ~55 spawns, 15-19,49-60) [G17.5,54.5 Azshara]: 60.27% single dropper (tooltip 12 Nov) - plain, "budget ~9 kills". Text says shoot Wasp Nests with the Pellet Gun; whether the nests spawn the wasps is unverified.
21. 88807 Slay the Spitelash (4,400 XP, 70s): kill 8 Spitelash Warrior 6190 (L46-47, 28 spawns) and 8 Spitelash Screamer 6193 (L47-48, 23 spawns) [G30.0,55.0 Azshara] (26-34,50-61).
22. 89228 Winter Frontier Fishery (4,400 XP, 70s): fish 10 Raw Winter Squid (item 13755; Forever tooltip name "Raw Winter Squid", qdb "Winter Squid") - no source in the data: where it bites and the skill needed are unverified (route fishing toward 200 by chapter 38, cap 225). Suggested line: fish the coast by the Spitelash leg; `[CI13755,10]`-held step. See Unsure U2.
23. Ride back to Talrendis. Turn in 5535, 5536 (Loh'atu 11.4,78.2); 88857, 88807 (Truesong 11.8,78.4); 89001, 89013, 89228 (Berdun 12.6,77.4). Gettin' Buzzed fixed rewards: Berdun's Trusty Rifle, Recipe: Potion of Beast Slaying, Potion of Beast Slaying (vendor the rifle and recipe).
   Level-45 XP so far: Darnassus 14,295 + 33,170 (minus Arcane Runes, handed in later) = 44,915; at the 65% share that is about 69k total XP against 61.6k from 46.5 to 47 (XP_TO_LEVEL 46 = 123,200): 47 expected here.

### Leg 5 - level 47 pickups at Talrendis, then east (mobs 48-52)
24. [OC] level line: "Level 47 now? If not, Spitelash at 30,55 until 47, then come back."
25. Accept 88821 Making Contact (req 47) - Truesong 11.8,78.4. Not taken: 92345 Beneath Nordrassil (round 3), 88809 Preserving Eldarath (out). Conditional: [O] "if Truesong offers 88812 Reclaiming Ravencrest (req 47), take it" - see conditional block.
26. 3449 Arcane Runes objectives: rubbings with the Drawing Kit on the four rune objects - Rune of Beth'Amara 149481 (36.9,53.2), Rune of Jin'yael 149480 (39.6,50.2), Rune of Markri 149482 (39.4,55.5), Rune of Sael'hai 149483 (42.4,64.2), Azshara. Hold each with [CI10563,1] / [CI10564,1] / [CI10565,1] / [CI10566,1] (rubbing items). Mobs: Spitelash Serpent Guard 6194 (L48-49), Siren 6195 (L50-52), Myrmidon 6196 (L50-51), Lingering Highborne 7864 (L48-50). **Warlord Krellian 8408 (L55, not elite in qdb; Wowhead 8 spawn points 40.4-41.6,52.4-53.8) stands between Jin'yael and Markri: pull around him.** Hand-in later (leg 9).
27. Accept 86746 The Legashi Threat (req 47 Wowhead; qdb none) - Ekkal 235903 (L50, AH) Azshara 42.0,38.9, on the way north-east. Wowhead side Alliance, sharable.
28. Turn in 88821 Making Contact - 490 XP - Saria Fairmoon 239831, Azshara 50.6,42.7 (Shattered Strand). Accept 88917 Slithering Looters. Saria's quests are a Wowhead series 88821 > 88917 > 88884 > 89037 > 89038 > 89053 with no prerequisites in qdb: write "if she offers more than one, take them all"; the route below works with one at a time.

### Leg 6 - Ruins of Eldarath (mobs 48-52)
29. 88917 Slithering Looters (5,100 XP, 0; req 47): requirements (Forever tooltip 13 Nov): Staff of Archmage Selwyn (238347) AND Lady Sesspira's Key (238345). Kill Lady Sesspira 239942 (L52, classification 0 = Normal on Wowhead; 45 spawn points in qdb, 12 on Wowhead, 34-38,48-57) [G36.5,53.0 Azshara] - key 37.5% of 16 sampled kills (data/drop_rates.json): plan override "one kill, kill her again if it does not drop - she gates the rest of Saria Fairmoon's chain". Then the staff from object 524759 (not in object.json: position "among the Ruins of Eldarath" only). Hold with [CI238345,1] and [CI238347,1]. Also there: Lord Sarthiss 239939 (L52). Turn in at Saria 50.6,42.7; accept 88884 Highborne Tablets.

### Leg 7 - Highborne Tablets (south; positions not in the data)
30. 88884 Highborne Tablets (5,100 XP): Tablet of Creation 238244 (obj 524260), Tablet of Manipulation 238245 (obj 524284), Tablet of Power 238246 (obj 524298) "among the ruins of Southridge Beach". None of the three objects is in qdb: Needs pull. The south coast around 44-61,69-90 holds Cliff Walker 6148 (L52-53 elite), Cliff Thunderer 6147 (L53-54 elite), Cliff Breaker 6146 (L54-55 elite), Thunderhead Patriarch/Consort (L52-54), Coursers (52-53): over him; avoid the giants. [CI] per tablet. Turn in at Saria; accept 89037 Murloc Thieves.

### Leg 8 - north and east (mobs 51-53)
31. Accept 3601 Kim'jael Indeed! (req 47) - Kim'jael 8420 (AH) Azshara 53.5,21.8. Collect Kim'Jael's Compass 10717, Scope 10715, Stuffed Chicken 10722, Wizzlegoober 10718 from Kim'jael's Equipment objects 153123 (15 spawns, 56-57,28-30, Thalassian Base Camp) [G56.5,28.8 Azshara]; Blood Elf Surveyor 6198 (L51-52), Reclaimer 6199 (L52-53), Magister Hawkhelm 246991 (L53) around. [CI] per item. Turn in at Kim'jael - 6,550 XP, 8s; fixed reward M73 Frag Grenade 10830. Not taken: 5534 (out, Some Rune 4.0%).
32. 86746 The Legashi Threat (5,250 XP, 80s): kill 5 Legashi Satyr 6200 (L51-52), 5 Legashi Rogue 6201 (L51-53), 5 Legashi Hellcaller 6202 (L52-53) [G62.5,21.5 Azshara] (60-67,16-25). Higher Legashi beside them (Soulstealer 236867, Hellraiser 236874 L53-54) are not objectives.
33. 89037 Murloc Thieves (5,100 XP): Memory Crystal 238385 from Razorgill 239971 (L52, 17 spawn points 87-90,29-34, near the Tower of Eldara) [G88.4,31.5 Azshara]: 100% single dropper (tooltip 12 Nov) - plain. Around: Storm Bay Warrior 6371 / Tidecaller 239966 (L51-52), Wavethrasher 6348, Makrinni Scrabbler 6370 (L52-53), Coralshell Lurker 6352 (L53-54).
34. Back west: turn in 86746 at Ekkal 42.0,38.9 - 5,250 XP, 80s. Turn in 89037 at Saria 50.6,42.7 - 5,100 XP; choice: Gear G2. Accept 89038 A Monumental Task.

### Leg 9 - Ravencrest Monument, Saria's end, Xiggs
35. 89038 A Monumental Task (5,650 XP, 40s): Mark of the Queen 238517 from object 525677 "among the ruins of the Ravencrest Monument" - object not in qdb: Needs pull. [CI238517,1]. Turn in at Saria; accept 89053 Your Final Reward.
36. 89053 Your Final Reward (5,650 XP, 0): "See what Saria has to show you"; ends at the object Saria's Knapsack 527828, Azshara 49.4,41.9 (qdb and Wowhead end "Object #527828"). Choice: Gear G3. Accept 89470 Ill Tidings from the same knapsack object (Wowhead start Object #527828).
37. 3449 Arcane Runes hand-in: swim to the small island off the southern peninsula and use the Standard Issue Flare Gun (10444; [UI10444], unverified tag) to signal Pilot Xiggs Fuselighter 8392 (AH), Azshara 77.8,91.4 - 2,550 XP, 0. **Mammoth Shark 12125 (L54 elite) swims at 78-80,91-95; Great Wavethrasher (L53-54) and Makrinni Razorclaw (L54-55) on the shore.** Accept 3461 Return to Tymor (from Xiggs; carried to chapter 57).
38. Hearth (bound at Talrendis). Turn in 89470 Ill Tidings - 2,800 XP, 85s - Truesong 11.8,78.4. [O] conditional Truesong hand-ins if taken.
39. Chapter ends at Talrendis Point; chapter 56 flies Talrendis - Theramore - Gadgetzan.

### Conditional / optional lines (never counted; plan's optional list)
- 5141 Dragonscale Leatherworking (4,200 XP, req 40; skill 165 at 225, quest row [17]) [O] gate "only at Leatherworking 225": Peter Galen 7866 (A, "Master Dragonscale Leatherworker") Azshara 37.6,65.4, among Mosshoof Coursers (52-53); pass him on the way from Talrendis to the Eldarath runes. Needs 2 Tough Scorpid Breastplate 8203, 2 Tough Scorpid Gloves 8204 (crafted; patterns 8395/8398 drop from Wastewander Bandit 5618 / Thief 5616 in Tanaris, no rate read), 10 Worn Dragonscale 8165 (1.7% over 29 dragonkin, none on this route). Exclusive with 5143/5144 (row [15]). His trainer list on Wowhead is empty (trainer_costs.json 12 Nov). Rule 11 gate; fires only if he has the items.
- 88812 Reclaiming Ravencrest (5,650 XP, 85s; req 47): [O] "if Truesong offers it" (series 88809 > 88812 > 88813; 88809 out). Kill 5 Spitelash Battlemaster, 5 Spitelash Enchantress, nullify 3 Naga Power Stones near the Ravencrest Monument (tooltip). Not sharable.
- 88813 The Head of the Serpent (5,650 XP; req 47): [O] "if offered after 88812": Krellian's Head 238057 from Warlord Krellian 8408 (L55; 100%). Eight levels over him: "only at 50+ or with a group". Gear G4.
- 86747 Legashi Horns (530 XP): no giver; 5 Severed Legashi Horn (tooltip); ends Ekkal 42.0,38.9: [O] "if a horn starts it while you kill Legashi".
- 90813 Pay Dirt! (6,550 XP; req 50): Humongous Crystal 243203 from Cliff Walker 6148 (L52-53 elite, no rate); ends Berdun. Req 50: cannot be accepted this round; line only if the crystal drops and he is 50.
- Ursolan furbolgs (Wowhead side None, not in QuestieDB; givers with no faction): [O] "if they offer it to Alliance" for each.
  - Furze/Bramblesnap series 86799 > 86804 > 86925 > 86926 > 86927 > 86812 > 86813: 86799 Encroaching Corruption (Furze 235909, 43-47,21-23 -> Elder Bramblesnap 235906, 42.1,20.9 / 43.3,20.3) 530; 86804 An Unlikely Source (Bramblesnap -> obj 506307, "Legashi Firewater in the Legashi Encampment") 3,950; 86925 Toil and Trouble (obj 506307; Legashi Firewater Recipe from satyr) 5,250; 86926 Felfire Burn, Cauldron Bubble (5 Satyrweed + a Fel Mote to the Legashi Cauldron) 5,250; 86927 Running Firewater (to Bramblesnap) 5,250, reward Recipe: Distilled Firewater (Alchemy 250); 86812 Transmuted Tincture (tincture on 3 Mosshoof Coursers or Thunderhead Skystormers) 3,950, reward Manual: Powerful Poultice (First Aid 280); 86813 Potential Panacea (panacea to Furze) 2,650, choice G5.
  - Ekkal/Rageroar/Korsa: 86752 Report to Rageroar (Ekkal -> Gatekeeper Rageroar 236573, no spawn) 530 > 86791 Missing Blackmaw Scouts (Rageroar -> Korsa 236770, 61.6-63.3,20.6-23.6) 530; series 86777 > 86792 > 86796 > 86797 > 86798 > 87346 > 86814 > 92065: 86777 Master Feardred (kill Master Feardred 236496 L53, his amulet) 5,250, G6; 86792 Thinning Their Forces (6 Legashi Hellraiser, 4 Soulstealer, 2 Blackguard) 5,450, 40s; 86796 Later, Satyr (Graal 237007, no spawn; escort out of Legashi Stronghold) 5,450, 60s; 86797 Return to Rageroar 530; 87346 Chieftain Bloodmaw 5,650 and 86814 Blackmaw Counter-Offensive 7,050 (GROUP on the pool flag): **both start at Gorn One Eye 11555 in Felwood 65.2,2.7** (Wowhead start n11555) - see Deviation D1.
  - Area mobs: Timbermaw / Blackmaw Shaman and Ursa L50-52 around Ursolan; Blackmaw Thrall 250023 L55-57 elite near the base camp.

## 5. Gear calls (level-40 band, tooltips 2026-11-12.json, central [conservative])
- G1 2972 Doling Justice: Nightscale Girdle 10706 (mail waist +14 Str +2 Sta) 28.0 [28.0] over Firwillow Wristbands 10705 (cloth wrist +2 Agi +10 Int) 19.1 [19.1]. Neither is a clear upgrade: Firwillow loses to the Arathi Armbands (round 1, leather wrist +7 Str +5 Agi = 19.6 computed); the girdle ties or loses to Twilight Initiate's Belt 29.8 (chapter 43) and Vinehedge Cinch 28.0 (chapter 50), beats the Violet Sash (27.2 computed). Line: "take the Nightscale Girdle: wear it only if your belt scores under 28; the Elunar Belt later in this chapter replaces it either way" (also the better vendor, 55s 21c vs 36s 66c).
- G2 89037 Murloc Thieves: Elunar Belt 260182 (leather waist +11 Spi +13 SP) 53.5 [29.5] over Scout's Dagger 260180 (1H dagger 31.1 dps +6 Str +6 Agi, 454.3, shield set only); Sentinel's Plate is plate. Replaces his waist (Twilight Initiate's Belt 29.8 or the girdle).
- G3 89053 Your Final Reward: Staff of Archmage Selwyn 260207 (2H staff 31.6 dps +16 Sta +16 Int +48 SP) 565.4 [517.4]. Wear only if the two-hander scores under it (Rage of the Storm 529.8 linear per the weights doc, Resurgence Rod 551.1, Staff of Lore 519.6). Bigger Rock on Bigger Stick 604.5 (chapter 43) and Bonebiter 583.5 beat it: then take Highborne Research Tablet 260205 (trinket, chance on hit 69-81 Arcane, double on naga and satyrs; the model does not score procs - Unsure U4). Highborne Memory Crystal 260201 is an off-hand (unusable in the 2H build).
- Fixed rewards: 89013 Berdun's Trusty Rifle 290333 (gun, unusable; sells 1g 53s 26c), Recipe: Potion of Beast Slaying 250999 (Alchemy 280; sells 25s), Potion of Beast Slaying 250955; 3601 M73 Frag Grenade 10830.
- Conditional: G4 88813 Truesong's Hammer 260209 (1H mace 32.9 dps +10 Str, 480.0, shield set only) over Prelate's Orb 260208 (off-hand) - take the hammer to sell (3g 1s 44c). G6 86777 Rageroar's Best Club 260166 (2H mace 40.3 dps +15 Str +15 Spi) 631.7 [616.7]: beats Bigger Rock 604.5 - wear it; runner-up Feardred's Cleansed Amulet 259892 (neck) 38.0. G5 86813 Amice of Sorrow 260169 (cloth shoulder +14 Int +9 SP) 41.7 [32.7] over Timbermaw Prayer Beads 260171 (neck +10 Agi +5 Spi) 23.7 and Mourner's Shroud 260168 (back +7 Str +9 Sta) 14.0, if his shoulder is under 41.7. 86814 Hippogryph Hide Boots 260185 (mail feet) 52.0 - unreachable (D1).

## 6. Out (silent; reasons from _decisions.tsv)
- 5534 Kim'jael's "Missing" Equipment: drop under 30%: Some Rune 4.0%.
- 88809 Preserving Eldarath: drop under 30%: Eldarath Relic 14.4%.
- 3381 A Meeting with the Master: no giver in the DB or on Wowhead.
- 3421 Return Trip, 3503 Meeting with the Master: no XP, nothing kept behind it.
- 92345 Beneath Nordrassil: LATER (round 3; ends in Darnassus after Azshara).
- Darnassus: 3841 An Orphan Looking For a Home (round 3), 4493 March of the Silithid (req 50), 4510, the Morrowgrain chain (round 3), 5091 (req 50), 2944 The Super Snapper FX (not in the plan).
- 89015 Deadliest Catch (Berdun, req 50, Mammoth Shark elite) and 97327 Blackmaw Pouches (Ekkal, level 60, Blackmaw Hold) are not in the plan's pool list: no tag.

## 7. End check
Log at the end: 2941 The Borrower (to 56), 3461 Return to Tymor (to 57). Conditionals possibly open: 88812/88813 (hand in at Truesong before flying; if 88813 is not done, [QS] abandon), furbolg quests if taken (finish or [QS]), 86747 if started. Everything else of the chapter handed in. Hearth: Talrendis Point. Flight points new: Talrendis Point.

## 8. Totals
Required 24 quests, 89,155 XP, 5g 73s (2972 5,250; 162 5,700; 4267 405; 2939 420; 2940 420; 3022 2,100 / 50s; 5535 4,200 / 50s; 5536 4,200 / 70s; 88857 4,200 / 50s; 98096 420; 88807 4,400 / 70s; 89001 4,400; 89013 4,400; 89228 4,400 / 70s; 3449 2,550; 88821 490; 88884 5,100; 88917 5,100; 89037 5,100; 3601 6,550 / 8s; 86746 5,250 / 80s; 89038 5,650 / 40s; 89053 5,650; 89470 2,800 / 85s) - equals the plan row. Optional 79,850 XP (the plan's 20 lines, summed) - equals the plan row; 12,700 of it (87346, 86814) cannot fire on this route (D1), and 90813's 6,550 cannot be accepted before 50.

## 9. Unverified / in-game test list; Needs pull; Unsure
Test list: the Rut'theran portal position; Astranaar - Talrendis road; Talrendis Point flight master and bind work as the data says; whether Saria Fairmoon offers her quests one at a time; the Pellet Gun and the wasp nests; where Raw Winter Squid bites and the Fishing skill it needs; Xiggs appears on the flare at 77.8,91.4; the Ursolan furbolgs offer to Alliance; Lady Sesspira's key rate; Krellian's patrol versus the runes; the Talrendis - Theramore - Gadgetzan flight.
Needs pull: positions of objects 524260, 524284, 524298 (tablets, Southridge Beach), 524759 (the staff's container, Ruins of Eldarath), 525677 (Mark of the Queen, Ravencrest Monument), 506307 (Legashi cauldron/object); spawns of Gatekeeper Rageroar 236573, Graal 237007, Lorekeeper Nok 249853; drop source of Raw Winter Squid 13755.
Unsure:
- U1 Gorn One Eye chains (87346, 86814): giver in Felwood; keep as listed-only or remove the two lines?
- U2 89228 Winter Frontier Fishery is required in the plan but its item has no source in the data (rule 5 says fishing stops are [O]): keep plain with a "[QS] if no squid bites" fallback, or make it [O]?
- U3 Lady Sesspira: rule 12 says a named mob's 30-60% item is "one kill only, then abandon"; the plan's override says kill again because the chain hangs on her. Written to the override.
- U4 89053 pick when he wields Bigger Rock: the trinket's proc is unscored.
- U5 Gear on entry (waist, wrist, two-hander) depends on chapters 43-54 picks; the calls are written as conditions.

## 10. Deviations from the route plan
- D1 87346 Chieftain Bloodmaw and 86814 Blackmaw Counter-Offensive start at Gorn One Eye 11555 in Felwood 65.2,2.7 (data/wowhead_quest_links.json start n11555; npc row [6] zone 361). The plan lists them with the Ursolan givers. No chapter of round 2 visits Felwood: they get no step here (proposal), XP left in the optional total.
- D2 88917 needs the key itself in the bags (tooltip requirement "Lady Sesspira's Key"), not only to open a chest; the step holds both items.
- D3 3449 Arcane Runes is handed in on Xiggs's island at the far south-east and gives 3461; the plan places the 45-level quests first, but the runes stand among level 48-52 Spitelash next to Krellian (55), so the rubbings are made in the level-47 leg and the hand-in closes the chapter. The quest stays counted here.
- D4 The plan says Talrendis Point "flight point not known": confirmed; it is a direct link to Astranaar, Auberdine and Theramore, not to Gadgetzan (chapter 56's flight goes through Theramore).
