from functools import cache
from http import HTTPStatus
from typing import ClassVar

from fastapi import Request
from fastapi.responses import ORJSONResponse

from naagin.utils import CustomHeader


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
    def handler(cls, _: Request | None = None, exception: Exception | None = None) -> ORJSONResponse:
        if isinstance(exception, ExceptionBase):
            return exception.handler()

        response = ORJSONResponse(*cls.get_args())
        CustomHeader.set(response, "Status", cls.code)
        return response
