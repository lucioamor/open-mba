# OpenMBA

**An open management curriculum for Brazilian learners, with individual learning paths.**

OpenMBA brings together business fundamentals, case studies, exercises, oral defense and competency-based learning plans. The learning material is written in **Brazilian Portuguese**. This README is the English entry point for international readers and contributors.

Created by [Lucio Amorim](https://lucioamorim.ai/) · [LinkedIn](https://www.linkedin.com/in/lucioamorim/)

**[Start learning — in Portuguese](START-HERE.md)** · [Available curriculum](CURRICULUM.md) · [Diagnostic](diagnostic/README.md) · [Learning paths](tracks/README.md) · [Contribute](CONTRIBUTING.md)

## Who it is for

Brazilian professionals, founders, technical builders and managers who want to understand how businesses work and make better decisions. Your objective determines relevance; demonstrated competence determines depth. Job titles and years of experience do not automatically exempt you from a subject.

Brazil is the program's operating context, not a translation setting. Examples use Brazilian business situations and BRL where appropriate. Local governance, regulation, employment, taxation and market-entry topics require Brazilian sources and context. International examples are used for comparison, with explicit limits on what transfers. See the [language and Brazil-context policy](docs/BRASIL-E-IDIOMA.md).

## What is available

- **Four introductory workshops:** business fundamentals, customer discovery, growth/distribution, and product/data/experimentation.
- **Eight advanced modules:** finance, unit economics, strategy, operations, people, market entry, governance/risk, and executive communication.
- **33 competencies** and **five starting paths**, with explicit prerequisites.
- Synthetic cases, public-source analyses, exercises, answer keys, templates and two financial workbooks.
- A capstone adapted to the learner's objective and a separate field-practice protocol.
- Optional tutor and decision-partner prompts; no paid AI service is required.

The current edition focuses on technology and AI businesses. A broader general-management foundation is being designed from the earlier curriculum research. The [coverage matrix](docs/CURRICULUM-DESIGN.md) distinguishes existing material, partial coverage and work still to be developed. It is not a completed general MBA curriculum.

## Try it in 30 minutes

Open [F1 — Business fundamentals](foundations/F1-business.md), attempt the case before reading the answer, and write your decision in five lines. Compare it with the rubric, then follow the [getting-started guide](START-HERE.md) to adapt your learning plan.

Prefer audio, voice or a study group? See [study modes](docs/STUDY-MODES.md). All learning instructions are in Portuguese.

## Knowledge, judgment and documented practice

| Dimension | Question | How to develop it |
|---|---|---|
| K — knowledge | Can you calculate and explain? | Lessons, exercises and assessments |
| J — judgment | Can you choose, explain trade-offs and revise a decision? | Cases, memos and oral defense |
| P — documented practice | Have you done this with real responsibility? | Authorized real projects and evidence review |

Simulation can develop K and J. It does not establish P. OpenMBA does not award an academic degree, professional certification or equivalence to an accredited MBA.

## Status and limitations

**Initial public edition, October 29, 2026.** The advanced material was adapted from a personal study program; the four introductory workshops are shorter and less developed. The curriculum, assessment thresholds and time estimates have not been externally validated.

Inherited references are marked as pending review for this public edition. AI-generated scores are provisional and cannot authorize an exemption in the planner. See [sources and limitations](SOURCES.md), [provenance](docs/MIGRATION.md) and [development priorities](ROADMAP.md).

## Local use

You can read the material in a browser. The optional planner and checks use Python 3.11+ with no external dependencies:

```sh
python scripts/plan.py --profile examples/technical-builder.json
python scripts/validate.py
python -m unittest discover -s tests
python scripts/build.py
```

The planner writes a Portuguese plan to the terminal. Use `--output learner/plan.md` to save a private plan. `learner/` is ignored by Git; inspect your files before publishing anything. Technical filenames and identifiers remain stable across language revisions.

## License

Original material, original adaptations and code are available under [Apache-2.0](LICENSE). External sources, trademarks and referenced materials retain their own rights. No affiliation or endorsement is implied. See [SOURCES.md](SOURCES.md).

## Authorship and maintenance

This project was created by [Lucio Amorim](https://lucioamorim.ai/). You can also find him on [LinkedIn](https://www.linkedin.com/in/lucioamorim/).

When reusing, redistributing, or citing this work, keep the attribution credits and include a link to this repository.
