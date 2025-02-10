from fastapi import APIRouter

from naagin.models.api import OwnerEpisodeGetResponseModel
from naagin.schemas import EpisodeSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

from . import __episode_mid__

router = APIRouter(prefix="/episode")

router.include_router(__episode_mid__.router)


@router.get("")
async def get(session: SessionDependency, owner_id: OwnerIdDependency) -> OwnerEpisodeGetResponseModel:
    episode_list = await session.find_all(EpisodeSchema, EpisodeSchema.owner_id == owner_id)
    return OwnerEpisodeGetResponseModel(episode_list=episode_list)
