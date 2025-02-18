from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase

from .owner import OwnerSchema


class OwnerRoomSchema(SchemaBase):
    __tablename__ = "owner_room"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)
    main_girl_mid: Mapped[int] = mapped_column(Integer, default=0)
    sub_girl_mid: Mapped[int] = mapped_column(Integer, default=0)
    set_no: Mapped[int] = mapped_column(Integer, default=0)

    __table_args__ = (
        CheckConstraint(main_girl_mid != sub_girl_mid, "main_girl_mid_ne_sub_girl_mid"),
        CheckConstraint(set_no.between(0, 19), "set_no_range"),
    )
