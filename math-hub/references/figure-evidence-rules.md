# Figure Evidence Rules

## Purpose

A contest figure must prove a claim. It is not decoration, page filling, or a substitute for missing tables.

Use this reference when planning, generating, selecting, writing, reviewing, or typesetting figures and tables.

## Main-Body Figure Triage

Before a figure enters the main body, classify it:

| Tier | Use | Main-body rule |
| --- | --- | --- |
| Claim figure | proves the answer to a subproblem | keep in main body |
| Mechanism figure | explains model logic, workflow, or allocation process | keep if it prevents long prose |
| Evidence bridge | links raw data to model inputs | keep only when it justifies a key scenario/constraint |
| Diagnostic figure | proves residuals, solver checks, feasibility checks, or data quality | appendix by default |
| Exploratory figure | helped analysis but is not needed for the final argument | exclude or appendix |

If a figure cannot be followed by one concrete conclusion sentence, it is not main-body ready.

## What Each Figure Type Proves

| Figure type | Best use | Required nearby evidence |
| --- | --- | --- |
| mechanism diagram | model logic, state/event chain, allocation process | variables, inputs, outputs, where equations enter |
| time series | trend, stability, event timing, threshold crossing | time unit, marked event/threshold, key numeric result |
| heatmap/spatial field | heterogeneity, hotspot, boundary region | colorbar unit, axes, scenario/time |
| convergence curve | solver/search stability | objective, seed/run id, stopping rule, feasible-best curve |
| sensitivity curve | parameter influence or robustness | baseline, tested range, sign/rank change |
| comparison bar/table | component contribution or method comparison | baseline, denominator, same scenario |
| Pareto/frontier plot | tradeoff and selected policy | feasible set, selected point, budget/constraint boundary |
| residual/error plot | numerical accuracy or fit quality | metric, unit, tolerance, unacceptable region |
| distribution plot | data quality or uncertainty | sample size, unit/bin rule, outlier handling |

## Default Paper Figure Package

For each solved subproblem, prefer a small package over a broad gallery:

| Role | Typical figure | Main-body rule |
| --- | --- | --- |
| Result/claim | relative change heatmap, ranking chart, Pareto/frontier plot | include if it directly answers the subproblem |
| Mechanism | dispatch time series, flow/allocation diagram, state trajectory | include if it explains the result better than prose |
| Robustness | sensitivity curve, stress-test heatmap, tornado/ranking-stability plot | include when the conclusion depends on parameter or scenario stability |
| Diagnostic | constraint binding, residual/error, convergence, missingness, raw ledger scan | appendix unless the task explicitly asks for validation evidence |

For multi-scenario, multi-metric comparisons, the main figure should usually show relative change from a named baseline. Absolute-value bar panels are acceptable as appendix or diagnostics, but they are weak main-body figures when values share different scales, tiny differences, or repeated constraint-boundary values.

## Plot Type Routing Library

Choose plot type from the claim, data geometry, and reader task:

| Claim shape | Prefer | Use carefully / demote / forbid |
| --- | --- | --- |
| time trend, schedule, sequence, threshold crossing | line, stepped line, area, marked line, local zoom | 3D line only when the third axis is a real variable |
| scenario or method comparison | horizontal bar, grouped bar, positive-negative bar, relative-change heatmap | raw multi-panel absolute bars when labels or scales crowd |
| component contribution or total decomposition | stacked bar, horizontal stacked bar, stacked area, Sankey flow | pie only for one whole with few categories |
| distribution, spread, uncertainty, outliers | boxplot, ridge/density plot, histogram with clear bins | decorative fills without sample size or unit |
| pairwise relation or clustering | scatter, grouped scatter, bubble/correlation heatmap | polar scatter only for cyclic or angular variables |
| spatial/grid/surface response | heatmap, pcolor, contour, surface/mesh when a real 2D domain exists | 3D surface/mesh for ordinary tables |
| network, path, dependency, transfer | directed graph, Sankey chart, route map | generic flowcharts with no model variables |
| multi-objective tradeoff | Pareto/frontier plot, selected-policy marker, normalized radar for few metrics | radar with raw incomparable units or mixed benefit/cost directions |
| qualitative text frequency | ranked term bar or compact frequency table | forbidden: word cloud |

