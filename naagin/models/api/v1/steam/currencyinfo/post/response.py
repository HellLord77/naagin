from naagin.bases import ModelBase


class SteamCurrencyResultModel(ModelBase):
    steam_currency_result: bool
    currency: int


class SteamCurrencyInfoPostResponseModel(ModelBase):
    steam_currency_result: SteamCurrencyResultModel
