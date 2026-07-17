# Innovation Forward-Test Protocol

## Purpose

Use this protocol to test whether an innovation claim survives contact with real contest problems. It protects the difference between "generated novelty" and a paper-usable modeling contribution.

Forward tests are lightweight but evidence-bound. They do not require solving an entire contest paper, but they must close the loop from 题面痛点 to baseline failure, 改动组件, required 证据, and the exact paper claim that would be allowed or rejected.

## When To Use

Use `forward_test_matrix.csv` when:

- proposing a new innovation family for the skill pack;
- promoting an innovation claim from `candidate` to `verified`;
- deciding whether an innovation sentence may enter the abstract, highlight paragraph, or conclusion;
- reviewing a prior contest pattern for reuse on a new problem.

Run 3-5 forward tests before trusting a new innovation rule as national-first-candidate guidance. Prefer real CUMCM, contest, or archived team problems with original statements and enough data or official outputs to build a baseline.

## Test Unit

One forward test is one real problem pain plus one proposed changed modeling decision. Do not combine several unrelated innovations in one row.

Required row:

```csv
forward_test_id,contest_problem,subquestion,problem_pain,baseline_model,baseline_failure,innovation_candidate,changed_component,required_evidence,expected_artifacts,pass_fail_rule,result_evidence_id,run_id,review_status,abstract_allowed,risk_note
```

Field rules:

- `problem_pain`: exact task-fit weakness, such as missing feasibility, unstable ranking, hidden geometry, error propagation, or incomplete result delivery.
- `baseline_model`: simplest defensible model a judge would accept as a fair comparison.
- `baseline_failure`: measured, demonstrated, or logically checked failure; it cannot be "baseline is simple" or "advanced model is better".
- `changed_component`: variable, constraint, metric, coupling, decomposition, validation action, or search loop changed by the innovation.
- `required_evidence`: table, figure, diagnostic, ablation, boundary check, or run record needed to prove the change helps.
- `pass_fail_rule`: concrete rule for promotion, including metric, unit, scenario, and minimum evidence status.
- `abstract_allowed`: `yes` only when `review_status=passed`, the evidence row is paper-ready, and wording stays inside the proven boundary.

## Pass Gate

A forward test passes only when all checks hold:

- the current problem statement really contains the named pain;
- the baseline is fair and its failure is visible;
- the changed component is mathematically specific;
- required evidence exists and is traceable to result, figure, run, or verification artifacts;
- the improvement has denominator, unit, scenario, and boundary;
- a reviewer can state why the innovation helps in two sentences.

If any item is missing, keep the innovation `candidate`, `blocked`, or `rejected`. Do not compensate with stronger wording.

## Minimum Set

For each new innovation pattern, use:

- one test where the innovation should pass;
- one test where it should fail or be unnecessary;
- one test where the baseline is adequate and the innovation must be downgraded;
- optionally two more tests from different problem families to check overfitting.

Record rejected tests. A rejected forward test is useful evidence that the skill does not force novelty where the problem does not need it.

## Output Template

```text
Forward test:
Problem pain:
Baseline:
Baseline failure:
Changed component:
Required evidence:
Evidence status:
Pass/fail rule:
Review status:
Abstract allowed:
Risk note:
```

Return unresolved evidence or route gaps to `math-hub`.
