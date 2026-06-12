---
name: math-code
description: Use when 高教社杯/CUMCM 数学建模任务需要实现计算、复现结果、生成表图、验证求解器输出、更新登记表，或发现建模交接中不能凭空补全的缺口。
---

# 竞赛代码与复现

## 用途

Execute contest calculations from a completed modeling handoff and produce reproducible tables, figures, logs, and evidence records.

核心规则：代码服从模型。若交接中公式、单位、阈值、输入或预期输出不明确，报告缺口，不用貌似合理的值补齐。

国一候选门槛：代码产物必须保护题目贴合、建模洞察、证据可信、可复现、边界清楚；这是提交质量门槛，不承诺获奖。计算脚本不仅要跑出数值，还要保留输入、参数、单位、基准、验证状态和降级边界，使评委能复核核心结论。

硬门禁：代码可以发现证据，但没有建模交接、完整运行记录、验证状态和登记表行时，不能把新发现的数值提升为论文就绪结果。

## 运行前检查

Before editing or running code, confirm:

- active subproblem and modeling handoff section;
- input files, schemas, units, and row/page counts;
- objective, constraints, parameters, and tolerances;
- target output tables, figures, and registry rows;
- which outputs are paper-ready versus diagnostics;
- baseline scenario, denominator, and comparison direction for every claimed improvement or stress effect;
- validation tier and robustness plan from `math-model`, including tested ranges, stability metrics, and downgrade rules when applicable;
- stale files or obsolete runs that must not be reused.

If any preflight item is missing, either stop with the blocker protocol or explicitly label the run `diagnostic-only`.

## 执行流程

1. Map each formula/constraint to code.
2. Validate schemas, units, ranges, timestamps, ids, and missing values.
3. Fail loudly on missing required columns, impossible values, or inconsistent units.
4. Compute reproducibly with recorded parameters and seeds.
5. Export result tables under `outputs/tables/`.
6. Export figures under `outputs/figures/` with stable descriptive names.
7. Write logs under `logs/`.
8. Export robustness or sensitivity tables when the model marks a route `scenario-check` or `robustness-required`.
9. Update `run_record.csv`, `result_registry.csv`, and when figures are used, `figure_evidence.csv`.
10. Compare outputs against the modeling handoff before calling them paper-ready.

Diagnostic exception: schema checks, exploratory plots, baseline probes, and feasibility probes may run before the full handoff only when their purpose is to repair the model. Store or report them as diagnostic; do not update `result_registry.csv` as paper-ready.

## 仿真执行门禁

For simulation routes, code must make the simulator auditable rather than only producing a curve or animation. Require the `Simulation Plan` from `math-model` before paper-ready status; exploratory simulators without that plan stay `diagnostic-only`.

Minimum implementation records:

- deterministic or grid simulation: export step/grid size, state variable table, initial/boundary conditions, update equation id, residual or conservation check, and step-size/grid sensitivity when the conclusion depends on discretization;
- discrete-event simulation: export event log, state-transition summary, resource utilization, queue/wait metrics, horizon or warm-up rule, replications, seed policy, and confidence intervals for stochastic outputs;
- Monte Carlo or scenario simulation: export random variable table, distribution/source, seed list, sample size, quantile or confidence interval summary, convergence or sampling-error check, and scenario coverage table;
- agent-based simulation: export agent state schema, interaction or neighborhood rule, update order, policy/payoff parameters, aggregate metrics, calibration or plausibility checks, and multi-seed stability when behavior is stochastic;
- simulation + optimization: separate the simulator evaluation from the decision search. Export baseline policy, candidate decision table, evaluation budget, objective uncertainty, feasibility checks, and final selected policy with validation status.

Recommended output names:

- `qX_state_trajectory.csv`
- `qX_event_log.csv`
- `qX_simulation_summary.csv`
- `qX_replication_summary.csv`
- `qX_scenario_simulation.csv`
- `qX_discretization_sensitivity.csv`
- `qX_simulation_diagnostics.csv`

