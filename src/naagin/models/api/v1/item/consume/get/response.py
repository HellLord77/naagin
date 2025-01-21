from naagin.models.base import BaseModel
from naagin.models.utils import ItemConsumeModel


class ItemConsumeGetResponseModel(BaseModel):
    item_consume_list: list[ItemConsumeModel]
