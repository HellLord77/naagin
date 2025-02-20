from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase

from .owner import OwnerSchema


class OwnerCountLoginSchema(SchemaBase):
    __tablename__ = "owner_count_login"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)
    value: Mapped[int] = mapped_column(Integer, default=1)

    __table_args__ = (CheckConstraint(value >= 1, "value_min"),)
