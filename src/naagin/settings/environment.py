from pydantic import FilePath
from pydantic_settings import SettingsConfigDict

from .base import BaseSettings


class EnvironmentSettings(BaseSettings):
    file: FilePath | None = None

    model_config = SettingsConfigDict(env_prefix="env_")
