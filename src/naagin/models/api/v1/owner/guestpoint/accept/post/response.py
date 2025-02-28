from naagin.bases import ModelBase
from naagin.models import WalletModel


class AcceptedGuestPointModel(ModelBase):
    guest_count: int
    guest_point: int


class OwnerGuestPointAcceptPostResponseModel(ModelBase):
    accepted_guest_point: AcceptedGuestPointModel
    wallet_list: list[WalletModel] | None = None
