import os
from pathlib import Path

NO_PROXY: bool = bool(os.getenv("NO_PROXY", "true").lower() == "true")

DATA_DIR: Path = Path(os.getenv("DATA_DIR", Path(__file__).parent / "data"))
