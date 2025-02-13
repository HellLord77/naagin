from http import HTTPStatus

from naagin.bases import ExceptionBase


class InternalServerErrorException(ExceptionBase):
    code = HTTPStatus.INTERNAL_SERVER_ERROR
    message = "internal server error"
