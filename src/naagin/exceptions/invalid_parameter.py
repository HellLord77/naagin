from .base import CustomBaseException


class InvalidParameterException(CustomBaseException):
    code = 1
    message = "invalid parameter(s)"
