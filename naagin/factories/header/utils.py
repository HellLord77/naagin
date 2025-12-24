from functools import lru_cache

from anyio.from_thread import start_blocking_portal

from naagin import settings
from naagin.models.json import ResourceFileListModel


@lru_cache
def get_resource_list() -> ResourceFileListModel:
    if settings.version.japan:
        from naagin.providers.json import provide_resource_list_encrypt as provide_resource_list  # noqa: PLC0415
    else:
        from naagin.providers.json import provide_resource_list  # noqa: PLC0415

    with start_blocking_portal() as portal:
        return portal.call(provide_resource_list)
