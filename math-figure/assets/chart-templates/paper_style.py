from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

import matplotlib.pyplot as plt


PALETTE = {
    "blue_main": "#0F4D92",
    "blue_secondary": "#3775BA",
    "green_1": "#DDF3DE",
    "green_2": "#AADCA9",
    "green_3": "#8BCF8B",
    "red_1": "#F6CFCB",
    "red_2": "#E9A6A1",
    "red_strong": "#B64342",
    "neutral_light": "#CFCECE",
    "neutral_mid": "#767676",
    "neutral_dark": "#4D4D4D",
    "neutral_black": "#272727",
    "gold": "#FFD700",
    "teal": "#42949E",
    "violet": "#9A4D8E",
    "magenta": "#EA84DD",
}

DEFAULT_COLORS = [
    PALETTE["blue_main"],
    PALETTE["green_3"],
    PALETTE["red_strong"],
    PALETTE["teal"],
    PALETTE["violet"],
    PALETTE["neutral_light"],
]

CONTEST_PAPER_COLORS = {
    "main_text": "#1F2933",
    "muted_text": "#5B6770",
    "axis": "#8A949E",
    "grid": "#E6E8EB",
    "accent_blue": "#4E79A7",
    "accent_orange": "#F28E2B",
    "accent_teal": "#59A14F",
    "accent_red": "#D95F5F",
    "accent_purple": "#8C6BB1",
    "neutral_fill": "#F7F8FA",
}

CONTEST_PAPER_SERIES = [
    CONTEST_PAPER_COLORS["accent_blue"],
    CONTEST_PAPER_COLORS["accent_orange"],
    CONTEST_PAPER_COLORS["accent_teal"],
    CONTEST_PAPER_COLORS["accent_red"],
    CONTEST_PAPER_COLORS["accent_purple"],
]


def apply_publication_style(font_size: int = 9, axes_linewidth: float = 0.8, use_tex: bool = False) -> None:
    configure_paper_matplotlib()
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "Microsoft YaHei", "SimSun"],
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
            "font.size": font_size,
            "axes.linewidth": axes_linewidth,
            "legend.frameon": False,
            "text.usetex": use_tex,
        }
    )


def configure_paper_matplotlib() -> None:
    plt.rcParams.update(
        {
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "axes.edgecolor": CONTEST_PAPER_COLORS["axis"],
            "axes.labelcolor": CONTEST_PAPER_COLORS["main_text"],
            "xtick.color": CONTEST_PAPER_COLORS["muted_text"],
            "ytick.color": CONTEST_PAPER_COLORS["muted_text"],
            "text.color": CONTEST_PAPER_COLORS["main_text"],
            "font.family": ["SimSun", "Microsoft YaHei", "DejaVu Serif"],
            "axes.unicode_minus": False,
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
        }
    )


def apply_paper_style(ax, *, grid_axis: str = "y", hide_top_right: bool = True) -> None:
    ax.grid(axis=grid_axis, color=CONTEST_PAPER_COLORS["grid"], linewidth=0.6)
    ax.set_axisbelow(True)
    if hide_top_right:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
    for side in ["left", "bottom"]:
        ax.spines[side].set_color(CONTEST_PAPER_COLORS["axis"])
        ax.spines[side].set_linewidth(0.8)
    ax.tick_params(axis="both", colors=CONTEST_PAPER_COLORS["muted_text"], labelsize=9)
    ax.title.set_visible(False)


def add_panel_label(
    ax,
    label: str,
    *,
    x: float = -0.06,
    y: float = 1.02,
    fontsize: int = 12,
    color: str | None = None,
    fontweight: str = "bold",
) -> None:
    ax.text(
        x,
        y,
        label,
        transform=ax.transAxes,
        fontsize=fontsize,
        fontweight=fontweight,
        color=color or CONTEST_PAPER_COLORS["main_text"],
        ha="left",
        va="bottom",
    )


def style_dark_image_ax(ax, *, facecolor: str = "black") -> None:
    ax.set_facecolor(facecolor)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


def get_series_colors(count: int) -> list[str]:
    if count <= 0:
        return []
    repeated: Iterable[str] = (
        CONTEST_PAPER_SERIES[index % len(CONTEST_PAPER_SERIES)]
        for index in range(count)
    )
    return list(repeated)


