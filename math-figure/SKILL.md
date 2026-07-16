---
name: math-figure
description: Use when 高教社杯/CUMCM 数学建模论文需要规划、选择、审查或修复图、图表、表格转图、图注、图像证据行、正文放置、附录降级或图后结论。
---

# 图表证据

## 用途

Select, generate, or review figures that prove a claim. Main-body figures must carry mechanism, comparison, robustness, or decision evidence; diagnostic and dense support figures default to appendix.

Read the project's shared quality contract only when promoting a figure to paper-ready, classifying blocked status, running a final gate, or writing a cross-module handoff. Local chart choice or visual repair can stay lightweight.

## Figure First Principles

- One main-body figure should prove one central claim.
- Prefer tables for exact values and figures for patterns, mechanisms, tradeoffs, and robustness.
- Do not include every generated figure.
- Write a caption, one post-figure conclusion, and one boundary/risk note near the figure.
- A figure with unknown source, unit, scenario, baseline, or validation status is not paper-ready.

## Evidence Contract

`figure_evidence.csv` should record figure id, claim id, source output, role, caption target, `post_figure_conclusion`, risk note, and `validation_status`.

The `validation_status` must be `paper_ready` before a figure supports abstract, conclusion, or final answer wording. Otherwise, keep it planned, generated, checked, blocked, or diagnostic.

A `paper_ready` `figure_evidence.csv` row must include either `render_check_status=passed` or `human_visual_check=passed`, plus a final-size readability note. A generated file is not paper-ready simply because it exists in an experiment directory.

For simulation figures, raw traces stay appendix unless they directly prove a required mechanism or failure mode. A single-run screenshot is diagnostic, not a paper-ready simulation result.

## Selection And Review

1. Identify the claim the figure must prove.
2. Select the smallest chart type that makes the claim visible.
3. Verify source output and units.
4. Generate or inspect the image.
5. Check caption, conclusion, and boundary sentence.
6. Decide main-body versus appendix.
7. Return blockers to `math-code`, `math-model`, `math-verifier`, or `math-hub`.

Read `references/selection-guide.md` for chart selection, `references/paper-figure-style.md` for Nature-style palette, title, and formal-paper figure defaults, `references/high-impact-chart-assets.md` when local templates are visually or structurally too weak, `references/visual-readiness-loop.md` for visual inspection, and `math-hub/references/figure-evidence-rules.md` when figure evidence rows matter.

When a requested figure matches a reusable chart family, read `references/chart-template-index.md`, apply `references/paper-figure-style.md`, and adapt the closest script from `assets/high-impact-templates/` after the claim, source output, unit, and evidence boundary are known. Use `assets/chart-templates/paper_style.py` when a claim needs a bespoke matplotlib chart rather than a vendored Nature pattern. Treat templates as starting assets, not proof; every adapted figure still needs source, caption, `post_figure_conclusion`, risk note, and validation status.

For main-body figures, read `references/paper-figure-style.md` and use the Nature-style contest defaults: calm `palette`, vector-first export, `no in-figure title`, light grid, readable labels, and a single claim sentence before plotting. Use `assets/chart-templates/paper_style.py` when writing matplotlib code.

## Visual Readiness

Inspect saved figures before labeling them paper-ready. Block or demote when text is unreadable, labels are clipped, units are missing, legends conflict, colors obscure groups, axes mislead, marks overlap, or the figure does not answer its claim.

For final evidence rows, keep `figure_id`, `render_check_status`, `human_visual_check`, and `visual_check_note` traceable to the saved file. Use the experiment output path until the claim, caption, units, and readability checks clear; only then copy or reference it as a paper figure.

## Output Contract

Return:

- selected or rejected figures;
- figure role and claim id;
- caption and `post_figure_conclusion`;
- render or human visual check status;
- `figure_evidence.csv` rows or edits;
- main-body versus appendix decision;
- blocked figures and repair owner.

Return to hub: math-hub.

## Red Lines

- Do not treat attractive figures as evidence.
- Do not let a figure support a claim without source output and validation status.
- Do not use screenshots as final simulation evidence.
- Do not hide exact central results in a chart when a table is needed.
