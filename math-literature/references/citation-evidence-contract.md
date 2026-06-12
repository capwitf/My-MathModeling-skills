# Citation Evidence Contract

## Reference Registry

Use `reference_registry.csv` for important sources that may enter the paper. In short contest workflows, ordinary background sources can be recorded in `reference_notes.md` instead.

```csv
reference_id,title,authors,year,venue,doi,url,source_tier,verified_from,supports,limits,status
```

`status` values:

- `candidate`: discovered but not verified.
- `verified`: metadata and relevance checked.
- `paper_ready`: mapped to a specific paper claim or paragraph.
- `blocked`: metadata, access, or relevance is insufficient.
- `rejected`: checked and not suitable.

## Claim Citation Map

Use `claim_citation_map.csv` when citations support paper text.

```csv
map_id,claim_id,location,reference_id,support_type,exact_supported_point,boundary,status
```

`support_type` examples:

- `background`
- `method_precedent`
- `parameter_source`
- `baseline`
- `dataset`
- `standard_or_policy`
- `limitation`

## Paper-Ready Citation Rules

A citation is paper-ready only when:

- the source has a verified registry row;
- the cited statement is narrower than or equal to the source support;
- the paper location is known;
- the source is the primary source when primary evidence is needed;
- the boundary explains what the source does not prove.

For 高教社杯/CUMCM-style papers, apply this strictly to method, parameter, standard, policy, dataset, and comparison claims. Do not require a row-level map for every generic background sentence unless the user or contest asks for a formal source audit.

## Related Work Structure

Write related work by topic:

1. Problem class and application context.
2. Main modeling routes used in prior work.
3. What each route handles well.
4. What remains missing for the active contest problem.
5. How the present model responds to that gap.

Avoid paper-by-paper summaries unless the user explicitly asks for an annotated bibliography.

## Red Flags

Block or downgrade when:

- a DOI, title, venue, year, or author list is guessed;
- a review article is used as if it were the primary source for data;
- a citation is attached to a number that came from the contest data or code output;
- a method is cited but the active model does not actually use that method;
- a Chinese source has only a search snippet and no verified export or page;
- related work claims novelty without naming the baseline or prior limitation.
