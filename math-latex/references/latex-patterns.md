# LaTeX Patterns

Use these patterns when the contest template does not already force another approach.

## Engine Choice

- Prefer `xeLaTeX` for Chinese-English mixed papers.
- Keep the existing engine if the project is already stable and the user did not request migration.
- Avoid engine switching late in the submission cycle unless it fixes a concrete blocker.

## Recommended Package Set

Small, common set for contest papers:

```tex
\usepackage{amsmath,amssymb,amsthm}
\usepackage{bm}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{multirow}
\usepackage{caption}
\usepackage{subcaption}
\usepackage{hyperref}
```

Add only what the document actually needs.

Optional packages for contest pain points:

```tex
\usepackage{tabularx}       % flexible-width tables
\usepackage{array}          % custom column alignment
\usepackage{algorithm}      % algorithm float
\usepackage{algpseudocode}  % algorithmicx pseudocode syntax
```

Add these only when the relevant table or pseudocode pattern is used and the official template does not already provide another environment.

## Optional Chinese Contest Section Numbering (ctexset)

Use this pattern only when the official template, active contest rules, or the user explicitly wants Chinese-style section numbering. Do not override an official template's heading style. If the active rules say fonts, sizes, or numbering are not unified, treat this as an optional repair snippet rather than a requirement.

When this style is allowed, first-level headings use Chinese numerals (一、二、三…), centered, with a trailing Chinese comma. Subsections use Arabic `X.Y` format, left-aligned.

```tex
\ctexset{
  section = {
    name = {,、},
    number = \chinese{section},
    format = \centering\zihao{3}\heiti,
    aftername = {},
    beforeskip = 1.5ex plus 0.5ex minus 0.2ex,
    afterskip = 1ex plus 0.2ex,
  },
  subsection = {
    number = \arabic{section}.\arabic{subsection},
    format = \zihao{4}\heiti,
    beforeskip = 1ex plus 0.3ex minus 0.1ex,
    afterskip = 0.8ex plus 0.1ex,
  },
  subsubsection = {
    number = \arabic{section}.\arabic{subsection}.\arabic{subsubsection},
    format = \zihao{-4}\heiti,
  }
}
```

This produces headings like:
- `一、问题重述` (centered, bold)
- `1.1 问题背景` (left-aligned, bold)
- `1.1.1 数据说明` (left-aligned, bold)

## Assumption List Format (模型假设)

Assumptions use `1、2、3、` numbering (Arabic numeral + Chinese enumeration comma), NOT `（1）（2）（3）`:

```tex
\usepackage{enumitem}  % in preamble

\section{模型假设}
\begin{enumerate}[label=\arabic*、, leftmargin=2em]
  \item 假设天气一直保持晴朗，太阳光线不会被云层遮盖
  \item 假设不发生光的散射
  \item 假设镜面反射率可以取为常数
  \item 假设每条反射光线携带的能量是相同的
\end{enumerate}
```

## Problem Restatement Format (问题重述)

In the problem restatement section, each sub-problem uses bold `问题一：` followed by a space, then the description. The colon is Chinese fullwidth `：`, and there is a space after it:

```tex
\section{问题重述}

\subsection{问题背景}
% 1-2 short paragraphs. Keep only task-relevant background.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.55\linewidth]{figures/context_scene.png}
\caption{现实中的[对象/场景]}
\label{fig:context-scene}
\end{figure}

\subsection{问题提出}

\textbf{问题一：} 在题目给定的圆形定日镜场内，将吸收塔建于该定日镜场的中心……

\textbf{问题二：} 根据题目给定的要求，定日镜场的额定功率为$60MW$……

\textbf{问题三：} 定日镜的额定功率仍为$60MW$，但此时每一个定日镜的尺寸……
```

Key formatting rules:
- Use `\textbf{问题一：}` with a space after the closing brace
- Chinese fullwidth colon `：` (not half-width `:`)
- Each problem statement is a separate paragraph, not a list item
- Use `\subsection{问题背景}` followed by `\subsection{问题提出}` when the template allows second-level headings
- The background figure is optional; include it only if it clarifies the real object, scenario, geometry, or decision context
- Caption background figures concretely, not decoratively

## Problem Analysis Format (问题分析)

Use a total-sub structure. Start with one short total paragraph that explains how the whole problem is decomposed, then write one paragraph per subproblem. Each subproblem label uses bold `问题一：` followed by a space:

```tex
\section{问题分析与思路概述}

本题可分解为[任务1]、[任务2]和[任务3]三个递进建模任务，其中问题一的结果将作为问题二的[输入/约束/基准]。

\textbf{问题一：} 问题一要求[交付物]，从数学结构看属于[问题类型]。该问题的难点在于[难点]。本文采用[模型]，输出[结果]，并通过[验证方式]检验。

\textbf{问题二：} 在问题一得到[结果/参数/约束]的基础上，问题二进一步考虑[新增因素]。该问题可归结为[问题类型]，采用[模型]求解，并通过[验证方式]检验。
```

