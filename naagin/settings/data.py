from functools import cached_property
from pathlib import Path  # noqa: TID251
from tempfile import gettempdir

from anyio import Path as AsyncPath
from pydantic import DirectoryPath

from naagin.bases import SettingsBase


class DataSettings(SettingsBase):
    temp: bool = True

    dir: DirectoryPath = Path.cwd() / "data"

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
    def www_dir(self) -> AsyncPath:
        return self.directory / "www"

    @cached_property
    def csv_dir(self) -> AsyncPath:
        return self.directory / "csv"
