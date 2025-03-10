from naagin.bases import ModelBase


class CasinoGameModel(ModelBase):
    game: int
    play_count: int
    win_count_total: int
    win_count_series: int
    win_count_series_max: int


class CasinoGameGetResponseModel(ModelBase):
    casino_game_list: list[CasinoGameModel]
