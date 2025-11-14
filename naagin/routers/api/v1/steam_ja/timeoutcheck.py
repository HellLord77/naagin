from fastapi import APIRouter

from naagin.models.api import SteamJaTimeoutCheckPostResponseModel

router = APIRouter(prefix="/timeoutcheck")


@router.post("")
async def post() -> SteamJaTimeoutCheckPostResponseModel:
    return SteamJaTimeoutCheckPostResponseModel(steam_timeout_check_result=False)
