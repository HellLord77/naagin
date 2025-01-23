from naagin.models.base import BaseModel
from naagin.models.common import OtherOwnerModel


class OwnerPutResponseModel(BaseModel):
    success: bool
    owner_list: list[OtherOwnerModel]
