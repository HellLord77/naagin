from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase

from .owner import OwnerSchema


class InformationReadSchema(SchemaBase):
    __tablename__ = "information_read"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)
    information_id: Mapped[int] = mapped_column(Integer, primary_key=True)
