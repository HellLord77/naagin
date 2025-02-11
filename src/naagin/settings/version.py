from functools import cached_property
from typing import Literal

from pydantic_settings import SettingsConfigDict

from .base import BaseSettings


class VersionSettings(BaseSettings):
    master: Literal[10] = 10
    application: int = 64500

    model_config = SettingsConfigDict(env_prefix="ver_")

    @cached_property
    def resource(self) -> str:
        return ",".join(map(str, (self.application,) * 3))
