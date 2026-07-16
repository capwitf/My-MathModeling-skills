# Formal Artifacts Schema

## Purpose

Use these artifacts to make an A-problem contest project auditable from current-question lock through final submission. The hub is a QC governor by default; DAGs and lane handoffs are dispatch-only artifacts. These are working files, not decorative appendices. Create only the rows that are supported by the current problem statement, data, official rules, and verified outputs.

Do not hardcode one contest year's submission rules into these artifacts. Page limits, archive formats, AI-use wording, and anonymity rules must come from the official notice or user-provided rules for the active contest.

## Artifact Gate

An artifact blocks downstream work when a required field is missing, contradicts another artifact, or points to a source that does not exist. Mark the file-level `artifact_status` explicitly instead of filling gaps with plausible values.

File-level `artifact_status` values:

- `draft`: logically shaped, still missing evidence.
- `candidate`: computed or written, not yet reviewed.
- `verified`: checked against source data, code, or paper body.
- `blocked`: cannot proceed without a modeling, data, code, or rule fix.
- `deprecated`: superseded; keep only when needed for traceability.

Keep file-level `artifact_status` separate from row-level claim and evidence fields. Paper-facing claim rows use `claim_ledger.csv.status`; computed or figure evidence rows use `validation_status`. A paper, abstract, or conclusion claim requires `claim_ledger.csv.status=paper_ready` plus backing `validation_status=paper_ready` evidence when the claim depends on computed or figure output.

## Artifact Sets

