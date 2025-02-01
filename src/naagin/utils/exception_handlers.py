from http import HTTPStatus

from fastapi import HTTPException
from fastapi import Request
from fastapi import Response
from fastapi.responses import JSONResponse

from naagin import apps
from naagin.exceptions import InternalServerErrorException
from naagin.exceptions import InvalidParameterException
from naagin.exceptions import MethodNotAllowedException
from naagin.exceptions import NotFoundException
from naagin.exceptions.base import BaseException
from naagin.models.common import ExceptionModel
from . import DOAXVVHeader


async def moved_permanently_handler(_: Request, __: HTTPException) -> JSONResponse:
    return JSONResponse(
        {"code": HTTPStatus.MOVED_PERMANENTLY, "message": "cache exception"},
        HTTPStatus.MOVED_PERMANENTLY,
    )


async def not_found_handler(request: Request, _: HTTPException) -> Response:
    if request.url.path.startswith("/game"):
        return await apps.game.not_found_handler(request, _)
    else:
        return await base_exception_handler(request, NotFoundException())


async def method_not_allowed_handler(
    request: Request, _: HTTPException
) -> JSONResponse:
    return await base_exception_handler(request, MethodNotAllowedException())


async def unprocessable_content_handler(
    request: Request, _: HTTPException
) -> JSONResponse:
    return await base_exception_handler(request, InvalidParameterException())


async def internal_server_error_handler(
    request: Request, _: HTTPException
) -> JSONResponse:
    return await base_exception_handler(request, InternalServerErrorException())


async def base_exception_handler(_: Request, exception: BaseException) -> JSONResponse:
    response = JSONResponse(
        ExceptionModel.model_validate(exception).model_dump(),
        exception.code if exception.code in HTTPStatus else HTTPStatus.OK,
    )
    DOAXVVHeader.set(response, "Status", exception.code)
    return response
