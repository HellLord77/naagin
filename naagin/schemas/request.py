from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import CheckConstraint
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase

from .owner import OwnerSchema


class RequestSchema(SchemaBase):
    __tablename__ = "request"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)
    request_mid: Mapped[int] = mapped_column(Integer, default=0)
    girl_mid1: Mapped[int] = mapped_column(Integer, default=0)
    girl_mid2: Mapped[int] = mapped_column(Integer, default=0)
    trend_status: Mapped[bool] = mapped_column(Boolean, default=False)
    started_at: Mapped[datetime | None] = mapped_column(DateTime, default=None)
    end_at: Mapped[datetime | None] = mapped_column(DateTime, default=None)

    __table_args__ = (
        CheckConstraint(started_at <= func.current_timestamp(), name="started_at_lte_now"),
        CheckConstraint(end_at >= func.current_timestamp(), name="end_at_gte_now"),
        CheckConstraint(started_at <= end_at, name="started_at_lte_end_at"),
    )
