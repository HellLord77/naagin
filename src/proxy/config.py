import os

SERVER_HOST: str = os.getenv("SERVER_HOST", "localhost")
SERVER_PORT: int = int(os.getenv("SERVER_PORT", 8000))

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
