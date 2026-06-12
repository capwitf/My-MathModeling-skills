---
name: math-table
description: Use when 高教社杯/CUMCM 数学建模论文需要格式化、修复、压缩或审查符号表、记号表、结果表，包括单位清理、longtable、列宽平衡或按截图修排版。
---

# 符号表与结果表

## 用途

Format notation tables without changing mathematical meaning.

核心规则：先保护符号和定义。排版修改不能悄悄重命名变量、改变定义域或修改单位。

国一候选门槛：表格必须让题目贴合、建模洞察、证据可信、可复现、边界清楚变得更可核验；这是提交质量门槛，不承诺获奖。符号、单位、来源和场景标签不清楚时，排版再紧凑也不能进入论文就绪状态。

硬门禁：单位是模型的一部分，不是装饰。单位未知或冲突时，符号表不能进入论文就绪状态。

## 流程

1. Read the current notation source and the first-use locations when available.
2. Preserve the symbol list unless the user explicitly asks to add/remove rows.
3. Normalize columns to: symbol, meaning, unit, and optionally domain/source.
4. Use `longtable` when the table may cross pages.
5. Use `booktabs` rules and avoid vertical lines.
6. Put `--` only for dimensionless or truly not-applicable units.
7. Mark unknown, conflicting, or unstated units as blockers or pending confirmation; do not hide them with `--`.
8. Wrap only long cells; do not shrink the whole table until unreadable.
9. Compile or run the smallest available LaTeX check after editing.

## 一致性检查

- Every formula symbol used in the body appears in the table or is locally defined.
- Every table symbol has one meaning and one unit across the paper.
- Indices, sets, parameters, variables, slack variables, and binary variables are distinguishable.
- Units match the result tables and axis labels.
- No stale symbols from old problems remain.

## 表格清单门禁

When auditing result tables as part of a paper pass, report `table_count` by subquestion and distinguish:

- required result tables that answer a deliverable;
- notation or parameter tables that make the model readable;
- diagnostic or appendix tables that should not crowd the main body;
- tables missing key data, units, scenario labels, baselines, source rows, or validation status.

Do not add tables just to show effort. If a result is exact, central, and short, prefer a table; if the table repeats a figure without adding exact values, remove, merge, or demote it. A main-body table is blocked when its units, source, or target subquestion are unknown.

## 红线

Stop and report a blocker when:

- a symbol appears with two meanings or two units;
- an engineering quantity has `--` as a unit without being dimensionless;
- a formula symbol is missing from both local definition and symbol table;
- notation was changed to fit layout rather than preserving math;
- stale symbols from another problem remain in the table.

## 推荐模式

```tex
\begin{longtable}{p{0.18\linewidth} p{0.62\linewidth} p{0.12\linewidth}}
\caption{Core notation}\label{tab:symbols}\\
\toprule
Symbol & Meaning & Unit \\
\midrule
\endfirsthead
\toprule
Symbol & Meaning & Unit \\
\midrule
\endhead
$t$ & Time-step index & -- \\
$\Delta t$ & Time-step length & h \\
\bottomrule
\end{longtable}
```

## 输出规则

- Keep edits minimal and reversible.
- Preserve mathematical notation exactly unless asked otherwise.
- Prefer compact spacing and balanced columns over decorative styling.
- Do not insert `\newpage` or `\clearpage` solely to place the symbol table.
- For paper table audits, include `table_count`, required tables missing, appendix candidates, and unit/source blockers.
