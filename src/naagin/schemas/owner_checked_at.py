from datetime import datetime

from sqlalchemy import CheckConstraint
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase

from .owner import OwnerSchema


class OwnerCheckedAtSchema(SchemaBase):
    __tablename__ = "owner_checked_at"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)
    news_checked_at: Mapped[datetime] = mapped_column(DateTime, default=func.current_timestamp())
    quest_checked_at: Mapped[datetime] = mapped_column(DateTime, default=func.current_timestamp())
    event_checked_at: Mapped[datetime] = mapped_column(DateTime, default=func.current_timestamp())
    reward_notification_checked_at: Mapped[datetime] = mapped_column(DateTime, default=func.current_timestamp())
    notification_checked_at: Mapped[datetime] = mapped_column(DateTime, default=func.current_timestamp())
    giftbox_checked_at: Mapped[datetime] = mapped_column(DateTime, default=func.current_timestamp())
    shared_giftbox_checked_at: Mapped[datetime] = mapped_column(DateTime, default=func.current_timestamp())
    friendship_checked_at: Mapped[datetime] = mapped_column(DateTime, default=func.current_timestamp())
    honor_checked_at: Mapped[datetime] = mapped_column(DateTime, default=func.current_timestamp())
    mission_checked_at: Mapped[datetime] = mapped_column(DateTime, default=func.current_timestamp())
    shared_login_bonus_checked_at: Mapped[datetime | None] = mapped_column(DateTime, default=None)
    subscription_checked_at: Mapped[datetime | None] = mapped_column(DateTime, default=None)
    lesson2onsen_exchanged_item_at: Mapped[datetime | None] = mapped_column(DateTime, default=None)
    comeback_login_bonus_expire_at: Mapped[None] = mapped_column(DateTime, default=None)
    compensation_create_girl_append_item_at: Mapped[None] = mapped_column(DateTime, default=None)

    __table_args__ = (
        # CheckConstraint(news_checked_at == created_at, "news_checked_at_eq_created_at"),
        # CheckConstraint(quest_checked_at == created_at, "quest_checked_at_eq_created_at"),
        # CheckConstraint(event_checked_at == created_at, "event_checked_at_eq_created_at"),
        # CheckConstraint(reward_notification_checked_at == created_at, "reward_notification_checked_at_eq_created_at"),
        # CheckConstraint(notification_checked_at == created_at, "notification_checked_at_eq_created_at"),
        # CheckConstraint(giftbox_checked_at == created_at, "giftbox_checked_at_eq_created_at"),
        # CheckConstraint(shared_giftbox_checked_at <= updated_at, "shared_giftbox_checked_at_lte_updated_at"),
        # CheckConstraint(friendship_checked_at <= updated_at, "friendship_checked_at_lte_updated_at"),
        # CheckConstraint(honor_checked_at <= updated_at, "honor_checked_at_lte_updated_at"),
        # CheckConstraint(mission_checked_at <= updated_at, "mission_checked_at_lte_updated_at"),
        # CheckConstraint(shared_login_bonus_checked_at <= updated_at, "shared_login_bonus_checked_at_lte_updated_at"),
        # CheckConstraint(subscription_checked_at <= updated_at, "subscription_checked_at_lte_updated_at"),
        # CheckConstraint(
        #     lesson2onsen_exchanged_item_at <= updated_at, "lesson2onsen_exchanged_item_at_lte_updated_at"
        # ),
        CheckConstraint(comeback_login_bonus_expire_at == None, "comeback_login_bonus_expire_at_const"),  # noqa: E711
        CheckConstraint(
            compensation_create_girl_append_item_at == None,  # noqa: E711
            "compensation_create_girl_append_item_at_const",
        ),
    )
