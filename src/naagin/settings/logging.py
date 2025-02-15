from functools import cached_property
from logging import Logger
from logging import getLogger

from pydantic import PositiveInt
from pydantic_settings import SettingsConfigDict

from naagin.bases import SettingsBase
from naagin.enums import LoggingLevelEnum


class LoggingSettings(SettingsBase):
    level: LoggingLevelEnum = LoggingLevelEnum.NOTSET

    duplicate_model: bool = False
    duplicate_model_length: PositiveInt = 3

    model_config = SettingsConfigDict(env_prefix="log_")

    @cached_property
    def logger(self) -> Logger:
        return getLogger("naagin")
