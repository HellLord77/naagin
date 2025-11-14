from naagin import loggers
from naagin import settings
from naagin.utils import CachedStaticFiles

app = CachedStaticFiles(
    directory=settings.data.game_dir,
    client=settings.game.client,
    logger=loggers.game,
    offline=settings.game.offline_mode,
)
