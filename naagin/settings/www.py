from functools import cached_property

from httpx import AsyncClient
from pydantic import AnyHttpUrl
from pydantic_settings import SettingsConfigDict

from naagin.bases import SettingsBase


class WWWSettings(SettingsBase):
    offline_mode: bool = False

    base_url: AnyHttpUrl = "https://doax-venusvacation.jp"
    user_agent: str = "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko"

    model_config = SettingsConfigDict(env_prefix="www_")

    @cached_property
    def client(self) -> AsyncClient:
        return AsyncClient(headers={"User-Agent": self.user_agent}, base_url=str(self.base_url))
