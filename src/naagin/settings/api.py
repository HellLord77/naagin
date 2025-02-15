from pydantic import Field
from pydantic_settings import SettingsConfigDict

from naagin.bases import SettingsBase


class APISettings(SettingsBase):
    compress: bool = True
    compress_level: int = Field(1, ge=-1, le=9)

    encrypt: bool = True

    model_config = SettingsConfigDict(env_prefix="api_")
