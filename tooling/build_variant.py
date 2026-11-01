#!/usr/bin/env python3
r"""Build a generator-made Guidelime addon (a class/race variant of the Forever Alliance guide). Added 1 Nov 2026.

    python tooling\build_variant.py tooling\variants\skyborne_warrior\variant.json            -> guide\<folder>\ + zip
    python tooling\build_variant.py <variant.json> --out <dir>      -> build into <dir> (zip <dir>.zip, report beside it)
    python tooling\build_variant.py <variant.json> --passthrough --out <dir>
                                    -> copy the source chapters through the same read/write path with every transform
                                       off; the chapter files must be byte-identical to the Alliance ones (regression test)
    --report <file>                 -> where the build report goes (default: tooling\variants\<v>\build_report.txt for a
                                       build into guide\, <out>_build_report.txt next to --out)

Inputs: the variant folder (variant.json, profile.json, chapters\, overlay\, the generated gear JSON named by
variant.json "generated_gear"), the source chapters (variant.json "source_folder", the Alliance addon). The source is
never written. Schema of variant.json: tooling\variants\skyborne_warrior\README.txt.

Per source chapter, in this order:
  1. overlay      overlay\<key>.txt (or overlay\<file stem>.txt), anchors resolved against the SOURCE file's lines
  2. filter       lines whose [A ...] tags exclude the variant are dropped (each category present - class / race /
                  faction - must name a "keep" word; an unknown word aborts); untagged [OC] lines whose first heading is
                  |cffffcc00Gear:|r / |cffffcc00Loot (...):|r are stripped. Lines written by the overlay are never
                  dropped or stripped.
  3. gear         generated gear lines (gear_calls.py --emit) go right after the [QT] line they belong to (matched by
                  source line number, else the first surviving [QT<id>] line of the chapter); "unstated" and
                  "not_gear" picks and quests listed in "gear_skip_quests" are left out and reported
  4. rewrite      the [D <source_d_prefix>\\ header prefix becomes <d_prefix> (an @header block replaces the
                  description too); the footer ]], "<source_group>") becomes ]], "<group>")
Hand-written chapters (chapters\<file>) are copied verbatim; a missing one is a warning (they arrive in Phase 2).
Then both TOCs, the zip and the build report (drops, strips, overlay ops, gear lines placed / not placed, inline
gear text on step lines, and "needs overlay" lines: kept source lines containing a variant flag word).

Overlay files (overlay\<key>.txt):
  Lines starting with '#' are comments. Everything else belongs to the directive above it; a block ends at the next
  line starting with '@'. Trailing blank lines of a block are dropped, inner blank lines are kept.
  Anchors (matched against the source chapter's raw lines; '#n' picks the nth match, 1-based; zero matches, or more
  than one without '#n', aborts the build):
      QA<id> QT<id> QC<id>    the line holding [QA<id>... / [QT<id>... / [QC<id>...
      TAR<id>                 the line holding [TAR<id> ...]
      G<x>,<y>                the line holding [G<x>,<y> ...] (numbers exactly as written)
      N <title>               the line [N <title>]
      T <text>                the line containing <text> literally (for untagged [OC] notes; pick a substring that
                              occurs on exactly one line of the source chapter; the text may not contain '#')
  Directives:
      @replace <anchor>       the block replaces the anchored line (1+ lines)
      @after <anchor>         the block goes after the anchored line
      @before <anchor>        the block goes before the anchored line
      @delete <anchor>        the anchored line is removed (no block)
      @header                 one-line block: the chapter's [D ...] description (the text after the prefix and \\)
      @gear-dungeon <anchor> [=> <dropper>]
                              after the anchored line, the generated dungeon loot lines of this chapter (all groups,
                              or the one whose dropper is <dropper>: a creature name, or "trash")
  One @replace or @delete per line; @after/@before blocks on the same line keep file order.
"""
import argparse, json, os, re, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.normpath(os.environ.get('FOREVER_ATLAS', os.path.join(HERE, '..')))

