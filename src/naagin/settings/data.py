from functools import cached_property
from pathlib import Path

from aiopath import AsyncPath
from pydantic import DirectoryPath
from pydantic_settings import SettingsConfigDict

from naagin.bases import SettingsBase


class DataSettings(SettingsBase):
    dir: DirectoryPath = Path.cwd() / "data"

    model_config = SettingsConfigDict(env_prefix="data_")

    @cached_property
    def api_dir(self) -> AsyncPath:
        return AsyncPath(self.dir / "api")

    @cached_property
    def api01_dir(self) -> AsyncPath:
        return AsyncPath(self.dir / "api01")

    @cached_property
    def game_dir(self) -> AsyncPath:
        return AsyncPath(self.dir / "game")

    @cached_property
    def csv_dir(self) -> AsyncPath:
        return AsyncPath(self.dir / "csv")