Treat flashy plot families as evidence tools, not decoration. 3D bars, 3D pies, and ornate polar figures are appendix-only unless they make a data relationship clearer than a 2D figure.

## Information Density Standard

A paper-ready figure should satisfy:

- one figure answers one claim;
- caption names object, scenario, metric, and what to notice;
- axes, legends, and colorbars have units or explicitly say dimensionless;
- baseline, threshold, selected solution, and constraints are marked when relevant;
- dense figures have a compact companion table;
- text after the figure states the conclusion in one sentence with a number or named qualitative proof;
- risk/boundary wording is nearby when the claim depends on scenario assumptions.

## Visual Readiness Check

Before a figure is labeled `paper_ready`, inspect the saved image at paper zoom and reject or fix:

- overlapping title/subtitle/axes/legend/annotations;
- unreadable scenario labels or long labels that should be abbreviated;
- inconsistent numeric formatting, such as mixed scientific notation and comma formats in one figure;
- missing units, denominator, baseline, threshold, scenario, or selected solution marker;
- debug/provenance text printed in the plot area instead of the evidence ledger or caption;
- decorative complexity that does not add a claim, mechanism, tradeoff, or robustness check.

## Size And Layout Rules

- Default single main-body figure width: `0.78\textwidth` to `0.86\textwidth`.
- Use full width only for central Pareto/frontier plots, mechanism diagrams, or figures that carry the main claim.
- A 2x2 panel is allowed only when all four panels answer one shared claim and remain readable at 100 percent PDF zoom.
- If one figure consumes most of a page, it must carry a main conclusion, not just diagnostics.
- Prefer appendix for raw traces, full scans, solver histories, or dense validation plots.

## `figure_evidence.csv`

Recommended fields:

```csv
figure_id,problem_id,claim_id,paper_role,figure_path,figure_type,plot_family,plot_type,why_this_plot,scenario,metric,unit,source_table,source_script,run_id,baseline_or_threshold,uncertainty_or_error,constraint_status,caption,post_figure_conclusion,validation_status,risk_note,data_source,notes
```

`validation_status` values:

- `planned`
- `generated`
- `checked`
- `paper_ready`
- `blocked`

`paper_ready` requires:

- existing figure path;
- existing source table/script or checked non-computational source;
- existing run id when computed;
- caption;
- post-figure conclusion;
- risk note when the claim has a scenario, relaxation, diagnostic, or uncertainty boundary.

## Caption Pattern

Use this compact pattern:

```text
[Object] under [scenario/parameter range]: [metric/trend/tradeoff] and [what to notice]
```

Examples:

- `Budget-feasible Pareto frontier for heterogeneous resource expansion`
- `Storage state rollover under compound stress in the rolling horizon`
- `Cost-fairness tradeoff under compensation policy scenarios`

## Post-Figure Conclusion Pattern

Write one sentence after the figure:

```text
Figure X shows that under [scenario], [metric] changes from [baseline] to [new value] [unit], so [claim].
```

For qualitative mechanism figures:

```text
Figure X decomposes the mechanism into [named stages], which maps directly to equations [ids] and output table [table].
```

If this sentence cannot be written, demote the figure to appendix or remove it.

## Forbidden Figures

Do not include:

- no-unit axes;
- tiny unreadable multi-panel plots;
- repeated table-as-picture with no extra insight;
- generic textbook flowcharts;
- word clouds;
- heatmaps without colorbar units;
- sensitivity plots without baseline/tested range;
- result figures with no scenario/metric in the caption;
- figures whose data cannot be traced to a source table or run.
