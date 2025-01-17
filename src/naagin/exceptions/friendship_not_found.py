from .base import BaseException


class FriendshipNotFoundException(BaseException):
    code = 802
    message = "friendship not found"
