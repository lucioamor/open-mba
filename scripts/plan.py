"""Gerador local de plano de aprendizagem, com regras explícitas e biblioteca padrão."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY_VERSION = '0.1'
ROUTES = ('SKIP', 'COMPRESS', 'STUDY_OR_ASSESS', 'DEEP')
PROOF = ('unreviewed', 'absent', 'documented', 'reviewed')


def load_catalog():
    return json.loads((ROOT / 'curriculum/modules.json').read_text(encoding='utf-8'))


def load_competencies():
    return json.loads((ROOT / 'curriculum/competencies.json').read_text(encoding='utf-8'))['competencies']


def validate_profile(profile, catalog=None):
    catalog = catalog or load_catalog()
    if not isinstance(profile, dict):
        raise ValueError('O perfil precisa ser um objeto JSON.')
    if profile.get('goal') not in catalog['goals']:
        raise ValueError('Objetivo desconhecido. Consulte tracks/README.md.')
    hours = profile.get('hours_per_week')
    if type(hours) not in (int, float) or not math.isfinite(hours) or hours <= 0:
        raise ValueError('hours_per_week deve ser um número finito maior que zero.')
    assessments = profile.get('assessments', {})
    if not isinstance(assessments, dict):
        raise ValueError('assessments deve ser um objeto por ID de competência.')
    valid_ids = {row['id'] for row in load_competencies()}
    for cid, row in assessments.items():
        if cid not in valid_ids:
            raise ValueError(f'Competência desconhecida: {cid}')
        if not isinstance(row, dict):
            raise ValueError(f'{cid}: avaliação deve ser um objeto.')
        for key in ('k', 'j'):
            score = row.get(key)
            if score is not None and (type(score) not in (int, float) or not math.isfinite(score) or not 0 <= score <= 100):
                raise ValueError(f'{cid}: {key} deve estar entre 0 e 100 ou ser null.')
        if row.get('review_type', 'self') not in ('self', 'ai', 'human'):
            raise ValueError(f'{cid}: review_type inválido.')
        for key in ('fatal_error', 'unassisted'):
            if key in row and type(row[key]) is not bool:
                raise ValueError(f'{cid}: {key} deve ser booleano.')
        cases = row.get('independent_cases', 0)
        if type(cases) is not int or cases < 0:
            raise ValueError(f'{cid}: independent_cases deve ser inteiro não negativo.')
        if row.get('proof', 'unreviewed') not in PROOF:
            raise ValueError(f'{cid}: proof inválido.')
        for key in ('reviewer', 'assessment_ref'):
            if key in row and not isinstance(row[key], str):
                raise ValueError(f'{cid}: {key} deve ser texto.')
    return profile


def competency_route(row):
    """A self-report or AI score cannot authorize compression or exemption."""
    if row.get('fatal_error', False):
        return 'DEEP'
    human = (row.get('review_type') == 'human'
             and bool(row.get('reviewer', '').strip())
             and bool(row.get('assessment_ref', '').strip())
             and row.get('unassisted') is True)
    k, j = row.get('k'), row.get('j')
    if not human or k is None or j is None:
        return 'STUDY_OR_ASSESS'
    if k >= 85 and j >= 80 and row.get('independent_cases', 0) >= 2:
        return 'SKIP'
    if k >= 70 and j >= 70 and row.get('independent_cases', 0) >= 1:
        return 'COMPRESS'
    return 'DEEP'


def selected_modules(goal, catalog):
    modules = {row['id']: row for row in catalog['modules']}
    ordered, active, done = [], set(), set()

    def visit(mid):
        if mid in active:
            raise ValueError(f'Ciclo nos pré-requisitos: {mid}')
        if mid in done:
            return
        if mid not in modules:
            raise ValueError(f'Módulo desconhecido: {mid}')
        active.add(mid)
        for dep in modules[mid]['requires']:
            visit(dep)
        active.remove(mid)
        done.add(mid)
        ordered.append(modules[mid])

    for mid in catalog['goals'][goal]:
        visit(mid)
    return ordered


def make_plan(profile):
    catalog = load_catalog()
    validate_profile(profile, catalog)
    competencies = load_competencies()
    results = profile.get('assessments', {})
    plan = []
    for module in selected_modules(profile['goal'], catalog):
        items = []
        for competency in competencies:
            if competency['owner'] != module['id']:
                continue
            record = results.get(competency['id'], {})
            items.append({**competency, 'route': competency_route(record),
                          'proof': record.get('proof', 'unreviewed')})
        if not items:
            raise ValueError(f"Módulo sem competências: {module['id']}")
        route = max((item['route'] for item in items), key=ROUTES.index)
        factor = 0 if route == 'SKIP' else 0.5 if route == 'COMPRESS' else 1
        plan.append({**module, 'route': route, 'estimated_hours': module['hours'] * factor,
                     'competencies': items})
    return plan


def render_plan(profile, plan):
    total = sum(row['estimated_hours'] for row in plan)
    weeks = math.ceil(total / profile['hours_per_week'])
    lines = ['# Plano privado — OpenMBA', '',
             f"Objetivo: `{profile['goal']}` · política {POLICY_VERSION}", '',
             f"Estimativa de instrução/prática dos módulos: **{total:g} horas**, "
             f"cerca de **{weeks} semanas** a {profile['hours_per_week']:g}h/semana.", '',
             'Estimativa não validada; não inclui diagnóstico, retestes, capstone ou prática de campo. '
             'Não é promessa de conclusão. SKIP dispensa instrução, não aplicação integrada.', '',
             'Siga a ordem dos pré-requisitos. STUDY_OR_ASSESS significa não avaliado: '
             'estude ou apresente uma avaliação, sem inferir incapacidade.', '',
             '| Módulo | Rota agregada | Horas indicativas |',
             '|---|---|---:|']
    for row in plan:
        lines.append(f"| {row['id']} — {row['title']} | {row['route']} | {row['estimated_hours']:g} |")
    lines += ['', '## Resultados por competência', '',
              '| Competência | Rota | Prática declarada no registro |', '|---|---|---|']
    for module in plan:
        for row in module['competencies']:
            lines.append(f"| {row['id']} — {row['name']} | {row['route']} | {row['proof']} |")
    lines += ['', 'P é exibido a partir do registro fornecido e não foi verificado pelo script. '
              'Sem prática revisada, considere um projeto de campo quando houver acesso e autorização. '
              'Essa recomendação é separada da rota de conhecimento.', '',
              'Use CURRICULUM.md no repositório para abrir as lições; '
              'guarde este plano e as evidências em learner/, sem publicar dados pessoais.', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile', required=True, type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    try:
        profile = json.loads(args.profile.read_text(encoding='utf-8'))
        text = render_plan(profile, make_plan(profile))
        if args.output:
            output = args.output.resolve()
            if output == args.profile.resolve():
                raise ValueError('A saída não pode sobrescrever o perfil de entrada.')
            if output.exists():
                raise ValueError('A saída já existe; escolha outro nome para preservar seu histórico.')
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(text, encoding='utf-8', newline='\n')
            print(f'Plano salvo: {output}')
        else:
            print(text)
    except (ValueError, OSError) as exc:
        parser.exit(2, f'Erro: {exc}\n')


if __name__ == '__main__':
    main()
