from fastapi import Request

from naagin.exceptions.base import BaseException
from . import request
from . import response


async def handle_base_exception(request: Request, call_next):
    try:
        response = await call_next(request)
    except BaseException as exception:
        return exception.handler()
    else:
        return response
