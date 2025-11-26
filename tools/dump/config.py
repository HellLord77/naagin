import os
from pathlib import Path

EXAMPLES: bool = os.getenv("EXAMPLES", "false").lower() == "true"

APPLICATION_VERSION: int = int(os.getenv("APPLICATION_VERSION", "73400"))
APPLICATION_VERSION_JP: int = int(os.getenv("APPLICATION_VERSION_JP", "90000"))

DATA_DIR: Path = Path(os.getenv("DATA_DIR", Path.cwd() / "data"))
