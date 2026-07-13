---
name: math-model
description: Use when 高教社杯/CUMCM 数学建模任务需要变量、假设、公式、约束、算法、验证设计、鲁棒性规划、灵敏度分析、结果 schema，或基于题面和本地证据的代码交接。
---

# 竞赛建模

## 用途

Turn the locked problem brief into a problem-driven model route: variables, constraints, assumptions, units, objective/mechanism, validation, robustness plan, result schema, and code handoff.

For a `paper_ready` promotion, final gate, or cross-module handoff, apply the current `math-hub` evidence rules. For exploratory model sketches, keep the boundary local.

国一候选门槛：建模输出必须同时体现题目贴合、建模洞察、证据可信、可复现、边界清楚；这是提交质量门槛，不承诺获奖。

Do not choose an algorithm because it sounds advanced. First state what mathematical problem the subquestion is, then choose the simplest route that can answer the required deliverable.

## Required Inputs

- `problem_brief.md` and `deliverable_matrix.csv`, or an equivalent current lock from `math-problem-reader`/`math-hub`;
- active subquestion, input data, assumptions, limits, and expected output;
- known units, source files, and official constraints;
- `research_brief.md` or `method_source_matrix.csv` when the route was literature-informed or when multiple source-backed candidate routes were scouted;
- prior model version if this is a revision.

If these are missing, return to `math-problem-reader` or `math-hub` instead of inventing the task.

## Modeling Flow

1. Restate the subquestion as inputs, limits, decision object, and outputs.
2. Name the mechanism or mathematical family before naming software or algorithms.
3. Define variables, domains, units, assumptions, objective, constraints, and boundary conditions.
4. Select one main route; keep secondary methods subordinate.
5. If source scouting produced candidates, compare their task fit, data fit, validation burden, and citation boundary before selecting the main route.
6. Add a baseline or reference scheme before advanced claims.
7. Define validation tier: direct check, scenario check, robustness-required, or diagnostic-only.
8. Write the result schema and paper figure/table plan.
9. Prepare `model_handoff.md` for `math-code` and `math_verification.csv` expectations for `math-verifier`.

Record method choice rationale with evidence id, baseline defect, and boundary: do not copy AI suggestions or write only "works better"; name the data, PoC, baseline failure, and condition under which the chosen route is valid.

## Model Family Triage

Do not choose MILP/MIP merely because the paper needs variables, objectives, and constraints. Start from the mechanism and use the least unsupported machinery.

- A discrete decision table with coupled binary logic may use MILP/MIP, but never as a generic wrapper.
- Flow, assignment, scheduling, and staged decisions should consider network flow/DP before generic MILP; use MILP when logic constraints or coupled binary decisions need it.
- A continuous resource allocation problem should consider LP/QP/convex optimization/nonlinear programming according to structure.
- A geometry or physics task needs derivation, direct numerical evaluation, or simulation according to the mechanism.
- A time evolution problem may require a dynamic model/state-space/time series route.
- A ranking or evaluation task needs an indicator system + sensitivity.
- Uncertainty tasks need scenario/robust/stochastic analysis.

Use MILP/MIP only when discrete decisions are linear or safely linearizable and the deliverable needs an auditable decision or allocation output, not as a generic wrapper.

For any dynamic route, use simulation only when its state evolution or event mechanism is needed by the deliverable.

## Simulation Route Fitness

Simulation is neither preferred nor downgraded by default. Select it only when it is the best-fitting route for the subproblem mechanism and required deliverable; otherwise keep simulation as validation, scenario exploration, or diagnostic evidence.

- `deterministic time-step / grid simulation`: state evolution, conservation, or spatial fields.
- `discrete-event simulation`: queues, arrivals, service, failures, or resource events.
- `Monte Carlo / scenario simulation`: uncertainty propagation and distributional output.
- `agent-based / game simulation`: interacting actors and local rules.
- `simulation + optimization`: policy evaluation coupled to an auditable decision search.