A_TAG = re.compile(r'\[A ([^\]]+)\]')
GA_TAG = re.compile(r'\[GA ([^\]]+)\]')
GEAR_HEAD = re.compile(r'^\[OC\]\s*\|cffffcc00(?:Gear|Loot)(?: \([^)]*\))?:\|r', re.I)
INLINE_GEAR = re.compile(r'\|cffffcc00(?:Gear|Loot)\b[^|]*\|r', re.I)
COLOR = re.compile(r'\|c[0-9a-fA-F]{8}|\|r')
QT_RE = re.compile(r'\[QT(\d+)(?!\d)')
DIRECTIVES = ('replace', 'after', 'before', 'delete', 'header', 'gear-dungeon')
CATEGORIES = ('classes', 'races', 'factions')


class BuildError(Exception):
    pass


# ---------------------------------------------------------------- variant
def load_variant(path):
    """variant.json as a dict, plus _path, _dir, _source (absolute source addon folder)."""
    path = os.path.abspath(path)
    try:
        v = json.load(open(path, encoding='utf-8'))
    except (OSError, ValueError) as e:
        raise SystemExit('cannot read %s: %s' % (path, e))
    for k in ('name', 'folder', 'group', 'd_prefix', 'source_folder', 'source_group', 'source_d_prefix', 'class', 'race',
              'chain', 'tag_words', 'chapters', 'toc'):
        if k not in v:
            raise SystemExit('%s: missing key "%s"' % (path, k))
    v['_path'] = path
    v['_dir'] = os.path.dirname(path)
    v['_source'] = os.path.normpath(os.path.join(BASE, v['source_folder']))
    return v


def profile_name(v):
    p = os.path.join(v['_dir'], v.get('profile', 'profile.json'))
    try:
        return json.load(open(p, encoding='utf-8'))['profile']
    except (OSError, ValueError, KeyError):
        return None


def tag_keeps(payload, v):
    """True when an [A payload] / [GA payload] tag admits the variant. Raises BuildError on a word the variant
    does not classify."""
    words = [w.strip() for w in payload.split(',') if w.strip()]
    tw = v['tag_words']
    for w in words:
        if not any(w in tw.get(c, {}).get(s, []) for c in CATEGORIES for s in ('keep', 'drop')):
            raise BuildError('tag word "%s" in [%s] is in neither keep nor drop of variant.json tag_words' % (w, payload))
    for c in CATEGORIES:
        keep, drop = tw.get(c, {}).get('keep', []), tw.get(c, {}).get('drop', [])
        present = [w for w in words if w in keep or w in drop]
        if present and not any(w in keep for w in present):
            return False
    return True


def line_keeps(line, v):
    return all(tag_keeps(m.group(1), v) for m in A_TAG.finditer(line))


def is_untagged_gear(line):
    return bool(GEAR_HEAD.match(line)) and not A_TAG.search(line)


def plain(s):
    return COLOR.sub('', s)


def chapter_list(v):
    """[{key, file, source (abs path or None), hand (abs path or None)}] in variant order."""
    out = []
    for c in v['chapters']:
        src = c.get('source')
        out.append(dict(key=c['key'], file=c['file'],
                        source=os.path.join(v['_source'], src) if src else None,
                        hand=None if src else os.path.join(v['_dir'], 'chapters', c['file'])))
    return out


def filter_source(text, v):
    """Source text with step 2 (filter) applied, no overlay: for gear_calls.py / dungeon_loot.py. Line count changes."""
    out = []
    for line in text.split('\n'):
        if not line_keeps(line, v) or is_untagged_gear(line):
            continue
        out.append(line)
    return '\n'.join(out)


def chapter_texts(v, filtered=True):
    """[{key, file, text, source, hand, line_map}] for the chapters that exist. Source chapters are filtered (step 2
    only) unless filtered=False; line_map[i] = source line number of filtered line i+1 (None for hand-written)."""
    out = []
    for c in chapter_list(v):
        p = c['source'] or c['hand']
        if not os.path.exists(p):
            continue
        text = open(p, encoding='utf-8', newline='').read()
        lm = None
        if c['source'] and filtered:
            lines, lm = [], []
            for i, line in enumerate(text.split('\n'), 1):
                if not line_keeps(line, v) or is_untagged_gear(line):
                    continue
                lines.append(line)
                lm.append(i)
            text = '\n'.join(lines)
        out.append(dict(c, text=text, line_map=lm))
    return out


# ---------------------------------------------------------------- overlay
ANCHOR = re.compile(r'^(?:(QA|QT|QC|TAR)(\d+)|G(\d+(?:\.\d+)?),(\d+(?:\.\d+)?)|N (.+?)|T ([^#]+?))(?:#(\d+))?$')


