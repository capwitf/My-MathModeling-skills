# Figure Selection Guide

Use this guide when deciding what figure to generate for a contest paper.

## Start With The Claim

1. Write the exact `claim_id` and the one-sentence claim.
2. Decide whether the reader needs an exact value or a visual pattern.
3. If exact values matter, prefer a table.
4. If the reader needs a trend, boundary, mechanism, robustness check, or tradeoff, prefer a figure.
5. Generate one primary candidate first.

## Quick Routing Table

| Need | Start with | Keep out of main body unless... |
| --- | --- | --- |
| exact values, lookup answers, ranking table | table | the chart reveals a pattern the table cannot show |
| time trend, threshold crossing, sequence | line, stepped line, local zoom | the claim depends on dense event timing |
| scenario or method comparison | bar, grouped bar, relative-change heatmap | labels remain readable and the comparison is the point |
| mechanism, allocation, state transition | mechanism diagram, flow diagram, state trajectory | the diagram shortens the explanation materially |
| robustness, sensitivity, stress test | sensitivity curve, tornado plot, stress heatmap | the conclusion depends on parameter stability |
| tradeoff, policy choice, frontier | Pareto/frontier plot, selected-point marker | the selected point must be defended visually |
| feasibility, residuals, solver health | diagnostic plot | the task explicitly asks for validation evidence |

## Reusable Template Assets

For common chart families, start from `references/chart-template-index.md` and the Nature patterns in `assets/high-impact-templates/figures4papers/`:

- grouped bars or multi-metric panels for scenario and method comparison;
- curves and ablation panels for sensitivity and robustness;
- heatmaps or matrices for scenario-method structure;
- surfaces and geometry panels for mechanisms or spatial structure;
- distributions for diagnostics and data-composition claims.

When no Nature pattern matches a Pareto frontier, feasibility diagnostic, or dispatch sequence, write the smallest claim-specific chart with `assets/chart-templates/paper_style.py` instead of starting from a generic demo template.

## Tie-Breaking Rules

When two candidates work, choose the one that:

- uses fewer panels;
- keeps units, baseline, and denominator visible;
- can be summarized in one sentence after the figure;
- avoids decorative complexity;
- matches the source data with the smallest transformation.

## What To Draft Before Plotting

For each candidate, write:

`figure_id, claim_id, paper_role, source_table/source_script, plot_family, plot_type, why_this_plot, caption_draft, post_figure_conclusion_draft, risk_note`

If you cannot write the post-figure conclusion, downgrade the figure or move it to appendix.

## Common Anti-Patterns

- making a chart just because data exists;
- choosing a plot family before deciding the claim;
- using a diagnostic plot as main-body evidence;
- turning exact values into a picture when a table is clearer;
- adding a second figure because the first one looks empty.
