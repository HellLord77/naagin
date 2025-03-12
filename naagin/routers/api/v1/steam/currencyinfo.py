from fastapi import APIRouter

from naagin.models.api import SteamCurrencyInfoPostRequestModel
from naagin.models.api import SteamCurrencyInfoPostResponseModel
from naagin.models.api.v1.steam.currencyinfo.post.response import SteamCurrencyResultModel

router = APIRouter(prefix="/currencyinfo")


@router.post("")
async def post(_: SteamCurrencyInfoPostRequestModel) -> SteamCurrencyInfoPostResponseModel:
    steam_currency_result = SteamCurrencyResultModel(steam_currency_result=True, currency=9)
    return SteamCurrencyInfoPostResponseModel(steam_currency_result=steam_currency_result)
