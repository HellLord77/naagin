from naagin.models.base import CustomBaseModel
from naagin.models.common import ItemConsumeModel


class ItemConsumeGetResponseModel(CustomBaseModel):
    item_consume_list: list[ItemConsumeModel]
