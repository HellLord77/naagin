from http import HTTPStatus

from .base import BaseException


class MethodNotAllowedException(BaseException):
    code = HTTPStatus.METHOD_NOT_ALLOWED
    message = "method not allowed"
