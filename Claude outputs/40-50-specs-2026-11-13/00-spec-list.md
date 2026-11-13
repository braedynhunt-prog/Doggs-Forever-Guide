# Round 2 (levels 42-50): spec list for Braedyn's approval - 13 Nov 2026

Sixteen chapter specs, one per chapter file `42`-`57`, drafted by Opus agents (57 by the main session) against `docs/40-50-plan-2026-11-12.md` (second revision, with the rulings the specs produced). The newest draft of each chapter is the spec: `45-draft3.md`, `48-draft3.md` to `57-draft3.md`, and `42-draft2.md`, `43-draft2.md`, `44-draft2.md`, `46-draft2.md`, `47-draft2.md` (written before the second revision; the amendments below bring them in line and are applied when the chapters are written). Nothing under `guide/` has been touched.

Checks run on the set (13 Nov): every required and every optional quest of the route file appears in its chapter's spec; `python tooling/route_xp.py docs/40-50-route-2026-11-12.txt` prints no prerequisite fault and no place fault; each spec's totals equal its row below.

## Titles and totals

| file | `[N]` title | level in > out | required | quest XP | conditional XP | starts > ends | hearth on exit |
|---|---|---|---|---|---|---|---|
| `42_RivergladesIII.lua` | 42-43 Riverglades | 42.0 > 42.0 | 0 | 0 | 10,500 | Farholde Keep > Farholde Keep | Farholde Keep |
| `43_KroldokStronghold.lua` | 42-43 Krol'dok Stronghold | 42.0 > 42.2 | 3 | 14,350 | 21,250 | Farholde Keep > Ironforge | Farholde Keep |
| `44_StormwindAeriePeak.lua` | 42-43 Stormwind and Aerie Peak | 42.2 > 42.4 | 7 | 12,290 | 9,050 | Ironforge > Aerie Peak | Stormwind |
| `45_BootyBay.lua` | 42-43 Stranglethorn Vale | 42.4 > 42.7 | 7 | 16,215 | 3,150 | Aerie Peak > the Ratchet boat | Booty Bay |
| `46_TanarisI.lua` | 42-44 Tanaris | 42.7 > 43.2 | 11 | 33,630 | 8,945 | Ratchet > Gadgetzan | Gadgetzan |
| `47_FeralasI.lua` | 43-44 Feralas | 43.2 > 43.4 | 12 | 18,725 | 12,200 | Gadgetzan > Thalanaar | Feathermoon |
| `48_Hinterlands.lua` | 43-44 The Hinterlands | 43.4 > 43.8 | 6 | 23,350 | 15,500 | Thalanaar > Ironforge | Aerie Peak |
| `49_StranglethornCape.lua` | 43-45 Stranglethorn Vale | 43.8 > 44.0 | 5 | 19,400 | 10,250 | Ironforge > the Ratchet boat | Booty Bay |
| `50_FeralasII.lua` | 44-45 Feralas | 44.0 > 44.5 | 9 | 31,255 | 4,700 | Ratchet > Feathermoon | Feathermoon |
| `51_ZulFarrak.lua` | 44-45 Zul'Farrak | 44.5 > 44.7 | 4 | 19,200 | 11,405 | Feathermoon > Gadgetzan | Gadgetzan |
| `52_SearingGorge.lua` | 44-46 Searing Gorge | 44.7 > 45.5 | 18 | 60,540 | 470 | Gadgetzan > Menethil Harbor | Ironforge |
| `53_TanarisII.lua` | 45-47 Tanaris | 45.5 > 46.1 | 11 | 41,580 | 13,400 | Menethil > Gadgetzan | Gadgetzan |
| `54_Maraudon.lua` | 46-47 Maraudon | 46.1 > 46.4 | 5 | 25,900 | 8,700 | Gadgetzan > Nijel's Point | Gadgetzan |
| `55_Azshara.lua` | 46-48 Azshara | 46.4 > 47.4 | 23 | 84,755 | 71,550 | Nijel's Point > Talrendis Point | Talrendis Point |
| `56_UnGoro.lua` | 47-49 Un'Goro Crater | 47.4 > 48.3 | 18 | 73,230 | 9,200 | Talrendis Point > Marshal's Refuge | Gadgetzan |
| `57_Ironforge.lua` | 48-49 Ironforge | 48.3 > 48.4 | 3 | 12,770 | 0 | Marshal's Refuge > Ironforge | Ironforge |
| | **total** | 42.0 > **48.4** | **142** | **487,190** | 210,270 | | |

