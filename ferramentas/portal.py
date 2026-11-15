"""Build, validate, preview and package the portable portal using stdlib only."""
import argparse
from datetime import datetime, timezone
from functools import partial
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import subprocess
import shutil
import tempfile
import hashlib
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


def check(directory=DIST):
    pages = list(directory.rglob('*.html'))
    if not pages:
        raise SystemExit('No HTML pages found')
    errors = []
    for page in pages:
        text = page.read_text(encoding='utf-8')
        parser = References()
        parser.feed(text)
        if '\u2014' in text:
            errors.append(f'{page.relative_to(directory)}: forbidden dash')
        for url in parser.urls:
            parts = urlsplit(url)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            if parts.path.startswith('/'):
                errors.append(f'{page.relative_to(directory)}: absolute internal path {url}')
                continue
            target = (page.parent / unquote(parts.path)).resolve()
            if not target.is_relative_to(directory.resolve()) or not target.exists():
                errors.append(f'{page.relative_to(directory)}: missing target {url}')
    for contact in ('pt/contato/index.html', 'en/contact/index.html'):
        text = (directory / contact).read_text(encoding='utf-8')
        if 'mailto:administrativo@ibdcyber.org.br' not in text:
            errors.append(f'{contact}: administrative email absent')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'OK: {len(pages)} HTML files, internal references and bilingual email')


def verify_clean():
    with tempfile.TemporaryDirectory(prefix='ibdcyber-build-') as workspace:
        source = Path(workspace) / 'portal'
        shutil.copytree(PORTAL, source, ignore=shutil.ignore_patterns('dist', '__pycache__'))
        subprocess.run([sys.executable, str(source / 'build.py')], cwd=source, check=True)
        generated = source / 'dist'
        check(generated)
        def digest_tree(directory):
            return {p.relative_to(directory).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in directory.rglob('*') if p.is_file()}
        if digest_tree(generated) != digest_tree(DIST):
            raise SystemExit('Clean build differs from portal/dist. Rebuild and review output.')
        print('OK: clean build reproduces every output file without existing dist')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('build', 'check', 'verify-clean', 'serve', 'package'))
    parser.add_argument('--port', type=int, default=4173)
    parser.add_argument('--host', default='127.0.0.1')
    args = parser.parse_args()
    if args.action == 'build':
        subprocess.run([sys.executable, str(PORTAL / 'build.py')], cwd=PORTAL, check=True)
        check()
    elif args.action == 'check':
        check()
    elif args.action == 'verify-clean':
        verify_clean()
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
