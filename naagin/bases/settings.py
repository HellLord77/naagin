from pydantic_settings import BaseSettings  # noqa: TID251
from pydantic_settings import SettingsConfigDict


class SettingsBase(BaseSettings):
    model_config = SettingsConfigDict(
        extra="ignore",  # deprecated
        frozen=True,
        env_parse_none_str="null",
    )
