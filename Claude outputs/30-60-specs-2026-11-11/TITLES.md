# Round 1 chapter table - authoritative (main session, 11 Nov 2026, after the reconciliation)

This table overrides the header of every spec. A writer copies the `[N]`, `[NX]`, file name and start / end state from here, and the route from the spec. `[NX]` must equal the next chapter's `[N]` text exactly (check_guide.py matches "min-max title"). The top level of each band covers the highest required level among the chapter's pickups.

| file | `[N]` | `[NX]` | starts at | hearth on entry -> on exit | ends at |
|---|---|---|---|---|---|
| `27_HillsbradAlterac.lua` | `[N 31-32 Hillsbrad Foothills]` | `[NX 31-33 City of Dalaran]` | Refuge Pointe (end of 26) | Sentinel Hill -> **Southshore** | Southshore |
| `28_CityOfDalaran.lua` | `[N 31-33 City of Dalaran]` | `[NX 32-33 Arathi Highlands]` | Southshore | Southshore | Southshore (hearth after the run) |
| `29_Arathi.lua` | `[N 32-33 Arathi Highlands]` | `[NX 32-34 Stranglethorn Vale]` | Southshore | Southshore | Aerie Peak (flight point taken) or Southshore |
| `30_StranglethornNorth.lua` | `[N 32-34 Stranglethorn Vale]` | `[NX 33-35 Booty Bay and the Drowned City]` | Southshore or Aerie Peak: fly to Stormwind | Southshore | Booty Bay (flight point taken) |
| `31_BootyBayDrownedCity.lua` | `[N 33-35 Booty Bay and the Drowned City]` | `[NX 34-36 Dustwallow Marsh]` | Booty Bay | Southshore -> **Booty Bay** | Ironforge (Historian Karnik) |
| `32_Dustwallow.lua` | `[N 34-36 Dustwallow Marsh]` | `[NX 35-36 Desolace]` | Ironforge (Gryth Thurden) | Booty Bay -> **Theramore** | Theramore |
| `33_Desolace.lua` | `[N 35-36 Desolace]` | `[NX 36-37 Scarlet Monastery]` | Theramore | Theramore -> **Nijel's Point** | Nijel's Point |
| `34_ScarletMonastery.lua` | `[N 36-37 Scarlet Monastery]` | `[NX 36-38 Badlands]` | Nijel's Point | Nijel's Point | Ironforge |
| `35_Badlands.lua` | `[N 36-38 Badlands]` | `[NX 37-38 Swamp of Sorrows]` | Ironforge (Gryth Thurden) | Nijel's Point -> **Thelsamar** | Ironforge (flown from Thelsamar) |
| `37_SwampOfSorrows.lua` | `[N 37-38 Swamp of Sorrows]` | `[NX 37-39 Riverglades]` | Ironforge (Gryth Thurden) | Thelsamar | Booty Bay (the hop is last; Nethergarde flight point taken) |
| `38_RivergladesI.lua` | `[N 37-39 Riverglades]` | `[NX 38-40 Storm, Heed, Tempest]` | Booty Bay: fly Darkshire - Lakeshire | Thelsamar -> **Farholde Keep** | Farholde Keep |
| `39_StormHeedTempest.lua` | `[N 38-40 Storm, Heed, Tempest]` | `[NX 39-40 Razorfen Downs]` | Farholde Keep: fly Lakeshire - Stormwind - Refuge Pointe | Farholde Keep | Myriam Moonsinger, The Barrens 49.0,94.9 |
| `39b_RazorfenDowns.lua` | `[N 39-40 Razorfen Downs]` | `[NX 39-40 The Tempest's Weapons]` | Myriam Moonsinger | Farholde Keep | Myriam / the Downs' door |
| `39c_Alterac.lua` | `[N 39-40 The Tempest's Weapons]` | `[NX 40-40 Level 40: Ironforge]` | the Downs' door: Ratchet, boat to Booty Bay | Farholde Keep | Ironforge |
| `39d_Level40.lua` | `[N 40-40 Level 40: Ironforge]` | `[NX 40-40 Uldaman]` | Ironforge | Farholde Keep | Thelsamar |
| `39e_Uldaman.lua` | `[N 40-40 Uldaman]` | `[NX 40-41 Riverglades]` | Thelsamar | Farholde Keep | Farholde Keep (hearth, after the Ironforge hand-ins) |
| `40_RivergladesII.lua` | `[N 40-41 Riverglades]` | `[NX 41-42 Powderfuse Port]` | Farholde Keep | Farholde Keep | Farholde Keep (then the ride west and the port: chapter 41) |
| `41_PowderfusePort.lua` | `[N 41-42 Powderfuse Port]` | none: last chapter of round 1 (closing `[OC]` note) | Farholde Keep | Farholde Keep | Farholde Keep (hearth) |

