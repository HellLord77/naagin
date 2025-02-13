from pydantic import FilePath
from pydantic_settings import SettingsConfigDict

from .base import CustomBaseSettings


class EnvironmentSettings(CustomBaseSettings):
    file: FilePath | None = None

    model_config = SettingsConfigDict(env_prefix="env_")
