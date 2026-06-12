# A-Problem Pattern Library

## Purpose

Use this library during A-problem triage after reading the actual题面. It gives repeatable patterns, not final answers. Always derive deliverables, rules, data fields, and constraints from the current contest problem.

For 2024 bench-dragon examples and 2023 heliostat examples, read [a-problem-2024-casebank.md](a-problem-2024-casebank.md) as supporting evidence, not as a template to copy.

## No-Match / Novel Mechanism Fallback

If the current A problem does not clearly match one of the patterns below, do not force a nearest pattern. Use `new_mechanism_route` and mark the first route as `low-confidence` until the current problem creates its own mechanism map.

When using `new_mechanism_route`:

- 不得硬选主模式 just to make the workflow continue.
- 从交付物反推: list the exact required tables, figures, decisions, parameters, or prose answers before naming a model.
- Identify the real-world mechanism in one sentence: conservation, geometry, motion, material response, signal extraction, economics, queueing, control, policy, or another problem-specific mechanism.
- Build a baseline from the simplest defensible accounting, physical relation, simulation, or direct calculation.
- Define the first validation action before advanced modeling: unit closure, boundary case, back-substitution, brute-force small case, visual reconstruction, or scenario stress.
- Only after this check may a new primary pattern be written into the project notes. Do not present a 2023/2024 pattern as a universal future-year rule.

## Pattern 1: Geometric Motion and Collision

| Item | Guidance |
| --- | --- |
| 题面信号 | moving linked bodies, curves, collision, turning space, path width, speed limits, rigid geometry |
| 第一版基准模型 | coordinate frame + path equation + recursive positions + simple distance or overlap check |
| 高分主模型 | geometry-aware recurrence with explicit frame transforms, candidate collision pruning, exact or high-precision threshold search, and complete state tables |
| 必要结果表 | time/entity position table, speed table, first-constraint-hit table, parameter-search table, final feasible solution table |
| 必要验证 | boundary cases, visual state reconstruction, threshold crossing evidence, smaller brute-force check, speed/position consistency |
| 常见扣分坑 | no coordinate frame, incomplete result table, collision drawn but not quantified, missing units, "first collision" asserted without proof |
| 可生成创新点 | collision candidate pruning, dynamic search, curve-segment state classifier, speed scaling relation, threshold-crossing ledger |
| 适合图表 | path reconstruction, local collision zoom, distance-to-threshold curve, speed heatmap, parameter search curve |

## Pattern 2: Physical Field or Efficiency Decomposition

| Item | Guidance |
| --- | --- |
| 题面信号 | heat, light, force, flow, diffusion, energy, efficiency, power, concentration, pressure |
| 第一版基准模型 | conservation/balance equation + component efficiency factors + direct numerical evaluation |
| 高分主模型 | mechanism decomposition, coordinate transforms, shadow/blocking or loss modeling, time/space aggregation, and output-power registry |
| 必要结果表 | component efficiency table, scenario/time summary, object-level metric table, annual/monthly or spatial aggregation table |
| 必要验证 | unit check, extreme sun/angle/boundary case, component contribution comparison, sensitivity to key size/position parameters |
| 常见扣分坑 | efficiency factors named but not derived, hidden geometry, no component contribution table, visual heatmap without units |
| 可生成创新点 | loss decomposition, projection or ray-sampling correction, symmetry-based variable grouping, component ablation |
| 适合图表 | coordinate-frame diagram, component loss stacked bars, spatial heatmap, monthly/seasonal trend, parameter sensitivity curve |

## Pattern 3: High-Dimensional Engineering Optimization

