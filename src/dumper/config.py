import os
from pathlib import Path

EXAMPLES: bool = os.getenv("EXAMPLES", "false").lower() == "true"

DATA_DIR: Path = Path(os.getenv("DATA_DIR", Path.cwd() / "data"))
