from typing import Literal

from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase

from .owner import OwnerSchema


class OnsenQualityStashSchema(SchemaBase):
    __tablename__ = "onsen_quality_stash"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)

    onsen_mid: Mapped[Literal[0]] = mapped_column(Integer, default=0, primary_key=True)
    quality_mid: Mapped[Literal[1, 2, 3]] = mapped_column(Integer, primary_key=True)

    __table_args__ = (
        CheckConstraint(onsen_mid == 0, "onsen_mid_const"),
        CheckConstraint(quality_mid.between(1, 3), "quality_mid_range"),
    )


raise NotImplementedError
