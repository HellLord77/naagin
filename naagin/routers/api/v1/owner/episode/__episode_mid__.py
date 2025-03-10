from bisect import bisect

from fastapi import APIRouter

from naagin.models.api import OwnerEpisodeEpisodeMidPostResponseModel
from naagin.models.api import OwnerEpisodeEpisodeMidPutRequestModel
from naagin.models.api import OwnerEpisodeEpisodeMidPutResponseModel
from naagin.models.api.v1.owner.episode.__episode_mid__.post.response import EpisodeResultModel
from naagin.models.api.v1.owner.episode.__episode_mid__.post.response import EpisodeResultOwnerModel
from naagin.schemas import EpisodeSchema
from naagin.schemas import OwnerSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies.csv import EpisodesCSVDependency
from naagin.types.dependencies.csv import OwnerLevelsCSVDependency

router = APIRouter(prefix="/{episode_mid}")


@router.put("")
async def put(
    episode_mid: int,
    _: OwnerEpisodeEpisodeMidPutRequestModel,
    database: DatabaseDependency,
    owner_id: OwnerIdDependency,
    episodes_csv: EpisodesCSVDependency,
) -> OwnerEpisodeEpisodeMidPutResponseModel:
    episode = await database.get(EpisodeSchema, (owner_id, episode_mid))

    success = episode is None
    if success:
        experience_gain = episodes_csv[episode_mid].experience_gain
        episode = EpisodeSchema(owner_id=owner_id, episode_mid=episode_mid, experience_gain=experience_gain)
        database.add(episode)
    else:
        episode.count += 1

    await database.flush()
    if success:
        await database.refresh(episode)

    return OwnerEpisodeEpisodeMidPutResponseModel(episode_list=[episode])


@router.post("")
async def post(
    episode_mid: int,
    database: DatabaseDependency,
    owner_id: OwnerIdDependency,
    owner_levels_csv: OwnerLevelsCSVDependency,
) -> OwnerEpisodeEpisodeMidPostResponseModel:
    owner = await database.get_one(OwnerSchema, owner_id)
    episode = await database.get_one(EpisodeSchema, (owner_id, episode_mid))

    experience_before = owner.experience
    experience_gain = episode.experience_gain
    experience_after = experience_before + experience_gain
    level_before = owner.level
    level_after = bisect(owner_levels_csv, experience_after)
    level_gain = level_after - level_before

    owner.level = level_after
    owner.experience = experience_after
    episode.count += 1
    episode.experience_gain = 0

    await database.flush()

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
