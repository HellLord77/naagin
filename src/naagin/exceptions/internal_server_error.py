from http import HTTPStatus

from .base import BaseException


class InternalServerErrorException(BaseException):
    code = HTTPStatus.INTERNAL_SERVER_ERROR
    message = "internal server error"
