---
name: math-templates
description: Use when 高教社杯/CUMCM mathematical modeling work needs lightweight reusable paper assets, national-prize style paragraph templates, section controls, per-question code/plot/test scaffolds, evidence registries, paper fragments, reproduction scripts, or safe reuse of prior contest project structure without copying old problem-specific content.
---

# Math Modeling Templates

## Purpose

Provide lightweight reusable assets for 高教社杯/CUMCM-style mathematical modeling papers and support packages. Use the assets to preserve good structure, not to import old conclusions.

Core rule: reuse structure, not old content. Unless the user explicitly says prior contest material is current source evidence, do not copy old problem names, numbers, scenario labels, file paths, figure titles, or conclusions into a new project.

National-first quality gate: `国一候选` is a quality target, not an award promise (`不承诺获奖`). Template use is acceptable only when it helps the current paper show 题目贴合, 建模洞察, 证据可信, 可复现, and 边界清楚. A template sentence, old project scaffold, or chart script cannot replace current evidence.

Language/output boundary: skill reasoning, template selection, schemas, code scaffolds, algorithms, file names, registry statuses, LaTeX commands, English literature terms, and official rule quotations may stay English; 该英文就用英文. Paper-facing deliverables should default to Chinese contest prose: paper body, abstract snippets, copyable paragraph templates, project manifests, and reproduction user messages. Do not sacrifice model judgment, evidence chains, reproducibility, or terminology precision for localization (`不因中文化牺牲`). 

Exact boundary for audits: the skill's internal 判断 may use English; only final 产出 inside paper-facing 交付文件 defaults to Chinese. Keep 算法名, 字段, code identifiers, and 官方规则原文 unchanged when precision would otherwise be lost.

Default to **light asset library mode**. Load or copy only the asset the user needs: style profile, section controls, paragraph phrases, code scaffold, chart template, evidence registry, or reproduction helper. Do not impose a project-management workflow unless the user asks to build or reorganize a full project.

## Asset Root

Reusable project assets live in:

`assets/contest-project-template/`

Use them when the user asks to:

- start a contest project;
- reuse code or paper assets from a prior project;
- create per-question computation, plotting, or test scaffolds;
- standardize `results/qX`, registries, figure plans, or paper fragments;
- create national-prize style paper sections or paragraph phrasing;
- borrow contest writing patterns without copying old content;
- prepare a reproducible support package.

## Reference Routing

Open only the smallest relevant reference:

| Need | Open |
| --- | --- |
| Asset inventory or categorization | [references/asset-library-index.md](references/asset-library-index.md) |
| Safe copying or rewriting of templates | [references/template-usage.md](references/template-usage.md) |
| Patterns from prior contest projects | [references/prior-contest-patterns.md](references/prior-contest-patterns.md) |
| Official-exemplar style observations | [references/official-exemplar-notes.md](references/official-exemplar-notes.md) |
| Paper style only, no project structure | [references/national-prize-style-profile.md](references/national-prize-style-profile.md) |
| Section labels, bold subquestion labels, colon spacing, 总分 structure | [references/section-format-controls.md](references/section-format-controls.md) |
| Assumptions, model evaluation, framework advantages, limitations, extension wording | [references/assumption-evaluation-controls.md](references/assumption-evaluation-controls.md) |
| Plain contest prose, empty-phrase removal, numbers/units, judge readability | [references/contest-language-guardrails.md](references/contest-language-guardrails.md) |
| Problem analysis, model-building, result, validation, and evaluation paragraph flow | [references/paragraph-flow.md](references/paragraph-flow.md) |

## Optional Full Scaffold

Use this only when the user asks to build or reorganize a full contest project. If they only need writing style, paragraph phrases, paper skeletons, or chart templates, skip this section.

1. Check the current problem statement, official rules, data files, and required subquestions.
2. Create only needed folders such as `data/raw`, `q1/src`, `q1/tests`, `results/q1`, `paper/fragments`, `logs`, and `tmp`.
3. Copy only the needed files from `assets/contest-project-template/`.
4. Rename `problem_template` to the active subquestion folder, such as `q1` or `q2`.
5. Replace placeholder schemas with current data columns, units, constraints, and output tables.
6. Add or update evidence registries: `run_record.csv`, `result_registry.csv`, `figure_evidence.csv`, and `numerical_diagnostics.csv`.
7. Keep official outputs under `results/qX/`; exploratory files stay out of final registries unless promoted by `math-hub`.
8. Build `paper/fragments/qX.md` only from verified result tables and figure evidence.
9. Add tests before a new compute or plot script supports a paper claim.

## Asset Selection

| Need | Asset |
| --- | --- |
| New subquestion computation | `problem_template/src/compute_template.py` |
| New subquestion plotting | `problem_template/src/plot_template.py` |
| Regression test scaffold | `problem_template/tests/test_pipeline_template.py` |
| Reproduce official runs | `reproduce_all.py` |
| Paper fragment handoff | `paper/fragments/fragment_protocol.md` |
| Subquestion writing guide | `paper/problem_guide_template.md` |
| National-prize paper section skeleton | `paper/section_templates_national.md` |
| National-prize paragraph phrases | `paper/paragraph_phrases_national.md` |
| Registry seeds | `registries/*.csv` |

## Reuse Safety

- Prior-project audit: separate reusable structure from problem-specific residue.
- Path audit: remove absolute local paths before reuse or packaging.
- Evidence audit: any template output that may enter the paper needs a registry row or verified source.
- Figure audit: any main-body figure template needs a figure plan/evidence row before paper use.
- Paper audit: fragments may cite only `results/qX`, figure evidence, checked formulas, and verified rules.
- Submission audit: reproduction scripts must run from the project root and must not depend on hidden local files.

## Output Contract

Return only what the current request needs:

- copied or created template paths;
- reused structure patterns;
- placeholders still needing current problem facts;
- tests or validation commands run;
- old-template residue removed or still open;
- evidence-chain or submission risks, returned to `math-hub` when they affect paper-ready status.
