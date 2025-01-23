from naagin.models.base import BaseModel
from naagin.models.common import OtherOwnerModel
from naagin.models.common import OwnerModel


class OwnerBirthdayPostResponseModel(BaseModel):
    owner: OwnerModel
    owner_list: list[OtherOwnerModel]
