---
name: math-model
description: Use when 高教社杯/CUMCM 数学建模任务需要变量、假设、公式、约束、算法、验证设计、鲁棒性规划、灵敏度分析、结果 schema，或基于题面和本地证据的代码交接。
---

# 竞赛建模

## 用途

Turn contest requirements and verified local evidence into a model that code and paper writers can execute without guessing.

核心规则：区分已证明、已计算、已假设、缺失、诊断性和不可识别的内容。不要让论文措辞掩盖无支撑的建模步骤。

国一候选门槛：建模输出必须同时显示题目贴合、建模洞察、证据可信、可复现、边界清楚；这是提交质量门槛，不承诺获奖。只列方法名、只给流程图、只把变量写全但没有机制/约束/验证，不足以进入后续代码或正文。

硬门禁：模型必须把具体分问交付物映射到变量、目标、约束、单位、结果 schema 和验证动作后，才允许进入代码、摘要或最终写作。

## 事实源规则

- Use the current problem statement, official attachments, user-provided constraints, and verified local artifacts first.
- Treat examples, excellent papers, screenshots, or previous-phase reports as references unless the user explicitly says they are source material.
- Do not convert a candidate value, screenshot estimate, prior answer, or demo output into a final parameter.
- If evidence conflicts, name the conflict and block the affected claim until resolved.

## 评委可见性标准

For each subproblem, present the modeling answer in this order:

1. Task target: exact required output.
2. Data and parameters: source path, unit, scope, and any missing fields.
3. Variables and domains: decision, state, auxiliary, binary, slack.
4. Objective: mathematical expression plus physical/economic meaning.
5. Constraints: balance laws, physical limits, logic constraints, boundary conditions.
6. Algorithm: solver/search/simulation route and why it fits the problem.
7. Result schema: tables and figures code must output.
8. Verification: feasibility, boundary checks, sensitivity, robustness, ablation.
9. Paper conclusion: one short answer with numbers and evidence ids.

If any item is unknown, mark it as `blocked` or `diagnostic-only`; do not skip the item.

## 主路线锁定

For A-problem work, lock one main route before adding advanced methods:

- State the main physical, geometric, operational, or optimization mechanism in one sentence.
- Build a simple baseline or reference scheme before claiming improvement.
- Keep secondary routes subordinate; they may support validation, comparison, or sensitivity, but must not create a second half-finished paper.
- Reject method-name-first plans such as "use neural network", "use genetic algorithm", or "use TOPSIS" until the variables, objective, constraints, and result table are known.
- Require a complete result table schema before sending work to `math-code`.

## Model Family Triage

Do not choose MILP/MIP merely because the paper needs variables, objectives, and constraints. First identify the subproblem mechanism, then choose the model family that expresses that mechanism with the least unsupported machinery.

Use this triage before naming the model:

- `discrete decision table`: choose MILP/network flow/DP/heuristic when the task requires route, schedule, assignment, location, loading, capacity, or time-window decisions.
- `structured discrete optimization`: prefer network flow/DP before generic MILP when the problem has clear path, matching, stage transition, or inventory-state structure; use MILP when logic constraints or coupled binary decisions need it.
- `continuous resource allocation`: choose LP/QP/convex optimization/nonlinear programming when decisions are mainly continuous quantities such as flow, power, speed, inventory, proportion, price, or resource level.
- `geometry or physics`: choose derivation, direct numerical evaluation, or simulation according to the mechanism; use simulation only when shape, motion, visibility, force, conservation, or spatial relation must be evaluated across states, time, space, or scenarios.
- `time evolution`: choose dynamic model/state-space/time series when the answer depends on state transition, trend, lag, recurrence, or temporal forecast.
- `ranking or evaluation`: choose indicator system + sensitivity when the task asks for scoring, ranking, classification, risk grade, or multi-criteria comparison.
- `uncertainty`: choose scenario/robust/stochastic analysis when parameters, demand, environment, or measurement noise drives the conclusion.
- `image or spatial data`: choose feature extraction + geometric/physical mapping before optimization or evaluation.
- `data-scarce but mechanism-strong`: prefer mechanism equations, accounting identities, geometry, or conservation checks over learning models.

Use MILP/MIP only when the subproblem has discrete decisions, the important constraints/objectives are linear or safely linearizable, and the paper needs an auditable decision or allocation output. Use MILP/MIP as a modeling family, not as a generic wrapper for any model with variables and constraints. If one condition fails, justify another family or keep MILP as a diagnostic/baseline comparison rather than the main model.

