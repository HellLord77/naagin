from naagin.bases import ExceptionBase


class AuthenticationFailedException(ExceptionBase):
    code = 11
    message = "authentication failed"
