from naagin.models.base import CustomBaseModel


class ItemFurnitureModel(CustomBaseModel):
    item_mid: int
    count: int


class FurnitureGetResponseModel(CustomBaseModel):
    item_furniture_list: list[ItemFurnitureModel]
