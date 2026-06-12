# MY MathModeling Skills

![Skills](https://img.shields.io/badge/skills-13-2563eb)
![License](https://img.shields.io/badge/license-MIT-16a34a)
![Focus](https://img.shields.io/badge/focus-CUMCM%20%2F%20Math%20Modeling-f97316)
![AI Use](https://img.shields.io/badge/AI%20use-disclosure%20aware-7c3aed)

面向高教社杯/CUMCM 风格数学建模竞赛的 Codex skill 包。这个仓库保留的是“厚质量门版”：它不只给建模建议，还会追问题面交付物、证据链、复现记录、图表来源、一致性、匿名合规和 AI 使用披露。

默认质量目标是“国一候选”：题目贴合、建模有洞察、证据可信、结果可复现、边界说清楚。它不是获奖承诺，而是一套更严格的赛中工作门槛。

## Language Boundary

目标是让 skill 的产出接近过一水平，不是限制 skill 本身必须全中文。skill 在判断、审查、建模和代码交接时可以使用英文；该英文就用英文。只有论文正文、可复制模板、项目清单、复现说明等交付文件默认中文竞赛文风。英文技术术语、算法名、字段名、代码接口、文件名、英文文献术语和官方规则原文可以保留，不因中文化牺牲建模判断、证据链或可复现性。

## Highlights

- 13 个数学建模专用 skills，覆盖读题后的建模、验证、代码、图表、摘要、LaTeX、审查、合规和模板资产。
- 以 `math-hub` 做质量枢纽，维护当前分问、交付物、证据状态、开放阻塞和下一步模块。
- 强调 paper-ready 证据链：最终摘要、正文结论、结果表和图表必须能追溯到模型、代码、运行记录或可靠来源。
- 保留竞赛论文常见硬门：单位、边界、可行性措辞、数值诊断、图后结论、模板残留、匿名性和提交包检查。
- 支持 AI 辅助，但不允许把 AI 输出直接包装成最终结论；需要按官方规则记录、核验和披露。

## Skills

| Skill | 作用 |
| --- | --- |
| `math-hub` | 质量枢纽和最终门禁，锁定题目范围、分问交付物、证据状态、合规风险和下一模块。 |
| `math-model` | 建模路线设计，定义变量、假设、公式、约束、算法、验证、鲁棒性和代码交接。 |
| `math-verifier` | 独立核验公式、单位、量纲、边界、约束、可行性措辞和数学结论。 |
| `math-code` | 实现计算、复现实验、生成表图、记录运行结果、诊断数值稳定性。 |
| `math-figure` | 规划、生成和审查图表证据，确保一图服务一个主结论。 |
| `math-table` | 修复符号表、记号表和结果表，检查单位、来源、首用位置和可读性。 |
| `math-abstract` | 写作或审查摘要、关键词、亮点句和第一页高密度结论。 |
| `math-latex` | 维护竞赛 LaTeX 模板，处理公式、表格、图、浮动体、PDF 编译和版面检查。 |
| `math-consistency` | 跨摘要、正文、表图、附录、登记表和代码结果做一致性审查。 |
| `math-review` | 从评委视角识别 P0/P1/P2/P3 风险、扣分点、可读性问题和最小修复项。 |
| `math-compliance` | 检查官方规则、匿名性、页数、附录、支撑材料、复现和 AI 使用披露。 |
| `math-literature` | 轻量文献检索、引用核验、标准/政策/参数来源确认和 claim-to-citation 映射。 |
| `math-templates` | 提供论文结构、句式库、代码/绘图脚手架、登记表和项目模板资产。 |

## Quick Start

Clone this repository:

```powershell
git clone https://github.com/capwitf/MY-MathModeling-skills.git
cd MY-MathModeling-skills
```

Install into your local Codex skills directory on Windows:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force .\math-* "$env:USERPROFILE\.codex\skills\"
```

Install on macOS/Linux:

```bash
mkdir -p ~/.codex/skills
cp -R math-* ~/.codex/skills/
```

Then call a skill explicitly in Codex, for example:

```text
使用 $math-hub 审查当前数模方案是否能进入 paper-ready。
使用 $math-model 为问题二设计变量、约束、验证和代码交接。
使用 $math-code 根据 model_handoff.md 复现计算并更新结果登记表。
```

## Recommended Contest Flow

1. Use `math-hub` to lock the active problem, subquestion, deliverables, source files and highest blocker.
2. Use `math-model` to produce a route with variables, objective, constraints, units, validation and result schema.
3. Use `math-verifier` before trusting formulas, units, constraints or feasibility language.
4. Use `math-code` only when the handoff is explicit enough that code does not need to invent parameters or output schema.
5. Use `math-figure`, `math-table`, `math-abstract` and `math-latex` to turn verified evidence into paper-facing material.
6. Use `math-consistency`, `math-review` and `math-compliance` before final submission.

## Evidence And Paper-Ready Rules

- A final claim must trace to a source, model, run, table, figure, formula or verified registry row.
- Candidate, diagnostic, stale, relaxed or unverifiable output should not appear as a final abstract or conclusion claim.
- Code-generated numbers need command, input, parameters, output path, run status and validation status.
- Figures are evidence only when their source output, unit, scenario, caption, post-figure conclusion and validation status are known.
- Robustness analysis should match the actual risk: weights, thresholds, fitted parameters, solver tolerances, stochastic runs or fragile assumptions.
- Do not use a fashionable method name as evidence. The model must fit the task mechanism and deliverable.

## AI Use Rules

Official competition rules always override this README.

- Track AI-assisted work when the official rules require it, especially adopted text, code, figures, tables, claims and summaries.
- Keep `ai_usage_log.md`, `ai_claim_disclosure.csv` or equivalent records when claim-level traceability is needed.
- Do not put AI disclosure text into the abstract, body prose, code comments, generated result tables or figure canvases unless the official rule explicitly asks for it.
- Do not allow AI to invent data, formulas, units, references, official rules, solver behavior or final conclusions.
- Human verification is required before any AI-assisted claim becomes paper-ready.
- Final wording, anonymity checks and package readiness should go through `math-compliance`.

## Repository Layout

```text
math-*/SKILL.md              skill instructions
math-*/agents/openai.yaml    display metadata and default prompts
math-*/references/           detailed protocols and checklists
math-templates/assets/       reusable paper/code/plot assets
tests/                       contract tests for the skill pack
```

## Validation

Run the contract tests:

```powershell
python -m unittest tests.test_skill_pack_contract
```

Or, if `pytest` is available:

```powershell
python -m pytest -q
```

## License

MIT License. See [LICENSE](LICENSE).
