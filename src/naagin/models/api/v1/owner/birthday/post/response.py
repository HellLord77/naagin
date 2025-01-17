from naagin.models.base import BaseModel
from naagin.models.utils import OtherOwnerModel
from naagin.models.utils import OwnerModel


class OwnerBirthdayPostResponseModel(BaseModel):
    owner: OwnerModel
    owner_list: list[OtherOwnerModel]
