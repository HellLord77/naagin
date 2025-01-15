from fastapi import APIRouter
from sqlalchemy import insert

from ......models.api import OwnerEpisodeEpisodeMidPutRequestModel
from ......models.api import OwnerEpisodeEpisodeMidPutResponseModel
from ......schemas import EpisodeSchema
from ......types.dependencies import OwnerId
from ......types.dependencies import Session

router = APIRouter(prefix="/{episode_mid}")


@router.put("")
async def put(
    episode_mid: int,
    request: OwnerEpisodeEpisodeMidPutRequestModel,
    session: Session,
    owner_id: OwnerId,
) -> OwnerEpisodeEpisodeMidPutResponseModel:
    episode = await session.scalar(
        insert(EpisodeSchema)
        .values(
            owner_id=owner_id,
            episode_mid=episode_mid,
            count=request.count,
        )
        .returning(EpisodeSchema)
    )
    return OwnerEpisodeEpisodeMidPutResponseModel(episode_list=[episode])
