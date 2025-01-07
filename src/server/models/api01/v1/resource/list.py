from pydantic import BaseModel
from pydantic import ConfigDict


class ResourceModel(BaseModel):
    version: int
    directory: str
    file_name: str
    file_size: int
    hash: str


class ResourceListModel(BaseModel):
    low: list[ResourceModel]
    common: list[ResourceModel]
    high: list[ResourceModel]
    exe: list[ResourceModel]


class ResourceListResponseModel(BaseModel):
    resource_list: ResourceListModel

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "resource_list": {
                        "low": [
                            {
                                "version": 63501,
                                "directory": "",
                                "file_name": "LOW006350100000_4c20026c.exe",
                                "file_size": 236147159,
                                "hash": "7e675d68e7f0b336de7b1fbcee4e7a47",
                            },
                            {
                                "version": 63502,
                                "directory": "",
                                "file_name": "LOW006350263501_ef57bddb.exe",
                                "file_size": 254587464,
                                "hash": "1758445ac7b8ce088051724dd692cc2a",
                            },
                            {
                                "version": 63503,
                                "directory": "",
                                "file_name": "LOW006350363502_9b700f0d.exe",
                                "file_size": 235057725,
                                "hash": "e31d82b8bc2ac20b2dcc93364ee9be49",
                            },
                            {
                                "version": 63504,
                                "directory": "",
                                "file_name": "LOW006350463503_667c5d58.exe",
                                "file_size": 231828642,
                                "hash": "31aacdb52204a38d822035ee79cb0f36",
                            },
                            {
                                "version": 63505,
                                "directory": "",
                                "file_name": "LOW006350563504_a01fd176.exe",
                                "file_size": 259340594,
                                "hash": "ce226f96fd7a005c3d78cefcb0d2ac54",
                            },
                            {
                                "version": 63506,
                                "directory": "",
                                "file_name": "LOW006350663505_77f7ef5c.exe",
                                "file_size": 299123,
                                "hash": "39c273bffc858bf9e0cdc19b9235da29",
                            },
                            {
                                "version": 63600,
                                "directory": "",
                                "file_name": "LOW006360063506_2efc7c9f.exe",
                                "file_size": 1559320,
                                "hash": "041897be264948f10bbbde8ffbe7afd5",
                            },
                            {
                                "version": 63700,
                                "directory": "",
                                "file_name": "LOW006370063600_be1fccb9.exe",
                                "file_size": 5517132,
                                "hash": "4cee71b96fa90a6ecb2a10dbcd4b773e",
                            },
                            {
                                "version": 63800,
                                "directory": "",
                                "file_name": "LOW006380063700_2a354505.exe",
                                "file_size": 1706496,
                                "hash": "3093396274c42569fc6ba9b63a6b2ee8",
                            },
                            {
                                "version": 63900,
                                "directory": "",
                                "file_name": "LOW006390063800_e13398e2.exe",
                                "file_size": 12951813,
                                "hash": "0ee1421f51443c44ef5c2d8d502871d5",
                            },
                        ],
                        "common": [
                            {
                                "version": 63501,
                                "directory": "",
                                "file_name": "COMMON006350100000_4c20026c.exe",
                                "file_size": 2411091608,
                                "hash": "ccb04055bf7f651acda58e23012f6198",
                            },
                            {
                                "version": 63502,
                                "directory": "",
                                "file_name": "COMMON006350263501_ef57bddb.exe",
                                "file_size": 2450498883,
                                "hash": "02e3f19696295fb302631245e75bdb24",
                            },
                            {
                                "version": 63503,
                                "directory": "",
                                "file_name": "COMMON006350363502_9b700f0d.exe",
                                "file_size": 2174487227,
                                "hash": "c999e62fd166653e5bc7c3a7edf61b47",
                            },
                            {
                                "version": 63504,
                                "directory": "",
                                "file_name": "COMMON006350463503_667c5d58.exe",
                                "file_size": 2390565371,
                                "hash": "e41ffed6f12459ef6ba2d67cab239fbe",
                            },
                            {
                                "version": 63505,
                                "directory": "",
                                "file_name": "COMMON006350563504_a01fd176.exe",
                                "file_size": 3486853344,
                                "hash": "1671a252bb106b606e81603fe731aee9",
                            },
                            {
                                "version": 63506,
                                "directory": "",
                                "file_name": "COMMON006350663505_77f7ef5c.exe",
                                "file_size": 299122,
                                "hash": "f4588a2c472e5f8557feb2d32e920f78",
                            },
                            {
                                "version": 63600,
                                "directory": "",
                                "file_name": "COMMON006360063506_2efc7c9f.exe",
                                "file_size": 24826639,
                                "hash": "0ea98abeacb71e038266e16794fd14f4",
                            },
                            {
                                "version": 63700,
                                "directory": "",
                                "file_name": "COMMON006370063600_be1fccb9.exe",
                                "file_size": 186675839,
                                "hash": "0e4bd1a447f80a6367e3d506254d5c60",
                            },
                            {
                                "version": 63800,
                                "directory": "",
                                "file_name": "COMMON006380063700_2a354505.exe",
                                "file_size": 115470773,
                                "hash": "cc8b7c943b7c14db64a300916c6794a3",
                            },
                            {
                                "version": 63900,
                                "directory": "",
                                "file_name": "COMMON006390063800_e13398e2.exe",
                                "file_size": 295850199,
                                "hash": "43fe59aeed2e55b792a512ca553d7783",
                            },
                        ],
                        "high": [
                            {
                                "version": 63501,
                                "directory": "",
                                "file_name": "HIGH006350100000_4c20026c.exe",
                                "file_size": 1755574621,
                                "hash": "b6b688b7da669605e70401978a37a1d3",
                            },
                            {
                                "version": 63502,
                                "directory": "",
                                "file_name": "HIGH006350263501_ef57bddb.exe",
                                "file_size": 1582883743,
                                "hash": "ac045a22bba5aebfe24ab4ff0a6c99f5",
                            },
                            {
                                "version": 63503,
                                "directory": "",
                                "file_name": "HIGH006350363502_9b700f0d.exe",
                                "file_size": 1677115555,
                                "hash": "626cc45bca49228b8dc61d114cf80924",
                            },
                            {
                                "version": 63504,
                                "directory": "",
                                "file_name": "HIGH006350463503_667c5d58.exe",
                                "file_size": 1651100676,
                                "hash": "9c91d3ecb9d771c7c4e7f70e5eacae2c",
                            },
                            {
                                "version": 63505,
                                "directory": "",
                                "file_name": "HIGH006350563504_a01fd176.exe",
                                "file_size": 1653233411,
                                "hash": "d362fc6df6180622e04c48b80ccf9817",
                            },
                            {
                                "version": 63506,
                                "directory": "",
                                "file_name": "HIGH006350663505_77f7ef5c.exe",
                                "file_size": 299121,
                                "hash": "5b6cf6e3f6e92adbba61856542aeb806",
                            },
                            {
                                "version": 63600,
                                "directory": "",
                                "file_name": "HIGH006360063506_2efc7c9f.exe",
                                "file_size": 3410701,
                                "hash": "919397cd17d8e05ccc623b6eb28cd8ed",
                            },
                            {
                                "version": 63700,
                                "directory": "",
                                "file_name": "HIGH006370063600_be1fccb9.exe",
                                "file_size": 24443333,
                                "hash": "0a8d91ce807e942583334f8035cfec38",
                            },
                            {
                                "version": 63800,
                                "directory": "",
                                "file_name": "HIGH006380063700_2a354505.exe",
                                "file_size": 5367788,
                                "hash": "1ceeefff7c894305441dc78a56ffaf85",
                            },
                            {
                                "version": 63900,
                                "directory": "",
                                "file_name": "HIGH006390063800_e13398e2.exe",
                                "file_size": 88171391,
                                "hash": "cd4d321912995f9e4520c2f86fc82532",
                            },
                        ],
                        "exe": [
                            {
                                "version": 63900,
                                "directory": "",
                                "file_name": "APP006390000000_a44bc3f4.exe",
                                "file_size": 16416190,
                                "hash": "f9416c0cb9f98831b9e684efa7d23c37",
                            }
                        ],
                    }
                }
            ]
        }
    )
