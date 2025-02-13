from http import HTTPStatus

from naagin.bases import ExceptionBase


class MethodNotAllowedException(ExceptionBase):
    code = HTTPStatus.METHOD_NOT_ALLOWED
    message = "method not allowed"
