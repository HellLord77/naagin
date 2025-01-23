from naagin.models.base import BaseModel
from naagin.models.common import OwnerModel


class OwnerGetResponseModel(BaseModel):
    owner: OwnerModel
