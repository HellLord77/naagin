from pydantic_settings import BaseSettings  # noqa: TID251
from pydantic_settings import SettingsConfigDict


class CustomBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(frozen=True, extra="ignore")
