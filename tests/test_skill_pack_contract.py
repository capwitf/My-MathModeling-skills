from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
REVIEWED_SKILLS = [
    "math-abstract",
    "math-code",
    "math-compliance",
    "math-consistency",
    "math-figure",
    "math-hub",
    "math-latex",
    "math-literature",
    "math-model",
    "math-review",
    "math-table",
    "math-templates",
    "math-verifier",
]


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def fenced_blocks(text: str) -> list[str]:
    return re.findall(r"```(?:[a-zA-Z0-9_-]+)?\n(.*?)```", text, flags=re.DOTALL)


def model_evaluation_advantage_lines(text: str) -> list[str]:
    lines: list[str] = []
    for block in fenced_blocks(text):
        if "模型的优点" not in block:
            continue
        in_advantages = False
        for line in block.splitlines():
            stripped = line.strip()
            if stripped.startswith("模型的优点"):
                in_advantages = True
                continue
            if in_advantages and (
                stripped.startswith("模型的缺点")
                or stripped.startswith("模型仍存在")
                or stripped.startswith("【缺点段】")
                or stripped.startswith("模型的推广")
            ):
                in_advantages = False
            if in_advantages and re.match(r"^[123]\.", stripped):
                lines.append(stripped)
    return lines


def paper_facing_template_paths() -> list[Path]:
    return sorted(
        [
            *ROOT.glob("math-templates/assets/contest-project-template/paper/**/*.md"),
            ROOT / "math-templates/references/assumption-evaluation-controls.md",
            ROOT / "math-hub/references/writing-templates.md",
            ROOT / "math-hub/references/writer.md",
        ]
    )


def frontmatter_value(text: str, key: str) -> str:
    match = re.search(rf"^{key}:\s*(.+)$", text, re.MULTILINE)
    if not match:
        return ""
    return match.group(1).strip().strip('"')


def discovered_skill_names() -> list[str]:
    return sorted(
        path.name
        for path in ROOT.glob("math-*")
        if (path / "SKILL.md").is_file()
    )


