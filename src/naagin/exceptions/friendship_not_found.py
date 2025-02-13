from .base import CustomBaseException


class FriendshipNotFoundException(CustomBaseException):
    code = 802
    message = "friendship not found"
