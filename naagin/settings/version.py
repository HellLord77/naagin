from naagin.bases import SettingsBase
from naagin.enums import MasterVersionEnum


class VersionSettings(SettingsBase):
    master: MasterVersionEnum = MasterVersionEnum.GLOBAL
    application: int = 73400
    resource: tuple[int, int, int] = 73400, 73400, 73400

    strict: bool = True
