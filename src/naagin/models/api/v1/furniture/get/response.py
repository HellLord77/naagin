from naagin.bases import ModelBase


class ItemFurnitureModel(ModelBase):
    item_mid: int
    count: int


class FurnitureGetResponseModel(ModelBase):
    item_furniture_list: list[ItemFurnitureModel]
