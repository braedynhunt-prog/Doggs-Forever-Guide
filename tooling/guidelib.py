#!/usr/bin/env python3
"""Shared parsing for the Forever Guidelime files and the data they are checked against.

Extracted from check_guide.py on 28 Oct 2026 so check_guide.py (flow) and verify.py (NPCs, spawns, gates) read
the Lua the same way. Nothing here prints; callers decide what is a finding.

Data (all relative to the "WoW Forever Atlas" folder, override with FOREVER_ATLAS; the addon folder with FOREVER_GUIDE):
  tooling/qdb/{quest,npc,object,item}.json   QuestieDB Forever 1.0.6 decoded by questiedb_baked.py
      quest row: [0] name, [1] startedBy [npcIds, objectIds, itemIds], [2] finishedBy [npcIds, objectIds], [3] reqLevel,
                 [11] preQuestGroup (all of), [12] preQuestSingle (any of)
      npc row:   [0] name, [6] spawns {zoneId: [[x, y], ...]}
      object row:[0] name, [3] spawns {zoneId: [[x, y], ...]}
  data/quests.json (+ tooling/extra_quests.json)   Wowhead Forever atlas rows: name, g.reqlevel, g.xp, info.start/end, series
Variants (1 Nov 2026): when FOREVER_GUIDE names a generator-built folder (tooling/variants/<v>/variant.json "folder"),
FOOTER / CHAINS / DEFAULT_CHAIN / RACES / RACE_WORDS follow that variant; baseline_path() gives per-folder baselines.
"""
import re, json, os, glob

