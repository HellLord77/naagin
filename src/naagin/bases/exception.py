from functools import cache
from http import HTTPStatus
from typing import ClassVar

from fastapi import Request
from fastapi.responses import ORJSONResponse

from naagin.utils import DOAXVVHeader
from naagin.utils import SingletonMeta


class ExceptionBase(Exception, metaclass=SingletonMeta):  # noqa: N818
    code: ClassVar[int]
    message: ClassVar[str]

    @classmethod
    @cache
    def get_args(cls) -> tuple[dict[str, int | str], int]:
        from naagin.models.common import ExceptionModel  # noqa: PLC0415

        self = cls()
        content = ExceptionModel.model_validate(self).model_dump()
        status_code = cls.code if cls.code in HTTPStatus else HTTPStatus.OK
        return content, status_code

    @classmethod
    def handler(cls, _: Request | None = None, exception: Exception | None = None) -> ORJSONResponse:
        if isinstance(exception, ExceptionBase):
            return exception.handler()

        response = ORJSONResponse(*cls.get_args())
        DOAXVVHeader.set(response, "Status", cls.code)
        return response
