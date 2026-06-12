# Literature Search Workflow

## Query Construction

Start from the paper need, not from generic keywords.

1. Extract the modeling object: grid, traffic, logistics, epidemic, reservoir, energy storage, scheduling, routing, allocation, risk, or policy.
2. Extract the modeling action: optimization, prediction, simulation, evaluation, classification, control, dispatch, planning, or sensitivity analysis.
3. Extract the evidence need: method precedent, parameter source, baseline, dataset, standard, policy, limitation, or application context.
4. Build bilingual terms when the problem statement is Chinese.
5. Combine terms with Boolean logic and test narrow/broad versions.

## Contest Modeling Query Patterns

| Need | Query shape |
| --- | --- |
| Method precedent | `"[object]" AND "[modeling action]" AND (optimization OR simulation OR evaluation)` |
| Parameter source | `"[object]" AND (parameter OR coefficient OR efficiency OR cost OR emission factor)` |
| Baseline method | `"[decision problem]" AND (baseline OR benchmark OR comparison) AND model` |
| Energy system | `(renewable OR photovoltaic OR wind) AND (dispatch OR storage OR hydrogen) AND optimization` |
| Transportation/logistics | `(routing OR location allocation OR scheduling) AND (optimization OR integer programming)` |
| Risk/evaluation | `(risk assessment OR comprehensive evaluation) AND (indicator system OR weighting)` |
| Chinese contest context | Chinese official term plus English translation, checked separately |

## Search Sequence

1. Start with structured scholarly sources for bibliographic records.
2. Search official standards, policy pages, or contest attachments separately when the claim is regulatory or rule-based.
3. Use broad web search only to discover leads, then verify the bibliographic record from a stable source.
4. For each accepted source, record what exact claim it supports before drafting prose.
5. Stop once the paper has enough verified sources for the active contest claim; do not chase exhaustive coverage by default.

## Broadening And Narrowing

If too many results:

- add the object domain, method family, year range, or "case study";
- require title/abstract matches when the source supports method precedent;
- add "review" only when seeking a map of the field.

If too few results:

- remove contest-specific phrasing;
- replace Chinese proper nouns with standard English technical terms;
- search for the mathematical problem class rather than the application name.

## Search Log

Record every nontrivial search:

```csv
search_id,source,query,date_checked,result_count,accepted_reference_ids,notes
```

Do not treat an unlogged search result as paper-ready evidence for important method, parameter, policy, standard, or data claims. For simple contest background, keep at least a compact note with title/source/date checked.
