from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase

from .owner import OwnerSchema


class SwimsuitArrangeFlagSchema(SchemaBase):
    __tablename__ = "swimsuit_arrange_flag"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)
    girl_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    variation: Mapped[int] = mapped_column(Integer)
    switch: Mapped[int] = mapped_column(Integer)

    __table_args__ = (CheckConstraint(switch.between(0, 5), "switch_range"),)
