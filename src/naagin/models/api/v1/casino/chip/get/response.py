from datetime import datetime

from naagin.bases import ModelBase


class CasinoChipModel(ModelBase):
    owner_id: int
    chip_normal: int
    chip_gold: int
    limit_chip_gold: int
    gold_chip_mid: int
    dealer_chip_count: int
    created_at: datetime
    updated_at: datetime | None


class CasinoChipGetResponseModel(ModelBase):
    casino_chip: CasinoChipModel
