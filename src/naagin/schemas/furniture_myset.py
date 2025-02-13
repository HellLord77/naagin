from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import CustomBaseSchema
from .owner import OwnerSchema


class FurnitureMySetSchema(CustomBaseSchema):
    __tablename__ = "furniture_myset"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), index=True)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    item_mid: Mapped[int] = mapped_column(Integer)
    layout_mid: Mapped[int] = mapped_column(Integer)
    rot_y: Mapped[int] = mapped_column(Integer)

    __table_args__ = (
        CheckConstraint(rot_y.between(0, 270), "rot_y_range"),
        CheckConstraint(rot_y % 90 == 0, "rot_y_mod"),
    )
