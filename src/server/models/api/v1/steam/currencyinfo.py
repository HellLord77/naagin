from pydantic import BaseModel
from pydantic import ConfigDict


class SteamCurrencyResultModel(BaseModel):
    steam_currency_result: bool
    currency: int


class SteamCurrencyInfoPostRequestModel(BaseModel):
    steam_id: str

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"steam_id": "76561198967489624"}],
        }
    )


class SteamCurrencyInfoPostResponseModel(BaseModel):
    steam_currency_result: SteamCurrencyResultModel

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "steam_currency_result": {
                        "steam_currency_result": True,
                        "currency": 9,
                    }
                }
            ],
        }
    )
