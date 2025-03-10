from fastapi import APIRouter

from naagin.models.api import OwnerEpisodeGetResponseModel
from naagin.schemas import EpisodeSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

from . import __episode_mid__

router = APIRouter(prefix="/episode")

router.include_router(__episode_mid__.router)


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> OwnerEpisodeGetResponseModel:
    episode_list = await database.find_all(EpisodeSchema, EpisodeSchema.owner_id == owner_id)
    return OwnerEpisodeGetResponseModel(episode_list=episode_list)
