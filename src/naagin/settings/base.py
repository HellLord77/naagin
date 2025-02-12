from pydantic_settings import BaseSettings  # noqa: TID251
from pydantic_settings import SettingsConfigDict


class BaseSettings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore")
