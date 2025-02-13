from naagin.models.base import CustomBaseModel
from naagin.models.common import OwnerModel


class OwnerGetResponseModel(CustomBaseModel):
    owner: OwnerModel
