from pydantic import FilePath

from naagin.bases import SettingsBase


class EnvironmentSettings(SettingsBase):
    file: FilePath | None = None
