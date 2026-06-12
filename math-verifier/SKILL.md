---
name: math-verifier
description: Use when 高教社杯/CUMCM 数学建模方案需要在代码、图表、摘要或最终提交前独立核验公式、单位、量纲、约束、边界情形、可行性措辞、假设或论文就绪数学结论。
---

# 数学核验

## 用途

Verify the math before it becomes paper language. Treat this skill as an independent hard gate for dimensional consistency, formula back-substitution, boundary behavior, feasibility claims, and assumption loss.

核心规则：不要解新问题，也不要发明缺失的模型部件。只按题面、建模交接、符号表和证据产物核验已经写出、算出或声称的内容。

国一候选门槛：数学核验必须保证题目贴合、建模洞察、证据可信、可复现、边界清楚有公式、单位、约束和边界案例支撑；这是提交质量门槛，不承诺获奖。漂亮结论只要无法回代、无法闭合单位或无法说明边界，就不能进入论文就绪状态。

硬门禁：单位、定义域、约束、边界条件、公式回代或可行性措辞只要未检查、不一致或未知，模型结论就不能进入论文就绪状态。

返回规则：本技能只把发现返回 `math-hub`。可以建议修复面，但不能直接路由、派发或调用另一个技能。

## 必要输入

Collect the smallest available set:

- current problem/subquestion and required deliverables;
- `problem_brief.md`, `model_handoff.md`, `assumption_log.csv`, and `symbol_table.csv` when available;
- formulas, constraints, objective, parameter values, units, and domains;
- result tables, `result_registry.csv`, `run_record.csv`, and `claim_ledger.csv` for computed claims;
- official or user-provided tolerances, hard constraints, and feasibility definitions.

If a needed source is missing, mark the affected check `blocked` or `diagnostic-only`; do not fill the gap from memory.

## 核验检查

Run only checks relevant to the active claim or model route:

| Check type | What to verify |
| --- | --- |
| `dimensional` | Every term in an equation has compatible dimensions and declared units. |
| `domain` | Variables, indices, sets, binary/slack roles, and parameter ranges match the problem and code handoff. |
| `constraint` | Hard constraints are represented, measurable, and not silently softened. |
| `formula back-substitution` | Substitute baseline, boundary, or reported values into formulas to catch algebra/sign/unit errors. |
| `boundary` | Extreme, zero, saturated, or limiting cases behave in the expected direction. |
| `conservation` | Flow, mass, count, probability, budget, or balance laws close within tolerance. |
| `feasibility wording` | Claims use strict feasible, relaxed diagnostic, candidate, not identifiable, or unavoidable gap correctly. |
| `assumption loss` | Simplifications name what realism, constraint, or uncertainty they remove. |
| `result schema` | The table/figure needed to prove the claim can hold all required units, scenarios, baselines, and tolerances. |

不要奖励复杂度。单位闭合、边界已检查的简单模型，优先于隐藏可行性缺口的复杂模型。

## 产物约定

When maintaining `math_verification.csv`, use:

```csv
check_id,subquestion,artifact,location,claim_id,check_type,input_ref,expected_relation,observed,status,severity,minimum_fix,owner
```

Statuses:

- `pass`: check is directly satisfied by cited evidence.
- `blocked`: required source, unit, formula, constraint, or tolerance is missing.
- `fail`: evidence contradicts the model or claim.
- `diagnostic-only`: check reduces uncertainty but is not enough for paper-ready use.

Severity:

- `P0`: contradiction, fabricated value, missing required deliverable, or rule-breaking feasibility wording.
- `P1`: unit, constraint, boundary, reproducibility, or validation gap blocking paper-ready status.
- `P2`: weak assumption explanation, missing stress case, or fragile boundary claim.
- `P3`: wording, notation, or presentation cleanup after the math is sound.

## 输出约定

Return:

```text
Verification lock:
Checked artifacts:
Hard check results:
P0/P1 blockers:
Claims allowed as paper-ready:
Claims downgraded to candidate/diagnostic:
Assumption and boundary losses:
Math verification rows:
Smallest repair order:
Return to hub: math-hub
Recommended repair surface:
```

`Recommended repair surface` may name `model`, `code`, `table`, `figure`, `abstract`, `latex`, or `hub QC`, but the handoff always returns to `math-hub`.

## 红线

Stop and mark a blocker when:

- a symbol has no unit, domain, or first-use definition;
- two terms are added or compared with incompatible dimensions;
- a hard constraint is absent from the model, code, or feasibility check;
- a reported result cannot be reproduced by formula back-substitution or a cited run;
- a relaxed, violated, or candidate solution is described as strict feasible;
- a boundary case contradicts the claimed mechanism or trend;
- an assumption removes a real constraint without naming the loss;
- verification starts designing a new route instead of checking the current one.

Do not hide failed checks in prose. Downgrade the claim or return the missing evidence to `math-hub`.
