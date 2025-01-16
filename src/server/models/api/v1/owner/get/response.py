from ....owner import OwnerModel
from .....base import NaaginBaseModel


class OwnerGetResponseModel(NaaginBaseModel):
    owner: OwnerModel
