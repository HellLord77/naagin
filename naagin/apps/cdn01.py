from naagin import loggers
from naagin import settings
from naagin.utils import CachedStaticFiles

app = CachedStaticFiles(
    directory=settings.data.cdn01_dir,
    client=settings.cdn01.client,
    logger=loggers.cdn01,
    offline=settings.cdn01.offline_mode,
)
