from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase

from .owner import OwnerSchema


class Pyon2RunSchema(SchemaBase):
    __tablename__ = "pyon2_run"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)
    girl_mid: Mapped[int] = mapped_column(Integer, default=0)
    stage_mid: Mapped[int] = mapped_column(Integer, default=0)
    lane_id: Mapped[int] = mapped_column(Integer, default=0)
    pos_id: Mapped[int] = mapped_column(Integer, default=0)
