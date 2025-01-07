from pydantic import BaseModel
from pydantic import ConfigDict


class BlackjackModel(BaseModel):
    owner_id: int
    game_mid: int
    bet: int
    girl_mid_npc1: int
    girl_mid_npc2: int
    is_even_money: int
    is_insurance: int
    split_player: int
    split_npc1: int
    split_npc2: int


class CasinoGameModel(BaseModel):
    game: int
    play_count: int
    win_count_total: int
    win_count_series: int
    win_count_series_max: int


class BlackjackBetDetailModel(BaseModel):
    bet_rate: int
    bet_count: int


class BlackjackVanishingModel(BaseModel):
    is_vanishing: int


class BlackjackThinkingNpcModel(BaseModel):
    position: int
    split: int
    thinking: int
    deck_id: int
    hand_number: int
    hand_suit: int


class BlackjackResultDealerModel(BaseModel):
    is_blackjack: int


class BlackjackRestartCounterModel(BaseModel):
    restart_status: int
    restart_counter: int


class BlackjackMainGirlModel(BaseModel):
    main_girl_mid: int


class CasinoBlackjackGetResponseModel(BaseModel):
    blackjack_list: list[BlackjackModel]
    casino_game_list: list[CasinoGameModel]
    blackjack_bet_detail: BlackjackBetDetailModel
    blackjack_split_list: list  # TODO
    blackjack_vanishing: BlackjackVanishingModel
    blackjack_hand_list: list  # TODO
    blackjack_thinking_npc_list: list[BlackjackThinkingNpcModel]
    blackjack_thinking_dealer_list: list  # TODO
    blackjack_result_list: list  # TODO
    blackjack_result_chip_list: list  # TODO
    blackjack_result_dealer: BlackjackResultDealerModel
    blackjack_restart_counter: BlackjackRestartCounterModel
    blackjack_main_girl: BlackjackMainGirlModel

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "blackjack_list": [
                        {
                            "owner_id": 288696,
                            "game_mid": 92,
                            "bet": 0,
                            "girl_mid_npc1": -1,
                            "girl_mid_npc2": -1,
                            "is_even_money": 0,
                            "is_insurance": 0,
                            "split_player": 0,
                            "split_npc1": 0,
                            "split_npc2": 0,
                        }
                    ],
                    "casino_game_list": [
                        {
                            "game": 2,
                            "play_count": 0,
                            "win_count_total": 0,
                            "win_count_series": 0,
                            "win_count_series_max": 0,
                        }
                    ],
                    "blackjack_bet_detail": {"bet_rate": 0, "bet_count": 0},
                    "blackjack_split_list": [],
                    "blackjack_vanishing": {"is_vanishing": 0},
                    "blackjack_hand_list": [],
                    "blackjack_thinking_npc_list": [
                        {
                            "position": 1,
                            "split": 0,
                            "thinking": 0,
                            "deck_id": 0,
                            "hand_number": 0,
                            "hand_suit": 0,
                        },
                        {
                            "position": 2,
                            "split": 0,
                            "thinking": 0,
                            "deck_id": 0,
                            "hand_number": 0,
                            "hand_suit": 0,
                        },
                        {
                            "position": 1,
                            "split": 1,
                            "thinking": 0,
                            "deck_id": 0,
                            "hand_number": 0,
                            "hand_suit": 0,
                        },
                        {
                            "position": 2,
                            "split": 1,
                            "thinking": 0,
                            "deck_id": 0,
                            "hand_number": 0,
                            "hand_suit": 0,
                        },
                        {
                            "position": 1,
                            "split": 2,
                            "thinking": 0,
                            "deck_id": 0,
                            "hand_number": 0,
                            "hand_suit": 0,
                        },
                        {
                            "position": 2,
                            "split": 2,
                            "thinking": 0,
                            "deck_id": 0,
                            "hand_number": 0,
                            "hand_suit": 0,
                        },
                    ],
                    "blackjack_thinking_dealer_list": [],
                    "blackjack_result_list": [],
                    "blackjack_result_chip_list": [],
                    "blackjack_result_dealer": {"is_blackjack": 0},
                    "blackjack_restart_counter": {
                        "restart_status": 0,
                        "restart_counter": 15,
                    },
                    "blackjack_main_girl": {"main_girl_mid": -1},
                }
            ],
        }
    )
