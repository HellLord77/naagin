from datetime import datetime
from typing import Literal

from sqlalchemy import CheckConstraint
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase

from .owner import OwnerSchema


class LoginBonusSchema(SchemaBase):
    __tablename__ = "login_bonus"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)
    bonus_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    count: Mapped[int] = mapped_column(Integer, default=0)
    complite: Mapped[Literal[0, 1, 7]] = mapped_column(Integer, default=0)
    received_at: Mapped[datetime | None] = mapped_column(DateTime, default=None)

    __table_args__ = (
        CheckConstraint(count >= 0, "count_min"),
        CheckConstraint(complite.in_((0, 1, 7)), "complite_const"),
        CheckConstraint(received_at <= func.current_timestamp(), name="received_at_lte_now"),
    )
