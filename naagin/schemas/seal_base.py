from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase

from .owner import OwnerSchema


class SealBaseSchema(SchemaBase):
    __tablename__ = "seal_base"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)

    girl_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    main_base_mid: Mapped[int] = mapped_column(Integer)
    sub_base_mid: Mapped[int] = mapped_column(Integer)
