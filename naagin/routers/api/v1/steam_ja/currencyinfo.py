from fastapi import APIRouter

from naagin.models.api import SteamJaCurrencyInfoPostRequestModel
from naagin.models.api import SteamJaCurrencyInfoPostResponseModel
from naagin.models.api.v1.steam_ja.currencyinfo.post.response import SteamCurrencyResultModel

router = APIRouter(prefix="/currencyinfo")


@router.post("")
async def post(_: SteamJaCurrencyInfoPostRequestModel) -> SteamJaCurrencyInfoPostResponseModel:
    steam_currency_result = SteamCurrencyResultModel(steam_currency_result=True, currency=9)
    return SteamJaCurrencyInfoPostResponseModel(steam_currency_result=steam_currency_result)
