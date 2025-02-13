from pydantic_settings import SettingsConfigDict

from .base import CustomBaseSettings


class APISettings(CustomBaseSettings):
    compress: bool = True
    compress_level: int = 1

    encrypt: bool = True

    model_config = SettingsConfigDict(env_prefix="api_")
