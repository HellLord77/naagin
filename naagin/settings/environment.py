from pydantic import FilePath
from pydantic_settings import SettingsConfigDict

from naagin.bases import SettingsBase


class EnvironmentSettings(SettingsBase):
    file: FilePath | None = None

    model_config = SettingsConfigDict(env_prefix="env_")
