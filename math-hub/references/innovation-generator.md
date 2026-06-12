# Innovation Generator

## Purpose

Use this reference to generate contest-safe innovation candidates for A-problem papers. Innovation must be a useful modeling decision with evidence, not a decorative model name. The output is `innovation_ledger.csv`, and only verified rows may enter the abstract or highlight sections.

## Innovation Candidate Sources

Look for innovations in these places:

- **Problem interpretation**: a sharper state/event, geometry, physical, or business mechanism that reduces ambiguity.
- **Constraint modeling**: a hidden feasibility, collision, shadowing, capacity, conservation, or boundary constraint made explicit.
- **Metric design**: a target-specific metric that connects the题面 to the objective or evaluation.
- **Search strategy**: a problem-shaped coarse-to-fine, dynamic, branch-pruned, or decomposition search that improves reliability.
- **Model coupling**: prediction-to-decision, simulation-to-optimization, mechanism-to-data, or local-to-global coupling.
- **Dimensional reduction**: justified grouping, symmetry, layer/ring aggregation, representative scenarios, or state compression.
- **Validation design**: a baseline, ablation, limit-case check, independent formula check, or visual/numeric cross-check that catches failure.
- **Result delivery**: a complete result table or artifact structure that makes a difficult deliverable machine-checkable.

## Innovation Screening Table

Before calling anything an innovation, fill this table:

| Check | Required answer |
| --- | --- |
| What exact problem pain does it solve? | Name the subproblem and failure mode. |
| What is new relative to the first baseline? | State the changed variable, constraint, metric, decomposition, or solver loop. |
| What evidence proves it helps? | Baseline/ablation/comparison table, constraint check, runtime, error, or feasibility result. |
| What is the cost? | Added assumptions, computation, data dependence, or interpretability burden. |
| Is it necessary? | Explain why the baseline alone is insufficient for the题面. |
| Is it reproducible? | Point to formula, script, run record, and result id. |
| Is it explainable in two sentences? | If not, simplify the claim. |

Reject candidates that cannot answer all seven checks.

## Innovation Evidence Chain

Every accepted innovation needs this chain:

```text
题面 pain -> baseline weakness -> proposed change -> implementation artifact -> comparison evidence -> paper claim
```

Minimum evidence by type:

- New constraint: violated/boundary examples before and after, with units.
- New metric: metric definition, direction, normalization, sensitivity, and ranking/decision impact.
- New search strategy: baseline search, new search, stopping rule, runtime or precision, and missed-solution check.
- New physical or geometric mechanism: coordinate frame, derived equations, boundary check, and at least one visual/numeric verification.
- New decomposition: original variable scale, reduced variable scale, justification, and back-check against representative full cases.

## Baseline and Ablation Requirements

Use the simplest baseline that a judge would consider fair:

- physical simulation: no correction term, coarse grid, analytic approximation, or known mechanism-only model;
- optimization: greedy, uniform allocation, fixed-route, fixed-parameter, coarse grid, or official initial scheme;
- prediction: persistence, mean/median, linear model, or simple seasonal baseline;
- evaluation/ranking: equal weights or single key metric;
- geometry/collision: full brute-force or a transparent distance/overlap check on a small subset.

Ablation removes exactly one proposed improvement at a time. Record:

- baseline setting;
- changed component;
- metric and unit;
- scenario/data split;
- result difference;
- whether the conclusion changes;
- source script and run id.

Do not claim improvement without the denominator. "Improves by 5%" is invalid unless the baseline value, new value, metric, unit, and scenario are stated.

## Forbidden Pseudo-Innovation

Do not call these innovation:

- replacing a simple model name with a fashionable algorithm name;
- adding PSO/GA/SA/AHP/TOPSIS without showing why the题面 needs it;
- using more figures or more code without a new model decision;
- tuning hyperparameters until a number looks better without a run record;
- adding unsupported "adaptive", "dynamic", "multi-objective", or "hybrid" wording;
- moving a result into the abstract without a body table;
- changing assumptions to make results easier while hiding the effect;
- claiming robustness from one scenario or one random seed;
- presenting a 2024 problem pattern as a universal future-year rule.

## `innovation_ledger.csv`

Required fields:

```csv
innovation_id,problem_id,candidate_name,source_type,baseline_id,changed_component,mechanism_summary,expected_benefit,evidence_required,ablation_plan,evidence_result_id,figure_or_table,run_id,status,risk_note,abstract_allowed
```

Field rules:

- `source_type`: `interpretation`, `constraint`, `metric`, `search`, `coupling`, `dimension_reduction`, `validation`, or `artifact`.
- `baseline_id`: must point to a result, model, or run record.
- `evidence_required`: must name the exact table/figure/diagnostic needed.
- `status`: `candidate`, `tested`, `verified`, `rejected`, or `blocked`.
- `abstract_allowed`: `yes` only when the `innovation_ledger.csv` row is verified, the claim has a baseline or ablation, and its evidence row is `validation_status=paper_ready` in `result_registry.csv` or `figure_evidence.csv`.

## Output Template

```text
创新候选:
题面痛点:
基准模型:
改动:
证据需求:
消融/对照:
当前状态:
能否进入摘要:
```

If evidence is missing, output a stronger experiment plan instead of stronger wording.
