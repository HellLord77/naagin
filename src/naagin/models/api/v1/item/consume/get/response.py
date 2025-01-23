from naagin.models.base import BaseModel
from naagin.models.common import ItemConsumeModel


class ItemConsumeGetResponseModel(BaseModel):
    item_consume_list: list[ItemConsumeModel]
