# Forever Alliance 20-30 — build notes (18 Oct 2026)

The 20-30 route exists: chapters 08-26 of `Guidelime_ForeverAlliance` on Braedyn's PC (`C:\Users\Braedyn\Documents\WoW Forever Atlas\guide\Guidelime_ForeverAlliance\`, zip beside the folder, 171 KB, TOC version 2026.10.18, group renamed **"Forever Alliance 1-30"** across all 29 chapter files; the old `08_LooseEnds.lua` checklist moved to `archive\guide-20-30-build-2026-10-18\`). Built as: route plan by Claude (this chat), data digest + one Sonnet agent per chapter (reading `tooling\qinfo.py`, the Forever DB, Wowhead XP, `tip.py` tooltips, TUGs for travel tricks), then a mechanical verification pass. Nothing has been tested in game.

## Chapters

| # | file | `[N]` | what | quest XP (shaman view, incl. optional/group) |
|---|---|---|---|---|
| 08 | 08_RuinsOfLordaeron | 20-21 Ruins of Lordaeron | boat trip north, the new 16-22 dungeon, Stormwind hand-ins (written by the retried run of this chat) | 11.3k |
| 09 | 09_LochModanMenethil | 21-22 Loch Modan and Menethil | dam, Loch Modan elites + A Dark Threat Looms (group), Dun Algaz, Menethil coast; shaman Call of Water 1-3 | 44k (13k group) |
| 10 | 10_Redridge2 | 22-23 Redridge | Goldshire/Azora walk-in, Lakeshire 20-25 quests, Stockade pickup 386, Red Waterskin | 21.6k |
| 11 | 11_Darkshore | 23-24 Darkshore | boat, Darnassus BFD pickups, Darkshore 17-20 quests in one loop, Kerlonian escort into Ashenvale | 43k (29k core) |
| 12 | 12_Ashenvale | 24-25 Ashenvale | Maestra's Post, Astranaar, Raene/Bathran/Talen/Velene loops, ends at the Zoram Strand | 29k |
| 13 | 13_Blackfathom | 25-26 Blackfathom Deeps | 5 quests inside (1275, 971, 1198→1200, 1199), hearth home | 2.4k now + 11k banked |
| 14 | 14_Duskwood | 25-26 Duskwood: Darkshire | walk in, Night Watch 1-2, Totem, Valor, Stars, Raven Hill, Worgen 1-2, Stalvan 1-3 via the hearth | 25k |
| 15 | 15_Stockade | 26-27 The Stockade | Stormwind round, the Stockade (5 quests), the Unsent Letter chain to An Audience with the King, Stalvan SW parts, shaman Ironforge hop | 28.7k |
| 16 | 16_RedridgeEastvale | 26-27 Redridge and Eastvale | bounties, Morganth, Gar'im, Songblade Search pickup, Eastvale Stalvan, Theocritus | 30k |
| 17 | 17_Duskwood2 | 27-28 Duskwood: Sven and the Hermit | Sven chain, Hermit chain to Bride of the Embalmer, Worgen 3-4, Stalvan finale, Night Watch 3 | 46k |
| 18 | 18_Wetlands1 | 28-29 Wetlands: Menethil and Whelgar | Stormwind pass (Farthing, Shoni, Grayson, Milton), Ironforge train, Menethil wreck chain, Whelgar (Ormer, Uncovering the Past, the Dragonmaw-arc pickups), shaman Hervdana | 25k |
| 19 | 19_Wetlands2 | 28-29 Wetlands: Dun Modr and the Dragonmaw | Greenwarden, Howin's Dragonmaw arc, Dun Modr (Thandol Span, Dark Iron War, Lost chain), Arathi bridge jump + Refuge Pointe FP, Nek'rosh block | 67k (36k group) |
| 20 | 20_Darnassus | 29-30 Darnassus and Astranaar | boat to Auberdine, Darnassus hand-ins (BFD, Prospector), Astranaar pickups, Stonetalon dip for Castpipe's Task | 17k |
| 21 | 21_AshenvaleEast | 29-30 Ashenvale: the East | Raene 4-12, Kayneth, Maseara, satyrs, Fallen Sky Lake, Howling Vale, optional Althalaxx finale on the way to the boat | 49k |
| 22 | 22_ExcavationSite | 29-30 Excavation Site: Wetlands | Menethil/Whelgar pickups, the new dungeon (all 9 quests), shaman Call of Water 6-8 via the hearth | 24.8k |
| 23 | 23_Hillsbrad | 30-31 Hillsbrad and Silverpine | Down the Coast chain, Hoard, Brewer's Trade, turtles, optional yeti/Syndicate/Preserving Knowledge; shaman Silverpine → Water Totem at Norric | 26.5k |
| 24 | 24_Gnomeregan | 30-31 Gnomeregan | Ironforge round (Magellas, Karnik, Magni, Balloo chain), Kharanos/Techbot outside, the run with all 20 quests incl. Sparklematic + the ring chain | 44k |
| 25 | 25_LooseEnds30 | 30-31 Loose Ends: Stormwind, Duskwood and Arathi | Missing Diplomat to Mikhail, Morbent Fel, Mor'Ladim, Dorin, Reassignment; shaman Call of Air → Elemental Aid | 31.7k |
| 26 | 26_RazorfenKraul | 30-31 Razorfen Kraul | Barrens ride, Ratchet, RFK (Willix, Mortality Wanes, Blueleaf Tubers, shaman Elemental Aid → Veyric) | 10.9k |

