from pydantic import BaseModel
from pydantic import ConfigDict


class VenusBoardPanelResponseModel(BaseModel):
    venus_board_girl_panel_list: list  # TODO

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"venus_board_girl_panel_list": []}],
        }
    )
