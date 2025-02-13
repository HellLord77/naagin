from functools import cached_property

from httpx import AsyncClient
from pydantic_settings import SettingsConfigDict

from .base import CustomBaseSettings


class GameSettings(CustomBaseSettings):
    offline_mode: bool = False
    no_proxy: bool = True

    base_url: str = "https://game.doaxvv.com"

    model_config = SettingsConfigDict(env_prefix="game_")

    @cached_property
    def client(self) -> AsyncClient:
        return AsyncClient(base_url=self.base_url, trust_env=not self.no_proxy)
