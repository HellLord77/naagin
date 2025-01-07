from pydantic import BaseModel
from pydantic import ConfigDict


class PhotoShootTodayCountResponseModel(BaseModel):
    photo_shoot_today_count: int
    photo_recover_today_count: int

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {"photo_shoot_today_count": 0, "photo_recover_today_count": 0}
            ],
        }
    )
