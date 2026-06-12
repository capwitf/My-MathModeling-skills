# 竞赛图表模板

这些是常见数学建模竞赛图表的 matplotlib 轻资产模板。使用时把对应脚本复制到当前项目的 `qX/src/` 或绘图目录，再按当前题目的列名、单位、图注和 `figure_evidence.csv` 证据行改写。

## 模板

- `relative_change_heatmap.py`：相对基准的场景或方法比较，适合百分比变化或相对变化。
- `pareto_frontier.py`：Pareto、权衡或前沿图，可标出选定方案。
- `sensitivity_tornado.py`：单因素灵敏度或压力测试龙卷风图。
- `feasibility_diagnostics.py`：约束残差、违反量、通过/失败诊断或求解器健康检查。
- `dispatch_time_series.py`：路线、调度、库存、功率平衡或状态轨迹时间序列。

## 规则

- 这些脚本只能作为起点，不能把未改过的示例图当成最终图。
- 精确数值放在表格里；图用于展示模式、机制、权衡、鲁棒性或诊断。
- 每张论文图仍需补齐 `figure_evidence.csv` 字段：claim id、源表、图注、图后结论、风险说明和验证状态。
- 正式项目使用前必须删除示例数据。
