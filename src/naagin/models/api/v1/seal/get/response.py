from naagin.bases import ModelBase


class ItemSealModel(ModelBase):
    id: int
    item_mid: int
    type: int
    base_mid: int
    pvp_base_mid: int
    in_lock: int
    skill_level: int
    cost: int
    rarity: int
    experience: int


class SealGetResponseModel(ModelBase):
    item_seal_list: list[ItemSealModel]
