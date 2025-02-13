from http import HTTPStatus

from .base import CustomBaseException


class NotFoundException(CustomBaseException):
    code = HTTPStatus.NOT_FOUND
    message = "not found"
