from naagin.models.base import BaseModel
from naagin.models.common import FriendshipModel


class FriendshipReceivedGetResponseModel(BaseModel):
    friendship_list: list[FriendshipModel]
