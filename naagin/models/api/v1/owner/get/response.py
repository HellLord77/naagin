from naagin.bases import ModelBase
from naagin.models import OwnerModel


class OwnerGetResponseModel(ModelBase):
    owner: OwnerModel
