from naagin.bases import ModelBase


class AcceptedGuestPointModel(ModelBase):
    guest_count: int
    guest_point: int


class WalletModel(ModelBase):
    owner_id: int
    zack_money: int
    guest_point: int
    vip_point: int
    paid_vstone: int
    free_vstone: int
    vip_coin: int


class OwnerGuestPointAcceptPostResponseModel(ModelBase):
    accepted_guest_point: AcceptedGuestPointModel
    wallet_list: list[WalletModel] | None = None
