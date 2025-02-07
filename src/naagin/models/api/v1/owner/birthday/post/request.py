from datetime import date

from pydantic import field_validator

from naagin.models.base import BaseModel


class OwnerBirthdayPostRequestModel(BaseModel):
    birthday: date

    @field_validator("birthday", mode="before")
    @classmethod
    def birthday_validator[T](cls, value: T) -> T:
        if isinstance(value, str):
            value = f"{value[:4]}-{value[4:6]}-{value[6:]}"
        return value
