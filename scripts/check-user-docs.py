"""Validate public documentation links without reading private development docs."""
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

root = Path(__file__).resolve().parent.parent / 'content'
manifest = json.loads((root / 'docs.json').read_text(encoding='utf-8'))
assert manifest['schemaVersion'] == 1
assert (root / 'index.md').is_file()
assert manifest['defaultLocale'] in manifest['locales']
page_ids = {}
for locale, directory in manifest['locales'].items():
    locale_root = (root / directory).resolve()
    assert locale_root.is_relative_to(root.resolve())
    assert (locale_root / 'index.md').is_file(), f'{locale}: missing index'
    ids = set()
    for page in locale_root.rglob('*.md'):
        text = page.read_text(encoding='utf-8')
        frontmatter = text.split('---', 2)
        assert len(frontmatter) == 3 and not frontmatter[0].strip(), f'{page}: missing frontmatter'
        match = re.search(r'^id:\s*(\S+)\s*$', frontmatter[1], re.M)
        assert match, f'{page}: missing stable id'
        identity = match.group(1)
        assert identity not in ids, f'{locale}: duplicate id {identity}'
        ids.add(identity)
        path = page.relative_to(locale_root).as_posix()
        assert page_ids.setdefault(path, identity) == identity, f'{path}: translation id mismatch'
pages = list(root.rglob('*.md'))
for page in pages:
    text = page.read_text(encoding='utf-8')
    for link in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', text):
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        target = (page.parent / unquote(parsed.path)).resolve()
        if not target.is_relative_to(root.resolve()) or not target.is_file():
            raise ValueError(f'{page.relative_to(root)}: broken local link {link}')
print(f'User documentation: {len(pages)} pages, local links valid')
