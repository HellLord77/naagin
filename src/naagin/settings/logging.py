from functools import cached_property
from logging import Logger
from logging import getLogger

from pydantic_settings import SettingsConfigDict

from naagin.enums import LoggingLevelEnum

from .base import CustomBaseSettings


class LoggingSettings(CustomBaseSettings):
    level: LoggingLevelEnum = LoggingLevelEnum.NOTSET

    duplicate_model: bool = False
    duplicate_model_length: int = 3

    model_config = SettingsConfigDict(env_prefix="log_")

    @cached_property
    def logger(self) -> Logger:
        return getLogger("naagin")
