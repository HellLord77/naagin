from naagin.models.base import BaseModel


class DishevelmentOtherModel(BaseModel):
    owner_id: int
    item_mid: int
    variation: int
    dishevelment: int


class DishevelmentOwnerIdItemMidGetResponseModel(BaseModel):
    dishevelment_other: DishevelmentOtherModel
