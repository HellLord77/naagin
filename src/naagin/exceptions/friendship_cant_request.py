from naagin.bases import ExceptionBase


class FriendshipCantRequestException(ExceptionBase):
    code = 804
    message = "friendship can't request"
