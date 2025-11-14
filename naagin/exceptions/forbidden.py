from http import HTTPStatus

from naagin.bases import ExceptionBase


class ForbiddenException(ExceptionBase):
    code = HTTPStatus.FORBIDDEN
    message = "forbidden"
