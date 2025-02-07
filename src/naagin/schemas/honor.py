from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import BaseSchema
from .owner import OwnerSchema


class HonorSchema(BaseSchema):
    __tablename__ = "honor"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)
    honor_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    times_received: Mapped[int] = mapped_column(Integer, default=1)
    parent_honor_mid: Mapped[int] = mapped_column(Integer, default=0)

    __table_args__ = (
        CheckConstraint(times_received == 1, "times_received_const"),
        CheckConstraint(parent_honor_mid == 0, "parent_honor_mid_const"),
    )
