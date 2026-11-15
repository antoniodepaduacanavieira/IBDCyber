"""Production discovery metadata, without changing portable navigation links."""
import json
import re
from urllib.parse import urljoin
from xml.sax.saxutils import escape


def enhance(directory, root):
    config = json.loads((root / 'source/production.json').read_text(encoding='utf-8'))
    base = config['canonicalBase'].rstrip('/') + '/'
    urls = []
    images = json.loads((root / 'source/images.json').read_text(encoding='utf-8'))
    for page in sorted(directory.rglob('index.html')):
        relative = page.relative_to(directory).as_posix()
        canonical = base + relative
        text = page.read_text(encoding='utf-8')
        def picture(match):
            tag = match[0]
            source = re.search(r'src="([^"]+)"', tag)
            if not source:
                return tag
            name = source[1].split('/')[-1]
            if name not in images:
                return tag
            prefix = source[1].rsplit('/', 1)[0] + '/'
            variants = ', '.join(prefix + v['file'] + ' ' + str(v['width']) + 'w' for v in images[name])
            return '<picture><source type="image/webp" srcset="' + variants + '" sizes="(max-width: 700px) 90vw, 600px">' + tag + '</picture>'
        text = re.sub(r'<img\b[^>]*>', picture, text)
        text = text.replace('</head>', f'<link rel="canonical" href="{canonical}"></head>')
        text = re.sub(r'(<link rel="alternate" hreflang="[^"]+" href=")([^"]+)',
                      lambda m: m[1] + urljoin(canonical, m[2]), text)
        if relative.startswith(('pt/', 'en/')):
            language = 'pt-BR' if relative.startswith('pt/') else 'en'
            text = text.replace('</head>', f'<link rel="alternate" hreflang="{language}" href="{canonical}"></head>')
        page.write_text(text, encoding='utf-8')
        urls.append(canonical)
    (directory / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{escape(url)}</loc></url>' for url in urls) + '</urlset>\n', encoding='utf-8')
    (directory / 'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: ' + base + 'sitemap.xml\n', encoding='utf-8')
