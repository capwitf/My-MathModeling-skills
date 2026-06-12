from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_RESULT_DIR = REPO_ROOT / "results" / "q1"


FIGURE_PLAN_FIELDS = [
    "figure_id",
    "figure_path",
    "paper_role",
    "claim_id",
    "source_table",
    "plot_family",
    "plot_type",
    "why_this_plot",
    "caption_draft",
    "post_figure_conclusion_draft",
    "risk_note",
    "validation_status",
]


def read_required_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Required result CSV is missing: {path}")
    return pd.read_csv(path, encoding="utf-8-sig")


def ensure_nonblank(path: Path) -> None:
    if not path.exists() or path.stat().st_size == 0:
        raise RuntimeError(f"Figure was not written or is empty: {path}")


def run_plot(result_dir: Path | str = DEFAULT_RESULT_DIR) -> dict[str, object]:
    result_dir = Path(result_dir)
    summary_path = result_dir / "q1_summary.csv"
    summary = read_required_csv(summary_path)

    figure_path = result_dir / "q1_summary_bar.png"
    fig, ax = plt.subplots(figsize=(6.5, 3.8), dpi=220)
    ax.bar(summary["metric"], summary["value"], color="#4C78A8", alpha=0.88)
    ax.set_ylabel("Value (active problem unit)")
    ax.grid(axis="y", color="#DDDDDD", linewidth=0.6)
    fig.tight_layout()
    fig.savefig(figure_path)
    plt.close(fig)
    ensure_nonblank(figure_path)

    figure_plan_path = result_dir / "q1_figure_plan.csv"
    plan = pd.DataFrame(
        [
            {
                "figure_id": "q1_fig1_summary_bar",
                "figure_path": str(figure_path.resolve()),
                "paper_role": "claim",
                "claim_id": "q1_main_result",
                "source_table": str(summary_path.resolve()),
                "plot_family": "comparison",
                "plot_type": "bar",
                "why_this_plot": "Replace with the exact claim this figure proves.",
                "caption_draft": "Replace with object, scenario, metric, and what to notice.",
                "post_figure_conclusion_draft": "Replace with the one-sentence conclusion supported by the figure.",
                "risk_note": "Replace with assumption, diagnostic, or boundary note.",
                "validation_status": "generated",
            }
        ],
        columns=FIGURE_PLAN_FIELDS,
    )
    plan.to_csv(figure_plan_path, index=False, encoding="utf-8")

    return {
        "figures": [figure_path],
        "figure_plan_path": figure_plan_path,
    }


def main() -> None:
    result = run_plot()
    print("plot complete")
    for figure in result["figures"]:
        print(figure)


if __name__ == "__main__":
    main()
