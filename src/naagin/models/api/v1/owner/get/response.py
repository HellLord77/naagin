from naagin.models.base import BaseModel
from naagin.models.utils import OwnerModel


class OwnerGetResponseModel(BaseModel):
    owner: OwnerModel
