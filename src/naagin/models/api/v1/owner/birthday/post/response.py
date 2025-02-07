from naagin.models.base import BaseModel
from naagin.models.common import OwnerModel
from naagin.models.common import OwnerOtherModel


class OwnerBirthdayPostResponseModel(BaseModel):
    owner: OwnerModel
    owner_list: list[OwnerOtherModel]
