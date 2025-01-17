from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import CheckConstraint
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.types.enums import FriendshipStateEnum
from naagin.types.enums.schemas import FriendshipStateEnumSchema
from .base import BaseSchema
from .owner import OwnerSchema


class FriendshipSchema(BaseSchema):
    __tablename__ = "friendship"

    owner_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True
    )
    friend_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True
    )
    state: Mapped[FriendshipStateEnum] = mapped_column(FriendshipStateEnumSchema)
    invited: Mapped[bool] = mapped_column(Boolean, default=False)
    sent_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.current_timestamp()
    )

    __table_args__ = (  # TODO MAX sent per owner_id <= 150
        CheckConstraint(sent_at <= func.current_timestamp(), "sent_at_lte_now"),
    )
