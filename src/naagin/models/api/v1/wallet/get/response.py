from naagin.bases import ModelBase
from naagin.models import WalletModel


class WalletGetResponseModel(ModelBase):
    wallet: WalletModel
