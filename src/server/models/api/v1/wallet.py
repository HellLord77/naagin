from pydantic import BaseModel
from pydantic import ConfigDict


class WalletModel(BaseModel):
    owner_id: int
    zack_money: int
    guest_point: int
    vip_point: int
    paid_vstone: int
    free_vstone: int
    vip_coin: int


class WalletResponseModel(BaseModel):
    wallet: WalletModel

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "wallet": {
                        "owner_id": 288696,
                        "zack_money": 38407921,
                        "guest_point": 140420,
                        "vip_point": 990,
                        "paid_vstone": 0,
                        "free_vstone": 17350,
                        "vip_coin": 242,
                    }
                }
            ],
        }
    )
