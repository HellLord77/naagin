from pydantic import NonNegativeInt
from pydantic_settings import SettingsConfigDict

from naagin.bases import SettingsBase


class FastAPISettings(SettingsBase):
    swagger: bool = False
    reqeust_max_size: NonNegativeInt | None = 1_000_000

    model_config = SettingsConfigDict(env_prefix="app_")