## Simulation Route Fitness

Simulation is neither preferred nor downgraded by default. Choose it only when it is the best-fitting route for the subproblem mechanism and required deliverable: state evolution, event timing, spatial/physical process, queueing, multi-agent interaction, uncertainty propagation, or policy performance under scenarios.

If the subproblem can be answered more directly by formula, accounting identity, geometry derivation, parameter estimation, evaluation/ranking, or an auditable optimization decision without simulating a process, keep simulation as validation, scenario exploration, or diagnostic evidence. Do not demote mechanism-driven simulation to a decorative figure, and do not wrap it in MILP unless the contest deliverable is an auditable decision table with valid linear structure.

Choose the simulation family by mechanism:

- `deterministic time-step / grid simulation`: for ODE/PDE, conservation, diffusion, motion, heat, flow, energy, inventory, or spatial field evolution. Require state variables, initial/boundary conditions, discretization rule, step/grid size, stability or residual check, and conservation/balance closure.
- `discrete-event simulation`: for arrival, queue, service, congestion, breakdown, repair, evacuation, emergency response, or reliability. Require event types, event clock, state transition table, resource rules, arrival/service assumptions, warm-up or horizon rule, replications, and confidence intervals when random.
- `Monte Carlo / scenario simulation`: for random demand, measurement error, environment, failure, or parameter uncertainty. Require random variables, distribution/source, sample size, seed policy, confidence interval or quantile output, and scenario coverage.
- `agent-based / game simulation`: for many actors, competition, cooperation, learning, policy response, or local interaction. Require agent states, action set, interaction graph or neighborhood, update order, payoff/utility or rule source, calibration or plausibility check, and aggregate metrics.
- `simulation + optimization`: use simulation to evaluate policies or scenarios and optimization/search to choose decisions. Require a shared input parameter table, baseline policy, fixed evaluation budget, stochastic uncertainty on objective values, and a decision table whose feasibility has been checked outside the simulator.

Before code handoff, publish a compact `Simulation Plan` when any subproblem uses simulation:

- simulation purpose: prediction, mechanism explanation, policy evaluation, feasibility screening, uncertainty propagation, or validation;
- state variables, units, domains, and update equations or event rules;
- time step, grid size, event horizon, stopping rule, warm-up rule, sample size, replications, seeds, and solver/search settings when applicable;
- initialization and boundary conditions, including what is measured, assumed, or calibrated;
- invariant checks: mass, count, budget, probability, capacity, energy, monotonicity, final-state feasibility, or back-substitution;
- baseline or analytic reference used to catch simulator mistakes;
- output schemas: time/state trajectory table, event log, scenario summary, replication summary, parameter table, and paper figure roles;
- downgrade rule: what becomes diagnostic-only if step-size sensitivity, repeated seeds, residuals, or baseline comparison fail.

Paper-facing simulation claims must report a mechanism and evidence, not just "we simulated". A simulation figure is main-body ready only when it is tied to a state variable, scenario, baseline, unit, and post-figure conclusion; animations, raw traces, and single-run screenshots are diagnostic unless they support a specific required answer.

## 鲁棒性计划门禁

Every subquestion needs a validation tier, but not every subquestion needs a full robustness study.

Use this tiering:

- `direct-check`: direct accounting, transcription, or deterministic formula substitution. Require unit closure, balance checks, and boundary or back-substitution checks. Do not force parameter scans.
- `scenario-check`: the result depends on multiple given cases or scenarios. Require coverage across the required scenarios and a table or figure showing spread, rank, or pass/fail variation.
- `robustness-required`: the conclusion depends on selected parameters, weights, thresholds, fitted values, solver tolerances, stochastic search, or a fragile modeling assumption. Require sensitivity, stress, multi-seed, tolerance, or ranking-stability evidence before paper-ready wording.
- `diagnostic-only`: the check probes uncertainty but is too narrow to support final claims.

Before code handoff, include a compact `Robustness Plan`:

- fragile inputs, parameters, weights, thresholds, assumptions, solver settings, or scenario choices;
- perturbation or stress range and why that range is defensible;
- stability metric, such as objective change, feasibility rate, rank flip, threshold margin, or sign/range preservation;
- table and figure outputs, with `paper_role=robustness` only when the evidence can support paper wording;
- downgrade rule: what result becomes candidate or diagnostic if the check fails.

For route-specific patterns, read `references/robustness-protocol.md`.

