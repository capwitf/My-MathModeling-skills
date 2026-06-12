---
name: math-abstract
description: Use when 高教社杯/CUMCM/电工杯 mathematical modeling abstracts, keywords, highlights, first-page claims, or high-density summaries need drafting, revision, audit, or style diagnosis, especially when feedback mentions too many numbers, weak focus, process-listing, empty official prose, buzzwords, missing structure, weak keywords, unsupported values, or first-page claim verification.
---

# Contest Abstract

## Purpose

Turn contest evidence into a dense, judge-friendly abstract, keywords, and first-page claim set.

Two modes:

- **Style coaching mode**: diagnose or rewrite a user-provided abstract for readability, focus, number burden, contest prose, and first-screen judge value. Use only claims supplied by the user; mark evidence gaps instead of inventing support.
- **Paper-ready mode**: generate or approve a final abstract only from verified paper evidence, using the evidence gates below.

Core rule: the abstract follows evidence. No number, ranking, feasibility statement, robustness statement, or innovation claim may appear in paper-ready text unless traceable to the body, table, figure, formula, registry row, or run log.

National-first quality gate: `国一候选` is a quality target, not an award promise (`不承诺获奖`). The abstract may compress only conclusions that show 题目贴合, 建模洞察, 证据可信, 可复现, and 边界清楚. A catchy but unsupported claim must be downgraded to an evidence gap.

Hard gate: the abstract cannot introduce new claims. It may only compress claims already proven later in the paper or verified in evidence artifacts.

Language/output boundary: internal checks, registries, status labels, schemas, algorithm names, and evidence IDs may stay English. Chinese contest abstracts, keywords, and copyable paper-facing snippets should be written in Chinese by default unless the user asks otherwise.

## Required Inputs

Collect only what the active mode needs.

### Style Coaching Inputs

Use when the user wants critique, diagnosis, rewrite suggestions, or a stronger draft from existing text:

- user-provided abstract, paragraph, keywords, or reviewer feedback;
- available contest/problem background;
- user-provided model route, key results, or paper fragments;
- official abstract rules only when the user asks for final compliance.

Do not demand registries before style diagnosis. If evidence is missing, continue the diagnosis and mark rewrites as `evidence-unverified`.

### Paper-Ready Inputs

Use when the user asks for final submission abstract or first-page claim set:

- contest name, problem id, and every subproblem deliverable;
- active abstract-page, anonymity, and submission rules;
- current paper body or modeling handoff;
- verified tables, figures, logs, and solver outputs;
- `result_registry.csv`, `claim_ledger.csv`, and `figure_evidence.csv` when available;
- `innovation_ledger.csv` for innovation wording;
- row-level `validation_status` for each result.

## Workflow

1. Classify the task as style coaching, draft rewrite, or paper-ready finalization.
2. In paper-ready mode, build or audit `claim_ledger.csv`: one row per abstract or first-page claim.
3. Cross-check every claim against `result_registry.csv`, `figure_evidence.csv`, body tables, formulas, or run logs.
4. In paper-ready mode, remove unsupported values, stale runs, candidate-only results, subjective praise, and generic claims; in style mode, flag the risk rather than blocking diagnosis.
5. Open around the problem's decision object, physical mechanism, or core conflict, not generic contest background.
6. Extract one abstract spine before writing.
7. For each major deliverable, use a compact sentence with model route, key constraint/algorithm, result, and decision meaning.
8. Add robustness or sensitivity only when numeric evidence exists.
9. End with the strongest verified conclusion, not a slogan.

If the strongest conclusion is not yet verified, write a weaker verified conclusion and list the missing evidence.

Before finalizing, require a `math-consistency` pass that writes or reports `consistency_audit.csv` rows whenever the abstract contains numbers, rankings, feasibility wording, innovation claims, or figure/table references. A hub-approved replacement must use equivalent fields and blocker semantics.

AI-use disclosure does not belong in the abstract. If the contest requires disclosure, route it to `math-hub`/`math-compliance` for the final submission checklist or separate disclosure file.

## First-Screen Judge Check

Read like a tired first-screen judge. Fix higher-priority failures before wording:

1. Fatal: missing subproblem answer or deliverable.
2. Fatal: method exists but no final answer, ranking, threshold, selected plan, or diagnostic conclusion.
3. High: model route lacks variables, constraints, mechanism, or task-fit reason.
4. Medium: official-sounding prose replaces evidence.
5. Medium: many numbers lack decision meaning.
6. Low: grammar, rhythm, and polish.

For critique output, report issues in `fatal -> high -> medium -> low` order. If the abstract lacks deliverables, key results, or credible route, do not start with grammar.

## Subproblem Coverage Table

For 高教社杯/CUMCM-style multi-question papers, maintain this table mentally or explicitly before finalization:

`Subproblem | Deliverable | Model route | Key result | Decision meaning`

If any row lacks a deliverable, route, key result, or decision meaning, the abstract is not final. In style coaching, include a compact table:

