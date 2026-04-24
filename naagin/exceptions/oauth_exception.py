from http import HTTPStatus

from naagin.bases import ExceptionBase


class OAuthExceptionException(ExceptionBase):
    code = 13
    message = "OAuth exception"
    status_code = HTTPStatus.OK
