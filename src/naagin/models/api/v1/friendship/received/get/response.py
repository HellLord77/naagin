from naagin.models.base import CustomBaseModel
from naagin.models.common import FriendshipModel


class FriendshipReceivedGetResponseModel(CustomBaseModel):
    friendship_list: list[FriendshipModel]
