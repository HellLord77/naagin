import os
from pathlib import Path

EXAMPLES: bool = os.getenv("EXAMPLES", "false").lower() == "true"

MASTER_VERSION: int = int(os.getenv("MASTER_VERSION", "10"))
MASTER_VERSION_JP: int = int(os.getenv("MASTER_VERSION_JP", "19"))
APPLICATION_VERSION: int = int(os.getenv("APPLICATION_VERSION", "73200"))
APPLICATION_VERSION_JP: int = int(os.getenv("APPLICATION_VERSION_JP", "85100"))

DATA_DIR: Path = Path(os.getenv("DATA_DIR", Path.cwd() / "data"))
