from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any


VECTOR_EXTS = {".pdf", ".svg", ".eps"}
RASTER_EXTS = {".png", ".tif", ".tiff"}
LOSSY_EXTS = {".jpg", ".jpeg"}


def check_contest_figure(path: str | Path, min_dpi: int = 300) -> tuple[list[tuple[str, str]], dict[str, Any]]:
    figure_path = Path(path)
    issues: list[tuple[str, str]] = []
    info: dict[str, Any] = {"path": str(figure_path), "exists": figure_path.exists()}

    if not figure_path.exists():
        return [("FAIL", "figure file does not exist")], info
    if figure_path.stat().st_size == 0:
        issues.append(("FAIL", "figure file is empty"))

    ext = figure_path.suffix.lower()
    info["ext"] = ext.lstrip(".")
    if ext in LOSSY_EXTS:
        issues.append(("FAIL", "JPEG is not suitable for line/text-heavy contest data figures"))
    elif ext not in VECTOR_EXTS and ext not in RASTER_EXTS:
        issues.append(("WARN", "unknown figure format; prefer PDF/SVG or PNG/TIFF"))

    if ext in RASTER_EXTS or ext in LOSSY_EXTS:
        try:
            from PIL import Image
        except ImportError:
            issues.append(("INFO", "Pillow is not installed; skipping raster size and DPI checks"))
            return issues, info

        try:
            image = Image.open(figure_path)
            info["size_px"] = image.size
            dpi = image.info.get("dpi")
            info["dpi"] = dpi
            if dpi is None:
                issues.append(("WARN", "raster figure has no embedded DPI metadata"))
            else:
                dpi_value = dpi[0] if isinstance(dpi, tuple) else dpi
                if round(float(dpi_value)) < min_dpi:
                    issues.append(("FAIL", f"raster DPI is below {min_dpi}"))
        except Exception as exc:
            issues.append(("FAIL", f"cannot read raster figure: {exc}"))

    return issues, info


def print_report(path: str | Path, issues: list[tuple[str, str]], info: dict[str, Any]) -> None:
    print(f"figure: {path}")
    for key, value in info.items():
        print(f"{key}: {value}")
    if not issues:
        print("OK: no deterministic format issues found")
        return
    for severity, message in issues:
        print(f"{severity}: {message}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Check contest figure files for deterministic readiness issues.")
    parser.add_argument("figures", nargs="+", help="figure files to inspect")
    parser.add_argument("--min-dpi", type=int, default=300)
    parser.add_argument("--strict", action="store_true", help="exit nonzero when any FAIL issue is found")
    args = parser.parse_args()

    has_fail = False
    for figure in args.figures:
        issues, info = check_contest_figure(figure, min_dpi=args.min_dpi)
        print_report(figure, issues, info)
        has_fail = has_fail or any(severity == "FAIL" for severity, _ in issues)
    if args.strict and has_fail:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
