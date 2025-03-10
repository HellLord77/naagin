from typing import Literal

from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase

from .owner import OwnerSchema


class VenusBoardGirlPanelSchema(SchemaBase):
    __tablename__ = "venus_board_girl_panel"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)

    content_mid: Mapped[Literal[1, 2]] = mapped_column(Integer)
    girl_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    panel_id: Mapped[int] = mapped_column(Integer, primary_key=True)

    __table_args__ = (CheckConstraint(content_mid.between(1, 2), "content_mid_const"),)
