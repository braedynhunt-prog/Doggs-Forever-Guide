# Lessons (WoW Forever Atlas)

Format: one or two lines per entry - what went wrong, why, the rule going forward. Merge duplicates.

- 29 Oct 2026: a plan predicted the Wowhead XP data would check as fresh without comparing its pull dates (17-18 Oct) to the latest client build (28 Oct). Rule: check the actual dates before stating an expected result in a plan.
- 29 Oct 2026: Wowhead XP was called "browser-only" after testing only Wowhead's own endpoints; third-party mirrors (PandaQuest's Wowhead overrides and MCP server) were never searched. Rule: before declaring a source unreachable or manual, search GitHub and Reddit for mirrors and APIs.
- 29 Oct 2026: a subagent brief said to reuse score_items.py's weights without checking docs/forever-enh-stat-weights.md, which marks the mace term obsolete since 17 Oct. Rule: check the current doc before telling an agent to reuse constants from code.
- 1 Nov 2026: the 29 Oct loot report said two dungeons had "no creatures" and bosses' drops were "invisible" when only the zone-spawn field was empty; the NPC rows and drops were in the DB. Rule: when one DB field is empty, check the other tables keyed on the same id before declaring data absent.
- 1 Nov 2026: the 29 Oct plan said the guide "names no head item", taken from a report column produced by a text matcher (Gear:/Loot: lines only). Rule: grep the chapter before stating a gap derived from a matcher.
