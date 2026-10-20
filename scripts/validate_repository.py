#!/usr/bin/env python3
"""Offline reading-guide integrity checks. Does not validate research claims."""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []
counts = dict(files=0, local_links=0, external_links=0, claims=0)
required = ['README.md','AGENTS.md','LLMS.txt','ATTRIBUTION.md','LICENSE',
            'CONTRIBUTING.md','CITATION.cff','VERIFICATION.md','references/paper.bib',
            'metadata/paper.json','metadata/claims.json','metadata/sources.json',
            'docs/01-concepts-and-context.md','docs/02-framework-and-architecture.md',
            'docs/03-patterns-and-pipeline.md','docs/04-evidence-and-limitations.md',
            'docs/05-paper-map.md','docs/06-discussion-and-design.md']

def check(condition, message):
    if not condition:
        errors.append(message)

def unfenced(text):
    output, inside = [], False
    for line in text.splitlines():
        if re.match(r'^\s*(```|~~~)', line):
            inside = not inside
        elif not inside:
            output.append(line)
    return '\n'.join(output)

def anchors(text):
    result, duplicates = set(), {}
    for line in unfenced(text).splitlines():
        match = re.match(r'^#{1,6}\s+(.+?)\s*#*\s*$', line)
        if match:
            title = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', match[1]).lower()
            title = re.sub(r'<[^>]+>', '', title)
            slug = ''.join(c for c in title if c.isalnum() or c in '_- ').replace(' ', '-')
            occurrence = duplicates.get(slug, 0)
            duplicates[slug] = occurrence + 1
            result.add(slug if occurrence == 0 else f'{slug}-{occurrence}')
    return result

def inspect_link(url, file):
    parsed = urlsplit(url)
    if parsed.scheme:
        counts['external_links'] += 1
        check(parsed.scheme in {'https','http','mailto'}, f'{file.name}: invalid scheme: {url}')
        return
    counts['local_links'] += 1
    target = (file.parent / unquote(parsed.path)).resolve() if parsed.path else file
    check(target.is_relative_to(ROOT), f'{file.name}: link escapes repository: {url}')
    check(target.is_file(), f'{file.name}: missing target: {url}')
    if target.is_file() and parsed.fragment:
        check(unquote(parsed.fragment) in anchors(target.read_text(encoding='utf-8')),
              f'{file.name}: missing anchor: {url}')

for name in required:
    check((ROOT / name).is_file(), f'Missing required file: {name}')
for file in ROOT.rglob('*'):
    if not file.is_file() or '.git' in file.parts or '__pycache__' in file.parts:
        continue
    counts['files'] += 1
    check(file.suffix.lower() not in {'.pdf','.png','.jpg','.jpeg'}, f'Unexpected source/figure asset: {file.name}')
    try:
        content = file.read_text(encoding='utf-8')
    except UnicodeError:
        errors.append(f'{file.name}: invalid UTF-8')
        continue
    check('\ufffd' not in content, f'{file.name}: replacement character')
    check(not any(ord(c)<32 and c not in '\n\r\t' for c in content), f'{file.name}: control character')
    if file.suffix == '.md' or file.name == 'LLMS.txt':
        fences = sum(bool(re.match(r'^\s*(```|~~~)', line)) for line in content.splitlines())
        check(fences % 2 == 0, f'{file.name}: unclosed code fence')
        for url in re.findall(r'(?<!!)\[[^\]]+\]\(([^)\s]+)\)', unfenced(content)):
            inspect_link(url, file)

try:
    paper = json.loads((ROOT/'metadata/paper.json').read_text(encoding='utf-8'))
    claims = json.loads((ROOT/'metadata/claims.json').read_text(encoding='utf-8'))
    sources = json.loads((ROOT/'metadata/sources.json').read_text(encoding='utf-8'))
    for name, data in [('paper',paper),('claims',claims),('sources',sources)]:
        check(data['schema_version']=='1.0.0', f'{name}: unsupported schema')
    check([a['name'] for a in paper['authors']]==['Asif Gill'], 'Author mismatch')
    check(paper['doi']=='10.36227/techrxiv.173153092.25969269/v1', 'DOI/version mismatch')
    check(paper['version']=='v1' and paper['page_count']==16, 'Version/page count mismatch')
    check(paper['posted_date']=='2024-11-13' and paper['manuscript_header_date']=='2024-11-16', 'Date discrepancy lost')
    check(paper['appendices']==[], 'No appendices in studied source')
    check(paper['evidence']['original_empirical_evaluation'] is False, 'Wrong evidence type')
    check(paper['evidence']['empirical_results']==[] and claims['empirical_results']==[], 'Invented empirical results')
    check(paper['companion']['experiments_run'] is False and paper['companion']['implementation_reproduced'] is False, 'Scope mismatch')
    check(paper['provenance']['source_substitution'] is False, 'Actual attachment is primary source')
    check(paper['provenance']['binary_sha256'] is None and paper['provenance']['attachment_binary_equality_verified'] is False, 'Unsupported binary provenance')
    check(paper['license']['spdx']=='CC-BY-4.0', 'License mismatch')
    source_ids=[s['id'] for s in sources['sources']]
    check(len(source_ids)==len(set(source_ids)), 'Duplicate source IDs')
    check(claims['source_id'] in source_ids, 'Missing primary source')
    check(claims['paper_version']=='techrxiv.173153092.25969269/v1', 'Claim version mismatch')
    ids = [c['id'] for c in claims['claims']]
    check(len(ids)==len(set(ids)), 'Duplicate claim IDs')
    counts['claims']=len(ids)
    for claim in claims['claims']:
        check(claim['kind'] in claims['claim_types'], f'{claim["id"]}: invalid claim kind')
        check(bool(claim['qualification']) and bool(claim['sources']), f'{claim["id"]}: missing scope/source')
        check(claim['pages']==[s['pdf_page'] for s in claim['sources']], f'{claim["id"]}: page mismatch')
        for source in claim['sources']:
            check(source['source_id'] in source_ids, f'{claim["id"]}: unknown source ID')
            check(1<=source['pdf_page']<=16, f'{claim["id"]}: invalid page')
            check(source['url']==paper['links']['version_doi'], f'{claim["id"]}: source version mismatch')
    cff=(ROOT/'CITATION.cff').read_text(encoding='utf-8')
    bib=(ROOT/'references/paper.bib').read_text(encoding='utf-8')
    check('cff-version: 1.2.0' in cff and 'preferred-citation:' in cff, 'CFF structure missing')
    for text in [cff,bib]:
        check(paper['title'] in text and paper['doi'] in text, 'Citation title/DOI mismatch')
    check('given-names: "Asif"' in cff and 'family-names: "Gill"' in cff and 'Gill, Asif' in bib, 'Citation author mismatch')
except (KeyError, ValueError, OSError) as exc:
    errors.append(f'Metadata integrity: {exc}')

if errors:
    print('\n'.join('ERROR: '+error for error in errors))
    sys.exit(1)
print('PASS: '+', '.join(f'{key}={value}' for key,value in counts.items()))
print('Scope: documentation, local links/anchors, source/claim/citation consistency. Not research validation or external reachability.')
