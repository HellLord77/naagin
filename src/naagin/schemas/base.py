from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import MetaData
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class BaseSchema(DeclarativeBase):
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        },
    )

    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.current_timestamp())
    updated_at: Mapped[datetime | None] = mapped_column(DateTime, default=None, onupdate=func.current_timestamp())

    # __table_args__ = (
    #     CheckConstraint(created_at <= func.current_timestamp(), "created_at_lte_now"),
    #     CheckConstraint(updated_at <= func.current_timestamp(), "updated_at_lte_now"),
    #     CheckConstraint(created_at <= updated_at, "created_at_lte_updated_at"),
    # )
