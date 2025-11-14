from functools import cached_property

from pydantic_settings import SettingsConfigDict

from naagin.bases import SettingsBase


class VersionSettings(SettingsBase):
    master: int = 10
    application: int = 73200

    model_config = SettingsConfigDict(env_prefix="ver_")

    @cached_property
    def resource(self) -> str:
        return ",".join(map(str, (self.application,) * 3))
