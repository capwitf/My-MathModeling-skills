---
name: math-figure
description: Use when 高教社杯/CUMCM 数学建模论文需要规划、选择、审查或修复图、图表、表格转图、图注、图像证据行、正文放置、附录降级或图后结论。
---

# 图表证据

## 用途

Gate contest figures as evidence, not decoration. A figure earns main-body space only when it proves a claim, explains a mechanism, or supports robustness better than prose or a table.

国一候选门槛：图表必须服务题目贴合、建模洞察、证据可信、可复现、边界清楚；这是提交质量门槛，不承诺获奖。主图不仅要好看，还要能证明一个结论、解释一个机制或支撑一个鲁棒性边界；否则降为附录或诊断图。

## 先选证据再画图

When the task is "what should I generate?", start from the claim and the smallest evidence that proves it. Use [references/selection-guide.md](references/selection-guide.md) for the full routing table.

When the request asks for a common contest chart or when code needs a stable plotting starting point, use [references/chart-template-index.md](references/chart-template-index.md) and adapt the matching script from `assets/chart-templates/`.

When the user provides only a result table, CSV, or Excel output and no exact figure claim, first run or mentally emulate a light result-table profile with `scripts/profile_result_table.py`: column types, missingness, numeric ranges, category counts, scenario columns, and candidate comparison axes. Then use [references/contest-chart-selection.md](references/contest-chart-selection.md) to choose the smallest contest evidence.

Before accepting or regenerating a figure package, check [references/contest-figure-pitfalls.md](references/contest-figure-pitfalls.md). For saved figures, use `scripts/check_contest_figure.py` and [references/visual-readiness-loop.md](references/visual-readiness-loop.md) for format, final-size, Chinese glyph, minus sign, overlap, legend, grayscale, and caption-readiness issues.

Rule of thumb:

- exact values or lookup answers -> table first;
- trend, threshold, or sequence -> line, stepped line, or local zoom;
- comparison, ranking, or scenario delta -> bar, grouped bar, or relative-change heatmap;
- mechanism, allocation, or state flow -> mechanism diagram, flow diagram, or state trajectory;
- robustness or sensitivity -> sensitivity curve, tornado plot, or stress heatmap;
- tradeoff or selected policy -> Pareto/frontier plot;
- feasibility or solver health -> diagnostic plot, usually appendix.

If you cannot write a one-sentence post-figure conclusion before plotting, do not generate the figure yet.

模板规则：图表模板是可复用绘图资产，不是证据。生成后的图仍然需要源表、计算型结果的 run id、图像证据行、图注、图后结论和风险说明。

SciPilot-style lesson to keep: profile -> choose -> render -> inspect -> revise. Adapt it to contest evidence, not journal submission ritual. Do not import Nature/Science/IEEE-specific burdens unless the user is actually preparing a journal figure.

核心规则：每张论文图都必须有结论 id、来源、图注、图后结论、风险说明和验证状态。

硬门禁：图像的 `figure_evidence.csv` 行不是 `validation_status=paper_ready` 时，不能支撑摘要、结论或最终答案措辞。

返回规则：本技能只把发现返回 `math-hub`。可以建议修复面，但不能直接路由、派发或调用另一个技能。

## 图像证据约定

For each candidate figure, require:

- `figure_id` and stable semantic filename;
- `claim_id` and exact subquestion deliverable;
- paper role: `claim`, `mechanism`, `robustness`, `diagnostic`, or `appendix`;
- source table, source script, checked non-computational source, and run id when computed;
- metric, unit, scenario, baseline or threshold, and uncertainty/error where relevant;
- caption naming object, scenario, metric, and what to notice;
- post-figure conclusion stating what the figure proves;
- risk note naming assumptions, relaxation, missingness, uncertainty, or scope limits;
- validation status: `planned`, `generated`, `checked`, `paper_ready`, or `blocked`.

Unknown source, unit, scenario, baseline, or validation status means the figure is not paper-ready.

## 正文图门禁

Keep a figure in the main body only when it satisfies one of these roles:

| Role | Main-body test |
| --- | --- |
| Claim | Directly answers a subquestion or carries a final result |
| Mechanism | Makes the model structure, state transition, allocation, route, or tradeoff clearer than prose |
| Robustness | Shows sensitivity, stress, ranking stability, or boundary behavior needed to trust the claim |

