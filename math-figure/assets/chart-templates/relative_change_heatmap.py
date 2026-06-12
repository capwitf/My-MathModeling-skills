from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def save_outputs(fig: plt.Figure, output_base: Path | str) -> list[Path]:
    output_base = Path(output_base)
    output_base.parent.mkdir(parents=True, exist_ok=True)
    paths = [output_base.with_suffix(ext) for ext in [".svg", ".pdf", ".png"]]
    for path in paths:
        fig.savefig(path, bbox_inches="tight", dpi=300)
    return paths


def plot_relative_change_heatmap(
    data: pd.DataFrame,
    *,
    row: str,
    column: str,
    value: str,
    output_base: Path | str,
    baseline: float = 0.0,
    value_label: str = "Relative change (%)",
    annotate: bool = True,
) -> list[Path]:
    pivot = data.pivot(index=row, columns=column, values=value)
    matrix = pivot.to_numpy(dtype=float)
    max_abs = float(np.nanmax(np.abs(matrix - baseline))) if matrix.size else 1.0
    max_abs = max(max_abs, 1e-12)

    fig, ax = plt.subplots(figsize=(7.2, 4.8), dpi=220)
    image = ax.imshow(matrix, cmap="RdBu_r", vmin=baseline - max_abs, vmax=baseline + max_abs, aspect="auto")
    ax.set_xticks(range(len(pivot.columns)))
    ax.set_xticklabels(pivot.columns, rotation=35, ha="right")
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels(pivot.index)
    ax.set_xlabel(column)
    ax.set_ylabel(row)
    cbar = fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label(value_label)

    if annotate:
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if np.isfinite(matrix[i, j]):
                    ax.text(j, i, f"{matrix[i, j]:.1f}", ha="center", va="center", fontsize=7)

    fig.tight_layout()
    paths = save_outputs(fig, output_base)
    plt.close(fig)
    return paths


if __name__ == "__main__":
    demo = pd.DataFrame(
        {
            "scenario": ["S1", "S1", "S2", "S2"],
            "method": ["A", "B", "A", "B"],
            "change_pct": [0.0, -8.4, 3.1, -12.7],
        }
    )
    plot_relative_change_heatmap(
        demo,
        row="scenario",
        column="method",
        value="change_pct",
        output_base=Path("relative_change_heatmap_demo"),
    )