| Item | Guidance |
| --- | --- |
| 题面信号 | many design variables, layout, allocation, sizing, siting, cost/benefit objective, hard feasibility constraints |
| 第一版基准模型 | fixed layout or uniform parameters + feasibility filter + objective evaluation |
| 高分主模型 | decomposition or dimension reduction, constrained search/solver, run record, baseline comparison, and feasibility diagnostics |
| 必要结果表 | design-variable table, objective and constraint table, solver/run record, baseline-vs-final comparison, parameter scan |
| 必要验证 | feasibility check, repeated seeds or deterministic restart, sensitivity to weights/bounds, local perturbation around final design |
| 常见扣分坑 | final design not completely tabulated, no solver status, no baseline denominator, black-box heuristic with no diagnostics |
| 可生成创新点 | symmetry/ring/layer grouping, coarse-to-fine search, adaptive feasible-region pruning, hybrid mechanism + heuristic loop |
| 适合图表 | design layout map, convergence curve, constraint violation curve, objective-vs-parameter curve, feasible-region plot |

## Pattern 4: Prediction to Decision

| Item | Guidance |
| --- | --- |
| 题面信号 | demand/risk/traffic/fault/price forecast followed by scheduling, allocation, routing, or policy |
| 第一版基准模型 | simple forecast + deterministic decision using predicted mean |
| 高分主模型 | uncertainty intervals or scenarios feed into robust/stochastic optimization with decision-impact evaluation |
| 必要结果表 | prediction accuracy table, scenario table, decision table, robustness comparison table |
| 必要验证 | leakage check, train/test split, forecast error propagation, worst-case or percentile performance |
| 常见扣分坑 | forecast and decision are separate chapters, only RMSE reported, no decision impact |
| 可生成创新点 | error-to-scenario conversion, robust constraint, risk-weighted objective, decision-aware metric |
| 适合图表 | prediction interval plot, scenario fan chart, decision sensitivity curve, robust-vs-deterministic comparison |

## Pattern 5: Evaluation, Ranking, and Policy Selection

| Item | Guidance |
| --- | --- |
| 题面信号 | ranking, risk level, comprehensive index, scheme comparison, priority order, policy recommendation |
| 第一版基准模型 | normalized indicators + equal weights + ranking |
| 高分主模型 | indicator provenance, redundancy check, weight sensitivity, rank stability, and actionable recommendation |
| 必要结果表 | indicator dictionary, standardized data table, weight table, ranking table, rank-stability table |
| 必要验证 | direction check, collinearity/redundancy, weight perturbation, top-k stability, expert or baseline comparison |
| 常见扣分坑 | AHP/TOPSIS name-dropping, indicator direction mismatch, ranking changes under tiny weight changes |
| 可生成创新点 | task-specific indicator, stability-weighted ranking, constraint-aware score, explainable top-k policy |
| 适合图表 | ranking bar chart, weight tornado chart, stability heatmap, radar chart only when dimensions are few and units are clear |

## Pattern 6: Discrete Event, Queue, and Reliability Simulation

| Item | Guidance |
| --- | --- |
| 题面信号 | arrival, waiting, service, congestion, repair, emergency response, failure, inventory state |
| 第一版基准模型 | state machine + baseline analytic or simple simulation |
| 高分主模型 | event logic, capacity/mutual-exclusion constraints, Monte Carlo or scenario simulation, optimization or policy comparison |
| 必要结果表 | event table, state-transition table, waiting/utilization table, scenario comparison, seed/run record |
| 必要验证 | multiple seeds, confidence interval, load stress test, conservation or final-state check |
| 常见扣分坑 | state transitions implied by prose, one simulation run, no seed, no steady-state or extreme-load check |
| 可生成创新点 | event-priority rule, adaptive dispatch policy, stress-test scenario design, state compression |
| 适合图表 | event timeline, queue length curve, utilization heatmap, confidence interval plot, scenario comparison table |

## Quick Pattern Selection

Use this output after reading the题面:

```text
match_confidence:
主模式:
辅模式:
if no clear match: new_mechanism_route
题面信号:
第一版基准:
高分主模型:
必须结果表:
必须验证:
潜在创新:
推荐图表:
当前阻塞:
```

If a pattern does not force a complete result table and validation action, the pattern was selected too vaguely.
