# 30-60 round 1 - chapter spec list for approval (11 Nov 2026)

Round A of the Phase 3 build (`docs/30-60-build-plan-2026-11-11.md`). No guide file has been written. The seventeen specs are in this folder (`27.md` ... `41.md`), drafted by Opus subagents from the route plan and checked against the data; each spec's sections 4 (route) and 9 (unverified) are the detail behind the lines below. Braedyn approves this list, with the decisions in the next section, before any chapter is written.

## Level curve from the specs (plain quest XP at a 65% quest share, pre-2.3 XP table)

| chapter | plain XP | optional XP | plain money | level after, plain only | level after, with every optional | note |
|---|---|---|---|---|---|---|
| 27 Hillsbrad / Alterac | 17,300 | 0 | 1g 50s | 31.5 | 31.5 | three targets are level 37-40 |
| 28 [O] City of Dalaran | - | 15,800 | - | 31.5 | 32.0 | |
| 29 Arathi Highlands | 14,550 | 10,650 | 0 | 32.0 | 32.7 | optional = three GROUP quests |
| 30 Stranglethorn north | 37,530 | 3,150 | 18s | 33.0 | 33.8 | optional = Colonel Kurzen GROUP |
| 31 Booty Bay / Faldir's Cove | 19,260 | 14,185 | 66s | 33.5 | 34.6 | the cove needs level 35 |
| 31b [O] The Drowned City | - | 20,350 | - | 33.5 | 35.1 | entrance not in any data file |
| 32 Dustwallow Marsh | 35,650 | 0 | 1g 70s | 34.4 | 35.9 | |
| 33 Desolace | 46,050 | 0 | 3g 05s | 35.5 | 36.9 | |
| 34 [O] Scarlet Monastery | - | 12,650 | - | 35.5 | 37.2 | |
| 35 Badlands | 37,140 | 0 | 64s | 36.4 | 37.9 | |
| 36 [O] Uldaman | - | up to 25,485 | - | 36.4 | 38.4 | |
| 37 Swamp of Sorrows | 24,900 | 0 | 1g 03s | 36.9 | 38.9 | |
| 38 Riverglades I | 78,385 | 3,300 | 1g 40s | 38.5 | 40.4 | quest levels 36-41 |
| 39 Level 40 | 18,450 | 3,900 | 1g 10s | 38.8 | 40.7 | triggered by the ding |
| 34b [O] Razorfen Downs | - | 16,385 | - | 38.8 | 41.0 | proposed on chapter 39's Barrens leg |
| 40 Riverglades II | 48,085 | 4,300 | 30s | 39.7 | 41.9 | quest levels 42-46 |
| 41 Powderfuse Port | 42,245 | 3,150 | 2g 55s | 40.4 | 42.6 | quest levels 38-45 |
| **total** | **419,545** | **133,305** | **14g 11s** | | | route plan said 505k plain |

Plain quests alone end the round at about 40.4 and reach 40 only in chapter 41; with the optional chapters the curve is the route plan's. The route plan's table was high because its script counted quests the text had ruled out, dungeon quests and two quests 1-30 already does, and because elite targets and level gates were not read (logged in `lessons.md`). Shimmering Flats was sized as a filler and is not worth it: about 11,000 XP is plain under the drop rule.

## Decisions for Braedyn

