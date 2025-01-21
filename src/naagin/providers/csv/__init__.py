from itertools import islice

from naagin.models.csv import EpisodeCSVModel
from naagin.models.csv import GirlCSVModel
from naagin.models.csv import GirlStatusCSVModel
from naagin.types.headers import MasterVersionHeader
from .utils import get_dict_reader
from .utils import get_reader


async def provide_girl_affection_levels(
    master_version: MasterVersionHeader,
) -> list[int]:
    reader = await get_reader(master_version, "Girl_Affection_Level")
    girl_affection_levels = next(islice(reader, 2, None))
    del girl_affection_levels[:2]
    count = int(girl_affection_levels.pop(0)) + 1
    return list(map(int, islice(girl_affection_levels, None, count)))


async def provide_girl_levels(master_version: MasterVersionHeader) -> list[int]:
    reader = await get_reader(master_version, "girl_level_table")
    girl_levels = next(islice(reader, 2, None))
    del girl_levels[:2]
    count = int(girl_levels.pop(0)) + 1
    return list(map(int, islice(girl_levels, None, count)))


async def provide_girls(master_version: MasterVersionHeader) -> dict[int, GirlCSVModel]:
    reader = await get_dict_reader(master_version, "girl_master")
    girls = map(GirlCSVModel.model_validate, reader)
    return {girl.girl_mid: girl for girl in girls}


async def provide_girl_statuses(
    master_version: MasterVersionHeader,
) -> list[GirlStatusCSVModel]:
    reader = await get_reader(master_version, "girl_status_table")
    girl_statuses = islice(reader, 3, None)
    appeals = next(girl_statuses)
    del appeals[:3]
    powers_or_technics = next(girl_statuses)
    del powers_or_technics[:2]
    staminas = next(girl_statuses)
    del staminas[:3]
    count = int(powers_or_technics.pop(0)) + 1
    return list(
        GirlStatusCSVModel(
            appeal=appeal, power_or_technic=power_or_technic, stamina=stamina
        )
        for appeal, power_or_technic, stamina in islice(
            zip(appeals, powers_or_technics, staminas), None, count
        )
    )


async def provide_owner_levels(master_version: MasterVersionHeader) -> list[int]:
    reader = await get_reader(master_version, "owner_level_table")
    owner_levels = next(reader)
    count = int(owner_levels.pop(0))
    return list(map(int, islice(owner_levels, None, count)))


async def provide_episodes(
    master_version: MasterVersionHeader,
) -> dict[int, EpisodeCSVModel]:
    reader = await get_dict_reader(master_version, "EpisodeList")
    episodes = map(EpisodeCSVModel.model_validate, reader)
    return {episode.episode_mid: episode for episode in episodes}
