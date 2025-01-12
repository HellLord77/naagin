import os
from pathlib import Path

SERVER_URL: str = os.getenv("SERVER_URL", "http://localhost:8000")

DATA_DIR: Path = Path(os.getenv("DATA_DIR", Path(__file__).parent / "data"))
