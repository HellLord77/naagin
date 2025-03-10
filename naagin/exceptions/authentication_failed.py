from http import HTTPStatus

from naagin.bases import ExceptionBase


class AuthenticationFailedException(ExceptionBase):
    code = 11
    message = "authentication failed"
    status_code = HTTPStatus.UNAUTHORIZED
