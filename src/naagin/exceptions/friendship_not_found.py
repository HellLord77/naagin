from naagin.bases import ExceptionBase


class FriendshipNotFoundException(ExceptionBase):
    code = 802
    message = "friendship not found"
