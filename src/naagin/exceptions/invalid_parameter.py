from naagin.bases import ExceptionBase


class InvalidParameterException(ExceptionBase):
    code = 1
    message = "invalid parameter(s)"
