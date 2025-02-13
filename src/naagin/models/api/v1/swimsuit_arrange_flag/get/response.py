from naagin.models.base import CustomBaseModel
from naagin.models.common import SwimsuitArrangeFlagModel


class SwimsuitArrangeFlagGetResponseModel(CustomBaseModel):
    swimsuit_arrage_flag_list: list[SwimsuitArrangeFlagModel]
