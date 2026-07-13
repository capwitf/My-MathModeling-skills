from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

from paper_style import CONTEST_PAPER_COLORS, apply_paper_style, configure_paper_matplotlib


def save_outputs(fig: plt.Figure, output_base: Path | str) -> list[Path]:
    output_base = Path(output_base)
    output_base.parent.mkdir(parents=True, exist_ok=True)
    paths = [output_base.with_suffix(ext) for ext in [".svg", ".pdf", ".png"]]
    for path in paths:
        fig.savefig(path, bbox_inches="tight", dpi=300)
    return paths


def plot_pareto_frontier(
    data: pd.DataFrame,
    *,
    x: str,
    y: str,
    output_base: Path | str,
    label: str | None = None,
    selected: str | None = None,
    x_label: str | None = None,
    y_label: str | None = None,
) -> list[Path]:
    configure_paper_matplotlib()
    frame = data.sort_values(x).reset_index(drop=True)
    fig, ax = plt.subplots(figsize=(6.8, 4.6), dpi=220)
    ax.plot(
        frame[x],
        frame[y],
        color=CONTEST_PAPER_COLORS["accent_blue"],
        linewidth=1.8,
        marker="o",
        markersize=4,
        label="candidate frontier",
    )

    if selected is not None and selected in frame.columns:
        chosen = frame.loc[frame[selected].astype(bool)]
        if not chosen.empty:
            ax.scatter(
                chosen[x],
                chosen[y],
                s=90,
                color=CONTEST_PAPER_COLORS["accent_orange"],
                edgecolor="white",
                linewidth=1.0,
                zorder=4,
                label="selected",
            )

    if label is not None and label in frame.columns:
        for _, item in frame.iterrows():
            ax.annotate(str(item[label]), (item[x], item[y]), xytext=(4, 4), textcoords="offset points", fontsize=7)

    ax.set_xlabel(x_label or x)
    ax.set_ylabel(y_label or y)
    apply_paper_style(ax, grid_axis="both")
    ax.legend(frameon=False)
    fig.tight_layout()
    paths = save_outputs(fig, output_base)
    plt.close(fig)
    return paths


if __name__ == "__main__":
    demo = pd.DataFrame(
        {
            "cost": [120, 135, 150, 180],
            "risk": [0.42, 0.31, 0.24, 0.20],
            "plan": ["P1", "P2", "P3", "P4"],
            "selected": [False, False, True, False],
        }
    )
    plot_pareto_frontier(demo, x="cost", y="risk", label="plan", selected="selected", output_base=Path("pareto_frontier_demo"))
