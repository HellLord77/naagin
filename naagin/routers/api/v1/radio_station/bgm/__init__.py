from fastapi import APIRouter

from naagin.models.api import RadioStationBgmGetResponseModel
from naagin.schemas import BgmSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

from . import __scene_mid__

router = APIRouter(prefix="/bgm")

router.include_router(__scene_mid__.router)


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> RadioStationBgmGetResponseModel:
    bgm_list = await database.find_all(BgmSchema, BgmSchema.owner_id == owner_id)
    return RadioStationBgmGetResponseModel(bgm_list=bgm_list)
