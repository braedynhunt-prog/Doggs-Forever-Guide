#!/usr/bin/env python3
"""Static checks for the Forever Guidelime files:
 - Lua long-string sanity (exactly one closing ]] per file, no stray ]] inside)
 - tag syntax: every [..] tag has a known Guidelime code and a parseable payload
 - every [G] has a zone Guidelime knows
 - quest flow across the chapter chain: each QA has a later QT or QS; each QT/QC has an earlier QA (or is item/inside-started);
   prerequisites (Questie preQuestSingle/Group, atlas series order) are turned in before the pickup
 - required level vs the chapter's stated level band
Parsing and data access live in guidelib.py (shared with verify.py since 28 Oct 2026).
"""
import re, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import guidelib as gl
from guidelib import qname, qreq, qpre, qstart_item

files = gl.chapter_files()   # 00a..07 = 1-20, 08.. = 20-30
problems = 0
def warn(f, ln, msg):
    global problems; problems += 1; print(f'{os.path.basename(f)}:{ln}: {msg}')

events = []  # (file, line, code, qid, optional)
# 25 Oct 2026: carried quests. A [QA] on a line containing the literal text "carry to 30-40" is a pickup whose turn-in
# lives in the next bracket's guide (e.g. the City of Dalaran lead-ins), so the flow check does not ask for a [QT]/[QS]
CARRIED = set()
RACE = {}    # (file, line) -> race the step applies to ('' = everyone)
GA = {}      # file -> race restriction from [GA ...] ('' when the chapter applies to everyone)
TXT = {}
for f in files:
    txt = TXT[f] = gl.read(f)
    GA[f] = gl.chapter_ga(txt)
    if txt.count(']]') != 1: warn(f, 0, f"expected exactly one ']]' (found {txt.count(']]')})")
    if not txt.startswith(gl.HEADER): warn(f, 1, 'bad header')
    if not txt.rstrip().endswith(gl.FOOTER): warn(f, 0, f'bad footer/group (expected {gl.FOOTER[:-1]})')   # variant group since 1 Nov 2026
    for ln, line in gl.steps(txt):
        RACE[(f, ln)] = gl.race_of(line, GA[f])
        if line.count('[') != line.count(']'): warn(f, ln, f'unbalanced brackets: {line[:80]}')
        optional = gl.is_optional(line)
        has_goto = False
        for code, payload in gl.tags(line):
            if code not in gl.CODES: warn(f, ln, f'unknown code [{code} {payload[:30]}]')
            if code in ('QA', 'QC', 'QT', 'QS'):
                q = gl.quest_tag(payload)
                if not q: warn(f, ln, f'bad quest tag [{code} {payload}]'); continue
                qid, _, title = q
                events.append((f, ln, code, qid, optional))
                if code == 'QA' and 'carry to 30-40' in line: CARRIED.add(qid)   # deliberately handed to the next bracket's guide
                if code == 'QA' and not title: warn(f, ln, f'[QA{qid}] has no title (new Forever quests show as numbers without one)')
            elif code == 'G':
                g = gl.goto_tag(payload)
                if not g: warn(f, ln, f'bad goto [{code} {payload}]'); continue
                if gl.zone_key(g[2]) not in gl.ZONES: warn(f, ln, f'unknown zone in [G {payload}]')
                has_goto = True
            elif code == 'TAR':
                if not re.match(r'\d+', payload): warn(f, ln, f'bad TAR [{payload}]')
            elif code == 'CI':
                if not re.match(r'\d+,\d+', payload): warn(f, ln, f'bad CI [{payload}]')
            elif code == 'UI':
                if not re.match(r'\d+', payload): warn(f, ln, f'bad UI [{payload}]')
            elif code == 'XP':
                if not re.match(r'\d+', payload): warn(f, ln, f'bad XP [{payload}]')
            elif code in ('A', 'GA'):
                for part in payload.split(','):
                    if part.strip() not in gl.RACE_WORDS: warn(f, ln, f'odd [A {payload}]')
        # optional steps with a quest tag must carry a [G] (no auto goto for optional steps)
        if optional and line.startswith('[O]') and re.search(r'\[Q[ACT]\d', line) and not has_goto:
            warn(f, ln, f'optional quest step without [G]: {line[:70]}')
        # 4 Nov 2026: a step whose only completable element is the [G] completes when the player is within 6 yards of it
        # (Guidelime CurrentGuide.lua updateStepCompletion). Travel steps want that; an action step (learn, buy, loot, use,
        # kill, skill up) does not - it needs a tag that holds it: [T] [V] [R] [S] [P] [QA] [QC] [QT] [CI] [UI] [SK] [LE] [XP]
        # Human and Hunter lines are not maintained (27 Oct 2026), so they are left out of this check
        if has_goto and not line.startswith('[OC]') and RACE[(f, ln)] != 'Human' and '[A Hunter]' not in line and not re.search(r'\[(T|V|R|S|P|H|F|QA|QC|QT|QS|QP|QW|CI|UI|SK|LE|SP|XP|REP)[\s\d\]]', line) \
                and re.search(r'\b(learn|train|buy|loot|use the|kill|cook to|bandage to|fish to)\b', line, re.I):
            warn(f, ln, f'goto-only action step (completes on arrival): {line[:70]}')

