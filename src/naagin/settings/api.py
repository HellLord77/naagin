from pydantic_settings import SettingsConfigDict

from naagin.bases import SettingsBase


class APISettings(SettingsBase):
    compress: bool = True
    compress_level: int = 1

    encrypt: bool = True

    model_config = SettingsConfigDict(env_prefix="api_")
