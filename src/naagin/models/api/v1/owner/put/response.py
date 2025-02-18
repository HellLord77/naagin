from naagin.bases import ModelBase
from naagin.models import OwnerOtherModel


class OwnerPutResponseModel(ModelBase):
    success: bool
    owner_list: list[OwnerOtherModel]
