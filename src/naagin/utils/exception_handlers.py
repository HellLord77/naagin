from fastapi import Request
from fastapi import Response

from naagin import apps
from naagin.exceptions import NotFoundException


async def not_found_handler(request: Request, exception: Exception) -> Response:
    if request.url.path.startswith("/game"):
        return await apps.game.not_found_handler(request, exception)
    else:
        return NotFoundException.handler()
