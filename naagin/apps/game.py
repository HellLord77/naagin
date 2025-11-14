from functools import partial

from naagin import loggers
from naagin import settings
from naagin.classes import StaticFiles

from .utils import not_found_handler

kwargs = {}
if not settings.game.offline_mode:
    kwargs["not_found_handler"] = partial(
        not_found_handler, directory=settings.data.game_dir, client=settings.game.client, logger=loggers.game
    )

app = StaticFiles(directory=settings.data.game_dir, html=True, **kwargs)
