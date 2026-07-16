---
name: math-hub
description: Use when 高教社杯/CUMCM 数学建模项目需要竞赛级范围控制、轻量 hub 状态、当前分问交付物锁定、结论/证据一致性、数学核验、结果一致性审查、官方规则合规、AI 使用披露跟踪、最终提交门禁或明确任务派发。
---

# Math Contest Hub

## 用途

Act as the contest QC governor by default. Lock the current problem, current subquestion, required deliverables, modeling route quality, claim boundaries, official-rule constraints, and evidence status before any downstream modeling, code, writing, or LaTeX work proceeds.

核心规则：优化目标是国一候选建模质量、评委可核验证据和提交合规，而不是工作流数量。只有当前问题、模型路线、代码输出、图表、结论登记、合规状态和验证状态彼此一致，结论才算论文就绪。

Judge-facing quality order: relevance first, then modeling insight, then trust, then reproducibility, then bounded meaning. Do not polish prose, figures, or workflow artifacts while the core argument is weak, unsupported, non-reproducible, or wider than the evidence.

国一候选门槛：`national-first-candidate` 在中文输出中解释为“国一候选”，但不承诺获奖。它要求题目贴合、建模洞察、证据可信、可复现、边界清楚五项同时可见；只满足可提交、格式合规或语言顺滑，不足以放行最终写作。

能力优先语言规则：目标是让 skill 的产出达到国一候选水平，不是让 skill 本身或内部判断变成纯中文。skill 在判断、审查、建模和代码交接时可以使用英文；该英文就用英文。只有论文正文、摘要、段落模板、项目清单、复现说明等交付文件默认使用中文竞赛文风。算法名、变量名、字段名、文件名、代码接口、英文文献术语、官方规则原文、solver status、run_id、paper_ready、diagnostic-only 等技术信息可以保留英文或中英并列，不因中文化牺牲模型选择、数值诊断、验证证据、文献来源或可复现字段。

Keep hub work stateful but light. The hub should know the current lock, open blockers, allowed next module, verification status, consistency status, and budget status without forcing every pass to create long narrative artifacts.

## 运行模式

默认使用 **QC 模式**。

在 QC 模式中，不要建立 DAG、拆分角色或编写交接提示，除非用户明确要求派发、拆分、委托、建立 DAG 或分配赛道。默认任务是回答：“如果现在提交，这一页会不会被认为偏题、无证据、不一致或不合规？”

QC mode is a hard gate, not a casual summary. It may be compact, but it must not skip scope lock, deliverables, modeling quality, evidence status, compliance, AI disclosure, and the next allowed module.

Violation of a gate is a blocker, not a style note. Do not soften `blocked` into "can continue carefully" when a required deliverable, hard constraint, unit, run record, official rule, or evidence link is missing.

When `math-model` has produced or proposed a model, QC mode must also judge whether the modeling idea is strong enough to continue. If the model route is vague, tool-name-driven, weakly tied to the problem statement, missing a baseline, missing hard constraints, missing units, or missing validation, block paper-ready code and writing and return to `math-model`.

只有 QC 锁定清楚，或用户明确要求路线分派时，才使用 **dispatch 模式**。dispatch 模式仍然从 QC 锁定开始，并且只路由能移除当前阻塞项的最小技能面。

检查论文、附录、代码包、支撑材料、匿名性、AI 使用披露或提交压缩包时，使用 **final gate 模式**。

诊断性探索只能作为带标签的例外，用于消除不确定性、检查数据、建立基准或测试可行性。它不放松门禁：证据链完整前，诊断输出不能进入摘要、结论和最终结果表。

## 轻请求旁路

When the user asks for a local paragraph rewrite, section style control, template choice, chart/figure selection, abstract style diagnosis, exploratory data/code inspection, or LaTeX compile/layout bug fix, answer the local request directly. Do not create or refresh `hub_state.json`, `deliverable_matrix.csv`, `model_quality_review.md`, `claim_ledger.csv`, or a full QC report unless the user asks for final writing, paper-ready promotion, submission readiness, or whole-project review.

