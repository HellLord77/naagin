from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class PvpBorderModel(BaseModel):
    from_: int = Field(alias="from")
    to: int
    score: int


class PvpMainPageDetailsModel(BaseModel):
    pvp_has_deck: int
    pvp_match_point_max: int
    pvp_grade: int
    pvp_ranking_id_list: list[int]
    pvp_played_count_refresh: int
    pvp_high_score: list[int]
    pvp_current_rank: list[int]
    pvp_border: list[list[PvpBorderModel]]
    trend_bonus: list[int]
    bromide_modifier: float
    arena_points: int
    arena_points_checked_at: str


class MatchingPvpPvpDetailsGetResponseModel(BaseModel):
    pvp_main_page_details: PvpMainPageDetailsModel

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "pvp_main_page_details": {
                        "pvp_has_deck": 0,
                        "pvp_match_point_max": 8,
                        "pvp_grade": 7,
                        "pvp_ranking_id_list": [302],
                        "pvp_played_count_refresh": 1736276400,
                        "pvp_high_score": [0],
                        "pvp_current_rank": [0],
                        "pvp_border": [
                            [
                                {"from": 1, "to": 1, "score": 1341577},
                                {"from": 2, "to": 2, "score": 1331032},
                                {"from": 3, "to": 3, "score": 1313268},
                                {"from": 4, "to": 10, "score": 1152464},
                                {"from": 11, "to": 100, "score": 763389},
                                {"from": 101, "to": 500, "score": 513728},
                                {"from": 501, "to": 1000, "score": 410376},
                                {"from": 1001, "to": 5000, "score": 150863},
                                {"from": 5001, "to": 10000, "score": 55935},
                                {"from": 10001, "to": 999999, "score": 1792},
                            ]
                        ],
                        "trend_bonus": [0, 40, 0, 0],
                        "bromide_modifier": 0.021500000000000002,
                        "arena_points": 5,
                        "arena_points_checked_at": "2025-01-07 07:16:58",
                    }
                }
            ],
        }
    )
