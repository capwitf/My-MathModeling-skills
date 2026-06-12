# Chart Template Index

Use these chart assets when `math-code` needs a stable starting point for common contest-paper figures. Copy the script into the active project and adapt names, units, labels, caption drafts, and figure evidence rows.

## Templates

| Claim shape | Template | Best for | Main-body default |
| --- | --- | --- | --- |
| Scenario or method delta | `assets/chart-templates/relative_change_heatmap.py` | relative cost, score, risk, load, or emissions change from a baseline | yes, if it answers a comparison claim |
| Tradeoff or policy choice | `assets/chart-templates/pareto_frontier.py` | cost-risk, cost-service, storage-cost, accuracy-complexity frontiers | yes, if the selected point matters |
| Parameter sensitivity | `assets/chart-templates/sensitivity_tornado.py` | one-way sensitivity, stress tests, threshold changes | yes, when robustness supports a final claim |
| Constraint or solver health | `assets/chart-templates/feasibility_diagnostics.py` | residuals, violations, feasibility pass/fail, diagnostic severity | appendix by default |
| Schedule, route, or state sequence | `assets/chart-templates/dispatch_time_series.py` | power balance, storage state, task schedule, route flow over time | yes, if it explains mechanism or dispatch |

## Adaptation Contract

Before using a template, define:

- `figure_id`
- `claim_id`
- source table
- plotted metric and unit
- baseline, threshold, or selected solution when relevant
- caption draft
- post-figure conclusion draft
- risk note

Do not keep demo data, placeholder labels, or generic captions in a final paper figure.

## Export Contract

The templates export SVG, PDF, and PNG. Prefer SVG or PDF for LaTeX when the toolchain supports it. Use PNG only when the contest template or local compiler makes vector export painful.