Key formatting rules:
- Use `\textbf{问题一：}` with a space after the closing brace
- Chinese fullwidth colon `：` (not half-width `:`)
- One subproblem per paragraph
- Do not turn every subproblem into `\subsection` unless the section is long or the official template requires it

## Optional Table of Contents (目录)

Only include `\tableofcontents` when the official template, active contest rules, or the user explicitly requires a table of contents. If the active rules say no table of contents, omit it. If the rule is unknown, do not insert a TOC and mark final formatting as blocked until the rule source is checked.

When a TOC is allowed and `\ctexset` is configured with Chinese numeral sections, it can produce this format:

```
目录

一、 问题重述 .....................................................3
    1.1 问题背景 ...................................................3
    1.2 问题重述 ...................................................3
二、 问题分析 .....................................................3
    2.1 问题一分析 .................................................3
三、 模型假设 .....................................................4
四、 符号说明 .....................................................5
五、 问题一模型的建立与求解 .......................................11
    5.1 模型的建立 ................................................11
        5.1.1 约束条件 ............................................11
参考文献 .........................................................39
附录 .............................................................40
```

Key points when a TOC is allowed:
1. First-level entries: Chinese numerals `一、`, `二、`, `三、`… (no indentation)
2. Subsections: indented, Arabic `X.Y` format
3. Subsubsections: further indented, Arabic `X.Y.Z` format
4. Dotted leaders `...` connecting title to right-aligned page number (default LaTeX TOC behavior)
5. `参考文献` and `附录` appear without numbering at the end
6. No extra TOC package needed — `\tableofcontents` with `ctexset` handles everything
7. Do NOT insert `\newpage` after the TOC unless the template requires it

## Avoiding Large Blank Spaces

Common causes of unwanted whitespace in contest papers:

1. **`\newpage` or `\clearpage` before sections** — Remove these unless the template requires page breaks at specific points.
2. **Symbol table using `table` + `tabular`** — The `table` float cannot break across pages. If the table doesn't fit the remaining space, LaTeX pushes it entirely to the next page, leaving a gap. **Use `longtable` instead** — it breaks naturally across pages.
3. **Tables or figures that don't fit** — Use `[htbp]` placement and let LaTeX flow content naturally. Avoid `[H]` which forces position and creates gaps.
4. **`longtable` needing `\usepackage{longtable}`** — Ensure the package is loaded in the preamble.

Fix pattern — symbol table that spans pages:
```tex
% WRONG: table float cannot break across pages, causes blank space above
\begin{table}[htbp]
\centering
\caption{核心符号说明}
\begin{tabular}{c p{0.58\linewidth} c}
\toprule
...
\bottomrule
\end{tabular}
\end{table}

% CORRECT: longtable breaks across pages naturally
\begin{longtable}{c p{0.58\linewidth} c}
\caption{核心符号说明}\label{tab:symbols} \\
\toprule
符号 & \makebox[0.58\linewidth][c]{符号说明} & 单位 \\
\midrule
\endfirsthead
\toprule
符号 & \makebox[0.58\linewidth][c]{符号说明} & 单位 \\
\midrule
\endhead
\bottomrule
\endfoot
$t$ & 时间步索引 & — \\
% ...
\end{longtable}
```

If a section must start on a fresh page (e.g., appendix), use `\clearpage` only there.

## Equation Patterns

Single important equation:

```tex
\begin{equation}
Z = \sum_{i=1}^{n} c_i x_i + \lambda \sum_{j=1}^{m} g_j(x)^2
\end{equation}
```

Aligned derivation:

```tex
\begin{align}
f(x)
  &= \sum_{i=1}^{n} a_i x_i \\
  &= \mathbf{a}^\top \mathbf{x}
\end{align}
```

Piecewise penalty:

```tex
\[
\phi_i(t_i)=
\begin{cases}
\alpha(E_i-t_i)^2, & t_i < E_i, \\
0, & E_i \le t_i \le L_i, \\
\beta(t_i-L_i)^2, & t_i > L_i.
\end{cases}
\]
```

## Table Pattern

```tex
\begin{table}[htbp]
\centering
\caption{Sensitivity analysis of key parameters}
\label{tab:sensitivity}
\begin{tabular}{cccc}
\toprule
Parameter & Value & Objective & Change rate (\%) \\
\midrule
$\alpha$ & 0.2 & 97504 & -1.3 \\
$\alpha$ & 0.5 & 96210 & 0.0 \\
$\alpha$ & 0.8 & 98112 & 2.0 \\
\bottomrule
\end{tabular}
\end{table}
```

## Figure Pattern

```tex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.82\linewidth]{figures/convergence_curve.png}
\caption{Convergence behavior of the hybrid algorithm}
\label{fig:convergence}
\end{figure}
```

## Contest Pain-Point Patterns

Use these snippets for common CUMCM layout failures. After applying any snippet, compile and inspect the rendered PDF at normal zoom.

### Three-line result table

