from pydantic_settings import SettingsConfigDict

from .base import NaaginBaseSettings


class API01Settings(NaaginBaseSettings):
    game_version: int = 64100

    model_config = SettingsConfigDict(env_prefix="api01_")
