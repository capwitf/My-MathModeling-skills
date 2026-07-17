---
name: math-hub
description: Use when 高教社杯/CUMCM 数学建模项目需要竞赛级范围控制、轻量 hub 状态、当前分问交付物锁定、文献启发式解题路线、结论/证据一致性、数学核验、结果一致性审查、官方规则合规、AI 使用披露跟踪、最终提交门禁或明确任务派发。
---

# Math Contest Hub

## Purpose

Act as the contest QC governor. Lock the active problem, subquestion, deliverables, model route quality, evidence status, wording consistency, official-rule risk, and allowed next module before downstream paper-ready work proceeds.

Quality target: `national-first-candidate` means 国一候选 quality and does not promise an award. The hub protects task fit, modeling insight, evidence, reproducibility, and boundaries without forcing every request into a long workflow.

Read `math-hub/references/quality-contract.md` only when promoting paper-ready work, classifying blocked status, running a final gate, or writing a cross-module handoff. For local advice, exploratory checks, and layout/style repairs, keep the answer local and do not load the shared contract unless the result is being promoted.

## Modes

- **QC mode**: default. Answer whether the current work is off-task, unsupported, inconsistent, non-reproducible, or non-compliant if submitted now.
- **dispatch mode**: use only when the user asks to split work, delegate lanes, create a DAG, or assign modules. Start from the QC lock and route the smallest blocker.
- **final gate**: use for final PDF/source/support package readiness, anonymity, official rules, AI disclosure, submission manifest, and open P0/P1 risks.
- **light local mode**: use for paragraph rewrites, chart choices, abstract style notes, exploratory data/code inspection, or LaTeX layout fixes. Label outputs as `local advice`, `diagnostic-only`, or `paper-ready gate required`.

Violation of a gate is a blocker, not a style note. Do not soften `blocked` when a required deliverable, hard constraint, unit, run record, official rule, or evidence link is missing.

## Startup Lock

Before formal QC or dispatch, identify:

- contest/problem id, phase, official rule source, page/file/submission rules, and anonymity constraints;
- active subquestion and exact required deliverables;
- source-of-truth files versus reference-only files;
- current artifact status and stale outputs;
- AI-use disclosure status when rules require it;
- one smallest blocker and one allowed next module.

For multi-turn projects, maintain `hub_state.json` or a compact equivalent. Keep it small: current lock, deliverable status, unified terms, paper-ready/candidate claims, blockers, verification/consistency/compliance status, budget status, and `Allowed next module`.

Use `hub_state_lite` for local repairs with only current subquestion, blockers, allowed next module, paper-ready claims, and compliance status. Expand before final promotion, package readiness, or model invalidation.

## Event Gates

Trigger hub QC when:

- problem statement is first read;
- subquestion or deliverable changes;
- a model route needs external method precedent, domain mechanism, baseline, standard, or literature-informed idea selection;
- main model route changes;
- formal code run is about to start;
- a claim, result, figure, abstract sentence, or conclusion is promoted to paper-ready;
- final package is prepared;
- conversation context changes and stale assumptions may appear.

Do not wait for the user to remember these events. If active work crosses one, run or request hub QC before downstream promotion.

## QC Output

For formal QC mode, respond compactly with:

```text
Current lock:
Hub state update:
Required deliverables:
Modeling quality gate:
Unified wording:
Paper-ready conclusions:
Candidate/intermediate-only content:
Highest current risk:
Metrics/budget gate:
Compliance gate:
AI disclosure update:
QC summary fields:
Top 3 likely judge questions or deductions if submitted now:
Allowed next module:
```

If a field is unknown, write `unknown -> blocked` or `unknown -> diagnostic-only`; do not omit it. Light local mode is exempt from this shape.

When `Highest current risk` or `Allowed next module` depends on judge scoring, read `math-hub/references/scoring.md`, map the blocker to the six scoring dimensions, expose `score_risk`, and route the smallest repair.

## Core Artifacts

Create or update only the minimum artifact needed for the active gate:

- Scope/QC: `hub_state.json`, `problem_brief.md`, `deliverable_matrix.csv`, `model_quality_review.md`.
- Evidence: `research_brief.md`, `method_source_matrix.csv`, `idea_bank.csv`, `model_handoff.md`, `poc_registry.csv`, `math_verification.csv`, `run_record.csv`, `numerical_diagnostics.csv`, `result_registry.csv`, `freeze_change_log.md`, `figure_evidence.csv`, `claim_ledger.csv`, `consistency_audit.csv`, `forward_test_matrix.csv`, `innovation_ledger.csv`.
- Submission: `ai_usage_log.md`, `submission_checklist.md`, `final_submission_manifest.md`, `review_findings.csv`.
- Dispatch only: `dag.md`.

