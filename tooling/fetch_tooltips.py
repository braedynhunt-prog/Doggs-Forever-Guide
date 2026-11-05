#!/usr/bin/env python3
r"""Fetch Forever item tooltips from the nether Wowhead endpoint and cache them as plain text.

Usage (repo root):  python tooling/fetch_tooltips.py 271096 270256 ...
               or:  python tooling/fetch_tooltips.py --from-file ids.txt     (whitespace-separated item ids)

GET https://nether.wowhead.com/forever/tooltip/item/<id> (JSON: "name" + HTML "tooltip"), at most one request per
second, plain "Mozilla/5.0" User-Agent, same as the repo's other tools. A 403/429 (or any HTTP error other than 404,
or a network failure) stops the run: what was fetched so far is saved and the script exits 2.

Output: weights/tooltips/<today YYYY-MM-DD>.json, merged into the file if it already exists. The HTML is turned into
the plain-text shape of weights/item_tooltips.json (dict keyed by item name -> {"id", "tooltip"}) so
weights/score_items.py parse() reads it the same way: <br> and newlines become " | ", every other tag is dropped
without a separator. "Dropped by" / "Drop Chance" lines (nether carries them for single-dropper items) are kept as
extra " | " segments. weights/item_tooltips.json (the 24 Sep 2026 scrape) is never written.
"""
import argparse, datetime, html, json, os, re, sys, time, urllib.request, urllib.error

BASE = os.path.abspath(os.environ.get('FOREVER_ATLAS', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
URL = 'https://nether.wowhead.com/forever/tooltip/item/%d'
UA = 'Mozilla/5.0'
OUT_DIR = os.path.join(BASE, 'weights', 'tooltips')


def to_text(h):
    """Wowhead tooltip HTML -> the plain-text shape used in weights/item_tooltips.json."""
    h = re.sub(r'<!--.*?-->', '', h, flags=re.S)
    h = re.sub(r'<br\s*/?>', ' | ', h)
    h = re.sub(r'<div class="whtt-extra', ' | <div class="whtt-extra', h)   # Dropped by / Drop Chance
    h = h.replace('\n', ' | ')
    h = re.sub(r'<span class="money(gold|silver|copper)">(\d+)</span>', lambda m: m.group(2) + m.group(1)[0], h)   # 5 Nov 2026: keep the unit ("Sell Price: 5s 50c")
    h = re.sub(r'<[^>]+>', '', h)
    return html.unescape(h).replace('\xa0', ' ').strip()


def fetch(item_id):
    """-> (json dict or None for 404). Raises urllib.error.HTTPError / URLError for anything else."""
    req = urllib.request.Request(URL % item_id, headers={'User-Agent': UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode('utf-8-sig'))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('ids', nargs='*', type=int, help='item ids')
    ap.add_argument('--from-file', help='file of whitespace-separated item ids')
    args = ap.parse_args()
    ids = list(args.ids)
    if args.from_file:
        with open(args.from_file, encoding='utf-8') as f:
            ids += [int(x) for x in f.read().split()]
    ids = list(dict.fromkeys(ids))
    if not ids:
        ap.error('no item ids given')

    out = os.path.join(OUT_DIR, datetime.date.today().isoformat() + '.json')
    data = {}
    if os.path.exists(out):
        with open(out, encoding='utf-8') as f:
            data = json.load(f)

    added, missing, stopped = 0, [], None
    last = 0.0
    try:
        for i in ids:
            wait = last + 1.0 - time.time()
            if wait > 0:
                time.sleep(wait)
            last = time.time()
            try:
                j = fetch(i)
            except urllib.error.HTTPError as e:
                stopped = 'HTTP %d on item %d' % (e.code, i)
                break
            except Exception as e:
                stopped = '%s on item %d: %s' % (type(e).__name__, i, e)
                break
            if not j or not j.get('name'):
                missing.append(i)
                print(i, 'no tooltip (404 or empty)')
                continue
            name = j['name']
            if name in data and data[name]['id'] != i:
                name = '%s [%d]' % (name, i)   # two items share a name
            data[name] = {'id': i, 'tooltip': to_text(j.get('tooltip', ''))}
            added += 1
            print(i, name)
    finally:
        if data:
            os.makedirs(OUT_DIR, exist_ok=True)
            with open(out, 'w', encoding='utf-8', newline='\n') as f:
                json.dump(data, f, indent=1, sort_keys=True)
                f.write('\n')
    print('wrote %s: %d items (%d new/updated this run), %d without tooltip' % (out, len(data), added, len(missing)))
    if stopped:
        print('STOPPED: ' + stopped + '. Saved what was fetched; not retrying.')
        raise SystemExit(2)


if __name__ == '__main__':
    main()
