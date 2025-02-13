from typing import Literal

from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase

from .owner import OwnerSchema


class MaxCombineSwimsuitSchema(SchemaBase):
    __tablename__ = "max_combine_swimsuit"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)
    item_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    variation: Mapped[Literal[1]] = mapped_column(Integer, default=1)

    __table_args__ = (CheckConstraint(variation == 1, "variation_const"),)
