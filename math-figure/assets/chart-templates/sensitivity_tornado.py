from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd


def save_outputs(fig: plt.Figure, output_base: Path | str) -> list[Path]:
    output_base = Path(output_base)
    output_base.parent.mkdir(parents=True, exist_ok=True)
    paths = [output_base.with_suffix(ext) for ext in [".svg", ".pdf", ".png"]]
    for path in paths:
        fig.savefig(path, bbox_inches="tight", dpi=300)
    return paths


def plot_sensitivity_tornado(
    data: pd.DataFrame,
    *,
    parameter: str,
    low: str,
    high: str,
    baseline: float,
    output_base: Path | str,
    x_label: str = "Change from baseline",
) -> list[Path]:
    frame = data.copy()
    frame["low_delta"] = frame[low].astype(float) - baseline
    frame["high_delta"] = frame[high].astype(float) - baseline
    frame["span"] = (frame["high_delta"] - frame["low_delta"]).abs()
    frame = frame.sort_values("span", ascending=True)

    fig, ax = plt.subplots(figsize=(7.2, 4.8), dpi=220)
    y_positions = range(len(frame))
    ax.barh(y_positions, frame["low_delta"], color="#72B7B2", alpha=0.85, label="low case")
    ax.barh(y_positions, frame["high_delta"], color="#C44E52", alpha=0.85, label="high case")
    ax.axvline(0, color="#263238", linewidth=1.1)
    ax.set_yticks(list(y_positions))
    ax.set_yticklabels(frame[parameter])
    ax.set_xlabel(x_label)
    ax.grid(axis="x", color="#DDDDDD", linewidth=0.6)
    ax.legend(frameon=False, loc="lower right")
    fig.tight_layout()
    paths = save_outputs(fig, output_base)
    plt.close(fig)
    return paths


if __name__ == "__main__":
    demo = pd.DataFrame(
        {
            "parameter": ["price", "capacity", "efficiency", "demand"],
            "low_value": [95, 102, 98, 91],
            "high_value": [112, 107, 105, 118],
        }
    )
    plot_sensitivity_tornado(
        demo,
        parameter="parameter",
        low="low_value",
        high="high_value",
        baseline=100,
        output_base=Path("sensitivity_tornado_demo"),
    )
