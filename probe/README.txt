DoggsProbe - data-logging addon for the Forever Dwarf Shaman (built 24 Sep 2026)

WHAT IT DOES
  Records, into SavedVariables (DoggsProbeDB), everything the stat-weight model guesses at:
  1. Character-sheet snapshots on login, level-up, gear change, talent change, imbue change and /probe:
     level, Str/Agi/Sta/Int/Spi (effective, base, +buff, -buff), attack power (total, base, +, -),
     melee crit, spell crit per school, dodge/parry/block, expertise + the expertise/hit/crit combat
     ratings and their bonuses, GetManaRegen (not casting / casting), max HP/mana, armour, weapon
     damage range + speed, spell damage per school + healing, imbue state (GetWeaponEnchantInfo),
     the main-hand tooltip lines (shows the imbue line), all 19 equipped item links, talents (if the
     classic talent API answers), current buffs, XP, zone.
  2. Rockbiter watcher: every second it samples AP + imbue state; the tick where the imbue appears,
     changes or drops is stored as before/after {AP, Str, Int, level, weapon damage} plus the
     Rockbiter spell text at that moment -> "Rockbiter's AP" = delta.
  3. Regen probe: 1 s sampler out of combat. Buckets keyed level|spirit|int|state, state = idle /
     drink / food (+fsr when within 5 s of a mana-costing cast). Seconds at full mana, seconds where
     mana dropped, combat and the second after combat are excluded. mana/s per bucket + a capped raw
     sample list (2,500). Swap a Spirit item on/off and compare buckets = mana/s per Spirit point.
  4. Spell probe: on login / level-up / gear change (and /probe scan) it walks the spellbook, finds
     the highest rank of Earth/Flame/Frost Shock, Lightning Shield, Lightning Bolt, Chain Lightning,
     Healing Wave, Lesser Healing Wave, the four weapon imbues, Stormstrike and a few totems, and
     stores id, rank, the description text (the tooltip numbers), mana cost and the spell damage /
     healing / crit the character had at that moment. Readings are deduped, so two gear states =
     two readings = the coefficient. The whole spellbook (id -> name/rank) is stored too.
  5. Item logger: every item tooltip shown (bags, loot, vendor, AH, chat links, quest rewards) plus
     scans of equipped items and bags on login and whenever bags change, every quest reward CHOICE
     (QUEST_DETAIL and QUEST_COMPLETE, so rewards you don't take are captured), every vendor's stock
     with prices, every loot window with its source. Per item: name, link, ilvl, required level,
     type/subtype/slot, GetItemStats table, the raw tooltip lines ("Equip: Increases your expertise
     by 6" survives even if GetItemStats misses it), where it was seen, first/last seen. Also quests
     (id, title, giver, objective text, XP, money, objectives list after accept, turn-in XP).
  6. Combat sampling (best effort): your own SWING_DAMAGE / SWING_MISSED bucketed by target level
     minus your level (hits, crits, glancing, miss types, damage sums/min/max), and SPELL_DAMAGE /
     SPELL_MISSED / SPELL_CAST_SUCCESS per spell. If Forever hides damage amounts (secret values) it
     drops to hit/miss counts; if even the event fields are unreadable it switches itself off and
     records why (/probe combat shows the mode).

INSTALL
  Copy the DoggsProbe folder (or unzip DoggsProbe.zip) into the client's Interface\AddOns\ so you get
  Interface\AddOns\DoggsProbe\DoggsProbe.toc. New addon folders need a FULL client restart, not
  /reload. Two TOCs: DoggsProbe.toc (Interface 16001, 11509) and DoggsProbe_Vanilla.toc (11509),
  so the same folder works on Classic Era and Forever. Test on Era (Dogg) first.

CHECK IT IS WORKING (type in chat)
  /probe status    -> shows the client build/toc, which API paths it took (spellInfo=..., tooltipHook=...),
                      "ticker running", counts, and the combat mode. If the addon is not loaded you get
                      "Type /help for a list of commands" instead.
  /probe           -> takes and prints a snapshot: "snapshot #N: L20 manual | Str .. | AP .. | crit .. | regen .. | imbue .."
  /probe spells    -> one line per watched spell with rank, mana cost, SP and the description text
  /probe items     -> item count + the last 5 items seen; hover a few bag items first and the count grows
  /probe regen     -> the regen buckets (needs a minute or two below full mana, out of combat, to fill)
  /probe rockbiter -> after casting Rockbiter Weapon: one line with AP before -> after (delta)
  /probe combat    -> after a few fights: swings by target level, miss types, spells
  /probe errors    -> anything the addon caught (should be empty)
  /probe help      -> the full list (quests, bags, scan, debug, export, reset)
  Everything also prints to chat as it happens (login snapshot ~3 s after entering the world, spell
  scan at ~5 s, item scan at ~7 s), because Forever's week-1 bug can reset saved settings on launch.

  IMPORTANT: SavedVariables are only written on /reload or logout. Do a /reload before you quit.

READING THE DATA
  The file is WTF\Account\<account>\SavedVariables\DoggsProbe.lua
    Era:     C:\Program Files (x86)\World of Warcraft\_classic_era_\WTF\Account\91845139#1\SavedVariables\DoggsProbe.lua
    Forever: the Forever client's WTF\Account\<account>\SavedVariables\DoggsProbe.lua
  python3 probe2json.py "<that file>" out.json   -> writes JSON and prints a summary (snapshots, regen
  buckets with mana/s, imbue deltas, spell readings, item/quest/vendor counts, combat mode).
  It uses ..\tooling\luatab.py if it is there and has its own copy of the parser otherwise.

  DB layout: DoggsProbeDB.items[<toc>][itemID] (account-wide per client), DoggsProbeDB.chars["Name-Realm"]
  = { meta, snapshots[], rockbiter[], regen{buckets{}, raw[] (rawFields lists the column order)},
      spells{name -> {id, rank, latest, readings[]}}, spellbook{id -> name}, combat{mode, swing{}, spell{}},
      quests{id -> ...}, vendors{name -> ...}, loot{source -> {itemID -> count}} }, DoggsProbeDB.errors[].

WHAT FEEDS WHAT (weights\enh_weights.py)
  regen buckets (idle, two Spirit values)        -> spirit_regen_scale + base regen
  snapshots: expertise % vs expertise rating     -> expertise_model
  rockbiter[].delta at 10 / 16 / 20              -> rockbiter_frac
  Earth Shock readings at two spell damages      -> shock_coef_scale
  items[] (lines + stats)                        -> score_items.py input, later the upgrade addon's DB

FILES
  DoggsProbe\DoggsProbe.toc, DoggsProbe_Vanilla.toc, Core.lua (compat layer, DB, events, ticker),
  Snapshot.lua, Regen.lua, Spells.lua, Items.lua, Combat.lua, Commands.lua
  DoggsProbe.zip - the same folder zipped
  probe2json.py  - SavedVariables -> JSON + summary
  test\          - the offline harness it was checked with (lua5.1 run.lua era|forever|blocked ..\DoggsProbe out.lua):
                   a stub of the WoW API in three flavours (Era globals; Forever C_ namespaces with secret
                   combat values; Forever with a fully unreadable combat log). Not needed in game.
