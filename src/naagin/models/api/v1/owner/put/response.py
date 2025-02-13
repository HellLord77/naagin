from naagin.models.base import CustomBaseModel
from naagin.models.common import OwnerOtherModel


class OwnerPutResponseModel(CustomBaseModel):
    success: bool
    owner_list: list[OwnerOtherModel]
