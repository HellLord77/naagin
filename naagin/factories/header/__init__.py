from functools import lru_cache

from naagin import settings
from naagin.enums import MasterVersionEnum

from .utils import get_resource_list


@lru_cache
def application_version_factory() -> int:
    application_version = settings.version.application
    if application_version is None:
        resource_list = get_resource_list()
        application_version = resource_list.resource_list.exe[0].version

    return application_version


def master_version_factory() -> MasterVersionEnum:
    return settings.version.master


@lru_cache
def resource_version_factory() -> str:
    resource_version = settings.version.resource
    if resource_version is None:
        resource_list = get_resource_list()
        resource_version = (
            resource_list.resource_list.common[-1].version,  # ?
            resource_list.resource_list.low[-1].version,
            resource_list.resource_list.high[-1].version,  # ?
        )

    return ",".join(map(str, resource_version))
