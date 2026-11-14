"""Make generated pages portable across file URLs and hosting subdirectories."""
import json
import posixpath
import re
from urllib.parse import urlsplit, urlunsplit


def relative_url(value, page):
    if not value.startswith('/') or value.startswith('//'):
        return value
    parts = urlsplit(value)
    target = parts.path.lstrip('/')
    if not target or target.endswith('/'):
        target += 'index.html'
    relative = posixpath.relpath(target, posixpath.dirname(page) or '.')
    return urlunsplit(('', '', relative, parts.query, parts.fragment))


def make_portable(directory):
    for path in directory.rglob('*.html'):
        page = path.relative_to(directory).as_posix()
        text = path.read_text(encoding='utf-8')
        text = re.sub(
            r'\b(href|src|action)=("|\')([^"\']*)\2',
            lambda m: f'{m[1]}={m[2]}{relative_url(m[3], page)}{m[2]}', text)
        text = re.sub(r'(content="0;url=)([^"\s]+)',
                      lambda m: m[1] + relative_url(m[2], page), text)

        def search_index(match):
            records = json.loads(match[2])
            for record in records:
                record['url'] = relative_url(record['url'], page)
            return match[1] + json.dumps(records, ensure_ascii=False).replace('</', '<\\/') + match[3]

        text = re.sub(r'(<script type="application/json" id="search-index">)(.*?)(</script>)',
                      search_index, text, flags=re.S)
        path.write_text(text, encoding='utf-8')