BASE = os.environ.get('FOREVER_ATLAS', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
ADDON = os.environ.get('FOREVER_GUIDE', os.path.join(BASE, 'guide', 'Guidelime_ForeverShaman'))
QDB = os.path.join(BASE, 'tooling', 'qdb')

# Guidelime zone keys as check_guide normalises them (lower case, no spaces/apostrophes, leading "The" dropped)
ZONES = {'dunmorogh', 'lochmodan', 'ironforge', 'westfall', 'stormwindcity', 'elwynnforest', 'redridgemountains', 'wetlands', 'deadmines', 'stockade', 'duskwood',
         'darkshore', 'teldrassil', 'darnassus', 'hillsbradfoothills', 'silverpineforest', 'ashenvale', 'alteracmountains', 'arathihighlands',
         'stranglethornvale', 'stonetalonmountains', 'barrens', 'tirisfalglades', 'dustwallowmarsh', 'badlands',
         'zephrasisle', 'moonglade'}   # Moonglade: druid class quests, added 2 Nov 2026. Zephras Isle: Skyborne start, Guidelime map 2521 (Data/MapDB.lua Forever block), added 1 Nov 2026
# zone display name (as written in [G x,y Zone]) -> Forever map id used by the DB spawn tables
ZID = {'Dun Morogh': 1, 'Loch Modan': 38, 'Ironforge': 1537, 'Westfall': 40, 'Elwynn Forest': 12, 'Stormwind City': 1519, 'Redridge Mountains': 44,
       'Duskwood': 10, 'Wetlands': 11, 'Darkshore': 148, 'Teldrassil': 141, 'Darnassus': 1657, 'Hillsbrad Foothills': 267, 'Silverpine Forest': 130,
       'Ashenvale': 331, 'Alterac Mountains': 36, 'Arathi Highlands': 45, 'Stranglethorn Vale': 33, 'Stonetalon Mountains': 406, 'The Barrens': 17,
       'Tirisfal Glades': 85, 'Dustwallow Marsh': 15, 'Badlands': 3, 'Zephras Isle': 16593, 'Moonglade': 493}
CODES = {'N', 'NX', 'D', 'GA', 'A', 'O', 'OC', 'QA', 'QC', 'QT', 'QS', 'G', 'L', 'XP', 'H', 'F', 'T', 'S', 'P', 'V', 'R', 'CI', 'UI', 'TAR', 'LE', 'SK', 'GG', 'GL', 'GT', 'GI', 'REP', 'SP'}
RACES = ('Dwarf', 'Human', 'Gnome', 'Night Elf', 'Skyborne')
RACE_WORDS = ('Shaman', 'Hunter', 'Alliance', 'Dwarf', 'Gnome', 'Human', 'Night Elf', 'Warrior', 'Skyborne', 'Druid')

TAG = re.compile(r'\[([A-Z]+)\s*([^\]]*)\]')
QUEST_PAYLOAD = re.compile(r'(\d+)(?:,(\d+))?\s*(.*)$')
GOTO_PAYLOAD = re.compile(r'(\d+\.?\d*)\s*,\s*(\d+\.?\d*)\s*(.*)$')
TAR_TAG = re.compile(r'\[TAR(\d+) ([^\]]*)\]')
A_TAG = re.compile(r'\[A ([^\]]+)\]')
HEADER = 'Guidelime.registerGuide([[\n'
FOOTER = '"Forever Shaman 1-30")'
ALLIANCE_FOLDER = 'Guidelime_ForeverShaman'
DEFAULT_CHAIN = 'Dwarf'   # verify.py's default chain

# ---------------------------------------------------------------- variants (1 Nov 2026)
# A generator-built addon (tooling/build_variant.py) is described by tooling/variants/<v>/variant.json. When
# FOREVER_GUIDE names a variant's output folder (its basename is the variant's "folder", or the folder holds
# "<folder>.toc"), FOOTER, CHAINS, DEFAULT_CHAIN, RACES and RACE_WORDS follow the variant.
VARIANTS_DIR = os.path.join(BASE, 'tooling', 'variants')

def variants():
    """[(path to variant.json, parsed dict)] for every tooling/variants/*/variant.json."""
    out = []
    for p in sorted(glob.glob(os.path.join(VARIANTS_DIR, '*', 'variant.json'))):
        try:
            out.append((p, json.load(open(p, encoding='utf-8'))))
        except (OSError, ValueError):
            continue
    return out

def find_variant(addon=None):
    """(path, dict) of the variant whose output folder is the addon folder, or None (the Alliance guide)."""
    a = os.path.normpath(os.path.abspath(addon or ADDON))
    for p, v in variants():
        f = v.get('folder')
        if f and (os.path.basename(a) == f or os.path.exists(os.path.join(a, f + '.toc'))):
            return p, v
    return None

def baseline_path(kind, addon=None):
    """tooling/<kind>_baseline.txt for the Alliance folder (names unchanged), tooling/<kind>_baseline_<folder>.txt
    for any other addon folder (kind: 'check_guide' or 'verify')."""
    folder = os.path.basename(os.path.normpath(os.path.abspath(addon or ADDON)))
    v = find_variant(addon)
    if v: folder = v[1]['folder']
    name = '%s_baseline.txt' % kind if folder == ALLIANCE_FOLDER else '%s_baseline_%s.txt' % (kind, folder)
    return os.path.join(BASE, 'tooling', name)

# ---------------------------------------------------------------- data
_cache = {}
def db(name):
    """quest / npc / object / item table of the Forever QuestieDB, keyed by id string."""
    if name not in _cache:
        _cache[name] = json.load(open(os.path.join(QDB, name + '.json'), encoding='utf-8'))
    return _cache[name]

def atlas():
    """Wowhead Forever atlas rows keyed by int quest id, with tooling/extra_quests.json merged in."""
    if 'atlas' not in _cache:
        wq = {int(k): v for k, v in json.load(open(os.path.join(BASE, 'data', 'quests.json'), encoding='utf-8')).items()}
        extra = os.path.join(BASE, 'tooling', 'extra_quests.json')
        if os.path.exists(extra):
            for k, v in json.load(open(extra, encoding='utf-8')).items(): wq[int(k)] = v
        _cache['atlas'] = wq
    return _cache['atlas']

def qname(qid):
    WQ = atlas()
    if qid in WQ and WQ[qid].get('name'): return WQ[qid]['name']
    r = db('quest').get(str(qid)); return r[0] if r else '?'

def qreq(qid):
    WQ = atlas()
    if qid in WQ and WQ[qid].get('g', {}).get('reqlevel'): return WQ[qid]['g']['reqlevel']
    r = db('quest').get(str(qid)); return r[3] if r else None

def qpre(qid):
    """(any-of list, all-of list) of prerequisite quest ids."""
    r = db('quest').get(str(qid))
    if r:
        r = list(r) + [None] * 40
        return (r[12] or [], r[11] or [])
    w = atlas().get(qid)
    if w and w.get('series'):
        ser = w['series']
        idx = [i for i, s in enumerate(ser) if s.get('current')]
        if idx and idx[0] > 0:
            return ([ser[idx[0] - 1]['id']], [])
    return ([], [])

def qstart_item(qid):
    r = db('quest').get(str(qid))
    if r and r[1] and len(r[1]) > 2 and r[1][2]: return True
    w = atlas().get(qid)
    if w:
        st = w.get('info', {}).get('start', [])
        if not st: return True  # atlas has no giver -> item/inside start
        if any(e['kind'] == 'item' for e in st): return True
    return False

def _ids(lst, i):
    if not lst or len(lst) <= i or not lst[i]: return []
    return [int(x) for x in lst[i] if x is not None]

def qstarts(qid):
    """{'npc': [...], 'object': [...], 'item': [...]} from the Forever DB (None when the quest is not in it)."""
    r = db('quest').get(str(qid))
    if not r: return None
    return {'npc': _ids(r[1], 0), 'object': _ids(r[1], 1), 'item': _ids(r[1], 2)}

def qends(qid):
    r = db('quest').get(str(qid))
    if not r: return None
    return {'npc': _ids(r[2], 0), 'object': _ids(r[2], 1)}

def npc_name(nid):
    n = db('npc').get(str(nid)); return (n[0] or '') if n else None

def npc_spawns(nid, zone_id=None):
    """[[x, y], ...] for the NPC (in one zone, or every zone when zone_id is None); [] when none, None when the NPC is unknown."""
    n = db('npc').get(str(nid))
    if not n: return None
    sp = n[6] if isinstance(n[6], dict) else {}
    zones = [str(zone_id)] if zone_id is not None else list(sp)
    return [p for z in zones for p in sp.get(z, []) if p and p[0] is not None and p[0] >= 0]

def npc_zones(nid):
    n = db('npc').get(str(nid))
    sp = (n[6] if n and isinstance(n[6], dict) else {})
    return [z for z, v in sp.items() if any(p and p[0] is not None and p[0] >= 0 for p in v)]

def object_name(oid):
    o = db('object').get(str(oid)); return (o[0] or '') if o else None

# ---------------------------------------------------------------- Lua
def chapter_files(addon=None):
    return sorted(glob.glob(os.path.join(addon or ADDON, '[0-9]*.lua')))

def read(path):
    return open(path, encoding='utf-8').read()

def body(txt):
    """The guide text between the [[ and ]] of registerGuide."""
    return txt.split('[[', 1)[1].split(']]', 1)[0]

def chapter_ga(txt):
    """Race restriction from the chapter's [GA ...] ('' for Alliance / everyone)."""
    m = re.search(r'^\[GA ([^\]]+)\]', txt, re.M)
    return m.group(1).strip() if m and m.group(1).strip() not in ('Alliance',) else ''

def chapter_title(txt):
    m = re.search(r'^\[N ([^\]]+)\]', txt, re.M)
    return m.group(1).strip() if m else None

def chapter_next(txt):
    return [m.group(1).strip() for m in re.finditer(r'^\[NX ([^\]]+)\]', txt, re.M)]

def chapter_band(txt):
    m = re.search(r'^\[N (\d+)-(\d+) ', txt, re.M)
    return (int(m.group(1)), int(m.group(2))) if m else (1, 60)

def steps(txt):
    """(line number, line) for every non-blank line of the body; numbering matches the file.
    The body starts with the remainder of line 1 (after '[['), so element 0 is line 1 - check_guide.py enumerated
    from 2 until 28 Oct 2026 and reported every line one too high."""
    for ln, line in enumerate(body(txt).split('\n'), 1):
        if line.strip(): yield ln, line

def race_of(line, ga):
    """Which race a step applies to: '' = everyone. Shaman lines count as Dwarf (the only shaman in this guide)."""
    mra = A_TAG.search(line)
    race = next((r for r in RACES if mra and r in mra.group(1)), ga)
    if mra and 'Shaman' in mra.group(1) and race == ga: race = 'Dwarf'
    return race

def is_optional(line):
    return line.startswith('[O]') or line.startswith('[OC]')

def tags(line):
    return [(m.group(1), m.group(2).strip()) for m in TAG.finditer(line)]

def quest_tag(payload):
    """payload of a [QA/QC/QT/QS ...] -> (qid, count or None, title) or None when malformed."""
    m = QUEST_PAYLOAD.match(payload)
    if not m: return None
    return int(m.group(1)), (int(m.group(2)) if m.group(2) else None), m.group(3)

def goto_tag(payload):
    """payload of a [G ...] -> (x, y, zone text as written) or None when malformed."""
    m = GOTO_PAYLOAD.match(payload)
    if not m: return None
    return float(m.group(1)), float(m.group(2)), m.group(3).strip()

def zone_key(zone_text):
    """'The Barrens' / 'Stormwind City' -> the key used in ZONES."""
    z = re.sub(r"[\s']", '', re.sub(r'^The ', '', zone_text.strip()).lower())
    if z.startswith('the'): z = z[3:]
    return z

def quest_tags(line):
    """[(code, qid, title)] for the QA/QC/QT/QS tags on a line (malformed ones skipped)."""
    out = []
    for code, payload in tags(line):
        if code in ('QA', 'QC', 'QT', 'QS'):
            q = quest_tag(payload)
            if q: out.append((code, q[0], q[2]))
    return out

def gotos(line):
    """[(x, y, zone text)] for the [G] tags on a line."""
    return [g for code, payload in tags(line) if code == 'G' for g in [goto_tag(payload)] if g]

def tars(line):
    """[(npc id int, name as written)] for the [TAR] tags on a line, in order."""
    return [(int(i), nm.strip()) for i, nm in TAR_TAG.findall(line)]

# ---------------------------------------------------------------- chapter chains
# Flow runs once per race chain: Human = 00a/00b + shared, Dwarf = 01a/01b + shared. Shaman lines are Dwarf.
CHAINS = {'Human': lambda f: not os.path.basename(f).startswith('01'), 'Dwarf': lambda f: not os.path.basename(f).startswith('00')}

VARIANT = find_variant()
if VARIANT:
    # a variant has one race chain over all of its chapters (variant.json "chain", e.g. Skyborne)
    _v = VARIANT[1]
    FOOTER = '"%s")' % _v['group']
    DEFAULT_CHAIN = _v.get('chain') or _v.get('race')
    CHAINS = {DEFAULT_CHAIN: lambda f: True}
    _tw = [w for cat in (_v.get('tag_words') or {}).values() for side in ('keep', 'drop') for w in cat.get(side, [])]
    RACE_WORDS = tuple(dict.fromkeys(RACE_WORDS + tuple(_tw)))
    _races = [w for side in ('keep', 'drop') for w in (_v.get('tag_words') or {}).get('races', {}).get(side, [])]
    RACES = tuple(dict.fromkeys(RACES + tuple(_races)))

def chain_files(chain, addon=None):
    return [f for f in chapter_files(addon) if CHAINS[chain](f)]

def on_chain(line, ga, chain):
    """True when a step applies to the given race chain."""
    return race_of(line, ga) in ('', chain)
