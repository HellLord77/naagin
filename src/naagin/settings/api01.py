from pydantic_settings import SettingsConfigDict

from .base import BaseSettings


class API01Settings(BaseSettings):
    no_proxy: bool = True

    base_url: str = "https://api01.doaxvv.com"

    model_config = SettingsConfigDict(env_prefix="api01_")
