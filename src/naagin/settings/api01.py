from pydantic_settings import SettingsConfigDict

from .base import BaseSettings


class API01Settings(BaseSettings):
    game_version: int = 64200

    model_config = SettingsConfigDict(env_prefix="api01_")
