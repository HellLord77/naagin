from pydantic import BaseModel
from pydantic import ConfigDict


class PvpFesDeckEquipmentListAllResponseModel(BaseModel):
    pvp_fes_deck_girl_equipment_full_list: list  # TODO

    model_config = ConfigDict(
        json_schema_extra={"examples": [{"pvp_fes_deck_girl_equipment_full_list": []}]}
    )
