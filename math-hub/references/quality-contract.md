# Math Quality Contract

Use this file as the shared standard source only when a task promotes `paper-ready`, classifies `blocked`, runs a final gate, or creates a cross-module handoff. Do not load it for ordinary local rewrites, style notes, exploratory checks, or layout fixes.

This contract defines common quality states and blocking principles. Concrete artifact fields, CSV layouts, and registry details belong in `artifacts-schema.md` or the owning module reference.

## Quality States

`national-first-candidate` means the work is a strong contest candidate, not an award promise. It requires task fit, visible modeling insight, trustworthy evidence, reproducibility, and clear boundaries.

`paper_ready` means a claim, result, table, figure, abstract sentence, or submission status may be used in final paper-facing language. It needs verified source evidence, reproducible support, consistency with the paper, and no open P0/P1 blocker.

`diagnostic-only` means the work reduces uncertainty but cannot support final language. Exploratory code, provisional figures, schema checks, feasibility probes, and unverified drafts stay in this state until their evidence chain is complete.

`blocked` means continuing would require guessing or would hide a material risk. Missing deliverables, unknown rules, undefined units, unchecked formulas, absent run evidence, stale results, or unsupported final claims are blockers.

## Evidence Chain

Paper-facing claims must trace from the problem requirement to the model or source, then to computed or documented evidence, then to validation, then to consistent paper wording. If any required upstream gate is absent, paper-ready promotion is blocked until the owning module repairs it.

For computed evidence, the chain must prove that a run exists, the output matches the model handoff, validation status supports the claim, and the claim is consistent with abstract, body, table, figure, appendix, and registries. The exact artifacts and fields are defined by the owning module.

For source-backed evidence, the chain must prove the source is verified and that the wording does not claim more than the source supports.

## Blocking Protocol

When a required upstream gate is missing, write the narrowest blocker and route to the module that can remove it. Do not soften `blocked` into "continue carefully" for final claims, official submissions, or paper-ready outputs.

If the same blocker loops, downgrade the claim to a baseline or `diagnostic-only`, or ask for the missing authority. Do not let repeated local edits become unreviewed final paper language.

## Public Red Lines

- Do not promote candidate, relaxed, stale, unverifiable, or diagnostic evidence into abstract, conclusion, result table, or main-body figure claims.
- Do not invent data, formulas, units, constraints, solver behavior, references, official rules, or AI-use disclosure language.
- Do not use a fashionable method name as evidence of a model.
- Do not hide unknown units, missing source rows, absent validation, or rule uncertainty behind polished prose.
- Do not treat routing permission as proof that downstream work is paper-ready.

## AI Disclosure Boundary

AI-use disclosure is a final-submission concern. Track AI-assisted claims and outputs when required, but keep disclosure wording out of abstracts, body prose, code comments, generated tables, and figure canvases unless the official rule explicitly says otherwise. Route final wording and package readiness to the compliance gate.
