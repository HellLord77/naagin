from http import HTTPStatus

from .base import CustomBaseException


class InternalServerErrorException(CustomBaseException):
    code = HTTPStatus.INTERNAL_SERVER_ERROR
    message = "internal server error"
