from .....other_owner import OtherOwnerModel
from .....owner import OwnerModel
from ......base import NaaginBaseModel


class OwnerBirthdayPostResponseModel(NaaginBaseModel):
    owner: OwnerModel
    owner_list: list[OtherOwnerModel]
