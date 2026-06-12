# Visual Readiness Loop

Use this for important main-body figures after the first draft is saved. The goal is to catch 最终尺寸 readability problems before LaTeX or Word hides them.

## Loop

1. Render at final paper size. Do not rely on later Word/LaTeX scaling to fix layout.
2. Export vector PDF/SVG when possible; keep PNG/TIFF only when the toolchain requires raster.
3. Make a 渲染预览 at normal reading size.
4. Run deterministic checks where possible: file exists, not blank, format, DPI, image dimensions, Chinese缺字, negative-sign/负号 display, label clipping, tick overlap.
5. AI 读图 or human preview: inspect title, axes, units, legend, annotations, panel labels, selected-point marker, and whether the figure supports exactly one claim.
6. Revise and rerender until the figure passes without needing zoom.

## Block Conditions

- 中文缺字, square boxes, or missing symbols appear.
- The minus sign is rendered as a box or ambiguous hyphen.
- Tick labels, annotations, title, legend, or colorbar overlap.
- 图例遮挡 data or selected solution markers.
- A heatmap or scatter color scale is not interpretable in grayscale.
- 灰度可分 fails: the conclusion disappears when color is removed.
- Final-size text is unreadable at normal PDF zoom.
- JPEG is used for line/text-heavy data figures.
- The caption does not name object, scenario, metric, and what to notice.

## Final-Size Defaults

- Single main-body evidence figure: about `0.78\textwidth` to `0.86\textwidth`.
- Central mechanism or spatial figure: full width only when it truly carries the main explanation.
- Prefer direct labels for a few series; use legends only when labels would clutter the plot.
