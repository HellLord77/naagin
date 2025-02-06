from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import BaseSchema
from .owner import OwnerSchema


class EpisodeSchema(BaseSchema):
    __tablename__ = "episode"

    owner_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True
    )
    episode_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    count: Mapped[int] = mapped_column(Integer, default=0)

    experience_gained: Mapped[bool] = mapped_column(Boolean, default=False)

    __table_args__ = (CheckConstraint(count >= 0, "count_min"),)
