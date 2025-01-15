from pydantic_settings import SettingsConfigDict

from .base import NaaginBaseSettings


class GameSettings(NaaginBaseSettings):
    offline_mode: bool = False
    no_proxy: bool = True

    base_url: str = "https://game.doaxvv.com"

    model_config = SettingsConfigDict(env_prefix="game_")