## 覆盖与单位闭合门禁

Before handing a model to code, abstract, or LaTeX, publish a compact coverage check:

- `subquestions_covered`: each required subquestion mapped to a model section, result schema, validation action, and paper-facing conclusion status;
- `deliverables_missing`: every required table, figure, formula, route, ranking, schedule, appendix item, or prose answer still absent;
- variable unit closure: each decision, state, parameter, objective term, constraint term, and reported metric has a unit or is explicitly dimensionless;
- notation closure: new symbols are added to the symbol table with type, domain, first use, and source;
- assumption closure: each assumption names the affected constraint or realism loss and the validation action that keeps the conclusion bounded.
- robustness closure: each subquestion has a validation tier, and `robustness-required` routes have a stress or sensitivity plan with output schemas.

If any subquestion is uncovered, do not compensate by strengthening another section. Keep the model in `blocked` or `diagnostic-only` status and return the smallest missing deliverable to `math-hub`.

## 可行性措辞门禁

Classify every reported solution before it reaches the paper:

- `strict feasible solution`: all hard constraints pass within tolerance.
- `relaxed diagnostic solution`: slack/soft constraints are used to diagnose a gap.
- `candidate solution`: computed but not fully checked.
- `not identifiable`: current evidence cannot determine the value.
- `unavoidable gap`: original requirements cannot be strictly satisfied under the data.

Never write a relaxed diagnostic as strict feasibility.

If a hard constraint is violated, the answer is not a strict feasible solution even when the objective value is good.

## 图表计划

For every result section, specify:

- exact result table schema and primary key;
- which figure proves which claim;
- whether the figure belongs in the main body or appendix;
- required units, scenario labels, baseline, threshold, and uncertainty/error information;
- `post_figure_conclusion` and `risk_note` text for `figure_evidence.csv`.

Main-body figures should be few and high-signal. Dense diagnostic plots, solver traces, large multi-panel scans, and raw-data checks usually belong in appendices unless they carry the central claim.

## 代码交接约定

The handoff must include:

- input files, required columns, units, and preprocessing rules;
- formulas and constraints in LaTeX or precise pseudocode;
- parameter values and source for each value;
- output table names, figure names, and registry updates;
- validation tolerances and failure conditions;
- robustness table/figure schemas, stability metrics, tested ranges, and downgrade rules when the validation tier is `scenario-check` or `robustness-required`;
- values that must remain `NA`, empty, diagnostic, or not identifiable;
- stale runs or obsolete assumptions that code must not reuse.

The handoff is blocked if code would need to invent a parameter, threshold, unit conversion, solver tolerance, output schema, or feasibility label.

## 核验交接

Before a route is treated as paper-ready, provide enough structure for `math-verifier` to check it:

- equations with units and domains for every term;
- hard constraints, relaxed constraints, and feasibility tolerances;
- baseline, boundary, and extreme cases that should be back-substituted;
- robustness or scenario checks that should preserve the claimed sign, ranking, feasibility class, threshold margin, or decision recommendation;
- conservation, balance, probability, count, or budget laws that should close;
- assumptions and the exact realism or constraint loss they introduce;
- result schemas that expose units, scenarios, baselines, and validation status.

If these items are missing, keep the route inside `math-model` or mark it diagnostic-only instead of handing final language to writing skills.

## 红线

Stop and repair the model when:

- the objective optimizes something different from the subquestion asks;
- a symbol has no unit, domain, or first-use definition;
- an assumption removes a real constraint without naming the loss of realism;
- a validation plan says only "compare results" without a baseline, boundary case, sensitivity check, or feasibility check;
- a main result depends on parameters, scenarios, solver choices, weights, or fragile assumptions but has no robustness plan;
- the model claims stability, robustness, or superiority without a tested range, baseline, denominator, and downgrade rule;
- the paper conclusion is written before the result schema and evidence ids exist.

## 论文表达约定

- Convert debugging history into modeling rationale, not narrative clutter.
- Define symbols near first use and keep the symbol table consistent.
- Put exact values in tables; use figures for trends, mechanisms, and tradeoffs.
- Each figure/table needs a conclusion sentence explaining what it proves.
- Improvements require a baseline, denominator, scenario, and evidence source.
- Robustness claims require stress tests, sensitivity ranges, or multiple-run evidence.

## 阻塞协议

```text
Blocker:
Affected claim/output:
Evidence currently available:
Smallest next check:
Owner:
```
