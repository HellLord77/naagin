from naagin.models.base import CustomBaseModel


class MaxCombineOtherModel(CustomBaseModel):
    owner_id: int
    item_mid: int
    variation: int
    max_combine: int


class MaxCombineOwnerIdItemMidGetResponseModel(CustomBaseModel):
    max_combine_other: MaxCombineOtherModel
