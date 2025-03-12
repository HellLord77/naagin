import csv
import functools
import hashlib
import json
import logging
import operator
import shutil
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from csv import DictReader
from io import StringIO
from pathlib import Path

import httpx

import config
import utils


# girl_mid, girl
# free_start
# 2, Kasumi
# 3, Honoka
# 4, Marie
# 5, Ayane
# 6, Nyotengu
# 7, Kokoro
# 8, Hitomi
# 9, Momiji
# 10, Helena
# free_end
# 11, Misaki
# 12, Luna
# 13, Tamaki
# 14, Leifang
# 16, Nagisa
# 18, Monica
# 19, Sayuri
# 22, Lobelia
# 23, Nanami
# 25, Koharu
# ...
# 32, ...

# request_mid, job, time
# 1, 'Tidy Up' as a pair, 0h10m
# 2, 'Clean Up' as a pair, 0h20m
# 3, 'Cook' as a pair, 1h0m
# 4, 'Shop' together, 3h0m
# 5, 'Check Out the island' together, 6h0m
# 6, 'Carry Out as nature survey' as friends, 12h0m
# 7, 'Create a written report' as friends, 20h0m
# 55, Friendly 'Lunch Making', 0h0m

# item_mid, item
# 25001, honor
# 35013, guest_point
# 35021, free_vstone
# 37980, venus_memory

# 35001 Upgrade APL Stone (S)
# 35002 Upgrade APL Stone (M)
# 35003 Upgrade APL Stone (L)
# 35004 Unlock APL Stone (M)
# 35004 Upgrade TEC Stone (M)
# 35005 Unlock APL Stone (L)
# 35006 Unlock APL Stone (XL)
# 35009 Fruit Basket
# 35010 Banana
# 35011 Candy
# 35015 Venus Ticket
# 35018 SSR Ticket
# 35030 Upgrade POW Stone (S)
# 35031 Upgrade POW Stone (M)
# 35032 Upgrade POW Stone (L)
# 35033 Upgrade POW Stone (XL)
# 35034 Unlock POW Stone (M)
# 35035 Unlock POW Stone (L)
# 35036 Unlock POW Stone (XL)
# 35048 Nostalgic SSR Gacha Coupon (24/10)
# 35050 SSR Gacha Coupon
# 35066 Upgrade STM Stone (S)
# 35067 Upgrade STM Stone (M)
# 35068 Upgrade STM Stone (L)
# 35069 Upgrade STM Stone (XL)
# 35072 FP Refill Drink
# 35073 Unlock STM Stone (M)
# 35074 Unlock STM Stone (L)
# 35075 Unlock STM Stone (XL)
# 35076 Upgrade TEC Stone (S)
# 35077 Upgrade TEC Stone (M)
# 35078 Upgrade TEC Stone (L)
# 35079 Upgrade TEC Stone (XL)
# 35080 Unlock TEC Stone (M)
# 35081 Unlock TEC Stone (L)
# 35082 Unlock TEC Stone (XL)
# 35083 VIP Points
# 35103 Kasumi Coin
# 35106 Ayane Coin
# 35109 Hitomi Coin
# 35110 Momiji Coin
# 35112 Misaki Coin
# 35125 Luna Coin
# 35178 Tamaki Coin
# 35229 VIP Coin
# 35243 Chinese Tea
# 35246 Leifang Coin
# 35252 Episode Coin
# 35316 Fiona Coin
# 35465 Closeness Medal
# 35680 POW Accessory Upgrade Material (M)
# 35681 POW Accessory Upgrade Material (L)
# 35682 POW Accessory Upgrade Material (XL)
# 35683 POW Accessory Unlock Material (M)
# 35684 POW Accessory Unlock Material (L)
# 35685 POW Accessory Unlock Material (XL)
# 35690 STM Accessory Unlock Material (M)
# 35691 STM Accessory Unlock Material (L)
# 35692 STM Accessory Unlock Material (XL)
# 35694 TEC Accessory Upgrade Material (M)
# 35695 TEC Accessory Upgrade Material (L)
# 35696 TEC Accessory Upgrade Material (XL)
# 35697 TEC Accessory Unlock Material (M)
# 35698 TEC Accessory Unlock Material (L)
# 35699 TEC Accessory Unlock Material (XL)
# 35828 100 FP Refill Drink
# 35857 Electrifying Deco-pen
# 35858 Shiny Deco-pen
# 35888 Monica Coin
# 36201 Moisturizing Fan (Momiji)
# 36452 Clover of Happiness
# 36628 Weekly SSR Ticket
# 36629 Weekly Gacha Ticket
# 36629 Weekly Gacha Ticket
# 37176 Bath Salts (L)
# 37177 Bath Salts (M)
# 37178 Bath Salts (S)
# 38273 Good Luck Bringing Coin
# 51078 Bathing, Splashing with Feet (Momiji)
# 52132 "Eyes Closed" Expression Card (Hitomi)
# 52134 "Eyes Closed" Expression Card (Momiji)
# 58420 Long 2 (Momiji)


