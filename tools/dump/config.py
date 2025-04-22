import os
from pathlib import Path

EXAMPLES: bool = os.getenv("EXAMPLES", "false").lower() == "true"

VERSION: int = int(os.getenv("VERSION", "10"))
APP_VERSION: int = int(os.getenv("APP_VERSION", "70300"))

DATA_DIR: Path = Path(os.getenv("DATA_DIR", Path.cwd() / "data"))

FLOW: bool = os.getenv("FLOW", "false").lower() == "true"
CSV: bool = os.getenv("CSV", "false").lower() == "true"
GAME: bool = os.getenv("GAME", "false").lower() == "true"
