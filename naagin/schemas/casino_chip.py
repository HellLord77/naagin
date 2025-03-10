from typing import Literal

from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase

from .owner import OwnerSchema


class CasinoChipSchema(SchemaBase):
    __tablename__ = "casino_chip"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)
    chip_normal: Mapped[int] = mapped_column(Integer, default=0)
    chip_gold: Mapped[Literal[0, 20]] = mapped_column(Integer, default=0)
    limit_chip_gold: Mapped[Literal[0, 20]] = mapped_column(Integer, default=0)
    gold_chip_mid: Mapped[Literal[0, 53]] = mapped_column(Integer, default=0)
    dealer_chip_count: Mapped[Literal[0]] = mapped_column(Integer, default=0)

    __table_args__ = (
        CheckConstraint(chip_normal >= 0, "chip_normal_min"),
        CheckConstraint(chip_normal % 10 == 0, "chip_normal_mod"),
        CheckConstraint(chip_gold.in_((0, 20)), "chip_gold_const"),
        CheckConstraint(limit_chip_gold.in_((0, 20)), "limit_chip_gold_const"),
        CheckConstraint(gold_chip_mid.in_((0, 53)), "gold_chip_mid_const"),
        CheckConstraint(dealer_chip_count == 0, "dealer_chip_count_const"),
    )
