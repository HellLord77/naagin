from typing import Self
from typing import override

from pydantic_settings import BaseSettings  # noqa: TID251
from pydantic_settings import DotEnvSettingsSource
from pydantic_settings import EnvSettingsSource
from pydantic_settings import PydanticBaseSettingsSource
from pydantic_settings import SecretsSettingsSource
from pydantic_settings import SettingsConfigDict


class SettingsBase(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore", frozen=True, env_parse_none_str="null")

    @override
    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[Self],
        init_settings: PydanticBaseSettingsSource,
        env_settings: EnvSettingsSource,
        dotenv_settings: DotEnvSettingsSource,
        file_secret_settings: SecretsSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        for key in tuple(env_settings.env_vars):
            if not key.startswith(env_settings.env_prefix):
                del env_settings.env_vars[key]
        for key in tuple(dotenv_settings.env_vars):
            if not key.startswith(dotenv_settings.env_prefix):
                del dotenv_settings.env_vars[key]

        return super().settings_customise_sources(
            settings_cls, init_settings, env_settings, dotenv_settings, file_secret_settings
        )
