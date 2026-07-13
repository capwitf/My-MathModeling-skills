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


def plot_feasibility_diagnostics(
    data: pd.DataFrame,
    *,
    scenario: str,
    violation: str,
    threshold: float,
    output_base: Path | str,
    y_label: str = "Maximum violation",
) -> list[Path]:
    configure_paper_matplotlib()
    frame = data.copy().sort_values(violation, ascending=False)
    colors = [
        CONTEST_PAPER_COLORS["accent_red"] if value > threshold else CONTEST_PAPER_COLORS["accent_teal"]
        for value in frame[violation].astype(float)
    ]

    fig, ax = plt.subplots(figsize=(7.4, 4.8), dpi=220)
    ax.barh(frame[scenario], frame[violation], color=colors, alpha=0.88)
    ax.axvline(threshold, color=CONTEST_PAPER_COLORS["main_text"], linewidth=1.2, linestyle="--", label="threshold")
    ax.set_xlabel(y_label)
    ax.set_ylabel(scenario)
    apply_paper_style(ax, grid_axis="x")
    ax.legend(frameon=False)
    fig.tight_layout()
    paths = save_outputs(fig, output_base)
    plt.close(fig)
    return paths


if __name__ == "__main__":
    demo = pd.DataFrame(
        {
            "scenario": ["S1", "S2", "S3", "S4"],
            "max_violation": [0.0, 0.002, 0.0, 0.015],
        }
    )
    plot_feasibility_diagnostics(
        demo,
        scenario="scenario",
        violation="max_violation",
        threshold=0.005,
        output_base=Path("feasibility_diagnostics_demo"),
    )
