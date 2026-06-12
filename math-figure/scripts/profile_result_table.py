from __future__ import annotations

import argparse
import json
import warnings
from pathlib import Path
from typing import Any

import pandas as pd


def _read_table(path: Path) -> pd.DataFrame:
    suffix = path.suffix.lower()
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(path)
    return pd.read_csv(path, encoding="utf-8-sig")


def _kind(series: pd.Series) -> str:
    non_null = series.dropna()
    if pd.api.types.is_bool_dtype(series):
        return "boolean"
    if pd.api.types.is_numeric_dtype(series):
        if non_null.nunique() <= 7 and non_null.astype(float).mod(1).eq(0).all():
            return "ordinal_or_small_integer"
        return "numeric"
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        parsed = pd.to_datetime(non_null.head(12), errors="coerce")
    if len(non_null) > 0 and parsed.notna().mean() >= 0.8:
        return "datetime_like"
    if non_null.nunique() <= min(30, max(3, len(non_null) // 2)):
        return "categorical"
    return "text"


def profile_result_table(path: str | Path) -> dict[str, Any]:
    table_path = Path(path)
    frame = _read_table(table_path)
    columns: list[dict[str, Any]] = []

    for name in frame.columns:
        series = frame[name]
        non_null = series.dropna()
        info: dict[str, Any] = {
            "name": str(name),
            "kind": _kind(series),
            "missing_count": int(series.isna().sum()),
            "missing_rate": float(series.isna().mean()),
            "unique_count": int(non_null.nunique()),
        }
        if pd.api.types.is_numeric_dtype(series) and len(non_null) > 0:
            info.update(
                {
                    "min": float(non_null.min()),
                    "max": float(non_null.max()),
                    "mean": float(non_null.mean()),
                    "median": float(non_null.median()),
                }
            )
        columns.append(info)

    numeric = [c["name"] for c in columns if c["kind"] in {"numeric", "ordinal_or_small_integer"}]
    categorical = [c["name"] for c in columns if c["kind"] == "categorical"]
    datetime_like = [c["name"] for c in columns if c["kind"] == "datetime_like"]

    candidates: list[str] = []
    if datetime_like and numeric:
        candidates.append("trend_or_state_sequence: line/stepped line with units and threshold markers")
    if categorical and numeric:
        candidates.append("scenario_or_method_comparison: grouped bar or relative-change heatmap")
    if len(numeric) >= 2:
        candidates.append("tradeoff_or_frontier: scatter/Pareto if a selected policy must be defended")
    if not candidates:
        candidates.append("table_first: exact values or sparse outputs are clearer as a table")

    return {
        "path": str(table_path),
        "row_count": int(len(frame)),
        "column_count": int(len(frame.columns)),
        "columns": columns,
        "candidate_chart_routes": candidates,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Profile a contest result table before choosing a figure.")
    parser.add_argument("path", help="CSV or Excel result table")
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON")
    args = parser.parse_args()

    report = profile_result_table(args.path)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return

    print(f"table: {report['path']}")
    print(f"shape: {report['row_count']} rows x {report['column_count']} columns")
    print("columns:")
    for column in report["columns"]:
        print(
            f"- {column['name']}: {column['kind']}, "
            f"missing={column['missing_count']}, unique={column['unique_count']}"
        )
    print("candidate chart routes:")
    for route in report["candidate_chart_routes"]:
        print(f"- {route}")


if __name__ == "__main__":
    main()
