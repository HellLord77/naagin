from functools import cached_property

from httpx import AsyncClient
from pydantic import AnyHttpUrl
from pydantic_settings import SettingsConfigDict

from naagin.bases import SettingsBase


class API01Settings(SettingsBase):
    no_proxy: bool = True

    base_url: AnyHttpUrl = "https://api01.doaxvv.com"

    model_config = SettingsConfigDict(env_prefix="api01_")

    @cached_property
    def client(self) -> AsyncClient:
        return AsyncClient(base_url=str(self.base_url), trust_env=not self.no_proxy)
