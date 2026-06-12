# Contest Figure Pitfalls

Use this checklist before a figure enters the main body. These are common ways a contest paper loses evidence quality even when the plot is visually polished.

## Block Or Repair

| Pitfall | Why It Hurts | Repair |
| --- | --- | --- |
| 小样本均值柱 | Hides individual cases and uncertainty; looks more certain than the data | Use table, dot plot, box plot, or show scenario values |
| 双 Y 轴 | Lets unrelated scales imply a false relation | Split panels or normalize to a shared baseline |
| 3D chart without geometric need | Adds occlusion and fake depth | Use 2D chart; keep 3D only for real spatial geometry |
| 饼图 for many categories | Hard to compare small differences | Use sorted bar chart or table |
| Y 轴截断 without warning | Exaggerates differences | Start at zero for bars; annotate truncation for line/detail views |
| 无 colorbar or missing unit | Heatmap cannot be interpreted | Add colorbar label with unit and baseline |
| rainbow/jet palette | Creates false visual boundaries and weak grayscale reading | Use sequential/diverging palettes tied to metric meaning |
| 一图多论点 | No single post-figure conclusion survives | Split or demote panels; keep one primary claim |
| exact values only in the figure | Judges cannot quote or verify the result | Put exact values in a table or registry |
| diagnostic plot used as final evidence | Solver health does not answer the subquestion | Move to appendix unless validation itself is asked |

## Contest-Specific Anti-Patterns

- Drawing a mechanism chart that only says `input -> model -> output`.
- Repeating a result table as a picture with no added trend, boundary, or mechanism.
- Adding a second figure because the first looks empty.
- Leaving demo labels, old problem names, or placeholder captions in generated plots.
- Using a large full-width figure that does not carry a central claim.

If a pitfall remains after repair, mark the figure as `blocked` or `appendix`, not `paper_ready`.
