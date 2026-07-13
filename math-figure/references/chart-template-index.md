# Chart Template Index

Use these chart assets when `math-code` needs a stable starting point for common contest-paper figures. Copy the script into the active project and adapt names, units, labels, caption drafts, and figure evidence rows.

## Nature-inspired Asset Reuse

Borrow only the useful asset discipline: figure contract before plotting, a chart atlas that maps claim shape to reusable scripts, formal Nature-style palette control, vector-first export, and final-size visual QA. Do not import journal-only burdens such as fixed journal dimensions, decorative multi-panel layouts, or backend rules that do not improve a contest claim.

## Contest adaptation map

| Nature-style asset idea | Contest adaptation | Local asset |
| --- | --- | --- |
| Chart atlas | Map a claim shape to a small evidence figure family | `references/chart-template-index.md` |
| Figure contract before plotting | Lock `claim_id`, source table, metric, unit, caption, post-figure conclusion, and risk note before scripting | `math-hub/references/figure-evidence-rules.md` |
| Reusable chart scripts | Start from a tested Python template, then replace data, labels, units, baseline, and scenario names | `assets/chart-templates/` |
| Paper figure style | Apply the Nature-style contest palette, no in-figure title, light grid, and final-paper readability defaults | `references/paper-figure-style.md` |
| High-impact assets | Use the vendored Nature v2.0.0 atlas and figures4papers templates after the contest evidence gate | `assets/high-impact-templates/`, `references/high-impact-chart-assets.md` |
| Vector-first export | Prefer SVG/PDF for LaTeX; keep PNG as a fallback for compiler trouble | template export settings |
| Visual QA loop | Inspect the final-size image before marking it paper-ready | `references/visual-readiness-loop.md` |

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

Apply `references/paper-figure-style.md` before final export. Use `assets/chart-templates/paper_style.py` for matplotlib palette and axis styling, remove in-figure titles, and keep the caption as the title carrier.

When the lightweight template family is too weak, read `references/high-impact-chart-assets.md` and borrow only the needed atlas/API/demo pattern. Keep demo data and paper-specific labels out of contest outputs.

The high-impact asset shelf contains `assets/high-impact-templates/chart-atlas/` with 10 atlas PNGs and `assets/high-impact-templates/figures4papers/` with 24 Python template scripts plus previews, copied from Nature `nature-figure v2.0.0` commit `5d2ba1d`. Treat these as pattern only resources: inspect layout, palette, annotation, legend, and export decisions, but do not copy demo data into a contest figure.

## Export Contract

The templates export SVG, PDF, and PNG. Prefer SVG or PDF for LaTeX when the toolchain supports it. Use PNG only when the contest template or local compiler makes vector export painful.
