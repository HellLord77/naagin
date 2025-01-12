import os
from aiopath import AsyncPath

NO_PROXY: bool = bool(os.getenv("NO_PROXY", "true").lower() == "true")

DATA_DIR: AsyncPath = AsyncPath(os.getenv("DATA_DIR", AsyncPath(__file__).parent / "data"))
