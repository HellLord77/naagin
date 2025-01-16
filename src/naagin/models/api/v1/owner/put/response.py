from .....base import BaseModel
from .....utils import OtherOwnerModel


class OwnerPutResponseModel(BaseModel):
    success: bool
    owner_list: list[OtherOwnerModel]
