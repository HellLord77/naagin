from naagin.models.base import BaseModel
from naagin.models.common import FriendshipModel
from naagin.models.common import OtherOwnerModel


class FriendshipPostResponseModel(BaseModel):
    friendship_list: list[FriendshipModel]
    owner_list: list[OtherOwnerModel]