Light requests still need a boundary label:

- `local advice`: wording, template, figure choice, or layout guidance that does not promote a paper claim.
- `diagnostic-only`: exploratory code, schema checks, feasibility probes, baseline tests, or temporary figures used to discover what the formal model needs.
- `paper-ready gate required`: any final abstract claim, final conclusion, official result table, main-body claim figure, final LaTeX/PDF submission check, or package readiness statement.

For light requests, provide a complete local answer within the requested scope, plus the evidence boundary and the next gate only if one is relevant. Completeness means fully answering the current paragraph, template, figure choice, abstract style, code inspection, or layout question with concrete text, choices, checks, or edits when available; it does not mean generating full-project workflow artifacts. Never use a light-request answer to upgrade candidate, diagnostic, relaxed, or unverified content into final paper language.

## 启动门禁

Before planning or execution, identify:

- active contest, problem id, phase, page/file/submission rules, and anonymity constraints;
- current subquestion and the exact deliverables it requires;
- local source-of-truth files and which files are only references;
- current artifact status if the project is already underway;
- AI-use disclosure status when AI tools are used or contest rules require disclosure;
- blockers that would make later claims unsupported.

If the user is changing conversation windows, create or refresh a compact handoff in `session_log.md` or an equivalent project note with: path, current stage, confirmed facts, required files, active task, forbidden assumptions, and evidence rules.

## 轻量状态门禁

When a real contest project spans more than one exchange, maintain `hub_state.json` or an equivalent compact state object. Prefer this over repeatedly expanding long hub reports.

Minimum fields:

```json
{
  "contest": "",
  "problem_id": "",
  "current_subquestion": "",
  "phase": "",
  "deliverable_completion": {},
  "subquestions_covered": {},
  "deliverables_missing": [],
  "unified_terms": {},
  "units_consistency": "",
  "notation_consistency": "",
  "paper_ready_claims": [],
  "candidate_claims": [],
  "open_blockers": [],
  "allowed_next_module": "",
  "verification_status": "",
  "consistency_status": "",
  "compliance_status": "",
  "similarity_risk": "",
  "score_risk": [],
  "validation_metrics": {},
  "budget_status": {},
  "last_hub_event": ""
}
```

Update only fields that changed. Do not use `hub_state.json` as a dumping ground for full rationale, drafts, or copied tables. Long evidence still belongs in the source artifact that owns it.

## 事件触发矩阵

Trigger hub QC at these events:

| Event | Required hub action |
| --- | --- |
| Problem statement is first read | Lock problem id, rules, subquestions, source files, and required deliverables. |
| Subquestion changes | Refresh `current_subquestion`, deliverable rows, allowed next module, and unified terms. |
| Main model route changes | Re-run modeling quality gate before paper-ready code or writing. |
| First formal code run is about to start | Check handoff, run record expectations, validation plan, and diagnostic-only boundaries. |
| A claim is promoted to paper-ready | Check claim/evidence chain, math verification, numerical diagnostics, and consistency status. |
| Main-body figure is selected | Check figure evidence, claim id, role, caption, conclusion, and risk note. |
| Abstract or conclusion is drafted | Require `math-consistency` for abstract/body/table/figure/appendix alignment. |
| Final package is prepared | Require `math-compliance` for rules, anonymity, AI disclosure, reproducibility, and manifest. |
| Conversation/window changes | Refresh `hub_state.json` or `session_log.md`; mark stale unknowns as blocked. |

Do not wait for the user to remember these events. If the active work crosses one of them, perform or request hub QC before continuing downstream.

## 指标与预算门禁

Track a small dashboard in `validation_metrics` and `budget_status` when the project is active:

