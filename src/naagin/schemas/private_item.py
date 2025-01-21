from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.types.enums import BooleanEnum
from naagin.types.enums import PrivateItemTypeEnum
from naagin.types.enums.schemas import BooleanEnumSchema
from naagin.types.enums.schemas import PrivateItemTypeEnumSchema
from .base import BaseSchema
from .owner import OwnerSchema


class PrivateItemSchema(BaseSchema):
    __tablename__ = "private_item"

    owner_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True
    )

    girl_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[PrivateItemTypeEnum] = mapped_column(PrivateItemTypeEnumSchema)
    item_mid: Mapped[int] = mapped_column(Integer, primary_key=True)

    is_favorite: Mapped[BooleanEnum] = mapped_column(
        BooleanEnumSchema, default=BooleanEnum.FALSE
    )

    __table_args__ = (
        # CheckConstraint(
        #     select(PrivateItemSchema)
        #     .where(
        #         owner_id == PrivateItemSchema.owner_id,
        #         girl_mid == PrivateItemSchema.girl_mid,
        #     )
        #     .count()
        #     <= 100,
        #     "private_item_count_max",
        # ),
    )
