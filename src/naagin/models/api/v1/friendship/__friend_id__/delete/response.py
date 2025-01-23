from typing import Optional

from naagin.models.base import BaseModel
from naagin.models.common import FriendshipModel
from naagin.models.common import OtherOwnerModel


class FriendshipFriendIdDeleteResponseModel(BaseModel):
    friendship_list: list[FriendshipModel]
    owner_list: Optional[list[OtherOwnerModel]] = None
