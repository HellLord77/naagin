from http import HTTPStatus

from .base import BaseException


class NotFoundException(BaseException):
    code = HTTPStatus.NOT_FOUND
    message = "not found"
