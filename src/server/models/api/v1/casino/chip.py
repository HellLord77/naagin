from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class CasinoChipModel(BaseModel):
    owner_id: int
    chip_normal: int
    chip_gold: int
    limit_chip_gold: int
    gold_chip_mid: int
    dealer_chip_count: int
    created_at: datetime
    updated_at: datetime


class CasinoChipResponseModel(BaseModel):
    casino_chip: CasinoChipModel

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "casino_chip": {
                        "owner_id": 288696,
                        "chip_normal": 1000,
                        "chip_gold": 0,
                        "limit_chip_gold": 0,
                        "gold_chip_mid": 0,
                        "dealer_chip_count": 0,
                        "created_at": "2021-04-05 04:25:12",
                        "updated_at": "2025-01-06 19:05:03",
                    }
                }
            ],
        }
    )
