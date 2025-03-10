from naagin.bases import ModelBase
from naagin.models import OwnerRoomModel


class RoomGirlsPostResponseModel(ModelBase):
    owner_room: OwnerRoomModel
