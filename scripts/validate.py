#!/usr/bin/env python3
"""Check deployable documents, links, assets and coverage without dependencies."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json, re, sys
ROOT=Path(__file__).resolve().parents[1]; SITE=ROOT/'site'; errors=[]
class Page(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.ids=set();self.title=False;self.main=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='title':self.title=True
        if tag=='main':self.main=True
        if 'id' in a:
            if a['id'] in self.ids:errors.append('duplicate id '+a['id'])
            self.ids.add(a['id'])
        if tag=='img' and not a.get('alt'):errors.append('image missing alt')
        for attr in ['href','src']:
            if attr in a:self.links.append(a[attr])
parsers={}
for f in SITE.rglob('*.html'):
    p=Page();p.feed(f.read_text());parsers[f.resolve()]=p
    if not p.title or not p.main:errors.append(f'{f}: missing title/main')
for f,p in parsers.items():
    for ref in p.links:
        u=urlsplit(ref)
        if u.scheme or u.netloc:continue
        dest=(f.parent/unquote(u.path)).resolve() if u.path else f
        if dest.is_dir():dest=dest/'index.html'
        if not dest.exists():errors.append(f'{f.relative_to(ROOT)}: broken link {ref}')
        elif u.fragment and dest in parsers and unquote(u.fragment) not in parsers[dest].ids:errors.append(f'{f.relative_to(ROOT)}: missing fragment {ref}')
ids=[p['id'] for p in json.loads((ROOT/'inventory.json').read_text())]
if len(ids)!=20 or len(set(ids))!=20:errors.append('Expected 20 unique project IDs')
for id in ids:
    for name in ['REPORT','ONBOARDING','EVIDENCE','STATUS']:
        if not (ROOT/'reports'/id/(name+'.md')).is_file():errors.append(f'missing {id}/{name}')
    if not (SITE/'assets'/f'{id}-flow.svg').is_file():errors.append(f'missing flow {id}')
for f in list(SITE.rglob('*'))+list((ROOT/'reports').rglob('*.md')):
    if f.is_file() and f.suffix in ['.html','.json','.md','.js','.css']:
        text=f.read_text()
        for pattern in [r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',r'gh[pousr]_[A-Za-z0-9]{30,}',r'github_pat_[A-Za-z0-9_]{50,}',r'sk-proj-[A-Za-z0-9_-]{30,}',r'AIza[A-Za-z0-9_-]{30,}']:
            if re.search(pattern,text):errors.append(f'credential-like content in {f.relative_to(ROOT)}')
        if '/Users/shashanksaxena/' in text:errors.append(f'private absolute path in {f.relative_to(ROOT)}')
if errors:
    print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(parsers)} HTML pages; local links/fragments/assets; 20 complete report folders; image alt text; publication content patterns.')
