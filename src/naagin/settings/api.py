from pydantic_settings import SettingsConfigDict

from .base import BaseSettings


class APISettings(BaseSettings):
    compress: bool = True
    encrypt: bool = True

    compress_level: int = 1

    model_config = SettingsConfigDict(env_prefix="api_")
