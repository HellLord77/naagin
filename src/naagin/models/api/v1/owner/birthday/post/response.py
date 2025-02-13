from naagin.bases import ModelBase
from naagin.models.common import OwnerModel
from naagin.models.common import OwnerOtherModel


class OwnerBirthdayPostResponseModel(ModelBase):
    owner: OwnerModel
    owner_list: list[OwnerOtherModel]