| Artifact | Mode | Owner | Consumers | Required fields | Blocks when |
| --- | --- | --- | --- | --- | --- |
| `hub_state.json` | core QC | hub | all roles | `contest`, `problem_id`, `current_subquestion`, `phase`, `deliverable_completion`, `subquestions_covered`, `deliverables_missing`, `unified_terms`, `units_consistency`, `notation_consistency`, `paper_ready_claims`, `candidate_claims`, `open_blockers`, `allowed_next_module`, `verification_status`, `consistency_status`, `compliance_status`, `similarity_risk`, `score_risk`, `validation_metrics`, `budget_status`, `last_hub_event` | current lock, blockers, allowed next module, claim lists, or budget/validation status is stale or unknown after a trigger event |
| `problem_brief.md` | core QC | hub | all roles | contest/problem id, current lock, task boundary, official-rule source, data files, forbidden assumptions, anonymity notes | active problem, subquestion, or rules that affect submission are unknown |
| `deliverable_matrix.csv` | core QC | hub | all roles | `deliverable_id`, `problem_id`, `subquestion`, `required_output`, `format`, `evidence_needed`, `owner`, `status`, `risk_note` | a subquestion has no explicit required output or accepted omission |
| `model_quality_review.md` | core QC | hub | modeling, code, writer, review | current route, quality class, task fit, baseline, variables, objective, constraints, units, result schema, validation plan, minimum repair | code or writing would proceed from a route that is not `national-first-candidate` |
| `symbol_table.csv` | core QC | modeling | code, writer, LaTeX, review | `symbol`, `type`, `meaning`, `unit`, `domain`, `first_use`, `source`, `status` | any formula/table uses an undefined symbol, conflicting unit, or unknown unit marked as harmless |
| `assumption_log.csv` | core QC | modeling | code, writer, review | `assumption_id`, `statement`, `affected_variables`, `affected_constraints`, `rationale`, `validation_plan`, `risk_if_false`, `status` | assumption changes the objective/constraints but has no validation plan |
| `result_registry.csv` | core QC | code | writer, abstract, review, LaTeX | `result_id`, `problem_id`, `scenario_id`, `metric`, `value`, `unit`, `source_table`, `source_script`, `run_id`, `validation_status` | a paper claim has no row or row `validation_status` is not `paper_ready` |
| `claim_ledger.csv` | core QC | writer or abstract | hub, review, LaTeX | `claim_id`, `location`, `claim_text`, `metric`, `value`, `unit`, `evidence_id`, `figure_or_table`, `status` | abstract/conclusion claim lacks evidence or mixes metric types |
| `ai_usage_log.md` | core QC when AI is used or rules require it | hub | writer, review, final checker | tool name/version, date/time, task phase, prompt or interaction summary, generated material, adopted material, human verification/modification, final checklist/disclosure-file location | AI-assisted content exists without traceable disclosure and human verification notes |
| `ai_claim_disclosure.csv` | core QC when AI is used or rules require claim-level disclosure | math-compliance | hub, review, final checker | `adopted_material_id`, `claim_id`, `artifact`, `location`, `ai_tool`, `model_or_version`, `date`, `task_phase`, `interaction_summary`, `human_verification`, `modification_summary`, `disclosure_location`, `status` | adopted AI-assisted material lacks claim-level traceability, human verification, or disclosure location |
| `submission_checklist.md` | core QC | hub or final checker | all roles | official-rule source checked, page/format rules, anonymity checks, appendix/code/support requirements, AI-use requirements, open blockers | official rules are unknown, required files are missing, or submission-blocking checks are unresolved |
| `model_handoff.md` | evidence/support | modeling | code, writer, review | subproblem, model route, equations, inputs, outputs, result table schema, figure list, diagnostics, unresolved gaps | code must infer formulas, units, thresholds, or output schemas |
| `math_verification.csv` | evidence/support | math-verifier | hub, modeling, code, writer, review | `check_id`, `subquestion`, `artifact`, `location`, `claim_id`, `check_type`, `input_ref`, `expected_relation`, `observed`, `status`, `severity`, `minimum_fix`, `owner` | a formula, unit, constraint, boundary case, or feasibility claim is unchecked, failed, or blocked |
| `run_record.csv` | evidence/support | code | modeling, writer, review, final checker | `run_id`, `problem_id`, `command`, `entry_script`, `input_files`, `parameters`, `seed`, `solver_status`, `warnings`, `output_tables`, `output_figures`, `log_path`, `run_status` | a result or figure references a missing `run_id`, or the run cannot reproduce the cited outputs |
| `numerical_diagnostics.csv` | evidence/support | math-code | hub, modeling, review, final checker | `diagnostic_id`, `run_id`, `subquestion`, `artifact`, `check_type`, `metric`, `value`, `threshold`, `status`, `severity`, `minimum_fix` | tolerance-sensitive, stochastic, or solver-based results have open P0/P1 diagnostics or no diagnostic row |
| `figure_evidence.csv` | evidence/support | math-code or math-figure | writer, abstract, math-figure, math-review, LaTeX | fields defined in [figure-evidence-rules.md](figure-evidence-rules.md), including `figure_id`, `claim_id`, `figure_path`, `run_id`, `caption`, `post_figure_conclusion`, `validation_status` | a paper figure, figure-backed claim, or abstract figure claim has no row or row `validation_status` is not `paper_ready` |
| `consistency_audit.csv` | evidence/support | math-consistency | hub, abstract, writer, review, final checker | `audit_id`, `claim_id`, `artifact_a`, `location_a`, `artifact_b`, `location_b`, `mismatch_type`, `expected`, `observed`, `severity`, `minimum_fix`, `owner`, `status` | abstract/body/table/figure/appendix/registry values, units, scenarios, baselines, or validation statuses disagree |
| `innovation_ledger.csv` | evidence/support | modeling | abstract, writer, review | fields defined in [innovation-generator.md](innovation-generator.md) | claimed innovation has no baseline, ablation, or evidence chain |
| `literature_search_log.csv` | evidence/support when needed | hub QC | writer, review, hub | `search_id`, `source`, `query`, `date_checked`, `result_count`, `accepted_reference_ids`, `notes` | important final related-work, source, or citation decisions rely on unlogged search work |
| `reference_registry.csv` | evidence/support | hub QC | writer, review, abstract, final checker | `reference_id`, `title`, `authors`, `year`, `venue`, `doi`, `url`, `source_tier`, `verified_from`, `supports`, `limits`, `status` | a paper citation has missing metadata, unverified source status, or unclear support boundary |
| `claim_citation_map.csv` | evidence/support when needed | hub QC | writer, review, consistency | `map_id`, `claim_id`, `location`, `reference_id`, `support_type`, `exact_supported_point`, `boundary`, `status` | an important citation-backed method, parameter, standard, policy, dataset, baseline, or comparison claim has no verified source mapping |
| `reference_notes.md` | lightweight evidence/support | hub QC or math-writing | writer, review | compact source list with title/source/date checked and supported sentence | routine background citations are too minor for full registry rows but still need a checked source note |
| `citation_audit.csv` | evidence/support when needed | hub QC or math-review | writer, final checker | `audit_id`, `location`, `reference_id`, `issue`, `severity`, `minimum_fix`, `status` | unsupported citation, secondary-source leakage, stale URL, or guessed DOI remains open |
| `review_findings.csv` | evidence/support | math-review | all roles | `finding_id`, `severity`, `dimension`, `score_risk`, `artifact`, `location`, `issue`, `impact`, `minimum_fix`, `owner`, `status` | severity P0/P1 remains open before final submission |
| `final_submission_manifest.md` | final gate | math-compliance, LaTeX, or math-review | final checker, math-compliance | active official-rule source, files included, files excluded, paper PDF path, code/data paths, anonymity checks, AI-use details when required, compile/run evidence | required file missing, anonymity risk open, official rules not checked, or checklist unresolved |
| `dag.md` | dispatch-only | architect | modeling, code, writer, review | nodes, dependencies, owner, input artifacts, output artifacts, validation gate, reverse-handoff trigger | dispatch was requested and a downstream node has no evidence source or validation gate |

