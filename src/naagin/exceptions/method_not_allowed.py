from http import HTTPStatus

from .base import CustomBaseException


class MethodNotAllowedException(CustomBaseException):
    code = HTTPStatus.METHOD_NOT_ALLOWED
    message = "method not allowed"
