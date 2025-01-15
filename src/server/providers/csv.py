from csv import DictReader
from csv import QUOTE_ALL
from csv import reader

from .. import settings
from ..models.csv import EpisodeCSVModel
from ..types.headers import MasterVersionHeader


async def provide_owner_levels(master_version: MasterVersionHeader) -> list[int]:
    csv_data = await (
        settings.data.csv_dir / str(master_version) / "owner_level_table.csv"
    ).read_text()
    csv_reader = reader(csv_data.splitlines(), quoting=QUOTE_ALL)
    return list(map(int, next(csv_reader)))[1:]


async def provide_episodes(
    master_version: MasterVersionHeader,
) -> dict[int, EpisodeCSVModel]:
    csv_data = await (
        settings.data.csv_dir / str(master_version) / "EpisodeList.csv"
    ).read_text()
    dict_reader = DictReader(csv_data.splitlines(), quoting=QUOTE_ALL)
    episodes = tuple(EpisodeCSVModel.model_validate(row) for row in dict_reader)
    return {episode.episode_mid: episode for episode in episodes}
