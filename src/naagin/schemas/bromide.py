from sqlalchemy import Boolean
from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import CustomBaseSchema
from .owner import OwnerSchema


class BromideSchema(CustomBaseSchema):
    __tablename__ = "bromide"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)

    bromide_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    variation: Mapped[int] = mapped_column(Integer)
    is_generate_seal: Mapped[bool] = mapped_column(Boolean, default=False)
    count: Mapped[int] = mapped_column(Integer, default=0)

    __table_args__ = (
        CheckConstraint(variation.between(1, 2), "variation_range"),
        CheckConstraint(count >= 0, "count_min"),
    )
