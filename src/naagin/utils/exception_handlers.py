from http import HTTPStatus

from fastapi import HTTPException
from fastapi import Request
from fastapi import Response
from fastapi.responses import JSONResponse

from naagin import apps
from naagin.exceptions import NotFoundException


async def moved_permanently_handler(_: Request, __: HTTPException) -> JSONResponse:
    return JSONResponse(
        {"code": HTTPStatus.MOVED_PERMANENTLY, "message": "cache exception"},
        HTTPStatus.MOVED_PERMANENTLY,
    )


async def not_found_handler(request: Request, exception: HTTPException) -> Response:
    if request.url.path.startswith("/game"):
        return await apps.game.not_found_handler(request, exception)
    else:
        return NotFoundException.handler()
