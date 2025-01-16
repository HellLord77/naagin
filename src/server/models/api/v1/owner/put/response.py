from ....other_owner import OtherOwnerModel
from .....base import NaaginBaseModel


class OwnerPutResponseModel(NaaginBaseModel):
    success: bool
    owner_list: list[OtherOwnerModel]
