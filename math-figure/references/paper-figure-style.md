# Paper Figure Style

Use this reference when generating or repairing main-body contest figures, especially when the user asks for Nature-style, formal-paper, clean, non-AI-looking, no-title, or consistent palette figures.

## Nature-style contest adaptation

Inherit the useful Nature-style discipline: calm palette, strong figure contract, no decorative chart families, vector-first export, final-size reading, and exact evidence boundary. Do not copy journal-specific sizes, dense multi-panel habits, or decorative editorial layouts when they do not help the contest claim.

## Style asset

Use `assets/chart-templates/paper_style.py` for matplotlib figures when possible. Copy it with the selected chart template, or copy the `CONTEST_PAPER_COLORS` values into the active project when a single-file script is required. Use `main_text` for main text and `grid` for light reading guides. For high-impact patterns, use `PALETTE`, `DEFAULT_COLORS`, `apply_publication_style`, and the helper functions summarized in `references/high-impact-chart-assets.md`.

`CONTEST_PAPER_COLORS`:

- `main_text`: `#1F2933`
- `muted_text`: `#5B6770`
- `axis`: `#8A949E`
- `grid`: `#E6E8EB`
- `accent_blue`: `#4E79A7`
- `accent_orange`: `#F28E2B`
- `accent_teal`: `#59A14F`
- `accent_red`: `#D95F5F`
- `accent_purple`: `#8C6BB1`
- `neutral_fill`: `#F7F8FA`

`PALETTE` and `DEFAULT_COLORS` provide a Nature-inspired scientific plotting palette for grouped bars, trends, heatmaps, forest intervals, and multi-panel patterns.

## Main-body figure defaults

- Start from the sentence: "This figure proves that ..."; if it cannot be written, keep the item as a table or appendix figure.
- Always remove in-figure titles for LaTeX/Word papers; let the caption carry the title.
- Use serif or system CJK-friendly fonts; never use a novelty font or heavy dashboard style.
- Prefer white background, light grid, restrained axes, and direct labels when series count is small.
- Use blue/orange/teal/red/purple accents in that order; reserve red for warning, violation, or selected-risk marks.
- Make the conclusion readable in grayscale and colorblind review; do not use color as the only carrier.
- Export SVG/PDF first and PNG fallback at 300 dpi.

## Block conditions

Block or demote a figure when it has in-figure titles, unreadable labels, missing units, clipped text, decorative 3D, unexplained color scales, weak claim linkage, or no `figure_evidence.csv` row.