Levels are required quest XP at the 65% share with required levels ignored. With them enforced: at exactly 65% he reaches Azshara's nine level-47 quests about 6,700 XP of any kind short (some 25 kills or one conditional quest); at 64% the route clears and ends at 48.0 with ten Un'Goro quests (required level 48-50) closed; at 60% it ends at 48.6 with five closed. `[NX]` chains each chapter to the next; chapter 41 gets its `[NX]` to 42 at the release; 57 has none.

## What each chapter does

- **42 Riverglades: pickups and loose ends.** One ridden loop from Farholde Keep: Tome of Twilight (Ashe Amberhall) and Eye of Mugg (Demar Brant) for the dungeon, Friz Frazzlespark's I Know a Guy and From Port to Port, Twilight Mementos at Sergeant Riftan (grind / luck), and three "if offered" quests (Biting the Hand, Her World, News to Farholde). No hearth used.
- **43 Krol'dok Stronghold.** Ironforge (level 42 row), Southshore and the Dalaran crater for Vengeance of the Highborne, hearth back, the one run (two boss-item quests, both one kill), crater hand-in, ends in Ironforge. Bigger Rock on Bigger Stick from Eye of Mugg is the weapon call (ties Rage of the Storm and Bonebiter within 1%).
- **44 Stormwind, the Temple door and Aerie Peak.** Bind Stormwind; Darkshire and Nethergarde by flight for the supply quests, ride to the Pool of Tears for In Search of The Temple, hearth, To The Hinterlands, fly to Aerie Peak: Talonaxe, Rhapsody Shindigger, and Rhapsody's Kalimdor Kocktail picked up. Conditional hand-ins in Stormwind (Delivering Closure, The Twilight Threat).
- **45 Booty Bay.** Bind Booty Bay. The gorillas north-east of town for Scaring Shaky (about 19 kills; keep every Gorilla Fang), the road north to Nesingwary (Raptor Mastery) and the Venture Co. ledger (We've Been Robbed!, The Big Payback: about 4 Agents), hearth, hand-ins, pickups for later (All's Well That Ends Well, Stoley's Debt, Tran'rek, Voodoo Dues), the Ratchet boat.
- **46 Tanaris I.** Road from Ratchet (unverified), Gadgetzan flight point and bind. Rocs for three gizzards, the water survey, Gnomish Garbage, the Wastewander quests with the pouches, Steamwheedle Port and Lost Rigger Cove (Southsea Shakedown, Stoley's Shipment, Andre Firebeard: one kill only), Caliph Scorpidsting last. Screecher Spirits picked up.
- **47 Feralas I.** Road to Thalanaar and the Feathermoon ferry (unverified), both flight points, bind Feathermoon. Ironfur bears and Groddoc apes for the livers, the Solarsal naga, the Gordunni ogres by level, the screechers, the Missing Courier chain to the Woodpaw gnolls, Thalanaar Delivery ends the chapter at Thalanaar.
- **48 The Hinterlands.** Theramore, the Menethil boat, Farholde Keep and the ride to Powderfuse Port (All's Well That Ends Well; Friz's two conditional hand-ins), then Aerie Peak (bind): Kocktail hand-in, Witherbark Cages, Skulk Rock, the Altar of Zul with Troll Necklace Bounty (Axe Throwers on the lower slopes, about 16 kills), ends in Ironforge by flight.
- **49 Nethergarde and the Cape.** Ironforge (level 44 row; Tabetha's Task from Bink), Stormwind (Rhapsody's Tale), Nethergarde (Thadius Grimshade, Nekrum's Medallion taken), Booty Bay (bind): Deliver to MacKinley, Stranglethorn Fever (ten fangs, then Unbagwa's summons to Mokk), the three Voodoo Dues ogres as a one-kill try, the Bloodsail ships last (three captains to level 48; Cortello's scroll picked up for round 3). Ratchet boat.
- **50 Feralas II.** Theramore: Sword in the Slime, ride to Tabetha (Tabetha's Task in, Tiara of the Deep out, the oozes for the sword), Thalanaar, the Woodpaw camps and the Writhing Deep, Freedom for All Creatures and Doling Justice, bind Feathermoon, the giants last (The Giant Guardian, Wandering Shay's escort).
- **51 Zul'Farrak.** Feathermoon to Gadgetzan by flight (bind), Screecher Spirits to Yeh'kinya first (opens The Prophecy of Mosh'aru), one run: Divino-matic Rod, Scarab Shells (collection, about 14 kills), the Prophecy, and three carried quests (Nekrum's Medallion, Tiara of the Deep, The Witch Doctor's Head). Troll Temper and Gahz'rilla optional. The Minotaur (2H axe) is the drop to roll on.
- **52 Tabetha, Nethergarde, the crater and the Searing Gorge.** The eastern trip at 45: Theramore and Tabetha (Tiara), the Menethil boat, Southshore and the crater (Witch Doctor's Head), Ironforge (bind, train), Stormwind to Nethergarde (Medallion, The Divination), hearth, Thelsamar and the Badlands road into the Gorge: the Suntara escort and Caught! first, the five level-45 quests when he turns 45 there, Thorium Point's flight point, Ironforge for the four Explorers' League pickups, Menethil.
- **53 Tanaris II and Uldum.** Boat to Theramore, flight to Gadgetzan (bind). The Gahz'ridian ornaments, the Dunemaul compound, the Uldum pedestal, the Noxious Lair and the silithid chain, Thistleshrub Valley, Tooga's escort, the Gaping Chasm, the egg-o-matic hand-in.
- **54 Maraudon.** Gadgetzan - Theramore - Nijel's Point, the ride to the door. One full run in the order outer cave, purple wing, orange wing, inner falls (the agent's recommendation over a split: a second visit gains under a tenth of a level and walks a wing twice). Seed of Life is taken and carried to round 3. Gatorbite Axe (Rotgrip, level 48) is the drop to roll on.
- **55 Darnassus and Azshara.** Nijel's Point - Auberdine - Rut'theran: six hand-ins in Darnassus and Rut'theran, Sisters In Duty and The Borrower taken. Astranaar and the road to Talrendis Point (bind, flight point). The level 45-46 quests first (Home on the Range: about 11 Runners), Saria Fairmoon's chain and the other level-47 quests after, Tymor's runes and the hand-in on Xiggs's island last.
- **56 Un'Goro Crater.** Talrendis - Theramore - Gadgetzan (The Borrower; bind), the ride into the crater, Marshal's Refuge. Written in four tiers by required level so it can be left after any of them: A at 47 (the raft, the pack, Crystals of Power and the three pylons: 25,080 XP), B at 48 (23,500), C at 49 (10,550), D at 50 (14,100). What is not open when he leaves starts round 3.
- **57 Ironforge: the round's hand-ins.** Marshal's Refuge - Gadgetzan - Theramore (Shadowshard Fragments hand-in if held), Menethil, Ironforge (bind): Return to Ironforge, A Future Task, Return to Tymor, the training rows 46 / 48 (50 if reached).

## Amendments the main session applies when the chapters are written

These come from reconciling the specs with each other and with the second revision; none changes the plan's quest list.
1. **42**: Her World's gather line gets no `[G]` (the Wildflower object has no position in any data); the line says "near Gray Dawnbright, unverified". Frazzlespark's Crate (280 XP, not in the pool) is not added.
2. **43**: add the pickup of The Witch Doctor's Head 96770 from Archmage Lan'dalock (Alterac 15.3,73.9) on the first crater visit. The level 42 row is bought here; chapter 44's trainer line stays "only if not bought".
3. **44**: the Stormwind bind stands (the spec's own proposal).
4. **45**: collect all ten Gorilla Fangs here (about 24 gorilla kills instead of 19), so chapter 49 goes straight to Unbagwa. Stranglethorn Fever itself stays in chapter 49 (Mokk is level 44).
5. **46**: add the Tran'rek 2864 hand-in and the Scarab Shells 2865 pickup at Tran'rek, the pickup of The Super Egg-O-Matic 2741 (needs 42), and Deliver to MacKinley as a carry to chapter 49. Ship Schedules and the OOX-17 pair become "if it drops" lines. The Gahz'rilla pickup at the Mirage Raceway is not added.
6. **47**: the OOX-22 pair becomes an "if the beacon drops" block. The Writhing Deep is not taken here (chapter 50 takes it at the same backpacks).
7. **50**: add the Hippogryph Egg for the egg-o-matic (object 141931, Feralas 53.7-58.6,74.4-78.2; mobs around it to be read when the chapter is written). Fuel for the Zapping is out.
8. **52**: Prayer to Elune is an "if he can be reached" line; The Key to Freedom is plain with the budget (key 5.1%, about 20 kills, covered by the 30 Dark Iron of Culling the Competition); Return to the Hinterlands is not picked up.
9. **53**: Oasis is an "if Tooga offers both" line.
10. **55**: Winter Frontier Fishery is an "if you can fish the squid" line; the two Gorn One Eye quests get no line (they start in Felwood).
11. **56**: Williden's Journal is an "if the journal has dropped" line (0.97% per kill); the tier gates are `[OC]` notes placed before each tier's first pickup.
12. **57**: as written.

## Calls for Braedyn (each has a default; say only where you disagree)

1. **Maraudon in one run at about 46** (default yes). The Princess is level 51; the agent's alternative is to split off the inner falls and run them from chapter 55's start, at the same level.
2. **Zul'Farrak at about 44.5** (default yes; it is the price of the eastern trip at 45). The dungeon's trash is 43-47, bosses 45-48.
3. **Feralas II's giants leg** (The Giant Guardian, Wandering Shay: 7,950 XP) is 3-8 levels over him at about 44.3 and elite giants stand beside the quest giver. Default: keep both required and last in the chapter, with a level-check line that says to skip the leg if under 45 - there is no later Feralas visit, so skipped means lost to round 2.
4. **The Bloodsail Buccaneers' last captain** (Firallon, level 48, at about 44): default keep required and last; if he cannot be killed the quest waits for round 3.
5. **Azshara's bind at Talrendis Point** (default yes): chapter 56 then flies Talrendis - Theramore - Gadgetzan and rebinds.

## In-game test list (the items that can change a chapter)

- The Altar of Zul: whether the level-50 elite Keepers stand on the trigger (it gates Thadius Grimshade, Nekrum's Medallion and The Divination).
- Skulk Rock, the Searing Gorge and Feralas: the DB places level 50-62 Forever-only creatures (Dream mobs, Firelands Invaders, Vale Screamers) across quest areas; whether they are live and hostile.
- Un'Goro: the level-60 Venomhide Ravasaurs the DB puts on Torwa Pathfinder; whether quest objects can be clicked below their quest's level.
- Offers: All's Well That Ends Well after The Big Payback; Tiara of the Deep without Tabetha's Task; the "if offered" quests of chapter 42; the Ursolan furbolgs to Alliance.
- Roads and boats not in the data: Ratchet - Gadgetzan, Gadgetzan - Thalanaar, the Feathermoon ferry, the Badlands road into the Searing Gorge, Astranaar - Talrendis Point, Gadgetzan - Marshal's Refuge, Menethil - Theramore.
- The Bloodsail Trunk's position (Get the Goods); the Stronghold's door and mob levels; the trainer's price (raw or 5% less).
Each spec's section 9 carries its full list; the build doc will hold the merged one.

## After approval

Chapters are written by Opus agents in waves of four from these specs and the amendments (never two agents on one file), each read against its spec and the data by the main session; then `check_guide.py`, `verify.py`, `tarcheck.py`, `gold.py`, both variants' `build_variant.py`, the TOC and zip, the build doc, and the release.
