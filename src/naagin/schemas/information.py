from datetime import datetime
from typing import Literal

from sqlalchemy import Boolean
from sqlalchemy import CheckConstraint
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import UnicodeText
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase
from naagin.enums import InformationCategoryEnum

from .enums import InformationCategoryEnumSchema


class InformationSchema(SchemaBase):
    __tablename__ = "information"

    information_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(UnicodeText)
    description: Mapped[str] = mapped_column(Text)
    html_page_url: Mapped[str] = mapped_column(Text)
    category: Mapped[InformationCategoryEnum] = mapped_column(InformationCategoryEnumSchema)
    publish_at: Mapped[datetime] = mapped_column(DateTime, default=func.current_timestamp())
    close_at: Mapped[datetime] = mapped_column(DateTime)
    announce_at: Mapped[None] = mapped_column(DateTime, default=None)
    prohibit_popup: Mapped[Literal[False]] = mapped_column(Boolean, default=False)
    priority: Mapped[Literal[1]] = mapped_column(Integer, default=1)

    __table_args__ = (
        CheckConstraint(information_id >= 1, "information_id_min"),
        CheckConstraint(publish_at <= close_at, "publish_at_lte_close_at"),
        CheckConstraint(announce_at == None, "announce_at_const"),  # noqa: E711
        CheckConstraint(~prohibit_popup, "prohibit_popup_const"),
        CheckConstraint(priority == 1, "priority_const"),
    )