def make_grouped_bar(
    ax,
    categories,
    series,
    labels,
    *,
    ylabel: str = "Value",
    colors: list[str] | None = None,
    annotate: bool = False,
    bar_width: float = 0.8,
):
    import numpy as np

    colors = colors or get_series_colors(len(series))
    n_groups = len(series)
    x = np.arange(len(categories))
    width = bar_width / max(n_groups, 1)
    containers = []
    for index, (values, label, color) in enumerate(zip(series, labels, colors)):
        offset = (index - (n_groups - 1) / 2) * width
        bars = ax.bar(
            x + offset,
            values,
            width=width,
            label=label,
            color=color,
            edgecolor="white",
            linewidth=0.8,
        )
        containers.append(bars)
        if annotate:
            for bar, value in zip(bars, values):
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_height(),
                    f"{value:.2f}",
                    ha="center",
                    va="bottom",
                    fontsize=8,
                )
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.set_ylabel(ylabel)
    apply_paper_style(ax)
    ax.legend(frameon=False)
    return containers


def make_trend(
    ax,
    x,
    y_series,
    labels,
    *,
    colors: list[str] | None = None,
    ylabel: str | None = None,
    xlabel: str | None = None,
    show_shadow: bool = False,
    shadow_alpha: float = 0.15,
    linewidth: float = 1.8,
    marker: str = "o",
):
    import numpy as np

    colors = colors or get_series_colors(len(y_series))
    for values, label, color in zip(y_series, labels, colors):
        array = np.asarray(values)
        if array.ndim == 2:
            mean = array.mean(axis=0)
            std = array.std(axis=0)
        else:
            mean = array
            std = None
        ax.plot(x, mean, color=color, linewidth=linewidth, marker=marker, label=label)
        if show_shadow and std is not None:
            ax.fill_between(x, mean - std, mean + std, color=color, alpha=shadow_alpha)
    if ylabel:
        ax.set_ylabel(ylabel)
    if xlabel:
        ax.set_xlabel(xlabel)
    apply_paper_style(ax)
    ax.legend(frameon=False)


def make_heatmap(
    ax,
    matrix,
    *,
    x_labels=None,
    y_labels=None,
    cmap: str = "viridis",
    cbar_label: str | None = None,
    annotate: bool = False,
    fmt: str = "{:.2f}",
):
    import numpy as np

    image = ax.imshow(matrix, cmap=cmap, aspect="auto")
    if cbar_label:
        colorbar = ax.figure.colorbar(image, ax=ax)
        colorbar.set_label(cbar_label)
    if x_labels is not None:
        ax.set_xticks(range(len(x_labels)))
        ax.set_xticklabels(x_labels, rotation=30, ha="right")
    if y_labels is not None:
        ax.set_yticks(range(len(y_labels)))
        ax.set_yticklabels(y_labels)
    if annotate:
        values = np.asarray(matrix)
        midpoint = (np.nanmin(values) + np.nanmax(values)) / 2
        for (row, col), value in np.ndenumerate(values):
            ax.text(
                col,
                row,
                fmt.format(value),
                ha="center",
                va="center",
                fontsize=8,
                color="white" if value < midpoint else CONTEST_PAPER_COLORS["main_text"],
            )
    ax.set_frame_on(False)
    ax.title.set_visible(False)
    return image


def make_forest_plot(
    ax,
    labels,
    estimates,
    ci_low,
    ci_high,
    *,
    colors: list[str] | None = None,
    ref: float = 0.0,
    xlabel: str | None = None,
):
    import numpy as np

    y_positions = np.arange(len(labels))[::-1]
    colors = colors or [CONTEST_PAPER_COLORS["accent_red"]] * len(labels)
    for y, estimate, low, high, color in zip(y_positions, estimates, ci_low, ci_high, colors):
        ax.plot([low, high], [y, y], color=color, linewidth=1.5)
        ax.plot(estimate, y, marker="o", markersize=5, color=color)
    ax.axvline(ref, color=CONTEST_PAPER_COLORS["muted_text"], linestyle="--", linewidth=1.0)
    ax.set_yticks(y_positions)
    ax.set_yticklabels(labels)
    if xlabel:
        ax.set_xlabel(xlabel)
    apply_paper_style(ax, grid_axis="x")


def finalize_figure(
    fig,
    output_base: str | Path,
    *,
    formats: list[str] | None = None,
    dpi: int = 300,
    close: bool = True,
) -> list[Path]:
    base = Path(output_base)
    if formats is None:
        if base.suffix:
            formats = [base.suffix.lstrip(".")]
            base = base.with_suffix("")
        else:
            formats = ["svg", "pdf", "png"]
    base.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    paths: list[Path] = []
    for fmt in formats:
        path = base.with_suffix(f".{fmt}")
        save_kwargs = {"bbox_inches": "tight"}
        if fmt.lower() in {"png", "tif", "tiff", "jpg", "jpeg"}:
            save_kwargs["dpi"] = dpi
        fig.savefig(path, **save_kwargs)
        paths.append(path)
    if close:
        plt.close(fig)
    return paths
