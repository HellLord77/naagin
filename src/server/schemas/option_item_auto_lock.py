from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import NaaginBaseSchema
from .owner import OwnerSchema
from ..types.enums import OptionLockEnum
from ..types.enums.schemas import OptionLockEnumSchema


class OptionItemAutoLockSchema(NaaginBaseSchema):
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
