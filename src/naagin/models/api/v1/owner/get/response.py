from .....base import BaseModel
from .....utils import OwnerModel


class OwnerGetResponseModel(BaseModel):
    owner: OwnerModel
