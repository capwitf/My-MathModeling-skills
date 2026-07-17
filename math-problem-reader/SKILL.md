---
name: math-problem-reader
description: Use when 高教社杯/CUMCM 数学建模任务刚开始、题面/附件/分问/交付物需要解读，或需要把模糊题意、隐含条件、数据字段、递推关系和评分侧重转成可建模的问题锁定。
---

# 题面解读

## 用途

Lock what the contest problem actually asks before modeling. Separate signal from noise, identify deliverables, translate vague wording into mathematical quantities, inspect attachments, and map subquestion dependencies.

Read `math-hub/references/quality-contract.md` only when promoting paper-ready interpretation, classifying blocked status, running a final gate, or writing a cross-module handoff. Ordinary first-read triage should stay lightweight.

Core rule: prove the team understands the problem before choosing a model. If deliverables, data fields, constraints, dependencies, or scoring focus are unknown, downstream work is `diagnostic-only`.

## Reading Flow

1. Identify contest, problem id, official materials, and attachments.
2. Split statement text into signal, constraints, deliverables, and background noise.
3. Build or update `problem_brief.md`.
4. Build or update `deliverable_matrix.csv`.
5. Translate vague terms into candidate mathematical quantities.
6. Probe attachments enough to know schemas, units, missingness, and usable fields.
7. Map dependency between subquestions.
8. Return the lock and blockers to `math-hub`; do not model yet.

## Output Contract

`problem_brief.md` should capture objective, object/system, known inputs, constraints, assumptions to verify, and scoring focus.

`deliverable_matrix.csv` or an equivalent table should include subquestion, required output, source evidence, dependency, expected artifact, and blocking unknowns.

Use these labels when useful:

- `ambiguous_word`: vague phrase from the problem statement.
- `candidate_math_quantity`: possible measurable interpretation.
- `evidence_source`: statement, attachment, official rule, or user-provided source.
- `data_inventory`: file/table/sheet inventory with size, fields, missingness, and unit probe.
- `dependency_graph`: upstream output, downstream use, and dependency type.

Return to hub: math-hub.

## Red Lines

- Do not skip attachments because the statement feels clear.
- Do not model before every subquestion has a deliverable row.
- Do not copy statement prose as problem analysis; rewrite as inputs, limits, and outputs.
- Do not treat fuzzy words such as optimal, reasonable, influence, risk, capacity, or fairness as self-explanatory.
- Do not let a downstream question depend on an uncertain upstream result without marking it `blocked` or scenario-check.
