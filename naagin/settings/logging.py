from pydantic import PositiveInt

from naagin.bases import SettingsBase
from naagin.enums import LoggingLevelEnum


class LoggingSettings(SettingsBase):
    level: LoggingLevelEnum = LoggingLevelEnum.NOTSET

    model: bool = False
    model_duplicate_length: PositiveInt = 3

    route: bool = False
