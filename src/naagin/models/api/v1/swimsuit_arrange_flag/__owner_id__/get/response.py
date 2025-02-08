from naagin.models.base import BaseModel
from naagin.models.common import SwimsuitArrangeFlagModel


class SwimsuitArrangeFlagOwnerIdGetResponseModel(BaseModel):
    swimsuit_arrage_flag_other_list: list[SwimsuitArrangeFlagModel]
