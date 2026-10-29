#!/usr/bin/env python3
"""Static checks for the Forever Guidelime files:
 - Lua long-string sanity (exactly one closing ]] per file, no stray ]] inside)
 - tag syntax: every [..] tag has a known Guidelime code and a parseable payload
 - every [G] has a zone Guidelime knows
 - quest flow across the chapter chain: each QA has a later QT or QS; each QT/QC has an earlier QA (or is item/inside-started);
   prerequisites (Questie preQuestSingle/Group, atlas series order) are turned in before the pickup
 - required level vs the chapter's stated level band
"""
import re, json, sys, glob, os

# Paths: everything lives in the "WoW Forever Atlas" folder (this file sits in its tooling\ subfolder).
# Override the folder with the FOREVER_ATLAS environment variable if you move things around.
BASE = os.environ.get('FOREVER_ATLAS', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
ADDON = os.path.join(BASE, 'guide', 'Guidelime_ForeverAlliance')
Q = json.load(open(os.path.join(BASE, 'tooling', 'qdb', 'quest.json'), encoding='utf-8'))          # Questie Classic quest DB (luatab.py)
WQ = {int(k): v for k, v in json.load(open(os.path.join(BASE, 'data', 'quests.json'), encoding='utf-8')).items()}  # Wowhead Forever atlas
_extra = os.path.join(BASE, 'tooling', 'extra_quests.json')                                          # hand-added atlas rows (optional)
extra = json.load(open(_extra, encoding='utf-8')) if os.path.exists(_extra) else {}
for k, v in extra.items(): WQ[int(k)] = v
ZONES = {'dunmorogh', 'lochmodan', 'ironforge', 'westfall', 'stormwindcity', 'elwynnforest', 'redridgemountains', 'wetlands', 'deadmines', 'stockade', 'duskwood',
         'darkshore', 'teldrassil', 'darnassus', 'hillsbradfoothills', 'silverpineforest', 'ashenvale', 'alteracmountains', 'arathihighlands',
         'stranglethornvale', 'stonetalonmountains', 'barrens', 'tirisfalglades', 'dustwallowmarsh', 'badlands'}
CODES = {'N', 'NX', 'D', 'GA', 'A', 'O', 'OC', 'QA', 'QC', 'QT', 'QS', 'G', 'L', 'XP', 'H', 'F', 'T', 'S', 'P', 'V', 'R', 'CI', 'UI', 'TAR', 'LE', 'SK', 'GG', 'GL', 'GT', 'GI', 'REP', 'SP'}
TAG = re.compile(r'\[([A-Z]+)\s*([^\]]*)\]')

def qname(qid):
    if qid in WQ and WQ[qid].get('name'): return WQ[qid]['name']
    r = Q.get(str(qid)); return r[0] if r else '?'
def qreq(qid):
    if qid in WQ and WQ[qid].get('g', {}).get('reqlevel'): return WQ[qid]['g']['reqlevel']
    r = Q.get(str(qid)); return r[3] if r else None
def qpre(qid):
    """(any-of list, all-of list) of prerequisite quest ids."""
    r = Q.get(str(qid))
    if r:
        r = list(r) + [None] * 40
        return (r[12] or [], r[11] or [])
    w = WQ.get(qid)
    if w and w.get('series'):
        ser = w['series']
        idx = [i for i, s in enumerate(ser) if s.get('current')]
        if idx and idx[0] > 0:
            return ([ser[idx[0] - 1]['id']], [])
    return ([], [])
def qstart_item(qid):
    r = Q.get(str(qid))
    if r and r[1] and len(r[1]) > 2 and r[1][2]: return True
    w = WQ.get(qid)
    if w:
        st = w.get('info', {}).get('start', [])
        if not st: return True  # atlas has no giver -> item/inside start
        if any(e['kind'] == 'item' for e in st): return True
    return False

files = sorted(glob.glob(f'{ADDON}/[0-9]*.lua'))   # 00a..07 = 1-20, 08.. = 20-30
problems = 0
def warn(f, ln, msg):
    global problems; problems += 1; print(f'{os.path.basename(f)}:{ln}: {msg}')

events = []  # (file, line, code, qid, optional)
# 25 Oct 2026: carried quests. A [QA] on a line containing the literal text "carry to 30-40" is a pickup whose turn-in
# lives in the next bracket's guide (e.g. the City of Dalaran lead-ins), so the flow check does not ask for a [QT]/[QS]
CARRIED = set()
RACE = {}    # (file, line) -> race the step applies to ('' = everyone)
GA = {}      # file -> race restriction from [GA ...] ('' when the chapter applies to everyone)
for f in files:
    txt = open(f, encoding='utf-8').read()
    mga = re.search(r'^\[GA ([^\]]+)\]', txt, re.M)
    GA[f] = mga.group(1).strip() if mga and mga.group(1).strip() not in ('Alliance',) else ''
    if txt.count(']]') != 1: warn(f, 0, f"expected exactly one ']]' (found {txt.count(']]')})")
    if not txt.startswith('Guidelime.registerGuide([[\n'): warn(f, 1, 'bad header')
    if not txt.rstrip().endswith('"Forever Alliance 1-30")'): warn(f, 0, 'bad footer/group (expected "Forever Alliance 1-30")')
    body = txt.split('[[', 1)[1].split(']]', 1)[0]
    for ln, line in enumerate(body.split('\n'), 2):
        if not line.strip(): continue
        mra = re.search(r'\[A ([^\]]+)\]', line)
        RACE[(f, ln)] = next((r for r in ('Dwarf', 'Human', 'Gnome', 'Night Elf') if mra and r in mra.group(1)), GA[f])
        if mra and 'Shaman' in mra.group(1) and RACE[(f, ln)] == GA[f]: RACE[(f, ln)] = 'Dwarf'   # Shaman lines are Dwarf-only in this guide
        if line.count('[') != line.count(']'): warn(f, ln, f'unbalanced brackets: {line[:80]}')
        optional = line.startswith('[O]') or line.startswith('[OC]')
        has_goto = False
        for m in TAG.finditer(line):
            code, payload = m.group(1), m.group(2).strip()
            if code not in CODES: warn(f, ln, f'unknown code [{code} {payload[:30]}]')
            if code in ('QA', 'QC', 'QT', 'QS'):
                mm = re.match(r'(\d+)(?:,(\d+))?\s*(.*)$', payload)
                if not mm: warn(f, ln, f'bad quest tag [{code} {payload}]'); continue
                qid = int(mm.group(1)); title = mm.group(3)
                events.append((f, ln, code, qid, optional))
                if code == 'QA' and 'carry to 30-40' in line: CARRIED.add(qid)   # deliberately handed to the next bracket's guide
                if code == 'QA' and not title: warn(f, ln, f'[QA{qid}] has no title (new Forever quests show as numbers without one)')
            elif code == 'G':
                mm = re.match(r'(\d+\.?\d*)\s*,\s*(\d+\.?\d*)\s*(.*)$', payload)
                if not mm: warn(f, ln, f'bad goto [{code} {payload}]'); continue
                z = re.sub(r"[\s']", '', re.sub(r'^The ', '', mm.group(3).strip()).lower())
                if z.startswith('the'): z = z[3:]
                if z not in ZONES: warn(f, ln, f'unknown zone in [G {payload}]')
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
                    if part.strip() not in ('Shaman', 'Hunter', 'Alliance', 'Dwarf', 'Gnome', 'Human', 'Night Elf'): warn(f, ln, f'odd [A {payload}]')
        # optional steps with a quest tag must carry a [G] (no auto goto for optional steps)
        if optional and line.startswith('[O]') and re.search(r'\[Q[ACT]\d', line) and not has_goto:
            warn(f, ln, f'optional quest step without [G]: {line[:70]}')

# flow check - run once per race chain (00a/00b = Human start, 01a/01b = Dwarf start, 02+ shared), so a turn-in on the
# Human path never satisfies a prerequisite on the Dwarf path (17 Oct 2026: the Forever DB's prerequisites exposed this)
CHAINS = {'Human': lambda f: not os.path.basename(f).startswith('01'), 'Dwarf': lambda f: not os.path.basename(f).startswith('00')}
_seen_warn = set()
_warn0 = warn
def warn(f, ln, msg):
    if (f, ln, msg) in _seen_warn: return
    _seen_warn.add((f, ln, msg)); _warn0(f, ln, msg)
for chain, keep in CHAINS.items():
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

# level requirement vs chapter band
# band = the [N min-max ...] header of each file (a pickup may need up to the chapter's top level)
bands = {}
for f in files:
    mn = re.search(r'^\[N (\d+)-(\d+) ', open(f, encoding='utf-8').read(), re.M)
    bands[f] = (int(mn.group(1)), int(mn.group(2))) if mn else (1, 60)
for f, ln, code, qid, opt in events:
    if code != 'QA': continue
    b = bands[f]
    req = qreq(qid)
    if req and req > b[1]: warn(f, ln, f'[QA{qid}] {qname(qid)} requires level {req} but the chapter tops out at {b[1]}')
# chapter chain: every [NX] must name an existing [N] exactly (Guidelime builds the key as "min-max title",
# so "20+ Loose Ends" does NOT match "[N 20-22 Loose Ends]")
names = {}
for f in files:
    m = re.search(r'^\[N ([^\]]+)\]', open(f, encoding='utf-8').read(), re.M)
    if m: names[m.group(1).strip()] = f
for f in files:
    for m in re.finditer(r'^\[NX ([^\]]+)\]', open(f, encoding='utf-8').read(), re.M):
        if m.group(1).strip() not in names: warn(f, 0, f'[NX {m.group(1)}] does not match any chapter [N ...]: {sorted(names)}')

print(f'\n{len(events)} quest events across {len(files)} files; {problems} problems')