@functools.cache
def get_csv_dir() -> Path:
    return config.DATA_DIR / "csv"


@functools.cache
def get_header_dir() -> Path:
    return config.DATA_DIR / "header"


@functools.cache
def get_json_dir() -> Path:
    return config.DATA_DIR / "json" / "csv"


@functools.cache
def get_schema_dir() -> Path:
    return config.DATA_DIR / "schema" / "csv"


@functools.cache
def get_model_dir() -> Path:
    return config.DATA_DIR / "model" / "csv"


def get_header_names() -> frozenset[str]:
    header_dir = get_header_dir() / str(config.VERSION)
    return frozenset(
        "".join(header_path.name.rsplit(".header", 1))
        for header_path in header_dir.rglob("*.header.csv")
    )


def game_to_csv():
    shutil.rmtree(get_csv_dir(), True)

    csv_list_path = (
        config.DATA_DIR / "api" / "v1" / "csv" / "list" / f"{config.APP_VERSION}.json"
    )
    with csv_list_path.open("rb") as file:
        csv_list = json.load(file)

    master_version = config.VERSION
    csv_file_list = csv_list["csv_file_list"]

    file_encrypt_key = csv_file_list.pop("file_encrypt_key")
    md5 = hashlib.md5(file_encrypt_key.encode())
    md5.update(str(master_version).encode())
    key = md5.hexdigest()

    header_names = get_header_names()
    header_dir = get_header_dir() / str(master_version)

    src_path = config.DATA_DIR / "game" / "production" / "csv" / str(master_version)
    dst_path = get_csv_dir() / str(master_version)
    for csv_file, initialization_vector in csv_file_list.items():
        encrypted_path = src_path / initialization_vector
        if not encrypted_path.is_file():
            logging.warning(f"[DOWNLOAD] {encrypted_path}")
            response = httpx.get(
                f"https://game.doaxvv.com/production/csv/{master_version}/{initialization_vector}"
            )
            response.raise_for_status()

            encrypted_path.parent.mkdir(parents=True, exist_ok=True)
            temp_path = encrypted_path.with_suffix(".temp")
            temp_path.write_bytes(response.content)
            temp_path.rename(encrypted_path)

        logging.info(f"[ENCRYPTED] {encrypted_path}")

        data = utils.decrypt_file(key, encrypted_path)
        if csv_file in header_names:
            header_path = (header_dir / csv_file).with_suffix(".header.csv")
            with header_path.open() as file:
                header = next(csv.reader(file))

            for index in range(len(header)):
                if header[index] == "":
                    header[index] = f"column_{index + 1}"

            string_io = StringIO()
            writer = csv.writer(string_io, quoting=csv.QUOTE_ALL)
            reader = csv.reader(data.decode("shift-jis").splitlines())

            writer.writerow(header)
            writer.writerows(reader)
            data = string_io.getvalue().encode("shift-jis")

        csv_path = dst_path / csv_file
        logging.warning(f"[CSV] {csv_path}")

        csv_path.parent.mkdir(parents=True, exist_ok=True)
        csv_path.write_bytes(data)


def isint(self: str) -> bool:
    return self[self[0] == "-" :].isdigit()


def csv_to_json(path: Path):
    logging.info(f"[CSV] {path}")

    dst_path = get_json_dir() / path.parent.name / path.stem
    dst_path.mkdir(parents=True, exist_ok=True)
    with path.open() as file:
        dict_reader = DictReader(file, quoting=csv.QUOTE_ALL)

        for index, data in enumerate(dict_reader, 1):
            for key, value in data.items():
                if value == "":
                    data[key] = None
                elif isint(value):
                    data[key] = int(value)

            path_name = f"row_{index}.json"
            json_path = dst_path / path_name

            logging.warning(f"[JSON] {json_path}")
            json_path.write_text(json.dumps(data, separators=(",", ":")))


def to_model():
    game_to_csv()

    shutil.rmtree(get_json_dir(), True)

    base_path = get_csv_dir() / str(config.VERSION)
    for csv_file in get_header_names():
        csv_path = base_path / csv_file
        if csv_path.is_file():
            csv_to_json(csv_path)

    shutil.rmtree(get_schema_dir(), True)
    json_to_schema = functools.partial(
        utils.json_to_schema, json_dir=get_json_dir(), schema_dir=get_schema_dir()
    )
    json_dirs = set(
        map(
            operator.attrgetter("parent"),
            filter(Path.is_file, get_json_dir().rglob("*.json")),
        )
    )
    with ThreadPoolExecutor() as executor:
        executor.map(json_to_schema, json_dirs)

    shutil.rmtree(get_model_dir(), True)
    schema_to_model = functools.partial(
        utils.schema_to_model, schema_dir=get_schema_dir(), model_dir=get_model_dir()
    )
    schema_paths = filter(Path.is_file, get_schema_dir().rglob("*.schema.json"))
    with ProcessPoolExecutor() as executor:
        executor.map(schema_to_model, schema_paths)
