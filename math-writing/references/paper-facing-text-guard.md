# Paper-Facing Text Guard

## Purpose

Use this guard before any content enters `main.tex`, a paper fragment, or final paper-facing Markdown.

## Classification

Classify incoming material as:

- final prose: can be read directly by a judge;
- evidence material: tables, figures, formulas, result rows, algorithm summaries, logs, run records, diagnostics, or source notes;
- diagnostic material: console output, debug logs, failed runs, exploratory bullets, model notes, temporary plots, or stale candidates.

Evidence material may support paper text. Diagnostic material must stay out of the paper body unless explicitly moved to an appendix with status and purpose.

## Blockers

Do not let raw console output, debug logs, bullet-list numeric dumps, code comments, model notes, or unsupported template prose enter `main.tex` as正文. Lists are allowed for assumptions, pseudocode, appendix manifests, compact checklists, and symbol tables; they are blocked only when they replace judge-facing explanation.

## Rewrite Rule

Turn evidence into prose by adding:

1. the conclusion the reader should keep;
2. the table, figure, formula, or result row that supports it;
3. the comparison, mechanism, or trend explaining why it matters;
4. the boundary, exception, or decision meaning.

Bad:

```text
- n0 = 12: tc = 57.0 s
- n0 = 14: tc = 52.0 s
```

Better:

```text
表X表明，随着初始参数 n0 从 12 增至 14，遮蔽时间由 57.0 s 降至 52.0 s，说明该方案对 n0 的增大呈负向响应。该趋势与轨迹间隔缩短导致有效覆盖窗口压缩相一致，因此后续优化应优先控制 n0 的上界。
```
