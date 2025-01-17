from ......base import BaseModel
from ......utils import FriendshipModel
from ......utils import OtherOwnerModel


class FriendshipAcceptPostResponseModel(BaseModel):
    friendship_list: list[FriendshipModel]
    owner_list: list[OtherOwnerModel]
