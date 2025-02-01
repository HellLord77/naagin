from typing import Optional

from pydantic import FilePath
from pydantic_settings import SettingsConfigDict

from .base import BaseSettings


class EnvironmentSettings(BaseSettings):
    file: Optional[FilePath] = None

    model_config = SettingsConfigDict(env_prefix="env_")
