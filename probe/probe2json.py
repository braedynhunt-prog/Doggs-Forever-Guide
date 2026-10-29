#!/usr/bin/env python3
"""DoggsProbe SavedVariables -> JSON (+ a quick summary).

    python3 probe2json.py "<path to WTF\\Account\\<acct>\\SavedVariables\\DoggsProbe.lua>" [out.json]

Uses the table parser from ..\\tooling\\luatab.py (same folder layout as WoW Forever Atlas);
falls back to a copy of that class if luatab.py is not found.
Prints, per character: snapshots, regen buckets with mana/s, Rockbiter AP deltas, watched
spells with their readings, item / quest / vendor counts and the combat sampling mode.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'tooling'))
try:
    from luatab import P
except ImportError:
    # ---- inline copy of luatab.P (Questie-style Lua table parser) ----
    class P:
        def __init__(self, s):
            self.s = s; self.i = 0; self.n = len(s)
        def ws(self):
            s = self.s; n = self.n
            while self.i < n:
                c = s[self.i]
                if c in ' \t\r\n': self.i += 1
                elif s.startswith('--', self.i):
                    if s.startswith('--[[', self.i):
                        j = s.find(']]', self.i + 4); self.i = n if j < 0 else j + 2
                    else:
                        j = s.find('\n', self.i); self.i = n if j < 0 else j + 1
                else: break
        def value(self):
            self.ws()
            s = self.s; c = s[self.i]
            if c == '{': return self.table()
            if c == '"' or c == "'": return self.string(c)
            if s.startswith('[[', self.i):
                j = s.find(']]', self.i + 2); v = s[self.i + 2:j]; self.i = j + 2; return v
            m = re.compile(r'-?\d+\.?\d*(?:[eE][-+]?\d+)?').match(s, self.i)
            if m:
                self.i = m.end(); t = m.group()
                return float(t) if ('.' in t or 'e' in t or 'E' in t) else int(t)
            m = re.compile(r'[A-Za-z_][A-Za-z0-9_]*').match(s, self.i)
            if m:
                self.i = m.end(); w = m.group()
                if w == 'nil': return None
                if w == 'true': return True
                if w == 'false': return False
                return ('IDENT', w)
            raise ValueError(f'unexpected char {c!r} at {self.i}: {s[self.i:self.i+40]!r}')
        def string(self, q):
            s = self.s; i = self.i + 1; out = []
            while True:
                c = s[i]
                if c == '\\':
                    d = s[i + 1]
                    out.append({'n': '\n', 't': '\t', 'r': '\r', '"': '"', "'": "'", '\\': '\\'}.get(d, d)); i += 2
                elif c == q:
                    i += 1; break
                else:
                    out.append(c); i += 1
            self.i = i
            return ''.join(out)
        def table(self):
            assert self.s[self.i] == '{'; self.i += 1
            pos = []; keyed = {}
            while True:
                self.ws()
                c = self.s[self.i]
                if c == '}': self.i += 1; break
                if c == ',' or c == ';': self.i += 1; continue
                if c == '[':
                    self.i += 1; k = self.value(); self.ws()
                    assert self.s[self.i] == ']'; self.i += 1; self.ws()
                    assert self.s[self.i] == '='; self.i += 1
                    keyed[k] = self.value(); continue
                m = re.compile(r'([A-Za-z_][A-Za-z0-9_]*)\s*=(?!=)').match(self.s, self.i)
                if m:
                    self.i = m.end(); keyed[m.group(1)] = self.value(); continue
                pos.append(self.value())
            if keyed:
                for idx, v in enumerate(pos, 1): keyed[idx] = v
                return keyed
            return pos


def load(path):
    txt = open(path, encoding='utf-8', errors='replace').read()
    m = re.search(r'DoggsProbeDB\s*=\s*', txt)
    if not m:
        raise SystemExit('no DoggsProbeDB table in ' + path)
    p = P(txt[m.end():])
    return p.value()


def as_list(t):
    """WoW writes arrays as {[1]=..,[2]=..}; the parser returns a dict with int keys."""
    if isinstance(t, list): return t
    if isinstance(t, dict):
        keys = [k for k in t if isinstance(k, int)]
        if keys and len(keys) == len(t):
            return [t[k] for k in sorted(keys)]
    return t


def summary(db):
    out = []
    items = db.get('items') or {}
    for toc, tbl in items.items():
        out.append(f'items (client toc {toc}): {len(tbl)}')
    for key, c in (db.get('chars') or {}).items():
        meta = c.get('meta', {})
        client = meta.get('client', {})
        out.append(f'\n== {key}  {meta.get("race")} {meta.get("class")} on {client.get("version")} (toc {client.get("toc")}), {meta.get("sessions")} session(s)')
        snaps = as_list(c.get('snapshots') or [])
        out.append(f'snapshots: {len(snaps)}')
        for s in snaps[-5:]:
            st = s.get('stats', {})
            def v(k): return (st.get(k) or [None])[0] if isinstance(st.get(k), (list, dict)) else '?'
            ap = as_list(s.get('ap') or [None])[0]
            regen = as_list(s.get('regen') or ['?', '?'])
            exp = as_list(s.get('expertise') or ['?'])[0]
            imb = s.get('imbue') or {}
            out.append(f'  L{s.get("lvl")} {s.get("reason")}: Str {as_list(st.get("str", [0]))[0]} Agi {as_list(st.get("agi", [0]))[0]} Sta {as_list(st.get("sta", [0]))[0]} '
                       f'Int {as_list(st.get("int", [0]))[0]} Spi {as_list(st.get("spi", [0]))[0]} | AP {ap} | crit {s.get("crit")} | regen {regen[0]}/{regen[1]} | '
                       f'SP nat {(s.get("sp") or {}).get("nature")} | exp {exp} | imbue {imb.get("mh")} id {imb.get("mhID")}')
        rb = as_list(c.get('rockbiter') or [])
        out.append(f'imbue changes: {len(rb)}')
        for r in rb:
            b, a = r.get('before', {}), r.get('after', {})
            out.append(f'  L{r.get("lvl")}: imbue {b.get("mh")}/{b.get("mhID")} -> {a.get("mh")}/{a.get("mhID")}  AP {b.get("ap")} -> {a.get("ap")} (delta {r.get("delta")})  Str {b.get("str")}->{a.get("str")} Int {b.get("int")}->{a.get("int")}')
        buckets = (c.get('regen') or {}).get('buckets') or {}
        out.append(f'regen buckets: {len(buckets)}  (raw samples kept: {len(as_list((c.get("regen") or {}).get("raw") or []))})')
        for k in sorted(buckets):
            b = buckets[k]
            mps = b['mana'] / b['manaSec'] if b.get('manaSec') else 0
            hps = b['hp'] / b['hpSec'] if b.get('hpSec') else 0
            out.append(f'  {k:<28} mana {b.get("manaSec", 0):6.0f} s -> {mps:6.2f}/s ({mps*5:5.1f} per 5 s)   hp {hps:5.2f}/s   [{b.get("n")} samples]')
        spells = c.get('spells') or {}
        out.append(f'watched spells: {len(spells)}')
        for name in sorted(spells):
            rec = spells[name]
            readings = as_list(rec.get('readings') or [])
            lat = rec.get('latest') or {}
            out.append(f'  {name} R{rec.get("rank")} (id {rec.get("id")}): {len(readings)} reading(s); latest mana {lat.get("mana")} SP nat {lat.get("spNature")} heal {lat.get("heal")}: {str(lat.get("desc"))[:110]}')
        out.append(f'quests: {len(c.get("quests") or {})}   vendors: {len(c.get("vendors") or {})}   loot sources: {len(c.get("loot") or {})}   spellbook entries: {len(c.get("spellbook") or {})}')
        cb = c.get('combat') or {}
        out.append(f'combat: mode {cb.get("mode")} events {cb.get("events")} errors {cb.get("errors")} blocked {cb.get("blocked")}')
        for k in sorted(cb.get('swing') or {}):
            b = cb['swing'][k]
            avg = b['dmg'] / b['dmgN'] if b.get('dmgN') else 0
            out.append(f'  swings vs {k}: {b.get("swings")} swings, {b.get("hits")} hits, {b.get("crits")} crit, {b.get("glances")} glance, miss {b.get("miss")}, avg {avg:.1f}')
    errs = as_list(db.get('errors') or [])
    out.append(f'\nerrors logged: {len(errs)}')
    for e in errs[-5:]:
        out.append(f'  {e.get("where")}: {e.get("msg")}')
    return '\n'.join(out)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    src = sys.argv[1]
    db = load(src)
    dst = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(os.path.basename(src))[0] + '.json'
    json.dump(db, open(dst, 'w'), indent=1, default=str)
    print(summary(db))
    print(f'\nwrote {dst}')
