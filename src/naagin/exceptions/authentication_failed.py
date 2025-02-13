from .base import CustomBaseException


class AuthenticationFailedException(CustomBaseException):
    code = 11
    message = "authentication failed"
