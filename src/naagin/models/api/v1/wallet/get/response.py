from naagin.bases import ModelBase


class WalletModel(ModelBase):
    owner_id: int
    zack_money: int
    guest_point: int
    vip_point: int
    paid_vstone: int
    free_vstone: int
    vip_coin: int


class WalletGetResponseModel(ModelBase):
    wallet: WalletModel
