from http import HTTPStatus

from naagin.bases import ExceptionBase


class InvalidParameterException(ExceptionBase):
    code = 1
    message = "invalid parameter(s)"
    status_code = HTTPStatus.BAD_REQUEST
