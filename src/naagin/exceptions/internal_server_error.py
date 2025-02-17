from http import HTTPStatus
from typing import override

from fastapi import Request
from fastapi.responses import ORJSONResponse

from naagin import settings
from naagin.bases import ExceptionBase

logger = settings.logging.logger


class InternalServerErrorException(ExceptionBase):
    code = HTTPStatus.INTERNAL_SERVER_ERROR
    message = "internal server error"

    @classmethod
    @override
    def handler(cls, reqeust: Request | None = None, exception: Exception | None = None) -> ORJSONResponse:
        logger.exception("Internal server error", exc_info=exception)
        return super().handler(reqeust, exception)
