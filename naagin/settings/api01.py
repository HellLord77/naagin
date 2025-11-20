from functools import cached_property

from httpx import AsyncClient
from pydantic import AnyHttpUrl

from naagin.bases import SettingsBase


class API01Settings(SettingsBase):
    base_url: AnyHttpUrl = "https://api01.doaxvv.com"

    user_agent: str = "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko"

    @cached_property
    def client(self) -> AsyncClient:
        return AsyncClient(headers={"User-Agent": self.user_agent}, base_url=str(self.base_url))
