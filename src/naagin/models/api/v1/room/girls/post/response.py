from naagin.bases import ModelBase
from naagin.models.common import OwnerRoomModel


class RoomGirlsPostResponseModel(ModelBase):
    owner_room: OwnerRoomModel
