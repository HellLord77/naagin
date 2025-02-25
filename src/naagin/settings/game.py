from functools import cached_property

from httpx import AsyncClient
from pydantic import AnyHttpUrl
from pydantic_settings import SettingsConfigDict

from naagin.bases import SettingsBase


class GameSettings(SettingsBase):
    list_dir: bool = False
    offline_mode: bool = False
    no_proxy: bool = True

    base_url: AnyHttpUrl = "https://game.doaxvv.com"
    user_agent: str | None = "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko"

    model_config = SettingsConfigDict(env_prefix="game_")

    @cached_property
    def client(self) -> AsyncClient:
        return AsyncClient(base_url=str(self.base_url), trust_env=not self.no_proxy)
