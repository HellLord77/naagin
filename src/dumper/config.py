import os
from pathlib import Path

EXAMPLES: bool = os.getenv("EXAMPLES", "false").lower() == "true"

VERSION: str = os.getenv("VERSION", 10)
APP_VERSION: int = int(os.getenv("APP_VERSION", 64800))

DATA_DIR: Path = Path(os.getenv("DATA_DIR", Path.cwd() / "data"))
