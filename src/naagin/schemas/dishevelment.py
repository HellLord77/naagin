from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import BaseSchema
from .owner import OwnerSchema


class DishevelmentSchema(BaseSchema):
    __tablename__ = "dishevelment"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)
    item_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    variation: Mapped[int] = mapped_column(Integer, default=1)

    __table_args__ = (CheckConstraint(variation == 1, "variation_const"),)
