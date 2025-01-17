from .base import BaseException


class FriendshipCantRequestException(BaseException):
    code = 804
    message = "friendship can't request"
