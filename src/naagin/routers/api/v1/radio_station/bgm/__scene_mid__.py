from fastapi import APIRouter

from naagin.enums import SceneEnum
from naagin.models.api import RadioStationBgmSceneMidPostRequestModel
from naagin.models.api import RadioStationBgmSceneMidPostResponseModel
from naagin.schemas import BgmSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/{scene_mid}")


@router.post("")
async def post(
    scene_mid: SceneEnum,
    request: RadioStationBgmSceneMidPostRequestModel,
    database: DatabaseDependency,
    owner_id: OwnerIdDependency,
) -> RadioStationBgmSceneMidPostResponseModel:
    bgm = await database.get(BgmSchema, owner_id, scene_mid, request.list_index)

    if bgm is None:
        bgm = BgmSchema(owner_id=owner_id, scene_mid=scene_mid, list_index=request.list_index)
        database.add(bgm)
    bgm.bgm_mid = request.bgm_mid

    await database.flush()

    return RadioStationBgmSceneMidPostResponseModel(bgm_list=[bgm])
