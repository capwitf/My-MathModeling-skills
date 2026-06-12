# 轻资产库索引

## 用途

整理本技能包中已经存在的可复用资产。本文件是索引，不是工作流；用它找到当前写作或建模任务所需的最小模板、句式、图表或脚手架。

## 论文风格资产

| 需求 | 资产 |
| --- | --- |
| 国奖式写作语气 | `math-templates/references/national-prize-style-profile.md` |
| 章节格式控制 | `math-templates/references/section-format-controls.md` |
| 假设与评价控制 | `math-templates/references/assumption-evaluation-controls.md` |
| 竞赛论文语言护栏 | `math-templates/references/contest-language-guardrails.md` |
| 段落流检查 | `math-templates/references/paragraph-flow.md` |
| 官方优秀论文观察 | `math-templates/references/official-exemplar-notes.md` |
| 完整章节骨架 | `math-templates/assets/contest-project-template/paper/section_templates_national.md` |
| 段落级句式 | `math-templates/assets/contest-project-template/paper/paragraph_phrases_national.md` |
| 详细章节段落模板 | `math-hub/references/writing-templates.md` |

规则：论文可复用模板从 `math-templates` 暴露；`math-hub` 中的质控、一致性和评分语言保持归属，除非用户明确要求复制成独立写作包。

## 论文片段资产

| 需求 | 资产 |
| --- | --- |
| 单个子问题写作指南 | `math-templates/assets/contest-project-template/paper/problem_guide_template.md` |
| 片段交接协议 | `math-templates/assets/contest-project-template/paper/fragments/fragment_protocol.md` |

## 代码与复现资产

| 需求 | 资产 |
| --- | --- |
| 单问计算脚手架 | `math-templates/assets/contest-project-template/problem_template/src/compute_template.py` |
| 单问绘图脚手架 | `math-templates/assets/contest-project-template/problem_template/src/plot_template.py` |
| 回归测试脚手架 | `math-templates/assets/contest-project-template/problem_template/tests/test_pipeline_template.py` |
| 一键复现正式运行 | `math-templates/assets/contest-project-template/reproduce_all.py` |
| 项目清单模板 | `math-templates/assets/contest-project-template/project_manifest_template.md` |

## 登记表资产

| 需求 | 资产 |
| --- | --- |
| 运行记录 | `math-templates/assets/contest-project-template/registries/run_record.csv` |
| 结果登记表 | `math-templates/assets/contest-project-template/registries/result_registry.csv` |
| 图像证据表 | `math-templates/assets/contest-project-template/registries/figure_evidence.csv` |
| 数值诊断表 | `math-templates/assets/contest-project-template/registries/numerical_diagnostics.csv` |

## 图表资产

| 需求 | 资产 |
| --- | --- |
| 图表模板索引 | `math-figure/references/chart-template-index.md` |
| 相对变化热力图 | `math-figure/assets/chart-templates/relative_change_heatmap.py` |
| Pareto/frontier 图 | `math-figure/assets/chart-templates/pareto_frontier.py` |
| 灵敏度龙卷风图 | `math-figure/assets/chart-templates/sensitivity_tornado.py` |
| 可行性诊断图 | `math-figure/assets/chart-templates/feasibility_diagnostics.py` |
| 调度/时间序列图 | `math-figure/assets/chart-templates/dispatch_time_series.py` |

规则：可执行图表模板保留在 `math-figure`；论文资产可以引用它们，不复制代码。

## 迁移建议

- 当资产是论文骨架、句式库、风格说明或可复用 Markdown 模板时，迁移到 `math-templates`。
- 当资产是可执行绘图代码或图像专项说明时，保留在 `math-figure`。
- 当资产是质控、一致性、评分或门禁语言时，保留在 `math-hub`。
- 优先在本索引中添加指针，不重复复制内容。
