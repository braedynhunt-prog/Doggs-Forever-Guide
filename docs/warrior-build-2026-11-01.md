# Forever Warrior 1-30 (Skyborne Protection Warrior): build record, 1 Nov 2026

Status: **built, 1 Nov 2026 (all four phases done).** The addon is `guide/Guidelime_ForeverWarrior/` with `Guidelime_ForeverWarrior.zip` beside it; rebuild after any change to `tooling/variants/skyborne_warrior/` with `python tooling/build_variant.py tooling/variants/skyborne_warrior/variant.json`. Plan: `docs/warrior-build-plan-2026-11-01.md`. Overlay spec: `docs/warrior-overlay-spec-2026-11-01.md`. The addon `guide/Guidelime_ForeverWarrior/` does not exist until Phase 4 builds it with `python tooling/build_variant.py tooling/variants/skyborne_warrior/variant.json`.

## Data used (all fresh on 1 Nov 2026, `python tooling/check_sources.py`: every row OK/INFO)
- QuestieDB Forever 1.0.9 (26 Oct), decoded 29 Oct: `tooling/qdb/*.json`.
- Client build 1.60.1.70707 (30 Oct): `tooling/client/1.60.1.70707/`.
- Wowhead Forever quest XP: every route zone browser-pulled 1 Nov 2026; Zephras Isle (16593) pulled for the first time 1 Nov (147 quests, no XP change against the Sep scrape).
- Item tooltips: `weights/tooltips/2026-11-01.json`, 639 items (Zephras rewards, Guard's set, Fire Hardened items, every reward choice of chapters 02-26 the prot emitter scores).
- Polestar Guides 0.2.6 (19 Oct, GPL-3) `compare/polestar-0.2.6/` and TUGs Forever (14 Oct) `compare/TUGs-1.12-2026-10-14/`: step order only, never data.
- Prep tables: `Claude outputs/warrior-phase2-prep/` (Zephras quests with the corrected Skyborne flag: 89 usable quests, 39,945 XP; island NPCs; the Guard's recipes).

## What was built
- **Tooling (Phase 0):** `weights/profiles.py` (enh / prot), `weights/prot_weights.py` + `docs/forever-prot-stat-weights.md`, tank stats in `score_items.parse()`, `gear_calls.py` / `dungeon_loot.py --profile --variant --emit`, `tooling/build_variant.py`, guidelib variant detection and Zephras Isle, per-folder baselines in `verify.py` and the hook. Alliance tools byte-identical before and after.
- **Chapters (Phase 2), hand-written under `tooling/variants/skyborne_warrior/chapters/`:**
  - `00s_ZephrasIsle1.lua` `[N 1-6 Zephras Isle]`: Thendal Grove, 16 quests, 3,215 XP, The Warrior's Path at 2, Skinning from the Harvesting Windstones book, carries The Next Step + The Adventurer.
  - `00t_ZephrasIsle2.lua` `[N 6-14 Zephras Isle]`: Shen'dar, Falaath, Western Watch, Windfield, Valanaar, Shrine of Akir, Shadowgale, the Lorthuna finale; 79 quest ids, 37,695 XP of required hand-ins, 94003 The Skybreaker Bulwark at 10 with the Zaal kill at the Shrine; exits about 14 with 94946 in the log.
  - `00u_DalaranToLochModan.lua` `[N 14 Dalaran to Loch Modan]`: Denaaris (Alterac map), the Skyborne Portal, Bolvar (93963 + 98021), Randal Emerson, Wu Shen, Stormwind flight point, tram, Mekkatorque + Magni, Ironforge flight point, A Visitor to Dun Morogh, Farsen's Dark Iron chain to Old Ironforge Incursion, South Gate. Carries 93963, 98021, 96393.
- **Professions:** Skinning + Mining (decided 1 Nov evening; the Guard's mail set needs ~34 Shadowgem and ~22 Pristine Leather by 25, so Blacksmithing is out), First Aid + Cooking + Fishing with the Alliance food thread.

## Decisions taken during the build
- The Reports (291) is not in the route: QuestieDB gives it prerequisites 287 + 98323 (Frostmane Hold / Secure the Mountain), a Dwarf chain a Skyborne never does.
- Stout to Kadrell (413/414) is out. The Classic warrior weapon chain was first dropped with the reason "race mask without Skyborne"; that was wrong (every Alliance warrior quest carries race mask 4294967373 = Human/Dwarf/Night Elf/Gnome + the 2^32 Skyborne bit, the same mask as the Fire Hardened chain) and the chain was restored as optional on 1 Nov 2026 (second pass, below).
- Camping 101: Mining is not taken on the island (no ore veins in the DB, hand-in NPC on the island); Fishing and Skinning Camping 101 are `[O]` hand-ins on the last Shen'dar pass.
- The Fire Hardened Mail chain runs 1698 -> 1699 -> 1702 only; 1701 needs Stonetalon chimaeras and Roogug (RFK), so it belongs to the 30-40 guide.

## In-game test list (unverified items written into the chapters)
Guidelime / data
1. Skyborne race filter in Guidelime 6.014 and whether 2^32-only quest masks hide steps.
2. Forever Dalaran has no Guidelime map: the two Dalaran steps sit on the Alterac Mountains map at 12.3,56.3 / 12.0,56.2 (QuestieDB zone 36). Where the Skyborne Portal really is, and where it lands in Stormwind.
3. Zephras XP values against the quest log (first browser pull of the zone).
Zephras Isle (00s / 00t)
4. Starting weapon and shield of a Skyborne warrior; Fevrath Skyhammer's shield prices (Large Round Shield 55 armor / Small Shield).
5. Whether the Harvesting Windstones reward book (Pelt Collecting for Beginners) teaches Skinning outright; Windstone Clusters per Raw Windstone.
6. Warrior ranks at 4, 6, 8, 10, 12, 14 on Forever (the chapters quote Classic: Charge/Rend at 4, Thunder Clap at 6).
7. The Skyborne racials (Walk on Air, Read Ley Line, +2% haste, +5% vs Elementals) and the tornado run-speed buff.
8. Whether Zerril Softbreeze (Cook), Messana Crestwind (Miner), Naleeia Tattermend (Medic) and Fenn Fairweather (Fisherman) in Shen'dar teach their professions; Halavuul Cragwind (Valanaar) is the only "Mining Trainer".
9. Whether Camping 101: Cooking completes on learning Cooking; inn / hearth binding on the island (DB innkeepers Coriella Calmbreeze, Donaal Downbreeze); which water near Fenn is fishable; ore veins on the island (none in the DB).
10. Charred Wolf Meat on Forever; the skill needed for Recipe: Skywall Souffle and Recipe: Pincer Bites; Recipe: Longjaw Mud Snapper sold by Nyalah Brightfire (bought at ~10, learned at Cooking 50).
11. 94003 The Skybreaker Bulwark: whether the quest or Seena's level-10 training gives Defensive Stance; Stormforged Protector stats; Zaal Stormshield's real position (DB 56.6,50.4 at the Shrine of Akir; Polestar's data put him by Hanaa's camp).
12. Every Zephras quest-item drop rate (unknown; kill lines carry budgets of ~15-35 kills); bow and dagger weapon skill for a Skyborne warrior (Bow of Hours, Quickblade's Dagger).
13. Boarding the skycutter at the High Order Dockmaster (65.7,83.2).
Join leg (00u)
14. QC objective indices for 93963 (Questie order: 1 Randal, 2 Mekkatorque, 3 Magni, 4 Tyrande).
15. The Stormwind Auction House location; the tram coordinate 73.1,49.2 (the Alliance guide's own number).
16. The Dark Iron Map drop rate (Dark Iron Spy / Captain Beld; budget ~15 spies after the 10).
Mainland (overlay, Phase 3)
17. Fire Hardened chain: 1698 offered by Wu Shen to a Skyborne; the Rethban Gauntlet at 22.
18. Warrior trainer stops: Stormwind (Wu Shen / Ilsa Corbin / Ander Germaine), Ironforge (Kelv Sternhammer / Kelstrum Stonebreaker / Bilban Tosslespanner), Darnassus (Arias'ta Bladesinger / Darnath Bladesinger / Sildanair).
19. Exploring the Alliance: Tyrande in Darnassus at 23-24, hand-in to Bolvar at 26 (Cloak of the Honored Guest: 14 armor +1 Sta +1 AP).
20. The prot gear picks (reasoning-only weights): whether the 1H + shield picks feel right in play; Defense's real value at 20-30.

## Phase 3: the overlay (chapters 02-26)
Three Opus subagents (blocks 02-09, 10-17, 18-26) wrote `tooling/variants/skyborne_warrior/overlay/<key>.txt`, 291 operations in all, after the builder gained a literal-text anchor (`T <text>`) for untagged notes. What the overlay does: restores the route steps the builder dropped with the Dwarf/Human tags (Kadrell's Rat Catching and Stormpike's Task, the Thelsamar-Ironforge flights in place of Honor Students, Dungar's flights, the tram hop), rewrites every carry-over log and check line, adds the warrior class thread (Wu Shen in 05/07/10/15/18/25, Kelv Sternhammer in 02/03/04/24, Arias'ta Bladesinger in 11/20; `[QC93963,4]` at Tyrande in 11 and `[QT93963]` at Bolvar in 15; `[QT98021]` at Gryan in 05; 1698 at Wu Shen in 10, the Rethban Gauntlet and The Shieldsmith at Yorus in 10, `[QT1702]` at Furen in 15), replaces the Leatherworking decision (14) with the Skinning + Mining note, rewords every shaman / hunter / duo note into tank notes (Defensive Stance, Thunder Clap, Taunt, Shield Block, Shield Bash), places `@gear-dungeon` loot calls per boss in 03, 07, 08, 13, 15, 22, 24, 26 (no trash groups), and adds hand notes for fixed rewards and weak picks. Block C made one flow change: the Expert First Aid book is bought at Stromgarde on the chapter-19 Arathi hop (the shaman bought it on a chapter-25 trip that drops). The build report lists 29 remaining flagged lines, all mob or quest names (Stonesplinter Shaman, A Hunter's Boast, Totem of Infliction, Spirit Healer and the like).

## Phase 4: the build
- `python tooling/build_variant.py tooling/variants/skyborne_warrior/variant.json`: 28 chapters (00s, 00t, 00u, 02-26), 270 lines dropped, 48 stripped, 291 overlay operations, 83 generated gear lines placed (0 unplaced, 0 unstated), 9 non-gear rewards worded by hand, zip and report written.
- Checks on the folder (`FOREVER_GUIDE=guide/Guidelime_ForeverWarrior`): `check_guide.py` 1468 quest events, 0 flow problems, the 7 cosmetic findings = `tooling/check_guide_baseline_Guidelime_ForeverWarrior.txt`; `verify.py --all` 31 findings = `tooling/verify_baseline_Guidelime_ForeverWarrior.txt`, every one the same message as an Alliance finding (the Alliance has six more, all on its Dun Morogh chapters); `tarcheck.py` 20 lines, a subset of the Alliance's 30. The hook checks each folder against its own baselines and flags edits inside the generated folder.
- Main-session review: every built chapter read end to end; a residual sweep for class, race and duo wording found one leftover (Chok'sul "tank friend", fixed through the overlay).
- Not done, by design: installing into the WoW AddOns folder (only when asked); playing it (the test list above).

## Known cosmetic leftovers
- Deleted lines leave their blank line behind, so a few chapters have two blank lines in a row (02 after the Call of Fire lines, 25 before the harbour note).
- Chapter 25's `[N]` title still says "Arathi" although the warrior's Arathi leg moved to chapter 19 (24's `[NX]` points at the title).
- The one inline gear line left (23, Yeti Fur Cloak) already reads right for a warrior.

## Second pass, 1 Nov 2026 (evening): the optional Classic weapon chain, Guard's-set wording
- **Restored as `[O][A Warrior]` lines** (data: QuestieDB Forever 1.0.9, Wowhead XP pulled 1 Nov, tooltips fetched 1 Nov): the Dwarf and Human level-10 chains are mutually exclusive in the DB (1639 Bartleby the Drunk `exclusiveTo` 1678 Vejrek / 1683 Vorlus Vilehoof and vice versa), but 1680 Tormus Deepforge accepts 1639 as its prerequisite, so the route uses the Stormwind start and never visits Vejrek (Dun Morogh 27.8,58.0). 00u: 1639 + 1640 (Harry Burlguard 77.1,53.3 / Bartleby 76.8,52.6, Pig and Whistle) at 14, 1680 at Muren Stormpike (70.8,90.3, beside Kelv), 1681 at Tormus Deepforge (Great Forge 48.6,42.5), Umbral Ore from Ironband's Strongbox (object 85562, Dun Morogh 78.0,62.2, the Dark Iron camp of Nip 'Em in the Bud). 02: 1681 hand-in, 1682 Grey Iron Weapons at Tormus on the Ironforge pass (630 XP). 15: 1665 Bartleby's Mug, 1666 Marshal Haggard after the Wu Shen stop. 16: 1666 hand-in, 1667 Dead-tooth Jack, badge from Dead-tooth's Strongbox (object 85563, Elwynn 89.3,78.9), 840 XP. Total 3,355 XP; nothing is carried through chapters 02-14 (Bartleby's Mug waits for 15).
- **Weapons** (prot weights, `weights/tooltips/2026-11-01.json`): Umbral Axe 7.8 dps +1 Sta scores 48.2, the Mace / Sword / Dagger 7.6-7.7 dps +1 Sta 47.2-47.4, Quickblade's Dagger 41.5 - a small upgrade for the rest of chapter 02 (Invader's Mace at its end). Haggard's four are the same stats, XP only at 27.
- **Guard's set wording cut:** the 00s note said "buy a Guard's piece on the AH if one is cheap" and chapter 14 said "check the Auction House for a cheap Guard's piece"; every Guard's piece in the tooltip cache is bind on pickup, so both clauses went (00s keeps the reason for no Blacksmithing; 14 now ends at "keep Skinning + Mining to 30"). Blacksmithing stays off (Braedyn, 1 Nov).
- Checks after the rebuild: `check_guide.py` 1487 quest events, 0 flow problems, the same 7 cosmetic findings; `verify.py --all` 31 findings, baseline rewritten for three line-number shifts (same messages); `tarcheck.py` 20 lines, unchanged. TOC notes bumped (version stays 2026.11.01).
- Test list additions: 21. whether Harry Burlguard offers Bartleby the Drunk to a Skyborne, and Muren Stormpike Tormus Deepforge after Beat Bartleby (the DB's prerequisite list; Classic required the race's own duel quest). 22. Dead-tooth's Strongbox at Elwynn 89.3,78.9 and whether a Dead-tooth Jack mob guards it (the Forever DB has no such NPC).