There is no chapter 31b, 34b or 36 (their specs are one-line stubs).

## Lines every chapter carries
- Line 2: `[D Forever Shaman 30-60 (Braedyn)\\<one-sentence description>]` (as 23_Hillsbrad.lua does for 1-30), then `[GA Alliance]` (the 1-30 shaman chapters from 23 on use `[GA Alliance]` with `[A Shaman]` on class steps: copy 23's header).
- The first step is the **level-check** `[OC]`: "this chapter wants level N" and what to do if under it (text in the spec).
- Footer: `]], "Forever Shaman 30-60")`.
- The last step is the `[OC]` **Check** note (log contents), as in 1-30.

## Carried quests between chapters (id: picked up -> handed in)
- 92456, 92489: carried from 1-30 -> done in 28 -> handed in at Stormwind in 30's opening.
- 92432: carried from 1-30 -> handed in in 27 (Modera); 92457, 92458: 27 -> 28.
- 96800 Past Due: 27 (Magus Olvek) -> 34 (Library; hand-in at Olvek on 34's Dalaran crater stop).
- 98463 Talk of the Town: 27 (Barkeep Kelly) -> 31.
- 95787, 95788, 95798 (Loremaster Dibbs): 27 -> 31 (the Drowned City; hand-ins at Dibbs and Abra Cadabra).
- 707: 27 (Ironforge) -> 35. 1453: 27 (Ironforge) -> 33. 1050: 27 (Ironforge) -> 34.
- 79358 Storm, Earth, and Fire: 29 (Veyric) -> totems in 32 (Water), 33 (Air), 35 (Fire), 37 (Earth) -> handed in in 39.
- 79192 Stepping Stones: carried through; its next step is not on the round-1 route (note in 29's Check).
- 97328: 30 (object, north Stranglethorn) -> 30's end (Lozgil, Booty Bay). 95786: 30 (Brother Nimetz) -> 31 (Dibbs).
- 1248 The Missing Diplomat: carried from 1-30 -> 32.
- 1052: 33 (after 261) -> 34. 79235 On the Lam: 33 -> 37 (Tokal, Booty Bay); 79236 in 37; 79242: 37 -> 39 (Illari's cache, Arathi).
- 96773 The Coldbringer's Eye: 34 (Lan'dalock, on the crater stop) -> 39b (the Eye) -> 39c (Lan'dalock).
- 721, 709: 35 (pickups) -> 39e. 739, 704: 35 if he is 38, else carried to 39e.
- 94929 Deliver the Second Shipment: 37 (Watcher Biggs) -> 38 (Demar Brant).
- 94928 A Few Furs for Friz: 38 (`[O]`, after A Fur Trade) -> 41. 94887: 40 only if the Field Marshal's Log dropped in 38.
- 3636 Bring the Light: 39 (Stormwind, only at level 39) -> 39b -> 39d (Benedictus). 96135: 39 -> ritual in 39 -> 39c (Veyric). 669: 39 (cove) -> 39c (Seahorn); 670, 667 in 39c. 95315: 39 (Captain Nials) -> 40 (Demar Brant).
- 2398, 1360: 39d (Ironforge) -> 39e.

## Training stops (prices per rank from tooling/trainer_costs.json: level 32 ranks 80s, 34 ranks 90s, 36 ranks 1g, 38 ranks 1g 10s, 40 ranks 1g 20s; the musts are the leveling sheet's)
27 Ironforge (Eldrun: what level 31-32 allows) | 29 Aerie Peak (Farseer Maret Firetend 270263: the 32 and 34 rows not yet bought; no Ghost Wolf) | 31 ends in Ironforge (Eldrun: the 34 row) | 34 ends and 35 starts in Ironforge (Eldrun: the 34 and 36 rows) | 37 starts in Ironforge (Eldrun: the 36 row if not bought) | 39d Ironforge (the 38 and 40 rows, Windfury Weapon rank 2 a must, Mail, riding). Each stop's line says "train every rank your level allows that the sheet marks must or buy" and lists the rows with prices; it must not assume an earlier stop was skipped or taken.

## Gold lines
Gold check lines at the end of 31 (about level 35) and 37 (the "Gold break" note: riding 100g at Friendly / 94g 74s at Honored, plus a ram listed at 20g and at 40g; the route works on foot) and in 39d (the purchase). `python tooling/gold.py` computes the running quest money once the chapters exist; the writer leaves the number as the spec gives it and the main session reconciles it.
