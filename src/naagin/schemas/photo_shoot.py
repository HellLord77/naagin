from datetime import date
from typing import Literal

from sqlalchemy import CheckConstraint
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase

from .owner import OwnerSchema


class PhotoShootSchema(SchemaBase):
    __tablename__ = "photo_shoot"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)
    shoot_count: Mapped[Literal[0, 1]] = mapped_column(Integer, default=0)
    recover_count: Mapped[Literal[0, 1]] = mapped_column(Integer, default=0)
    today: Mapped[date] = mapped_column(Date, default=func.current_date())

    __table_args__ = (
        CheckConstraint(shoot_count.between(0, 1), "shoot_count_range"),
        CheckConstraint(recover_count.between(0, 1), "recover_count_range"),
        CheckConstraint(shoot_count >= recover_count, "shoot_count_gte_recover_count"),
        # CheckConstraint(today <= updated_at, "today_lte_updated_at"),
    )
