"""Verifica estrutura, codificação, links locais e contexto privado acidental.

Não atesta precisão factual, liberação de direitos ou eficácia de aprendizagem.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile

from plan import load_catalog, load_competencies, make_plan, selected_modules

ROOT = Path(__file__).resolve().parents[1]
PRIVATE_CONTEXT = re.compile(
    r'mega.curriculo|master.context|NXLV|IesBrazil|Ocyan|Gamma Quant|RioDoceHelp|'
    r'Paul Rios|\bDylan\b|GOAL-FAST|FTMBA-LA|[CH]:[\\/]|lucio-amorim|\bLucio\b',
    re.IGNORECASE,
)
TEXT_EXT = {'.md', '.py', '.json', '.yml', '.yaml', '.csv'}


def main():
    errors = []
    catalog = load_catalog()
    modules = {row['id']: row for row in catalog['modules']}
    competencies = load_competencies()
    if len(modules) != len(catalog['modules']):
        errors.append('Duplicate module ID')
    if len({c['id'] for c in competencies}) != len(competencies):
        errors.append('Duplicate competency ID')
    for competency in competencies:
        if competency['owner'] not in modules:
            errors.append(f"Unknown owner: {competency['id']}")
    for row in modules.values():
        if not (ROOT / row['path']).is_file():
            errors.append(f"Missing canonical lesson: {row['path']}")
        if not any(c['owner'] == row['id'] for c in competencies):
            errors.append(f"No competencies for {row['id']}")
        if row['id'].startswith('M'):
            for name in ('module.md', 'workbook.md', 'cases.md', 'answer-key.md', 'sources.md', 'source-packet.md'):
                if not (ROOT / row['path']).with_name(name).is_file():
                    errors.append(f"Missing {name} for {row['id']}")
        elif '## Resposta e rubrica' not in (ROOT / row['path']).read_text(encoding='utf-8'):
            errors.append(f"No correction section in {row['id']}")
    for goal in catalog['goals']:
        try:
            selected_modules(goal, catalog)
        except ValueError as exc:
            errors.append(str(exc))

    files = [p for p in ROOT.rglob('*') if p.is_file() and not any(
        part in {'.git', '__pycache__', 'build', 'learner', '.venv'} for part in p.relative_to(ROOT).parts)]
    for path in files:
        relative = path.relative_to(ROOT)
        if path.suffix in TEXT_EXT:
            raw = path.read_bytes()
            try:
                text = raw.decode('utf-8')
            except UnicodeDecodeError:
                errors.append(f'Not UTF-8: {relative}')
                continue
            if raw.startswith(b'\xef\xbb\xbf') or '\ufffd' in text:
                errors.append(f'BOM or replacement character: {relative}')
            if path.suffix == '.json':
                try:
                    json.loads(text)
                except ValueError:
                    errors.append(f'Invalid JSON: {relative}')
            if relative.parts[0] in {'modules', 'foundations', 'diagnostic', 'sources', 'curriculum'}:
                checked = re.split(r'## (?:Authorship and maintenance|Autoria e manutenção)', text)[0]
                found = PRIVATE_CONTEXT.search(checked)
                if found:
                    errors.append(f'Private-origin context in {relative}: {found.group()}')
            if path.name == 'README.md' and not any(header in text for header in ('Authorship and maintenance', 'Autoria e manutenção')):
                errors.append(f'Missing authorship in {relative}')
            if path.suffix == '.md':
                for target in re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)', text):
                    target = target.strip().strip('<>')
                    if urlsplit(target).scheme or target.startswith('#'):
                        continue
                    dest = (path.parent / unquote(target.split('#')[0])).resolve()
                    if not dest.is_relative_to(ROOT) or not dest.exists():
                        errors.append(f'Broken local link in {relative}: {target}')
        elif path.suffix == '.xlsx':
            with ZipFile(path) as archive:
                for item in archive.namelist():
                    if 'externalLinks/' in item or item.endswith('vbaProject.bin'):
                        errors.append(f'External link or macro in {relative}')
                    if item.endswith('.xml'):
                        text = archive.read(item).decode('utf-8')
                        if PRIVATE_CONTEXT.search(text):
                            errors.append(f'Private-origin context in {relative}:{item}')
                        if re.search(r'<c\b[^>]*\bt="e"', text):
                            errors.append(f'Cached spreadsheet error in {relative}:{item}')

    for path in sorted((ROOT / 'examples').glob('*.json')):
        try:
            profile = json.loads(path.read_text(encoding='utf-8'))
            if profile.get('example_only') is not True:
                errors.append(f'Example not labeled synthetic: {path.name}')
            make_plan(profile)
        except ValueError as exc:
            errors.append(f'{path.name}: {exc}')
    if errors:
        for error in errors:
            print(f'FAIL {error}')
        return 1
    print(f'PASS: {len(modules)} módulos; {len(competencies)} competências; '
          f'{len(catalog["goals"])} objetivos; {len(files)} arquivos verificados.')
    print('Escopo: estrutura, UTF-8, links locais, padrões de contexto privado, arquivos de planilha e planos de exemplo.')
    print('Precisão de fontes externas, direitos e eficácia educacional continuam sujeitos a revisão humana.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
