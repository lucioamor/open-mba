import copy
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('plan', ROOT / 'scripts/plan.py')
plan = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plan)


def reviewed(**changes):
    row = dict(k=90, j=85, independent_cases=2, unassisted=True,
               fatal_error=False, review_type='human', reviewer='Synthetic reviewer',
               assessment_ref='Synthetic case 1 and case 2', proof='unreviewed')
    return row | changes


class RoutingTests(unittest.TestCase):
    def test_unknown_is_not_a_gap_claim(self):
        self.assertEqual(plan.competency_route({}), 'STUDY_OR_ASSESS')

    def test_ai_and_self_cannot_skip_or_compress(self):
        for kind in ('ai', 'self'):
            self.assertEqual(plan.competency_route(reviewed(review_type=kind)), 'STUDY_OR_ASSESS')

    def test_human_results_can_skip(self):
        self.assertEqual(plan.competency_route(reviewed()), 'SKIP')

    def test_fatal_error_overrides_high_scores(self):
        self.assertEqual(plan.competency_route(reviewed(fatal_error=True)), 'DEEP')

    def test_one_case_does_not_skip(self):
        self.assertEqual(plan.competency_route(reviewed(independent_cases=1)), 'COMPRESS')

    def test_zero_cases_does_not_compress(self):
        self.assertEqual(plan.competency_route(reviewed(independent_cases=0)), 'DEEP')

    def test_no_metadata_or_assistance_does_not_skip(self):
        for changes in ({'reviewer': ''}, {'assessment_ref': ''}, {'unassisted': False}):
            self.assertEqual(plan.competency_route(reviewed(**changes)), 'STUDY_OR_ASSESS')

    def test_boundary_scores(self):
        self.assertEqual(plan.competency_route(reviewed(k=85, j=80)), 'SKIP')
        self.assertEqual(plan.competency_route(reviewed(k=84, j=80)), 'COMPRESS')
        self.assertEqual(plan.competency_route(reviewed(k=70, j=70)), 'COMPRESS')
        self.assertEqual(plan.competency_route(reviewed(k=69, j=90)), 'DEEP')

    def test_proof_does_not_change_instruction(self):
        self.assertEqual(plan.competency_route(reviewed(proof='absent')), 'SKIP')
        self.assertEqual(plan.competency_route({'proof': 'reviewed'}), 'STUDY_OR_ASSESS')

    def test_weak_competency_is_not_hidden_by_average(self):
        rows = {c['id']: reviewed() for c in plan.load_competencies() if c['owner'] == 'M1'}
        rows['FIN-02'] = reviewed(k=20)
        profile = dict(goal='builder', hours_per_week=5, assessments=rows)
        m1 = next(m for m in plan.make_plan(profile) if m['id'] == 'M1')
        self.assertEqual(m1['route'], 'DEEP')
        self.assertEqual(next(c for c in m1['competencies'] if c['id'] == 'FIN-01')['route'], 'SKIP')

    def test_all_goals_include_dependencies_before_dependents(self):
        catalog = plan.load_catalog()
        for goal in catalog['goals']:
            seen = set()
            for row in plan.selected_modules(goal, catalog):
                self.assertTrue(set(row['requires']) <= seen)
                self.assertNotIn(row['id'], seen)
                seen.add(row['id'])

    def test_cycle_detected(self):
        catalog = copy.deepcopy(plan.load_catalog())
        catalog['modules'][0]['requires'] = ['M2']
        with self.assertRaises(ValueError):
            plan.selected_modules('builder', catalog)

    def test_profile_rejects_bad_inputs(self):
        bad = [dict(goal='unknown', hours_per_week=5), dict(goal='builder', hours_per_week=0),
               dict(goal='builder', hours_per_week=True), dict(goal='builder', hours_per_week=float('nan'))]
        for row in bad:
            with self.assertRaises(ValueError):
                plan.validate_profile(row)
        for assessment in ({'k': 101}, {'j': True}, {'fatal_error': 'false'},
                           {'independent_cases': 1.5}, {'review_type': 'verified'}, {'proof': 'P3'}):
            with self.assertRaises(ValueError):
                plan.validate_profile(dict(goal='builder', hours_per_week=5, assessments={'FIN-01': assessment}))

    def test_unknown_competency_rejected(self):
        with self.assertRaises(ValueError):
            plan.make_plan(dict(goal='builder', hours_per_week=5, assessments={'typo': {}}))

    def test_examples_are_valid_and_different(self):
        import json
        outputs = []
        for path in sorted((ROOT / 'examples').glob('*.json')):
            profile = json.loads(path.read_text(encoding='utf-8'))
            result = plan.make_plan(profile)
            outputs.append([(row['id'], row['route']) for row in result])
            self.assertTrue(plan.render_plan(profile, result).startswith('# Plano privado'))
        self.assertEqual(len(outputs), 3)
        self.assertNotEqual(outputs[0], outputs[1])


if __name__ == '__main__':
    unittest.main()