def anchor_regex(anchor):
    m = ANCHOR.match(anchor.strip())
    if not m:
        raise BuildError('bad anchor "%s" (QA<id> QT<id> QC<id> TAR<id> G<x>,<y> N <title> T <text>, optional #n)' % anchor)
    code, num, gx, gy, title, text, nth = m.groups()
    if code:
        rx = re.compile(r'\[' + code + num + r'(?!\d)')
    elif gx:
        rx = re.compile(r'\[G\s*' + re.escape(gx) + r'\s*,\s*' + re.escape(gy) + r'(?![\d.])')
    elif text is not None:
        if not text.strip():
            raise BuildError('bad anchor "%s" (T needs text)' % anchor)
        rx = re.compile(re.escape(text.strip()))   # literal substring, 1 Nov 2026 (untagged [OC] notes)
    else:
        rx = re.compile(r'^\[N ' + re.escape(title.strip()) + r'\]\s*$')
    return rx, (int(nth) if nth else None)


def resolve(anchor, src_lines, where):
    try:
        rx, nth = anchor_regex(anchor)
    except BuildError as e:
        raise BuildError('%s: %s' % (where, e))
    hits = [i for i, l in enumerate(src_lines) if rx.search(l)]
    if not hits:
        raise BuildError('%s: anchor "%s" matches no line' % (where, anchor))
    if nth is None:
        if len(hits) > 1:
            raise BuildError('%s: anchor "%s" is ambiguous - %d lines (%s); add #n' % (
                where, anchor, len(hits), ', '.join(str(h + 1) for h in hits)))
        return hits[0]
    if nth < 1 or nth > len(hits):
        raise BuildError('%s: anchor "%s" asks for match %d of %d' % (where, anchor, nth, len(hits)))
    return hits[nth - 1]


def parse_overlay(path):
    """[{op, arg, body, ln}] from an overlay file."""
    ops, cur = [], None
    rel = os.path.relpath(path, BASE)
    for ln, line in enumerate(open(path, encoding='utf-8').read().split('\n'), 1):
        if line.startswith('#'):
            continue
        if line.startswith('@'):
            m = re.match(r'@([a-z-]+)\s*(.*)$', line.rstrip())
            if not m or m.group(1) not in DIRECTIVES:
                raise BuildError('%s:%d: unknown directive "%s" (known: %s)' % (rel, ln, line.strip(), ', '.join('@' + d for d in DIRECTIVES)))
            cur = dict(op=m.group(1), arg=m.group(2).strip(), body=[], ln=ln, file=rel)
            ops.append(cur)
            continue
        if cur is None:
            if line.strip():
                raise BuildError('%s:%d: text before the first directive' % (rel, ln))
            continue
        cur['body'].append(line)
    for o in ops:
        while o['body'] and not o['body'][-1].strip():
            o['body'].pop()
        where = '%s:%d @%s' % (o['file'], o['ln'], o['op'])
        if o['op'] in ('replace', 'after', 'before') and not o['body']:
            raise BuildError('%s: needs a block' % where)
        if o['op'] in ('delete', 'gear-dungeon') and o['body']:
            raise BuildError('%s: takes no block' % where)
        if o['op'] == 'header':
            if o['arg'] or len(o['body']) != 1:
                raise BuildError('%s: takes no anchor and exactly one line' % where)
        elif not o['arg']:
            raise BuildError('%s: needs an anchor' % where)
        if o['op'] == 'gear-dungeon':
            a, _, d = o['arg'].partition('=>')
            o['anchor'], o['dropper'] = a.strip(), (d.strip() or None)
        elif o['op'] != 'header':
            o['anchor'] = o['arg']
    return ops


def overlay_path(v, c):
    d = os.path.join(v['_dir'], 'overlay')
    cands = [p for p in (os.path.join(d, c['key'] + '.txt'), os.path.join(d, c['file'][:-4] + '.txt')) if os.path.exists(p)]
    if len(cands) > 1:
        raise BuildError('two overlay files for chapter %s: %s' % (c['key'], ', '.join(cands)))
    return cands[0] if cands else None


# ---------------------------------------------------------------- generated gear
def load_gear(v):
    p = os.path.join(v['_dir'], v.get('generated_gear', 'generated_gear.json'))
    if not os.path.exists(p):
        return None, p
    return json.load(open(p, encoding='utf-8')), p


