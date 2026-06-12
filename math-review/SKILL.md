---
name: math-review
description: Use when 高教社杯/CUMCM 数学建模论文、模型、结果集、摘要、图表包或提交草稿需要评委视角审查、评分风险映射、结论/证据检查、创新审查或可能追问准备。
---

# Contest Review

## 用途

Audit contest work from the judge's side of the table. Treat every result, figure, formula, paragraph, and package file as something a tired but sharp reviewer must verify quickly.

核心规则：审查是硬门禁，不是安慰性总结。结论只有在相关性、洞察、可信度、可复现性和边界措辞都可见时才可接受。

国一候选门槛：审查目标是让论文接近“国一候选”，但不承诺获奖。所有高价值结论都要同时显示题目贴合、建模洞察、证据可信、可复现、边界清楚；若只是格式合规或语言漂亮，仍按 P2 或更高风险处理。

硬门禁：只要当前论文、证据产物、代码包、匿名性表面或合规记录中仍有开放的 P0 或 P1 问题，最终提交就必须阻塞。

返回规则：本技能只把发现返回 `math-hub`。可以建议修复面，但不能直接路由、派发或调用另一个技能。

## 审查视角

Map findings to these scoring dimensions:

1. Real-world prototype or source of the mathematical model.
2. Accuracy and rationality of the mathematical reduction.
3. Correctness and theoretical level of the modeling process.
4. Model innovation.
5. Application prospect of the model or software.
6. Overall presentation.

Do not use generic praise or generic criticism. Every issue must say which dimension loses points, what evidence is missing, and the smallest repair that would change the judge's view.

## 评委可读性门禁

Treat first-pass readability as a scoring overlay, not a separate official dimension. It mainly maps to dimension 6 / overall presentation, but it can also expose weaknesses in dimensions 1-3 when the model route, equations, or evidence cannot be followed quickly.

Check reading cost before calling a paper national-first quality:

- formula dumping: formulas appear without task meaning, variable explanation, transition text, or nearby validation.
- logic jumps: the paper moves from problem statement to model, model to algorithm, or result to conclusion without explaining the bridge.
- figure/table chaos: figures and tables are dense, out of order, missing units, or not followed by a conclusion sentence.
- notation burden: too many symbols are introduced before the reader sees what decision, state, metric, or constraint they serve.
- section rhythm: long derivations, code-like detail, or appendix-level diagnostics interrupt the main answer.

可读性问题不是普通润色：if a tired judge cannot identify the route, claim, evidence, and boundary within one pass, mark a readability risk. A readability risk may stay P3 only when evidence is sound and the fix is local wording; it 可升级为 P2 when reading cost hides the modeling idea, result table, validation, or required deliverable.

## 严重级别门禁

Use these severities:

| Severity | Blocks | Meaning |
| --- | --- | --- |
| P0 | submission | Fabrication, contradiction, anonymity leak, rule violation, missing required deliverable, or claim unsupported by any source |
| P1 | paper-ready status | Hard constraint, model route, feasibility, reproducibility, code/run, figure evidence, or AI disclosure gap |
| P2 | national-first quality | Weak validation, unclear boundary, crowded figure, notation drift, fragile innovation, or missing comparison |
| P3 | polish only | Style, wording, ordering, or minor layout issue after evidence is sound |

P0/P1 are blockers and must be resolved before final submission. P2 must be resolved or explicitly accepted with risk notes. P3 is non-blocking and must not distract from unresolved P0/P1/P2.

## 量化评分风险

Each finding must estimate how it can cost points in the judge's scoring lens. Use `score_risk` as a compact risk label, not a fake exact score.

Suggested labels:

- `fatal`: likely disqualifies or invalidates the answer surface.
- `major`: likely prevents national-first quality or paper-ready status.
- `moderate`: likely visible to reviewers and damages trust or clarity.
- `minor`: polish or local readability risk after evidence is sound.

When maintaining `review_findings.csv`, every P0/P1/P2 row must include:

- scoring dimension number or name;
- `score_risk`;
- missing evidence or contradiction;
- `minimum_fix` that would change the judge's view;
- owner or repair surface;
- status.

Do not assign a low `score_risk` to an unsupported final claim just because the prose is polished.

## 结论与证据约定

For each high-value claim, verify:

- exact subquestion and required deliverable;
- body location and whether the claim appears in abstract, conclusion, figure caption, table title, or appendix;
- evidence id in `claim_ledger.csv`, `result_registry.csv`, `figure_evidence.csv`, a formula, a checked table, or a run log;
- source script, input data, parameters, seed, and run id when computed;
- feasibility wording: strict feasible, relaxed diagnostic, candidate, not identifiable, or unavoidable gap;
- baseline, denominator, scenario, and unit for improvements or innovation claims;
- boundary sentence naming assumptions, uncertainty, non-identifiability, or contest-rule limits.

If a claim cannot pass this contract, downgrade it, remove it, or recommend the smallest repair surface for hub QC to decide.

## 创新与追问风险

Innovation claims require a baseline or ablation, a changed model component, and evidence that the change improves task fit, feasibility, robustness, interpretability, or reproducibility. Do not accept fashionable method names, extra plots, tuned hyperparameters, or complex wording as innovation.

For judge-question preparation, write likely questions only from real weak points:

- Why does this model answer the exact subquestion?
- What breaks if the strongest assumption is false?
- How do you know the constraints are feasible?
- Where can the cited number be reproduced?
- What is new beyond the baseline?
- Why is this figure in the main body?
- What official rule or AI-use disclosure could block submission?

Each likely question must map to evidence or a repair action. Do not create a separate defense workflow unless explicitly requested.

## 输出约定

Return compact findings first:

```text
Review lock:
Submission status:
Top findings:
P0/P1 blockers:
Scoring dimension map:
Claim/evidence failures:
Innovation risks:
Readability risks:
Likely judge questions:
Smallest repair order:
Return to hub: math-hub
Recommended repair surface:
```

When maintaining `review_findings.csv`, use:

```csv
finding_id,severity,dimension,score_risk,artifact,location,issue,impact,minimum_fix,owner,status
```

`Recommended repair surface` may name `model`, `code`, `figure`, `abstract`, `latex`, `table`, `compliance`, or `hub QC`, but the handoff always returns to `math-hub`.

## 红线

Stop and mark a blocker when:

- the paper answers a nearby problem instead of the required deliverable;
- a conclusion has no evidence id or cites a non-paper-ready row;
- feasibility wording hides a relaxed, violated, candidate, or diagnostic result;
- a figure has no claim id, caption, post-figure conclusion, or risk note;
- code/support files cannot reproduce core numbers cited in the paper;
- innovation wording lacks baseline, ablation, or comparison evidence;
- official rules, anonymity, AI disclosure, or package requirements are unknown before final submission;
- the review starts routing, dispatching roles, calling another skill, or building a DAG without returning to `math-hub`.

Do not compensate for missing evidence with stronger prose. Reduce the claim or repair the evidence chain.
