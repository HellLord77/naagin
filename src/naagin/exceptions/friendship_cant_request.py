from .base import CustomBaseException


class FriendshipCantRequestException(CustomBaseException):
    code = 804
    message = "friendship can't request"
