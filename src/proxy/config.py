import os
from pathlib import Path

SERVER_HOST: str = os.getenv("SERVER_HOST", "localhost")
SERVER_PORT: int = int(os.getenv("SERVER_PORT", 8000))

DATA_DIR: Path = Path(os.getenv("DATA_DIR", Path(__file__).parent / "data"))
