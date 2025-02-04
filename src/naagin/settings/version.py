from functools import cached_property

from pydantic_settings import SettingsConfigDict

from .base import BaseSettings


class VersionSettings(BaseSettings):
    master: int = 10
    application: int = 64500

    model_config = SettingsConfigDict(env_prefix="ver_")

    @cached_property
    def resource(self) -> str:
        return ",".join(map(str, (self.application,) * 3))
