from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class BaseSettings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore")
