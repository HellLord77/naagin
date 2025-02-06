from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.enums import ItemConsumeTypeEnum

from .base import BaseSchema
from .enums import ItemConsumeTypeEnumSchema
from .owner import OwnerSchema


class ItemConsumeSchema(BaseSchema):
    __tablename__ = "item_consume"

    owner_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True
    )
    item_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    count: Mapped[int] = mapped_column(Integer, default=0)
    type: Mapped[ItemConsumeTypeEnum] = mapped_column(ItemConsumeTypeEnumSchema)

    __table_args__ = (CheckConstraint(count >= 0, "count_min"),)
