from functools import cached_property
from pathlib import Path  # noqa: TID251
from tempfile import gettempdir

from aiopath import AsyncPath
from pydantic import DirectoryPath
from pydantic_settings import SettingsConfigDict

from naagin.bases import SettingsBase


class DataSettings(SettingsBase):
    temp: bool = True

    dir: DirectoryPath = Path.cwd() / "data"

    model_config = SettingsConfigDict(env_prefix="data_")

    @cached_property
    def directory(self) -> AsyncPath:
        return AsyncPath(self.dir.resolve())

    @cached_property
    def temp_dir(self) -> AsyncPath:
        return (self.directory / "temp") if self.temp else AsyncPath(gettempdir())

    @cached_property
    def api_dir(self) -> AsyncPath:
        return self.directory / "api"

    @cached_property
    def api01_dir(self) -> AsyncPath:
        return self.directory / "api01"

    @cached_property
    def game_dir(self) -> AsyncPath:
        return self.directory / "game"

    @cached_property
    def cdn01_dir(self) -> AsyncPath:
        return self.directory / "cdn01"

    @cached_property
    def csv_dir(self) -> AsyncPath:
        return self.directory / "csv"
