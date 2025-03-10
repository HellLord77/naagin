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
from naagin.enums import ClearRankEnum

from .enums import ClearRankEnumSchema
from .owner import OwnerSchema


class QuestSchema(SchemaBase):
    __tablename__ = "quest"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)

    quest_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    quest_new: Mapped[bool] = mapped_column(Boolean, default=True)
    quest_clear: Mapped[bool] = mapped_column(Boolean, default=False)
    clear_rank: Mapped[ClearRankEnum] = mapped_column(ClearRankEnumSchema, default=ClearRankEnum.F)
    started_at: Mapped[datetime] = mapped_column(DateTime, default=func.current_timestamp())
    first_cleared_at: Mapped[datetime | None] = mapped_column(DateTime, default=None)
    srank_cleared_at: Mapped[datetime | None] = mapped_column(DateTime, default=None)
    arank_cleared_at: Mapped[datetime | None] = mapped_column(DateTime, default=None)

    __table_args__ = (
        CheckConstraint(~quest_clear | ~quest_new, "quest_clear_or_quest_new"),
        CheckConstraint(~quest_clear | (clear_rank != ClearRankEnum.F), "quest_clear_or_clear_rank"),
        # CheckConstraint(started_at <= first_cleared_at, "started_at_lte_first_cleared_at"),
        CheckConstraint(
            (clear_rank == ClearRankEnum.S) & (srank_cleared_at != None),  # noqa: E711
            "clear_rank_and_srank_cleared_at",
        ),
        # CheckConstraint(first_cleared_at <= srank_cleared_at, "first_cleared_at_lte_srank_cleared_at"),
        CheckConstraint(
            ((clear_rank == ClearRankEnum.A) | (clear_rank == ClearRankEnum.S)) & (arank_cleared_at != None),  # noqa: E711
            "clear_rank_and_arank_cleared_at",
        ),
        # CheckConstraint(first_cleared_at <= arank_cleared_at, "first_cleared_at_lte_arank_cleared_at"),
    )
