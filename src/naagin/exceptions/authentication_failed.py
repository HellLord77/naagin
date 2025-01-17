from .base import BaseException


class AuthenticationFailedException(BaseException):
    code = 11
    message = "authentication failed"
