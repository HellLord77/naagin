from ......base import BaseModel
from ......utils import FriendshipModel


class FriendshipReceivedGetResponseModel(BaseModel):
    friendship_list: list[FriendshipModel]