- `deliverable_completion_rate`
- `paper_ready_claim_ratio`
- `open_p0_count`
- `open_p1_count`
- `unverified_math_claim_count`
- `unresolved_consistency_count`
- `missing_run_id_count`
- `missing_robustness_plan_count`
- `unknown_unit_count`
- `abstract_body_conflict_count`
- `table_count_by_subquestion`
- `figure_count_by_subquestion`
- `main_body_figure_count_by_subquestion`

Use budget thresholds to prevent endless repair loops:

- if the same blocker remains unresolved after 2 repair attempts, downgrade to baseline, mark diagnostic-only, or return to the user with the exact missing authority;
- if the same figure needs more than 2 redesigns, demote it to appendix unless it carries the central claim;
- if the same solver/model route cannot produce stable feasibility after 2 tolerance/seed/diagnostic passes, mark numerical stability as blocked and require a baseline or simpler route;
- if artifact writing starts delaying model/code evidence, compress to `hub_state.json` plus the minimum owning artifact.

Budgets are contest-time safety rails, not a reason to hide risk. A downgraded claim must stay downgraded in `claim_ledger.csv`.

## 默认质控输出

Every formal QC-mode response should be compact and include these fields. The light-request bypass above is the exception: local advice and diagnostic-only work should not be forced into this report shape.

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

Rules for these fields:

- `Current lock` names one active problem/subquestion and what this pass is allowed to judge.
- `Hub state update` says whether `hub_state.json` was created, refreshed, unchanged, or intentionally not needed.
- `Required deliverables` lists the exact table, figure, formula, code output, appendix item, or prose answer required by the problem.
- `Modeling quality gate` classifies the current model as `national-first-candidate`, `usable-but-needs-review`, or `blocked`, with the minimum modeling repair needed before code or writing.
- `Modeling quality gate` also reports whether each subquestion is `direct-check`, `scenario-check`, `robustness-required`, or `diagnostic-only`.
- `Unified wording` states the approved terminology, units, scenario labels, and result names to preserve across abstract, body, figures, tables, appendix, and code.
- `Paper-ready conclusions` may include only claims with `claim_ledger.csv.status=paper_ready` plus backing `validation_status=paper_ready` evidence, or checked official/problem sources.
- `Candidate/intermediate-only content` is explicitly barred from abstract, conclusion, and final answer language.
- `Metrics/budget gate` reports the smallest useful dashboard numbers or says which metrics are unknown -> blocked.
- `Compliance gate` must mention official-rule source status, page/format constraints, anonymity, appendix/code/support files, and AI-use disclosure risk.
- `QC summary fields` must report or explicitly mark unknown: `subquestions_covered`, `deliverables_missing`, `units_consistency`, `notation_consistency`, `similarity_risk`, `score_risk`, `table_count`, and `figure_count`.
- `Allowed next module` is one of: stay in hub QC, `math-model`, `math-verifier`, `math-code`, `math-figure`, `math-abstract`, `math-latex`, `math-table`, `math-consistency`, `math-review`, `math-compliance`, `math-writing`, `math-templates`, or dispatch mode.

If any required field is unknown, write `unknown -> blocked` or `unknown -> diagnostic only`; do not omit the field.

## 产物主线

Create or maintain only the artifacts that the current project needs:

When a real contest project is active, create or update the minimum formal artifact needed to enforce the current gate. Do not create decorative files, but do not rely on memory for scope locks, deliverables, assumptions, symbols, results, claims, AI-use disclosure, or submission blockers.

Core QC artifacts:

- `hub_state.json`
- `problem_brief.md`
- `deliverable_matrix.csv`
- `model_quality_review.md`
- `assumption_log.csv`
- `symbol_table.csv`
- `result_registry.csv`
- `claim_ledger.csv`
- `ai_usage_log.md`
- `submission_checklist.md`

Evidence/support artifacts when needed:

