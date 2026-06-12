---
name: math-literature
description: Use when 高教社杯/CUMCM mathematical modeling papers need lightweight literature search, citation verification, method/background references, standards or policy sources, Chinese-English source routing, DOI/BibTeX checks, or claim-to-citation mapping without fabricated sources.
---

# Contest Literature

## Purpose

Build a contest-grade literature layer for mathematical modeling papers. References support background, method choice, parameter provenance, comparison baselines, data sources, standards, policies, and limitations; they do not decorate unsupported claims.

Core rule: cite only what the source actually supports. Do not fabricate papers, DOI, venues, parameters, citation counts, standards, or journal requirements. In Chinese: 不要编造论文、DOI、发表 venue、参数值、引用次数或期刊要求。

Contest scope: do enough source work for 高教社杯/CUMCM and similar contests, not a journal-style systematic review. Prefer a small set of verified, relevant sources over broad literature coverage.

National-first quality gate: `国一候选` is a quality target, not an award promise (`不承诺获奖`). The literature layer should strengthen 题目贴合, 建模洞察, 证据可信, 可复现, and 边界清楚; it must not hide a weak model behind citation volume.

Hard gate: any citation-backed final claim needs a verified source and an explicit paper use. This applies to method precedent, external parameters, official standards, policy facts, third-party data, and explicit comparisons. In time-limited contest work, routine background may use compact notes.

Language/output boundary: internal search planning, source tiers, DOI/BibTeX fields, English titles, database names, and official source text may stay English. Chinese paper-facing prose should be written in Chinese by default when it is meant to enter the contest paper.

## Reference Routing

| Need | Open |
| --- | --- |
| Decide how much literature work is enough | [references/contest-scope.md](references/contest-scope.md) |
| Plan or run a search, build queries, choose sources | [references/search-workflow.md](references/search-workflow.md) |
| Judge source reliability, fallback order, Chinese-source handling | [references/source-tiers.md](references/source-tiers.md) |
| Verify citations, registries, claim maps, related-work audit | [references/citation-evidence-contract.md](references/citation-evidence-contract.md) |

## Workflow

1. Identify paper use: background, method precedent, parameter source, baseline, dataset, policy context, standard, or limitation.
2. Extract 2-5 core concepts from the problem statement, model route, or target paragraph.
3. Build bilingual query terms when Chinese contest wording matters: official Chinese term, standard English translation, abbreviation, and domain synonym.
4. Choose source tiers before searching. Prefer structured academic sources for bibliographic records; use general web search for official rules, standards, policy pages, or hard-to-index Chinese materials.
5. Search in small batches. Log queries only when a source affects final wording, a parameter, a standard, a method choice, or a comparison.
6. Verify candidate records before use: title, authors, year, venue, DOI/URL, abstract or full text, and exact supported claim.
7. Deduplicate by DOI first, then normalized title plus first author plus year.
8. Write or update `reference_registry.csv` and `claim_citation_map.csv` for important citation-backed claims. For routine background, compact `reference_notes.md` is acceptable.
9. Draft related-work or background prose from verified source groups, not from a paper-by-paper list.
10. Return unresolved source gaps to `math-hub` when a paper-ready claim depends on them.

## Artifacts

Use these files only when they remove real risk:

- `literature_search_log.csv`: one row per search query or manual source check.
- `reference_registry.csv`: one row per verified reference.
- `claim_citation_map.csv`: one row per paper claim, paragraph, method choice, parameter, or baseline that uses a reference.
- `citation_audit.csv`: optional final audit for missing DOI, unsupported citation, secondary-source leakage, or stale URLs.
- `reference_notes.md`: compact fallback for routine background in time-limited contest work.

Required schemas:

```csv
search_id,source,query,date_checked,result_count,accepted_reference_ids,notes
```

```csv
reference_id,title,authors,year,venue,doi,url,source_tier,verified_from,supports,limits,status
```

```csv
map_id,claim_id,location,reference_id,support_type,exact_supported_point,boundary,status
```

`status=paper_ready` requires a verified source and a specific supported point. A citation that only appears in a search result is `candidate`.

## Writing Rules

- Use citations for context, methods, parameters, standards, baselines, data, policies, or limitations.
- Do not cite a source for a claim broader than the source.
- Do not cite review articles for original data when the primary paper is available and needed.
- Do not cite a source solely because it has a similar title.
- Group related work by mechanism, modeling route, data type, or decision problem.
- Mark CNKI, Wanfang, and similar Chinese databases as manual-check sources unless a verified export is provided.
- If the user asks for current/latest literature, verify with current search before answering.

## Output Contract

Return:

- search plan or queries used;
- verified references with IDs;
- rejected or unresolved sources;
- claim-to-citation map when important claims depend on references;
- Chinese draft prose when requested for the paper;
- missing evidence that blocks final citation use;
- return to hub: `math-hub` when a paper-ready claim depends on the literature layer.
