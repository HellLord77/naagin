from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class NaaginBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="ngn_")  # TODO