def dungeon_lines(gear, key, dropper):
    if not gear:
        return []
    for d in gear.get('dungeons', []):
        if d.get('chapter') == key:
            return [g['text'] for g in d.get('groups', []) if g.get('text') and (dropper is None or g['dropper'] == dropper
                    or (dropper.isdigit() and int(dropper) in g.get('npc_ids', [])))]
    return []


# ---------------------------------------------------------------- build one chapter
def build_chapter(v, c, gear, rep, passthrough):
    raw = open(c['source'], encoding='utf-8', newline='').read()
    src = raw.split('\n')
    if passthrough:
        return '\n'.join(src)
    name = os.path.basename(c['source'])
    entries = []                      # dict(text, src line no or None, prot, kind)
    ops = []
    op_path = overlay_path(v, c)
    if op_path:
        ops = parse_overlay(op_path)
    before, after, repl, extra = {}, {}, {}, {}
    header = None
    for o in ops:
        where = '%s:%d @%s %s' % (o['file'], o['ln'], o['op'], o['arg'])
        if o['op'] == 'header':
            header = o['body'][0]
            rep['overlay'].append('%s: %s' % (c['key'], where))
            continue
        i = resolve(o['anchor'], src, where + ' (in %s)' % name)
        if o['op'] in ('replace', 'delete'):
            if i in repl:
                raise BuildError('%s: line %d already has @%s from line %d' % (where, i + 1, repl[i][0], repl[i][1]))
            repl[i] = (o['op'], o['ln'], o['body'])
        elif o['op'] == 'before':
            before.setdefault(i, []).extend(o['body'])
        elif o['op'] == 'after':
            after.setdefault(i, []).extend(o['body'])
        else:
            gl_ = dungeon_lines(gear, c['key'], o['dropper'])
            if not gl_:
                rep['warn'].append('%s: no generated dungeon loot lines for chapter %s%s' % (
                    where, c['key'], (' dropper ' + o['dropper']) if o['dropper'] else ''))
            extra.setdefault(i, []).extend(gl_)
        rep['overlay'].append('%s: %s -> source line %d' % (c['key'], where, i + 1))
    for i, line in enumerate(src):
        for t in before.get(i, []):
            entries.append(dict(text=t, src=None, prot=True, kind='overlay'))
        if i in repl:
            if repl[i][0] == 'replace':
                for t in repl[i][2]:
                    entries.append(dict(text=t, src=None, prot=True, kind='overlay', replaces=i + 1))
        else:
            entries.append(dict(text=line, src=i + 1, prot=False, kind='source'))
        for t in after.get(i, []):
            entries.append(dict(text=t, src=None, prot=True, kind='overlay'))
        for t in extra.get(i, []):
            entries.append(dict(text=t, src=None, prot=True, kind='gear'))

    # 2. filter
    kept = []
    for e in entries:
        if not e['prot']:
            try:
                ok = line_keeps(e['text'], v)
            except BuildError as ex:
                raise BuildError('%s:%d: %s' % (name, e['src'], ex))
            if not ok:
                rep['drops'].append('%s:%d  %s' % (name, e['src'], plain(e['text'])[:150]))
                continue
            if is_untagged_gear(e['text']):
                rep['strips'].append('%s:%d  %s' % (name, e['src'], plain(e['text'])[:150]))
                continue
            for m in GA_TAG.finditer(e['text']):
                if not tag_keeps(m.group(1), v):
                    rep['warn'].append('%s:%d: chapter tag [GA %s] excludes the variant' % (name, e['src'], m.group(1)))
        kept.append(e)

    # 3. generated gear after the [QT] lines
    skip = set(v.get('gear_skip_quests', []))
    for q in (gear or {}).get('quests', []):
        if q.get('chapter') != c['key']:
            continue
        label = '%s QT%d %s' % (c['key'], q['qid'], q.get('quest', ''))
        if q['qid'] in skip:
            rep['gear_skipped'].append(label + ' (gear_skip_quests)')
            continue
        if q.get('status') == 'not_gear':
            rep['gear_nongear'].append(label + ' (choices: %s)' % ', '.join(ch.get('name', '?') for ch in q.get('choices', [])))
            continue
        if q.get('status') == 'unstated' or not q.get('text'):
            rep['gear_unstated'].append(label + ' (missing tooltips: %s)' % ' '.join(map(str, q.get('missing_tooltips', []))))
            continue
        pos = next((k for k, e in enumerate(kept) if e['src'] == q.get('line') and QT_RE.search(e['text'])
                    and int(q['qid']) in [int(x) for x in QT_RE.findall(e['text'])]), None)
        if pos is None:
            pos = next((k for k, e in enumerate(kept) if int(q['qid']) in [int(x) for x in QT_RE.findall(e['text'])]), None)
        if pos is None:
            rep['gear_unplaced'].append(label + ' (no surviving [QT%d] line)' % q['qid'])
            continue
        k = pos + 1
        while k < len(kept) and kept[k]['kind'] == 'gear' and kept[k].get('after') is kept[pos]:
            k += 1
        kept.insert(k, dict(text=q['text'], src=None, prot=True, kind='gear', after=kept[pos]))
        rep['gear_placed'].append('%s after source line %s' % (label, kept[pos]['src']))

    # 4. header / footer
    pre = '[D %s\\\\' % v['source_d_prefix']
    hits = [e for e in kept if e['text'].startswith(pre)]
    if not hits:
        rep['warn'].append('%s: no [D %s\\\\...] header line' % (name, v['source_d_prefix']))
    for e in hits:
        rest = e['text'][len(pre):]
        if header is not None:
            rest = header + ']'
        e['text'] = '[D %s\\\\%s' % (v['d_prefix'], rest)
    foot_old = ']], "%s")' % v['source_group']
    foot_new = ']], "%s")' % v['group']
    fh = [e for e in kept if e['text'].rstrip() == foot_old]
    if len(fh) != 1:
        raise BuildError('%s: expected one footer line %s, found %d' % (name, foot_old, len(fh)))
    fh[0]['text'] = fh[0]['text'].replace(foot_old, foot_new)

    # report: flag words and inline gear text on kept source lines
    # whole word, any case, optional plural s/es
    flags = [(w, re.compile(r'(?<![A-Za-z0-9])' + re.escape(w) + r'(?:s|es)?(?![A-Za-z0-9])', re.I)) for w in v.get('flag_words', [])]
    for e in kept:
        if e['kind'] != 'source':
            continue
        t = plain(e['text'])
        hit = [w for w, rx in flags if rx.search(t)]
        if hit:
            rep['flags'].append('%s:%d  [%s]  %s' % (name, e['src'], ', '.join(hit), t[:160]))
        if not e['text'].startswith('[OC]') and INLINE_GEAR.search(e['text']):
            rep['inline_gear'].append('%s:%d  %s' % (name, e['src'], t[:160]))
    return '\n'.join(e['text'] for e in kept)


