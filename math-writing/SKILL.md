---
name: math-writing
description: Use when 高教社杯/CUMCM 数学建模论文需要正文写作、段落改写、问题重述、问题分析、模型假设、结果分析、灵敏度分析、模型评价、论文语言润色，或需要阻止代码输出、原始结果、项目符号数字堆直接进入 main.tex。
---

# Contest Paper Writing

## Purpose

Shape verified modeling evidence into judge-facing paper prose. This skill owns paper-facing prose quality, but is not a workflow, not the hub, and not a substitute for modeling, computation, consistency, citation, or LaTeX gates.

Read the project's shared quality contract, when available, only when promoting wording to paper-ready, classifying blocked status, running a final gate, or writing a cross-module handoff. Local paragraph rewrites and style diagnosis should stay lightweight unless they change final claims.

## Reference Routing

- `references/paper-facing-text-guard.md`: raw-output leaks, bullet-list numeric dumps, and evidence-to-prose boundaries.
- `references/writing-templates.md`: section and paragraph templates for problem restatement, analysis, model building, results, validation, and evaluation.
- `references/section-writing-controls.md`: section shape, subquestion labels, and problem analysis format.
- `references/paragraph-flow.md`: paragraph repair when claims, evidence, formulas, or figures do not connect.
- `references/contest-language-guardrails.md`: Chinese contest-paper tone, claim strength, and empty phrase cleanup.
- `references/assumption-writing-controls.md`: assumption and model evaluation wording.
- `references/result-analysis-writing.md`: result analysis and sensitivity prose.
- `references/model-evaluation-writing.md`: model advantages, limitations, and promotion boundaries.

## Local Checks

Before writing or modifying paper-facing prose, classify each input as final text, evidence material, or diagnostic material. Evidence material includes tables, figures, formula outputs, code summaries, run records, result rows, and validation notes; it may support text, but must not be pasted as final prose.

Computed or figure-backed final wording needs traceable evidence such as `claim_ledger.csv`, `result_registry.csv`, `figure_evidence.csv`, verified tables, formulas, or source notes. If the source, unit, scenario, validation status, or claim boundary is missing, mark the wording candidate or blocked and return the gap.

Use the result-analysis pattern `conclusion -> evidence -> comparison/mechanism -> boundary/decision meaning`. A paragraph that only lists values, parameters, or scenario outputs is evidence material, not finished paper-facing prose.

## Scope Boundaries

- Route model variables, objectives, constraints, assumptions that affect equations, and validation design to `math-model` or `math-verifier`.
- Route code execution, plots, tables, logs, and registries to `math-code`, `math-table`, or `math-figure`.
- Route abstract, keywords, and first-page claim density to `math-abstract`.
- Route formatting, float placement, PDF inspection, and template preservation to `math-latex`.
- Route cross-artifact value, unit, scenario, or claim-status alignment to `math-consistency`.
- Route judge-facing score risk and readability diagnosis to `math-review`; perform paragraph repair here only after the issue is scoped.

## Output Contract

Return rewritten paper-facing prose or diagnosis, source/evidence gaps, claims that remain candidate or blocked, suggested table/figure references, and the owning module for unresolved risks.

Return to hub: math-hub.

## Red Lines

- Do not put raw console output, debug logs, bullet-list numeric dumps, code comments, model notes, or unsupported template prose into `main.tex`.
- Do not polish unsupported claims until evidence status is clear.
- Do not convert diagnostic-only, candidate, stale, relaxed, or failed results into final wording.
- Do not turn `math-writing` into a project-management workflow or global dispatcher.
