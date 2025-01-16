from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.types.enums import OptionLockEnum
from naagin.types.enums.schemas import OptionLockEnumSchema
from .base import BaseSchema
from .owner import OwnerSchema


class OptionItemAutoLockSchema(BaseSchema):
    __tablename__ = "option_item_auto_lock"

    owner_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True
    )
    option_lock_only: Mapped[OptionLockEnum] = mapped_column(
        OptionLockEnumSchema, default=OptionLockEnum.LOCK
    )
    option_lock_sr: Mapped[OptionLockEnum] = mapped_column(
        OptionLockEnumSchema, default=OptionLockEnum.LOCK
    )
    option_lock_ssr: Mapped[OptionLockEnum] = mapped_column(
        OptionLockEnumSchema, default=OptionLockEnum.LOCK
    )
