import os
from importlib import import_module
from pathlib import Path

from src.app import app

ROOT = Path(__file__).parent


def import_listeners(directory: Path):
    for path in sorted(directory.rglob("[!_]*.py")):
        import_module(".".join(path.relative_to(ROOT).with_suffix("").parts))


import_listeners(ROOT / "src" / "listeners")

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", "3000")))
