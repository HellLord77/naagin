from pydantic import BaseModel
from pydantic import ConfigDict


class OwnerRoomModel(BaseModel):
    owner_id: int
    main_girl_mid: int
    sub_girl_mid: int
    set_no: int


class RoomPostResponseModel(BaseModel):
    owner_room: OwnerRoomModel

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "owner_room": {
                        "owner_id": 288696,
                        "main_girl_mid": 16,
                        "sub_girl_mid": 3,
                        "set_no": 0,
                    }
                }
            ],
        }
    )
