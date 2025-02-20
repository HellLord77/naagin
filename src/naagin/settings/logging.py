from pydantic import PositiveInt
from pydantic_settings import SettingsConfigDict

from naagin.bases import SettingsBase
from naagin.enums import LoggingLevelEnum


class LoggingSettings(SettingsBase):
    level: LoggingLevelEnum = LoggingLevelEnum.NOTSET

    model: bool = False
    model_dup_len: PositiveInt = 3

    model_config = SettingsConfigDict(env_prefix="log_")
