import sys
from pathlib import Path

_rvg_path = str((Path(__file__).resolve().parent / "rvg").resolve())
if _rvg_path not in sys.path:
    sys.path.insert(0, _rvg_path)
