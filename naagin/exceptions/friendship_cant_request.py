from http import HTTPStatus

from naagin.bases import ExceptionBase


class FriendshipCantRequestException(ExceptionBase):
    code = 804
    message = "friendship can't request"
    status_code = HTTPStatus.FORBIDDEN
