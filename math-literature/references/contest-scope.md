# Contest Literature Scope

Use this scope for 高教社杯/CUMCM and similar mathematical modeling contests.

## Goal

Support the paper enough for judges to trust the modeling context, method choice, parameters, standards, and external comparisons. Do not spend contest time building a journal-style systematic review unless the problem explicitly asks for it.

If literature is being used to create the solution route rather than verify paper citations, return the route-search need to `math-hub`. This file governs the citation layer after the route or source need is known.

## Enough For Contest Use

For most contest papers, aim for:

- 2-5 high-quality references in the final paper when references are useful;
- official contest statement and attachments as the primary source for task facts;
- official standards, policy pages, or data portals for regulatory or public-data claims;
- one or two method precedent references when using a named method not derived in the paper;
- compact source notes for parameters not supplied by the contest data.

## When A Full Map Is Worth It

Use `reference_registry.csv` and `claim_citation_map.csv` when:

- a parameter, threshold, cost, coefficient, or standard comes from outside the contest attachments;
- a method claim says prior work uses or validates a modeling route;
- a related-work paragraph compares multiple approaches;
- a final claim depends on a public data source;
- the paper may be checked for unsupported references.

For a simple background sentence, a `reference_notes.md` entry or BibTeX record can be enough.

## What Not To Do

- Do not write long related-work sections just to look academic.
- Do not cite papers that are not used by the model or discussion.
- Do not let literature search delay core modeling, code, figures, or final formatting.
- Do not cite a source for contest-provided data; cite the contest attachment or problem statement instead.
- Do not guess references from memory.

## Contest Output Pattern

For a time-limited contest response, a useful literature output is:

```text
References to use:
- [R1] source, supports method/background/parameter, exact sentence it can support
- [R2] source, supports policy/standard/data, exact sentence it can support

Do not cite:
- [source], reason

Missing source:
- [claim], why it remains unsupported
```
