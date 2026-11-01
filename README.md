# Dogg's Forever Guide

A [Guidelime](https://github.com/max-ri/Guidelime) levelling guide for **WoW Forever, Alliance, levels 1-30**. Written for a Dwarf Shaman (2H Enhancement); Dwarf and Human Hunter lines are in the files but no longer maintained.

## Install (players)

1. Install the **Guidelime** addon if you don't have it.
2. Download `Guidelime_ForeverAlliance.zip` from the [latest release](https://github.com/braedynhunt-prog/Doggs-Forever-Guide/releases/latest).
3. Unzip it into `World of Warcraft\_classic_era_\Interface\AddOns\` so you end up with `Interface\AddOns\Guidelime_ForeverAlliance\`.
4. Restart the game, open Guidelime and pick **Forever Alliance 1-30**.

**Skyborne Protection Warrior?** The same route rebuilt for a Skyborne warrior (1H + shield, Skinning + Mining) is `Guidelime_ForeverWarrior.zip` in the same release: it starts on Zephras Isle, joins the Alliance route at Loch Modan, and picks **Forever Warrior 1-30** in Guidelime. It is generated from the Alliance chapters by `tooling/build_variant.py` (see `docs/warrior-build-2026-11-01.md`); it has not been played yet, and its unverified lines say so.

## What it covers

- Every new-to-Forever Alliance zone, dungeon and hub reachable in the bracket: Northshire to Westfall, Hall of Thanes, Deadmines, Ruins of Lordaeron, Loch Modan, Redridge, Darkshore, Ashenvale + Blackfathom Deeps, Duskwood, the Stockade, Wetlands, Darnassus, Excavation Site, Hillsbrad, Gnomeregan, Razorfen Kraul.
- Shaman class quests (Call of Earth / Fire / Water / Air) threaded in at level.
- Cooking, Fishing and First Aid stops so the food buffs are ready when you need them.
- Gear calls at every reward choice for a 2H Enhancement shaman.
- Dungeon quests labelled normal / grind up front; no rare-drop farms.

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