# flow check - run once per race chain (00a/00b = Human start, 01a/01b = Dwarf start, 02+ shared), so a turn-in on the
# Human path never satisfies a prerequisite on the Dwarf path (17 Oct 2026: the Forever DB's prerequisites exposed this)
_seen_warn = set()
_warn0 = warn
def warn(f, ln, msg):
    if (f, ln, msg) in _seen_warn: return
    _seen_warn.add((f, ln, msg)); _warn0(f, ln, msg)
for chain, keep in gl.CHAINS.items():
  accepted = {}   # qid -> (file, ln, optional)
  turned = set(); skipped = set(); completed = {}
  for i, (f, ln, code, qid, opt) in enumerate(events):
      if not keep(f): continue
      if RACE.get((f, ln), '') not in ('', chain): continue   # other race's line
      if code == 'QA':
          r0 = RACE.get((accepted[qid][0], accepted[qid][1]), '') if qid in accepted else ''
          r1 = RACE.get((f, ln), '')
          if qid in accepted and qid not in turned and not (r0 and r1 and r0 != r1):
              warn(f, ln, f'[QA{qid}] {qname(qid)} accepted twice without turn-in')
          any_of, all_of = qpre(qid)
          # prerequisites must be turned in earlier (scheduled turn-ins earlier in the same line count via event order)
          if any_of and not any(p in turned for p in any_of):
              warn(f, ln, f'[QA{qid}] {qname(qid)} needs one of {any_of} turned in first ({[qname(p) for p in any_of]})')
          for p in all_of:
              if p not in turned: warn(f, ln, f'[QA{qid}] {qname(qid)} needs {p} {qname(p)} turned in first')
          accepted[qid] = (f, ln, opt)
      elif code in ('QC',):
          if qid not in accepted: warn(f, ln, f'[QC{qid}] {qname(qid)} before any [QA]')
          completed[qid] = (f, ln)
      elif code == 'QT':
          if qid not in accepted:
              if qstart_item(qid): pass
              else: warn(f, ln, f'[QT{qid}] {qname(qid)} before any [QA] (and it is not item-started)')
          turned.add(qid)
      elif code == 'QS':
          skipped.add(qid)
  for qid, (f, ln, opt) in accepted.items():
      if qid not in turned and qid not in skipped and qid not in CARRIED:
          warn(f, ln, f'[QA{qid}] {qname(qid)} is never turned in or skipped' + (' (optional)' if opt else ''))

# hearth binds (2 Nov 2026, after the Lakeshire bind in 06 was followed by "Hearth to Sentinel Hill" in 07-10 without a
# rebind): on each chain, every [H X] must match the latest [S X]; the first [H] before any [S] is taken as the starting
# inn (a new character is bound there) and the chain's bind is set to it
for chain, keep in gl.CHAINS.items():
    bound = None
    for f in files:
        if not keep(f): continue
        for ln, line in gl.steps(TXT[f]):
            if RACE.get((f, ln), '') not in ('', chain): continue
            for code, payload in gl.tags(line):
                if code == 'S':
                    bound = (payload.strip(), os.path.basename(f), ln)
                elif code == 'H':
                    h = payload.strip()
                    if bound is None: bound = (h, os.path.basename(f), ln)
                    elif h != bound[0]:
                        warn(f, ln, f'[H {h}] but the hearth is bound to {bound[0]} ([S] at {bound[1]}:{bound[2]}) on the {chain} chain')

# level requirement vs chapter band
# band = the [N min-max ...] header of each file (a pickup may need up to the chapter's top level)
bands = {f: gl.chapter_band(TXT[f]) for f in files}
for f, ln, code, qid, opt in events:
    if code != 'QA': continue
    b = bands[f]
    req = qreq(qid)
    if req and req > b[1]: warn(f, ln, f'[QA{qid}] {qname(qid)} requires level {req} but the chapter tops out at {b[1]}')
# chapter chain: every [NX] must name an existing [N] exactly (Guidelime builds the key as "min-max title",
# so "20+ Loose Ends" does NOT match "[N 20-22 Loose Ends]")
names = {}
for f in files:
    t = gl.chapter_title(TXT[f])
    if t: names[t] = f
for f in files:
    for nx in gl.chapter_next(TXT[f]):
        if nx not in names: warn(f, 0, f'[NX {nx}] does not match any chapter [N ...]: {sorted(names)}')

print(f'\n{len(events)} quest events across {len(files)} files; {problems} problems')
