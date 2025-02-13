from naagin.bases import ModelBase
from naagin.models.common import OwnerModel


class OwnerGetResponseModel(ModelBase):
    owner: OwnerModel
