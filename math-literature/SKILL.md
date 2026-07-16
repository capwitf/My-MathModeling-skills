---
name: math-literature
description: Use when 高教社杯/CUMCM mathematical modeling papers need lightweight literature search, citation verification, method/background references, standards or policy sources, Chinese-English source routing, DOI/BibTeX checks, or claim-to-citation mapping without fabricated sources.
---

# Contest Literature

## Purpose

Plan lightweight source work, verify citations, map claims to references, and prevent fabricated or over-broad literature support in contest papers.

This skill is for citation and source verification in 高教社杯/CUMCM work. If the user needs literature to generate solution ideas or compare candidate model routes, return the source gap and route-search need to `math-hub`; do not reverse-cite a finished model.

国一候选门槛：引用工作应服务题目贴合、建模洞察、证据可信、可复现、边界清楚；这是提交质量门槛，不承诺获奖。

For a citation-backed `paper_ready` claim, final gate, or cross-module handoff, apply the current `math-hub` evidence rules. Local source triage can stay lightweight.

## Source Routing

- Official rules, policies, standards, datasets, and parameters require primary or authoritative sources.
- Method background can use credible papers, textbooks, or official documentation.
- Ordinary contest background can use compact verified notes when it does not carry a parameter, baseline, policy, or method-validity claim.
- If current facts, policies, standards, prices, or public figures may have changed, verify online from primary sources.

## Workflow

1. State the claim needing support.
2. Decide source tier and search language.
3. Search or inspect provided sources.
4. Verify metadata, DOI/BibTeX, publisher, date, and source status when relevant.
5. Record in `literature_search_log.csv` and `reference_registry.csv` when the source supports paper claims.
6. Create `claim_citation_map.csv` rows for parameter, standard, policy, baseline, public-data, or method-validity claims.
7. Return unresolved source gaps to `math-hub`.

A verified source supports only the point it actually says. Do not widen the paper claim to sound stronger.

Keyword match alone is never bibliography-ready. A reference needs paper location, exact supported point, support boundary, and verified metadata before it can support final prose.

When a request is really "help me find ideas before modeling" rather than "verify this claim/source", return the active subquestion, evidence need, and current source gaps to `math-hub` for route selection.

## Output Contract

Return:

- search plan or verified sources;
- source tier and support boundary;
- `literature_search_log.csv`, `reference_registry.csv`, or `claim_citation_map.csv` rows when needed;
- citation wording or BibTeX/DOI fixes;
- unresolved gaps and route.

Return to hub: math-hub.

## Red Lines

- 不要编造论文、DOI、作者、期刊、标准或政策原文。
- Do not cite search snippets as verified sources.
- Do not use an unverified citation for a paper-ready claim.
- Do not let a source support broader wording than it justifies.
