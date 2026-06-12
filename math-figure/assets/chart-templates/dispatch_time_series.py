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


def plot_dispatch_time_series(
    data: pd.DataFrame,
    *,
    time: str,
    supply_columns: list[str],
    demand_column: str,
    output_base: Path | str,
    state_column: str | None = None,
    y_label: str = "Power",
    state_label: str = "State",
) -> list[Path]:
    frame = data.sort_values(time)
    fig, ax = plt.subplots(figsize=(8.2, 4.8), dpi=220)
    ax.stackplot(frame[time], *[frame[col] for col in supply_columns], labels=supply_columns, alpha=0.82)
    ax.plot(frame[time], frame[demand_column], color="#263238", linewidth=2.0, label=demand_column)
    ax.set_xlabel(time)
    ax.set_ylabel(y_label)
    ax.grid(axis="y", color="#DDDDDD", linewidth=0.6)

    if state_column is not None and state_column in frame.columns:
        ax2 = ax.twinx()
        ax2.plot(frame[time], frame[state_column], color="#C44E52", linewidth=1.8, linestyle="--", label=state_column)
        ax2.set_ylabel(state_label)
        handles1, labels1 = ax.get_legend_handles_labels()
        handles2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(handles1 + handles2, labels1 + labels2, frameon=False, ncol=2, loc="upper left")
    else:
        ax.legend(frameon=False, ncol=2, loc="upper left")

    fig.tight_layout()
    paths = save_outputs(fig, output_base)
    plt.close(fig)
    return paths


if __name__ == "__main__":
    demo = pd.DataFrame(
        {
            "hour": [1, 2, 3, 4],
            "wind": [5, 7, 4, 3],
            "solar": [0, 2, 6, 3],
            "grid": [4, 1, 0, 2],
            "load": [9, 10, 9, 8],
            "storage_state": [2, 3, 5, 4],
        }
    )
    plot_dispatch_time_series(
        demo,
        time="hour",
        supply_columns=["wind", "solar", "grid"],
        demand_column="load",
        state_column="storage_state",
        output_base=Path("dispatch_time_series_demo"),
    )
