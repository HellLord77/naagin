from typing import Literal

from sqlalchemy import Boolean
from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase
from naagin.enums import ItemEquipmentTypeEnum

from .enums import ItemEquipmentTypeEnumSchema
from .owner import OwnerSchema


class ItemEquipmentSchema(SchemaBase):
    __tablename__ = "item_equipment"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), index=True)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    item_mid: Mapped[int] = mapped_column(Integer)
    type: Mapped[ItemEquipmentTypeEnum] = mapped_column(ItemEquipmentTypeEnumSchema)
    level: Mapped[int] = mapped_column(Integer, default=1)
    experience: Mapped[int] = mapped_column(Integer, default=0)
    girl_mid: Mapped[int] = mapped_column(Integer, default=0)
    favorite: Mapped[Literal[False]] = mapped_column(Boolean, default=False)
    in_lock: Mapped[bool] = mapped_column(Boolean, default=False)
    unlock_count: Mapped[int] = mapped_column(Integer, default=0)
    upgrade_count: Mapped[int] = mapped_column(Integer, default=0)
    combine_count: Mapped[int] = mapped_column(Integer, default=0)

    __table_args__ = (
        CheckConstraint(id >= 1, "id_min"),
        CheckConstraint(type != ItemEquipmentTypeEnum.HAIRSTYLE_OR_EXPRESSION, "type_const"),
        CheckConstraint(level.between(1, 90), "level_range"),
        CheckConstraint(experience.between(0, 480000), "experience_range"),
        CheckConstraint(favorite == False, "favorite_const"),  # noqa: E712
        CheckConstraint(unlock_count.between(0, 4), "unlock_count_range"),
        CheckConstraint(upgrade_count >= 0, "upgrade_count_min"),
        CheckConstraint(combine_count.between(0, 4), "combine_count_range"),
    )
