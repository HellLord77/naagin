from naagin import settings
from naagin.enums import MasterVersionEnum


def application_version_factory() -> int:
    return settings.version.application


def master_version_factory() -> MasterVersionEnum:
    return settings.version.master


def resource_version_factory() -> str:
    return settings.version.resource
