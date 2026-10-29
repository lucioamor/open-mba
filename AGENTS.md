# OpenMBA maintenance

- Public educational repository. Never import private learner data, career context, resumes, client material, or source repository history.
- Keep Portuguese UTF-8 without BOM. Use apply_patch for manual edits.
- Canonical curriculum lives in `curriculum/`; canonical lessons in `foundations/` and `modules/`. `build/` is generated and ignored.
- Do not invent learner results, external verification, adoption metrics, or academic equivalence.
- Routing is per competency; self-reports and AI scores never authorize SKIP. Keep code, diagnostic policy and tests consistent.
- Preserve source attribution. Historical references remain pending until individually checked and logged.
- Run `python scripts/validate.py` and `python -m unittest discover -s tests` before publishing.
- No runtime dependency is required. Read workspace package policy before adding any.
