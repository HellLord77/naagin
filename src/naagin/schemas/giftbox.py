from datetime import datetime
from typing import Literal

from sqlalchemy import CheckConstraint
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import column_property
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase
from naagin.enums import GiftBoxMessageTypeTypeEnum

from .enums import GiftBoxMessageTypeTypeEnumSchema
from .owner import OwnerSchema


class GiftBoxSchema(SchemaBase):
    __tablename__ = "giftbox"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    sender_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), index=True)
    sender_name: Mapped[str] = column_property(
        select(OwnerSchema.name).where(OwnerSchema.owner_id == sender_id).scalar_subquery()
    )
    item_mid: Mapped[int] = mapped_column(Integer)
    count: Mapped[int] = mapped_column(Integer)
    message_type: Mapped[GiftBoxMessageTypeTypeEnum] = mapped_column(GiftBoxMessageTypeTypeEnumSchema)
    message: Mapped[str] = mapped_column(String(0))
    parameter1: Mapped[Literal[0, 14324]] = mapped_column(Integer)
    expired_at: Mapped[datetime] = mapped_column(DateTime)
    accepted_at: Mapped[datetime | None] = mapped_column(DateTime, default=None)

    __table_args__ = (
        CheckConstraint(id >= 1, "id_min"),
        CheckConstraint(count >= 1, "count_min"),
        CheckConstraint(message == "", "message_const"),
        CheckConstraint(
            parameter1 == 14324 if message_type == GiftBoxMessageTypeTypeEnum._VALUE_35 else parameter1 == 0,  # noqa: PLR2004, SLF001
            "parameter1_const",
        ),
        CheckConstraint(expired_at >= func.current_timestamp(), "expired_at_gte_now"),
        CheckConstraint(accepted_at <= func.current_timestamp(), "accepted_at_lte_now"),
    )
