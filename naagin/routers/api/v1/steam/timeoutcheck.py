from fastapi import APIRouter

from naagin.models.api import SteamTimeoutCheckPostResponseModel

router = APIRouter(prefix="/timeoutcheck")


@router.post("")
async def post() -> SteamTimeoutCheckPostResponseModel:
    return SteamTimeoutCheckPostResponseModel(steam_timeout_check_result=False)
