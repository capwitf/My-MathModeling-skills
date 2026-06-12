---
name: math-consistency
description: Use when 高教社杯/CUMCM 数学建模论文、摘要、正文、表图、附录、登记表、结论、数值、单位、场景标签、可行性措辞或提交包需要跨材料一致性审查。
---

# 竞赛一致性审查

## 用途

Audit whether the same claim means the same thing everywhere it appears. Compare abstract, body, tables, figures, appendix, code outputs, and registries for value, unit, scenario, baseline, feasibility, and wording drift.

核心规则：论文可以压缩证据，但不能改变结论的数值、分母、单位、场景、验证状态或确定性等级。

国一候选门槛：一致性审查保证题目贴合、建模洞察、证据可信、可复现、边界清楚在摘要、正文、表图、附录和支撑材料中保持同一含义；这是提交质量门槛，不承诺获奖。任何数值、单位、场景或证据状态漂移都会削弱国一候选质量。

硬门禁：只要任何高价值结论缺少一致的证据行，或在不同材料中措辞冲突，摘要、结论、正文主图和最终结果表都必须阻塞。

返回规则：本技能只把发现返回 `math-hub`。可以建议修复面，但不能直接路由、派发或调用另一个技能。

## 必要输入

Collect only the current draft and active evidence set:

- abstract, body sections, figure captions, table titles, conclusion, appendix, and support notes;
- `claim_ledger.csv`, `result_registry.csv`, `figure_evidence.csv`, `run_record.csv`, and `symbol_table.csv` when available;
- `math_verification.csv` and `numerical_diagnostics.csv` when the claim depends on math or solver evidence;
- `ai_usage_log.md` or `ai_claim_disclosure.csv` only for final-submission audits when AI-use disclosure is required;
- official formatting or support-material rules when consistency affects submission readiness.

If a source is missing, mark only the affected claim as `blocked` or `diagnostic-only`.

## 审查流程

1. Extract high-value claims from the abstract, body, figure captions, table titles, conclusion, and appendix.
2. Link each claim to `claim_id`, `result_id`, `figure_id`, `run_id`, or an official/problem source.
3. Compare numbers, units, scenario labels, baselines, denominators, signs, ranks, and feasibility wording.
4. Check that abstract and conclusion contain only `paper_ready` claims.
5. Check that figures do not contain exact values absent from tables or registries.
6. Check that appendix/code/support files reproduce or explain every main-paper result they support.
7. Downgrade or remove claims whose validation status, wording, or evidence source is inconsistent.

## 一致性规则

- `abstract` may summarize but not introduce a new claim.
- `body` must define each result before the abstract or conclusion relies on it.
- `figure` captions must match `figure_evidence.csv` and nearby prose.
- `table` values must match `result_registry.csv` and cited run outputs.
- `appendix` must not contradict the main paper's feasibility, unit, or scenario wording.
- `claim_ledger.csv` owns paper-facing claim status; `result_registry.csv` owns exact computed values.
- Final language requires `claim_ledger.csv.status=paper_ready` or an explicitly approved equivalent status, and backing `result_registry.csv` or `figure_evidence.csv` rows with `validation_status=paper_ready` when the claim depends on computed or figure evidence.
- Units and scenario names must match `symbol_table.csv` and the hub's unified wording.

## 摘要布尔项

When the audit is used as a hub or final-gate input, include these compact fields in addition to row-level findings:

- `units_consistent`: `true` only when paper text, result tables, figure axes/colorbars, symbol table, and code registries agree for the checked claims;
- `notation_consistent`: `true` only when symbols, subscripts, scenario names, indices, and feasibility labels keep the same meaning across checked artifacts;
- `claims_consistent`: `true` only when all high-value abstract/conclusion/table/figure claims have matching evidence and acceptable validation status;
- `blocked_claims`: claim ids that prevent paper-ready or final status.

Use `unknown -> blocked` for any field whose sources were not inspected.

## 产物约定

When maintaining `consistency_audit.csv`, use:

```csv
audit_id,claim_id,artifact_a,location_a,artifact_b,location_b,mismatch_type,expected,observed,severity,minimum_fix,owner,status
```

Common `mismatch_type` values: `value`, `unit`, `scenario`, `baseline`, `denominator`, `rank`, `feasibility`, `certainty`, `validation_status`, `missing_evidence`, `stale_template`, `ai_disclosure`.

Severity:

- `P0`: contradiction, unsupported final claim, missing required deliverable, anonymity/rule conflict, or fabricated-looking evidence.
- `P1`: result, unit, figure, run, verification, AI disclosure, or appendix mismatch blocking paper-ready status.
- `P2`: weak wording alignment, missing risk note, stale but non-final artifact, or accepted diagnostic caveat.
- `P3`: minor wording or formatting drift after claims are sound.

## 输出约定

Return:

```text
Consistency lock:
Artifacts compared:
Paper-ready claim count:
units_consistent:
notation_consistent:
claims_consistent:
Mismatches by severity:
Abstract/body/table/figure/appendix conflicts:
Claims downgraded or removed:
Consistency audit rows:
Smallest repair order:
Return to hub: math-hub
Recommended repair surface:
```

`Recommended repair surface` may name `abstract`, `body`, `table`, `figure`, `code`, `verifier`, `compliance`, or `hub QC`, but the handoff always returns to `math-hub`.

## 红线

Stop and mark a blocker when:

- an abstract or conclusion claim lacks a `claim_ledger.csv` row or official source;
- the same value appears with different units, scenarios, baselines, denominators, or signs;
- a figure caption states a stronger conclusion than `figure_evidence.csv`;
- an appendix table contradicts a main-body table or cited run;
- `paper_ready` wording relies on candidate, diagnostic, relaxed, stale, or unverifiable evidence;
- AI-use disclosure wording appears inside abstract, body text, code outputs, result tables, or figure canvases instead of the final checklist or separate disclosure file;
- AI-assisted adopted material lacks final-checklist or separate-file disclosure when required;
- the audit starts rewriting the paper instead of reporting consistency failures.

Do not average or reconcile conflicting values by guess. Return the conflict to `math-hub` with the smallest repair surface.