Use this for a main-body result table with exact values. Keep one table tied to one claim; move secondary diagnostics to appendix.

```tex
\begin{table}[htbp]
\centering
\caption{问题二不同方案下的配送成本与约束满足情况}
\label{tab:q2-cost-feasibility}
\begin{tabularx}{0.92\linewidth}{@{}l r r r X@{}}
\toprule
方案 & 成本/元 & 总里程/km & 违约次数 & 说明 \\
\midrule
基准方案 & 128430 & 842.6 & 3 & 未考虑时间窗惩罚 \\
改进方案 & 119870 & 801.4 & 0 & 满足容量与时间窗约束 \\
\bottomrule
\end{tabularx}
\end{table}
```

Repair order for a crowded table: shorten headers, put units in headers, reduce columns to the claim, use `tabularx` or fixed `p{}` columns, split by subquestion, then appendix. Do not use `resizebox` as the first repair.

### Side-by-side subfigures

Use side-by-side panels only when both panels support the same conclusion.

```tex
\begin{figure}[htbp]
\centering
\begin{subfigure}[t]{0.47\linewidth}
  \centering
  \includegraphics[width=\linewidth]{figures/q1-baseline.png}
  \caption{基准方案}
  \label{fig:q1-baseline}
\end{subfigure}
\hfill
\begin{subfigure}[t]{0.47\linewidth}
  \centering
  \includegraphics[width=\linewidth]{figures/q1-improved.png}
  \caption{改进方案}
  \label{fig:q1-improved}
\end{subfigure}
\caption{问题一两类方案下关键指标的空间分布对比}
\label{fig:q1-spatial-compare}
\end{figure}
```

If the two panels need different takeaways, split them into separate figures. If labels are unreadable at 100 percent PDF zoom, reduce panel count before enlarging the whole float.

### Long equation line breaking

Use `align`, `aligned`, or `split`; break at `=`, `+`, `-`, `\le`, or summation boundaries. Name repeated terms instead of forcing one giant expression.

```tex
\begin{align}
J(\mathbf{x})
  &= \sum_{i \in \mathcal{I}} c_i x_i
   + \lambda_1 \sum_{t \in \mathcal{T}} \max\{0, d_t-s_t\} \notag \\
  &\quad
   + \lambda_2 \sum_{(i,j)\in\mathcal{E}} y_{ij}
   + \lambda_3 \sum_{k \in \mathcal{K}} \Delta_k^2 .
\label{eq:objective-expanded}
\end{align}
```

For a numbered equation with internal line breaks:

```tex
\begin{equation}
\begin{aligned}
P_{\mathrm{loss}}
  &= P_{\mathrm{geo}} + P_{\mathrm{shade}} + P_{\mathrm{trunc}} \\
  &= \eta_{\mathrm{geo}} A I
   + \eta_{\mathrm{shade}} A I
   + \eta_{\mathrm{trunc}} A I .
\end{aligned}
\label{eq:loss-decomposition}
\end{equation}
```

Do not turn equations into images. Do not reduce font size until semantic line breaks and notation compression have been tried.

### Contest pseudocode

Use pseudocode when the algorithm itself is part of the method, not for ordinary preprocessing. Show inputs, outputs, stopping rule, and the paper-facing result.

```tex
\begin{algorithm}[htbp]
\caption{问题三约束修复启发式}
\label{alg:q3-repair}
\begin{algorithmic}[1]
\Require 初始解 $\mathbf{x}^{(0)}$，最大迭代次数 $K$，容差 $\varepsilon$
\Ensure 可行解 $\mathbf{x}^{*}$ 与目标函数值 $J(\mathbf{x}^{*})$
\State $\mathbf{x}\gets \mathbf{x}^{(0)}$
\For{$k=1,\ldots,K$}
  \State 计算违反约束集合 $\mathcal{V}(\mathbf{x})$
  \If{$\mathcal{V}(\mathbf{x})=\emptyset$ and $|J_k-J_{k-1}|<\varepsilon$}
    \State \textbf{break}
  \EndIf
  \State 按最大违反量更新对应决策变量
\EndFor
\State \Return $\mathbf{x}^{*}\gets\mathbf{x}$
\end{algorithmic}
\end{algorithm}
```

If the pseudocode exceeds half a page, move low-level steps to appendix and keep the main body focused on the modeling contribution and stopping rule.

## Common Repairs

### Overfull lines

- Rewrite the sentence first.
- Move long formulas into display math.
- Shorten captions.
- Adjust figure width before touching spacing parameters.

### Floats piling up

- Reduce figure count on dense pages.
- Move less important tables to later pages or appendix.
- Use more natural float sizes.
- Avoid stacking many `[H]` floats.

### Mixed style across sections

- Standardize one caption format.
- Standardize one table format.
- Standardize one notation style for vectors, matrices, and sets.

### Bibliography ugliness

- Fix source metadata before hand-formatting output.
- Normalize title capitalization at the `.bib` level where appropriate.
- Keep one citation backend only.
