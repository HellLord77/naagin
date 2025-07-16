from csv import QUOTE_ALL
from csv import DictReader
from csv import reader

from naagin import settings
from naagin.types_ import CSVReader


async def get_lines(master_version: int, name: str) -> list[str]:
    data = await (settings.data.csv_dir / str(master_version) / f"{name}.csv").read_text("shift_jis")
    return data.splitlines()


async def get_reader(master_version: int, name: str) -> CSVReader:
    lines = await get_lines(master_version, name)
    return reader(lines, quoting=QUOTE_ALL)


async def get_dict_reader(master_version: int, name: str) -> DictReader:
    lines = await get_lines(master_version, name)
    return DictReader(lines, quoting=QUOTE_ALL)
