from naagin.bases import ModelBase
from naagin.models import OwnerModel
from naagin.models import OwnerOtherModel


class OwnerBirthdayPostResponseModel(ModelBase):
    owner: OwnerModel
    owner_list: list[OwnerOtherModel]