A `Simulation Plan` names state variables, initial/boundary conditions, horizon or step size, replications, seeds, baseline, invariant checks, step-size sensitivity, output schema, and a downgrade rule. Raw or single-run screenshots are diagnostic and cannot support paper-ready wording.

For simulation, include state variables, initialization, boundary conditions, event rules, seeds/replications when stochastic, calibration/back-test when data allow it, and a downgrade rule when sensitivity fails.

## 鲁棒性计划门禁

Every subquestion needs a validation tier:

- `direct-check`: unit, balance, accounting, boundary, or formula substitution is enough.
- `scenario-check`: compare named scenarios, stress cases, or baselines.
- `robustness-required`: conclusion depends on weights, thresholds, fitted parameters, solver tolerances, stochastic search, or fragile assumptions.
- `diagnostic-only`: check reduces uncertainty but cannot support final wording.

A robustness plan must name varied inputs, tested range, baseline, stability metric, pass/fail criterion, and downgrade rule.

Read `references/robustness-protocol.md` for route-specific checks.

## PoC Gate

Before a computational route can support `paper_ready` evidence, require a `poc_registry.csv` row for each main or baseline candidate: a `<=30-line` PoC script or command run on a `real data` slice or real attachment-derived sample, with input path, command, candidate id, output number or failure verdict, and status. A synthetic-data PoC may guide modeling, but it stays `diagnostic-only` and cannot support `paper_ready` promotion.

If a candidate failed its PoC or is rejected after comparison, keep `poc_registry.csv.status` as `passed/failed/blocked/diagnostic-only`, record `failure_reason`, and mark the deprecated route in `model_handoff.md`; any remaining reference to it is diagnostic-only. A rejected method must not remain as a backup main conclusion; paper wording is blocked until the surviving route has passed real-data evidence.

## Code Handoff

The code handoff in `model_handoff.md` is blocked if implementation would need to invent a parameter, threshold, unit, solver tolerance, output schema, feasibility label, or missing constraint. Keep the route inside `math-model` until these are explicit.

Minimum handoff content:

- active subquestion and deliverable;
- variables, constraints, units, assumptions, and objective/mechanism;
- input files and trusted columns;
- PoC ids from `poc_registry.csv`, including which candidate passed, failed, or stayed diagnostic-only;
- algorithm or solver route with parameters and tolerances;
- output tables/figures and expected filenames;
- validation and robustness checks;
- paper-ready versus diagnostic-only boundaries.

When a route is replaced, publish a new `model_handoff.md` version with changed assumptions/variables/constraints and which prior claims or runs are no longer paper-ready.

## Verification Handoff

Before paper-ready promotion, provide enough structure for `math-verifier`:

- formula list, units, domains, and boundary cases;
- feasibility wording and hard constraints;
- assumptions that may fail;
- expected rows for `math_verification.csv`.

If these are missing, keep the route `blocked` or `diagnostic-only`.

## 覆盖与单位闭合门禁

Before handing a model to code or writing, publish `subquestions_covered` and `deliverables_missing`. Each required subquestion must map to a model section, result schema, validation action, and paper-facing conclusion status. Each variable, parameter, objective term, constraint term, and reported metric needs a unit or an explicit dimensionless label; uncovered deliverables remain `blocked` or `diagnostic-only`.

## Output Contract

Return:

- model route and why it fits the subquestion;
- source-backed route rationale and adaptation boundary when literature scouting was used;
- variables, constraints, units, assumptions, and objective/mechanism;
- validation tier and robustness plan;
- result schema and figure/table plan;
- `model_handoff.md` content or edits;
- blockers and the next owner module.

Return to hub: math-hub.

## Red Lines

- Do not model before deliverables and attachments are understood.
- Do not use a method name as the model.
- Do not treat a literature idea as the selected model until it is adapted to current deliverables, data, units, constraints, and validation.
- Do not omit units, domains, hard constraints, or feasibility conditions.
- Do not hand code a model that requires guessing.
- Do not promote simulation, optimization, ranking, or fitted results without validation and downgrade rules.
- Do not strengthen another subquestion to hide an uncovered deliverable.
