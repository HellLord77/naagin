from naagin.models.base import BaseModel
from naagin.models.utils import OtherOwnerModel


class OwnerPutResponseModel(BaseModel):
    success: bool
    owner_list: list[OtherOwnerModel]
