from typing import Optional

from ......base import BaseModel
from ......utils import FriendshipModel
from ......utils import OtherOwnerModel


class FriendshipFriendIdDeleteResponseModel(BaseModel):
    friendship_list: list[FriendshipModel]
    owner_list: Optional[list[OtherOwnerModel]] = None
