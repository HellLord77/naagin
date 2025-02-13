from naagin.bases import ModelBase


class DishevelmentOtherModel(ModelBase):
    owner_id: int
    item_mid: int
    variation: int
    dishevelment: int


class DishevelmentOwnerIdItemMidGetResponseModel(ModelBase):
    dishevelment_other: DishevelmentOtherModel
