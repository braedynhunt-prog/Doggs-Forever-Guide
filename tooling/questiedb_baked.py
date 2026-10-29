#!/usr/bin/env python3
r"""Decode QuestieDB's baked TOC store (QuestieDB_Forever.toc etc.) into luatab.py-style JSON.

The official Questie release (v12.x) ships the Forever database inside QuestieDB\QuestieDB_Forever.toc as
`## X-<Entity>-<id>-<field>: <base64 CBOR>` lines (scalar fields packed in `-S`, each table field on its own line,
long values chunked as `~N~` + `-1..-N` parts, the ID list zlib-compressed). This writes quest/npc/object/item.json
with the same row layout as tooling\qdb\ (row[k-1] = field k of QuestieDB.<entity>Keys), so pool.py, check_guide.py,
loc.py and tugs_diff.py can read it unchanged.

Usage:  python3 tooling\questiedb_baked.py <path to QuestieDB_Forever.toc> <outdir>
"""
import sys, os, re, json, base64, zlib, struct
from collections import defaultdict

FIELDS = {
    'Quest': 36, 'Npc': 15, 'Object': 7, 'Item': 16,
}
# positions whose Lua table is keyed by zone id (keep as dict) rather than positional (list)
ZONE_KEYED = {
    ('Npc', 7, ()), ('Npc', 8, ()), ('Object', 4, ()), ('Object', 7, ()),
    ('Quest', 9, (2,)),            # triggerEnd = {text, {zone = coords}}
}
OUTNAME = {'Quest': 'quest', 'Npc': 'npc', 'Object': 'object', 'Item': 'item'}

class Break(Exception): pass

def cbor(b):
    pos = 0
    def rd(n):
        nonlocal pos
        v = b[pos:pos + n]; pos += n; return v
    def head():
        nonlocal pos
        ib = b[pos]; pos += 1
        mt, ai = ib >> 5, ib & 31
        if ai < 24: val = ai
        elif ai == 24: val = b[pos]; pos += 1
        elif ai == 25: val = struct.unpack('>H', rd(2))[0]
        elif ai == 26: val = struct.unpack('>I', rd(4))[0]
        elif ai == 27: val = struct.unpack('>Q', rd(8))[0]
        elif ai == 31: val = None
        else: raise ValueError(f'bad additional info {ai}')
        return mt, ai, val
    def item():
        mt, ai, val = head()
        if mt == 0: return val
        if mt == 1: return -1 - val
        if mt == 2:
            if val is None:
                out = b''
                while True:
                    try: out += item()
                    except Break: return out
            return bytes(rd(val))
        if mt == 3:
            if val is None:
                out = ''
                while True:
                    try: out += item()
                    except Break: return out
            return rd(val).decode('utf-8', 'replace')
        if mt == 4:
            if val is None:
                out = []
                while True:
                    try: out.append(item())
                    except Break: return out
            return [item() for _ in range(val)]
        if mt == 5:
            out = {}
            if val is None:
                while True:
                    try: k = item()
                    except Break: return out
                    out[k] = item()
            for _ in range(val):
                k = item(); out[k] = item()
            return out
        if mt == 6: return item()          # tag: ignore
        if mt == 7:
            if ai == 20: return False
            if ai == 21: return True
            if ai in (22, 23): return None
            if ai == 25: return struct.unpack('>e', struct.pack('>H', val))[0]
            if ai == 26: return struct.unpack('>f', struct.pack('>I', val))[0]
            if ai == 27: return struct.unpack('>d', struct.pack('>Q', val))[0]
            if ai == 31: raise Break()
            return val
        raise ValueError('bad major type')
    v = item()
    return v

