#!/usr/bin/env python3
r"""Forever item tooltips (one line each) from nether.wowhead.com, cached in tooling\item_tips.json.
python3 tooling\tip.py 3567 2562 ..."""
import sys, os, json, re, html, urllib.request
BASE = os.environ.get('FOREVER_ATLAS', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
CACHE = os.path.join(BASE, 'tooling', 'item_tips.json')
tips = json.load(open(CACHE, encoding='utf-8')) if os.path.exists(CACHE) else {}
for a in sys.argv[1:]:
    if a not in tips:
        try:
            req = urllib.request.Request(f'https://nether.wowhead.com/forever/tooltip/item/{a}', headers={'User-Agent': 'Mozilla/5.0'})
            d = json.load(urllib.request.urlopen(req, timeout=20))
            t = re.sub(r'<br\s*/?>', ' | ', d.get('tooltip', '')); t = re.sub(r'<[^>]+>', '', t); t = html.unescape(re.sub(r'\s+', ' ', t))
            t = re.sub(r'Sell Price:.*$', '', t).replace('Binds when picked up', 'BoP ').replace('Binds when equipped', 'BoE ')
            tips[a] = {'name': d.get('name'), 'quality': d.get('quality'), 'tip': t.strip()}
        except Exception as e:
            tips[a] = {'name': None, 'tip': f'ERROR {e}'}
    print(a, '|', tips[a]['tip'][:300])
json.dump(tips, open(CACHE, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
