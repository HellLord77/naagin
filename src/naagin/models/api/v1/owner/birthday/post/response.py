from ......base import BaseModel
from ......utils import OtherOwnerModel
from ......utils import OwnerModel


class OwnerBirthdayPostResponseModel(BaseModel):
    owner: OwnerModel
    owner_list: list[OtherOwnerModel]
