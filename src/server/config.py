import os
from pathlib import Path

DATA_DIR: Path = Path(os.getenv("DATA_DIR", Path(__file__).parent / "data"))
