from naagin.bases import ModelBase


class MaxCombineOtherModel(ModelBase):
    owner_id: int
    item_mid: int
    variation: int
    max_combine: int


class MaxCombineOwnerIdItemMidGetResponseModel(ModelBase):
    max_combine_other: MaxCombineOtherModel
