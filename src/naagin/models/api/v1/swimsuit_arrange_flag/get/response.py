from naagin.models.base import BaseModel
from naagin.models.common import SwimsuitArrangeFlagModel


class SwimsuitArrangeFlagGetResponseModel(BaseModel):
    swimsuit_arrage_flag_list: list[SwimsuitArrangeFlagModel]