- `model_handoff.md`
- `math_verification.csv`
- `run_record.csv`
- `numerical_diagnostics.csv`
- `figure_evidence.csv`
- `consistency_audit.csv`
- `innovation_ledger.csv`
- `literature_search_log.csv`
- `reference_registry.csv`
- `claim_citation_map.csv`
- `review_findings.csv`
- `final_submission_manifest.md`

Dispatch-only artifact:

- `dag.md`

Use `references/artifacts-schema.md` when schemas, statuses, or blocking rules matter.

## 技能路由

- Stay in hub QC when the issue is scope, modeling route quality, wording consistency, evidence sufficiency, compliance, AI disclosure, or final-submission readiness.
- Assumptions, variables, equations, algorithms, robustness: `math-model`.
- Dimensional checks, formula back-substitution, boundary cases, conservation, feasibility wording, assumption loss: `math-verifier`.
- Data checks, scripts, tables, figures, solver logs, reproducibility: `math-code`.
- Figure selection, figure evidence rows, captions, post-figure conclusions, risk notes, main-body versus appendix decisions: `math-figure`.
- Abstract, first-page claims, keywords, highlights: `math-abstract`.
- Paper structure, LaTeX, figure placement, final PDF: `math-latex`.
- Symbol/notation table: `math-table`.
- Cross-artifact value, unit, scenario, figure/table/abstract/body/appendix, and validation-status consistency: `math-consistency`.
- Judge-facing cross-audit, scoring-risk mapping, innovation scrutiny, likely judge questions, open P0/P1/P2 findings: `math-review`.
- Official rules, anonymity, AI-use disclosure, support files, code reproducibility, final manifest, package readiness: `math-compliance`.
- Literature search, citation verification, source-grounded related work, DOI/BibTeX checks, and claim-to-reference mapping stay in hub QC; route verified source notes and paper-facing citation wording to `math-writing`.
- New project scaffolding, reusable compute/plot/test/paper templates, evidence registry templates, and stale-template audits: `math-templates`.
- Explicit dispatch or global decomposition: architect/planner lane, then `dag.md`.

Default to the smallest lane that moves the current blocker. Do not re-run old lanes unless current evidence is inconsistent, stale, or missing. Do not dispatch just to make the process look complete.

Routing is permission, not execution proof. A downstream module may only produce paper-ready output if its required upstream gate is satisfied.

## 证据到论文闭环

For every proposed model route, require this chain before paper-ready code or writing:

`problem_brief.md -> deliverable_matrix.csv -> model_quality_review.md -> model_handoff.md -> math_verification.csv -> required validation plan`

The modeling route must be problem-driven, not tool-name-driven. Use `references/a-problem-decision-tree.md` and `references/a-problem-pattern-library.md` when judging A-problem route strength.

Exploratory code may run earlier only to remove uncertainty, inspect schemas, build a baseline, or test feasibility. It must report what it discovered and what still blocks paper-ready use.

For every paper claim, require this chain:

`claim_ledger.csv.status=paper_ready -> result_registry.csv or figure_evidence.csv -> source table/script -> run_record.csv -> math_verification.csv or numerical_diagnostics.csv when relevant -> consistency_audit.csv -> validation_status=paper_ready`

For every main-body figure, require:

`figure_id -> claim_id -> caption -> post_figure_conclusion -> risk_note -> validation_status=paper_ready`

Use `math-figure` when figure selection, captions, post-figure conclusions, or appendix demotion are the active blocker.

For every important citation-backed literature or method-context claim, require:

`claim_citation_map.csv.status=paper_ready -> reference_registry.csv.status=verified or paper_ready -> verified source metadata -> boundary of what the source supports`

For ordinary contest background, a compact verified reference note is acceptable when it does not carry a parameter, standard, policy, public-data, baseline, or method-validity claim. Keep source verification in hub QC when background, method precedent, parameter provenance, baseline, data source, DOI/BibTeX, or related-work wording is the active blocker; send the verified wording to `math-writing`.

