from fastapi import APIRouter
from sqlalchemy import select

from naagin.models.api import OwnerEpisodeGetResponseModel
from naagin.schemas import EpisodeSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

from . import __episode_mid__

router = APIRouter(prefix="/episode")

router.include_router(__episode_mid__.router)


@router.get("")
async def get(session: SessionDependency, owner_id: OwnerIdDependency) -> OwnerEpisodeGetResponseModel:
    episode_list = (await session.scalars(select(EpisodeSchema).where(EpisodeSchema.owner_id == owner_id))).all()
    return OwnerEpisodeGetResponseModel(episode_list=episode_list)
