# 论文片段协议

## 使用场景

当多个轮次或多个对话分别撰写各子问题片段时，使用本文件控制边界。它只规定片段交接方式，不强制项目工作流。

## 子问题提示格式

```text
你只负责论文片段 qX。不要编辑 paper/main.tex 或其他子问题片段。

先读取：
1. session_log.md or hub_state.json
2. problem_brief.md
3. deliverable_matrix.csv
4. paper/qX_guide.md
5. results/qX 中的正式结果表、图、诊断文件和 qX_figure_plan.csv

写入 paper/fragments/qX.md，内容包括：
- 建模思路
- 变量、参数与约束
- 求解方法
- 来自正式结果表的主要结果
- 建议使用的图表
- 本问结论
- 不得进入最终正文的诊断性或不确定内容

只使用正式结果表、登记表或已核查源文件中的数值。
```

## 合并规则

最终控制者负责 LaTeX 转换、图号、表号、一致性、页数限制、匿名性检查和最终编译。
