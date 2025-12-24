import os
from pathlib import Path

EXAMPLES: bool = os.getenv("EXAMPLES", "false").lower() == "true"

APPLICATION_VERSION: int = int(os.getenv("APPLICATION_VERSION", "74000"))
APPLICATION_VERSION_JP: int = int(os.getenv("APPLICATION_VERSION_JP", "90400"))

DATA_DIR: Path = Path(os.getenv("DATA_DIR", Path.cwd() / "data"))