## Hub QC Summary Fields

Every hub QC response or `hub_state.json` refresh should expose these review-facing fields when the project is active:

- `subquestions_covered`: required subquestions mapped to covered, partial, blocked, or not-started.
- `deliverables_missing`: required outputs still absent, including tables, figures, formulas, code outputs, or prose answers.
- `units_consistency` and `notation_consistency`: summary status from symbol, result, figure, table, and consistency checks.
- `table_count` and `figure_count`: counts by subquestion, separating main-body evidence from appendix or diagnostic material.
- `similarity_risk`: plagiarism/template-reuse risk status when a similarity check or stale-template audit exists; otherwise `unknown -> blocked` only for final submission.
- `score_risk`: highest open scoring risk from `review_findings.csv`.

These fields are summary gates, not replacements for row-level artifacts. If the summary is positive but the owning artifact has open P0/P1 rows, the row-level blocker wins.

## `problem_brief.md`

Required sections:

- Current contest and problem scope.
- Current lock: active problem/subquestion and what this pass is allowed to judge.
- Exact subproblem deliverables, including complete tables, schedules, rankings, routes, figures, or attachments.
- Data inventory with source path, file type, row/page count when known, and whether original files may be modified.
- Rule inventory: official notice/user-provided rules that affect page count, archive format, AI-use disclosure, anonymity, and file naming.
- Non-negotiable constraints from the user.
- Open blockers.

Consumer rule: no role should start final claim writing until `problem_brief.md` lists every subproblem deliverable.

## `deliverable_matrix.csv`

Use one row per required output or accepted non-output. This is the hub's guard against answering a different question than the one asked.

Required fields:

```csv
deliverable_id,problem_id,subquestion,required_output,format,evidence_needed,owner,status,risk_note
```

`status` values:

- `required`
- `in_progress`
- `provided`
- `accepted_omission`
- `blocked`

A subquestion is not ready for writing until every required row is `provided` or explicitly `accepted_omission` with a risk note.

## `model_quality_review.md`

Use this file whenever a modeling route is proposed, changed, or handed to paper-ready code/writing. It records whether the idea is strong enough for a national-first-candidate paper, without promising any award outcome.

Required sections:

- Current lock: active problem/subquestion and required deliverable ids.
- Proposed main route and secondary routes, with secondary routes explicitly limited.
- Quality class: `national-first-candidate`, `usable-but-needs-review`, or `blocked`.
- Task fit: how the route answers each required deliverable.
- Baseline/reference scheme and why it is adequate for comparison.
- Variables, domains, units, objective, constraints, and boundary conditions.
- Algorithm/solver/simulation route and why it follows from the model.
- Result schema: tables, figures, registry rows, and paper-facing conclusions expected.
- Validation plan: feasibility, boundary/extreme cases, sensitivity/robustness, baseline/ablation, and reproducibility evidence.
- Main risks, missing evidence, and minimum repair before paper-ready code/writing.

Downstream rule: paper-ready code outputs, final abstract claims, and final LaTeX/PDF submission work should not proceed from a modeling route whose quality class is not `national-first-candidate`. Exploratory/diagnostic code, abstract style coaching, and local LaTeX compile/layout fixes may proceed when clearly labeled as local advice or `diagnostic-only`; they must not promote claims into final paper language.

## `dag.md`

Create `dag.md` only when dispatch mode is explicitly requested or when the project truly needs multi-lane coordination. Do not create a DAG as the default hub response.

Each node must state:

- `node_id`
- role owner
- upstream artifacts
- downstream artifacts
- expected output
- validation gate
- reverse-handoff trigger

Example node shape:

```text
node_id: q2_collision_model
owner: modeling
upstream: problem_brief.md, symbol_table.csv
output: model_handoff.md#q2, assumption_log.csv rows A02-A04
validation_gate: collision condition has a numeric threshold, unit, and boundary test
reverse_handoff_trigger: code finds a first collision before the claimed safe interval
```

## `model_handoff.md`

For each subproblem, include:

- task target and required output table;
- model route and why it matches the problem statement;
- variables, units, domains, and symbol table references;
- objective and constraints in LaTeX;
- assumptions and assumption ids;
- input files and required columns;
- preprocessing and unit conversions;
- result table schema;
- figure evidence requirements;
- diagnostics required from code;
- values that must remain `NA`, empty, or `not identifiable`;
- unresolved gaps and owner.

