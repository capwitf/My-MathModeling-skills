# Robustness Protocol

Use this reference when a modeling route needs a validation tier or robustness plan. Keep the plan proportional: direct accounting should not receive a full sensitivity study, and fragile optimization or ranking claims should not pass with only a balance check.

## Tier Selection

| Situation | Minimum tier | Required evidence |
| --- | --- | --- |
| Direct formula accounting, deterministic unit conversion, or data transcription | `direct-check` | unit closure, formula back-substitution, balance residuals, boundary sanity |
| Required answer spans several given scenarios, regions, periods, or cases | `scenario-check` | all-case coverage, spread/ranking/pass-fail table, representative figure when useful |
| Main claim depends on uncertain parameters, weights, thresholds, calibrated values, or selected assumptions | `robustness-required` | sensitivity/stress table, tested range, stability criterion, downgrade rule |
| Solver, heuristic, stochastic, or tolerance-sensitive result supports a claim | `robustness-required` | tolerance or seed/restart evidence, solver gap/status, constraint violation summary |
| Exploratory probe used only to understand risk | `diagnostic-only` | diagnostic table/log, explicit ban from abstract and conclusion |

## Route Patterns

| Model route | Robustness checks to design |
| --- | --- |
| Linear/MILP/nonlinear optimization | constraint residuals, solver status/gap, tolerance stress, key cost/capacity/bound perturbation, baseline comparison |
| Heuristic or stochastic search | fixed seed record, multi-seed/restart distribution, convergence trace, best-vs-baseline comparison |
| Ranking, evaluation, TOPSIS, AHP, entropy weights | weight perturbation, indicator deletion, rank flip count, threshold margin |
| Prediction feeding a decision | train/validation separation, forecast error interval, error-to-scenario propagation, decision-impact table |
| Geometry, physics, or simulation | step-size or grid sensitivity, boundary/extreme cases, key size/angle/position perturbation |
| Monte Carlo convergence | pilot run variance, confidence half-width or relative half-width, seed-block or batch-means stability, replication increase rule |
| Calibrated simulation | parameter fit table, calibration error, holdout or back-test, decision impact of fitted-parameter uncertainty |
| Policy or system impact analysis | scale/penetration stress, synchronized vs diversified scenario, peak/ramp/shortage pressure metrics |
| Pure explanation or proof-style subquestion | boundary counterexample search, assumption-loss statement, formula back-substitution |

## Output Contract

Name robustness outputs semantically:

- `qX_sensitivity_summary.csv`
- `qX_robustness_summary.csv`
- `qX_stress_scenarios.csv`
- `qX_ranking_stability.csv`
- `qX_solver_diagnostics.csv`

Each table should include:

```csv
run_id,subquestion,check_id,baseline_case,stress_case,parameter_or_assumption,tested_range,metric,baseline_value,stress_value,unit,stability_criterion,status,validation_status,risk_note
```

Use `paper_role=robustness` only when the check is broad enough to support a paper claim. Narrow probes stay `diagnostic-only`.
