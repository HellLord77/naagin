from naagin import loggers
from naagin import settings
from naagin.utils import CachedResource

app = CachedResource(
    directory=settings.data.www_dir, client=settings.www.client, logger=loggers.www, offline=settings.www.offline_mode
)
