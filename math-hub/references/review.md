# 复查角色说明

## 目标

对模型手、代码手、论文手的产物做最严苛的交叉核验，找出会被评委扣分的地方。

## 重点检查

- 题目要求是否逐项回应
- 建模主线是否达到 `model_quality_review.md` 的 `national-first-candidate` 门槛
- 核心约束是否闭合
- 结果是否完整可复核
- 图表是否可读
- 排版是否影响可信度
- 结论是否有证据链
- 正式 artifacts 是否完整，按 [artifacts-schema.md](artifacts-schema.md) 检查阻塞条件。
- 图表证据是否符合 [figure-evidence-rules.md](figure-evidence-rules.md)，重点查单位、阈值、对照组、误差、敏感性和图后结论句。
- 创新点是否通过 [innovation-generator.md](innovation-generator.md) 的 baseline/ablation/evidence chain 检查。
- 建模路线是否通过 [a-problem-decision-tree.md](a-problem-decision-tree.md) 和 [a-problem-pattern-library.md](a-problem-pattern-library.md) 的题型、基准模型、结果表和验证动作检查。
- 六项评分维度是否都有可见得分证据，详见 [scoring.md](scoring.md)

## 证据链复查表

对摘要、结论和强 claim 逐条建表：

| claim | 数值/结论 | 正文位置 | 图/表/公式 | 附录/支撑材料 | 状态 |
| --- | --- | --- | --- | --- | --- |

规则：

- 摘要数字必须能追到正文、图表、公式、日志、附录或支撑材料。
- 正文引用的支撑文件必须存在，文件名、用途和输出结果一致。
- 关键结果不能只出现在摘要或结论。
- 指标类型要一致：最优值、终端值、阈值时刻、持续时间、误差和效率不能混用。
- 每条 claim 应能映射到 `claim_ledger.csv`；如果涉及创新，还要映射到 `innovation_ledger.csv`。
- 若使用 AI 辅助内容、代码、翻译、润色或验证，应能映射到 `ai_usage_log.md` 和最终提交材料中的披露位置。

## 一致性反例检查

- 图题、表题和正文情景编号是否一致。
- 摘要最优方案、正文结果表和附录输出是否一致。
- 表头单位、符号表单位和代码单位是否一致。
- 参考文献是否支撑核心理论、领域参数或算法来源。
- 支撑材料是否包含完整结果表、运行说明和必要脚本。
- `result_registry.csv` 中 `validation_status=paper_ready` 的结果是否全部能被正文或附录找到。
- `figure_evidence.csv` 中 `validation_status=paper_ready` 的图是否均有可读图题、单位和图后结论句。

## 终审规范清单

- 先查官方规则或用户提供规则，并更新 `submission_checklist.md`，再检查页数、附件、命名、AI-use 声明和提交格式。
- 匿名赛制下检查标题页、正文、附录、文件名、PDF metadata、代码注释和支撑材料说明。
- 检查正文页码、附录起点、参考文献格式、图表编号、公式编号和交叉引用。
- 检查附件清单：论文提到的 Excel、代码、图表、日志和完整结果文件必须存在。

## A 题主赛题通用高分信号

- 现实原型或业务机理交代充分，能说明模型从哪里来、服务什么决策。
- 题目交付物完整，关键结果有表格、图、公式或附件支撑。
- 核心数学归结准确，目标函数、变量、约束与题意一致。
- 建模与求解过程充分，关键方程量纲一致，约束闭合。
- 至少有基准方案、对照实验、消融分析或多模型定量对比。
- 对极端工况、边界条件、关键参数做验证或敏感性分析。
- 创新点能被数学表达和结果证明，而不是只堆模型名词。
- 给出应用解释、适用范围、局限性和可落地建议。

## 常见扣分信号

- 功率平衡或能量守恒不明确
- 关键交付结果缺失
- 验证环节单薄
- 排版差
- 参考文献或图表不规范
- 摘要或结论没有对应证据
- 只写方法，不写可复核结果

## 输出格式

- 发现的问题
- 影响范围
- 最小修复方案
- 是否需要回到建模或代码重做
- 对应评分维度

## Optimization feasibility review

For optimization, scheduling, routing, allocation, and solver-backed results, check:

- Whether the final plan still has hard-constraint violations, positive slack, or softened constraints.
- Whether any violation is labeled correctly as `relaxed diagnostic solution` or proven as an `unavoidable gap`, instead of being described as strictly feasible.
- Whether every optimization or scheduling subproblem has a complete result summary table with core numbers in the table.
- Whether baseline, ablation or comparison, sensitivity analysis, and solver/run record are present when the paper claims improvement or innovation.
- Whether solver status, optimality gap, runtime, variable count, constraint count, and parameter/weight scan evidence are available.
- Whether there are blank subplots, division-by-zero denominators, unexplained indicators, unstable rankings, or metrics whose physical meaning is not interpretable.
