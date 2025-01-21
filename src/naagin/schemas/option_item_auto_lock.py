from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.enums import BooleanEnum
from .base import BaseSchema
from .enums import BooleanEnumSchema
from .owner import OwnerSchema


class OptionItemAutoLockSchema(BaseSchema):
    __tablename__ = "option_item_auto_lock"

    owner_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True
    )
    option_lock_only: Mapped[BooleanEnum] = mapped_column(
        BooleanEnumSchema, default=BooleanEnum.TRUE
    )
    option_lock_sr: Mapped[BooleanEnum] = mapped_column(
        BooleanEnumSchema, default=BooleanEnum.TRUE
    )
    option_lock_ssr: Mapped[BooleanEnum] = mapped_column(
        BooleanEnumSchema, default=BooleanEnum.TRUE
    )
