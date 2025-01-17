from typing import Optional

from naagin.models.base import BaseModel
from naagin.models.utils import FriendshipModel
from naagin.models.utils import OtherOwnerModel


class FriendshipFriendIdDeleteResponseModel(BaseModel):
    friendship_list: list[FriendshipModel]
    owner_list: Optional[list[OtherOwnerModel]] = None
