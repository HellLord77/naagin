from datetime import datetime

from pydantic import field_validator

from naagin.bases import ModelBase


class OwnerOtherModel(ModelBase):
    owner_id: int
    status: int
    name: str | None
    island_name: str | None
    message: str | None
    team_id: int
    honor1_mid: int
    honor2_mid: int
    level: int
    experience: int
    stamina: int
    main_girl_mid: int
    lend_girl_mid: int
    spot_mid: int
    spot_phase_mid: int
    license_point: int
    license_level: int
    checked_license_level: int
    birthday: None
    stamina_checked_at: datetime
    last_logged_at: datetime
    friend_code: str
    created_at: datetime

    @field_validator("birthday", mode="before")
    @classmethod
    def birthday_validator[T](cls, _: T) -> None:
        pass
