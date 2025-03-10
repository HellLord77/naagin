from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase

from .owner import OwnerSchema


class TutorialSchema(SchemaBase):
    __tablename__ = "tutorial"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)
    event_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    flag: Mapped[int] = mapped_column(Integer, default=0)

    __table_args__ = (CheckConstraint(flag >= 0, "flag_min"),)
