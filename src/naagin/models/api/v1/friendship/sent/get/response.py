from naagin.models.base import CustomBaseModel
from naagin.models.common import FriendshipModel


class FriendshipSentGetResponseModel(CustomBaseModel):
    friendship_list: list[FriendshipModel]
