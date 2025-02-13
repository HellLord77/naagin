from naagin.models.base import CustomBaseModel


class DishevelmentOtherModel(CustomBaseModel):
    owner_id: int
    item_mid: int
    variation: int
    dishevelment: int


class DishevelmentOwnerIdItemMidGetResponseModel(CustomBaseModel):
    dishevelment_other: DishevelmentOtherModel
