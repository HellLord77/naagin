from naagin.models.base import BaseModel


class WalletModel(BaseModel):
    owner_id: int
    zack_money: int
    guest_point: int
    vip_point: int
    paid_vstone: int
    free_vstone: int
    vip_coin: int


class WalletGetResponseModel(BaseModel):
    wallet: WalletModel
