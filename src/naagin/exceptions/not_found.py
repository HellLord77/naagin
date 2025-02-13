from http import HTTPStatus

from naagin.bases import ExceptionBase


class NotFoundException(ExceptionBase):
    code = HTTPStatus.NOT_FOUND
    message = "not found"
