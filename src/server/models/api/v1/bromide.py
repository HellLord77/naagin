from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class BromideModel(BaseModel):
    item_mid: int
    variation: int
    is_generate_seal: int
    count: int
    created_at: datetime


class BromideGetResponseModel(BaseModel):
    bromide_list: list[BromideModel]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "bromide_list": [
                        {
                            "item_mid": 8,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2020-05-16 15:48:47",
                        },
                        {
                            "item_mid": 50,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 0,
                            "created_at": "2021-04-07 03:24:43",
                        },
                        {
                            "item_mid": 73,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 2,
                            "created_at": "2020-04-09 08:53:11",
                        },
                        {
                            "item_mid": 112,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2020-07-29 10:25:43",
                        },
                        {
                            "item_mid": 426,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2019-09-14 02:51:19",
                        },
                        {
                            "item_mid": 426,
                            "variation": 2,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2020-04-25 05:55:51",
                        },
                        {
                            "item_mid": 427,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2020-05-16 15:50:47",
                        },
                        {
                            "item_mid": 427,
                            "variation": 2,
                            "is_generate_seal": 0,
                            "count": 0,
                            "created_at": "2021-04-06 07:22:23",
                        },
                        {
                            "item_mid": 428,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 0,
                            "created_at": "2021-09-27 17:45:13",
                        },
                        {
                            "item_mid": 429,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2020-07-29 10:21:57",
                        },
                        {
                            "item_mid": 430,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2019-12-05 08:38:33",
                        },
                        {
                            "item_mid": 431,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 2,
                            "created_at": "2020-03-17 14:12:05",
                        },
                        {
                            "item_mid": 431,
                            "variation": 2,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2020-10-25 04:56:35",
                        },
                        {
                            "item_mid": 432,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2020-04-24 03:05:51",
                        },
                        {
                            "item_mid": 432,
                            "variation": 2,
                            "is_generate_seal": 0,
                            "count": 0,
                            "created_at": "2021-04-06 07:23:09",
                        },
                        {
                            "item_mid": 433,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2020-08-19 05:22:02",
                        },
                        {
                            "item_mid": 434,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 3,
                            "created_at": "2019-08-30 13:04:36",
                        },
                        {
                            "item_mid": 434,
                            "variation": 2,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2019-12-05 09:04:33",
                        },
                        {
                            "item_mid": 448,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2020-06-17 11:44:02",
                        },
                        {
                            "item_mid": 460,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2020-03-22 02:48:41",
                        },
                        {
                            "item_mid": 460,
                            "variation": 2,
                            "is_generate_seal": 0,
                            "count": 0,
                            "created_at": "2021-04-06 07:22:51",
                        },
                        {
                            "item_mid": 493,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 0,
                            "created_at": "2022-01-10 17:27:18",
                        },
                        {
                            "item_mid": 505,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2020-03-17 14:10:25",
                        },
                        {
                            "item_mid": 519,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2020-08-22 17:34:39",
                        },
                        {
                            "item_mid": 549,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2020-09-24 03:35:38",
                        },
                        {
                            "item_mid": 569,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2020-06-15 19:02:27",
                        },
                        {
                            "item_mid": 571,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2020-08-15 09:25:39",
                        },
                        {
                            "item_mid": 638,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2020-06-06 12:27:27",
                        },
                        {
                            "item_mid": 679,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2020-04-30 07:13:12",
                        },
                        {
                            "item_mid": 706,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2019-09-05 05:08:42",
                        },
                        {
                            "item_mid": 778,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 0,
                            "created_at": "2022-04-22 04:52:12",
                        },
                        {
                            "item_mid": 917,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2019-12-14 06:27:54",
                        },
                        {
                            "item_mid": 922,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2020-09-24 03:31:26",
                        },
                        {
                            "item_mid": 934,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2020-04-09 08:47:49",
                        },
                        {
                            "item_mid": 934,
                            "variation": 2,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2020-08-16 08:59:46",
                        },
                        {
                            "item_mid": 966,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 0,
                            "created_at": "2022-01-10 17:23:36",
                        },
                        {
                            "item_mid": 1099,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 2,
                            "created_at": "2020-10-22 08:42:15",
                        },
                        {
                            "item_mid": 1108,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 0,
                            "created_at": "2021-04-05 03:40:30",
                        },
                        {
                            "item_mid": 1116,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2020-08-22 17:43:05",
                        },
                        {
                            "item_mid": 1369,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 2,
                            "created_at": "2020-10-22 08:50:48",
                        },
                        {
                            "item_mid": 1583,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 0,
                            "created_at": "2022-01-10 17:08:36",
                        },
                        {
                            "item_mid": 1704,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 0,
                            "created_at": "2021-04-05 03:48:28",
                        },
                        {
                            "item_mid": 1710,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 0,
                            "created_at": "2021-04-06 07:49:01",
                        },
                        {
                            "item_mid": 1712,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 0,
                            "created_at": "2021-04-05 03:47:05",
                        },
                        {
                            "item_mid": 1713,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 0,
                            "created_at": "2021-04-11 04:22:52",
                        },
                        {
                            "item_mid": 1763,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 0,
                            "created_at": "2021-04-06 07:18:59",
                        },
                        {
                            "item_mid": 2276,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 1,
                            "created_at": "2020-09-24 03:21:20",
                        },
                        {
                            "item_mid": 2394,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 0,
                            "created_at": "2021-09-28 02:34:59",
                        },
                        {
                            "item_mid": 2483,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 0,
                            "created_at": "2021-08-14 03:16:00",
                        },
                        {
                            "item_mid": 4840,
                            "variation": 1,
                            "is_generate_seal": 0,
                            "count": 0,
                            "created_at": "2023-08-13 19:16:32",
                        },
                    ]
                }
            ],
        }
    )