def luaify(v, entity, field, path):
    """Lua tables come back as CBOR arrays or int-keyed maps; make them lists (positional, None for holes)
    unless the position is zone-keyed. Non-int keys stay dicts with string keys."""
    if isinstance(v, list):
        if (entity, field, path) in ZONE_KEYED:   # zone 1..n only -> the encoder emitted an array; keep it zone-keyed
            return {str(i + 1): luaify(x, entity, field, path + (i + 1,)) for i, x in enumerate(v) if x is not None}
        return [luaify(x, entity, field, path + (i + 1,)) for i, x in enumerate(v)]
    if isinstance(v, dict):
        if (entity, field, path) in ZONE_KEYED or not all(isinstance(k, int) for k in v):
            return {str(k): luaify(x, entity, field, path + (k,)) for k, x in v.items()}
        mx = max(v) if v else 0
        if mx > 64 and len(v) < mx / 4:   # sparse int keys = an id-keyed map, not a sequence with holes
            return {str(k): luaify(x, entity, field, path + (k,)) for k, x in v.items()}
        out = [None] * mx
        for k, x in v.items():
            if k >= 1: out[k - 1] = luaify(x, entity, field, path + (k,))
        return out
    if isinstance(v, bytes): return v.decode('utf-8', 'replace')   # Lua strings are emitted as CBOR byte strings
    if isinstance(v, float) and v.is_integer() and abs(v) < 1e15: return int(v)
    return v

def main(toc, outdir):
    os.makedirs(outdir, exist_ok=True)
    raw = {}       # key -> value (base64 or ~N~)
    parts = defaultdict(dict)
    for line in open(toc, encoding='utf-8', errors='replace'):
        if not line.startswith('## X-'): continue
        key, _, val = line[3:].partition(':')
        key = key.strip(); val = val.strip()
        m = re.match(r'^(X-(?:Quest|Npc|Object|Item)-(?:IDS|\d+-(?:S|\d+)))-(\d+)$', key)
        if m: parts[m.group(1)][int(m.group(2))] = val
        else: raw[key] = val
    def stored(key):
        v = raw.get(key)
        if v is None: return None
        m = re.match(r'^~(\d+)~$', v)
        if m:
            n = int(m.group(1)); p = parts.get(key, {})
            if len(p) != n: raise SystemExit(f'{key}: {n} parts declared, {len(p)} found')
            v = ''.join(p[i] for i in range(1, n + 1))
        return v
    stats = {}
    for entity, nfields in FIELDS.items():
        prefix = f'X-{entity}-'
        ids = cbor(zlib.decompress(base64.b64decode(stored(prefix + 'IDS'))))
        rows = {}
        missing_scalar = 0
        for qid in ids:
            s = stored(f'{prefix}{qid}-S')
            if s is None: missing_scalar += 1; continue
            srow = cbor(base64.b64decode(s))
            if isinstance(srow, list): srow = {i + 1: v for i, v in enumerate(srow)}   # a dense row is emitted as an array
            row = [None] * nfields
            for k, v in srow.items():
                if isinstance(k, int) and 1 <= k <= nfields: row[k - 1] = luaify(v, entity, k, ())
            pres = srow.get('p', 0) or 0
            for k in range(1, nfields + 1):
                t = stored(f'{prefix}{qid}-{k}')
                if t is None: continue
                row[k - 1] = luaify(cbor(base64.b64decode(t)), entity, k, ())
            rows[str(qid)] = row
        fn = os.path.join(outdir, OUTNAME[entity] + '.json')
        json.dump(rows, open(fn, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
        stats[entity] = (len(ids), len(rows), missing_scalar)
        print(f'{entity}: {len(ids)} ids, {len(rows)} rows written, {missing_scalar} without scalar row -> {fn}')
    flavor = raw.get('X-Flavor'); ver = None
    for line in open(toc, encoding='utf-8', errors='replace'):
        if line.startswith('## Version:'): ver = line.split(':', 1)[1].strip(); break
    json.dump({'source': os.path.basename(toc), 'flavor': flavor, 'version': ver, 'contract': raw.get('X-Contract-Version'),
               'build_commit': raw.get('X-BUILD-COMMIT'), 'build_time': raw.get('X-BUILD-TIME'), 'counts': stats},
              open(os.path.join(outdir, 'META.json'), 'w'), indent=1)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