Never promote a simulation result from a single stochastic run, an unrecorded seed, an unchecked time step/grid, or a screenshot-only output. If analytic validation is impossible, use the strongest available baseline: limiting case, conservation law, direct accounting, historical observation, simplified queueing formula, or independent reimplementation of a small case.

## 数值稳定性硬检查

For optimization, simulation, parameter estimation, matrix computation, stochastic search, or any result sensitive to tolerances, create or update `numerical_diagnostics.csv` before promoting outputs to paper-ready.

Minimum columns:

```csv
diagnostic_id,run_id,subquestion,artifact,check_type,metric,value,threshold,status,severity,minimum_fix
```

Required checks when applicable:

- coefficient/input magnitude ranges and suspicious scaling ratios;
- matrix condition number or solver-reported conditioning indicator;
- solver status, gap, tolerance, infeasibility, unboundedness, interruption, and warning text;
- `printQuality` or equivalent solver quality report when supported;
- constraint violation counts and maximum violation;
- objective and feasibility changes under a tolerance sweep;
- multiple seed/restart summary when randomness or heuristics affects a paper claim;
- baseline comparison showing whether the advanced route improves the actual contest deliverable.

论文就绪状态要求没有开放的 P0/P1 数值诊断。若诊断未知、只有警告或不稳定，结果只能保持 `diagnostic-only`，或把阻塞项返回 `math-hub`。

## 鲁棒性证据门禁

Do not apply the same robustness burden to every subquestion. Use the model handoff's validation tier:

- `direct-check`: report balance residuals, unit checks, formula back-substitution, and boundary sanity. A full sensitivity table is not required unless the paper claims stability under changes.
- `scenario-check`: compute all required cases and export a spread, ranking, pass/fail, or scenario-comparison table. If a scenario is missing, keep the conclusion candidate.
- `robustness-required`: export a robustness table before paper-ready status. Include tested range, baseline, stress case, stability metric, criterion, status, and risk note.
- `diagnostic-only`: write diagnostics, but do not update final claims as paper-ready from those rows.

Recommended table names:

- `qX_sensitivity_summary.csv`
- `qX_robustness_summary.csv`
- `qX_stress_scenarios.csv`
- `qX_ranking_stability.csv`
- `qX_solver_diagnostics.csv`

When a robustness check fails, downgrade the affected registry rows to `candidate` or keep them out of `result_registry.csv`; do not hide the failure with stronger prose.

## 图表生产门禁

Generate a paper figure package, not a pile of plots. Before plotting more than one candidate figure, create a compact figure plan table such as `outputs/tables/q1_figure_plan.csv` with:

- `figure_id`
- `figure_path`
- `paper_role`: `claim`, `mechanism`, `robustness`, `diagnostic`, or `appendix`
- `claim_id`
- `source_table`
- `plot_family`
- `plot_type`
- `why_this_plot`
- `caption_draft`
- `post_figure_conclusion_draft`
- `risk_note`

Use these defaults unless the modeling handoff says otherwise:

- **Claim figure**: answers the subproblem result in one high-signal visual.
- **Mechanism figure**: explains why the result occurs, such as schedules, flows, states, or allocation paths.
- **Robustness figure**: shows sensitivity, stress tests, parameter ranges, or ranking stability.
- **Diagnostic figure**: checks feasibility, constraints, convergence, missingness, or solver behavior; appendix by default.

For scenario comparison, prefer a relative-to-baseline heatmap or indexed change plot as the main-body figure. Keep raw absolute multi-panel bar charts as diagnostics unless each panel is readable and supports one shared claim.

Choose plot types by claim shape, not by visual novelty. Use the figure evidence rules reference for the plot routing library. Do not use word-cloud figures. Use 3D, radar, pie, or Sankey figures only when the data structure genuinely needs them and the nearby conclusion sentence becomes clearer.

When a requested plot matches a common contest chart family, adapt the relevant `math-figure/assets/chart-templates/` script instead of rebuilding the plotting pattern from scratch. Still update the source table, units, caption, post-figure conclusion, risk note, and `figure_evidence.csv` row for the active problem.

