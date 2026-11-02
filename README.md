# Dogg's Forever Guide

[Guidelime](https://github.com/max-ri/Guidelime) levelling guides for **WoW Forever, Alliance, levels 1-30**. Three addons, one route:

- **Forever Shaman 1-30** (`Guidelime_ForeverShaman`): the original guide, written for a Dwarf Shaman (2H Enhancement). Dwarf and Human Hunter lines are in the files but no longer maintained.
- **Forever Warrior 1-30** (`Guidelime_ForeverWarrior`): the same route rebuilt for a Skyborne Protection Warrior (1H + shield, Skinning + Mining). It starts on Zephras Isle, crosses to Stormwind and Ironforge, and joins the shaman's route at Loch Modan. Generated from the shaman chapters by `tooling/build_variant.py`; first build 1 Nov 2026, not yet played, and the lines the data could not settle say "(unverified)".
- **Forever Druid 1-30** (`Guidelime_ForeverDruid`): the same route rebuilt for a Skyborne Feral Druid (bear 10-20, cat from 20, Skinning + Mining). Zephras Isle, then the Skyborne join leg with the Cure Poison chain through Moonglade, Auberdine and Darnassus at 14, the shaman's route from Loch Modan with the Aquatic Form and Windborne Cat Spirit quests threaded in at 17-18 and 20. Generated from the shaman chapters by `tooling/build_variant.py`; first build 2 Nov 2026, not yet played; the test list is in `docs/druid-build-2026-11-02.md`.

## Install (players)

1. Install the **Guidelime** addon, the Forever build (6.014 or later) - older Classic Era copies do not know Zephras Isle or the Skyborne.
2. Download the zip for your character from the [latest release](https://github.com/braedynhunt-prog/Doggs-Forever-Guide/releases/latest): `Guidelime_ForeverShaman.zip`, `Guidelime_ForeverWarrior.zip` or `Guidelime_ForeverDruid.zip`.
3. Unzip it into `World of Warcraft\_forever_\Interface\AddOns\` (the Forever client's own folder, not `_classic_era_`) so you end up with `Interface\AddOns\Guidelime_ForeverShaman\` (or `...\Guidelime_ForeverWarrior\`, `...\Guidelime_ForeverDruid\`).
4. Restart the game, open Guidelime and pick **Forever Shaman 1-30**, **Forever Warrior 1-30** or **Forever Druid 1-30**.

The shaman addon was called `Guidelime_ForeverAlliance` until 1 Nov 2026; if you installed that, delete the old folder.

## What the guides cover

Both:
- Every new-to-Forever Alliance zone, dungeon and hub reachable in the bracket: Loch Modan, Hall of Thanes, Westfall, Redridge, Deadmines, Ruins of Lordaeron, Darkshore, Ashenvale + Blackfathom Deeps, Duskwood, the Stockade, Wetlands, Darnassus, Excavation Site, Hillsbrad, Gnomeregan, Razorfen Kraul.
- Cooking, Fishing and First Aid stops so the food buffs are ready when you need them.
- Dungeon quests labelled normal / grind up front; no rare-drop farms.

Shaman: Northshire or Coldridge Valley start, the shaman class quests (Call of Earth / Fire / Water / Air) threaded in at level, gear calls at every reward choice for a 2H Enhancement shaman.

Warrior: Zephras Isle 1-14 in full, the Skyborne join leg, the warrior class thread (trainer stops in Stormwind, Ironforge and Darnassus, The Skybreaker Bulwark, Exploring the Alliance, the Fire Hardened chain to The Shieldsmith), gear calls for a 1H + shield tank, tank notes and per-boss loot calls in every dungeon.

Druid: Zephras Isle 1-14 in full with the Bear Form quests at 10, the Skyborne join leg with the Cure Poison chain (Moonglade, Auberdine, Darnassus) at 14, Aquatic Form at 17-18, the Windborne Cat Spirit quests and Cat Form at 20, trainer stops in the Stormwind Park, Darnassus and Moonglade, feral gear calls at every reward choice, bear/cat notes and per-boss loot calls in every dungeon.

Found something wrong in game (missing NPC, bad coordinates, quest that won't take)? Open an issue with the chapter and step text.

Everything below this line is the data and tooling the guide is built from. Players can ignore it.

---

# WoW Forever Alliance Quest Atlas — scraper

Pulls every quest that Wowhead's Forever database flags as **new** or **updated** in the Alliance 1-30 zones and dungeons, then builds the atlas page from it. Built 23 Sep 2026 during the Forever beta (cap 20).

## Run it

1. Python 3 (any 3.9+; nothing to pip install, it only uses the standard library).
2. Double-click `run.bat`. It deletes the `raw\` page cache, refetches everything at about one page per second (30-45 minutes), rebuilds `data\*.json`, and writes the page.
3. Open `forever-alliance-quest-atlas.local.html` in a browser.
4. To update the published artifact (Forever Alliance Quest Atlas), attach `forever-alliance-quest-atlas.html` in the Wow Classic Vanilla project and ask Claude to republish it to the same URL.

You can also run the steps by hand from a terminal in this folder:

    python scrape.py            # zones -> quest pages -> NPC/object pages (cached in raw\)
    python scrape.py reparse    # re-parse cached pages without refetching (after a parser change)
    python build_report.py      # writes forever-alliance-quest-atlas.html and .local.html

`scrape.py` skips any page already in `raw\`, so if a run is interrupted, just run it again. Delete `raw\zone_*.html` (or the whole `raw\` folder, which `run.bat` does) to refetch the zone lists after the level cap rises, otherwise new quests won't be picked up.

## Files

- `scrape.py` — fetcher/parser. The `ZONES` dict near the bottom is the zone list (Wowhead zone ids). Add 30-60 zones there once the beta cap or launch makes them worth scraping (ids are in `zones.json`, e.g. Arathi 45, Alterac 36, STV 33, Desolace 405, Badlands 3, Swamp of Sorrows 8, Hinterlands 47, Feralas 357, Tanaris 440, Riverglades 16591).
- `build_report.py` — turns `data\` into the page. `ORDER` sets the section order; `ZONE_NOTE` holds the one-line zone notes.
- `report.css`, `report.js` — page styling and the filter controls.
- `zones.json` — Wowhead's Forever zone list (id, name, level range, new/updated flag).
- `data\` — parsed output from the last run (`quests.json`, `entities.json`, one `zone_<id>.json` per zone).
- `forever-alliance-quests-2026-09-23.tsv` — flat snapshot of the 23 Sep run, opens in Excel.
- `scrape.log` — progress and any HTTP errors.

## Notes

- Wowhead has no API; this reads the JSON that its zone, quest and NPC pages embed. Keep the one-request-per-second pacing (`min_gap` in `fetch`) so it doesn't get the IP blocked.
- "New"/"updated" are Wowhead's own change flags against Classic Era. Updated quests carry Wowhead's diff lines (e.g. "Rewards: adds X").
- Coordinates come from Wowhead client sightings, so a quest that nobody has picked up yet shows "no coords yet" or an empty giver. That is why the 20-30 zones are thin while the cap is 20.
- Alliance-usable means side Alliance, both, or unspecified; Horde-only rows are hidden by default and can be shown with the checkbox.