class SkillPackContractTest(unittest.TestCase):
    def assert_contains_all(self, text: str, tokens: list[str]) -> None:
        missing = [token for token in tokens if token not in text]
        self.assertEqual(missing, [])

    def test_p0_hard_gate_skills_exist(self):
        self.assertTrue((ROOT / "math-verifier" / "SKILL.md").is_file())
        self.assertTrue((ROOT / "math-consistency" / "SKILL.md").is_file())

    def test_hub_has_state_events_metrics_and_budget_contracts(self):
        hub = read("math-hub/SKILL.md")

        self.assert_contains_all(
            hub,
            [
                "hub_state.json",
                "current_subquestion",
                "deliverable_completion",
                "unified_terms",
                "open_blockers",
                "allowed_next_module",
                "## 事件触发矩阵",
                "## 指标与预算门禁",
                "paper_ready_claim_ratio",
                "same blocker",
            ],
        )

    def test_reviewed_skills_covers_every_math_skill(self):
        self.assertEqual(sorted(REVIEWED_SKILLS), discovered_skill_names())

    def test_hub_state_schema_matches_skill_minimum_fields(self):
        schema = read("math-hub/references/artifacts-schema.md")

        self.assert_contains_all(
            schema,
            [
                "paper_ready_claims",
                "candidate_claims",
            ],
        )

    def test_hub_light_requests_bypass_formal_qc_but_keep_final_gates(self):
        hub = read("math-hub/SKILL.md")
        schema = read("math-hub/references/artifacts-schema.md")

        self.assert_contains_all(
            hub,
            [
                "## 轻请求旁路",
                "local paragraph rewrite",
                "chart/figure selection",
                "abstract style diagnosis",
                "LaTeX compile/layout bug fix",
                "Do not create or refresh `hub_state.json`",
                "complete local answer",
                "within the requested scope",
                "Completeness means fully answering",
                "does not mean generating full-project workflow artifacts",
                "local advice",
                "diagnostic-only",
                "paper-ready gate required",
                "Every formal QC-mode response",
            ],
        )
        self.assertNotIn("return compact help", hub)
        self.assert_contains_all(
            hub,
            [
                "paper-ready code outputs, final abstract claims, or final LaTeX/PDF submission work",
                "exploratory or diagnostic code",
                "style coaching",
                "local compile, layout, figure placement, or table formatting issues",
            ],
        )
        self.assert_contains_all(
            schema,
            [
                "paper-ready code outputs, final abstract claims, and final LaTeX/PDF submission work",
                "Exploratory/diagnostic code",
                "abstract style coaching",
                "local LaTeX compile/layout fixes",
                "local advice or `diagnostic-only`",
            ],
        )
        self.assertNotIn(
            "Downstream rule: `math-code`, `math-abstract`, and `math-latex` should not proceed",
            schema,
        )

    def test_paper_ready_claim_contract_uses_claim_status_and_evidence_validation(self):
        hub = read("math-hub/SKILL.md")
        schema = read("math-hub/references/artifacts-schema.md")

        self.assertNotIn("Claim-supporting rows use `validation_status`", schema)
        self.assert_contains_all(
            hub,
            [
                "claim_ledger.csv.status=paper_ready",
                "validation_status=paper_ready",
            ],
        )

    def test_new_verifier_and_consistency_skills_publish_artifacts(self):
        verifier = read("math-verifier/SKILL.md")
        consistency = read("math-consistency/SKILL.md")

        self.assert_contains_all(
            verifier,
            [
                "math_verification.csv",
                "dimensional",
                "boundary",
                "formula back-substitution",
                "Return to hub: math-hub",
            ],
        )

        self.assert_contains_all(
            consistency,
            [
                "consistency_audit.csv",
                "abstract",
                "body",
                "figure",
                "appendix",
                "claim_ledger.csv",
                "Return to hub: math-hub",
            ],
        )

    def test_code_compliance_review_have_new_diagnostics(self):
        code = read("math-code/SKILL.md")
        compliance = read("math-compliance/SKILL.md")
        review = read("math-review/SKILL.md")

        self.assert_contains_all(
            code,
            [
                "## 数值稳定性硬检查",
                "numerical_diagnostics.csv",
                "condition number",
                "tolerance sweep",
            ],
        )

        self.assert_contains_all(
            compliance,
            [
                "claim-level AI disclosure",
                "ai_claim_disclosure.csv",
                "adopted_material_id",
            ],
        )

        self.assert_contains_all(
            review,
            [
                "## 量化评分风险",
                "score_risk",
                "minimum_fix",
            ],
        )

    def test_artifact_schema_lists_new_gate_artifacts(self):
        schema = read("math-hub/references/artifacts-schema.md")

        self.assert_contains_all(
            schema,
            [
                "hub_state.json",
                "math_verification.csv",
                "numerical_diagnostics.csv",
                "consistency_audit.csv",
                "ai_claim_disclosure.csv",
                "score_risk",
            ],
        )

    def test_review_report_actionable_fields_are_contract_locked(self):
        hub = read("math-hub/SKILL.md")
        schema = read("math-hub/references/artifacts-schema.md")
        model = read("math-model/SKILL.md")
        code = read("math-code/SKILL.md")
        latex = read("math-latex/SKILL.md")
        table = read("math-table/SKILL.md")
        figure = read("math-figure/SKILL.md")
        consistency = read("math-consistency/SKILL.md")
        abstract = read("math-abstract/SKILL.md")

        self.assert_contains_all(
            hub,
            [
                "subquestions_covered",
                "deliverables_missing",
                "units_consistency",
                "notation_consistency",
                "similarity_risk",
                "score_risk",
                "table_count",
                "figure_count",
            ],
        )
        self.assert_contains_all(
            schema,
            ["## Hub QC Summary Fields", "subquestions_covered", "table_count", "figure_count"],
        )
        self.assert_contains_all(
            model,
            ["## 覆盖与单位闭合门禁", "subquestions_covered", "deliverables_missing"],
        )
        self.assert_contains_all(code, ["numerical_diagnostics.csv"])
        self.assert_contains_all(latex, ["## 合规报告门禁", "compliance_report"])
        self.assert_contains_all(table, ["## 表格清单门禁", "table_count"])
        self.assert_contains_all(
            figure,
            ["## 图表数量与覆盖门禁", "figure_count_by_subquestion", "missing_figure_support"],
        )
        self.assert_contains_all(
            figure,
            ["references/chart-template-index.md", "assets/chart-templates/", "模板规则"],
        )
        self.assert_contains_all(code, ["math-figure/assets/chart-templates/"])
        self.assert_contains_all(consistency, ["units_consistent", "notation_consistent"])
        self.assert_contains_all(abstract, ["## Format Gate", "keyword count", "word/page limit"])

    def test_latex_skill_covers_contest_pain_point_layout_patterns(self):
        latex = read("math-latex/SKILL.md")
        patterns = read("math-latex/references/latex-patterns.md")
        checklist = read("math-latex/references/final-checklist.md")
        metadata = read("math-latex/agents/openai.yaml")

        self.assert_contains_all(
            latex,
            [
                "## 竞赛高频排版修复",
                "三线表",
                "多图并列",
                "长公式断行",
                "伪代码",
                "rendered PDF",
                "Do not use `resizebox` as the default repair",
            ],
        )
        self.assert_contains_all(
            patterns,
            [
                "## Contest Pain-Point Patterns",
                "Three-line result table",
                "Side-by-side subfigures",
                "Long equation line breaking",
                "Contest pseudocode",
                "tabularx",
                "subcaption",
                "aligned",
                "algorithmicx",
                "algpseudocode",
            ],
        )
        self.assert_contains_all(
            checklist,
            [
                "三线表",
                "并列子图",
                "长公式",
                "伪代码",
            ],
        )
        self.assert_contains_all(metadata, ["三线表", "多图并列", "长公式", "伪代码"])

    def test_review_skill_has_readability_overlay_for_judge_first_pass(self):
        review = read("math-review/SKILL.md")
        scoring = read("math-hub/references/scoring.md")
        metadata = read("math-review/agents/openai.yaml")

        self.assert_contains_all(
            review,
            [
                "## 评委可读性门禁",
                "first-pass readability",
                "reading cost",
                "formula dumping",
                "logic jumps",
                "figure/table chaos",
                "dimension 6 / overall presentation",
                "可升级为 P2",
                "Readability risks:",
            ],
        )
        self.assert_contains_all(
            scoring,
            [
                "## 可读性 Overlay",
                "不是第 7 个官方维度",
                "维度 6",
                "公式堆砌",
                "逻辑跳跃",
                "图表混乱",
                "阅读成本",
            ],
        )
        self.assert_contains_all(metadata, ["可读性", "阅读成本", "逻辑跳跃"])

    def test_ai_disclosure_is_final_artifact_not_abstract_or_code_content(self):
        hub = read("math-hub/SKILL.md")
        schema = read("math-hub/references/artifacts-schema.md")
        abstract = read("math-abstract/SKILL.md")
        code = read("math-code/SKILL.md")
        writer = read("math-hub/references/writer.md")

        self.assertNotIn("AI-use statements", frontmatter_value(abstract, "description"))
        self.assert_contains_all(
            abstract,
            [
                "AI-use disclosure does not belong in the abstract",
                "final submission checklist or separate disclosure file",
            ],
        )
        self.assert_contains_all(
            code,
            [
                "## AI 披露边界",
                "Do not write AI-use disclosure text",
                "final submission checklist or separate disclosure file",
            ],
        )
        self.assert_contains_all(
            hub,
            [
                "final AI-use statement or official disclosure form",
                "Do not place AI-use disclosure wording in the abstract, body text, code comments",
            ],
        )
        self.assert_contains_all(
            schema,
            [
                "AI-use disclosure artifacts are final-submission materials",
                "The disclosure wording itself belongs in the final checklist or separate required disclosure file",
            ],
        )
        self.assert_contains_all(
            writer,
            [
                "不把 AI 使用说明",
                "正文",
                "最终提交清单或单独披露文件",
            ],
        )

    def test_skill_frontmatter_and_openai_metadata_are_present(self):
        for skill in REVIEWED_SKILLS:
            with self.subTest(skill=skill):
                skill_md = read(f"{skill}/SKILL.md")
                openai_yaml = read(f"{skill}/agents/openai.yaml")

                self.assertEqual(frontmatter_value(skill_md, "name"), skill)
                self.assertNotEqual(frontmatter_value(skill_md, "description"), "")
                self.assert_contains_all(
                    openai_yaml,
                    ["interface:", "display_name:", "short_description:", "default_prompt:"],
                )

    def test_skill_pack_has_no_runtime_template_residue(self):
        for path in ROOT.glob("math-*/SKILL.md"):
            with self.subTest(path=str(path.relative_to(ROOT))):
                self.assertNotIn("$ARGUMENTS", path.read_text(encoding="utf-8"))

        for path in ROOT.glob("math-templates/**/*.md"):
            with self.subTest(path=str(path.relative_to(ROOT))):
                self.assertNotIn("path/to/context-image.png", path.read_text(encoding="utf-8"))

        casebank = read("math-hub/references/a-problem-2024-casebank.md")
        self.assertNotIn("C:\\Users\\T\\Desktop", casebank)

    def test_a_problem_triage_has_no_match_fallback_for_novel_mechanisms(self):
        pattern_library = read("math-hub/references/a-problem-pattern-library.md")
        decision_tree = read("math-hub/references/a-problem-decision-tree.md")
        architect = read("math-hub/references/architect.md")

        self.assert_contains_all(
            pattern_library,
            [
                "## No-Match / Novel Mechanism Fallback",
                "new_mechanism_route",
                "不得硬选主模式",
                "从交付物反推",
                "baseline",
                "validation action",
            ],
        )
        self.assert_contains_all(
            decision_tree,
            [
                "match_confidence",
                "low-confidence triage",
                "new_mechanism_route",
                "不强行归类",
                "机制审计",
            ],
        )
        self.assert_contains_all(
            architect,
            [
                "若匹配清楚",
                "若不匹配",
                "new_mechanism_route",
                "不强行套库",
            ],
        )

    def test_consistency_metadata_and_claim_status_contract_are_specific(self):
        consistency_skill = read("math-consistency/SKILL.md")
        consistency_metadata = read("math-consistency/agents/openai.yaml")
        schema = read("math-hub/references/artifacts-schema.md")

        self.assert_contains_all(
            consistency_metadata,
            [
                "claim/result/figure/run 记录",
                "数学核验",
                "数值诊断",
                "AI 披露",
            ],
        )
        self.assertNotIn("A claim with `validation_status` below", consistency_skill)
        self.assertNotIn("A claim with `validation_status` below", schema)
        self.assert_contains_all(
            consistency_skill,
            ["claim_ledger.csv.status=paper_ready", "validation_status=paper_ready"],
        )
        self.assert_contains_all(
            schema,
            ["claim_ledger.csv.status=paper_ready", "validation_status=paper_ready"],
        )

    def test_abstract_consistency_gate_requires_auditable_rows(self):
        abstract = read("math-abstract/SKILL.md")

        self.assertNotIn("or equivalent audit", abstract)
        self.assert_contains_all(
            abstract,
            ["math-consistency", "consistency_audit.csv", "equivalent fields and blocker semantics"],
        )

    def test_abstract_skill_controls_contest_summary_style_failures(self):
        abstract = read("math-abstract/SKILL.md")
        metadata = read("math-abstract/agents/openai.yaml")

        self.assert_contains_all(
            abstract,
            [
                "## Chinese Contest Abstract Style Gate",
                "one A4 page",
                "Avoid result-list prose",
                "number budget",
                "abstract spine",
                "Too many numbers",
                "focus is scattered",
            ],
        )
        self.assert_contains_all(
            metadata,
            [
                "first-page quality",
                "subproblem coverage",
                "number budget",
                "boundary",
            ],
        )

    def test_abstract_skill_blocks_empty_officialese_and_term_stacking(self):
        abstract = read("math-abstract/SKILL.md")

        self.assert_contains_all(
            abstract,
            [
                "## One-Minute Scan",
                "background + method + result + decision meaning",
                "Empty official prose",
                "Process-list abstract",
                "Buzzword stack",
                "Missing structure",
                "What problem is studied",
                "How is it solved",
                "What result is obtained",
                "What is it for",
                "BP-LSTM-CNN-GRU-Transformer",
            ],
        )

    def test_abstract_skill_separates_coaching_from_paper_ready_contracts_without_language_locking(self):
        abstract = read("math-abstract/SKILL.md")
        metadata = read("math-abstract/agents/openai.yaml")
        description = frontmatter_value(abstract, "description")

        self.assert_contains_all(
            abstract,
            [
                "### Style Coaching Inputs",
                "### Paper-Ready Inputs",
                "Do not demand registries before style diagnosis",
                "Subproblem-by-subproblem wording is allowed",
                "route, result, and decision meaning",
                "empty official prose",
                "buzzwords",
                "missing structure",
                "weak keywords",
            ],
        )
        self.assert_contains_all(
            description,
            ["empty official prose", "buzzwords", "missing structure", "weak keywords"],
        )
        self.assert_contains_all(
            metadata,
            ["subproblem coverage", "number budget", "evidence gates"],
        )

    def test_abstract_skill_encodes_first_round_judge_triage(self):
        abstract = read("math-abstract/SKILL.md")
        metadata = read("math-abstract/agents/openai.yaml")

        self.assert_contains_all(
            abstract,
            [
                "## First-Screen Judge Check",
                "Fatal",
                "missing subproblem answer",
                "no final answer",
                "model route lacks variables",
                "official-sounding prose replaces evidence",
                "numbers lack decision meaning",
                "## Subproblem Coverage Table",
                "Subproblem | Deliverable | Model route | Key result | Decision meaning",
                "not final",
                "first-screen judge",
            ],
        )
        self.assert_contains_all(
            metadata,
            ["first-page", "subproblem coverage", "abstract"],
        )

    def test_abstract_skill_has_number_selection_value_and_format_gates(self):
        abstract = read("math-abstract/SKILL.md")

        self.assert_contains_all(
            abstract,
            [
                "## Number Selection",
                "final answer",
                "best/selected plan",
                "constraint boundary",
                "improvement against a baseline",
                "validation error",
                "Delete intermediate arrays",
                "decision meaning",
                "泛价值句",
                "do not put formulas, figures, tables, citations, footnotes, or table-of-contents headings",
                "3-5",
                "综合考虑多种因素",
                "建立了较为合理的模型",
                "结果表明模型具有较好效果",
            ],
        )

    def test_abstract_skill_binds_triage_coverage_and_evidence_to_output(self):
        abstract = read("math-abstract/SKILL.md")

        self.assert_contains_all(
            abstract,
            [
                "Core rule: the abstract follows evidence",
                "evidence-unverified",
                "numbers, rankings, feasibility wording, innovation claims",
                "fatal -> high -> medium -> low",
                "Q | Status | Missing item | Revision",
                "missing evidence blocking a stronger abstract",
                "paper-ready status and residual risks",
                "泛价值句",
            ],
        )

    def test_abstract_bad_pressure_fixture_has_expected_diagnostics_without_chinese_heading_lock(self):
        abstract = read("math-abstract/SKILL.md")

        self.assert_contains_all(
            abstract,
            [
                "missing subproblem answer",
                "method exists but no final answer",
                "model route lacks variables",
                "official-sounding prose replaces evidence",
                "Process-list abstract",
                "泛价值句",
                "Subproblem Coverage Table",
            ],
        )

    def test_abstract_skill_entrypoint_is_english_first_with_chinese_deliverable_boundary(self):
        abstract = read("math-abstract/SKILL.md")
        metadata = read("math-abstract/agents/openai.yaml")

        self.assert_contains_all(
            abstract,
            [
                "# Contest Abstract",
                "## Purpose",
                "## Required Inputs",
                "## First-Screen Judge Check",
                "## Subproblem Coverage Table",
                "## Chinese Contest Abstract Style Gate",
                "## Number Selection",
                "## One-Minute Scan",
                "## Format Gate",
                "## Output Contract",
                "evidence-unverified",
                "Chinese contest abstracts",
            ],
        )

        self.assertNotIn("paper-ready blocked", abstract)

        self.assert_contains_all(
            metadata,
            [
                'display_name: "Contest Abstract"',
                "first-page",
                "subproblem coverage",
                "number budget",
                "evidence gates",
            ],
        )

    def test_downstream_entrypoints_preserve_hub_return_handoff(self):
        for skill in [
            "math-code",
            "math-compliance",
            "math-consistency",
            "math-figure",
            "math-review",
            "math-verifier",
        ]:
            with self.subTest(skill=skill):
                openai_yaml = read(f"{skill}/agents/openai.yaml")
                self.assert_contains_all(openai_yaml, ["return", "math-hub"])

        code = read("math-code/SKILL.md")
        self.assert_contains_all(code, ["Return to hub: math-hub"])

    def test_robustness_gate_is_tiered_and_contract_locked(self):
        hub = read("math-hub/SKILL.md")
        model = read("math-model/SKILL.md")
        code = read("math-code/SKILL.md")
        protocol = read("math-model/references/robustness-protocol.md")

        self.assert_contains_all(
            model,
            [
                "## 鲁棒性计划门禁",
                "direct-check",
                "scenario-check",
                "robustness-required",
                "diagnostic-only",
                "references/robustness-protocol.md",
            ],
        )
        self.assert_contains_all(
            code,
            [
                "## 鲁棒性证据门禁",
                "qX_robustness_summary.csv",
                "validation tier",
                "downgrade",
            ],
        )
        self.assert_contains_all(
            hub,
            [
                "missing_robustness_plan_count",
                "validation tier",
                "robustness plan",
            ],
        )
        self.assert_contains_all(
            protocol,
            [
                "Tier Selection",
                "Route Patterns",
                "Ranking",
                "Policy or system impact analysis",
            ],
        )

    def test_literature_skill_adds_source_grounded_search_contract(self):
        hub = read("math-hub/SKILL.md")
        schema = read("math-hub/references/artifacts-schema.md")
        literature = read("math-literature/SKILL.md")
        scope = read("math-literature/references/contest-scope.md")
        search = read("math-literature/references/search-workflow.md")
        tiers = read("math-literature/references/source-tiers.md")
        citation = read("math-literature/references/citation-evidence-contract.md")

        self.assert_contains_all(
            literature,
            [
                "literature_search_log.csv",
                "reference_registry.csv",
                "claim_citation_map.csv",
                "不要编造论文",
                "高教社杯/CUMCM",
                "Return unresolved source gaps to `math-hub`",
            ],
        )
        self.assert_contains_all(
            scope,
            [
                "Enough For Contest Use",
                "2-5 high-quality references",
                "reference_notes.md",
                "Do not spend contest time",
            ],
        )
        self.assert_contains_all(
            search,
            [
                "Contest Modeling Query Patterns",
                "Energy system",
                "Chinese contest context",
                "search_id,source,query,date_checked",
            ],
        )
        self.assert_contains_all(
            tiers,
            [
                "T1",
                "CrossRef",
                "arXiv",
                "CNKI/Wanfang",
                "manual confirmation",
            ],
        )
        self.assert_contains_all(
            citation,
            [
                "Paper-Ready Citation Rules",
                "method_precedent",
                "parameter_source",
                "claim_citation_map.csv",
            ],
        )
        self.assert_contains_all(
            hub,
            [
                "math-literature",
                "claim_citation_map.csv.status=paper_ready",
                "reference_registry.csv.status=verified or paper_ready",
            ],
        )
        self.assert_contains_all(
            schema,
            [
                "literature_search_log.csv",
                "reference_registry.csv",
                "claim_citation_map.csv",
                "Paper-ready wording",
            ],
        )

    def test_templates_skill_adds_reusable_contest_project_assets(self):
        hub = read("math-hub/SKILL.md")
        templates = read("math-templates/SKILL.md")
        usage = read("math-templates/references/template-usage.md")
        asset_index = read("math-templates/references/asset-library-index.md")
        style_profile = read("math-templates/references/national-prize-style-profile.md")
        section_controls = read("math-templates/references/section-format-controls.md")
        assumption_eval = read("math-templates/references/assumption-evaluation-controls.md")
        guardrails = read("math-templates/references/contest-language-guardrails.md")
        paragraph_flow = read("math-templates/references/paragraph-flow.md")
        exemplar = read("math-templates/references/official-exemplar-notes.md")
        prior = read("math-templates/references/prior-contest-patterns.md")
        hub_writing = read("math-hub/references/writing-templates.md")
        hub_writer = read("math-hub/references/writer.md")
        compute = read("math-templates/assets/contest-project-template/problem_template/src/compute_template.py")
        plot = read("math-templates/assets/contest-project-template/problem_template/src/plot_template.py")
        test_template = read(
            "math-templates/assets/contest-project-template/problem_template/tests/test_pipeline_template.py"
        )
        fragment = read("math-templates/assets/contest-project-template/paper/fragments/fragment_protocol.md")
        problem_guide = read("math-templates/assets/contest-project-template/paper/problem_guide_template.md")
        section_templates = read("math-templates/assets/contest-project-template/paper/section_templates_national.md")
        phrase_library = read("math-templates/assets/contest-project-template/paper/paragraph_phrases_national.md")

        self.assert_contains_all(
            templates,
            [
                "assets/contest-project-template/",
                "section-format-controls.md",
                "contest-language-guardrails.md",
                "paragraph-flow.md",
                "Default to **light asset library mode**",
                "Do not impose a project-management workflow",
                "reuse structure, not old content",
                "per-question computation, plotting, or test scaffolds",
                "National-prize paper section skeleton",
                "National-prize paragraph phrases",
                "`math-hub`",
            ],
        )
        self.assert_contains_all(
            usage,
            [
                "旧模板残留检查",
                "不要把这些资产变成必需工作流",
                "paragraph_phrases_national.md",
            ],
        )
        self.assert_contains_all(
            phrase_library,
            ["# 国奖式段落句式库", "## 问题分析", "**问题一：** "],
        )
        self.assert_contains_all(
            usage,
            [
                "qX/src",
                "qX/tests",
                "results/qX",
                "run_record.csv",
                "旧模板残留检查",
                "模型准备",
                "paragraph_phrases_national.md",
                "不要把这些资产变成必需工作流",
            ],
        )
        self.assert_contains_all(
            asset_index,
            [
                "轻资产库索引",
                "论文风格资产",
                "章节格式控制",
                "假设与评价控制",
                "竞赛论文语言护栏",
                "段落流检查",
                "段落级句式",
                "图表资产",
                "迁移建议",
            ],
        )
        self.assert_contains_all(
            style_profile,
            [
                "国奖式风格画像",
                "不是工作流",
                "摘要结果优先",
                "复杂题使用模型准备",
                "语言是技术说明书风格",
                "模型假设紧凑",
                "框架优点",
                "section-format-controls.md",
                "assumption-evaluation-controls.md",
                "contest-language-guardrails.md",
                "paragraph-flow.md",
            ],
        )
        self.assert_contains_all(
            section_controls,
            [
                "章节格式控制",
                "全局分问标签规则",
                "**问题一：**",
                "\\textbf{问题一：}",
                "1.1 问题背景",
                "1.2 问题提出",
                "背景图是可选项",
                "问题分析",
                "默认形状：总分",
                "不要写成 `问题一:`",
            ],
        )
        self.assert_contains_all(
            assumption_eval,
            [
                "模型假设与评价控制",
                "默认形状：4-6 条编号假设",
                "framework-level advantages",
                "框架优点",
                "难点转译",
                "判定闭环",
                "跨问递推",
                "约束显式化",
                "不要只写统一坐标",
                "图像必须说明机制",
                "证据钩子",
                "式[编号]",
                "表[编号]",
                "图[编号]",
                "运行记录",
                "模型评价",
                "好模式",
                "坏模式",
            ],
        )
        paper_copyable_templates = [
            assumption_eval,
            section_templates,
            phrase_library,
            hub_writing,
            problem_guide,
            hub_writer,
        ]
        for copyable_template in paper_copyable_templates:
            with self.subTest(copyable_template="paper_copyable_text"):
                self.assertNotIn("judgment functions", copyable_template)
                for block in fenced_blocks(copyable_template):
                    self.assertNotIn("证据钩子", block)
                    self.assertNotIn("run_id", block)

        for model_eval_template in [assumption_eval, section_templates, phrase_library, hub_writing]:
            with self.subTest(copyable_template="model_evaluation_copyable_text"):
                self.assert_contains_all(
                    model_eval_template,
                    ["证据钩子", "式[编号]", "表[编号]", "图[编号]"],
                )
                for line in model_evaluation_advantage_lines(model_eval_template):
                    self.assertNotIn("见式[编号]", line)
                    self.assertNotIn("见表[编号]", line)
                    self.assertNotIn("见图[编号]", line)
                    self.assertIn("见[式/表/图/前问结果/支撑材料]", line)
        self.assert_contains_all(
            guardrails,
            [
                "竞赛论文语言护栏",
                "评委可读的精确表达",
                "分问标签格式",
                "**问题一：**",
                "数字与单位",
                "结论强度",
                "删除空话",
                "公式与图表语言",
            ],
        )
        self.assert_contains_all(
            paragraph_flow,
            [
                "竞赛段落流",
                "该段的唯一任务",
                "分章节段落任务",
                "**问题二：**",
                "问题分析",
                "结果分析",
                "好模式",
                "坏模式",
            ],
        )
        self.assert_contains_all(
            exemplar,
            [
                "2025 A196 观察",
                "关系图",
                "模型准备",
                "支撑材料目录",
                "AI 使用材料",
                "紧凑编号",
                "建模框架清楚",
            ],
        )
        self.assert_contains_all(
            prior,
            [
                "电工杯",
                "先计算，后绘图",
                "先有图像计划，再进正文",
                "诊断不自动提升",
            ],
        )
        self.assert_contains_all(
            compute,
            [
                "run_compute",
                "require_columns",
                "validation_status",
                "summary_path",
            ],
        )
        self.assert_contains_all(
            plot,
            [
                "FIGURE_PLAN_FIELDS",
                "caption_draft",
                "post_figure_conclusion_draft",
                "ensure_nonblank",
            ],
        )
        self.assert_contains_all(
            test_template,
            [
                "test_compute_template_writes_summary",
                "test_plot_template_writes_figure_and_plan",
                "sys.path",
            ],
        )
        self.assert_contains_all(
            fragment,
            [
                "paper/fragments/qX.md",
                "只使用正式结果表",
                "最终控制者负责 LaTeX 转换",
            ],
        )
        self.assert_contains_all(
            problem_guide,
            [
                "子问题写作指南模板",
                "子问题信息",
                "建模路线",
                "写作边界",
                "结果段落句式",
                "纸面结果见表/图[编号]",
            ],
        )
        self.assertNotIn("Problem X Guide Template", problem_guide)
        self.assertNotIn("Result Paragraph Pattern", problem_guide)
        self.assert_contains_all(
            section_templates,
            [
                "国奖式论文章节模板",
                "1.1 问题背景",
                "1.2 问题提出",
                "背景图是可选项",
                "假设默认 4-6 条",
                "框架优点",
                "证据钩子",
                "问题分析与思路概述",
                "模型准备",
                "问题一模型的建立与求解",
                "问题二模型的建立与求解",
                "通常合计占正文主要篇幅",
                "不要理解为问题一单独占 60%",
                "按题目权重、建模难度、数据处理量、结果表图和检验需求分配",
                "**问题一：**",
                "模型检验、灵敏度分析与结果讨论",
                "模型评价、改进与推广",
                "不要放目录",
            ],
        )
        self.assert_contains_all(
            phrase_library,
            [
                "国奖式段落句式库",
                "问题分析",
                "**问题一：**",
                "模型准备",
                "公式引入",
                "结果分析",
                "灵敏度与检验",
                "模型评价",
                "证据钩子",
                "模型的优点",
                "模型的缺点",
            ],
        )
        self.assert_contains_all(
            hub_writing,
            [
                "难点转译",
                "判定闭环",
                "跨问递推",
                "约束显式化",
                "不要只写统一坐标",
                "图像必须说明机制",
                "证据钩子",
            ],
        )
        self.assert_contains_all(
            hub_writer,
            [
                "竞赛论文写作",
                "证据可见段落结构",
                "分问闭环",
                "图表写作规则",
                "最终写作检查",
            ],
        )
        self.assertNotIn("Contest Paper Writer", hub_writer)
        self.assertNotIn("Short pattern", hub_writer)
        self.assert_contains_all(hub, ["math-templates", "reused template"])

    def test_figure_chart_templates_are_present_and_compile(self):
        index = read("math-figure/references/chart-template-index.md")
        readme = read("math-figure/assets/chart-templates/README.md")
        template_dir = ROOT / "math-figure" / "assets" / "chart-templates"
        expected_templates = [
            "dispatch_time_series.py",
            "feasibility_diagnostics.py",
            "pareto_frontier.py",
            "relative_change_heatmap.py",
            "sensitivity_tornado.py",
        ]

        self.assertEqual(
            sorted(path.name for path in template_dir.glob("*.py")),
            sorted(expected_templates + ["paper_style.py"]),
        )
        self.assert_contains_all(
            index,
            [
                "relative_change_heatmap.py",
                "pareto_frontier.py",
                "sensitivity_tornado.py",
                "feasibility_diagnostics.py",
                "dispatch_time_series.py",
                "figure_id",
                "post-figure conclusion",
            ],
        )
        self.assert_contains_all(
            readme,
            [
                "relative_change_heatmap.py",
                "Pareto",
                "tornado",
                "feasibility",
                "dispatch_time_series.py",
            ],
        )
        for template_name in expected_templates:
            source = read(f"math-figure/assets/chart-templates/{template_name}")
            with self.subTest(template=template_name):
                compile(source, str(template_dir / template_name), "exec")
                self.assert_contains_all(source, ["matplotlib.use(\"Agg\")", "save_outputs", "fig.savefig"])

    def test_figure_skill_has_contest_visual_triage_and_readiness_loop(self):
        figure = read("math-figure/SKILL.md")
        selection = read("math-figure/references/contest-chart-selection.md")
        pitfalls = read("math-figure/references/contest-figure-pitfalls.md")
        readiness = read("math-figure/references/visual-readiness-loop.md")
        script_dir = ROOT / "math-figure" / "scripts"

        self.assert_contains_all(
            figure,
            [
                "references/contest-chart-selection.md",
                "references/contest-figure-pitfalls.md",
                "references/visual-readiness-loop.md",
                "scripts/profile_result_table.py",
                "scripts/check_contest_figure.py",
                "light result-table profile",
                "contest evidence",
            ],
        )
        self.assert_contains_all(
            selection,
            [
                "结论类型",
                "数据结构",
                "评委阅读任务",
                "精确值优先表格",
                "机制图手工绘制",
                "国赛",
            ],
        )
        self.assert_contains_all(
            pitfalls,
            [
                "小样本均值柱",
                "双 Y 轴",
                "3D",
                "饼图",
                "Y 轴截断",
                "无 colorbar",
                "rainbow/jet",
                "一图多论点",
            ],
        )
        self.assert_contains_all(
            readiness,
            [
                "渲染预览",
                "中文缺字",
                "负号",
                "图例遮挡",
                "灰度可分",
                "最终尺寸",
                "AI 读图",
            ],
        )
        for script_name in ["profile_result_table.py", "check_contest_figure.py"]:
            source = read(f"math-figure/scripts/{script_name}")
            with self.subTest(script=script_name):
                compile(source, str(script_dir / script_name), "exec")

    def test_paper_facing_fenced_templates_do_not_leak_internal_qc_terms(self):
        forbidden_terms = ["run_id", "证据钩子", "judgment functions"]
        forbidden_english_result_patterns = [
            "Under [scenario]",
            "Table/Figure X",
            "This answers",
            "This means",
            "The result should be read",
            "support materials keep",
        ]
        for path in paper_facing_template_paths():
            text = path.read_text(encoding="utf-8")
            for index, block in enumerate(fenced_blocks(text), start=1):
                with self.subTest(path=str(path.relative_to(ROOT)), block=index):
                    for term in forbidden_terms:
                        self.assertNotIn(term, block)
                    for pattern in forbidden_english_result_patterns:
                        self.assertNotIn(pattern, block)

    def test_paper_facing_guidance_keeps_run_ids_out_of_body_evidence_options(self):
        forbidden_body_evidence_patterns = [
            "run_id=[编号]",
            "对应 run_id",
            "可用式[编号]、表[编号]、图[编号]、run_id",
            "挂接式[编号]、表[编号]、图[编号]、run_id",
        ]
        required_boundary_terms = ["运行记录", "支撑材料"]
        for path in paper_facing_template_paths():
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=str(path.relative_to(ROOT))):
                for pattern in forbidden_body_evidence_patterns:
                    self.assertNotIn(pattern, text)
                if "运行记录" in text or "run_id" in text:
                    self.assert_contains_all(text, required_boundary_terms)

    def test_copyable_subproblem_labels_use_fullwidth_colon_and_one_space(self):
        label_pattern = re.compile(r"\*\*问题[一二三四五六七八九十]+[：:]\s*\*\*\s*")
        good_label_pattern = re.compile(r"\*\*问题[一二三四五六七八九十]+：\*\* ")
        forbidden_patterns = [
            r"\*\*问题[一二三四五六七八九十]+:\*\*",
            r"\*\*问题[一二三四五六七八九十]+ ：\*\*",
            r"\*\*问题[一二三四五六七八九十]+：\*\*(?! )",
            r"\*\*问题[一二三四五六七八九十]+：\*\*  +",
        ]

        found_good_label = False
        for path in paper_facing_template_paths():
            text = path.read_text(encoding="utf-8")
            for index, block in enumerate(fenced_blocks(text), start=1):
                with self.subTest(path=str(path.relative_to(ROOT)), block=index):
                    for forbidden_pattern in forbidden_patterns:
                        self.assertIsNone(re.search(forbidden_pattern, block))
                    for label in label_pattern.findall(block):
                        found_good_label = True
                        self.assertRegex(label, good_label_pattern)

        self.assertTrue(found_good_label)

    def test_copyable_subproblem_paragraph_leads_are_bold(self):
        unbolded_lead_pattern = re.compile(r"(?m)^(问题[一二三四五六七八九十]+：)")

        for path in paper_facing_template_paths():
            text = path.read_text(encoding="utf-8")
            for index, block in enumerate(fenced_blocks(text), start=1):
                with self.subTest(path=str(path.relative_to(ROOT)), block=index):
                    self.assertIsNone(unbolded_lead_pattern.search(block))

    def test_model_evaluation_templates_keep_all_framework_advantage_types(self):
        model_eval_templates = {
            "math-templates/references/assumption-evaluation-controls.md": read(
                "math-templates/references/assumption-evaluation-controls.md"
            ),
            "math-templates/assets/contest-project-template/paper/section_templates_national.md": read(
                "math-templates/assets/contest-project-template/paper/section_templates_national.md"
            ),
            "math-templates/assets/contest-project-template/paper/paragraph_phrases_national.md": read(
                "math-templates/assets/contest-project-template/paper/paragraph_phrases_national.md"
            ),
            "math-hub/references/writing-templates.md": read("math-hub/references/writing-templates.md"),
        }

        for path, text in model_eval_templates.items():
            advantage_text = "\n".join(model_evaluation_advantage_lines(text))
            with self.subTest(path=path):
                self.assertIn("难点", advantage_text)
                self.assertIn("判定闭环", advantage_text)
                self.assertIn("跨问递推", advantage_text)
                self.assertIn("约束", advantage_text)

    def test_model_promotion_template_stays_compact_for_contest_papers(self):
        writing_templates = read("math-hub/references/writing-templates.md")

        self.assert_contains_all(
            writing_templates,
            [
                "## 十、模型推广与应用建议（默认并入模型评价）",
                "竞赛论文默认写 1 段，2-4 句",
                "同构场景",
                "改什么参数/数据/约束",
                "不要求跨领域类比",
                "不虚构量化收益",
            ],
        )
        for journal_style_requirement in [
            "四段式：场景迁移 → 参数适配 → 价值量化 → 边界与局限",
            "至少给出一个同领域放大场景和一个跨领域类比场景",
            "价值量化可以是估算",
            "第一段：同领域放大",
            "第二段：跨领域类比",
        ]:
            self.assertNotIn(journal_style_requirement, writing_templates)

    def test_national_phrase_library_uses_chinese_paper_facing_anchors(self):
        phrase_library = read("math-templates/assets/contest-project-template/paper/paragraph_phrases_national.md")

        self.assert_contains_all(
            phrase_library,
            [
                "# 国奖式段落句式库",
                "## 使用边界",
                "## 摘要",
                "## 问题分析",
                "## 模型准备",
                "## 公式引入",
                "## 求解方法",
                "## 结果分析",
                "## 灵敏度与检验",
                "## 模型评价",
            ],
        )

    def test_fragment_protocol_keeps_chinese_deliverable_boundary_without_renaming_files(self):
        fragment = read("math-templates/assets/contest-project-template/paper/fragments/fragment_protocol.md")

        self.assert_contains_all(
            fragment,
            [
                "# 论文片段协议",
                "## 使用场景",
                "## 子问题提示格式",
                "## 合并规则",
                "只负责论文片段",
                "只使用正式结果表",
                "最终控制者负责",
            ],
        )
        self.assert_contains_all(
            fragment,
            [
                "session_log.md or hub_state.json",
                "deliverable_matrix.csv",
                "paper/fragments/qX.md",
            ],
        )

    def test_template_reference_navigation_preserves_output_style_controls(self):
        reference_contracts = {
            "math-templates/references/section-format-controls.md": [
                "# 章节格式控制",
                "## 全局分问标签规则",
                "## 问题重述",
                "## 问题分析",
                "## 分问题模型章节",
            ],
            "math-templates/references/assumption-evaluation-controls.md": [
                "# 模型假设与评价控制",
                "## 模型假设",
                "## 模型评价",
                "## 框架优点的含义",
            ],
            "math-templates/references/contest-language-guardrails.md": [
                "# 竞赛论文语言护栏",
                "## 基本语气",
                "## 分问标签格式",
                "## 数字与单位",
                "## 结论强度",
            ],
            "math-templates/references/paragraph-flow.md": [
                "# 竞赛段落流",
                "## 核心原则",
                "## 读者检查",
                "## 分章节段落任务",
                "## 修复动作",
            ],
            "math-templates/references/template-usage.md": [
                "# 模板使用指南",
                "## 复制规则",
                "## 最小新项目骨架",
                "## 提升边界",
                "## 国奖式论文骨架",
            ],
            "math-templates/references/asset-library-index.md": [
                "# 轻资产库索引",
                "## 论文风格资产",
                "## 论文片段资产",
                "## 代码与复现资产",
                "## 迁移建议",
            ],
            "math-templates/references/national-prize-style-profile.md": [
                "# 国奖式风格画像",
                "## 风格信号",
                "## 避免事项",
                "## 相关资产",
            ],
            "math-templates/references/official-exemplar-notes.md": [
                "# 官方优秀论文观察",
                "## 2025 A196 观察",
                "可复用结构经验",
            ],
            "math-templates/references/prior-contest-patterns.md": [
                "# 既有竞赛项目模式",
                "## 可复用结构",
                "## 可迁移模式",
                "## 不要复制的内容",
                "## 模板审查问题",
            ],
        }
        for relative_path, required_terms in reference_contracts.items():
            text = read(relative_path)
            with self.subTest(path=relative_path):
                self.assert_contains_all(text, required_terms)

    def test_templates_skill_entrypoint_is_english_first_asset_library_mode(self):
        templates = read("math-templates/SKILL.md")
        metadata = read("math-templates/agents/openai.yaml")

        self.assert_contains_all(
            templates,
            [
                "# Math Modeling Templates",
                "## Purpose",
                "Default to **light asset library mode**",
                "Do not impose a project-management workflow",
                "## Asset Root",
                "## Optional Full Scaffold",
                "## Reuse Safety",
                "## Asset Selection",
                "## Output Contract",
                "National-prize paragraph phrases",
                "`math-hub`",
            ],
        )
        self.assert_contains_all(
            metadata,
            [
                'display_name: "Math Modeling Templates"',
                "lightweight",
                "paper assets",
                "Chinese is for paper-facing deliverables",
            ],
        )

    def test_national_first_standard_is_explicit_across_quality_gates(self):
        hub = read("math-hub/SKILL.md")
        review = read("math-review/SKILL.md")
        style_profile = read("math-templates/references/national-prize-style-profile.md")
        section_templates = read("math-templates/assets/contest-project-template/paper/section_templates_national.md")

        for path, text in {
            "math-hub/SKILL.md": hub,
            "math-review/SKILL.md": review,
            "math-templates/references/national-prize-style-profile.md": style_profile,
            "math-templates/assets/contest-project-template/paper/section_templates_national.md": section_templates,
        }.items():
            with self.subTest(path=path):
                self.assert_contains_all(
                    text,
                    [
                        "国一候选",
                        "不承诺获奖",
                        "题目贴合",
                        "建模洞察",
                        "证据可信",
                        "可复现",
                        "边界清楚",
                    ],
                )

        for path in [
            "math-hub/agents/openai.yaml",
            "math-review/agents/openai.yaml",
            "math-templates/agents/openai.yaml",
        ]:
            with self.subTest(path=path):
                metadata = read(path)
                self.assert_contains_all(metadata, ["国一候选", "证据", "边界"])

    def test_national_first_standard_reaches_model_code_and_figure_lanes(self):
        lane_contracts = {
            "math-model/SKILL.md": ["国一候选", "题目贴合", "建模洞察", "证据可信", "可复现", "边界清楚"],
            "math-code/SKILL.md": ["国一候选", "题目贴合", "建模洞察", "证据可信", "可复现", "边界清楚"],
            "math-figure/SKILL.md": ["国一候选", "题目贴合", "建模洞察", "证据可信", "可复现", "边界清楚"],
        }

        for path, required_terms in lane_contracts.items():
            with self.subTest(path=path):
                self.assert_contains_all(read(path), required_terms)

        for path in [
            "math-model/agents/openai.yaml",
            "math-code/agents/openai.yaml",
            "math-figure/agents/openai.yaml",
        ]:
            with self.subTest(path=path):
                metadata = read(path)
                self.assert_contains_all(metadata, ["国一候选", "证据", "边界"])

    def test_math_skill_entrypoints_keep_identity_without_language_locking(self):
        for skill in REVIEWED_SKILLS:
            with self.subTest(skill=skill):
                body = read(f"{skill}/SKILL.md")
                metadata = read(f"{skill}/agents/openai.yaml")
                description = frontmatter_value(body, "description")

                self.assertEqual(frontmatter_value(body, "name"), skill)
                self.assertRegex(body, r"(?m)^#\s+\S+")
                self.assertIn("高教社杯/CUMCM", description)
                self.assert_contains_all(
                    metadata,
                    ["interface:", "display_name:", "short_description:", "default_prompt:"],
                )

        hub = read("math-hub/SKILL.md")
        templates = read("math-templates/SKILL.md")
        readme = read("README.md")

        for path, text in {
            "math-hub/SKILL.md": hub,
            "math-templates/SKILL.md": templates,
            "README.md": readme,
        }.items():
            with self.subTest(path=path):
                self.assert_contains_all(
                    text,
                    [
                        "产出",
                        "交付文件",
                        "判断",
                        "该英文就用英文",
                        "算法名",
                        "字段",
                        "官方规则原文",
                        "不因中文化牺牲",
                    ],
                )

    def test_national_first_boundary_reaches_every_math_skill(self):
        required_terms = ["国一候选", "不承诺获奖", "题目贴合", "建模洞察", "证据可信", "可复现", "边界清楚"]

        for skill in REVIEWED_SKILLS:
            with self.subTest(skill=skill):
                self.assert_contains_all(read(f"{skill}/SKILL.md"), required_terms)
                self.assert_contains_all(read(f"{skill}/agents/openai.yaml"), ["国一候选", "证据", "边界"])

    def test_model_skill_has_model_family_triage_before_milp(self):
        model = read("math-model/SKILL.md")

        self.assert_contains_all(
            model,
            [
                "## Model Family Triage",
                "Do not choose MILP/MIP merely because the paper needs variables, objectives, and constraints",
                "discrete decision table",
                "network flow/DP before generic MILP",
                "MILP when logic constraints or coupled binary decisions need it",
                "continuous resource allocation",
                "LP/QP/convex optimization/nonlinear programming",
                "geometry or physics",
                "derivation, direct numerical evaluation, or simulation according to the mechanism",
                "use simulation only when",
                "time evolution",
                "dynamic model/state-space/time series",
                "ranking or evaluation",
                "indicator system + sensitivity",
                "uncertainty",
                "scenario/robust/stochastic analysis",
                "Use MILP/MIP only when",
                "discrete decisions",
                "linear or safely linearizable",
                "auditable decision or allocation output",
                "not as a generic wrapper",
            ],
        )
        self.assertNotIn("paper must output a complete decision table", model)

    def test_simulation_routes_are_selected_by_mechanism_fit(self):
        model = read("math-model/SKILL.md")
        code = read("math-code/SKILL.md")
        model_metadata = read("math-model/agents/openai.yaml")
        code_metadata = read("math-code/agents/openai.yaml")

        self.assert_contains_all(
            model,
            [
                "## Simulation Route Fitness",
                "Simulation is neither preferred nor downgraded by default",
                "best-fitting route for the subproblem mechanism and required deliverable",
                "keep simulation as validation, scenario exploration, or diagnostic evidence",
                "deterministic time-step / grid simulation",
                "discrete-event simulation",
                "Monte Carlo / scenario simulation",
                "agent-based / game simulation",
                "simulation + optimization",
                "Simulation Plan",
                "state variables",
                "initial/boundary conditions",
                "replications",
                "seeds",
                "step-size sensitivity",
                "downgrade rule",
                "single-run screenshots are diagnostic",
            ],
        )
        self.assert_contains_all(
            code,
            [
                "## 仿真执行门禁",
                "Simulation Plan",
                "qX_state_trajectory.csv",
                "qX_event_log.csv",
                "qX_simulation_summary.csv",
                "qX_replication_summary.csv",
                "qX_discretization_sensitivity.csv",
                "single stochastic run",
                "unchecked time step/grid",
                "screenshot-only output",
            ],
        )
        self.assert_contains_all(model_metadata, ["只有当题目机制需要", "选择仿真路线", "蒙特卡洛", "多主体", "Simulation Plan"])
        self.assert_contains_all(code_metadata, ["仿真", "状态轨迹", "事件日志", "随机种子"])

    def test_project_manifest_template_is_chinese_and_submission_focused(self):
        manifest = read("math-templates/assets/contest-project-template/project_manifest_template.md")

        self.assert_contains_all(
            manifest,
            [
                "# 竞赛项目清单模板",
                "## 当前锁定",
                "## 项目文件夹",
                "## 证据登记表",
                "## 最终提交包说明",
                "官方规则来源",
                "匿名性规则",
                "复现命令",
                "未解决问题",
            ],
        )
        self.assert_contains_all(
            manifest,
            [
                "data/raw/",
                "qX/src/",
                "result_registry.csv",
                "numerical_diagnostics.csv",
            ],
        )

    def test_reproduce_all_template_has_chinese_user_messages_and_compiles(self):
        source = read("math-templates/assets/contest-project-template/reproduce_all.py")

        compile(
            source,
            str(ROOT / "math-templates/assets/contest-project-template/reproduce_all.py"),
            "exec",
        )
        self.assert_contains_all(
            source,
            [
                "请替换为当前项目的正式脚本",
                "缺少正式脚本",
                "复现完成",
            ],
        )
        for english_user_message in [
            "Replace these entries",
            "Missing formal script",
            "Reproduction complete",
        ]:
            self.assertNotIn(english_user_message, source)


if __name__ == "__main__":
    unittest.main()
