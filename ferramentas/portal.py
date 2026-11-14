"""Build, validate, preview and package the portable portal using stdlib only."""
import argparse
from datetime import datetime, timezone
from functools import partial
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import subprocess
import sys
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
PORTAL = ROOT / 'portal'
DIST = PORTAL / 'dist'


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        self.urls.extend(value for key, value in attrs
                         if key in ('href', 'src', 'action') and value)


def check():
    pages = list(DIST.rglob('*.html'))
    if not pages:
        raise SystemExit('No HTML pages found')
    errors = []
    for page in pages:
        text = page.read_text(encoding='utf-8')
        parser = References()
        parser.feed(text)
        if '\u2014' in text:
            errors.append(f'{page.relative_to(DIST)}: forbidden dash')
        for url in parser.urls:
            parts = urlsplit(url)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            if parts.path.startswith('/'):
                errors.append(f'{page.relative_to(DIST)}: absolute internal path {url}')
                continue
            target = (page.parent / unquote(parts.path)).resolve()
            if not target.is_relative_to(DIST.resolve()) or not target.exists():
                errors.append(f'{page.relative_to(DIST)}: missing target {url}')
    for contact in ('pt/contato/index.html', 'en/contact/index.html'):
        text = (DIST / contact).read_text(encoding='utf-8')
        if 'mailto:administrativo@ibdcyber.org.br' not in text:
            errors.append(f'{contact}: administrative email absent')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'OK: {len(pages)} HTML files, internal references and bilingual email')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('build', 'check', 'serve', 'package'))
    parser.add_argument('--port', type=int, default=4173)
    parser.add_argument('--host', default='127.0.0.1')
    args = parser.parse_args()
    if args.action == 'build':
        subprocess.run([sys.executable, str(PORTAL / 'build.py')], cwd=PORTAL, check=True)
        check()
    elif args.action == 'check':
        check()
    elif args.action == 'serve':
        handler = partial(SimpleHTTPRequestHandler, directory=str(DIST))
        with ThreadingHTTPServer((args.host, args.port), handler) as server:
            print(f'Preview: http://{args.host}:{args.port}', flush=True)
            try:
                server.serve_forever()
            except KeyboardInterrupt:
                pass
    else:
        check()
        out = ROOT / 'entregas'
        out.mkdir(exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
        archive = out / f'IBDCyber-portal-{stamp}.zip'
        with ZipFile(archive, 'x', ZIP_DEFLATED) as package:
            for file in sorted(DIST.rglob('*')):
                if file.is_file():
                    package.write(file, file.relative_to(DIST).as_posix())
        with ZipFile(archive) as package:
            if package.testzip() is not None:
                raise SystemExit('ZIP integrity check failed')
        print(archive)


if __name__ == '__main__':
    main()
