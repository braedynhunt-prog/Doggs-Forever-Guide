#!/usr/bin/env python3
"""Parse Questie-style Lua data files (`[id] = {...},` rows) into Python/JSON.
Handles numbers, strings ("..", '..', [[..]]), nil/true/false, nested tables with
positional and keyed entries. Positional tables -> lists (nil kept as None),
keyed tables -> dicts. Mixed tables -> dict with int keys for positional items.
"""
import re, json, sys

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

def parse_rows(path, encoding='utf-8'):
    """Yield (id, row) for each top-level `[id] = {...},` line."""
    txt = open(path, encoding=encoding, errors='replace').read()
    for m in re.finditer(r'^\[(\d+)\] = (\{.*\}),?\s*$', txt, re.M):
        p = P(m.group(2))
        try:
            yield int(m.group(1)), p.value()
        except Exception as e:
            print('parse fail', m.group(1), e, file=sys.stderr)

if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    rows = {k: v for k, v in parse_rows(src)}
    json.dump(rows, open(dst, 'w'))
    print(dst, len(rows), 'rows')
