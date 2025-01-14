from functools import cached_property
from pathlib import Path

from aiopath import AsyncPath
from pydantic import DirectoryPath
from pydantic_settings import SettingsConfigDict

from .. import NaaginBaseSettings


class DataSettings(NaaginBaseSettings):
    data_dir: DirectoryPath = Path.cwd() / "data"

    model_config = SettingsConfigDict(env_prefix="")  # TODO

    @cached_property
    def api_dir(self) -> AsyncPath:
        return AsyncPath(self.data_dir / "api")

    @cached_property
    def api01_dir(self) -> AsyncPath:
        return AsyncPath(self.data_dir / "api01")

    @cached_property
    def game_dir(self) -> AsyncPath:
        return AsyncPath(self.data_dir / "game")
