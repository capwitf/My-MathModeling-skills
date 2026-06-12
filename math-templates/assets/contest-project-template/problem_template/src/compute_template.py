from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Iterable

import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DATA_DIR = REPO_ROOT / "q1" / "src" / "data"
DEFAULT_RESULT_DIR = REPO_ROOT / "results" / "q1"


def default_run_id(prefix: str = "q1") -> str:
    stamp = datetime.now().astimezone().strftime("%Y%m%dT%H%M%S")
    return f"{prefix}_{stamp}"


def read_required_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Required input CSV is missing: {path}")
    return pd.read_csv(path, encoding="utf-8-sig")


def require_columns(df: pd.DataFrame, file_name: str, columns: Iterable[str]) -> None:
    missing = [column for column in columns if column not in df.columns]
    if missing:
        raise ValueError(f"{file_name} missing required column(s): {', '.join(missing)}")


def numeric_column(df: pd.DataFrame, file_name: str, column: str) -> pd.Series:
    values = pd.to_numeric(df[column], errors="coerce")
    if values.isna().any():
        raise ValueError(f"{file_name} column {column} contains non-numeric or empty values")
    return values


def run_compute(
    data_dir: Path | str = DEFAULT_DATA_DIR,
    result_dir: Path | str = DEFAULT_RESULT_DIR,
    run_id: str | None = None,
) -> dict[str, object]:
    data_dir = Path(data_dir)
    result_dir = Path(result_dir)
    run_id = run_id or default_run_id("q1")

    # Replace this input contract with the active problem's source files.
    input_path = data_dir / "input.csv"
    df = read_required_csv(input_path)
    require_columns(df, input_path.name, ["entity_id", "value"])
    df = df.copy()
    df["value"] = numeric_column(df, input_path.name, "value")

    result_dir.mkdir(parents=True, exist_ok=True)
    summary_path = result_dir / "q1_summary.csv"

    summary = pd.DataFrame(
        [
            {
                "run_id": run_id,
                "metric": "total_value",
                "value": float(df["value"].sum()),
                "unit": "active_problem_unit",
                "validation_status": "computed",
            }
        ]
    )
    summary.to_csv(summary_path, index=False, encoding="utf-8", float_format="%.12g")

    return {
        "run_id": run_id,
        "summary_path": summary_path,
        "summary": summary.iloc[0].to_dict(),
    }


def main() -> None:
    result = run_compute()
    print(f"compute complete: run_id={result['run_id']}")
    print(result["summary_path"])


if __name__ == "__main__":
    main()
