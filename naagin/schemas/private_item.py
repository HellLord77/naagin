from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase
from naagin.enums import PrivateItemTypeEnum

from .enums import PrivateItemTypeEnumSchema
from .owner import OwnerSchema


class PrivateItemSchema(SchemaBase):
    __tablename__ = "private_item"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)

    girl_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[PrivateItemTypeEnum] = mapped_column(PrivateItemTypeEnumSchema)
    item_mid: Mapped[int] = mapped_column(Integer, primary_key=True)

    favorite: Mapped[bool] = mapped_column(Boolean, default=False)

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
