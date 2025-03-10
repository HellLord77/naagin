from fastapi import APIRouter

from naagin.models.api import QuestCheckLicensePointPostRequestModel
from naagin.models.api import QuestCheckLicensePointPostResponseModel

router = APIRouter(prefix="/license_point")


@router.post("")
async def post(_: QuestCheckLicensePointPostRequestModel) -> QuestCheckLicensePointPostResponseModel:
    return QuestCheckLicensePointPostResponseModel(root=[])
