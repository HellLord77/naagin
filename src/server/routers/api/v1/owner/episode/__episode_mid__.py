from bisect import bisect

from fastapi import APIRouter

from ......models.api import OwnerEpisodeEpisodeMidPostResponseModel
from ......models.api import OwnerEpisodeEpisodeMidPutRequestModel
from ......models.api import OwnerEpisodeEpisodeMidPutResponseModel
from ......models.api.v1.owner.episode.__episode_mid__.post.response import (
    EpisodeResultModel,
)
from ......models.api.v1.owner.episode.__episode_mid__.post.response import (
    EpisodeResultOwnerModel,
)
from ......schemas import EpisodeSchema
from ......schemas import OwnerSchema
from ......types.dependencies import OwnerIdDependency
from ......types.dependencies import SessionDependency
from ......types.dependencies.csv import EpisodesCSVDependency
from ......types.dependencies.csv import OwnerLevelsCSVDependency

router = APIRouter(prefix="/{episode_mid}")


@router.put("")
async def put(
    episode_mid: int,
    _: OwnerEpisodeEpisodeMidPutRequestModel,
    session: SessionDependency,
    owner_id: OwnerIdDependency,
) -> OwnerEpisodeEpisodeMidPutResponseModel:
    episode = await session.get(EpisodeSchema, (owner_id, episode_mid))
    if episode is None:
        episode = EpisodeSchema(owner_id=owner_id, episode_mid=episode_mid)
        session.add(episode)
    else:
        episode.count += 1
    await session.flush()
    await session.refresh(episode)
    return OwnerEpisodeEpisodeMidPutResponseModel(episode_list=[episode])


@router.post("")
async def post(
    episode_mid: int,
    session: SessionDependency,
    owner_id: OwnerIdDependency,
    owner_levels_csv: OwnerLevelsCSVDependency,
    episodes_csv: EpisodesCSVDependency,
) -> OwnerEpisodeEpisodeMidPostResponseModel:
    owner = await session.get_one(OwnerSchema, owner_id)
    episode = await session.get_one(EpisodeSchema, (owner_id, episode_mid))

    experience_before = owner.experience
    experience_gain = (
        episodes_csv[episode_mid].experience_gain if episode.count == 0 else 0
    )
    experience_after = experience_before + experience_gain
    level_before = owner.level
    level_after = bisect(owner_levels_csv, experience_after)
    level_gain = level_after - level_before

    owner.level = level_after
    owner.experience = experience_after
    episode.count += 1
    await session.flush()
    await session.refresh(owner)
    await session.refresh(episode)

    episode_result_owner = EpisodeResultOwnerModel(
        experience_before=experience_before,
        experience_gain=experience_gain,
        experience_after=experience_after,
        level_before=level_before,
        level_gain=level_gain,
        level_after=level_after,
    )
    episode_result = EpisodeResultModel(episode=episode, owner=episode_result_owner)
    return OwnerEpisodeEpisodeMidPostResponseModel(
        episode_result=episode_result, owner_list=[owner], episode_list=[episode]
    )
