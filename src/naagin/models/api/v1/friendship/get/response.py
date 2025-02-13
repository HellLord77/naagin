from naagin.models.base import CustomBaseModel
from naagin.models.common import FriendshipModel


class FriendshipGetResponseModel(CustomBaseModel):
    friendship_list: list[FriendshipModel]
