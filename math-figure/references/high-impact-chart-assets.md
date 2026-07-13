# High-Impact Chart Assets

Use this reference when a contest figure needs stronger visual form than the lightweight local templates provide. It inherits useful parts of GitHub `Yuan1z0825/nature-skills`, `nature-figure v2.0.0`, checked at commit `5d2ba1d` on 2026-06-20.

## Contest evidence gate

Apply the contest evidence gate first: define the claim, source table, metric, unit, caption, post-figure conclusion, and risk note. Use high-impact assets only after that gate. Rule: do not copy demo data; also remove manuscript-specific labels, local paths, and biomedical storylines before adapting a pattern into a math-modeling paper.

## Local inherited assets

- `assets/high-impact-templates/chart-atlas/`: 10 atlas PNGs covering common high-impact chart families.
- `assets/high-impact-templates/figures4papers/`: 24 Python template scripts plus bundled previews from the Nature demo shelf. Use them as pattern only references for layout, axis treatment, annotation, legend placement, and export behavior.
- `assets/chart-templates/paper_style.py`: local distilled API helpers for contest data, including `PALETTE`, `DEFAULT_COLORS`, `apply_publication_style`, `add_panel_label`, `make_grouped_bar`, `make_trend`, `make_heatmap`, `make_forest_plot`, and `finalize_figure`.

## What to borrow

- `chart-atlas`: use as a visual routing atlas, not as direct evidence. It covers bar charts, line trends, heatmaps, scatter/bubble, radar/polar, distributions, forest/interval, area/stacked, image plates, and network/matrix figures.
- `figures4papers`: use as Python/matplotlib pattern examples for layout, axes, legend, annotation, and export. Keep the math-modeling source data and claim boundaries.
- `api.md`: borrow `PALETTE`, `DEFAULT_COLORS`, `apply_publication_style`, `add_panel_label`, `make_grouped_bar`, `make_trend`, `make_heatmap`, `make_forest_plot`, and vector-first export helpers. Local distilled versions live in `assets/chart-templates/paper_style.py`.
- `chart-types.md`: borrow radar, conceptual 3D sphere, scatter, fill-between area, log-scale bar, and GridSpec multi-panel patterns only when they make the contest claim clearer.

## Demo routing map

| Need | Nature demo family | Contest adaptation |
| --- | --- | --- |
| Method comparison or ablation bars | `figure_ImmunoStruct`, `figure_CellSpliceNet`, `figure_brainteaser` | candidate comparison, robustness ablation, model variant comparison |
| Radar or multi-metric profile | `figure_VIGIL` | only for normalized multi-indicator score profiles; avoid when exact values matter |
| Trend or review-style time line | `figure_VIGIL`, `figure_ophthal_review` | time, iteration, threshold, or scenario trend with direct labels |
| Heatmap or matrix | `figure_RNAGenScape`, `figure_ophthal_review` | scenario-method matrix, relative-change heatmap, sensitivity matrix |
| Conceptual geometry or manifold | `figure_Dispersion`, `figure_Cflows`, `figure_RNAGenScape` | mechanism diagram or geometric intuition; keep as appendix unless central |
| Distribution or prior/motivation | `figure_FPGM`, `figure_brainteaser` | diagnostic distribution, prior/weight comparison, data composition |

## Math-modeling rules

- Prefer table for final parameter vectors and exact rankings; use high-impact charts for pattern, mechanism, comparison, robustness, or feasibility.
- Keep main-body figures sparse: one conclusion per figure, no in-figure title, readable units, and a nearby post-figure conclusion.
- Demote rich demo-style composites to appendix unless they answer a required subquestion directly.
- For generated code, copy only the local helper or selected pattern; do not vendor the full upstream demo tree into a contest project.
