Skyborne Protection Warrior variant of the Forever guide (plan: docs/warrior-build-plan-2026-11-01.md; tooling added 1 Nov 2026)

Build:  python tooling\build_variant.py tooling\variants\skyborne_warrior\variant.json     -> guide\Guidelime_ForeverWarrior\ + zip
Gear:   python tooling\gear_calls.py --profile prot --variant tooling\variants\skyborne_warrior\variant.json --emit tooling\variants\skyborne_warrior\generated_gear.json
        (also writes missing_tooltips.txt here; fetch them with python tooling\fetch_tooltips.py --from-file tooling\variants\skyborne_warrior\missing_tooltips.txt)
Check:  FOREVER_GUIDE=guide\Guidelime_ForeverWarrior python tooling\check_guide.py   (verify.py / tarcheck.py the same way;
        baselines tooling\check_guide_baseline_Guidelime_ForeverWarrior.txt / verify_baseline_Guidelime_ForeverWarrior.txt)

Files
  variant.json          the variant (schema below)
  profile.json          {"profile": "prot"} - the weights/profiles.py profile for gear calls
  chapters\             hand-written chapters, copied verbatim (00s, 00t, 00u; Phase 2)
  overlay\<key>.txt     anchored edits to the Alliance source chapters (Phase 3); syntax in tooling\build_variant.py
                        anchors: QA/QT/QC/TAR<id>, G<x>,<y>, N <title>, T <literal text of an untagged line> (added 1 Nov evening), #n for the nth match
  generated_gear.json   gear_calls.py --emit output read by the builder (schema at the top of tooling\gear_calls.py)
  missing_tooltips.txt  item ids the last --emit had no tooltip for
  build_report.txt      the last build's report (drops, strips, overlay ops, gear placement, "needs overlay" lines)

variant.json schema (all keys required unless marked optional)
  name                 variant id, matches the folder name under tooling\variants\ and generated_gear.json "variant"
  folder               output addon folder name under guide\ (Guidelime_ForeverWarrior)
  group                Guidelime group string, the second argument of registerGuide ("Forever Warrior 1-30")
  d_prefix             the [D ...] header prefix written before the "\\" ("Forever Warrior 1-30 (Braedyn)")
  source_folder        the route source, relative to the atlas folder (guide/Guidelime_ForeverAlliance)
  source_group         the source's group string, replaced in every footer ("Forever Alliance 1-30")
  source_d_prefix      the source's [D ...] prefix, replaced in every header
  class, race, faction the character (Warrior, Skyborne, Alliance)
  chain                the race-chain name guidelib uses for this folder (check_guide / verify --chain): Skyborne
  profile              optional, default "profile.json"
  generated_gear       optional, default "generated_gear.json" (relative to this folder, or absolute)
  missing_tooltips     optional, default "missing_tooltips.txt"
  gear_skip_quests     optional list of quest ids whose generated gear line is not inserted (the overlay words it)
  tag_words            {"classes"|"races"|"factions": {"keep": [...], "drop": [...]}} - every word that appears in an [A ...] or
                       [GA ...] tag of the source must be listed; a line is dropped when, for a category its tag names, none
                       of the named words is a keep word (so [A Shaman] and [A Dwarf,Hunter] go, [A Warrior] stays). guidelib
                       also adds every listed word to RACE_WORDS (and the race words to RACES) for this folder.
  chapters             ordered list of {"key", "file", "source"}: key = chapter key (overlay file name, gear JSON "chapter"),
                       file = output file name, source = Alliance file name to build from, or null for a hand-written
                       chapter in chapters\<file>
  toc                  {"headers": [["Interface", "16001"], ["Title", ...], ...]} written as "## Key: value" lines, then the
                       chapter files in order
  toc_files            optional, default ["<folder>.toc", "<folder>_Forever.toc"]
  flag_words           words that put a kept source line on the build report's "needs overlay" list (whole word, any case,
                       optional plural)
