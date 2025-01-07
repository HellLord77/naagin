from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class AcceptedGuestPointModel(BaseModel):
    guest_count: int
    guest_point: int


class WalletModel(BaseModel):
    owner_id: int
    zack_money: int
    guest_point: int
    vip_point: int
    paid_vstone: int
    free_vstone: int
    vip_coin: int


class OwnerGuestPointAcceptPostResponseModel(BaseModel):
    accepted_guest_point: AcceptedGuestPointModel
    wallet_list: Optional[list[WalletModel]] = None

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "accepted_guest_point": {"guest_count": 1, "guest_point": 50},
                    "wallet_list": [
                        {
                            "owner_id": 288696,
                            "zack_money": 38407921,
                            "guest_point": 140470,
                            "vip_point": 990,
                            "paid_vstone": 0,
                            "free_vstone": 17350,
                            "vip_coin": 242,
                        }
                    ],
                },
                {"accepted_guest_point": {"guest_count": 0, "guest_point": 0}},
            ],
        }
    )
