from naagin.bases import ModelBase
from naagin.models.common import FriendlyValueModel


class RoomGirlFriendlyGetResponseModel(ModelBase):
    friendly_value_list: list[FriendlyValueModel]