`Q | Status | Missing item | Revision`

Example: `Q2 | incomplete | no key result | keep selected plan and threshold`.

## Chinese Contest Abstract Style Gate

Before generating or approving Chinese contest abstract text:

- Follow active rules; if unknown, keep a style draft within roughly one A4 page and mark official limit as unverified.
- Keep background to 1-2 short sentences.
- The first paragraph must name the object, conflict, and method family.
- Subproblem-by-subproblem wording is allowed only when each sentence carries route, result, and decision meaning.
- Avoid result-list prose. Every result should answer "what decision does this support?"
- Use a number budget: Chinese abstracts usually keep 3-6 decision-changing numbers; secondary table values go back to the body.
- When focus is scattered, compress toward one ranking, tradeoff, feasibility boundary, cost-metric balance, or bottleneck.
- Name model categories by mathematical role and contest use; do not stack long algorithm chains unless each component changes the result.
- Keywords must fit the problem object. Avoid generic terms such as "mathematical modeling", "optimization", "analysis", "MATLAB", or bare "model" unless the contest requires them.

## Number Selection

Numbers prove contribution; they do not show computation volume. Keep them in this order:

1. final answer required by the problem;
2. best/selected plan or top-ranked object;
3. constraint boundary, feasibility threshold, or bottleneck;
4. improvement against a baseline;
5. validation error, sensitivity range, or robustness result.

Delete intermediate arrays, full scenario lists, repeated table values, and numbers without decision meaning.

## One-Minute Scan

Before fine polishing, check whether a reviewer can answer four questions in one minute:

`background + method + result + decision meaning`

- What problem is studied: object, conflict, or decision?
- How is it solved: model/algorithm route and why it fits?
- What result is obtained: quantitative or ranking conclusion?
- What is it for: planning, prediction, control, classification, scheduling, location, allocation, evaluation, warning, or policy decision?

If any item is missing, mark `structure gap` and repair that part before style polish.

## Common Failure Repairs

- Empty official prose: replace phrases such as "综合考虑多种因素" or "取得较好效果" with variables, model route, result, or decision.
- Process-list abstract: keep sequence only when each step carries route and key result.
- Buzzword stack: if a component's role cannot be explained in one short phrase, remove it from the abstract. Example: "BP-LSTM-CNN-GRU-Transformer with Attention" should be reduced to the component that actually changes the contest result.
- Missing structure: do not compensate with more numbers or algorithms; add the missing claim.
- Too many numbers: keep baseline failure, selected plan, and final risk/threshold; delete intermediate comparisons.
- Heavy background: start from the problem's decision mechanism instead of policy/history padding.
- Heavy method: replace theory exposition with why the method fits this problem plus one result/validation sentence.
- Bad Chinese patterns to replace: "综合考虑多种因素", "建立了较为合理的模型", "结果表明模型具有较好效果", and "具有一定参考价值" as a 泛价值句.

## Claim Rules

- The abstract must fit the active contest abstract-page rule; if unknown in final mode, mark `unknown -> blocked`.
- Each subproblem sentence must answer the asked deliverable, not merely name a method.
- Improvements need baseline, denominator, scenario, and value.
- Feasibility needs constraint-check evidence.
- Robustness needs sensitivity, stress-test, or multiple-run evidence.
- Innovation needs explicit method change plus baseline or ablation evidence.
- "Effective", "optimal", "robust", "significant", and similar words require proof.
- Scenario analysis must not be worded as observed real-world behavior.

## Format Gate

Before finalizing abstract text, report:

- active abstract word/page limit, or `unknown -> blocked`;
- Chinese abstract present when required;
- English abstract present when required;
- keyword count and active rule fit, commonly 3-5 when no stricter local rule is supplied;
- whether keywords reuse approved paper terminology and avoid unsupported method buzzwords.

Unless the official template explicitly requires them, do not put formulas, figures, tables, citations, footnotes, or table-of-contents headings on the abstract page.

## Red Flags

Remove or downgrade abstract text when:

- a number appears only in a candidate run, screenshot, prompt output, or unarchived console log;
- "optimal", "best", "robust", "significant", or "innovative" has no exact evidence row;
- the abstract references a figure/table/result absent from the body;
- the opening is generic contest background rather than the problem's decision object or mechanism;
- AI-use disclosure appears in the abstract instead of the final checklist or separate disclosure file.

## Anti-Template-Residue Check

Before finalizing, search for leftover topic words, problem names, figure names, scenario labels, or disclosure examples from old templates or prior contests. Any mismatch between the active problem and the abstract is a submission risk.

## Output Contract

Return only what the active mode needs:

- abstract text and keywords;
- issue diagnosis ordered by severity for style coaching;
- subproblem coverage table when relevant;
- claim ledger rows or edits;
- removed unsupported/risky claims;
- missing evidence blocking a stronger abstract;
- paper-ready status and residual risks.
