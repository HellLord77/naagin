from fastapi import Request

from naagin.exceptions.base import BaseException
from naagin.utils.exception_handlers import base_exception_handler


async def handle_base_exception(request: Request, call_next):
    try:
        response = await call_next(request)
    except BaseException as exception:
        return await base_exception_handler(request, exception)
    else:
        return response
