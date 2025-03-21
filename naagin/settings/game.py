from functools import cached_property

from httpx import AsyncClient
from pydantic import AnyHttpUrl
from pydantic_settings import SettingsConfigDict

from naagin.bases import SettingsBase


class GameSettings(SettingsBase):
    offline_mode: bool = False

    base_url: AnyHttpUrl = "https://game.doaxvv.com"

    model_config = SettingsConfigDict(env_prefix="game_")

    @cached_property
    def client(self) -> AsyncClient:
        return AsyncClient(base_url=str(self.base_url))
