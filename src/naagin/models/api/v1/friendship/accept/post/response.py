from naagin.models.base import BaseModel
from naagin.models.common import FriendshipModel
from naagin.models.common import OwnerOtherModel


class FriendshipAcceptPostResponseModel(BaseModel):
    friendship_list: list[FriendshipModel]
    owner_list: list[OwnerOtherModel]
