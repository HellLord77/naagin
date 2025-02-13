from naagin.bases import ModelBase
from naagin.models.common import OwnerOtherModel


class OwnerPutResponseModel(ModelBase):
    success: bool
    owner_list: list[OwnerOtherModel]
