> **ARCHIVED (3 Sep 2026):** Braedyn left OctoWoW (server DDoS) and now plays Classic Era as a Troll Rogue. See `claude/STATUS.md` and `claude/classic-era-rogue.md`. Kept for reference only. (Moved out of the Claude project to this folder on 24 Sep 2026.)

# OctoWoW client setup (Braedyn)

- Client folder: `C:\OctoWoW` (1.12 client with VanillaFixes, dxvk). Connected to Cowork sessions as a folder.
- Addons live in `C:\OctoWoW\Interface\AddOns`. Launcher-installed addons are git clones (each has a `.git` folder). The local VM shell can reach GitHub (git clone, curl to release assets) and has python3, so installs and patches can be done straight into the folder. The VM shell cannot delete inside the mount; disabled addons go to `Interface\AddOns_disabled\` instead.
- Account: DOGGFOUR (WTF\Account). Character: Troll Warlock (Horde). Forum handle: Dogg.

## Client mods (dlls) — state as of 2 Sep 2026
- `dlls.txt` (read by VanillaFixes at launch; LF line endings, blank line between entries) lists: VanillaMultiMonitorFix, transmogfix, VanillaHelpers, nampower, SuperWoWhook. The launcher did NOT strip the hand-added SuperWoWhook line on relaunch.
- nampower v4.6.2 confirmed loading (Logs\nampower_debug.log). Well above SuperCleveRoids' 3.0 minimum.
- SuperWoW 2.2: `SuperWoWhook.dll` (1,000,448 bytes, sha256 bd214b32…351d) from github.com/balakethelock/SuperWoW release "Release", placed in C:\OctoWoW, listed after nampower. CONFIRMED loading (game launched clean, SuperAPI popup gone). `SuperWoWlauncher.exe` from the zip not copied (VanillaFixes injects). Closed-source; README says it doesn't hide from Warden — Octo's official stance not confirmed (community octo-updater ships it).
- UnitXP_SP3: was briefly enabled, then VanillaFixes threw "DLL entry point returned an error (0)" — that message means LoadLibrary returned null for a listed dll (VanillaFixes src/loader.c), not a client-version issue. The dll is absent from the folder and out of dlls.txt (launcher toggle removed it, or AV quarantined it — UnitXP_SP3 commonly gets flagged). Only cost: SuperCleveRoids range/[multiscan] conditionals and the UnitXP settings addon.
- VC++ x86 runtime is present (VanillaMultiMonitorFix imports MSVCP140/VCRUNTIME140 and loads).
- Companion settings addons installed: NampowerSettings, UnitXP_SP3_Addon, SuperAPI.

## VoiceOver (Sep 2026)
- `AI_VoiceOver` = Alukarho fork ("VoiceOver Turtle – Darkneo", Turtle WoW Sudamérica, Spanish UI). Detects sound packs generically via `X-VoiceOver-DataModule-Version` in TOCs; expects module version 1.
- English sound pack `AI_VoiceOverData_Vanilla` (v0.1 data, from mrthinger/wow-voiceover release v1.3.1) installed as a sibling folder — ~1.2 GB, ~9,555 sound files. Structure verified correct.
- Addon self-handles the "Load out of date AddOns" flag for the pack. New addon folders need a full client restart (not /reload) in 1.12.
- If wanting a stock English addon instead: swap `AI_VoiceOver` for the 1.12 build from github.com/mrthinger/wow-voiceover; same pack works.

## Addon audit (2 Sep 2026)
- All addons are `## Interface: 11200`; all hard deps satisfied.
- Deleted: Guda (duplicate bag addon vs Bagshui — DFUI-Reforged integrates with Bagshui), pfQuest-turtle (Turtle DB, wrong for Octo), GetHead (archived world-buff auto-logout), Decursive (little use on a warlock).
- Installed: `pfQuest-octo` (github.com/paokkerkir/pfQuest-octo; Octo DB extension; requires pfQuest). pfQuest itself is launcher-installed v7.0.1 (shagu, commit 2025-08-25).
- Known harmless missing-file nits (FrameXML.log): BigWigs `Raids\Other\Nerubian.lua`; ConsumesManager `LibCompress.xml`; Bagshui `Components\Ui.Skin.lua`; SuperMacro `SM_Extend.lua`.
- Bagshui installed by launcher is the absir/Bagshui fork (last commit Dec 2024), not the official veechs/Bagshui — swap if it misbehaves.
- ShaguTweaks nameplate mods (castbar/classcolor/scale) should be toggled off since GudaPlates handles nameplates.
- Turtle-server-hook addons (TWThreat, TurtleCalendar, AutoLFM, TurtleMail) untested on Octo's backend.
- ShaguTweaks modules worth knowing: "Equip Compare" (hold Shift on an item tooltip to see the equipped item), "Sell Junk" (adds a sell-greys BUTTON to merchants, not automatic), "Vendor Values". DFUI-Reforged's settings panel exposes the same modules under `/dfrl` → tooltip / vendor.
- pfQuest 7.0.1 gotcha: `pfQuest.route.SetTarget(node)` sets `pfMap.queue_update = true`, and map.lua:1094 then does `queue_update + .25` → "attempt to perform arithmetic on field queue_update (a boolean)" spam that also stops the map/arrow updating. Any addon calling SetTarget must set `pfMap.queue_update = GetTime()` right after (pfQuest's own pin click does).

## UI tweaks (in-game commands worked out 2 Sep 2026)
- pfQuest arrow: `/db arrow` TOGGLES (default on — running it once turns it off); or `/db config` → "Show quest arrow" / Routes → "Show Arrow Along Routes". The arrow only appears when a quest in the log has a known objective location. pfQuest tracker: `/db config` → "Enable Quest Tracker"; `/db lock` to unlock/drag. The pfQuest arrow must be ON for VanillaGuide's Shift+click targeting to show anything.
- DFUI-Reforged: `/dfrl` → Bars → "mainbar deco" → "Show gryphon/wyvern decorations" (the lions); "mainbar" → bar background; "multibar 1" → bottom-left bar. DFRL also owns the red Lua-error display ("DFRL: Error [Source: addon]").
- Cursive: settings via its minimap icon (not `/cursive`). Position frame with "Show Frame Background", then "Allow clickthrough". Placed on left side.
- ExtraResourceBars: `/erb` (duplicates DFUI unit-frame HP/mana above action bar).
- Pet: Imp starts on Defensive and only engages after you're hit; Ctrl+1 = pet attack. Pull macro that fixed the "pet won't attack" feel: `/script PetAttack()` + `/cast Corruption` (Shadow Bolt before level 4).

## Leveling guide (replaced 2 Sep 2026)
- Zygor does NOT work on 1.12 — no version ever targeted 1.12.
- TourGuide-Turtle + TomTom-TWOW were tried first and rejected (steps are bare "Accept/Complete X" with no instructions; TomTom arrow only exists for steps with coords, so it kept vanishing). Both moved to `Interface\AddOns_disabled\` (not deleted).
- Now installed: `VanillaGuide` = VanillaGuide-Enhanced v2.0.0 (github.com/GabHST/VanillaGuide-Enhanced, commit ec355bf, 2026-04-08), assembled by hand: repo root code (the newer 1/2-step UI) + the `en/` GuideTables (English Joana Horde 1-60; the repo root and pt-br folders carry Portuguese guides), Portuguese chat/tooltip strings in `VG_Enhancements.lua` and `Frame_MainFrame.lua` translated to English via sed. Commands: `/vge` (help), `/vge autoquest`, `/vge skip`, `/vge combat`; Shift+click a step = point the pfQuest arrow; right-click step = skip; right-click minimap button = 1-step / 2-step mode.
- Its Shift+click / auto arrow expects a `pfQuest_PointTo(x, y, zoneid, title, kind)` global that only exists in a SoloCraft pfQuest fork. Added `VG_pfQuestShim.lua` (loaded before VG_Enhancements.lua, `pfQuest` added to OptionalDeps) which implements it with stock pfQuest: `pfMap:DeleteNode("VGuide")` → `pfMap:AddNode{ addon="VGuide", arrow=true, ... }` → `pfQuest.route.SetTarget{ title=label, layer=1 }` → `pfMap.queue_update = GetTime()`. First version set queue_update before SetTarget and caused the boolean-arithmetic error spam above; fixed 2 Sep. VG's own two `SetTarget(data[3])` calls (VG_Enhancements.lua, Frame_MainFrame.lua) got the same one-line fix.
- Upstream bug fixed locally in `GuideTable.lua`: `PrepareGuidesTableHorde/Alliance` merged all three starting-zone tables, which share guide IDs (0106, 0610, 1012), so "1-6 Durotar" was overwritten by Mulgore/Tirisfal and unselectable. Now only the player's race zone goes into the main list (Troll/Orc → Durotar); the other two come through the NoGuide path as intended. Verified with a Lua harness against the real guide tables.
- Auto-advance rewritten (2 Sep, evening): the Enhanced code only auto-accepted/advanced on Portuguese keywords ("aceite", "entregue", "compre", "aprenda"), and after any quest interaction it blindly advanced ONE step, so with English guides the pointer drifted. Now `VG_Enhance:SyncStepWithQuestLog()` (in VG_Enhancements.lua) runs 0.4 s after every QUEST_LOG_UPDATE and moves to the step after the furthest satisfied step: #GET = quest in log (or seen+gone), #DO = in log and complete (or seen+gone), #IN = seen and gone; untagged steps in between (travel, trainer) are treated as done; an unsatisfied quest step blocks. "Seen" quests are tracked in `VG_EnhanceDB.seenQuests`, so quests turned in before this existed won't auto-satisfy their step (right-click once). English keywords added for auto accept / turn-in / trainer / vendor. Toggle: `/vge autoskip`. Simulated against the real 1-6 Durotar guide before deploy. Known quirk: two quests both titled "Sarkoth" make the guide sit on the "turn in Sarkoth" step until pt.2 is handed in.
- Guide steps are generic vanilla routing; they know nothing about Octo custom quests. pfQuest-octo covers those.

## Custom addons written for Braedyn (2 Sep 2026)
- `AutoSellJunk` — sells every grey item automatically on MERCHANT_SHOW (0.15 s between sales), prints total earned using SellValue / ShaguTweaks price DB. `/asj` toggle, `/asj on|off|status`. SavedVariables `AutoSellJunkDB`.
- `UpgradeCheck` — adds an "Upgrade +X% / Downgrade / Sidegrade / Can't use" line to item tooltips (bags, loot, vendors, quest rewards, chat links) by parsing tooltip text with Affliction-warlock weights (shadow dmg 1, spell dmg 1, int 0.55, stam 0.6, spirit 0.15, mp5 1.2, spell crit 6/%, spell hit 8/%, armor 0.015, wand DPS 3.5) and comparing against the weakest equipped item in that slot. Red tooltip lines = can't use; "Requires Level" is shown as "(level N)". Trinkets/shirts/tabards skipped. `/uc` toggle, `/uc weights`, `/uc wand <n>`. SavedVariables `UpgradeCheckDB`. Weights table is at the top of `UpgradeCheck.lua`.
- Both are Lua 5.0-style (no `#`, `%`, `string.match`), logic unit-tested against a mock of the 1.12 tooltip/bag API before install; both loaded without FrameXML.log complaints on first launch. Pawn for 1.12 (github.com/finidigeorge/Pawn, Pawn 1.1.2 port) was the off-the-shelf alternative but only shows scale numbers, no upgrade verdict.

## Warlock / QoL additions (installed 2 Sep 2026)
- `Cursive` 3.1.1 (github.com/pepopo978/Cursive) — multi-target DoT/curse timers + auto-curse. Needs nampower loaded (confirmed working).
- `SuperCleveRoidMacros` (github.com/jrc13245/SuperCleveRoidMacros) — macro conditionals; meant to replace SuperMacro (coexists). Confirmed registering with nampower.
- `AtlasLoot` + `Atlas` Turtle editions (github.com/Otari98/AtlasLoot, github.com/Otari98/Atlas).

## Other addons installed
AttackBar, AutoLFM, Bagshui, BetterCharacterStats, BigWigs, ConsumesManager, DoiteAuras, DragonflightUI-Reforged, ExtraResourceBars, FishingBuddy, FlightTracker, GNS, GudaPlates, LevelRange-Turtle, MessageBox, ModernMapMarkers, NampowerSettings, Necrosis, Outfitter, SellValue, ShaguDPS, ShaguTweaks (+extras), SimpleActionSets, SuperAPI, SuperMacro, TWThreat, TurtleCalendar, TurtleMail, UnitXP_SP3_Addon, aux-addon, pfExtend, pfQuest, pfQuest-octo, VanillaGuide, AutoSellJunk, UpgradeCheck, Cursive, SuperCleveRoidMacros, AtlasLoot, Atlas. Disabled (in AddOns_disabled): TourGuide-Turtle, TomTom-TWOW.
