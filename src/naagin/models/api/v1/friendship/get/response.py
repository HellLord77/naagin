from naagin.models.base import BaseModel
from naagin.models.utils import FriendshipModel


class FriendshipGetResponseModel(BaseModel):
    friendship_list: list[FriendshipModel]
