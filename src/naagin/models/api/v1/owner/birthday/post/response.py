from naagin.models.base import CustomBaseModel
from naagin.models.common import OwnerModel
from naagin.models.common import OwnerOtherModel


class OwnerBirthdayPostResponseModel(CustomBaseModel):
    owner: OwnerModel
    owner_list: list[OwnerOtherModel]
