Phase 2 prep tables for the Skyborne warrior chapters (built 1 Nov 2026 from tooling/qdb 1.0.9 and data/zone_16593.json pulled 1 Nov 2026).
zephras_quests.tsv  126 rows: every Wowhead quest in category 16593 (Zephras Isle) or -666 (Camping 101) with level, XP,
                    race/class masks, starter and finisher NPC with their island spawn, prerequisites, and skyborne_warrior_ok
                    (corrected 1 Nov evening: the flag now also requires side != 2 - Horde - and treats only 2^32 as the Alliance Skyborne bit, 2^33 being the Horde Skyborne bit; 92466 Call of Earth and 92598 The Gift of Skysight were wrongly flagged before). Excluded for a Skyborne: 92466/92467/92468 Call of Earth, 92598, 92595, 94411, 92579, 92700.
zephras_npcs.tsv    305 NPCs spawning on the island with subname (trainer / vendor) and faction.
guard_plans.json    the Guard's mail recipes (spell ids, reagents, skill ranges) from nether - informational only, professions are Skinning + Mining.
Key island NPCs: Blademaster Ren 251964 (Warrior Trainer, Thendal Grove 43.6,24.1); Seena Skybreaker 252377 (Warrior Trainer, Valanaar 59.9,72.9);
Corsan Earthrazer 254088 (Warrior Trainer); Halavuul Cragwind 252388 Mining Trainer 65.4,80.5; Skinners Ishlee Breezewhisper 257003 59.6,76.1 and
Mendalass Tattermend 257024 43.3,43.4; Cooks Zerril Softbreeze 251905 43.9,43.8 and Nyalah Brightfire 257006 60.6,72.7; Fishers Fenn Fairweather
251992 45.0,48.4 and Baelann Swiftcurrent 257008 63.3,75.7; Zaal Stormshield 257196 DB spawn 56.6,50.4; Genn Fairweather 265756 53.8,81.3;
Denaaris Stargale 259084 zone 36 @12.3,56.3; Randal Emerson 275491 Stormwind 79.0,45.0. Whether the Skinner/Miner/Cook/Fisher NPCs teach is unverified.
