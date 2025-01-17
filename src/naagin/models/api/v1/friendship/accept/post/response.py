from naagin.models.base import BaseModel
from naagin.models.utils import FriendshipModel
from naagin.models.utils import OtherOwnerModel


class FriendshipAcceptPostResponseModel(BaseModel):
    friendship_list: list[FriendshipModel]
    owner_list: list[OtherOwnerModel]
