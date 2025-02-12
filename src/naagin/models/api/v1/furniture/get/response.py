from naagin.models.base import BaseModel


class ItemFurnitureModel(BaseModel):
    item_mid: int
    count: int


class FurnitureGetResponseModel(BaseModel):
    item_furniture_list: list[ItemFurnitureModel]
