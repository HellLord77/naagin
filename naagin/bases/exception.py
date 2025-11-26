from functools import cache
from http import HTTPStatus
from typing import ClassVar

from fastapi import Request

from naagin import loggers
from naagin import settings
from naagin.enums import DOAXVVHeaderEnum
from naagin.enums import NaaginHeaderEnum
from naagin.imports import JSONResponse
from naagin.utils import DOAXVVHeader


class ExceptionBase(Exception):  # noqa: N818
    code: ClassVar[int]
    message: ClassVar[str]

    status_code: ClassVar[HTTPStatus] = HTTPStatus.INTERNAL_SERVER_ERROR

    def __init_subclass__(cls) -> None:
        if cls.code in HTTPStatus:
            cls.status_code = HTTPStatus(cls.code)

    @classmethod
    @cache
    def get_args(cls) -> tuple[dict[str, int | str], HTTPStatus]:
        from naagin.models import ExceptionModel  # noqa: PLC0415

        self = cls()
        content = ExceptionModel.model_validate(self).model_dump()
        status_code = cls.status_code
        return content, status_code

    @classmethod
    def handler(cls, _: Request | None = None, exception: Exception | None = None) -> JSONResponse:
        if isinstance(exception, ExceptionBase):
            return exception.handler()

        response = JSONResponse(*cls.get_args())
        if exception is not None:
            exception_type = type(exception).__name__
            exception_message = str(exception)
            loggers.app.debug("%s: %s", exception_type, exception_message)
            if settings.app.debug_headers:
                response.headers[NaaginHeaderEnum.EXCEPTION_TYPE] = exception_type
                response.headers[NaaginHeaderEnum.EXCEPTION_MESSAGE] = exception_message
        response.headers[DOAXVVHeader(DOAXVVHeaderEnum.STATUS)] = str(cls.code)
        return response