Totals (quest XP only, Dwarf Shaman view, turned-in basis, everything incl. group blocks): 1-20 = 143k, 20-30 chapters = 568k. 20→30 needs 281k, so **on quest XP alone the shaman is 30 at the end of chapter 18**; with dungeon/mob XP it will be 30 around chapters 16-17 and everything after is 30-32 content (deliberate: launch has the 60 cap and these are the right next dungeons). A Human Hunter sees slightly less (no Call of Water/Air; ~35 Forever quests carry a "no Human" race flag on Wowhead that Questie disagrees with — unresolved until tested).

## Verification done
- `tooling\check_guide.py` (now scans all chapters, group "1-30", level band read from each `[N]`, Kalimdor/northern zones): 1,599 quest events across 29 files, **0 flow problems** — every pickup has a later turn-in or `[QS]`, every turn-in an earlier pickup, prerequisites in order, no pickup above its chapter's level band. The 7 remaining findings are the known cosmetic "optional step without [G]" lines in 03/05/07/08.
- `tooling\tarcheck.py` on 08-26: clean (only Lady Dena Kennedy, a new NPC with no DB spawn). Fixed in passing: Thulman/Einris line in 08, Bretta Goldfury (IF ammo vendor) in 03/04 was 18 units off.
- `[N]`/`[NX]` chain 00a → 26 intact; every title is a level range.
- Quest-log simulation (shaman, required steps only): peaks 23-24 in chapters 18-19 and 21 in 11/21, ~3 of which are stale 1-20 leftovers the 09 opener now tells you to abandon (`[QS217] [QS271] [QS95041]`). Classic's log is 20; chapters 18, 19 and 22 carry a "log space" note saying what to drop. If Forever's log is 25 there is no issue. (Later note, 25 Oct: Forever's quest log cap is 40, so log-space management is unneeded.)
- Agents' own judgement calls that changed the plan (all in the files): Gath'Ilzogg optional (four elites on him); Preserving Knowledge is Crushridge Hold with 34-38 elites, optional; Techbot is OUTSIDE Gnomeregan; Prehistoric Prism follows a 27% relic drop (optional); Veyric's Tempest's Weapons / Heed My Call are level-40 quests (left); Storm, Earth and Fire: Wowhead says Horde, Questie says both — left out; Satyr Slaying and the Zoram Strand/Pridewings skipped (far west, low XP); Darkshore north needs two trips; Call of Water 94502 is at Stendel's Pond (Westfall) and the Manifestation for 94503/94505 in Silverpine (Wowhead's zone filing), chapter 22 notes the doubt.

## What is unverified (first in-game test list for 20-30)
1. Whether Guidelime accepts the new tags the agents used: `[CI itemId,count]` (buy Silk Cloth, chapter 15) and `[UI itemId]` (use the Blue Waterskin, chapter 20) — if the parser rejects them, those two lines need rewording.
2. Dungeon layouts/boss notes for the Excavation Site and Ruins of Lordaeron (web sources only), and the Classic-era boss notes for BFD/Stockade/Gnomer/RFK.
3. Three NPC positions with no DB spawn: Lady Dena Kennedy (Stormwind, ch08), Ardin Grassman and Daewyn (inside the Excavation Site).
4. Flight routing assumptions (Stormwind → Menethil goes via Ironforge; Vesprystus → Astranaar via Auberdine).
5. Dragonslayer's Shield/Lance item spots (SoD-era sources).
6. The Duskwood Missions dailies (Nightmare Incursion) — only a note in chapter 14.

## Tooling added today (all under `tooling\`)
`qinfo.py` (quest fact sheets), `pool30.py` / `compare\pool_20-30.txt`, `tarcheck.py` (TAR vs DB spawn), `tip.py` + `item_tips.json` (Forever tooltips cache, ~200 items), `check_guide.py` extended to 1-30, `tugs_diff.py` glob widened; `compare\route_digest_20-30.md` (the 88 KB data digest the plan was built from), `compare\forever_20-30_candidates.tsv`. Working files in `$HOME/work` of the device VM are throwaway.