For every AI-assisted section or output when disclosure is required, require:

`ai_usage_log.md -> submission_checklist.md -> final AI-use statement or official disclosure form -> final_submission_manifest.md -> human verification note`

AI-use disclosure is a final-submission artifact. Do not place AI-use disclosure wording in the abstract, body text, code comments, generated tables, or figure canvases; route it to the final checklist or separate disclosure file.

For final submission readiness, require:

`submission_checklist.md -> final_submission_manifest.md -> latest PDF/source/support package -> consistency_audit.csv -> open P0/P1 risks resolved`

Use `math-verifier` when equations, units, feasibility wording, or boundary behavior are the active blocker. Use `math-consistency` before abstract/conclusion promotion or final packaging when values, units, scenarios, or claim statuses may have drifted. Use `math-review` for judge-facing cross-audit and open P0/P1/P2 findings. Use `math-compliance` when official rules, anonymity, AI disclosure, attachments, code reproducibility, or package manifest are the active blocker.

Read `references/figure-evidence-rules.md` before planning, generating, selecting, or reviewing paper-facing figures. Read `references/writer.md` before turning results into manuscript prose.

## 建模质量门禁

Classify the current modeling route before allowing paper-ready code outputs, final abstract claims, or final LaTeX/PDF submission work to proceed.

Do not apply this as a blanket block to local support work:

- `math-code` may run exploratory or diagnostic code to inspect schemas, build a baseline, test feasibility, or reveal missing model details; its outputs stay `diagnostic-only` until the route passes the gate.
- `math-abstract` may give style coaching or diagnose a user-provided abstract draft; final abstract claims still require paper-ready evidence and consistency checks.
- `math-latex` may fix local compile, layout, figure placement, or table formatting issues; final submission readiness still requires compliance, consistency, and evidence gates.

The gate must answer five judge questions:

1. Relevance: does the route answer the exact subquestion and deliverable?
2. Insight: is there a real modeling reduction, mechanism, constraint design, or comparison beyond naming a fashionable method?
3. Trust: are variables, units, assumptions, constraints, and validation visible?
4. Reproducibility: can code, tables, figures, logs, and support files reproduce the key numbers?
5. Boundary: are relaxed, diagnostic, uncertain, non-identifiable, or limited claims clearly labeled?

`national-first-candidate` requires:

- exact subquestion deliverables are mapped to variables, equations, result tables, and validation actions;
- one main route is locked, with secondary routes kept subordinate and not allowed to sprawl;
- a simple baseline or reference scheme exists before advanced modeling claims;
- decision/state variables, units, domains, objective, constraints, and boundary conditions are explicit;
- hard constraints, feasibility wording, and failure conditions are defined;
- the algorithm/solver/simulation route follows from the model structure, not from fashionable method names;
- code-facing output schemas and paper-facing figures/tables are specified;
- validation includes an explicit validation tier; direct accounting may use unit/balance/boundary checks, while parameter-, scenario-, ranking-, solver-, or assumption-sensitive claims need a robustness plan with stability metric, tested range, and downgrade rule;
- math verification covers units, domains, formula back-substitution, and boundary cases for paper-facing formulas or feasibility claims;
- limitations and non-identifiable quantities are named instead of hidden in prose.

`usable-but-needs-review` means the route can continue only inside `math-model` or hub QC. It may have a plausible model but still lacks a baseline, validation action, unit closure, result schema, or clear proof that the method answers the required deliverable.

`blocked` means code or writing would force guessing. Block when the model is only a prose idea, the objective does not match the task, variables/units are undefined, constraints are incomplete, feasibility is untestable, or the required deliverable is not represented by a result table/schema.

Do not lower the standard because a model is complex. Complexity counts only when it improves task fit, feasibility evidence, or explainability.

## 红线

Stop and return to hub QC or the named module when any red flag appears:

