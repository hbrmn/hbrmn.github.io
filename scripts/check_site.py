"""Validate preserved routes and core integrations after the Jekyll build."""
import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

root = Path(sys.argv[1])
expected = json.loads(Path('scripts/site-routes.json').read_text())

def resolve(path):
    path = unquote(path).lstrip('/')
    candidates = [root / path, root / path / 'index.html', root / (path + '.html')]
    return next((p for p in candidates if p.is_file()), None)

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ('img', 'script') and attrs.get('src'):
            self.urls.append(attrs['src'])
        if tag == 'link' and attrs.get('rel') in ('stylesheet', 'icon'):
            self.urls.append(attrs.get('href', ''))

failures = []
for route in expected:
    page = resolve(route)
    if page is None:
        failures.append('Missing page: ' + route)
        continue
    html = page.read_text()
    parser = Links()
    parser.feed(html)
    for url in parser.urls:
        parsed = urlsplit(url)
        if parsed.netloc not in ('', 'hbrmn.github.io'):
            continue
        if parsed.path.startswith('/') and resolve(parsed.path) is None:
            failures.append(route + ': missing asset ' + parsed.path)

home = resolve('/').read_text()
for required in ['henrik[at]usp.br', 'mailto:henrik@usp.br', '/images/profile.png', '/assets/css/fontawesome.css']:
    if required not in home:
        failures.append('Missing home integration: ' + required)
if 'Recommended citation:' in resolve('/publications/').read_text():
    failures.append('Publication index repeats full citations')
article = resolve('/publication/2021-09-15-FLP-RESPDOR').read_text()
if article.count('<h2>Citation</h2>') != 1:
    failures.append('Publication detail must have one citation section')
for route in ['/posts/2021/08/2021-06-28-ssnake-howto-processing/', '/posts/2021/08/2023-04-11-ssnake-howto-fit/', '/posts/2026/09/ssnake-czjzek-fitting/']:
    html = resolve(route).read_text()
    if 'MathJax.Hub.Config' not in html or 'mathjax/2.7.4/' not in html:
        failures.append('Missing equation renderer: ' + route)
if failures:
    raise SystemExit('\n'.join(sorted(set(failures))))
print(f'Validated {len(expected)} routes, local assets, contact links, publication layout and tutorial mathematics.')
