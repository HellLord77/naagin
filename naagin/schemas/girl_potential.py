from sqlalchemy import Boolean
from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase

from .girl_equipment import ItemEquipmentSchema
from .owner import OwnerSchema


class GirlPotentialSchema(SchemaBase):
    __tablename__ = "girl_potential"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)
    girl_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    skill_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    polishing_count: Mapped[int] = mapped_column(Integer, default=0)
    is_favorite: Mapped[bool] = mapped_column(Boolean, default=False)
    equipment_id: Mapped[int] = mapped_column(Integer, ForeignKey(ItemEquipmentSchema.id), default=0)
    pvp_equipment_id: Mapped[int] = mapped_column(Integer, ForeignKey(ItemEquipmentSchema.id), default=0)

    __table_args__ = (CheckConstraint(polishing_count >= 0, "polishing_count_min"),)
