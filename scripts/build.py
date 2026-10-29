"""Generate portable study volumes without evaluator answers. No dependencies."""
from pathlib import Path
import json
from hashlib import sha256

ROOT = Path(__file__).resolve().parents[1]


def main():
    catalog = json.loads((ROOT / 'curriculum/modules.json').read_text(encoding='utf-8'))
    student, evaluator = ['# OpenMBA — volume de estudo\n'], ['# OpenMBA — correção após a tentativa\n']
    for row in catalog['modules']:
        path = ROOT / row['path']
        if row['id'].startswith('F'):
            text = path.read_text(encoding='utf-8')
            before, marker, after = text.partition('## Resposta e rubrica')
            student.append(before)
            evaluator.append(f"# {row['id']}\n\n{marker}{after}")
        else:
            for name in ('module.md', 'cases.md', 'workbook.md'):
                student.append((path.parent / name).read_text(encoding='utf-8'))
            evaluator.append((path.parent / 'answer-key.md').read_text(encoding='utf-8'))
    output = ROOT / 'build'
    output.mkdir(exist_ok=True)
    records = []
    for name, parts in (('STUDENT.md', student), ('EVALUATOR.md', evaluator)):
        # Canonical files remain the navigation source; concatenation is for text import.
        text = ('> Volume gerado para leitura/importação. Links relativos usam como base '
                'o arquivo canônico indicado em CURRICULUM.md, não este volume. '
                'Referências históricas pendentes: consulte SOURCES.md.\n\n' + '\n\n'.join(parts))
        data = text.encode('utf-8')
        (output / name).write_bytes(data)
        records.append({'file': name, 'sha256': sha256(data).hexdigest()})
    (output / 'manifest.json').write_text(json.dumps(records, indent=2) + '\n', encoding='utf-8')
    print('Gerados build/STUDENT.md, build/EVALUATOR.md e manifest.json (ignorados pelo Git).')


if __name__ == '__main__':
    main()
