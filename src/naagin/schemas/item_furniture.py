from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import CustomBaseSchema
from .owner import OwnerSchema


class ItemFurnitureSchema(CustomBaseSchema):
    __tablename__ = "item_furniture"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), index=True)

    item_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    count: Mapped[int] = mapped_column(Integer, default=0)

    __table_args__ = (CheckConstraint(count >= 0, "count_min"),)
