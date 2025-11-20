from naagin.bases import SettingsBase
from naagin.enums import MasterVersionEnum


class VersionSettings(SettingsBase):
    master: MasterVersionEnum = MasterVersionEnum.GLOBAL
    application: int = 73300
    resource: tuple[int, int, int] = 73300, 73300, 73300

    strict: bool = True