Result table schema must include at least:

- `problem_id`
- `scenario_id`
- primary entity key such as `time`, `object_id`, `route_id`, `sample_id`, or `solution_id`
- decision variables with units
- derived metrics with units
- feasibility flag or `validation_status`
- source script/run id

## `math_verification.csv`

Use one row per mathematical hard check. This file is owned by `math-verifier`; it should verify the model, not redesign it.

Required fields:

```csv
check_id,subquestion,artifact,location,claim_id,check_type,input_ref,expected_relation,observed,status,severity,minimum_fix,owner
```

Common `check_type` values: `dimensional`, `domain`, `constraint`, `formula back-substitution`, `boundary`, `conservation`, `feasibility wording`, `assumption loss`, `result schema`.

Paper-ready formulas and feasibility claims are blocked while relevant rows are `blocked`, `fail`, or missing.

## `result_registry.csv`

Use one row per paper-usable result. Do not use a single row for a vague sentence such as "model performs well".

Required fields:

```csv
result_id,problem_id,scenario_id,metric,value,unit,comparison_or_baseline,source_table,source_figure,source_script,run_id,validation_status,notes
```

`validation_status` values:

- `raw`
- `computed`
- `checked`
- `paper_ready`
- `blocked`

Only `paper_ready` rows may support abstract claims.

## `run_record.csv`

Use one row per reproducible formal run that creates paper-usable tables, figures, diagnostics, or final decisions. A `run_id` is stable only when the command, scripts, inputs, parameters, seed, and outputs are recorded.

Required fields:

```csv
run_id,problem_id,command,entry_script,input_files,parameters,seed,solver,solver_status,warnings,output_tables,output_figures,log_path,started_at,completed_at,run_status,notes
```

`run_status` values:

- `completed`
- `partial`
- `failed`
- `blocked`

A `result_registry.csv` or `figure_evidence.csv` row is not paper-ready unless its `run_id` exists in `run_record.csv` and `run_status=completed`, or the row explicitly cites a non-computational checked source.

## `numerical_diagnostics.csv`

Use this file for solver, tolerance, conditioning, and stochastic stability checks.

Required fields:

```csv
diagnostic_id,run_id,subquestion,artifact,check_type,metric,value,threshold,status,severity,minimum_fix
```

Common `check_type` values: `scaling`, `condition number`, `solver warning`, `constraint violation`, `tolerance sweep`, `multi-seed`, `baseline comparison`.

A tolerance-sensitive result is not paper-ready while open P0/P1 diagnostics remain or while no diagnostic row exists for a known numerical risk.

## `figure_evidence.csv`

Use one row per generated figure that supports a paper claim. The schema and figure-specific validation rules are defined in [figure-evidence-rules.md](figure-evidence-rules.md).

Only `validation_status=paper_ready` figure rows may support abstract, conclusion, or highlight claims.

## `claim_ledger.csv`

Required fields:

```csv
claim_id,location,claim_text,metric,value,unit,scenario,evidence_id,evidence_type,body_location,status,risk_note
```

Rules:

- Abstract and conclusion claims require `claim_ledger.csv.status=paper_ready` or an explicitly approved equivalent status. They must map to a `result_registry.csv` row with `validation_status=paper_ready`, a `figure_evidence.csv` row with `validation_status=paper_ready`, a formula, or a checked appendix table.
- Improvements require baseline value, denominator, and scenario.
- Feasibility claims require constraint check evidence.
- Robustness claims require sensitivity or stress-test evidence.

## Literature Artifacts

Use `literature_search_log.csv`, `reference_registry.csv`, and `claim_citation_map.csv` when an important paper paragraph depends on external literature, standards, policy pages, datasets, baselines, or method precedent. For ordinary 高教社杯/CUMCM background, a compact `reference_notes.md` entry can be enough if it records source, date checked, and the sentence it supports.

`literature_search_log.csv` required fields:

```csv
search_id,source,query,date_checked,result_count,accepted_reference_ids,notes
```

`reference_registry.csv` required fields:

```csv
reference_id,title,authors,year,venue,doi,url,source_tier,verified_from,supports,limits,status
```

`claim_citation_map.csv` required fields:

```csv
map_id,claim_id,location,reference_id,support_type,exact_supported_point,boundary,status
```

Status values:

- `candidate`: discovered but not checked enough for final paper use.
- `verified`: metadata and relevance are checked.
- `paper_ready`: mapped to a specific claim or paragraph.
- `blocked`: missing metadata, unsupported claim, or inaccessible source blocks final use.
- `rejected`: checked and not suitable.

