# Contest Chart Selection

Use this file when a 高教社杯/CUMCM result table needs a paper figure. This is a 国赛 chart triage card: the choice should be based on `结论类型 + 数据结构 + 评委阅读任务`, not on which chart looks impressive.

## Selection Rule

Start with the sentence the figure must support:

```text
图X需要说明：[对象/场景]下，[指标]呈现[趋势/差异/边界/机制]，因此[回答子问题结论]。
```

If this sentence cannot be written, keep the evidence as a table or postpone plotting.

## Routing Table

| 结论类型 | 数据结构 | 评委阅读任务 | 首选证据 | 主体条件 |
| --- | --- | --- | --- | --- |
| 精确值、查表答案、最终排名 | 少量数值或完整方案表 | 快速核对答案 | 精确值优先表格 | 只有当图能显示表格看不出的模式时才画 |
| 趋势、阈值、阶段变化 | 时间、迭代、距离、参数序列 | 看变化方向和临界点 | 折线、阶梯线、局部放大 | 标出单位、阈值、关键点 |
| 方案、场景、方法对比 | 分类 + 指标 | 比较谁更好、差多少 | 分组柱状图、差值图、相对变化热力图 | 标签可读，基准明确 |
| 权衡和方案选择 | 两个或多个目标 | 理解取舍与选点理由 | Pareto/frontier、选点标记 | 选中方案必须可解释 |
| 鲁棒性、灵敏度、压力测试 | 参数扰动、权重扰动、场景扰动 | 判断结论是否稳定 | 灵敏度曲线、龙卷风图、压力热力图 | 必须有基准和测试范围 |
| 可行性或求解健康 | 约束残差、违反量、收敛记录 | 判断结果是否可信 | 诊断图 | 默认附录，除非检验是核心贡献 |
| 机制、分问递进、状态转移 | 变量、公式、流程、输入输出关系 | 缩短模型解释 | 机制图手工绘制、流程图、状态轨迹 | 每个框或箭头对应变量、公式、约束、结果或分问关系 |
| 空间、路径、覆盖、几何关系 | 坐标、轨迹、区域、距离 | 看位置关系和边界 | 平面示意、轨迹图、覆盖图 | 坐标系、比例、关键对象必须清楚 |

## Contest Defaults

- Table first when exact values matter.
- One main claim per figure.
- Prefer two clear panels over six crowded panels.
- Use color as reinforcement, not the only carrier of meaning.
- Mechanism diagrams are usually manually drawn or editable; do not force a fixed matplotlib template.
- Put raw diagnostics in appendix unless they directly defend a final claim.
