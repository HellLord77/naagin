from fastapi import APIRouter

from naagin.models.api import NGWordPostRequestModel
from naagin.models.api import NGWordPostResponseModel

router = APIRouter(prefix="/ngword")


@router.post("")
async def post(_: NGWordPostRequestModel) -> NGWordPostResponseModel:
    return NGWordPostResponseModel(ng_word_list=[])