Paper-ready wording for method, parameter, standard, policy, dataset, baseline, or explicit comparison claims requires `claim_citation_map.csv.status=paper_ready` and a verified or paper-ready `reference_registry.csv` row. A DOI, title, author list, year, or source-supported point must not be guessed.

## `consistency_audit.csv`

Use one row per mismatch or cleared high-risk consistency check across abstract, body, tables, figures, appendix, registries, and support files.

Required fields:

```csv
audit_id,claim_id,artifact_a,location_a,artifact_b,location_b,mismatch_type,expected,observed,severity,minimum_fix,owner,status
```

Common `mismatch_type` values: `value`, `unit`, `scenario`, `baseline`, `denominator`, `rank`, `feasibility`, `certainty`, `validation_status`, `missing_evidence`, `stale_template`, `ai_disclosure`.

Final abstract, conclusion, and package readiness are blocked while P0/P1 consistency rows remain open.

## `ai_usage_log.md`

Use this file whenever AI tools are used for content, code, translation, summarization, formatting, idea generation, verification, or polishing and the active contest rules require disclosure.

AI-use disclosure artifacts are final-submission materials. They should not be inserted into the abstract, main body, generated code outputs, result tables, or figure canvases unless the active official rule explicitly provides a separate required disclosure location.

Required sections:

- Official AI-use rule source checked, with date checked.
- Tool name, version/model when known, provider, and date/time.
- Task phase: problem understanding, modeling, coding, plotting, writing, LaTeX, review, or translation.
- Interaction summary or key prompt/response excerpt sufficient to explain the use without exposing irrelevant private material.
- Material adopted into the paper, code, figures, or support files.
- Human verification and modification notes.
- Final submission checklist, official disclosure form, separate AI-use statement, appendix/support-file if explicitly required, or manifest disclosure location.

No AI-assisted formal claim may enter the paper, code package, or final support materials unless this log explains how it was used and checked. The disclosure wording itself belongs in the final checklist or separate required disclosure file, not in the abstract/body/code outputs.

## `ai_claim_disclosure.csv`

Use this file when the official rules or user require claim-level AI-use traceability for adopted material.

Required fields:

```csv
adopted_material_id,claim_id,artifact,location,ai_tool,model_or_version,date,task_phase,interaction_summary,human_verification,modification_summary,disclosure_location,status
```

`claim_id` may be empty only for non-claim surfaces such as formatting or translation. For final paper claims, code results, or figure conclusions, it must link back to `claim_ledger.csv`.

## `review_findings.csv`

Severity:

- `P0`: fabricated, contradictory, anonymous-risk, or submission-blocking issue.
- `P1`: required deliverable, hard constraint, evidence chain, or reproducibility issue.
- `P2`: clarity, figure density, notation, or nonfatal validation weakness.
- `P3`: polish.

Scoring dimensions should use the six dimensions in [scoring.md](scoring.md).

Every P0/P1/P2 finding should include `score_risk` as `fatal`, `major`, `moderate`, or `minor`, plus the smallest `minimum_fix` that would change a judge's view.

## `submission_checklist.md`

Use this as the hub's hard compliance gate before final writing and final packaging.

Required sections:

- Official rule source checked, with date checked.
- Current paper structure constraints: cover/abstract/body/appendix, page limit, table of contents rule, naming, and electronic/paper consistency.
- Anonymity checks: title page, headers/footers, PDF metadata, filenames, comments, code, appendix, and support materials.
- Appendix/support checks: complete source code, run instructions, data/support list, result tables, figures, and logs needed to reproduce claims.
- AI-use checks: whether AI was used, whether disclosure is required, where the final checklist, official disclosure form, or separate AI-use statement lives, and whether `ai_usage_log.md` is complete.
- Open blockers and owner.

Final writing is blocked while this checklist has unresolved official-rule, anonymity, appendix, code reproducibility, or AI-use disclosure risks.

## `final_submission_manifest.md`

Required sections:

- Official rule source checked, with date checked.
- Paper PDF path and compile command.
- Main source path.
- Included support files and why each is needed.
- Excluded files and why each is safe to exclude.
- Result tables and figures cited by the paper.
- Code run records that reproduce core results.
- Anonymity check: title page, PDF metadata, filenames, comments, appendix, and support materials.
- AI-use disclosure/support details when the official notice or user requires them.
- Remaining risks.

Final rule: if the manifest cannot point to the latest verified paper, result registry, claim ledger, submission checklist, AI-use log when required, and review findings, the submission is not ready.