Demote to appendix or remove:

- diagnostic solver traces, missingness checks, residual scans, raw data galleries, and convergence plots unless they are the central validation;
- repeated table-as-picture figures that add no pattern or mechanism;
- dense multi-panel figures where no single conclusion sentence survives;
- decorative 3D, radar, pie, Sankey, or polar plots unless the data geometry genuinely needs them;
- any plot whose evidence is weaker than a small table.

## 图表数量与覆盖门禁

Before accepting a figure package, report `figure_count` and `figure_count_by_subquestion`:

- count only figures intended for the main body separately from appendix/diagnostic figures;
- tag each figure with a `figure_topic_tag` such as `claim`, `mechanism`, `robustness`, `feasibility`, or `diagnostic`;
- check whether every required subquestion has enough visual or tabular evidence to support its main claim;
- list `missing_figure_support` only when a figure is actually needed to prove a trend, mechanism, robustness, or feasibility point better than a table;
- demote repeated, decorative, or low-evidence figures even if the code generated them successfully.

If a subquestion is uncovered, return the missing support to `math-hub`; do not inflate `figure_count` with diagnostic plots.

## 图注与结论门禁

Use this caption pattern:

```text
[Object] under [scenario/parameter range]: [metric/trend/tradeoff] and [what to notice]
```

Use this post-figure conclusion pattern:

```text
Figure X shows that under [scenario], [metric] changes from [baseline] to [new value] [unit], so [claim].
```

For mechanism figures:

```text
Figure X decomposes [mechanism] into [stages], matching equations [ids] and output table [table].
```

If the conclusion sentence cannot be written with a claim, source, and boundary, the figure is not main-body ready.

## 视觉就绪门禁

Inspect saved figures before labeling them paper-ready. Block or demote when:

- title, subtitle, legend, tick labels, annotations, or colorbars overlap;
- labels are unreadable at normal PDF zoom;
- units, baseline, threshold, scenario, denominator, or selected solution marker are missing;
- numeric formatting is inconsistent;
- debug file names, provenance notes, or caveats are printed inside the plot canvas;
- color alone carries a result that a grayscale or color-weak reader cannot recover;
- visual novelty hides a simpler table, comparison, or boundary check.

For LaTeX placement, default single main-body evidence figures to about `0.78\textwidth` to `0.86\textwidth`. Use full width only when the figure carries a central claim or necessary mechanism.

Use a visual readiness loop for important main-body figures: render at final paper size, preview as PNG or PDF, inspect with programmatic checks where possible, then read the image as a judge would. A figure is not ready if Chinese text becomes boxes, the minus sign is wrong, legends cover data, labels overlap, grayscale loses the conclusion, or the final-size image needs zooming to read.

## 输出约定

Return:

```text
Figure lock:
Figure count:
Main-body figures:
Appendix or diagnostic figures:
Blocked figures:
Missing subquestion support:
Profile summary:
Pitfall blocks:
Caption repairs:
Post-figure conclusions:
Visual readiness checks:
Risk notes:
Registry updates:
Return to hub: math-hub
Recommended repair surface:
```

When editing or proposing `figure_evidence.csv`, use:

```csv
figure_id,problem_id,claim_id,paper_role,figure_path,figure_type,plot_family,plot_type,why_this_plot,scenario,metric,unit,source_table,source_script,run_id,baseline_or_threshold,uncertainty_or_error,constraint_status,caption,post_figure_conclusion,validation_status,risk_note,data_source,notes
```

`Recommended repair surface` may name `code` for regeneration, `latex` for placement, `abstract` for claim wording, `review` for scoring audit, `compliance` for package or rule issues, or `hub QC`, but the handoff always returns to `math-hub`.

## 红线

Stop and repair or demote when:

- a figure is selected because it looks impressive rather than because it proves a claim;
- a figure has no claim id, source table/script, run id, caption, conclusion, or risk note;
- a sensitivity or robustness plot has no baseline or tested range;
- a heatmap has no colorbar unit;
- a result figure lacks scenario, metric, or denominator;
- the exact value appears only in the figure and not in a table or registry;
- a main-body figure would consume most of a page without carrying a central claim;
- the figure audit starts routing, dispatching, or calling another skill instead of returning findings to `math-hub`.