# ---------------------------------------------------------------- outputs
def toc_text(v, files):
    return ''.join('## %s: %s\n' % (k, val) for k, val in v['toc']['headers']) + ''.join(f + '\n' for f in files)


def prepare_out(out, v):
    if os.path.normpath(out) == os.path.normpath(v['_source']):
        raise BuildError('--out is the source folder %s' % out)
    if os.path.isdir(out):
        existing = os.listdir(out)
        if existing and not os.path.exists(os.path.join(out, v['folder'] + '.toc')):
            raise BuildError('%s exists, is not empty and is not a build of %s (no %s.toc) - refusing to write into it'
                             % (out, v['name'], v['folder']))
        for f in existing:   # a previous build of this variant: clear its chapters and TOCs (stale files)
            if f.endswith('.lua') or f.endswith('.toc'):
                os.remove(os.path.join(out, f))
    os.makedirs(out, exist_ok=True)


def build(v, out, passthrough=False, report=None):
    rep = {k: [] for k in ('warn', 'drops', 'strips', 'overlay', 'gear_placed', 'gear_unplaced', 'gear_unstated',
                           'gear_skipped', 'gear_nongear', 'flags', 'inline_gear')}
    gear, gear_path = (None, None) if passthrough else load_gear(v)
    if not passthrough and gear is None:
        rep['warn'].append('no generated gear file %s (run gear_calls.py --emit) - no gear lines inserted' % os.path.relpath(gear_path, BASE))
    if gear is not None and gear.get('variant') not in (None, v['name']):
        raise BuildError('%s was emitted for variant %s, not %s' % (gear_path, gear.get('variant'), v['name']))
    texts = []
    for c in chapter_list(v):
        if c['source']:
            if not os.path.exists(c['source']):
                raise BuildError('source chapter %s missing' % c['source'])
            texts.append((c['file'], build_chapter(v, c, gear, rep, passthrough)))
        else:
            if not os.path.exists(c['hand']):
                rep['warn'].append('hand-written chapter %s missing (expected %s) - left out of the build and the TOC'
                                   % (c['key'], os.path.relpath(c['hand'], BASE)))
                continue
            texts.append((c['file'], open(c['hand'], encoding='utf-8', newline='').read()))
    for fn, t in texts:
        if any(ord(ch) > 127 for ch in t):
            raise BuildError('%s: non-ASCII text in the output' % fn)
        if '\r' in t:
            raise BuildError('%s: CR line endings in the output' % fn)
    prepare_out(out, v)
    for fn, t in texts:
        with open(os.path.join(out, fn), 'w', encoding='ascii', newline='') as f:
            f.write(t)
    files = [fn for fn, _ in texts]
    toc = toc_text(v, files)
    tocs = v.get('toc_files') or [v['folder'] + '.toc', v['folder'] + '_Forever.toc']
    for tn in tocs:
        with open(os.path.join(out, tn), 'w', encoding='ascii', newline='') as f:
            f.write(toc)
    zpath = os.path.normpath(out) + '.zip'
    with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
        for fn in files + tocs:
            z.write(os.path.join(out, fn), v['folder'] + '/' + fn)
    # report
    L = ['Build report - variant %s%s' % (v['name'], ' (passthrough)' if passthrough else ''),
         'out: %s' % out, 'zip: %s' % zpath, 'chapters written: %d (%s)' % (len(files), ' '.join(f.split('_')[0] for f in files)),
         'profile: %s; generated gear: %s' % (profile_name(v), os.path.relpath(gear_path, BASE) if gear_path else '-'), '']
    sec = [('warn', 'Warnings'), ('drops', 'Dropped lines (tagged only for other classes/races)'),
           ('strips', 'Stripped untagged [OC] Gear/Loot lines'), ('overlay', 'Overlay operations'),
           ('gear_placed', 'Generated gear lines placed'), ('gear_unplaced', 'Generated gear lines NOT placed'),
           ('gear_unstated', 'Unstated picks (missing tooltips; no line written)'), ('gear_skipped', 'Gear skipped by gear_skip_quests'),
           ('gear_nongear', 'Non-gear rewards only (bag/potion/food; no line written - word it in the overlay)'),
           ('inline_gear', 'Inline gear text on step lines (needs overlay)'),
           ('flags', 'Needs overlay (kept source lines with a flag word: %s)' % ', '.join(v.get('flag_words', [])))]
    for k, title in sec:
        L += ['== %s: %d ==' % (title, len(rep[k]))] + ['  ' + x for x in rep[k]] + ['']
    rp = report or (os.path.normpath(out) + '_build_report.txt')
    with open(rp, 'w', encoding='ascii', errors='replace', newline='\n') as f:
        f.write('\n'.join(L))
    return rep, files, zpath, rp


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('variant', help='tooling/variants/<v>/variant.json')
    ap.add_argument('--passthrough', action='store_true', help='copy the source chapters with every transform off (regression test)')
    ap.add_argument('--out', help='output addon folder (default guide/<folder>)')
    ap.add_argument('--report', help='build report path')
    a = ap.parse_args()
    v = load_variant(a.variant)
    out = os.path.abspath(a.out) if a.out else os.path.join(BASE, 'guide', v['folder'])
    report = a.report or (None if a.out else os.path.join(v['_dir'], 'build_report.txt'))
    try:
        rep, files, zpath, rp = build(v, out, a.passthrough, report)
    except BuildError as e:
        sys.stderr.write('build_variant: %s\nbuild aborted, nothing written\n' % e)
        return 2
    for w in rep['warn']:
        print('WARNING ' + w)
    print('%d chapters -> %s; zip %s; report %s' % (len(files), out, zpath, rp))
    print('dropped %d, stripped %d, overlay ops %d, gear placed %d / not placed %d / unstated %d / non-gear %d, inline gear %d, '
          'needs overlay %d' % tuple(len(rep[k]) for k in ('drops', 'strips', 'overlay', 'gear_placed', 'gear_unplaced',
                                                         'gear_unstated', 'gear_nongear', 'inline_gear', 'flags')))
    return 0


if __name__ == '__main__':
    sys.exit(main())
