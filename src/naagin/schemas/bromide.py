from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.enums import BooleanEnum
from .base import BaseSchema
from .enums import BooleanEnumSchema
from .owner import OwnerSchema


class BromideSchema(BaseSchema):
    __tablename__ = "bromide"

    owner_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True
    )

    bromide_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    variation: Mapped[int] = mapped_column(Integer)
    is_generate_seal: Mapped[BooleanEnum] = mapped_column(
        BooleanEnumSchema, default=BooleanEnum.FALSE
    )
    count: Mapped[int] = mapped_column(Integer, default=0)

    __table_args__ = (
        CheckConstraint(variation.between(1, 2), "variation_range"),
        CheckConstraint(count >= 0, "count_min"),
    )
