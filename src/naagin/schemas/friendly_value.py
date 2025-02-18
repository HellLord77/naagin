from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase

from .owner import OwnerSchema


class FriendlyValueSchema(SchemaBase):
    __tablename__ = "friendly_value"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)
    girl_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    friendly_girl_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    value: Mapped[int] = mapped_column(Integer, default=0)
    level: Mapped[int] = mapped_column(Integer, default=1)
    unlock_count: Mapped[int] = mapped_column(Integer, default=0)

    __table_args__ = (
        CheckConstraint(girl_mid < friendly_girl_mid, "girl_mid_lt_friendly_girl_mid"),
        CheckConstraint(value >= 0, "value_min"),
        CheckConstraint(level >= 1, "level_min"),
        CheckConstraint(unlock_count.between(0, 2), "unlock_count_range"),
    )
