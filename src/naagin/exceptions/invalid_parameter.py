from .base import BaseException


class InvalidParameterException(BaseException):
    code = 1
    message = "invalid parameter(s)"
