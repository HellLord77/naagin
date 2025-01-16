from .....utils import OtherOwnerModel
from .....utils import OwnerModel
from ......base import NaaginBaseModel


class OwnerBirthdayPostResponseModel(NaaginBaseModel):
    owner: OwnerModel
    owner_list: list[OtherOwnerModel]
