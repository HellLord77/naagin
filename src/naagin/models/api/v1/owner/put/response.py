from naagin.models.base import BaseModel
from naagin.models.common import OwnerOtherModel


class OwnerPutResponseModel(BaseModel):
    success: bool
    owner_list: list[OwnerOtherModel]