1. **The level gap.** Recommended: every chapter opens with a level-check line ("wants level N; if under, run the optional chapter before it"), the level-40 Alterac targets (537 Dark Council, 522 / 523 Baron's Demise, 551 / 554 the Parchment) move from 27 to chapter 39's Alterac leg, and Faldir's Cove (663-669) is conditional on level 35 in 31 and otherwise rides to chapter 39's Arathi stop with 670 / 667. Alternatives: count 30-60% drop quests as plain with a budget in chapters 27-37 (about 30,000 XP back), or leave it as specced.
2. **A Booty Bay hop in chapter 37** (Darkshire flight, he is already there): the Bloodsail chain 595 > 597 > 599 > 604 (needs level 37; 9,320 XP plain), Tokal's 79236 and 79242's pickup (Traveled Gloves, +15 over Seawolf), and `[O]` 608 the three captains for the Blackwater Cap. Recommended: yes. It is not in any spec yet.
3. **Elite quests become `[O]` GROUP** (rule: elites get the optional test): 685 Otto and Falconcrest (Arathi Armbands), 684 Marez Cowl (Wild Headdress, one kill), 202 Colonel Kurzen (Dark Hearted Hammer, only if he holds no Defender of Dalaran), 95991 Ghostmaw (only if his legs score under 31), 762 Infernus inside the Uldaman chapter. 92867 Ground to Keep: the Old Leather Jacket is +0.9 to +1.4 over what he wears; recommended out. 193 / 197 / 208 (Bhag'thera, Tethis, Bangalash): out, rewards are no upgrade.
   **Added after the specs were written** (Wowhead NPC pages, `wowhead_maps_20261111.txt`; QuestieDB leaves these ranks blank, so the specs list the quests as plain): Snargl is a level 40 elite (94679 Snargl's Snout, 3,150), Chogg'Zac a level 41 elite (95562 Cut Off the Heads, 3,300), Overlord Kilgar a level 46 elite (94890 Bring Me His Head, 5,050, and 94891 News to Farholde, 4,050, behind it), Komuk a level 45 elite (94926 Drop the Hammer, 4,850; its reward is plate), Old Rot-Chum a level 42 elite (95120, 4,300; its reward is a polearm), Scaldaron a level 43 rare elite (decision 6). Under the rule as written these six become `[O]` GROUP or drop out, which takes about 24,700 XP off the plain total and ends the round near 39.9 on plain quests. **The question for Braedyn: is an elite at or below his own level a plain step with a warning, or always GROUP?**
4. **Field Marshal's Log** (1.6% drop-start from the Sunnyglade cultists; it gates 94885 > 94887 > 94892 > 94893, 13,650 XP). Recommended: one conditional line "if the Log drops while you do Saving Sunnyglade", XP not counted.
5. **A Fur Trade** (8 Prized Lion Hides at 48%, about 17 kills, 3,000 XP) is XP-only by the optional test, but it opens Friz Frazzlespark's Powderfuse chain (94928, 95288, 95293, 95294: 5,945 XP more). Recommended: keep as `[O]` with the budget.
6. **Hail the Dragonslayer** (4,450 XP + 1g 20s; Scaldaron's head 7 of 29 kills on Wowhead, a thin sample; level 43). Recommended: conditional, one kill only.
7. **Razorfen Downs moves to chapter 39's Barrens / Thousand Needles leg** (Myriam Moonsinger stands on the road he takes for Heed My Call; 3636 needs level 39). Recommended: yes, as `39b`.
8. **Hearth sequence**: Southshore (27, kept through 31b), Theramore (32), Nijel's Point (33), Thelsamar (35), Farholde Keep (38). Booty Bay is not bound; Nethergarde has no inn in the data.
9. **Drowned City (31b)**: no entrance position in QuestieDB, the client taxi table or the Wowhead pages read so far. Recommended: write the pickups and hand-ins, hold the dungeon legs until the entrance is known (in game, or a source I find before round B).
10. **Imbue line in chapter 39**: the spec follows your 11 Nov decision (Windfury Weapon from 30, rank 2 at 40 as a must). The weights doc still says Rockbiter; confirm and I record it there.
11. **Mount money**: plain quest money for the whole round is 14g 11s (the route plan said 18.5g by 40). Veron Amberstill lists each ram at 20g and at 40g on top of the 100g riding skill (raw Wowhead values; Honored is 94g 74s, not 90g). The "Gold break" note at the end of 37 quotes these.
12. **1-30 fixes** (round C): Elemental Aid 2,650 -> 3,300 at 25:68 and 26:85. Camp Tent at 02:59 and Heavy Linen at 02:68 quote 1s where Wowhead now reads 1s 5c: both wait for an in-game price.

## What changes against the route plan without needing a decision
- Out by the drop rule on the 11 Nov rates: 2418 Power Stones (11%), 2500 Badlands Reagent Run (24% / 28% / 11%) and 17 Uldaman Reagent Run behind it, 94842 Unsavory Plant Food (22%), 94881 Curious Trinkets (25.5%), 95913, 95984 with 95986, 95988 with 95957 and 95975, 94829 with 94858 (6.6%), 94961 / 94963 (16.5%), 95261 (12.5%), 95326 (20%), 512 (11%), 79624 (8.3%), 98233, 1204 / 1258 (the crawlers for 1258 spawn only in the Swamp).
- Out by a gate: Nat Pagle 6609 / 6607 (Fishing 225) and with it every "fish Nat's fish here" note; 6625 Alliance Trauma (First Aid 225); 1139 Lost Tablets of Will (needs a second Uldaman run); 79365 (Horde side); 95219 (Feralas delivery).
- Already done in 1-30: 659, 555, 95161.
- Added: 1050 pickup in Ironforge (was not carried), 510 Foreboding Plans, 95786 An Acquaintance in Southshore (Brother Nimetz to Loremaster Dibbs, 3,150 XP), 97328 Anything of Value in chapter 30 (object source), 1219 / 1220 in Dustwallow, 79229 Highway Robbery in Desolace, 1392 Noboru the Cudgel in the Swamp (cudgel 34 of 38 kills), 94929 Swamp breadcrumb into the Riverglades, 95315 Arathi breadcrumb (picked up in 39), 2439 for the Thawpelt Sack in Uldaman, 3523 / 3525 in Razorfen Downs, 95789 / 95791 in the Drowned City, chapter 41.
- Travel: chapter 32 enters by Stormwind, Menethil and the Theramore boat (the Missing Diplomat and Hyal pickups are on that line); chapter 33 enters by Astranaar and the Charred Vale road (Nijel's Point is undiscovered); chapter 34 runs from Nijel's Point by the Auberdine boat and includes a Dalaran crater stop; chapter 35 starts at Ironforge when 34 is run.
- Gear corrections: Servomechanic Sledgehammer needs Engineering 100; Pauldron of Order is plate and Rot-Covered Harpoon a polearm (not usable); Dwarven Charge loses to Rock Pulverizer; Thermaplugg's Left Arm (478.8) beats the Defender of Dalaran (469.8) if he has it. `score_items` does not exclude plate: fixed before round B.
- Trainers: Farseer Maret Firetend at Aerie Peak trains shamans (Wowhead now lists 163 spells at Eldrun's prices, no Ghost Wolf).

## Still to pull or settle before round B
- Wowhead map positions for about thirty Riverglades mobs and ground objects (running).
- The Drowned City entrance; the source of The Lost Magic of the Runemasters (96800) and of The Coldbringer's Eye (96773); 97328's prerequisite.
- A reconciliation pass over the specs for the decisions above (hearths, moved quests, the chapter 37 hop, 95315 in 39), done by the main session before any writer starts.

## Per-chapter extracts
(Sections 8 Totals, 6 Out, 5 Gear calls and 10 Deviations of each spec, verbatim.)

### Spec 27 - Hillsbrad / Alterac 31-33 (drafted 11 Nov 2026)
**Totals**
- Plain quests completed in the chapter: 10 - 564 2,700; 511 1,350; 510 1,350; 514 1,350; 525 1,350; 537 3,150; 522 710; 523 3,900; 551 780; 92432 660 = **17,300 XP**.
- Quest money: 537 50s + 523 1g = **1g 50s** (zone_36 money field; all others 0).
- [O] XP: 95534 2,800 (+40s) if the note drops.
- Pickups carried out worth later: 554 1,550 (+50s), 707 710, 1453 1,300, 1050 3,550, 96800 2,850 (+45s), 98463 265, 95787 3,150, 95788 3,150, 95798 2,350 (+35s), 92457/92458 3,950 each.
- 1-30 running money at end of 26: 17g 05s (brief) -> 18g 55s after 27.
**Out**
- 6609 I Got Nothin' Left! - quest.json row [3] req 35 and [17] requiredSkill = [356, 225] (Fishing 225; he has 127); 6607 Nat Pagle has the same gate ([17] = [356, 225], req 35): Artisan Fishing chain out of round 1 (main-session correction 11 Nov).
- 6625 Alliance Trauma - row [3] req 35 and [17] = [129, 225] (First Aid 225; he was 76 on 9 Nov): cannot be taken at 31-33; round 2 (Triage), not the Ironforge loop.
- 500 Crushridge Bounty - Dirty Knucklebones 2843: Crushridge Ogre 575/2455 = 23.4%, Brute 318/1513 = 21.0% (drop_rates.json) - under 30%, out; 504 Crushridge Warmongers (pre [500], also 15 ELITE L39-40 Warmongers) out with it.
- 512 Noble Deaths - 7 Alterac Signet Rings (3505) from Syndicate L35-39 (multi-dropper, no rate in drop_rates.json); reward is XP + 40s only, so 30-60% would be an XP-only [O] = out; plain only if the pulled rate is >= 60% (Needs pull). 510 does not need it.
- 565 Bartolo's Yeti Fur Cloak - route plan: yeti fur 7%; also an [O] in 23.
- 659 / 658 / 657 / 660 / 661 Hints of a New Plague? - 659 done in 1-30 (brief); the rest is chapter 29.
- 555 Soothing Turtle Bisque - done in 23 (brief).
- 647 MacKreel's Moonshine - starts at Foggy MacKreel (2696) Arathi 43.2,92.6, ends Bilger in Southshore (3,050 XP + 55s, req 28): not in the route plan; belongs to chapter 29 (Arathi) if anywhere - flagged to the main session.
- 98459 A Lack of Virtue - quest level 21 (grey at 31), 165 XP, delivery to Menethil; skipped in 23 already.
- 510/512 Syndicate - see above; 1712/1713/1714/1791/1792 Cyclonian chain (side 3, Bath'rah; Classic shaman/warrior-era "Whirlwind Weapon" chain - qdb 1791 needs 1719, not on the route); 79362/79363 (reqclass 64 + Horde races 162); 6681/6701/96779/96781/96782/96783/96786 (reqclass 8 = rogue); 7042/7043/79482/79484 (Winter Veil); 8374/8384/8391-8408/7081-8385 (battlegrounds); 99193/99194 (donations, level 40/60); 80411/80453-80526, 8233-8249, 82110, 84880/84881 (req 44-55); 81944, 7645, 99326 (req 40+).
- 97130 / 96773 - not out, but not here (req 34): see Deviations.
**Gear calls**
- **564 Costly Menace** (choice): Shepherd's Gloves (leather +7 Str +6 Agi) **19.7 | 19.7** over Shepherd's Girdle (leather +7 Sta +7 SP) 14.0 | 7.0. Neither beats his likely gloves/belt: Zodiac Gloves 24.1 (chapter 17/20 pick), Operator's Gloves 22.0 (chapter 25); belts Daewyn's Girdle 29.0 (25), Demolition Girdle 34.0, Moss Cinch 24.0. Line: "take Shepherd's Gloves only if your gloves score lower (Naga Battle Gloves 18.0, Wolfclaw 15.7, Gold-flecked 14.0); else vendor". Fixed: Recipe: Tasty Lion Steak + one steak.
- **95534 Strahnbrad Mystery** [O] (fixed): Brilliant Cloak (+5 Sta +5 Int +6 SP) **20.2 | 14.2**. Upgrade over Golem War Cloak 12.0, Yeti Fur Cloak 11.7, Cloak of the Faith 10.0, Excavation Cloak 8.0, Watch Master's Cloak 0.0; NOT over Glowing Thresher Cape 26.0, Explorer's League Dustcover 25.5, Repairman's Cape 21.4.
- 537, 523, 551, 510, 511, 514, 525, 92432: no item rewards (zone_36/267 itemchoices empty).
- Pickups whose rewards come later (for the later specs): 96800 Salve and Salvation (held off-hand, unusable for 2H) / Knucklebound Thimble (ring +8 Sta, 0.0); 95798 Apprentice Sorcerer's Slacks 73.3 | 48.4 over Rune-Etched Epaulets 10.4; 1050 Explorers' League Commendation 22.5 | 13.5 (below Giantstone Medallion / Thermaplugg Medal 25.0).
**Deviations from the route plan**
- 659 removed (done in 1-30, brief); 555 removed (done in 23, brief); plan listed both.
- 6609 and 6625 moved out of the Ironforge loop: both req 35 with skill 225 ([17] = [356,225] / [129,225]); 6609 out of round 1 (main-session correction); 6625 to round 2.
- 1050 added to the Ironforge loop (plan said carried; no `[QA1050` in 00-26).
- **97130 and 96773 are req 34** (qdb row [3], Wowhead r34): they cannot be picked up at 31-33. Proposals: pick up both at the end of chapter 28 if he is 34 (Timear 16.2,71.7 and Lan'dalock 15.9,73.1 are 12 units south of Modera); otherwise on the chapter-34 Dalaran pass. 31b (The Drowned City) comes before 34, so 97130 is only available to 31b if chapter 28 is run at 34 - the main session may want 31b after 34, or 97130 dropped from 31b.
- 92457/92458 are picked up here but their XP counts in chapter 28 (the plan's 27 total of 34,600 counted them, 659, 554 and the dungeon pair); this spec's 27 plain XP is **17,300**, money 1g 50s (plan 3.00g) - the 65% level estimate for 27 drops accordingly (main session re-runs route_xp).
- 522's contract is from the Shadowy Assassin (npc 2434, 90.91%, one spawn in Southshore), not "Syndicate at Strahnbrad".
- 510 Foreboding Plans added (same object as 511, free 1,350 XP delivery); 512 behind it out pending the ring rate.
- 98463 Talk of the Town pickup added here (plan's chapter 31 says it is carried from Southshore's Barkeep Kelly, but 27 did not list the pickup).
- 96800, 95787, 95788, 95798 pickups placed (plan: 27 picks them up). Hand-ins: 96800 at Olvek and 95798 at Abra Cadabra need a later Dalaran visit - proposal: chapter 34's trip north (Southshore -> Alterac -> Tirisfal) stops at Dalaran.
- 554 is carried out to the next Ironforge stop (the plan had it handed in inside 27's Ironforge loop, which is impossible: 551 needs the Ruins of Alterac chest and 537 needs the Ironforge leg first).

### Spec 28 - [O] City of Dalaran (dungeon chapter, 32-34) (drafted 11 Nov 2026)
**Totals**
- In the chapter: 92457 3,950 + 92458 3,950 = 7,900 XP, no money; 92459 265 if offered.
- With the Stormwind hand-ins: + 92456 3,950 + 92489 3,950 (+1g) = **15,800 XP, 1g**. (Route plan said 16,460 incl. 92432's 660, which is handed in in 27.)
**Out**
- 96984 Heart of Disruption, 96986 The Grave Knight, 96987 Opportunistic Education, 96988 Source of Power - zone_16544 side 2 (Horde).
- 92434 Blood in the Streets, 97287 Shrewd Negotiations - Horde races only (qinfo).
- Nothing Alliance in zone 16544 is left out.
**Gear calls**
- **92458** (choice): **Defender of Dalaran** 2H mace 31.21 dps +9 Str +13 Sta +9 Int **469.8** over Renewing Footpads (leather +5 Sta +11 Int, +4 SP) 26.1 | 22.1 and Spellguard Pauldrons (mail, 40+). Defender beats Heavehammer 420.2, Manual Crowd Pummeler 442.8, Corpsemaker 435.3, Slaghammer 354.5; it **loses to Thermaplugg's Left Arm 478.8** (2H axe 31.3 dps +17 Str +5 Sta +4 Int, req 31, Gnomeregan roll). Line: "Defender of Dalaran unless you won Thermaplugg's Left Arm; then Renewing Footpads (26.1, beats Disjointed Shoes 22.0 and Lancer Boots 14.8)". Bonebiter (583.5, chapter 34) and Rage of the Storm (529.8, chapter 39) replace it later.
- **92489** (choice, Stormwind hand-in): Violet Sash (cloth waist +9 Int +6 SP) **26.9 | 20.9** over Runebound Gloves (leather +7 Sta +4 Spi +12 AP) 22.0 | 18.0. Sash beats Moss Cinch 24.0 and Shepherd's Girdle 14.0, not Daewyn's Girdle 29.0 / Demolition Girdle 34.0 / Blightleaf Rope 30.5; Runebound beats Shepherd's Gloves 19.7 / Naga Battle Gloves 18.0, not Zodiac 24.1 / Operator's 22.0 (tie). Line: "Violet Sash if your belt scores under 26.9, else Runebound Gloves if your gloves score under 22; else the higher sell price".
- **92457** (choice): Fallen Guard's Pendant (neck +3 Str, +7 Arcane res) 6.0 vs Arcane Infused Rod (held off-hand; unusable with a 2H). Vendor either (sell 31s 70c / 31s 82c).
- **92456** (choice, Stormwind hand-in): Vine Pruner's Cloak (+6 Sta +5 SP) 10.0 | 5.0 vs Thorn Protecting Girdle (mail, 40+). Cloak only over Excavation Cloak 8.0 / Dwarven Guard Cloak 0.9 / plainer; else vendor.
- 92459: no reward in zone_36.
**Deviations from the route plan**
- 92432 hand-in moved to chapter 27 (Modera is the 27 pickup point for 92457/92458), so its 660 XP is not in 28.
- 92458 labelled grind/luck (plan: all normal) - Wowhead 40.75% for the Mote.
- Plan's "Defender of Dalaran is the weapon until Bonebiter" holds unless he has Thermaplugg's Left Arm (478.8 vs 469.8, band 30).
- Plan's gear list quoted Renewing Footpads 26.6 and Violet Sash 27.2; this run gives 26.1 and 26.9 (band-30 weights, 11 Nov tooltips).
- Added: 92459 Friend of the Kirin Tor (conditional), boss-loot calls (new tooltips), req-34 pickups 97130/96773 (conditional), Stormwind hand-in placement.

### Spec: chapter 29 Arathi Highlands 32-34 (drafted 11 Nov 2026)
**Totals**
- Plain hand-ins: 6 (681, 658, 657, 660, 661, 92872) + 1 pickup (79358, XP in 39).
- Plain XP: 2,500 + 2,800 + 0 (657 blank) + 2,850 + 3,550 + 2,850 = **14,550** (11,700 if 92872 goes out).
- `[O]` XP: 685 3,900 + 684 3,750 + 92867 3,000 = **10,650** (+45s from 92867).
- Quest money plain: **0** (681, 658-661, 92872 all 0 in zone_45/zone_267). Optional: 45s. Vendor: Lightstep Leggings 44s 42c if sold. Spend: Expert Leatherworking 50s if the detour runs.
**Out**
- 682 Stromgarde Badges - drop rule: Stromgarde Badge 13% (route plan); nothing requires 682.
- 691 Worth Its Weight in Gold and 693-697 (Skuerto chain) - drop rule (tusks 8%, pouch 11%, knife 7.5%, route plan); 693 needs 691.
- 635/642/651/652/653 Myzrael chain, 687 - out per chapter 27's plan section (motes 30% + Fozruk elite; 687 needs 653+688).
- 79624 Anyone Can Cook - drop-start from Illegible Recipe 213422 (Boulderfist Ogre 2562 L32-33 x31-38 y40-50, Enforcer 2564 L33-34, Brute 2566, Magus 2567 in the south-east, plus the Stromgarde elites 2569-2571 per item row; rate not pulled). Ends at Skonk (217300) 57.4,74.4. 1,550 XP, 0 money, **no item reward** in zone_45 (itemchoices and itemrewards empty) and none in qdb; Skonk then offers 79677 A Quick Grocery Run (3,150; Hybrid Haunch from Wild Gryphons/Granistad/Kurdros L40, which are friendly, + Smuggler's Spice Blend with no source) and 79678 Taste Testing (3,150; Shawarmageddon 213105, a one-hand mace 22.1 dps - useless for 2H). No recipe anywhere in the chain = XP-only = out by the optional-step test, whatever the rate. Outcome if the Wowhead quest page shows a food-thread recipe reward: `[O]` pickup on the Boulderfist Ogres/Enforcers at 31-38,40-50 (between Refuge Pointe and Northfold, on the route): plain kill-line budget if rate >= 60%, `[O]` "drop quest, ~1/rate kills" at 30-60%, out below 30%; hand-in Skonk 57.4,74.4 (a ~20-unit detour south-east of Refuge Pointe).
- 92867 Ground to Keep - out if Lomar's spawn cannot be found (see Leg 4b).
- 95315 The Riverglades Report - req 36 (he is 32-33): not available; Captain Nials gives it later (chapter 39's Arathi visit or the Riverglades chapter's opening - main session).
- 636 Legends of the Earth - Wowhead "<NYI>", no starter/ender.
- 662-670 Faldir's Cove - chapter 31.
- 79975/79976 (Sleeping Bag chain Arathi steps) - not reachable yet (79192 first hands in at Stonetalon); placed in a later chapter.
**Gear calls**
What he likely wears (from 1-30 picks): head Defender's Leather Helm 24.0 [24.0] (13:38 / 26:60), or from the optional RFK run Whisperwind Headdress 41.5 [23.5] / Geomancer Headdress 43.0 [25.0]; chest Snapbrook Armor 30.5 [21.5] (21:56), Raptorbane Armor 31.0 [31.0] counting its +15 AP vs beasts (16.0 otherwise; 18:66), or a crafted Totemic Leather Armor 28.9 [23.9]; wrist Bands of Serra'kis 12.0 (20:10 names it) or Staghide Armguards 2.8 / Demonhide Bracers 9.8; legs Triprunner Dungarees 23.1 (24:96).
- **685 Otto and Falconcrest** -> Arathi Armbands (leather wrist +7 Str +5 Agi) 18.8 [18.8]; runners-up not usable: War Rider Bracers (mail, 40+), Rod of Sorrow (wand). Replaces Bands of Serra'kis (+6.8). Vendor values: Arathi Armbands sell 30s 62c.
- **684 Marez Cowl** -> Wild Headdress (leather head +11 Int +12 SP) 42.1 [30.1]; runner-up Arcane Runed Bracers (cloth wrist +1 Sta +9 SP) 18.0 [9.0] (below Arathi Armbands); Stromgarde Bracers mail. Replaces Defender's Leather Helm (+18.1 / +6.1). Over Whisperwind +0.6 / +6.6; Geomancer keeps the slot on central (43.0 vs 42.1), Wild Headdress wins conservative (30.1 vs 25.0). Line: "take it unless you wear the Geomancer Headdress".
- **92867 Ground to Keep** -> Old Leather Jacket (leather chest +15 Str +2 Agi +2 Sta) 31.9 [31.9]; runner-up Stromgarde Hood (cloth head +8 Sta, +110 armor, +0.5% hit) 0.0 in score_items (it does not read hit); with the band-30 hit value (8.63 per 1%, forever-enh-stat-weights.md table) it is 4.3 - never an upgrade. Jacket over Snapbrook +1.4 [+10.4], over Raptorbane +0.9 [+0.9] (beast AP counted) or +15.9 vs non-beasts, over Totemic Leather Armor +3.0 [+8.0]. A marginal upgrade - see Unsure.
- **661 Hints of a New Plague?** -> neither is an upgrade: Dustfall Robes (cloth chest +8 Sta +13 SP) 26.0 [13.0] < Snapbrook 30.5; Lightstep Leggings (leather legs +13 Agi +5 Sta) 12.3 [12.3] < Triprunner Dungarees 23.1. Take **Lightstep Leggings to sell** (sell 44s 42c vs Dustfall 35s 41c).
- 79358, 658, 657, 660, 681, 92872: no item reward (zone_45 itemchoices/itemrewards empty).
**Deviations from the route plan**
1. **685 Otto and Falconcrest: plain -> `[O]` GROUP 3+** (qdb: Otto 2599 L38 rank 1 elite, Falconcrest 2597 L40 rank 1 elite, surrounded by Syndicate elites 35-39; optional-step test kept it for Arathi Armbands +6.8).
2. **92867 Ground to Keep: plain -> `[O]` GROUP 3+, and out unless Lomar is located** (all four kill targets rank 1 elite 35-38; starter npc 219 absent from qdb; Old Leather Jacket +0.9-1.4; Stromgarde Hood never an upgrade).
3. **92872 Dutiful Steps: plain but conditional** on the throw spot (Faldir's Cove guess); out if the spot is behind the Boulderfist elite camp (no reward, XP-only).
4. **79358 XP is not counted here** (3,600 + 60s paid at the chapter-39 hand-in); the plan's 8 plain / 21,450 XP / 0.45g becomes 6 plain / 14,550 XP / 0 money (the 45s was 92867's).
5. **79192 / Thoradin's Wall is not visited**: the plan's carried list says "chapter 29 visits it", but qdb chains 79192 -> 79980 -> 79974 (Stonetalon) -> 79975 (Loch Modan dam) before the Arathi Messenger Bag (79975 ends there; 79976 starts there). The Arathi step belongs after Stonetalon and the dam - chapter 39's Arathi visit is the natural place (main session).
6. **658 rate is 78.02% (Forever tooltip)**, not "Classic 100%, unverified": plain stands, with a 4-bodyguard warning.
7. **Hearth: Southshore used for 661**; the plan says "hearth stays Southshore" - consistent; no bind in 29.
8. **Aerie Peak road given from Hillsbrad**, not "east out of Arathi" (the Arathi road passes Hammerfall's L50 guards); the detour sits after the 661 hand-in in Southshore.
9. **Maret Firetend**: no `[T]` step (Wowhead list empty), test line only.

### Spec 30 - Stranglethorn north 33-35 (drafted 11 Nov 2026)
**Totals**
- Plain quests (20): 583 245; 185 1,250; 186 1,300; 187 2,050; 188 2,850; 190 1,250; 191 1,300; 192 2,150; 194 1,350; 195 1,400; 215 1,300; 200 1,350; 328 1,400; 329 1,400; 330 285; 331 2,850; 203 1,950; 204 2,700; 574 2,850; 207 3,550 = **34,780 XP**, quest money **0** (all 0 in data/zone_33.json money).
- Conditional plain (N1): 97328 Anything of Value 2,750 XP + **18s** (1800c).
- [O]: 202 Colonel Kurzen 3,150 XP (GROUP 2+, gear-conditional).
- Vendor spend: [O] recipes 50s + 30s. Vendor income from rewards (Cleaver 63s 96c if not the Mantle, Pauldrons 38s 4c, Scepter 83s 84c, Tiger Gloves 21s 36c if not worn) ~1g 50s-2g 7s of sale value (tooltip sell prices).
- Plan table said 26 quests / 48,025 / 0.32g; the difference is D1-D4.
**Out**
- 193 Panther Mastery (Bhag'thera, 40 ELITE, 3,150): optional-step test, elite quest whose only reward (Panther Hunter Leggings 9.5) is no upgrade -> XP-only -> out.
- 196 Raptor Mastery (Jungle Stalker 687, 40-41, 2,450): mobs 6-7 levels above him at 34-35; and it only leads to 197. Round 2 (STV 40-45 leftovers) - deviation D1.
- 197 Raptor Mastery (Tethis, 43 ELITE, 3,600): optional-step test, Raptor Hunter Tunic 10.8 no upgrade -> out.
- 208 Big Game Hunter (King Bangalash 43 ELITE, 88.5%, 5,350): optional-step test, rewards are bow/rifle/wand/sword (none usable) -> XP-only -> out; also needs 193 + 197 (pre(all) 188, 193, 197), both out.
- 198 Supplies to Private Thorsen (640 + 16s): starts at Krazek in Booty Bay (qdb start 773, 26.9,77.2) and ends at Thorsen in the north; cannot be taken on a Duskwood entry. Left to chapter 31 (it is a north trip from Booty Bay: recommend out there).
- 201 Investigate the Camp (255 + 16s): **starts and ends at Krazek in Booty Bay** (qdb start/end 773; nether tooltip requirements "Rethban Caverns" + "Locate the hunters' camp"). It cannot be carried out of 30: it must be picked up in Booty Bay first, then the Nesingwary camp visited. Left to chapter 31 (recommend out: a 255-XP return north).
- 205 Troll Witchery (Skullsplitter Fetish 2466 at 19.3%) and 206 Mai'Zoth behind it (needs 202 + 205): drop rule, under 30% -> out with the chain.
- 97047 The Cook in the Cage (Compound Cage Key 216616 at 8.9%) and 97048 Returning to Port behind it: drop rule -> out.
- 338 The Green Hills of Stranglethorn and 339-342 Chapter I-IV: random page collection, XP-only (plan) -> out.
- 189 Bloodscalp Ears (17%) and 209 Skullsplitter Tusks behind it (19%, req 37): drop rule -> out.
- 210 Krazek's Cookery (Corporal Kaleb, Rebel Camp) -> 627 -> 622: needs a Mining node item (plan; he dropped Mining) -> out.
- 97329 Where's the Key? (Primitive Key 1%) -> 97331 Zimmix's Great Escape -> 97332 (req 36): drop rule -> out.
- 97420 Reduce, Reuse, Reconcile (drum 1.6%), 95384 Partial Mystical Notes (8.4%): drop rule -> out.
- 349 Stranglethorn Fever (gorilla fang 46%, XP blank on Wowhead) and 348 behind it (req 40): plan out.
- 93928 Of Mice and Milk (Westfall mouse -> Hemet, 105 XP): not picked up in 1-30 (no [QA93928] in 00-26) -> out.
- 93443 Lost Shipping Crate (req 36, object with no spawn), 97405 Noise Complaints (req 38), 95786 An Acquaintance in Southshore (starter unknown): not in this chapter's window; 95786 is listed under chapter 31's out in the plan.
- 78830/78823 Terror of the Desert Skies (Hunter / Badlands drop-start), 79731 (Priest), 5762/5763 (Thousand Needles / Horde) end at Hemet: not ours.
- **Left to chapter 31 (Booty Bay / south)**: 575 Supply and Demand -> 577 -> 628 Excelsior, 213 Hostile Takeover, 605/600, 616 The Haunted Isle -> 578 -> 601 -> 602 -> 603 -> 610 -> 611 (Stone of the Tides, [O]), 595/597/599/604/608 Bloodsail chain, 606/607/609/613, 617/623, 621, 587, 576, 1181/1182, 98463 Talk of the Town (if carried), 198 and 201 (above), 1041 The Caravan Road (Ruzzgot, Booty Bay; needs 1040), 2904 A Fine Mess (if he kept it from 24 - Scooty, Booty Bay).
**Gear calls**
- **188 Tiger Mastery (fixed): Tiger Hunter Gloves** (leather hands +7 Str +8 Agi) 21.6 [21.6]. Worn: Operator's Gloves 22.0 [18.0] (25_LooseEnds30.lua:14), or Shepherd's Gloves 19.7 [19.7] (564, chapter 27), or Runebound Gloves 22.0 [18.0] (28, optional). Line: wear them only over Shepherd's Gloves or worse (a -0.4 side-grade against Operator's/Runebound on central, +3.6 on conservative); else vendor (sell 21s 36c).
- **204 Bad Medicine (choice): Palm Frond Mantle** (cloth shoulder +7 Int +6 Spi) 26.5 [20.5] vs **Guerrilla Cleaver** (1H axe 17.68 dps +3 Agi +4 Sta, 1H - shield set only) 250.4. Worn shoulders: Mantle of Honor 29.0 [22.0] (17_Duskwood2.lua:97) or Faerie Mantle 24.9 [18.9] (21_AshenvaleEast.lua:75). Line: take the Mantle only over Faerie Mantle or a plainer shoulder; with Mantle of Honor take the Cleaver to vendor (63s 96c against the Mantle's 18s 75c).
- **331 Report to Doren (choice): Junglewalker Sandals** (cloth feet +8 Sta +5 Int +2 Spi) 13.2 [11.2] vs **Frost Metal Pauldrons** (mail shoulder +11 Sta; mail, not wearable until 40 and scores 0 at band 40 too). Worn feet: Disjointed Shoes 22.0 [17.0] (16_RedridgeEastvale.lua:58) or Totemic Leather Boots 20.0, or Renewing Footpads 26.1 (28). Line: no upgrade; take the Pauldrons to vendor (sell 38s 4c vs the Sandals' 27s 49c).
- **328 The Hidden Key (fixed): Bookmaker's Scepter** (1H mace 13.04 dps +6 Int +30 SP) 252.5 - 1H, vendor (83s 84c).
- **[O] 202 Colonel Kurzen (choice): Dark Hearted Hammer** (2H mace 88-132, 3.80, 28.95 dps, +12 Str +8 Sta) 429.3 vs Madman's Blade (1H dagger 14.74 dps +7 Spi +32 SP, 287.9 - 1H) and Shrapnel Blaster (gun - shaman can't use). Worn 2H: Defender of Dalaran 469.8 (28) > Manual Crowd Pummeler ~442.8 (Gnomeregan, from the guide line) > **Dark Hearted Hammer 429.3** > Heavehammer 420.2 (24) > Ironwood Destroyer (22.2 dps). Pick: the Hammer either way (if not wielded it is the best sale: 1g 35s 30c vs Madman's 1g 8s 49c).
- Not taken (out): 193 Panther Hunter Leggings (leather legs +10 Agi +11 Sta) 9.5 vs worn Carnage Trousers 13.2 (19_Wetlands2.lua:48) / Totemic Leather Pants 38.6; 197 Raptor Hunter Tunic (+4 Str +3 Agi +16 Sta) 10.8 vs worn Raptorbane Armor 31.0 (18_Wetlands1.lua:66) / Snapbrook Armor 30.5; 208 Master Hunter's Bow / Rifle / Wand / Spellsword (2H sword 507.0 but a sword - shaman can't use); 97048 Kurzen Headshrinker's Cinch 10.0, Crusty Cuffs 12.5, Jailer's Discarded Chain (mail).
**Deviations from the route plan**
- D1 **196 Raptor Mastery dropped to round 2**: Jungle Stalker 687 is level 40-41 (qdb npc row [3]/[4]) at 28.9,44.9; he is 34-35 here. Plan had it plain.
- D2 **193 and 197 out** (plan had them plain): Bhag'thera 728 and Tethis 730 are ELITE (qdb npc row [5] = 1, level 40 and 43); the brief's rule "elite and group quests get the same test" removes them because Panther Hunter Leggings (9.5) and Raptor Hunter Tunic (10.8) are not upgrades. **208 out** (plan had it [O] GROUP 2+ as "group finale"): the test allows no XP-only optional, all four rewards are unusable, and it needs 193 + 197.
- D3 **97328 Anything of Value** moved from chapter 31's plain list into this chapter's Leg 5 (its starter object 661516 and the Zul'Kunda shipments are in the north at 31.6,12.9 / x22-27 y8-14); hand-in at Lozgil at the end of 30 (or 31). Conditional on N1.
- D4 **198 and 201 cannot be in 30**: both start at Krazek in Booty Bay (qdb 773). Plan listed them in 30 ("201 Krazek hand-in in 31"). Left to 31, where both need a return north - recommended out (895 XP + 32s together).
- D5 **202 Colonel Kurzen is [O] GROUP 2+** (plan: plain): Colonel Kurzen 813 is 39-40 ELITE; the test keeps it only for the Dark Hearted Hammer when he has no better 2H.
- D6 Plan said "Roast Raptor (Nerrist, Booty Bay / Corporal Bluth)": Nerrist 1148 stands at 32.7,29.2 (Grom'gol, Horde); the Alliance seller is Corporal Bluth 734 (Rebel Camp), who also sells Recipe: Jungle Stew 12231. Both need Cooking 175 (tooltips 11 Nov).
- D7 Plan said "hearth stays Southshore until 31" - unchanged; plan's entry "Darkshire flight, the road south" - unchanged.

### Spec: chapter 31 Booty Bay and Faldir's Cove 35-36 (drafted 11 Nov 2026)
**Totals**
- Plain quests (8): 201 (255), 98463 (265), 663 (690), 664 (3,150), 665 (3,150), 666 (3,900), 668 (1,550), 669 (3,150) = **16,110 XP**; money **16s** (201). 670 is accepted here, counted in 39.
- `[O]`: Stone of the Tides 616 (285) + 578 (2,850) + 601 (2,850) + 602 (1,400) + 603 (1,400) + 610 (2,250) + 611 (3,150) = **14,185 XP, 80s** (578 40s, 601 40s); carried-only hand-ins 97328 (2,750, 18s), 2904 (2,450).
- Spending: Expert Fishing book 1g (plain); Eldrun level 36 3g (sheet musts/buys); optional Cooked Glossy Mightfish 1g 60s, Rockscale Cod 22s.
- The route plan's table had 17 plain / 42,625 XP / 1.38g for this chapter; the gap is the Bloodsail chain (req 37: 14,170 XP + 40s) and the quests that failed the optional test (Deviation 13).
**Out**
Faldir's Cove (Arathi 45; 667 and 670 belong to chapter 39):
- 662 Deep Sea Salvage (3,150): optional-step test - XP-only (reward Black Water Hammer, 1H mace; the build is 2H); four wreck objects at 20-23,84-86 under water.
Booty Bay / southern Stranglethorn (re-checked against `data/drop_rates.json`, 11 Nov):
- 595 > 597 > 599 > 604 > 608 The Bloodsail Buccaneers: **req 37** (qdb row [3] = 37, Wowhead reqlevel 37) - above this chapter (35-36). Moved, not dropped: Deviation 2.
- 587 Up to Snuff: Snuff 25.6% overall (multi-dropper) < 30, also req 37 and behind 597.
- 576 Keep An Eye Out: Dizzy's Eye 2.0%.
- 605 Singing Blue Shards: 37.1% would be `[O]`, but no item reward (35s) -> optional-step test XP-only; 600 Venture Company Mining behind it 29.5% < 30 (Silver Spade 459.5 was its prize).
- 213 Hostile Takeover: Tumbled Crystal 31.6% -> `[O]` by rate, but Gemmed Gloves 27.1 | 22.1 against Seawolf Gloves 24.9 | 24.9 that 664 gives plain in this chapter = +2.2 central / -2.8 conservative; Geologists are in northern Stranglethorn (x28-48 y7-24, ~55 units from Booty Bay). Fails the optional-step test (Deviation 4).
- 575 > 577 > 628 Supply and Demand / Some Assembly Required / Excelsior: 577 needs **575** (2 Large River Crocolisk Skins, 35.7% single-dropper tooltip 4053, River Crocolisks north at x32-41 y8-14), which the plan missed; 575 and 577 both start at Drizzlik in Booty Bay, so it is three Booty Bay <-> north-river round trips; 577 Snapjaw skins 34.7% (~15 kills, x38-42 y15-33), 628 Elder Saltwater Crocolisk is ELITE level 38 (4 spawns), 73.3%. Excelsior Boots 22.5 | 22.5 is below Renewing Footpads 26.1 (28 [O]) and only beats Junglewalker Sandals 13.2 (30). Out on the optional-step test plus travel (Deviation 5).
- 621 Zanzil's Secret: Zanzil's Mixture 30.9% -> `[O]` by rate, but Belt of Corruption 14.8 < Violet Sash 26.9 (28); mobs level 43-44. Test fails.
- 606 Scaring Shaky (Mistvale Giblets 27.9%) and 607 > 609 > 613 behind it (Maury's Key 4.7%).
- 617 > 623 Akiris by the Bundle: Akiris Reed 29.1%; req 38.
- 1116 Dream Dust in the Swamp: needs 1115 (Shimmering Flats chain, not on the route); dust 30.4%.
- 1127 Fool's Stout: needs 1122 (same chain).
- 97329 Where's the Key?: Primitive Key 0.9%; 97331 Zimmix's Great Escape behind it; 97332 Twice Misplaced Trust (req 36, Lozgil -> Powderfuse Port delivery; Wowhead series after 97331) goes with them.
- 97405 Noise Complaints: req 38, four Mosh'Ogg ELITE kill sets (level 41-44), starter unknown.
- 93443 Lost Shipping Crate: object start with no spawn, a Powderfuse Port delivery (round 2).
- 189 Bloodscalp Ears (16.7%) and 209 Skullsplitter Tusks (19.1%): start at Kebok in town; out (plan placed them in 30).
- 624 > 625 Cortello's Riddle: drop-start item 4056, req 35, ends in the Swamp/Dustwallow; XP-only chain.
- 348/349 Stranglethorn Fever: plan's call (chapter 30).
- 95776 The Only Good Brinescale..., 95775 The Drowned City, 96774 Ancient Gurubashi Idol: Horde (Wowhead side 2).
Pool reconciliation (`pool30.py L28-41 33`, 82 quests): the rest are northern Stranglethorn (Nesingwary 185-197/208, Rebel Camp 198/200-207/215/328-331/574, 338-342, 210/627/622, 95384, 97047/97048, 97420) = chapter 30. Arathi pool (`pool30.py L28-41 45`): 662-670 handled above; the other Arathi quests are chapters 29/39.
**Gear calls**
- 664 Seawolf Gloves (fixed) 24.9 | 24.9 -> wear; replaces Tiger Hunter Gloves 21.6 (30) / Runebound Gloves 22.0 (28 [O]) / Shepherd's Gloves 19.7 (27).
- 666 vendor both: Servomechanic Sledgehammer needs Engineering (100) (tooltip text); Gnomish Zapper is a wand. Sell the Sledgehammer (1g 48s 87c).
- 611 [O] Robe of Crystal Waters 39.0 | 30.0 over Tidal Bracers 14.8 | 14.8 and Undertow Legguards (mail 40+; 23.7); replaces Dustfall Robes 26.0 (29).
- 2904 [O] none usable as an upgrade: Fairywing Mantle 17.9 < Palm Frond Mantle 26.5 (30); Technician's Bracers 14.6 < Arathi Armbands 18.8 (29); Fire-welded Bracers mail. Vendor (16s 30c).
- For the record (not in this chapter): 608 Blackwater Cap 40.0 (head) < Saltseer's Helm 48.3 (31b) and ~ Wild Headdress 42.1 (29 [O]); 79242 Traveled Gloves 40.0 | 29.0 would beat Seawolf Gloves 24.9 by 15; 667 (chapter 39) Coldwater Ring 27.4 > Tiger Band 22.5.
**Deviations from the route plan**
1. **Order: Booty Bay first, cove second, Booty Bay last** (plan: cove first). Data: cove quests req 35 (qdb [3]); plan XP table puts him at 33.9 after 30; Booty Bay FP undiscovered and he is already in Stranglethorn; 669 ends in Booty Bay.
2. **Bloodsail chain 595 > 597 > 599 > 604 > 608 moved out**: req 37 on every step (qdb row [3] = 37; Wowhead reqlevel 37). Proposal: a Booty Bay side hop in chapter 37 (Swamp of Sorrows, 39-40, which flies to Darkshire; Darkshire - Booty Bay is a direct link) or round 2's "STV 40-45 leftovers". 608's Blackwater Cap 40.0 is no longer an upgrade over Saltseer's Helm 48.3 / Wild Headdress 42.1.
3. **Tokal's 79236 Cherry for Your Thoughts? / 79242 No Honor Among Thieves cannot be in 31**: 79235 starts at Bibbly F'utzbuckle in Desolace (62.3,39.0, chapter 33) and ends at Tokal (27.0,77.3 Booty Bay). First chapter after 33 that can pass Booty Bay: **37** (Darkshire -> Booty Bay hop); 79236 needs a Cherry Grog (item 4600, vendors Barkeep Kelly 2366 and Nixxrax Fillamug 2832 per qdb; sell 85c -> 3s 40c), and 79242's cache (object 418855) is at 94.1,69.3 Arathi = chapter 39's Arathi visit. 79242 pays 3,900 + 1g and Traveled Gloves 40.0 (+15 over Seawolf Gloves). Recommend bundling it with Deviation 2's side hop in 37; else round 2.
4. **213 Hostile Takeover out** (plan `[O]`): Gemmed Gloves 27.1 | 22.1 vs Seawolf Gloves 24.9 | 24.9 from 664 in this chapter; Geologists 55 units north.
5. **577 > 628 out** (plan `[O]`): prerequisite 575 Supply and Demand was missing from the plan (qdb 577 row [12] = [575]); three round trips north; Excelsior Boots 22.5 < Renewing Footpads 26.1; 628's crocolisk is a level-38 elite.
6. **666's Servomechanic Sledgehammer is not a prize**: tooltip "Requires Engineering (100)". The plan listed it as "2H 423".
7. **97328 Anything of Value is chapter 30's pickup**: start object 661516 at 31.6,12.9 and the shipments at Zul'Kunda (north); 31 only hands in at Lozgil.
8. **Hearth: keep Southshore, no Booty Bay bind** (plan and brief: bind Booty Bay). Data: after 31 the next stops are 31b's hand-ins at Loremaster Dibbs (Southshore 50.6,57.1; Wowhead 95787/95788 end n2277) and Alterac (Abra Cadabra 12.1,70.3, Timear 16.2,71.7), and chapter 32's quickest way in from the Eastern Kingdoms is Southshore -> Menethil (direct link) -> Theramore boat. A Booty Bay bind is never used again. Main session's call; the bind line is ready if kept.
9. **Two Drowned City quests found that the plan did not list**: 95789 Shady Saltseers and 95791 The Saltseer Captain (Krazek, Booty Bay; req 34; 3,900 XP each, 95789 +1g; Wowhead side null, qdb race mask none = both factions). Picked up in Leg D for 31b.
10. **97130 is picked up here, not in chapter 27**: req 34 (qdb [3], Wowhead reqlevel 34) - chapter 27 runs 31-33.
11. **Cooked Glossy Mightfish (+30 AP, Cooking 225, 1g 60s at Kelsey Yance)** - a food-thread candidate the plan does not mention (RULES 5 thread ends at Mithril Head Trout +20 AP). Listed `[O]`; Braedyn's call whether the thread changes.
12. **Shaman trainer stop added** on the Refuge Pointe -> Ironforge -> Booty Bay flight (level-36 ranks, 3g of sheet buys); the next Ironforge pass is chapter 35.
13. **Plain XP 16,110 instead of 42,625** (see Totals); with the optional chain 30,295. 31b adds 20,350 (optional).
14. **98463 Talk of the Town** is not "carried" (chapter 23 skipped it); it is picked up in this chapter's Southshore leg if chapter 27 did not.
15. Plan's Nerrist "Booty Bay" (professions thread) is wrong: Nerrist 1148 spawns at 32.7,29.2 (Grom'gol, Horde). Not used here.

### Spec: chapter 31b [O] The Drowned City (drafted 11 Nov 2026)
**Totals**
- 95787 3,150 + 1g 50s; 95788 3,150; 95798 2,350 + 35s; 97130 3,900 + 50s; 95789 3,900 + 1g; 95791 3,900. **20,350 XP, 3g 35s** (Wowhead zone_16550 / zone_36 xp and money fields).
- Certain (objects / kills): 95787, 95791, 97130 if the idol is an object = 10,950 XP; luck-dependent: 95788 (+95798 behind it if it is the follow-up), 95789.
- The route plan listed 3 quests / 10,200 XP for this dungeon; the extra rows are 95798 (2,350), 95789 and 95791 (7,800).
**Out**
- 95775 The Drowned City (Wowhead side 2, race mask 8589934770 = Horde), 95776 The Only Good Brinescale... (side 2), 96774 Ancient Gurubashi Idol (side 2) - Horde versions of the same objectives.
- Nothing Alliance in `data/zone_16550.json` is left out.
**Gear calls**
- 95798 (choice): **Apprentice Sorcerer's Slacks** 279878 (cloth legs +9 Int +17 Spi +8 SP) **73.3 | 48.4** over Rune-Etched Epaulets 279879 (leather shoulder +11 Agi +12 Sta +4 Defense) 10.4 | 10.4. Replaces whatever legs he wears (Lightstep Leggings 12.3 is the only scored leg reward in the plan's 27-30 list) - the biggest single upgrade of round 1 so far.
- 95789 (choice): **Saltseer's Helm** 279930 (leather head +12 Int +5 Spi +8 SP) **48.3 | 35.3** over Rusted Troll War Belt 279882 (mail waist +4 Sta +9 Int +12 AP; unusable until 40, then 27.2 at band 40 = a tie with Violet Sash 27.2). Replaces Wild Headdress 42.1 | 30.1 (29 [O]) or anything lesser.
- 95791 (choice): neither is an upgrade on the plan's picks - Mutinous Cuffs 279883 (cloth wrist +7 Sta +7 SP) 14.0 | 7.0 < Arathi Armbands 18.8 (29); South Seas Shroud 279884 (cloak +7 Sta +3 Spi +3 Defense) 7.5 | 4.5 - take the Shroud only if his cloak scores below 7.5, else take it to vendor (sell 40s 43c vs the cuffs' 26s 86c).
- 95787, 95788, 97130: no item rewards (Wowhead).
**Deviations from the route plan**
1. Plan listed 95787, 95788, 97130 (and 95798 under the addendum); **95789 Shady Saltseers and 95791 The Saltseer Captain added** - Krazek (Booty Bay) quests for the same dungeon, req 34, in `data/zone_16550.json` with side null and in qdb with no race mask.
2. **95787 / 95788 end at Loremaster Dibbs in Southshore** (Wowhead E:n2277), not in Stranglethorn; with 95798 (Abra Cadabra) and 97130 (Timear) the hand-ins are all in Hillsbrad / Alterac. Hence chapter 31's recommendation to keep the Southshore hearth.
3. **97130 req 34** - picked up in chapter 31 (Alterac leg), not chapter 27 (31-33).
4. Plan said 97130 "starts in Alterac per Wowhead's zone tag - verify": verified, Archmage Timear 31439, 16.2,71.7 Alterac (qdb spawn; Wowhead S/E n31439).
5. Level band 36-37 instead of the plan's 35-40 (entry level from chapter 31; quest level 40).

### Spec 32 - Dustwallow Marsh 36-37 (drafted 11 Nov 2026)
**Totals**
- Plain quests: 27 turn-ins - 1248, 1301, 1260, 1302, 1249, 1250, 1264, 1132, 1282, 1265, 1266, 1324, 1267, 1218, 1206, 1219, 1220, 1222, 1284, 1252, 1253, 1259, 1285, 1286, 1287, 1319, 1320.
- Plain XP: **35,650** at full value (1132 at 80% = 960 makes it 35,410 at level 36).
- `[O]` XP: 0 (no optional quests).
- Quest money: **1g 70s** (1267 1g 30s + 1222 40s).
- Outgoing money: flights ~10s 10c, Soothing Spices 4s 80c; the boat is free.
**Out**
- 1204 Mudrock Soup and Bugs (2,850) and 1258 ... and Bugs (3,150, Baroque Apron): optional-step test fails. Baroque Apron (cloth chest +6 Str +6 Sta +7 Spi) scores 29.5 | 22.5, a side-grade to Snapbrook Armor 30.5 | 21.5 (leather +4 Str +9 Spi, chapter 21 pick; -1 central, +1 conservative) and well below Robe of Crystal Waters 39.0 | 30.0 (chapter 31 [O]). And 1258's Pristine Crawler Legs drop only in Swamp of Sorrows (Silt Crawler 922 L40-41 25 spawns, 62%; Monstrous Crawler 1088 L43-44, 10.7%), turn-in Theramore - not reachable in round 1 after chapter 37. 1204 alone (39.1%, ~21 kills) is XP-only. Nothing else needs 1204/1258 (1258 is the only quest naming 1204).
- 1177 Hungry! (12 Mirefin Heads, 25.6%): drop rule, under 30%.
- 1203 / 81570 Jarl Needs a Blade (Moonsteel Broadsword, a crafted item; no drop source in qdb): not obtainable on the route; nothing gated behind it.
- 6609 I Got Nothin' Left! and 6607 Nat Pagle, Angler Extreme: both need **Fishing 225** (qdb quest row [17] requiredSkill = [356, 225]; 356 = Fishing in SkillLine.csv) and level 35. Plan target is Fishing 200 by 40, so both go to round 2 (Nat Pagle's four fish: Feralas Ahi - object 400006 Feralas 62.8,51.6; Misty Reed Mahi Mahi - 400007 Swamp of Sorrows 87.1,61.4; Sar'theris Striker - 400008 Desolace 28.8,62.1; Savage Coast Blue Sailfin - 400009 Stranglethorn Vale 28.5,34.6; they only drop with the quest in the log, so the round-1 "[O] fish them on the spot" notes in chapters 30/33/37 cannot work either).
- 98233 Sword in the Slime (3,450 + 55s): Jameson's Training Sword 35.2% -> XP-only optional (Jameson's Backup Sword is a 2H sword: shaman cannot use) -> out (brief).
- 1288 Vimes's Report: not in QuestieDB 1.0.14 (Wowhead: 285 XP, no starter/ender).
- 6624 Triage (First Aid 225) and 6625: round 2.
- 7070 Shadowshard Fragments: Maraudon, req 39, round 2.
- 1271 Feast at the Blue Recluse (after 1222): starts and ends at Angus Stern in Stormwind, Wowhead lists no XP.
- 1133 Journey to Astranaar (Fiora; delivery to Astranaar, no XP listed) and 1135 Highperch Venom (Fiora; Highperch wyverns in Thousand Needles, off route).
- 98205 Whelps are the Worst!, 98215 Dragon Scales, Post Burnt Tails, 98231 Active Ingredient (new, Wowhead side "both", req 39, L44): not in the QuestieDB 1.0.14 quest table; starters Drazzit Dripvalve 270723 / Gizzix Grimegurgle 270727 have no spawns; targets Searing Hatchling/Whelp are L41-43. Round 2 candidate.
- 625/626 Cortello's Riddle: chain from 624 (Stranglethorn); 625 starts on a Swamp of Sorrows object, which the route reaches after Dustwallow.
- Horde-only Dustwallow quests (1238/1239/1269/1270/98192 ...) and the mage class quests (1947-1958, 1799, 4961, 4976): not for him.
- Higher bands: 2846/2861 (req 40), 81764/81765 (req 45), 95194/95196/95198 (req 48), 6582-6585, 8227, 8970.
- Pool reconciliation (`pool30.py L28-41 15`, 23 rows): in = 1206 1218 1219 1220 1222 1252 1253 1259 1260 1282 1284 1285 1286 1287 1319 1320; out = 1177 1203 81570 1204 1258 1271 98233 (reasons above).
**Gear calls**
- 1267 Jaina's Signet Ring (fixed, ring +3 Str +7 Sta): 6.0 | 6.0. He wears Seal of Wrynn 22.9 (chapter 15) and Tiger Band 22.5 (chapter 26); Ring of Forlorn Spirits (chapter 17) is ~16. Vendor it (sell 46s 30c - worth noting for the mount fund).
- 1222 Elixir of Fortitude (item 3825; the 11 Nov tooltip names it "Elixir of Lesser Fortitude": +120 max health 1 h): consumable, keep for a hard pull.
- 1218 Frog Leg Stew: food (841 health over 27 s), eat it.
- No reward choices in the plain quests. (1258's Baroque Apron, the one gear prize of the zone, is out: see Out.)
**Deviations from the route plan**
1. **Entry route**: plan default was the Booty Bay -> Ratchet boat and the Barrens road, with Stormwind/Menethil "if the boat route is used". This spec makes Stormwind + Menethil + the Theramore boat the route: 1248 is in his log (25:63, never [QS]-abandoned) and the whole Missing Diplomat chain (13,550 XP with 1301/1260/1132) hangs on Mikhail in Menethil.
2. **1204/1258 out** (plan: `[O]` pair for the Baroque Apron): 1258's crawlers are in Swamp of Sorrows only (qdb npc 922/1088 spawns, zone 8) and the apron (29.5) does not beat Snapbrook Armor (30.5) or Robe of Crystal Waters (39.0).
3. **6609 -> 6607 Nat Pagle out of round 1** (plan: pickup here): requiredSkill Fishing 225 on both (qdb row [17]); also 6609 is req 35, so chapter 27 (31-33) could not take it even without the skill gate.
4. **1219 The Orc Report -> 1220 Captain Vimes added** (3,440 XP, a ground object 0.4 units from Jarl, Alliance side 1 on Wowhead; the plan did not list it).
5. **1301 James Hyal and 1248/1249/1250 counted in this chapter** (plan listed 1302 and the Dustwallow half of the Diplomat chain). 1132 kept plain (plan: "if he passes" - he does).
6. **1324 added to the Diplomat list** (the plan's "1264-1267" skips the event quest id; qdb: 1266 -> 1324 -> 1267).
7. Totals: 27 plain / 35,650 XP / 1g 70s vs plan 26 / 39,755 / 1.70g (the difference is 1204+1258 out, 1219/1220 and 1301/1248-1250 in).

### Spec 33 - Desolace 37-38 (round 1 of the 30-60 guide, drafted 11 Nov 2026)
**Totals**
- Plain: 19 quests, **46,050 XP**, **3g 05s**: 1453 1,300; 1454 3,000; 1455 1,500; 1437 1,950; 1465 1,950; 1438 2,650; 1439 2,650; 1440 3,300; 97284 2,650 (65s); 5741 2,650 (35s); 6027 3,550 (45s); 5501 2,250; 5821 2,750; 5943 2,850; 5561 2,000; 79229 1,550 (25s); 6132 2,250 (45s); 6134 2,250 (45s); 261 3,000 (45s).
- `[O]` quest XP: 0 (the only `[O]` steps are the two recipes: 30s + 70s).
- Carried out with XP elsewhere: 1052 1,550 (34), 79235 1,550.
- The plan's ~62k for 33 included 1052/1053 and the Draenethyst pair; the difference is accounted for in Deviations.
**Out**
- 1387 Centaur Bounty: 15 Centaur Ears 18.3% (drop rule <30%).
- 93224 Carved Centaur Totems: 25.5% (drop rule).
- 1456 / 1457 Karnitol's Satchel: 7.4% (drop rule); 1457 needs 1456 (only dependant). Reclaimers chain ends at 1455.
- 1458 Reagents for Reclaimers: Hatefury Claw 16.7% / Horn 16.8% (drop rule); 1459 -> 1466 -> 1467 behind it (row [12] chain) go too.
- 6161 Claim Rackmore's Treasure!: Rackmore's Golden Key 5.3% (drop rule).
- 96222 Khan Hratha (Umarak 253066, L45 elite, faction "Kolkar Clan", 43.1,78.2): Maraudine Key Fragment from Khan Hratha (L42 elite with 39-40 guards) + War Horn Mouthpiece 6074 (rate not pulled). Group content; the only scored reward is Ceremonial Centaur Blanket 25.8 [16.8] (cloak) - optional-step test fails unless his cloak is under ~20 (Repairman's Cape 21.4); out.
- Gelkis / Magram chains (Braedyn's ruling, reputation): 1382, 1384, 1370, 1373, 1374, 1380, 1385, 1386, 1369, 1371, 1375, 1381, 92743, 93196, 92754, 92755, 92814, 92817, 92818, 93226, 93227.
- Valley of Bones / Shen'dralas chains (ruled out): 92841, 93034, 93035, 93037, 93041, 93045.
- 93464 / 93465 / 93678 Draenethyst: the route does Desolace before the Swamp, and 93464 starts at Magtoor in the Swamp (BRIEF correction). Side: data/zone_405.json (9 Nov) reads 2 for 93464/93465, the main session's 11 Nov Wowhead pull reads Both - out of round 1 by route order either way.
- 94841 Lost Shipping Crate: object 656789 has no spawn in qdb; 285 XP; ends at Powderfuse Port (chapter 41) - XP-only, out.
- 7028 / 7041 / 7065 / 7067: Maraudon, req 39-45 - round 2.
- 6141 Brother Anton: breadcrumb from Stormwind; 261 does not need it.
- 6607 Nat Pagle fish: not in the log (see Deviations).
- 79236 / 79242: not available here (start at Tokal, Booty Bay).
- 1277, 1441, 1460, 1461, 8458 (<UNUSED>/<nyi>), 92811 / 92812 (level 60): not real quests.

Pool reconciliation (`pool30.py L28-41 405`, 57 rows): every row is placed above as plain or out. 79229 Highway Robbery is in the pool but not in the route plan - added as plain (object start on the Kodo Graveyard road, hands in at Bibbly whom the route visits).
**Gear calls**
- 1440 Return to Vahlarriel: Grappler's Belt (leather +7 Str +5 Sta) 14.0 [14.0] = Gloves of Insight 14.0 [7.0] = Moonlit Amice 14.0 [7.0] > Garrison Cloak 2.8. None beats the planned picks (Violet Sash 26.9 waist from 28, Seawolf Gloves 24.9 / Tiger Hunter Gloves 21.6 hands, Palm Frond Mantle 26.5 / Batwing Mantle 33.0 shoulders). Call: Grappler's Belt only if your belt scores under 14 (no Violet Sash); otherwise take Moonlit Amice to vendor (18s 46c, the highest sell).
- 5561 Kodo Roundup: **Kodo Rustler Boots** (cloth +3 Sta +8 Int +5 Spi) 25.7 [20.7] over Wrangling Spaulders (mail, 40+, 17.9). Replaces Excelsior Boots 22.5 (31 `[O]`) or Junglewalker Sandals 13.2 (30); keep Renewing Footpads 26.1 [22.1] (28) if you have them - a tie.
- 5821 Bodyguard for Hire: Trader's Ring (+8 Sta) fixed, scores 0 -> vendor (40s 40c) unless a ring slot is empty.
- 5943 Gizelton Caravan: nothing usable for a 2H shaman (Sidegunner Shottie gun, Kodo Brander wand, Studded Ring Shield, Farseer's Forgotten Shield). Take Kodo Brander for the vendor (69s 35c; Shottie 69s 9c).
- 5501 Bone Collector: Kodobone Necklace (+7 Sta +4 Spi) fixed, 10.0 [6.0] - below Giantstone Medallion 25.0 (22 `[O]`) / Thermaplugg Medal 25.0 (24 loot); vendor 49s 12c unless the neck is empty.
- 6134 Ghost-o-plasm Round Up: Condor Bracers (cloth +6 Sta +7 SP) 14.0 [7.0] vs Anchorhold Buckler (shield, not used, 19.9). Arathi Armbands 18.8 (29) stay; take the Anchorhold Buckler for the vendor (65s 62c).
- 6027 Book of the Ancients: Silkstream Cuffs (cloth +4 Sta +5 Int +4 Spi) 18.2 [14.2] vs Arcmetal Shoulders (mail 40+, 8.5). Arathi Armbands 18.8 [18.8] stay (a tie on central, better on conservative); take Arcmetal Shoulders for the vendor (43s 53c) - or Silkstream if your wrist is weaker than 18.
- Twisted Air Totems: no reward here (79358 hands in at Veyric in chapter 39).
**Deviations from the route plan**
- **Nat Pagle fish out**: 6609 and 6607 need Fishing 225 (quest.json row [17] = [356, 225]) and level 35, so 6607 is not in his log in round 1; the Sar'theris Strand step is not placed (the fishing spots exist: object 400008 at 35.3,31.7 / 36.1,32.8 by the Karnitol wreck, for round 2).
- **Travel**: the Theramore -> Nijel's Point flight cannot be used on the first trip (undiscovered); entry by Astranaar + Stonetalon road.
- **79229 Highway Robbery added** (plain, 1,550 + 25s): in the pool, not in the plan.
- **79235 On the Lam** pickup placed at Bibbly at the end of leg 7; carried out to a Booty Bay visit in 37 or round 2 (plan: 'Tokal's two hand-ins fit the Booty Bay flights').
- **96222 Khan Hratha** (not in the plan) listed out.
- **Draenethyst** (plan: Phase 3 decision): out of round 1 by route order (Swamp start).
- Plan XP ~62k vs 46,050 plain here: 1052 (1,550) and 1053 (4,700) are counted in chapter 34, Draenethyst (6,150) is out, 79235 (1,550) is handed in later.

### Spec 34 - [O] Scarlet Monastery 37-39 (dungeon chapter, drafted 11 Nov 2026)
**Totals**
- 1052 1,550; 1053 4,700; 1050 3,550; 96800 2,850 (45s) = **12,650 XP, 45s**.
- Optional chapter, not counted in the level budget.
**Out**
- 1048, 1049, 1051, 1113, 1160: Horde (side 2).
- 79946, 79963, 79970: paladin (reqclass 2).
- 89474, 89475: level 60.
- Graveyard wing: no Alliance quest needs it; skipped.
**Gear calls**
- **1053: Bonebiter** (2H axe 38.8 dps +20 Str +10 Sta) **583.5** over Black Menace (dagger, 1H) 415.4 / Sword of Serenity (sword, unusable) / Orb of Lorica (off-hand). Replaces **Defender of Dalaran 469.8** (chapter 28) - +113.7; it also beats Dark Hearted Hammer 429.3 (30), Servomechanic Sledgehammer 423.2 (31) and **Rock Pulverizer 471.1** (chapter 35, after this - skip it there if Bonebiter is in hand). At 40 the plan's verdict holds: Rage of the Storm (529.8 linear) wins by ~1% only with Stormstrike; Bonebiter is carried until then (docs/forever-enh-stat-weights.md 11 Nov).
- 1050: Explorers' League Commendation (neck +9 Sta +9 Spi, fixed) 22.5 [13.5] - below Giantstone Medallion / Thermaplugg Medal 25.0; wear only if your neck scores under 22.5.
- 96800: Salve and Salvation (off-hand, not used, 28.5) vs Knucklebound Thimble (ring +8 Sta, 0). Take the Thimble (43s 99c, vendor or an empty ring slot; the off-hand sells for 43s 83c).
- Boss loot (`[OC]` roll calls, live tooltip drop chances):
  - **Mograine's Might** (2H mace 38.8 dps +8 Str +14 Sta +16 Int, req 39; Mograine 27.4%) **585.9** - ties Bonebiter; roll, either is fine.
  - Ravager (2H axe 37.3 dps, req 37; Herod 24.7%) 522.1 - beats Defender of Dalaran until Bonebiter is handed in; low priority.
  - **Whitemane's Chapeau** (cloth head +9 Sta +10 Int +12 Spi +7 SP, req 39; 34.0%) 60.5 [41.5] - beats Wild Headdress 42.1 / Blackwater Cap 40.0: roll (BoP; wear at 39).
  - **Triune Amulet** (neck +7 Sta +7 Spi +8 SP, req 39; Whitemane 34.0%) 33.5 - beats Giantstone 25.0: roll.
  - **Mantle of Doan** (cloth shoulders +6 Int +8 Spi +7 SP, req 34; Doan 32.1%) 43.9 [28.9] - beats Batwing Mantle 33.0: roll. Inquisitor's Shawl (cloth shoulders +13 Int +7 SP, req 37; Fairbanks 29.1%) 35.5 - second choice.
  - Pass: Library Walkers 24.9 (below Kodo Rustler Boots 25.7 / Renewing Footpads 26.1), Band of Crimson Light 12.0, Robe of Doan 20.0, Loksey's Training Stick (staff 438.1), Hand of Righteousness (1H), Herod's Shoulder / Raging Berserker's Helm / Gauntlets of Divinity (mail, 40+), Dog Training Gloves (no stats), Branded Leather Bracers (+6 Sta).
**Deviations from the route plan**
- The plan says "Getting there: Southshore hearth"; the hearth is Nijel's Point after 33, so the way in is the Auberdine flight + boat to Southshore and chapter 08's trek; the way out is the Southshore -> Ironforge flight, which also takes over chapter 35's opening travel.
- Adds the Dalaran-crater stop: 96773 pickup (req 34, cannot be taken in 27) and the 96800 hand-in at Olvek.
- The plan lists 6626 here as an RFD lead-in; it is in 34b.
- Gear: adds scored boss-loot roll calls (Mograine's Might ties Bonebiter; Whitemane's Chapeau, Triune Amulet and Mantle of Doan are upgrades).
- Adds a training stop at Eldrun on the Ironforge hand-in.

### Spec 34b - [O] Razorfen Downs (dungeon chapter, drafted 11 Nov 2026, revised the same day)
**Totals**
- 6626 3,450 (75s), 3523 285, 3525 4,250, 3636 4,300 (Stormwind hand-in), 96773 4,100 (55s, Lan'dalock hand-in) = **16,385 XP, 1g 30s** with the chapter-39 placement; **7,985 XP, 75s** if run from Nijel's Point before 34; 12,085 XP if run after 34 without 3636.
- Not counted in the level budget (optional chapter).
**Out**
- 3341 / 6521 / 6522 / 97196: Horde (side 2).
- 93604 Agamaggan's Blood: not in the Forever DB (qdb) and its zone-file side is unset - out.
- 3636 is in only with the chapter-39 placement; if 34b runs from Nijel's Point at 38, 3636 is out (level 39, Stormwind start, rule 2: no second run).
**Gear calls**
- 3525: Dragonclaw Ring (+7 Sta, 5 hp/5s) 0.0 -> vendor 40s 84c.
- 3636 (at the Stormwind hand-in): Vanquisher's Sword fixed (sword, a shaman cannot use it; sells 1g 80s 3c) + choice **Purified Ring** (+12 Int +5 SP) 29.8 [24.8] over Amberglow Talisman (neck +1 Agi +7 Sta +10 Spi) 25.9 [15.9]. Replaces Tiger Band 22.5 / Coldwater Ring 27.4 (39). Amberglow only if your neck is under 25.9 and both ring slots beat 29.8.
- 6626 / 96773: money only.
- Boss loot (`[OC]` roll calls, drop chances from the live tooltips):
  - **Deathmage Sash** (cloth waist +15 Int +7 SP, req 36; Mordresh 27.4%) 38.8 [31.8] - beats Violet Sash 26.9: roll.
  - **Glowing Eye of Mordresh** (neck +8 Int +7 SP, req 36; Mordresh 36.8%) 27.2 [20.2] - just above Giantstone Medallion / Thermaplugg Medal 25.0; below SM's Triune Amulet 33.5 if that dropped.
  - **Deathchill Armor** (mail chest +3 Sta +9 Int +15 Spi +7 SP, req 39; Amnennar 25.4%) 66.3 [44.4] on the 30 band; at 40 mail is wearable - roll (re-score with `--band 40` before writing).
  - Swine Fists (leather hands +8 Str +8 Agi, req 37; Plaguemaw 34.2%) 23.6 - below Seawolf Gloves 24.9 and Traveled Gloves 40.0: pass unless your gloves are weaker.
  - Pass: Coldbringer Spine (staff 444.9, below Bonebiter 583.5 / Rage of the Storm), X'caliboar (2H sword, unusable), Glutton's Cleaver (1H), Icemetal Barbute (plate), Robes of the Lich (+20 Sta, 0), Bonefingers 14.8, Fleshhide Shoulders 15.7, Silky Spider Cape (+10 Sta), Arachnid Gloves (no stats).
**Deviations from the route plan**
- The plan puts an RFD chapter "at 37-39 after 34"; this spec recommends chapter 39's Thousand Needles leg (near-zero travel, 3636 and 96773 both possible), since 33 -> 35 run from a Nijel's Point bind and 96773 / 3636 cannot be in the log earlier.
- Adds 3523 / 3525 (Belnistrasz, 4,535 XP): in the zone pool (side Both), not in the plan.
- 96773 is picked up in 34 (Dalaran crater), not in 27 (req 34).

### Spec 35 - Badlands 38-39 (drafted 11 Nov 2026)
**Totals**
- Plain (16 quests, 37,140 XP): 707 710, 738 1,450, 739 3,450, 704 2,850, 720 1,350, 721 2,750, 718 2,150, 703 2,350, 722 3,150, 723 2,350, 724 3,150, 725 1,550, 726 2,350, 709 3,150, 727 780, 1360 3,600.
  - If 722's amulet does not drop: minus 723-726 (9,400) and 722 (3,150).
- Rate-dependent: 2500 3,000 (+45s), 2418 3,500.
- Quest money (plain): 738 4s + 1360 60s = 64s; with 2500 1g 09s.
- Ironforge reputation: 707 25, 724 100, 725 50, 726 75 (+ 2500 100) - relevant to gold-plan option (c), Honored = 90g riding.
- Level: ~37k quest XP plus kill XP from ~38 should put him at ~39 (check against the pre-2.3 table in warcraft.wiki.gg before quoting it in the chapter - not done here).
**Out**
- 692 The Lost Fragments - three fragments at 3.79 / 5.83 / 5.83% (Enraged Rock Elemental) and needs 687; drop rule (<30%).
- 705 Pearl Diving - Giant Clams on the Stranglethorn coast; wrong continent (route plan).
- 706 Fiery Blaze Enchantments - req 40, Black Drake's Heart 3.8%; drop rule.
- 708 The Black Box - drop start (Corroded Black Box 4613, no dropper in qdb); not in the plan's list; out (drop start, unknown rate).
- 710 Study of the Elements: Rock - Small Stone Shard 33.5%: `[O]` range but XP-only -> optional-step test; 711 (22.89%) / 712 (26.17%) drop rule; 716 / 734 / 777 / 778 behind them go with the chain.
- 713 / 714 / 715 - crafted items (Frost Oil, Gyrochronatom, potions); route plan.
- 719 A Dwarf and His Tools - Ryedol's Lucky Pick 6.7%; drop rule (Ryedol's Hammer 1H mace 278 would not be used anyway).
- 732 Tremors of the Earth - req 40 (Sign of the Earth 92.86% from Boss Tho'grun; needs 718): round 2 with the mail chest; 717 behind it likewise.
- 733 Scrounging - Scrap Metal 14.4%; drop rule.
- 735 / 737 - Star of Xil'yeh 3.85%; drop rule (chain from 727).
- 1108 Indurium - 23.7% and needs 1106; drop rule.
- 2501 Badlands Reagent Run II - req 40, Scorched Guardian elites L43-45 (east Badlands); round 2.
- 97617 Safety Checks (new, req 35, 3,150 XP + 25s, Wowhead side 1) - starter and ender unlinked in qdb, Dorgaron (269577) has no spawn, two of its three items (278403 helmet, 278404 mattock) have no source; Unstudied Artifact 278402 drops from Shadowforge Tunnelers/Darkweavers and the Bonesnapper/Stonevault Shaman camp (multi-dropper, no rate). Out until a Wowhead page settles it - Needs pull.
- 3375 Replacement Phial - only if the Talvash phial is lost (chapter 36 chain is out anyway).
**Gear calls**
- 739 Murdaloc (fixed): **Rock Pulverizer** 2H mace 31.22 dps +34 AP = 471.1. Against Defender of Dalaran (ch 28 `[O]`) 470.1 = side-grade (+1); against Dark Hearted Hammer (ch 30) 429.3 = upgrade; against Bonebiter (ch 34 `[O]`) 583.5 = keep Bonebiter. Sell 1g 60s 78c.
- 704 Agmond's Fate: **Prospector Gloves** (leather +8 Int +9 SP) 31.5 | 22.5 over Restorer's Fine Gloves (cloth +6 Sta +8 Spi +4 SP) 28.0 | 16.0. Excavator Gauntlets (mail +8 Str +8 Spi) 36.0 is mail - not before 40. Replaces Seawolf Gloves 25.4 (ch 31 Faldir's Cove), Gemmed Gloves 28.2, Tiger Hunter Gloves 23.0 or Shepherd's Gloves 20.7, whichever he wears. Note: the Wowhead atlas row says "Rewards: no longer Prospector Gloves", but data/zone_1337.json itemchoices (the newer Forever row) and qdb both still list 4980 - test list.
- 709 Solution to Doom: **Doomsayer's Robe** (cloth chest +18 Spi +6 SP) 57.0 | 33.0 over Doomcaller's Pants (leather legs +13 Str +9 Int) 41.2 | 41.2 and Fists of Impending Doom (mail) 31.8. Robe replaces Old Leather Jacket 32.2 (92867 `[O]`, if taken) or Baroque Apron 29.5 (1258 `[O]`): +25..28. Take the Pants instead only if his legs score under ~15 (no Apprentice Sorcerer's Slacks 73.7 from 31b and nothing better); under the conservative set the pants win (41.2 vs 33.0) - say so in the line.
- 762 / 1139 / 2240: chapter 36.
- 2418 (if in): **Everlast Boots** (cloth feet +9 Spi +3 SP) 28.5 | 16.5 over Charged Leather Bracers 14.5 (below Arathi Armbands 19.6 / Silkstream Cuffs 18.4), Duracin Bracers (mail) 13.1, Energized Stone Circle (shield) 6.0. Boots replace Renewing Footpads 26.6 (ch 28 `[O]`), Kodo Rustler Boots 26.0 (ch 33) or Excelsior Boots 24.1: +1.9..4.4.
- 738: vendor everything (belt no stats). 703: food + recipe (Cooking). 718, 720-727, 1360, 2500: no item choice.
**Deviations from the route plan**
- **Bind Thelsamar** (plan: "hearth stays Nijel's Point"): the chapter returns to Thelsamar twice and chapter 36 hearths out of Uldaman to Ghak; Nijel's Point is not used again in round 1 (37 flies from Ironforge, 38 binds Farholde Keep). Changes the Hearth / bind sequence line.
- **Start via Ironforge** (plan: "fly to Thelsamar"): training (no trainer since 27) and the 1360 pickup; Menethil -> Ironforge -> Thelsamar costs one flight hop.
- **1360 Reclaimed Treasures moved from 36 to 35**: Krom's chest (124389) has only a Badlands spawn (35.6,23.5), outside the instance.
- **709's tablet is outside the instance** (Ancient Chest 126260, Badlands 39.3,18.8), so 709 completes in this chapter (plan put the tablet "inside Uldaman").
- **722 is outside the instance** (Hammertoe 37.9,10.6 and Magregan 39.0,19.7 are Badlands spawns); the Ironforge legs 724-726 are done at the end of this chapter (plan folded them into 36). 762 and 1139 stay with 36.
- **2418's droppers are the Shadowforge elites**, not Dustbelcher ogres (plan: "plain if 30%+ with the Dustbelcher kills"); outcomes rewritten (section 4 step 25).
- **Twisted Fire Totem droppers**: qdb lists only the Stonevault troggs; Wowhead's best droppers are the Dustbelcher Warrior / Mystic (13.7 / 14.8%); a kill line at the 718 crate added.
- **703's Badlands rate is ~31%** (24.1 / 33.0 / 30.8% on the three Badlands buzzards), not 37%: budget ~13 kills, not ~11.
- **Hammertoe's Amulet 58.06%** (named mob, 30-60%): "one kill only, then abandon" note on 722 - not in the plan.
- **Order**: 739 ends and 704 starts at Ironband in Loch Modan, so the Badlands take two passes from Loch Modan; the plan did not say.
- **2500** carries the two-outcome rule; added 708, 2501, 97617, 3375 to the out list.

### Spec 36 - [O] Uldaman 39-40 (dungeon chapter, drafted 11 Nov 2026)
**Totals**
- Always (if the run happens): 762 4,650 + 1g 25s; 2398 315 + 5s; 2240 3,900 = 8,865 XP, 1g 30s.
- With 2500 done in 35: 17 3,450 + 55s.
- At level 40 at the Discs: 2278 4,200 + 2279 5,250 + 2439 420 (Thawpelt Sack) = 9,870.
- Luck: 2198 3,300.
- Maximum 25,485 XP, 1g 85s. (Without 1139, which would add 5,850 + 1g 30s.)
**Out**
- 1139 The Lost Tablets of Will (5,850 + 1g 30s, Medal of Valor 12.0) - offered by Advisor Belgrum only after 762 is handed in (qdb 1139 preQuestSingle [762], start 2918 Ironforge), and 762 needs the Infernus kill in the Badlands; the Tablet (object 142088) is inside the instance, so it needs a second run - rule 2 (one run, never a re-run). Unless Infernus is killed and 762 handed in **before** the run (an Ironforge round trip between Angor Fortress and the portal) - see Unsure.
- 2199 Lore for a Price (2,450; 5 Silver Bars from chests or the AH; Braedyn has no Mining) - XP-only; optional-step test. 2200 Back to Uldaman, 2201 Find the Gems, 2204, 2361 - 2200 is taken in Ironforge after 2199 and sends him back into Uldaman (Remains of a Paladin 6912; gems from the Shadowforge Cache, Grimlok, the Conspicuous Urn; power source from Archaedas) - a second run, rule 2. 3375 Replacement Phial - behind 2201.
- 2501 Badlands Reagent Run II - req 40, elite Scorched Guardians L43-45 in the east Badlands; round 2.
- 2963 Portents of Uldum (behind 2439) - req 45; round 2.
**Gear calls**
- 762 An Ambassador of Evil: Thane's Hammer (1H mace 17.7 dps +8 Int +38 SP) 337.7 - a one-hander, not used by the 2H build; **Ironforge Agent's Gloves** (leather +7 Str +11 Agi) 26.3 | 26.3 is below Prospector Gloves 31.5 (ch 35's 704 pick) - no upgrade; Dwarf Captain's Sword (sword, shaman cannot use) 372.4. Pick for value: **Dwarf Captain's Sword (sells 1g 55s 84c)** over Thane's Hammer (1g 38s 77c) and the gloves (37s 21c); take the gloves only if he did not take Prospector Gloves and wears Seawolf Gloves 25.4 or worse.
- 2240 The Hidden Chamber: Dwarven Charge (2H axe 31.2 dps +12 Str +11 Sta) 460.9, Guardian Staff (2H staff 31.2 dps +11 Agi +11 Sta) 449.8, Explorer's League Lodestar (off-hand) 10.0. **Neither 2H beats Rock Pulverizer 471.1** (ch 35) or Bonebiter 583.5 (ch 34 `[O]`). Pick for value: **Guardian Staff (sells 1g 62s 91c)** over Dwarven Charge (1g 60s 78c). The route plan's "Dwarven Charge 2H 461" is a vendor item now that 739's Pulverizer comes first.
- 2439: Thawpelt Sack (14-slot bag) fixed; potion choice free (Greater Mana Potion or Superior Healing Potion - his call).
- 17: Greater Mender's Potion (+44 spell healing 30 s) - not used by the model.
- 1139 (out): Medal of Valor (+12 AP) 12.0 would have been the pick over Medal of Courage (+9 Sta) 0.0; neither beats Explorers' League Commendation 22.5 (ch 34 `[O]`).
- 2361 (out): Talvash's Enhancing Necklace (+10 Sta +1 Int +12 SP) 25.7 | 13.7 would beat the Commendation 22.5 - the reason the chain was wanted.
- Boss loot: not scored in this spec (dungeon_loot.py works per written chapter; run it after 36 is written).
**Deviations from the route plan**
- **1139 out** (plan: "722, 1139, 709's tablet" in the run): 1139 is only offered after 762 is handed in (qdb), so it needs a second run - rule 2.
- **722, 709's tablet and 1360 are done in chapter 35**: their NPCs/objects are Badlands spawns outside the instance (Hammertoe 37.9,10.6; Magregan 39.0,19.7; Ancient Chest 39.3,18.8; Krom's chest 35.6,23.5).
- **17's prerequisite verified**: 2500 (qdb preQuestSingle). 17's caps also spawn in the outer cave (8 Badlands spawns), so 17 needs no deep clear.
- **Talvash chain cut to 2198** (plan: "pick up if the necklace drops, finish on the Ironforge passes"): 2200-2204 are inside Uldaman after an Ironforge hand-in (2199), i.e. a second run.
- **Dwarven Charge is not an upgrade** (plan: "Dwarven Charge 2H 461" as the prize): Rock Pulverizer (471.1) from 739 comes first in chapter 35.
- **Added 2439 The Platinum Discs (Thawpelt Sack, 14-slot bag)** behind 2279 - passes the optional-step test (a bag); not in the plan.
- **762 Ambassador of Evil moved into this chapter** (plan: chapter 35 chain "-> 762 ... -> 1139"): it is the group elite of the Badlands and its pickup comes after 726 in Ironforge.

### Spec 37 - Swamp of Sorrows 39-40 (drafted 11 Nov 2026)
**Totals**
- Plain quests turned in here: 8 - 93585 2,700; 93429 2,750; 1396 2,850; 1421 2,750; 1398 3,450; 1425 2,550; 1393 2,850; 1389 2,750 = **22,650 XP**. Plus 94929 285 (picked up here, turned in in 38).
- [O] XP: 0.
- Quest money: 93429 18s + 1393 85s = **1g 03s** (matches the plan's 1.03g).
- Gold check number: gold.py cannot compute it until chapters 27-36 exist. Plan-table estimate of plain quest money at the end of 37: 17g 05s (end of 26) + 3.00 + 0.45 + 0.32 + 1.38 + 1.70 + ~5 + 0.04 + 1.03 = **~29g 97s** (+ up to ~4g 65s from the [O] dungeon chapters 28/34/36). The writer runs `python tooling/gold.py 37_SwampOfSorrows.lua:<line>` after 27-36 are written and uses that figure; purchases since 30 to quote: chapter 22/24 level-30 training 4g 20s, 32 training, Expert LW/belts, Expert Fishing 1g, Expert Skinning 50s (Balthus 5000 c) and whatever 27-36 list - take them from those chapters' [V]/[T] lines.
**Out**
- 1363 / 1364 Mazen's Behest: 1364's Khadgar's Essays (6065) is **6.1%** overall (Swampwalker 10/197, Elder 6/57, Tangled Horror 8/141): out under 30% (drop rule); 1363 (330 XP, Stormwind talk-to) exists only to lead into 1364 - out with it (prompt: "1363 only if 1364 is in").
- 93430 Taking the Bait Back: Lucky Lure 258530 **17.1%** (Lost One Fisherman, tooltip): out (<30%).
- 1116 Dream Dust in the Swamp: needs 1115 (Krazek, STV chain not taken) and Speck of Dream Dust ~30% (plan): out.
- 1392 Noboru the Cudgel: drop start from a single named mob (5477, L39, 54.9,34.1); rate not in drop_rates/tooltips: out unless the pull shows >= 60% (then plain: the mob stands on the route; 2,250 XP, ends at Magtoor). Needs pull.
- 1423 The Lost Supplies: starts from item 6172 out of Scattered Crate objects (28604, 17 spawns x4-64 y20-50); Wowhead lists no XP; chance unknown; plan had it out as a drop start - out (an unknown-XP optional fails the optional-step test).
- 93176 My Little Friends (Amaryllis Webb 217412, 25.1,54.2; 2,750 + 35s; reward Weevil K. Neevil = a companion pet): the three bugs are in STV (217588, 43.4,17.7), Arathi (217589, 31.3,27.2) and Desolace (217590, 49.0,58.7) - zones already behind the route; a pet is not a gate/bag/gear: out. Not in the route plan; listed so the reason is on record.
- 624/625 Cortello's Riddle (drop start in STV), 93464/93465/93678 Draenethyst chain (Desolace is before the Swamp - brief correction), Horde quests (698, 699, 1418, 1420, 1422, 1424, 1426-1430, 93663 Lost in Transit - race mask 8589934770 = Horde bit), 45+ quests (2621+, 3374, 3512, 3626-3628, 8417-8425, 93679): out.
- pool30 reconciliation (`python tooling/pool30.py L28-41 8`, 14 rows): 1116, 1389, 1392, 1393, 1396, 1398, 1421, 1423, 1425, 93429, 93430, 93464, 93585, 94929 - every row is in section 4 or above.
**Gear calls**
- 1393 Galen's Escape: Visionary Buckler (6828, shield, +4 Sta +7 Spi; 17.5 central, off-hand - not usable in the 2H build): **vendor** (sell 62s 68c, tooltip). No choice.
- No other quest in the chapter has an item reward (zone_8 itemchoices/itemrewards empty for 1389, 1396, 1398, 1421, 1425, 93429, 93585, 94929).
**Deviations from the route plan**
- Hearth: plan says "bind Nethergarde Keep if the Blasted Lands hand-in is the last stop"; qdb has no innkeeper at Nethergarde (zone 4) or any Alliance one in the Swamp (zone 8): hearth unchanged.
- **Nat Pagle Misty Reed Mahi Mahi step removed** (main session 11 Nov): 6607/6609 need Fishing 225 (quest.json row [17] = [356, 225]) and level 35, so 6607 is not in his log in round 1. The plan's professions line ("Nat's four fish are fished where the route passes ... noted [O] on the spot") does not apply to round 1.
- 1363 Mazen's Behest: plan lists it plain (330); out here because 1364 is out (prompt rule).
- **94929 Deliver the Second Shipment added** (not in the plan): plain, free pickup at Biggs, 285 XP, hand-in at Demar Brant, Farholde Keep - **chapter 38 must carry the [QT94929] line** (Demar Brant 257558, Riverglades 66.7,81.0).
- Plan's 37 XP 26,280 vs this spec 22,650 + 285: the plan's figure is 22,650 + 1363 (330) + 1364 (3,300), both out here.
- 1425 titled "Deliver the First Shipment" (Wowhead Forever) instead of the plan's "Deliver the Shipment".
- 93176 My Little Friends (not in the plan) recorded as out.

### Spec 38 - Riverglades I 39-40 (drafted 11 Nov 2026)
**Totals**
- Plain quests turned in: **40** - 94929 285; 94999 700; 94857 300; 94861 3,000; 94843 2,150; 94931 2,850; 94678 2,850; 94679 3,150; 95147 285; 95148 285; 94613 285; 95329 285; 95330 285; 95603 2,150; 95613 2,150; 95615 2,150; 96082 1,550; 96083 315; 95156 2,100; 95561 1,450; 94615 1,450; 94617 2,850; 94614 2,850; 94618 1,450; 94992 2,850; 96009 2,150; 95943 2,150; 94923 2,150; 94924 3,000; 95064 3,000; 95426 3,000; 95983 710; 95066 1,500; 96084 3,150; 94877 3,150; 94879 3,150; 95642 3,150; 95643 3,150; 95562 3,300; 94884 1,650 = **78,385 XP**.
- `[O]` (Braedyn's call): 94925 3,000 (+ 94928 300 in chapter 41).
- Conditional (Log drop, 1.6%): 94885 3,150 + 25s here; the rest in 40 / round 2.
- Quest money (plain): 94923 20s + 94614 20s + 94992 20s + 95613 30s + 94924 25s + 95562 25s = **1g 40s**. Purchases: Holy Candles 35s, Recipe: Plain Ol' Paletusk 20s.
**Out**
- 94842 Unsavory Plant Food - drop rule: Mudfin Murloc Head 22% (Oracle 350/1576, Warrior 353/1551) < 30%. Nothing behind it (no series, no qdb dependant).
- 94881 Curious Trinkets - drop rule: Twilight Charm 25.5% (Shadowmancer 522/2288, Neophyte 784/2826), 25 needed. Nothing behind it.
- 95913 Fit for a Princess - drop rule: Coyote Pelt 16.58% (Plains Coyote, tooltip). Behind it on Wowhead's series: 95961 Stepped Out (kept as "take if offered", Leg B step 20).
- 95984 Song of the Strider - drop rule: Intact Tallstrider Beak 15.95% (Roving Tallstrider). Behind it: 95986 King of the Wild Plains (out with it; its Ombassa's Hide 99.4% does not matter).
- 95988 Goes Down Smooth (Powderfuse, side Alliance) - drop rule: Crawler Spittle 12.21% (Shore Crawler). Behind it: 95957 Drink Up! and 95975 Her World (out with it; prerequisite unverified - if Gray offers Her World in chapter 41 without the others, chapter 41 decides).
- 94829 What We Lost - drop rule: Farmers' Mementos 266148 6.61% from Twilight Raiders (nether tooltip 11 Nov), 5 needed. Behind it: 94858 All That's Left (out with it; Discarded Doll is an object and the Damaged Locket 75.76%, but the series puts it behind 94829).
- 95184 The Sharpest of Blades - 8 Solid Sharpening Stones (7964): no vendor and no drop in qdb (crafted by Blacksmiths); AH-only; not a kill/object quest. Out (Braedyn could buy 8 on the AH for 2,850 XP + 20s - mention in the report only).
- 94881/95913/95984/95988/94829 count as 5 drop-rule outs; 95184 the one source out.
- Not in this chapter (chapter 40 or 41 or round 2): 96081 (to 40), 96085 (40), 95912/95991/96125/96126/94927/94926 (40), the Twilight's Shroud chain (40), 95935 (40, conditional), 95059 Frazzlespark's Crate (starts at Friz, chapter 41 -> Demar), 95219 (round 2), 95161 (level 22 - done in 1-30: 14_Duskwood.lua:18 `[QT95161]`), the 33 side-Both quests (chapter 41).
**Gear calls**
1. **94679 Snargl's Snout** (choice): Bristle Hills Mystic Robe (cloth chest +11 Int +12 SP) 42.6 [30.6]; Gnollhide Tunic (leather chest +11 Agi +11 Spi) 39.8 [28.8]; Southern Watch Leggings (mail legs +13 Str +8 Sta; wearable from 40) 26.0 [26.0]; Unbalanced Fighting Stick (polearm - shaman can't use). Worn chest: Doomsayer's Robe 57.0 [33.0] (709, chapter 35) - no chest upgrade. **Pick Southern Watch Leggings**: an upgrade at 40 over Triprunner Dungarees 26.2 only by a hair and over Lightstep Leggings 14.6 (+11.4) if those are his legs; no upgrade over Apprentice Sorcerer's Slacks 73.7 (31b `[O]`) or Doomcaller's Pants 41.2 (35, if taken); it also sells best (69s 28c vs Tunic 57s 53c, Robe 43s 26c). If he wears Doomsayer's Robe and the Slacks, take the Leggings to sell.
2. **95615 In Memoriam** (choice + fixed Warding Candle): **Verger Greaves** (mail feet +7 Str +8 SP) 30.0 [22.0], usable from 40, over Sacristan Band (ring +7 Sta +2 SP) 4.0 [2.0]. Replaces Everlast Boots 28.5 [16.5] (35, if taken) or Kodo Rustler Boots 26.0 [21.0] (33) - a small upgrade **once he is 40** (wear it after the ding). Warding Candle: keep (5 charges, removes 1 Curse/Bane and 1 Disease).
3. **95064 Preventative Measures** (choice): Farholde Horns (mail head +13 Sta +12 AP) 12.0 [12.0]; Brute Slayer Band (ring +6 Int) 10.1 [10.1]. Neither beats Saltseer's Helm 48.3 (31b) / Wild Headdress 42.6 (29) or Coldwater Ring 27.6 / Tiger Band 22.5. **Take Farholde Horns to sell** (44s 92c vs 40s 5c).
4. **94877 Saving Sunnyglade** (choice): Neophyte's Wand (wand - can't use), Twilight Carver (1H sword - can't use). **Take Twilight Carver to sell** (1g 4s 84c vs 86s 60c).
5. **94861 Helping Hands** (choice): Hurley's Felling Axe (2H axe 27.73 dps +7 Str) 402.2; Curly's Chopper (1H axe 21.5 dps) 301.0. His 2H at this point is Bonebiter 583.5 (34 `[O]`) or Rock Pulverizer 471.1 (35) / Defender of Dalaran 469.8 (28) - no upgrade. **Take Hurley's Felling Axe to sell** (1g 28s 96c vs 1g 2s 79c).
6. **96009 High Stakes** (fixed): Lumber Luggers (leather hands +11 Str) 22.0 [22.0] < Prospector Gloves 31.5 (35) / Traveled Gloves 40.0 (39, conditional) - vendor (23s 1c).
7. **95066 The Rog'mar Situation** (fixed): Orc Bone Bow (bow - can't use) - vendor (80s 18c).
8. **95561 Apple of My Eye** (fixed): Goldenbark Apple (food, 841 health over 27 s) - eat.
**Deviations from the route plan**
- Plan: chapter 38 = the quest-level 36-40 block, ~52 quests, 104k XP. Spec: **40 plain quests, 78,385 XP** - the drop rule removes 94842, 94881, 95913 (+95961 conditional), 95984 (+95986), 95988 (+95957, 95975), 94829 (+94858); 95184 has no buyable source; 94925 is `[O]`; 94885 is a 1.6% drop-start (conditional block); 96081 moved to 40.
- Moved **into** 38 across the split (location): 95562 Cut Off the Heads (L41) and 94884 An Unsettling Discovery (L41) - same cave and same giver as 95642/95643. 95986 King of the Wild Plains (L41) would have joined Leg E but is out.
- Gnollhide/Bristle Hills Mystic Robe were the plan's 94679 picks (42.6 / 37.4 at band 30); at band 40 with Doomsayer's Robe worn neither is an upgrade: pick the Southern Watch Leggings (wearable at 40).
- New food-thread step (not in the plan): Recipe: Plain Ol' Paletusk (+10 Str, +5% kill XP; Cooking 185) at Martha Wellsworth.
- Hearth: plan says bind Farholde Keep - confirmed by qdb (Barracks Master Harlan, innkeeper flag).

### Spec 39 - Level 40: training, mail, mount, Storm / Heed / Tempest (drafted 11 Nov 2026)
**Totals**
- Plain quests (5): 79358 3,600; 96135 3,150; 96016 3,900; 670 3,150; 667 4,650 = **18,450 XP**, money 60s + 50s = **1g 10s** (matches the plan).
- [O]/conditional: 79242 3,900 XP + 1g.
- Spend at this stop: training 9g 50s (sheet 34-40) to 14g 90s (with laters) - or 4g 30s / 6g 70s if 36 trained 34-38; Artisan Skinning 5g; riding 100g (Friendly) + ram (unknown); flights. Gold check: the writer runs `python tooling/gold.py 39_Level40.lua:<line>` once 27-38 are written (plan-table estimate of plain quest money by the end of 39: ~29g 97s at end of 37 + 38's ~1g 80s + 1g 10s here = ~32g 87s, plus [O] dungeons and vendor income - the plan's "35-45g after training").
**Out**
- 79365 With Wind Beneath Your Wings: Horde-side (Wowhead side Horde; qdb race mask 162; ends at Rau Cliffrunner, Freewind Post). Brief correction.
- 79442 / 79360 / 79361 / 79364: Horde copies of the shaman chain (Orc/Tauren/Troll race masks).
- Bath'rah's other quests (1712/1713/1792, 8410-8413 class quests at 50-52, 96137 Ira's Dagger req 18 Duskwood) - not this band / not the route.
**Gear calls**
- **96016 The Tempest's Weapons -> Rage of the Storm** (2H mace 102-154, 3.60, 35.56 dps, +16 Str +15 Sta, +10% Stormstrike damage; 529.8 [529.8]). Quote the doc, do not re-derive: "Weapon verdict at 40: Rage of the Storm, by a hair. Rage 222.4 against Bonebiter 220.1 with Rockbiter, 218.2 against 217.8 with Windfury; without Stormstrike Bonebiter leads 170.3 to 167.5. The linear score (Bonebiter 583.5, Rage of the Storm 529.8) cannot see the Stormstrike bonus or the 3.6 speed that normalized Stormstrike rewards. A 1% gap means either is fine; Bonebiter is worth carrying if it arrives first, not worth a dungeon run on its own." Runner-ups: Lightning's Grasp (1H fist, 18.18 dps +6 Int +46 SP; 356.7 [310.7], shield set only), Tidebringer's Claw (1H fist, 18.13 dps +5 Sta, healing; 309.8 [281.8]). Replaces his 2H from round 1 - most likely Rock Pulverizer (739, chapter 35; 471.1) or Dwarven Charge (2240, [O] 36; 460.9) / Defender of Dalaran ([O] 28; 470.1) / Thermaplugg's Left Arm (Gnomeregan drop; 479.0); all below 529.8. If he holds Bonebiter, the doc says either is fine (take Rage: Windfury/Stormstrike case favours it).
- **Elementalist's Guard** (fixed, shield +9 Sta +6 Int, 2 mp5; 10.1, off-hand - not usable in the 2H build): vendor, sell 82s 81c.
- **667 Death From Below -> Coldwater Ring** (+3 Int +9 Spi; 27.6 [18.6]) over Seafire Band (+2 Str +2 Agi +10 Sta; 6.2 [6.2]). Replaces his weaker ring: Tiger Band (chapter 26 pick; 22.5 [17.5]) unless round 1 gave better (Purified Ring 30.3 from [O] 34b 3636; Electrocutioner Lagnut 23.5 Gnomeregan drop).
- **79242 No Honor Among Thieves (conditional) -> Traveled Gloves** (leather +9 Str +11 SP; 40.0 [29.0]) if his gloves are below 40: likely Prospector Gloves (704, chapter 35; 31.5) or Excavator Gauntlets (704's mail choice, usable from 40; 36.0) or Seawolf Gloves (664, 25.4). **If chapter 38 gave Prisoner Handwraps** (94927; cloth +12 Spi +15 SP; 60.0) no reward is an upgrade: take Soldier's Visor for its sell price (81s 38c vs Determined Band 66s 95c, Traveled Gloves 41s 42c). Soldier's Visor is **plate** (score_items lists it as usable at 28.0 - a gap in score_items.usable(), which does not exclude plate; see Unsure); Determined Band (+8 Sta, +9 AP) 9.0.
- 79358, 96135, 670: no item rewards (zone files).
**Deviations from the route plan**
- Plan step 4 says "fly Theramore -> the Great Lift road, or Gadgetzan if known": spec uses Theramore -> Ratchet flight and the Barrens road (Gadgetzan/Thalanaar undiscovered; Ratchet known from 26).
- Plan's order Ironforge -> Amberstill -> Arathi -> TN -> Alterac kept, but the data forces a **second Arathi pass**: 96135 starts and ends at Veyric and 96016 starts at Veyric (Wowhead quest page + qdb), so the TN trip returns to Arathi before Alterac.
- Plan's Mail note: "SkillRaceClassInfo row 145" confirmed: Availability 0, MinLevel 40; Eldrun's list has no Mail.
- Riding: plan "100g (90g at Honored)"; data gives 94g 74s at Honored (raw x0.90).
- Training total: plan quotes 34g 31s for 31-40 (all ranks incl. 32); spec lists the sheet picks (9g 50s / 14g 90s for 34-40) and the all-ranks figure 28g 71s for 34-40.
- 79242 placed as conditional [O] at Illari's cache (plan addendum: "the cache fits the level-40 Arathi visit").

### Spec 40 - Riverglades II 40-41 (drafted 11 Nov 2026)
**Totals**
- Plain quests turned in here: **14** - 94886 375; 94907 3,750; 95912 4,300; 96085 4,300; 96081 1,550; 96125 360; 96126 3,750; 94927 4,650; 94926 4,850; 94888 3,750; 94889 3,750; 94890 5,050; 96015 3,600; 94891 4,050 = **48,085 XP**. Picked up and carried: 94894 4,850 (Stormwind).
- `[O]`: 95991 4,300 (GROUP 2+, gear). Conditional pickup from 39: 95315 285.
- Conditional (Braedyn's call): 95935 4,450 + 1g 20s; 94887 2,100, 94892 4,200 (here), 94893 4,200 + 70s (Stormwind).
- Quest money (plain): 94889 30s = **30s**. (Plan said "Riverglades II's 12g": the zone JSON gives money only to 94889 in this block besides the conditional 95935 1g 20s and 94893 70s.)
**Out**
- 95935 Hail the Dragonslayer - drop rule (Head of Scaldaron 24.1%, a drop-start) - **written as a conditional block for Braedyn's call** (Leg D 24), not as plain.
- 94885 > 94887 > 94892 > 94893 - Field Marshal's Log 1.6% drop-start: conditional block only (38 Leg F / 40 Legs D-E).
- 95986 King of the Wild Plains, 95984 - out with the 16% beak (38.md).
- 94984 Tome of Twilight (after 94907) - Krol'dok Stronghold, round 2 (route plan).
- 95219 From Port to Port (req 40, Friz -> Feathermoon, Feralas) - round 2 (BRIEF correction).
- The 33 side-Both quests (Powderfuse, Eastsea, Gelinda Coppergleam 262399 at 30.2,69.0 (Wowhead map) with 95792/95934, Fuzzle 94961/94963, Sleebo 96063/96067) - chapter 41's.
**Gear calls**
1. **94927 Dunston Checks Out** (choice): **Prisoner Handwraps** (cloth hands +12 Spi +15 SP) **60.0 [33.0]** over Bolder'ok Loincloth (cloth legs +13 Spi +9 SP) 50.5 [28.5] and Dunston's Ogre Duster (1H mace 29.81 dps, 437.3 - 1H, not used by the 2H build). Replaces Traveled Gloves 40.0 (39, conditional) / Prospector Gloves 31.5 (35) / Excavator Gauntlets 36.0 (35's mail choice, from 40) - +20 or more. Exception: if his legs are Southern Watch Leggings 26.0 or Triprunner 26.2 (no Slacks 73.7 / Doomcaller's 41.2) the Loincloth gains +24.3 against the Handwraps' +20.0 over Traveled Gloves - take the Loincloth then; against Prospector Gloves (+28.5) the Handwraps still win.
2. **94926 Drop the Hammer** (fixed): **Pauldron of Order is PLATE** (shoulder +11 Str +7 Spi; score_items' usable() did not flag plate - it scores 39.5 but a shaman cannot wear plate) - vendor (81s 66c). The route plan's "Pauldron of Order 39.5" pick is wrong.
3. **95912 WANTED: Blademaster Kaijo** (choice): Bladewind (2H sword - shaman can't use), Bladewhisper's Namesake (thrown - can't use). **Take Bladewind to sell** (1g 68s 43c vs 98s 57c).
4. **96015 A Miner Problem** (fixed): Twilight Mine Light (cloth head +12 Sta +13 SP, +4 Mining) 26.0 [13.0] < Saltseer's Helm 48.3 (31b) / Wild Headdress 42.6 (29) - vendor (50s 18c).
5. **94890 Bring Me His Head** (choice): Twilight Overlord Drape (cloak +9 Sta +4 SP) 8.0 [4.0] < Glowing Thresher Cape 26.0 / Brilliant Cloak 20.4; Farholde Bastion (shield - 2H build). **Take Farholde Bastion to sell** (1g 16s 3c vs 53s 81c). 94891's Farholde Keep Tabard: keep or vendor (1g 25s sell) - cosmetic.
6. **[O] 95991 WANTED: Ghostmaw** (fixed): Crocskin Waders (leather legs +8 Str +11 Sta +6 Spi, +47 armor) 31.0 [25.0]. Upgrade only over Southern Watch Leggings 26.0 (38), Triprunner 26.2, Lightstep 14.6; not over Doomcaller's Pants 41.2 or Apprentice Sorcerer's Slacks 73.7.
7. **96085 Upstream Contamination** (fixed): Superior Healing Potion - keep.
- Not in this chapter (for completeness): 94893's and 94894's rewards are not in the zone JSON (none listed).
**Deviations from the route plan**
- Plan: ~24 quests, 82k XP, "Riverglades II's 12g". Spec: **14 plain, 48,085 XP, 30s** - 94885 chain is a 1.6% drop-start (conditional), 95935 is a 24% drop-start (conditional, Braedyn's call), 95562/94884 moved to 38 (location), 95986 out (16% beak chain), 95219/94984 round 2, 94894 carried to Stormwind. The plan's 12g money figure is not supported by zone_16591.json (largest single amounts: 95935 1g 20s, 94893 70s).
- Plan's gear notes corrected: Pauldron of Order is plate (vendor); Verger Greaves are now worn from 38 at the ding.
- 95219 From Port to Port: plan called it the Powderfuse flight hop; it is a Feralas delivery (BRIEF) and chapter 41 / round 2's.

### Spec 41 - Powderfuse Port 41-42 (drafted 11 Nov 2026)
**Totals**
- Plain (13): 95792 3,450; 95934 3,450; 95260 345; 95118 3,300; 95119 3,600; 95120 4,300; 95122 3,750; 95123 3,750; 95124 3,900; 95165 3,750; 95254 3,450; 96063 2,850; 96067 2,350 = **42,245 XP**.
- `[O]`: 95121 3,150.
- Conditional: 95267 3,450 (if offered without 95261); Friz block 95288 + 95293 + 95294 = 5,645 (+ 94928's 300 counted in chapter 38).
- Quest money (all plain): 95118 40s + 95119 60s + 95120 30s + 95122 30s + 95124 65s + 95254 30s = **2g 55s**. Optional/conditional quests pay 0. Plus vendored rewards up to 2g 88s 33c (harpoon 1g 58s 86c plain; bottle 1g 29s 47c conditional). 1-30 running total 17g 05s (gold.py); round-1 totals are the main session's.
- XP levels: all quest levels 38-45 against a level 41-42 player: none 6+ below, so full XP (verify.py's 80% rule does not apply).
**Out**
- 94961 Biting the Hand (2,350) - 20 Twilight Finger Bones at 16.5% overall (Shadowmancer 17.8%, Neophyte 18.3%, Raider 16.4%): drop rule, under 30% -> out; and **94963 Biting the Hand** (3,150, 50s; Fuzzle escort, ends at Fuzzle's Treasure 625582, 41.7,47.7 Wowhead map) behind it in the series (*>94963). Both are Sunnyglade (Fuzzle 45.6,47.8), chapter 38/40 ground anyway.
- 95261 It Takes Guts (3,450) - 15 Beast Entrails at 12.5% overall (best route mobs: Mature Paletusk 24.2%, Shore Crawler 20.2%, Sand Crawler 9.1%) -> out. Its 8 Rotflesh Mushrooms (object 630588, 100%) do not save it.
- 95267 The Monster Surfaces (3,450) - **out only if** Argo requires 95261 first (no series on Wowhead; qdb shows no prerequisite; the Big Ball o' Bait is made of entrails). Kept conditional in leg C/G.
- 95982 Not My Circus (2,850, no reward) - 10 Briny Seafood Stew = 20 Murloc Eye (730, not in the Riverglades) + 10 Tender Crab Meat (Swamp/STV) + 10 Hot Spices and Cooking 200: XP-only, optional-step test -> out.
- 95326 The Big Payback (3,000) - Ruzzgot's Shipment 20.44% (Venture Co. Agent 260429, STV): drop rule -> out; and **95327 All's Well That Ends Well** (3,150; starts at Ruzzgot, returns to Friz) presumably behind it (no Wowhead series; 95326 ends at Ruzzgot and 95327 starts there) -> out with it, unverified.
- 95295 I Know a Guy (315) -> 95322 Get the Goods (2,350) -> 95325 We've Been Robbed! (2,350; Venture Co. Ledger 630887 at STV 42.7,18.5 Wowhead map): the legs leave the zone for Booty Bay/STV; **not picked up** in round 1 (rule 9: no carry with no named hand-in chapter). Pointer for round 2 (STV 40-45 leftovers at 47-49 in the plan).
- 95296 Shipping and Handling (315, "Money: 10" requirement) -> 95383 Shipping and Handling (315) -> 95312 Coming to Collect (315) -> 95321 Tazzik's Dues (3,150) -> 95472 Consolation Prize (2,350, Sweat-Stained Shirt, sells 55s; returns to Friz): Tanaris (Steamwheedle Port 67.6,23.1 / Gadgetzan 51.6,27.4); **not picked up** in round 1. Pointer for round 2 Tanaris (44-46). 95296 follows 95294 in the series, so it is only offered if the Friz block was done.
- 95331 REUSE ME - placeholder, no XP: out.
- 95059 / 95062 Frazzlespark's Crate, 95219 From Port to Port, 94895 Lost Shipping Crate: not side "Both" (95059 and 95219 Alliance, 95062 and 94895 Horde); not in this chapter's pool - see Unsure for 95059.
- Pool reconciliation: the 32 side-"Both" rows of riverglades_sheet.txt are all placed above (13 plain, 1 `[O]`, 1 conditional, 3 in the conditional Friz block, 14 out/not picked up). pool30.py was not run (the zone has no zoneOrSort; the sheet is the id list).
**Gear calls**
No quest in this chapter has a reward choice (zone_16591.json itemchoices empty for all 32). Fixed rewards:
- 95120 -> **Rot-Covered Harpoon** (274963): Two-Hand **Polearm**, 62-94, speed 2.50, 31.20 dps, disease proc, 2x vs aquatic; sell 1g 58s 86c. **A shaman cannot use polearms**: client SkillRaceClassInfo 70888 has two rows for skill 229 (SkillLine "Polearms"): row 136 ClassMask 7 (warrior/paladin/hunter) and row 2483 ClassMask 1024 (druid); no row covers the shaman bit (64). score_items.py also marks Polearm unusable. Line: "vendor it (1g 58s 86c) - shamans cannot learn polearms". He keeps Rage of the Storm (529.8 at band 40, chapter 39) or Bonebiter (583.5) if it dropped; the harpoon would not compete anyway (31.2 dps vs 35.56 / 38.82).
- 95267 -> **Bottle of Powderfuse Port** (274948): Main Hand Dagger 16.11 dps, +7 Int, +21 spell damage / +63 healing; sell 1g 29s 47c. One-hander in a 2H build: vendor.
- 95254 -> Undermine Clam Chowder (16766): food, req 35, eat it.
- 96063 -> Riverglades Marsh Gas (274922): utility throwable, keep.
- 95121 -> Recipe: Briny Seafood Stew (274972): Requires Cooking (200); the stew (274971, req 25): 841 health over 27 s, well fed **+14 spell damage for 15 min and +5% experience from kills**. Reagents: Murloc Eye x2 (item **730**, the Classic crafting reagent - not the quest's Saltwater Murloc Eye 268344, which is a quest item; qdb drops 730 only from Classic murlocs in zones 11/40/148/44/331/130/45/36), Tender Crab Meat (12206; qdb drops only in Swamp of Sorrows (2) and STV (1)), Hot Spices (2692; vendors e.g. Nerrist Booty Bay, Micha Yance Southshore). Against the food thread (Mithril Head Trout +20 AP): +14 SP = 28 AP-equivalent on the central SP 2.0, 14 on the conservative 1.0; the kill-XP 5% is extra. So it is a **food-thread candidate** that the main session should put to Braedyn (Unsure); on the 555 Soothing Turtle Bisque precedent (cooking-recipe reward -> `[O]` with budget) it passes the optional-step test either way.
- Money from vendored rewards: 1g 58s 86c (harpoon) + 1g 29s 47c (bottle, if 95267) = up to **2g 88s 33c** toward the mount.
**Deviations from the route plan**
- **Chapter 41 itself is new** (approved 11 Nov after the 33 side-"Both" quests were found; the plan's Riverglades section counted only Alliance-flagged quests).
- Route plan says "95219 From Port to Port (req 40, 330) is the Powderfuse flight hop": brief correction - it is a Feathermoon delivery, round 2; Powderfuse Port has no flight path (TaxiNodes 3274/3275 unlinked). Not in this chapter.
- Plan's bind sequence ends at Farholde Keep; this spec keeps it (no rebind at Zizplink) - reasons in section 3.
- Plan said "buy the mount at ~43"; this chapter adds up to 2g 55s quest money + 2g 88s from vendored rewards toward it.
