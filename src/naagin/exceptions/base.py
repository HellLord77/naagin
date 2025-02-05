from functools import cache
from http import HTTPStatus
from typing import ClassVar
from typing import Optional

from fastapi import Request
from fastapi.responses import JSONResponse

from naagin.models.common import ExceptionModel
from naagin.utils import DOAXVVHeader


class BaseException(Exception):
    code: ClassVar[int]
    message: ClassVar[str]

    @classmethod
    @cache
    def get_args(cls) -> tuple[dict[str, int | str], int]:
        self = cls()
        content = ExceptionModel.model_validate(self).model_dump()
        status_code = HTTPStatus.OK
        if cls.code in HTTPStatus:
            status_code = cls.code
        return content, status_code

    @classmethod
    def handler(
        cls, _: Optional[Request] = None, exception: Optional[Exception] = None
    ) -> JSONResponse:
        if isinstance(exception, BaseException):
            return cls.handler()
        else:
            response = JSONResponse(*cls.get_args())
            DOAXVVHeader.set(response, "Status", cls.code)
            return response
