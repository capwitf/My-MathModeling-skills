from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent

# 请替换为当前项目的正式脚本。
SCRIPTS = [
    ROOT / "q1" / "src" / "compute.py",
    ROOT / "q1" / "src" / "plot.py",
]


def main() -> None:
    for script in SCRIPTS:
        if not script.exists():
            raise FileNotFoundError(f"缺少正式脚本：{script}")
        print(f"[RUN] {script.relative_to(ROOT)}")
        subprocess.run([sys.executable, str(script)], cwd=ROOT, check=True)
    print("复现完成。")


if __name__ == "__main__":
    main()
