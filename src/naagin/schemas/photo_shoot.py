from datetime import date

from sqlalchemy import Boolean
from sqlalchemy import CheckConstraint
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase

from .owner import OwnerSchema


class PhotoShootSchema(SchemaBase):
    __tablename__ = "photo_shoot"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)
    shoot: Mapped[bool] = mapped_column(Boolean, default=False)
    recover: Mapped[bool] = mapped_column(Boolean, default=False)
    last_today: Mapped[date] = mapped_column(Date, default=func.current_date())

    __table_args__ = (
        CheckConstraint(recover == False or shoot == True, "recover_or_shoot"),  # noqa: E712
        # CheckConstraint(last_today <= updated_at, "checked_at_lte_updated_at"),
    )
