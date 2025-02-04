from functools import cache
from http import HTTPStatus
from typing import ClassVar
from typing import Optional

from fastapi import Request
from fastapi.responses import JSONResponse

from naagin.models.common import ExceptionModel
from naagin.utils import DOAXVVHeader


class BaseException(Exception, metaclass=type("", (type,), {})):
    code: ClassVar[int]
    message: ClassVar[str]

    def __init__(self):
        raise NotImplementedError

    @classmethod
    @cache
    def get_args(cls) -> tuple[dict[str, int | str], int]:
        content = ExceptionModel.model_validate(cls).model_dump()
        status_code = HTTPStatus.OK
        if cls.code in HTTPStatus:
            status_code = cls.code
        return content, status_code

    @classmethod
    def handle(cls, _: Optional[Request] = None, __: Optional[Exception] = None) -> JSONResponse:
        response = JSONResponse(*cls.get_args())
        DOAXVVHeader.set(response, "Status", cls.code)
        return response
