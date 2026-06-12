# Final Checklist

Use this order so evidence and layout issues are caught before final export.

## 1. Template Compliance

- Confirm the required `documentclass` and page geometry are intact.
- Confirm anonymity rules: no names, school, acknowledgements, metadata leaks, or identifying filenames if blind review is required.
- Confirm page limit, abstract position, keyword format, appendix policy, file naming, and archive requirements.
- Confirm AI-use or reproducibility statements only appear when required and match the active problem.

## 2. Compilation Health

- Compile from a clean state.
- Resolve undefined citations and references.
- Check missing image files, duplicate labels, and bibliography errors.
- Inspect warnings related to font substitution, overfull boxes, float placement, and bookmark encoding.

## 3. Evidence Consistency

- Every abstract/conclusion claim appears in the body.
- Every numeric claim maps to `result_registry.csv`, `figure_evidence.csv`, a body table, a formula, or checked appendix evidence.
- Every computed result cites a completed run or checked source.
- Feasibility, robustness, and improvement claims have the required supporting evidence.

## 4. Layout Readability

- Read the first two pages in PDF form, not source form.
- Check section breaks for large white gaps.
- Check whether equations overflow or distort line spacing.
- Check long formulas: 长公式 should use semantic line breaks instead of tiny fonts or image equations.
- Check whether figures appear before the reader knows why they matter.
- Check captions stay near their figures/tables.

## 5. Figure And Table Density

- Make a contact sheet or page screenshots when possible.
- Flag any page where one figure takes most of the page.
- Flag any page with dense 2x2 or multi-panel figures.
- For 并列子图, verify every panel is readable and all panels support one shared claim.
- For 三线表, verify `booktabs`, no vertical rules, units in headers, and readable numeric alignment.
- For 伪代码, verify inputs, outputs, stopping rule, and iteration/complexity cue are visible without crowding the page.
- Verify every main-body figure proves a main claim.
- Demote diagnostic/exploratory figures to appendix when they crowd the narrative.
- Verify labels, legends, axes, and colorbars are readable at 100 percent zoom.

## 6. Math And Notation

- Verify notation is introduced before heavy use.
- Verify symbol meanings and units are consistent across all questions.
- Verify equation numbering only appears where useful.
- Verify assumptions and slack/diagnostic variables are labeled correctly.

## 7. References

- Verify all cited entries appear in the bibliography.
- Verify bibliography formatting is consistent.
- Verify English and Chinese titles are not broken by bad encoding.

## 8. Final PDF Sanity Check

- Open the PDF outside the editor.
- Scroll all pages once.
- Check bookmarks, hyperlinks, page order, page count, and final filename.
- Confirm the final PDF and included source/data/code files match the submission manifest.
