import os
from pathlib import Path

SERVER_URL: str = os.getenv("SERVER_URL", "http://localhost:8000")
DATA_DIR: Path = Path(os.getenv("DATA_DIR", Path.cwd() / "data"))

WRITE_FILE: bool = os.getenv("WRITE_FILE", "false").lower() == "true"
WRITE_CONSOLE: bool = os.getenv("WRITE_CONSOLE", "false").lower() == "true"

REAPI: bool = not WRITE_FILE
REAPI01: bool = not WRITE_FILE
REGAME: bool = True
RECDN01: bool = True
RENONCE: bool = False
