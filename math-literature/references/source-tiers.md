# Source Tiers

Use this tiering to decide how much trust a source can carry.

## Tiers

| Tier | Source type | Use |
| --- | --- | --- |
| T1 | Official APIs, publisher pages, DOI records, PubMed/CrossRef/arXiv records, official standards or policy pages | Primary bibliographic and rule evidence |
| T2 | Semantic Scholar, institutional repositories, university pages, repository metadata, verified preprint servers | Secondary discovery and citation graph support |
| T3 | Google Scholar snippets, web pages without stable metadata, scraped databases, forum posts, unverified Chinese database snippets | Discovery only unless manually verified |

## Domain Routing

| Domain | Primary route | Secondary route | Manual route |
| --- | --- | --- | --- |
| Math/CS/optimization | arXiv, CrossRef, publisher DOI | Semantic Scholar | Google Scholar |
| Engineering/energy/power systems | CrossRef, IEEE/Elsevier/Springer DOI pages, official standards | Semantic Scholar | CNKI/Wanfang export if provided |
| Biomedical/clinical | PubMed | Semantic Scholar | journal site |
| Policy/standards | official ministry, standards body, regulator, contest notice | institutional mirror | web snippets only as leads |
| Chinese literature | verified CNKI/Wanfang export, DOI page when available | author/institution pages | manual check required |

## Reliability Rules

- Use T1 whenever a paper-ready citation, DOI, publication year, or rule claim matters.
- Use T2 when T1 coverage is incomplete, but verify final metadata before citation.
- Use T3 only to discover leads or identify Chinese titles that require manual confirmation.
- If the source cannot be opened or metadata cannot be verified, keep the reference as `candidate`.
- For changing policies, standards, model versions, or journal instructions, check the current source date.

## Fallback

If T1 search fails, broaden terms before dropping to weaker sources. If all sources fail, report the gap and do not fabricate a reference.
