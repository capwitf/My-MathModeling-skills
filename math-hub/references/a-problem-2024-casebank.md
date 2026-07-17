# A-Problem 2024 Casebank

## Source and Use Limits

This casebank summarizes reusable patterns from locally archived 2024 A-problem materials identified as:

- `A053`
- `A163`
- `A242`

**OCR risk warning**: The provided 2024 materials are page images. OCR was used for extraction, so this file records structural patterns only. Do not copy wording. Do not trust exact numeric values, exact OCR page numbers, or any numeric value here as final evidence for another paper.

A locally archived 2023 A-problem heliostat paper identified as `A092.pdf` is used only as near-year pattern context in the final section, not as part of the 2024 casebank.

## Shared 2024 A-Problem Pattern: Bench Dragon

All three 2024 materials solve a linked-body motion and path-optimization problem with these recurring modules:

1. Represent the path in a coordinate frame.
2. Derive the leader position from speed and arc length.
3. Recursively derive follower handle positions from rigid geometry.
4. Derive or approximate follower speeds.
5. Detect first collision or constraint contact.
6. Search a path parameter such as pitch or speed under feasibility constraints.
7. Extend the motion model across multiple path segments for the turning stage.
8. Export complete position/speed tables and support files.

Reusable lesson: high-score work is not "use a better optimizer" first. It is "make the geometry, state, threshold, result table, and verification chain explicit".

## Case A053 Pattern Notes

Observed route:

- Uses polar-coordinate spiral modeling and arc-length relation for the leader.
- Recursively computes the positions of body and tail handles.
- Frames collision as rectangle overlap and uses a separation-axis style test.
- Uses coarse-to-fine or variable-step traversal for pitch search.
- Uses particle swarm for a maximum-speed style optimization.
- Includes result tables, local collision visualization, sensitivity wording, and code appendix fragments.

Reusable patterns:

- Convert a physical path into a small number of state variables before optimizing.
- For collision, reduce the search region by proving where first contact can occur, then run exact geometric checks.
- For parameter search, record both the final parameter and the constraint-contact evidence.
- For figures, pair global state reconstruction with local zoom. The local zoom should carry the actual feasibility argument.

Risks to guard against:

- OCR indicates some possible unit inconsistency in a reported speed phrase; future workflows must force unit checks in `result_registry.csv`.
- Particle swarm or heuristic claims need convergence, seed, and baseline evidence before they can be called innovation.

## Case A163 Pattern Notes

Observed route:

- Uses a geometric model with position iteration and velocity iteration.
- Collision is checked through selected corner points and distances to board-center lines.
- For pitch, brackets inside/outside turning-space cases and then refines the boundary.
- For turning, creates a segment classifier/judgment function for multiple curve cases.
- Identifies the target body segment most likely to create the maximum speed and uses that to scale the leader speed.
- Provides support-material and code-list style appendices.

Reusable patterns:

- A "state classifier" is valuable when the path has several curve segments; it prevents a pile of ambiguous case prose.
- For maximum-speed problems, first locate the critical entity/time window, then solve the scalar maximum.
- A geometric impossibility proof can be a strong result when it explains why an apparent optimization cannot improve the objective.

Risks to guard against:

- The state classifier must be documented as a table of cases with boundary conditions; otherwise the code and paper can diverge.
- "Exact" wording should be tied to tolerance, not just a program output.

## Case A242 Pattern Notes

Observed route:

- Uses polar geometry, bisection, recurrence, and derivative-based speed formulas.
- Narrows collision detection to an inner and adjacent outer ring, then uses a distance threshold.
- Uses dynamic/coarse-to-fine search plus bisection for first collision.
- Uses particle swarm or heuristic comparison for a difficult subroutine, then combines it with variable-step search.
- Shows distance-to-threshold and speed-maximum curves for validation.
- Uses a speed scaling relation and ternary search after identifying a unimodal window.
- Lists support files and result spreadsheets in the appendix.

Reusable patterns:

- Dynamic search is persuasive when paired with a threshold curve proving the crossing was not skipped.
- Speed-limit questions can often be transformed by scaling all speeds relative to a fixed leader-speed run.
- A unimodality claim needs a plotted local window or numerical scan before ternary search is credible.
- A support-material manifest helps the paper's result tables and code outputs stay aligned.

Risks to guard against:

- Search-window reduction must have a physics/geometric reason and a fallback diagnostic.
- A single run of a heuristic is not enough for an innovation claim.

## Cross-Case High-Value Moves

| Move | Why it works | Required artifact |
| --- | --- | --- |
| Coordinate-frame-first modeling | makes every later formula auditable | `symbol_table.csv`, `model_handoff.md` |
| Recursive state table | turns a complex linked system into complete deliverables | `result_registry.csv` |
| Constraint threshold curve | proves first contact or feasibility boundary | `figure_evidence.csv` |
| Local zoom around failure/contact | shows geometric credibility | `figure_evidence.csv` |
| Coarse-to-fine search | balances speed and precision | `run_record.csv`, `diagnostics` |
| Critical-window reduction | makes maximum search tractable | `assumption_log.csv`, `diagnostics` |
| Segment/state classifier | handles multi-curve or multi-state path logic | `model_handoff.md`, `result_registry.csv` |
| Baseline or impossible-improvement proof | prevents fake optimization | `innovation_ledger.csv`, `claim_ledger.csv` |

## Cross-Case Pitfalls

- Complete result tables are mandatory; selected rows in the body need full tables in support files.
- Units must be enforced for positions, speeds, pitch, radius, time, and thresholds.
- A figure without a threshold, unit, or conclusion sentence is not evidence.
- "First collision", "minimum pitch", "maximum speed", and "shortest path" all require a search log or proof, not just an endpoint.
- If a path has multiple segments, code must expose segment state, not hide it in formulas.
- Heuristics need convergence, repeated runs or deterministic checks, and a baseline.

## 2023 A092 Pattern Context

The 2023 A092 PDF is a heliostat-field optimization paper. Text extraction is readable, but some numeric values appear blank due to PDF font/layout issues, so use it for pattern shape only.

Reusable context:

- Break a physical objective into named efficiency/loss components before optimizing.
- Use projection or sampling to convert geometry loss into computable evidence.
- For many-variable layouts, justify dimension reduction with symmetry or grouping, then back-check representative cases.
- Put component efficiency, final design parameters, and support spreadsheets into formal tables.
- Use component trend, spatial distribution, and sensitivity figures with units and conclusion sentences.

Connection to 2024:

- Bench-dragon collision and heliostat shadowing are both "geometry constraint or loss detection" problems.
- Bench-dragon pitch/speed search and heliostat layout optimization both need baseline, run record, feasibility diagnostics, and result registry.
- In both years, the best reusable innovation is often a problem-shaped reduction plus evidence, not a generic heuristic name.
