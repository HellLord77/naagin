from fastapi import Request

from naagin.exceptions.base import BaseException
from naagin.utils.exception_handlers import base_exception_handler
from . import request
from . import response


async def exception_handler(request: Request, call_next):
    try:
        response = await call_next(request)
    except BaseException as exception:
        return await base_exception_handler(request, exception)
    else:
        return response
