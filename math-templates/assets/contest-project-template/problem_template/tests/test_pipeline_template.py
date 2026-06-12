from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import pytest


SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

pytestmark = [
    pytest.mark.filterwarnings("ignore:.*parseString.*:DeprecationWarning"),
    pytest.mark.filterwarnings("ignore:.*resetCache.*:DeprecationWarning"),
    pytest.mark.filterwarnings("ignore:.*enablePackrat.*:DeprecationWarning"),
]


def test_compute_template_writes_summary(tmp_path: Path) -> None:
    from compute_template import run_compute

    data_dir = tmp_path / "q1" / "src" / "data"
    result_dir = tmp_path / "results" / "q1"
    data_dir.mkdir(parents=True)
    pd.DataFrame(
        [
            {"entity_id": "a", "value": 1.0},
            {"entity_id": "b", "value": 2.0},
        ]
    ).to_csv(data_dir / "input.csv", index=False, encoding="utf-8")

    result = run_compute(data_dir=data_dir, result_dir=result_dir, run_id="unit-q1")

    summary = pd.read_csv(result["summary_path"], encoding="utf-8-sig")
    assert summary.loc[0, "run_id"] == "unit-q1"
    assert summary.loc[0, "value"] == 3.0
    assert summary.loc[0, "validation_status"] == "computed"


def test_plot_template_writes_figure_and_plan(tmp_path: Path) -> None:
    from compute_template import run_compute
    from plot_template import run_plot

    data_dir = tmp_path / "q1" / "src" / "data"
    result_dir = tmp_path / "results" / "q1"
    data_dir.mkdir(parents=True)
    pd.DataFrame([{"entity_id": "a", "value": 1.0}]).to_csv(
        data_dir / "input.csv", index=False, encoding="utf-8"
    )

    run_compute(data_dir=data_dir, result_dir=result_dir, run_id="unit-q1")
    result = run_plot(result_dir=result_dir)

    assert result["figures"][0].stat().st_size > 0
    plan = pd.read_csv(result["figure_plan_path"], encoding="utf-8-sig")
    assert plan.loc[0, "figure_id"] == "q1_fig1_summary_bar"
    assert plan.loc[0, "validation_status"] == "generated"
