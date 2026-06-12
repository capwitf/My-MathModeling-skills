# 代码手角色说明

## 目标

把建模手的公式无损落成可执行代码，并产出可以直接进论文的表、图和数值。代码手负责保证计算步骤正确、可复现、可审计。

## 核心要求

- 先做防御性读取，再做建模映射。
- 做 EDA，识别分布、缺失、离群、异常时段。
- 保证每个约束都能追溯到公式来源。
- 所有随机算法必须显式设置并记录随机种子；若题面或团队规范指定种子，则以其为准，不把某个固定数值写成通用推荐。
- 优先向量化和分块，避免低效循环。
- 对 TB/GB 级数据优先考虑分块读取、列选择、类型压缩、延迟计算或 Polars。
- 在代码注释中标明关键公式来源，例如 `# Eq. (3-2): capacity constraint`。

## 必做模块

- 数据读取与 schema 校验
- 缺失值与离群点处理
- 归一化 / 标准化
- 核心求解与结果导出
- 断言与异常捕获
- 高分辨率绘图
- EDA 报告：字段类型、行列规模、缺失率、异常率、分布摘要、关键相关性、时间覆盖范围。
- `result_registry.csv`：登记每个可进论文的数值结果、来源表、来源脚本、run id 和验证状态。
- `figure_evidence.csv`：按 [figure-evidence-rules.md](figure-evidence-rules.md) 登记每张图证明的 claim、单位、阈值、误差或约束状态。

## 运行记录 schema

每次正式运行必须生成日志或表格，至少包含：

- 运行时间、脚本入口、代码版本或文件清单。
- 输入文件、输出文件、核心参数、单位换算。
- 随机种子、网格/步长、搜索范围、停止条件。
- 约束违背数量、最大违背量、警告和失败信息。
- 可复现命令。
- 输出 `run_record.csv` 行，并让 `result_registry.csv` 和 `figure_evidence.csv` 引用同一个 `run_id`。

## 优化诊断 schema

用于枚举、启发式、随机优化、非线性优化和仿真优化。

- 基准方案和对照方案。
- 搜索区间、步长/变步长策略、可行性筛选条件。
- 目标函数历史、最优可行值历史、约束违背历史。
- 多种子或重启结果表。
- 最终可行解表和约束检查表。
- baseline/ablation 结果，用于支持 `innovation_ledger.csv`，没有对照不得报告创新收益。

## 数值仿真输出清单

用于 PDE/ODE、网格仿真、阈值判定和时间推进。

- 网格分辨率、时间范围、求解器、停止条件。
- 初始条件、边界条件、界面条件的代码实现说明。
- 阈值附近局部数据表。
- 残差、误差、稳定性或步长敏感性证据。
- 全量结果文件和正文摘要表。

## 调度/状态结果表 schema

按题型选择列，不要强行套用全部字段。

- 实体编号、任务编号、场景编号。
- 状态、动作、资源编号、开始时间、结束时间。
- 关键派生指标、约束状态、异常/故障标记。
- 最终状态、可行性标记、结果来源脚本。

## 默认工程结构

若项目尚无既定结构，默认使用：

```text
data/              原始附件与清洗数据
src/               可运行 Python 脚本
outputs/tables/    论文和附录结果表
outputs/figures/   可进论文的图
logs/              运行日志、警告和求解器信息
paper/             论文源文件、最终图表副本和提交材料
requirements.txt
```

原始附件不改名、不覆盖；若数据较多，可细分 `data/raw/` 与 `data/proc/`。所有计算产物必须进入 `outputs/`，方便论文手和复查手追溯。

## 命名口径

文件名要短、像比赛现场会真的使用的名字：小写 ASCII、题号前缀、清楚缩写。

- 脚本：`run_all.py`, `cfg.py`, `utils.py`, `q1_eda.py`, `q1_prep.py`, `q1_base.py`, `q2_opt.py`, `q2_sim.py`, `q2_eval.py`, `q3_sens.py`, `q3_rob.py`, `q3_viz.py`
- 表格：`q1_desc.csv`, `q1_clean.csv`, `q2_sched.csv`, `q2_rank.csv`, `q3_sens.csv`, `sum_metrics.csv`
- 图：`q1_dist.png`, `q1_missing.png`, `q2_route.png`, `q2_conv.png`, `q3_sens.png`, `fig_arch.png`
- 日志：`run_all.log`, `run_q2_opt.log`, 必要时用 `run_YYYYMMDD_HHMM.log`

避免 `final_final.py`、`new2.csv`、`temp.png`、空格和过长句子式文件名。官方附件只在生成清洗副本时另存，不直接改名。

## 防御规则

- 遇到 OOM、奇异矩阵、不可行解时必须显式捕获。
- 发现负需求、负功率、越界 SOC 等物理错误时必须断言失败。
- 不得用“看起来合理”的常数替代缺失数据。
- 随机森林、K-Means、遗传算法等随机过程必须显式设置随机种子。
- 图像输出默认 `dpi=300` 或更高；避免花哨特效，优先保证信息密度和可读性。

## 输出要求

- `requirements.txt`
- Python 脚本
- 结果表
- 图表
- 执行说明
- `result_registry.csv`
- `run_record.csv` 或等价日志
- `figure_evidence.csv` 表
- `diagnostics` 表或日志，覆盖收敛、可行性、敏感性、约束违背和异常情况

Python 脚本应尽量符合 PEP 8，包含 `main()` 入口、路径配置、日志或运行记录、输出目录创建和失败信息。

## 说明风格

- 图表要学术化、克制、可复现。
- 结果说明要让论文手能直接拿去写结果分析。
- 对论文手说明每张图表揭示的变量关系、异常点、边界效应和可引用的关键数值。

## Optimization result schemas

Use these schemas for optimization, scheduling, routing, allocation, and solver-backed subproblems. Choose the relevant columns; do not force irrelevant fields.

### Result summary table

Required columns:
- `problem_id`, `scenario_id`, `entity_id` or `solution_id`;
- decision variables with units;
- objective value and main derived metrics with units;
- feasibility status: `strict_feasible`, `relaxed_diagnostic`, or `unavoidable_gap`;
- violated constraint count, maximum violation, and slack total when applicable;
- baseline value, improvement denominator, and improvement percentage when claiming improvement;
- source script, source data, random seed or solver run id.

### Solver run record

Required columns:
- `run_id`, `problem_id`, `solver`, `solver_version`;
- variable count, constraint count, integer/binary variable count when applicable;
- status, objective value, best bound, optimality gap, runtime, iteration/node count;
- stopping rule, tolerance, random seed, and warning message;
- output table path, convergence figure path, and log path.

### Parameter or weight scan table

Required columns:
- `scan_id`, parameter name, tested value, value source or rationale;
- objective value, feasibility status, key metrics, and ranking/order change;
- baseline parameter set, delta from baseline, and sensitivity conclusion;
- note explaining why the scan grid is small when only a few points are tested.

### Constraint violation or unsatisfied sample diagnostic table

Required columns:
- `sample_id`, `constraint_id`, constraint type, hard/soft flag;
- left-hand side, right-hand side, unit, violation amount, and tolerance;
- diagnosis: data conflict, physical-boundary conflict, modeling error, or solver failure;
- recommended action: keep as unavoidable gap, adjust model, inspect data, or rerun solver.
