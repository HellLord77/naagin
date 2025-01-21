from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.types.enums import SpecialOrderTypeEnum
from naagin.types.enums.schemas import SpecialOrderTypeEnumSchema
from .base import BaseSchema
from .owner import OwnerSchema


class SpecialOrderSchema(BaseSchema):
    __tablename__ = "special_order"

    owner_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True
    )

    item_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    count: Mapped[int] = mapped_column(Integer, default=0)
    type: Mapped[SpecialOrderTypeEnum] = mapped_column(SpecialOrderTypeEnumSchema)

    __table_args__ = (CheckConstraint(count >= 0, "count_min"),)
