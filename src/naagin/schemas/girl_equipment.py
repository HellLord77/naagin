from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import BaseSchema
from .item_equipemnt import ItemEquipmentSchema
from .owner import OwnerSchema


class GirlEquipmentSchema(BaseSchema):
    __tablename__ = "girl_equipment"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)
    girl_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    swimsuit_equipment_item_id: Mapped[int] = mapped_column(Integer, ForeignKey(ItemEquipmentSchema.id), default=0)
    accessory_head_equipment_item_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(ItemEquipmentSchema.id),
        default=0,
    )
    accessory_face_equipment_item_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(ItemEquipmentSchema.id),
        default=0,
    )
    accessory_arm_equipment_item_id: Mapped[int] = mapped_column(Integer, ForeignKey(ItemEquipmentSchema.id), default=0)