Main-body figures must be compact, readable, and tied to one claim, with baseline/threshold/scenario/unit visible. Diagnostic or appendix figures may be denser, but must not be mislabeled as strict feasibility or final evidence.

Do not force every generated figure into the paper. For each candidate paper figure, write or update `figure_evidence.csv` with:

- `figure_id`
- `paper_role`
- `figure_path`
- `claim_id`
- `figure_type`
- `plot_family`
- `plot_type`
- `why_this_plot`
- `source_table`
- `source_script`
- `run_id`
- `caption`
- `post_figure_conclusion`
- `risk_note`
- `validation_status`

Use stable semantic filenames such as `q2_pareto_frontier.png`, not `1.png`, `2.png`, or hash-like names in final paper source.

### 论文就绪图检查

Before marking a figure `paper_ready`, inspect the saved image and fix or demote it if any of these occur:

- title, subtitle, legend, labels, annotations, or tick text overlap;
- units, baseline, threshold, scenario, or comparison denominator are missing;
- numeric formats are inconsistent within the same figure;
- axis labels are too long to read, especially scenario names;
- a value table has been redrawn as a picture without showing a trend, mechanism, or tradeoff;
- debug notes, file names, CSV provenance comments, or uncertainty caveats are printed inside the plot canvas;
- visual differences are hidden by unsuitable scales when the claim is about relative change.

For paper figures, put source/provenance, feasibility caveats, and diagnostic caveats in `figure_evidence.csv`, the caption, or nearby prose, not inside the plotted panel.

## 优化诊断

For MILP, nonlinear optimization, simulation, heuristic, or stochastic search, export enough evidence to reproduce and judge the run:

- search range, step strategy, feasibility filters, baseline policy;
- seed, hyperparameters, objective definition, penalties, stopping rule;
- solver status, gap/tolerance, runtime, warnings;
- numerical diagnostics row ids, including condition number, tolerance sweep, and warning status when applicable;
- best objective history and constraint-violation history when iterative;
- multiple-seed or restart summary when randomness affects the result;
- final feasibility flag and violated constraint count.

## 登记表标准

- `run_record.csv`: one row per reproducible formal run.
- `result_registry.csv`: one row per paper-usable result, not vague prose.
- `figure_evidence.csv`: one row per figure that supports a claim.
- `claim_ledger.csv`: writer/abstract-owned, but code should provide evidence ids and exact values.

Only mark `paper_ready` when the source run exists, completed successfully, and the output matches the model handoff.

Never mark a result paper-ready because it "looks reasonable". Paper-ready requires a reproducible command, input files, parameters/seeds, output path, and validation check.

## AI 披露边界

Do not write AI-use disclosure text, prompt logs, model names, or AI-assistance notes into code comments, generated result tables, figure canvases, or code-facing output files. If AI-use disclosure is required, report the need back to `math-hub` or `math-compliance` so it can be recorded in the final submission checklist or separate disclosure file.

## 输出约定

返回：

- files changed or created;
- command(s) run;
- generated tables and figures;
- key numeric results with source paths;
- feasibility/convergence/robustness evidence, including validation tier and table paths;
- warnings, missing data, and unresolved modeling issues;
- whether outputs are `paper_ready`, `checked`, `computed`, or only diagnostic.
- Return to hub: math-hub.

## 红线

Stop and report a blocker when:

- the script silently fills missing units, thresholds, columns, or parameters;
- the solver returns infeasible, interrupted, warning-only, or unknown status but the output is described as final;
- `numerical_diagnostics.csv` has open P0/P1 rows or no row for a tolerance-sensitive claim;
- a `scenario-check` or `robustness-required` model has no robustness table or downgrade decision;
- random or heuristic results lack seed/restart evidence when they affect a claim;
- a figure is saved without a source table, claim id, caption, post-figure conclusion, and validation status;
- the final numeric value appears only in a plot or console output, not in a table or registry.

## 阻塞协议

```text
Incomplete modeling part:
Why code cannot proceed safely:
Smallest evidence check or model fix:
Suggested owner:
Return to hub: math-hub
```
