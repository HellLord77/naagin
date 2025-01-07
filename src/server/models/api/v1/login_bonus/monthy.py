from pydantic import BaseModel
from pydantic import ConfigDict


class MonthlyLoginModel(BaseModel):
    monthly_login_count: int
    monthly_login_collect: int


class WalletModel(BaseModel):
    owner_id: int
    zack_money: int
    guest_point: int
    vip_point: int
    paid_vstone: int
    free_vstone: int
    vip_coin: int


class RankingIdActiveGetResponseModel(BaseModel):
    monthly_login: MonthlyLoginModel
    wallet: WalletModel

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "monthly_login": {
                        "monthly_login_count": 1,
                        "monthly_login_collect": 0,
                    },
                    "wallet": {
                        "owner_id": 288696,
                        "zack_money": 38407921,
                        "guest_point": 140470,
                        "vip_point": 990,
                        "paid_vstone": 0,
                        "free_vstone": 17350,
                        "vip_coin": 242,
                    },
                }
            ],
        }
    )
