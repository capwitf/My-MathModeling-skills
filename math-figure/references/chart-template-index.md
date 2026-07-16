# Chart Template Index

Use this index when `math-code` needs a stable starting point for a contest-paper figure. Start from the closest vendored Nature pattern, then adapt data, units, labels, caption drafts, and figure evidence rows.

## Nature-inspired Asset Reuse

Borrow only the useful asset discipline: figure contract before plotting, a chart atlas that maps claim shape to reusable scripts, formal Nature-style palette control, vector-first export, and final-size visual QA. Do not import journal-only burdens such as fixed journal dimensions, decorative multi-panel layouts, or backend rules that do not improve a contest claim.

## Contest adaptation map

| Nature-style asset idea | Contest adaptation | Local asset |
| --- | --- | --- |
| Chart atlas | Map a claim shape to a small evidence figure family | `references/chart-template-index.md` |
| Figure contract before plotting | Lock `claim_id`, source table, metric, unit, caption, post-figure conclusion, and risk note before scripting | `math-hub/references/figure-evidence-rules.md` |
| Reusable chart scripts | Start from a vendored Nature pattern, then replace data, labels, units, baseline, and scenario names | `assets/high-impact-templates/figures4papers/` |
| Paper figure style | Apply the Nature-style contest palette, no in-figure title, light grid, and final-paper readability defaults | `references/paper-figure-style.md` |
| High-impact assets | Use the vendored Nature v2.0.0 atlas and figures4papers templates after the contest evidence gate | `assets/high-impact-templates/`, `references/high-impact-chart-assets.md` |
| Vector-first export | Prefer SVG/PDF for LaTeX; keep PNG as a fallback for compiler trouble | template export settings |
| Visual QA loop | Inspect the final-size image before marking it paper-ready | `references/visual-readiness-loop.md` |

## Nature Asset Routing

| Claim shape | Nature family | Best for | Main-body default |
| --- | --- | --- | --- |
| Scenario or method comparison | `figure_ImmunoStruct`, `figure_CellSpliceNet`, `figure_brainteaser` | grouped bars, uncertainty, ablation, and multi-metric comparisons | yes, if it answers a comparison claim |
| Trend or robustness | `figure_VIGIL`, `figure_ophthal_review` | data-fraction, hyperparameter, time, iteration, or threshold curves | yes, when stability supports a final claim |
| Matrix or heatmap structure | `figure_RNAGenScape`, `figure_ophthal_review` | scenario-method matrices, relative changes, or sensitivity structure | yes, if labels remain readable |
| Geometry, surface, or mechanism | `figure_Dispersion`, `figure_Cflows`, `figure_RNAGenScape` | spatial fields, manifolds, response surfaces, and geometric intuition | appendix unless the mechanism is central |
| Distribution or composition | `figure_FPGM`, `figure_brainteaser`, `figure_VIGIL` | diagnostic distributions, priors, weights, and data composition | appendix unless it proves a required claim |
| Pareto, feasibility, or dispatch | no fixed vendored default | write the smallest claim-specific chart with `paper_style.py` | decide from the claim and evidence role |

## Adaptation Contract

Before adapting a Nature pattern or writing a bespoke chart, define:

- `figure_id`
- `claim_id`
- source table
- plotted metric and unit
- baseline, threshold, or selected solution when relevant
- caption draft
- post-figure conclusion draft
- risk note

Do not keep upstream demo data, biomedical labels, local paths, placeholder labels, or generic captions in a final paper figure.

Apply `references/paper-figure-style.md` before final export. Use `assets/chart-templates/paper_style.py` for bespoke matplotlib palette and axis styling, remove in-figure titles, and keep the caption as the title carrier.

Read `references/high-impact-chart-assets.md` before adapting a vendored script and borrow only the needed atlas, API, or demo pattern. Keep demo data and paper-specific labels out of contest outputs.

The high-impact asset shelf contains `assets/high-impact-templates/chart-atlas/` with 10 atlas PNGs and `assets/high-impact-templates/figures4papers/` with 27 Python template scripts plus previews. The shelf was initialized from Nature `nature-figure v2.0.0` commit `5d2ba1d` and synchronized with `main` commit `b98b53e` on 2026-07-14. Treat these as pattern only resources: inspect layout, palette, annotation, legend, and export decisions, but do not copy demo data into a contest figure.

## Export Contract

The templates export SVG, PDF, and PNG. Prefer SVG or PDF for LaTeX when the toolchain supports it. Use PNG only when the contest template or local compiler makes vector export painful.
