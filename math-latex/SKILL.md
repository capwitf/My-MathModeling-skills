---
name: math-latex
description: Use when 高教社杯/CUMCM 数学建模论文需要 LaTeX 排版、模板保持、中英文摘要、公式、表格、图、参考文献、匿名性、页数、浮动体或最终 PDF 质量检查。
---

# 竞赛 LaTeX 排版

## 用途

Format mathematical modeling papers for submission. Prefer compliance, readability, and evidence visibility over decorative restyling.

核心规则：评委读到的是 PDF。必须编译并检查渲染后的页面，而不是只看源代码。

国一候选门槛：排版必须让题目贴合、建模洞察、证据可信、可复现、边界清楚被评委快速看到；这是提交质量门槛，不承诺获奖。版面修饰不能替代证据链，任何影响可读性、匿名性、页数或表图可核验性的布局都要阻塞最终状态。

硬门禁：官方模板和提交规则高于本地审美偏好。规则未知时，最终排版状态必须阻塞。

## 核心流程

1. Inspect official template and contest rules before changing structure.
2. Preserve `documentclass`, margins, headers, numbering, and required sections unless the user asks otherwise.
3. Fix structure, references, equations, tables, and figures before cosmetic style.
4. Compile early and often.
5. Inspect rendered PDF pages for whitespace, crowding, unreadable figures, float order, and anonymity.
6. Run the final submission checklist before calling the paper complete.

If the official rule says no table of contents, do not insert one. If the rule is unknown, leave structure conservative and mark final submission blocked.

Read `references/final-checklist.md` for final inspection order and `references/latex-patterns.md` for repair snippets.

## 结构规则

- Each subproblem should close the loop: model, solve, result, validation, conclusion.
- Keep section titles short and parallel.
- Move derivations, raw diagnostics, solver traces, and large ledgers to appendix when allowed.
- Do not insert gratuitous `\newpage` or `\clearpage` between body sections.
- Avoid manual spacing hacks. Use them only as the smallest repair after structural fixes.
- Do not force a decorative heading style, section numbering style, or page break pattern unless the official template or user requires it.

## 图表密度门禁

For every figure/table in the main body, ask:

- What claim does it prove?
- Is that claim already better shown by a table or a smaller figure?
- Can a reader understand it at 100 percent PDF zoom?
- Does it need to be in the main body, or is appendix better?
- Is there a nearby conclusion sentence and boundary/risk sentence?

Default figure sizing:

- single main-body evidence figure: usually `0.78\textwidth` to `0.86\textwidth`;
- full-width only for a mechanism diagram, Pareto/frontier plot, or dense figure that carries a central claim;
- two-panel figures: only when the two panels answer the same claim;
- 2x2 figures: use only when every panel remains readable and the combined figure has one clear takeaway.

Avoid final paper image paths like `1.png`, `2.png`, or hash names. Prefer semantic filenames.

## 标题与证据规则

- Captions should name object, scenario, metric, and what to notice.
- Mention each figure/table before or near where it appears.
- Put units in headers, axes, and colorbars.
- Do not let figures appear before their first meaningful mention unless the template requires it.
- If `figure_evidence.csv` exists, every main-body figure should map to a row with `validation_status=paper_ready`.

## 公式与记号规则

- Number display equations only when referenced or important.
- Use `align`/`aligned` for multi-line derivations.
- Define symbols near first use and keep notation table consistent.
- Avoid oversized inline formulas that damage line spacing.

## 表格

- Prefer `booktabs` and no vertical rules.
- Put units in column headers.
- Use `longtable` for tables likely to cross pages.
- Do not use `resizebox` to hide an unreadable table. Split or redesign the table.

## 竞赛高频排版修复

Before final layout, actively check these contest pain points in the rendered PDF, not only in source:

- 三线表: use `booktabs` with clear headers, units, and aligned numeric columns. Do not use `resizebox` as the default repair for a wide table; first shorten headers, split columns by claim, use `tabularx`/`p{}` columns, or move secondary diagnostics to appendix.
- 多图并列: use subfigures only when panels answer one shared claim. Keep panel labels, axes, legends, and captions readable at normal zoom; split the figure if each panel needs a different conclusion sentence.
- 长公式断行: use `align`, `aligned`, `split`, or named intermediate variables. Break at relations or operators, not inside semantic units. Avoid shrinking equations as an image or using tiny font to make them fit.
- 伪代码: use a stable algorithm environment only when the algorithm is part of the modeling contribution or reproducibility path. Keep it shorter than the surrounding explanation and make inputs, outputs, stopping rule, and complexity or iteration limit visible.

Use `references/latex-patterns.md` for snippets. Any repair must preserve official template structure, page limits, labels, references, and evidence visibility.

## 合规报告门禁

When final-format readiness is requested, produce or update a compact `compliance_report` rather than only saying the outline looks right. At minimum it should record:

- cover/title-page requirements checked against the active official template;
- Chinese and English abstract presence, active word/page limits, and keyword count;
- required section order and whether every subproblem has a result/validation/conclusion loop;
- equation numbering continuity and whether referenced equations exist;
- figure/table numbering, captions, first mentions, units, and source/evidence rows;
- reference style consistency and whether every citation resolves;
- page limit, anonymity, PDF metadata, compile command, and rendered-page inspection status.

If the official format source is unknown, `compliance_report` must say `official rules unknown -> blocked`; do not infer from an older contest template.

## 最终 PDF 视觉检查

Use a contact sheet or page screenshots when available. Check:

- pages with a figure taking most of the page;
- large blank gaps caused by floats or forced breaks;
- pages with too many dense figures;
- captions separated from figures;
- unreadable labels, legends, or colorbars;
- stale template residue in appendices or separate AI-use statement files.

Final claims are blocked if PDF inspection has not been performed after the last layout-affecting edit.

## 输出预期

When using this skill, report:

- binding template constraints;
- files changed;
- compile command and result;
- layout issues fixed;
- unresolved compile, float, page-limit, anonymity, or evidence risks.

## 红线

Stop and repair before finalizing when:

- the PDF does not compile from a clean command;
- page limits, table-of-contents rules, anonymity, or appendix rules are unknown;
- figures/tables are unreadable at normal zoom;
- captions, references, or figure order make a claim hard to verify;
- appendix code/support files mentioned in the paper are missing or stale;
- separate AI-use statement files or support materials contain old-template residue.
