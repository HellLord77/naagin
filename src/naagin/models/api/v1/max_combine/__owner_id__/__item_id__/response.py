from naagin.models.base import BaseModel


class MaxCombineOtherModel(BaseModel):
    owner_id: int
    item_mid: int
    variation: int
    max_combine: int


class MaxCombineOwnerIdItemMidGetResponseModel(BaseModel):
    max_combine_other: MaxCombineOtherModel