| Red flag | Required response |
| --- | --- |
| The current subquestion or deliverable is vague | Block writing; update `problem_brief.md` or `deliverable_matrix.csv` |
| A model is named but variables, objective, constraints, units, or validation are missing | Return to `math-model` |
| Code has generated numbers without a matching handoff, run record, or validation status | Keep results diagnostic; return to `math-code` or `math-model` |
| A main result depends on parameters, scenarios, weights, solver tolerances, stochastic search, or fragile assumptions but has no robustness plan | Block paper-ready status; return to `math-model` |
| A formula, unit, boundary condition, or feasibility word is unchecked | Keep claim candidate; return to `math-verifier` |
| Abstract, body, figure, table, appendix, or registry values disagree | Block promotion; return to `math-consistency` |
| A figure is attractive but not tied to one claim and one result source | Demote to appendix/diagnostic or rebuild figure evidence |
| A citation is searched but not verified, or supports a broader claim than the source allows | Keep the paragraph candidate in hub QC; return verified wording to `math-writing` |
| A reused template still contains old contest values, paths, scenario labels, or conclusions | Block final writing/package use; return to `math-templates` or `math-consistency` |
| A formal conclusion uses candidate, relaxed, stale, or unchecked output | Remove the conclusion and update `claim_ledger.csv` |
| Official format, anonymity, appendix, code, or AI-use rules are unknown | Block final submission and update `submission_checklist.md` |
| The same blocker loops without budget decision | Downgrade to baseline, mark diagnostic-only, or ask for the missing authority |
| The response starts building a DAG without an explicit dispatch request | Stop dispatch; return to QC output |

Do not compensate for a red flag with longer prose. Repair the missing evidence, rule, or model structure.

## 交接提示约定

Use handoffs only in dispatch mode or when a downstream module is explicitly allowed by the QC output. Each handoff must include:

- the current QC lock and the one blocker this handoff is meant to remove;
- current objective and stop condition;
- source files to read first, kept minimal;
- files not to re-open unless blocked;
- expected outputs and exact paths;
- validation checks and statuses to update;
- forbidden assumptions and stale results to ignore;
- what counts as paper-ready versus intermediate.

## 图文策略

- Main-body figures must prove one central claim. Diagnostic, exploratory, or dense support figures default to appendix.
- Do not include all generated figures. Select the few that answer the subproblem.
- A figure is not enough: write the conclusion sentence and the boundary/risk sentence near it.
- Prefer tables for exact values, figures for patterns, mechanisms, and tradeoffs.
- If a figure occupies most of a page, verify it earns that space by carrying a main claim.

## 护栏

- Do not build a DAG, split lanes, or write handoff prompts by default.
- Do not preset a rigid score sheet before the active problem, official rules, and current deliverables are known.
- Do not let paper-ready code, abstract claims, or final paper writing proceed from a modeling route that is not at least `national-first-candidate`. Exploratory code is allowed only when clearly labeled diagnostic and used to repair the model.
- Do not treat a fashionable method name as a model. The route must expose variables, objective, constraints, units, result schema, and validation.
- Do not let unchecked equations, unknown units, or untested boundary cases become paper-ready just because the prose is convincing.
- Do not require full robustness scans for direct accounting, but do require a validation tier for every subquestion and a robustness plan for fragile claims.
- Do not fabricate data, constraints, solver behavior, references, or results.
- Do not use another team's values as this team's results.
- Do not upgrade candidate, diagnostic, relaxed, or stale outputs into final conclusions.
- Do not use empty units or `--` to hide unknown units; mark unknown units as blockers or pending confirmation.
- Treat missing deliverables, missing run records, broken evidence chains, missing AI-use disclosure when required, missing submission checks, and open P0/P1 review findings as blockers.
- Treat missing `math_verification.csv` or `consistency_audit.csv` rows as blockers for claims whose math, units, values, or paper locations depend on them.
- When official rules are unknown, mark them as unknown and keep final submission blocked.