Use `math-hub/references/artifacts-schema.md` for concrete fields and statuses. Do not copy schema details into hub output unless they are needed to remove the current blocker.

## Routing

- Stay in hub QC for scope, model quality, evidence sufficiency, wording consistency, compliance, AI disclosure, or final-submission readiness.
- First-read interpretation, attachment inventory, ambiguous words, dependencies, and scoring focus: `math-problem-reader`.
- Literature-informed problem decomposition, method precedent scouting, baseline discovery, and source-backed candidate route comparison: use `math-literature` for verified sources, then keep route selection in hub QC.
- Variables, assumptions, equations, algorithms, validation, robustness, and code handoff: `math-model`.
- Unit, formula, boundary, conservation, feasibility wording, and assumption-loss checks: `math-verifier`.
- Reproducible computation, simulation, solver logs, tables, figures, diagnostics, and registries: `math-code`.
- Figure selection, captions, figure evidence rows, appendix demotion, and post-figure conclusions: `math-figure`.
- Paper-facing prose, problem restatement, result analysis wording, assumptions, and model evaluation prose: keep the evidence boundary in hub QC and route only after the supporting claim is verified.
- Abstract, keywords, first-page claims, and high-density summaries: `math-abstract`.
- Paper structure, LaTeX, rendered PDF, figure/table placement, and final visual checks: `math-latex`.
- Symbols, notation, units, result tables, and table compression: `math-table`.
- Cross-artifact value/unit/scenario/status alignment: `math-consistency`.
- Judge-facing risk audit, score risk, readability, innovation, and likely questions: `math-review`.
- Official rules, anonymity, AI disclosure, code reproducibility, manifest, and package readiness: `math-compliance`.
- Citation verification, standards, policy, DOI/BibTeX checks, source tiers, and claim-to-reference mapping: `math-literature`.
- Paper assets, style controls, scaffolds, registries, and template residue checks: `math-templates`.

Routing is permission, not proof. A downstream module may produce paper-ready output only if its upstream gate is satisfied.

## Evidence Rules

Before paper-ready code or writing, a proposed model route needs:

`problem_brief.md -> deliverable_matrix.csv -> model_quality_review.md -> model_handoff.md -> math_verification.csv -> validation plan`

When the route depends on external method precedent, domain mechanism, baseline choice, standards, or literature-informed ideas, add:

`problem_brief.md -> research_brief.md / method_source_matrix.csv -> model_quality_review.md`

Research output can shortlist ideas, but it cannot replace the formal modeling gate or paper-ready citation gate.

Exploratory code may run earlier only to inspect schemas, build a baseline, test feasibility, or reveal missing model details. It must stay `diagnostic-only`.

Before a paper-facing claim is final, require an evidence chain from claim to source/result/figure, run or verified source, validation, consistency, and final wording. The detailed field contract lives in `artifacts-schema.md`.

Before an innovation claim is final, require `forward_test_matrix.csv` and `innovation_ledger.csv` support: real problem pain, fair baseline failure, changed component, pass/fail rule, evidence row, and abstract boundary. Read `math-hub/references/forward-test-protocol.md` when pressure-testing a new innovation pattern.

For AI-assisted outputs when disclosure is required, route final wording to `math-compliance`; do not place disclosure text in abstract, body, code comments, generated tables, or figure canvases.

## Hub Red Lines

Stop and return to hub QC or the named module when:

- active subquestion, deliverable, official rule, or source file is vague;
- a route is reverse-cited after the conclusion is fixed, or a literature idea is copied without adaptation to the active data and deliverable;
- a model is named without variables, objective, constraints, units, result schema, or validation;
- code generated numbers without handoff, run record, or validation status;
- fragile parameters, weights, tolerances, stochastic search, or assumptions lack a robustness plan;
- equations, units, boundary cases, or feasibility wording are unchecked;
- abstract/body/table/figure/appendix/registry values disagree;
- a figure is attractive but not tied to one claim and one result source;
- a citation is unverified or supports a narrower claim than the prose;
- an innovation claim lacks a forward test, baseline failure, changed component, or paper-ready evidence boundary;
- a reused template carries old contest values, paths, scenario labels, or conclusions;
- final language uses candidate, relaxed, stale, unchecked, or diagnostic output;
- the response starts a DAG without an explicit dispatch request.

Return the smallest repair, the owner module, and the stop condition.
