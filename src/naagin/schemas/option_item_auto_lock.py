from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase

from .owner import OwnerSchema


class OptionItemAutoLockSchema(SchemaBase):
    __tablename__ = "option_item_auto_lock"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)
    option_lock_only: Mapped[bool] = mapped_column(Boolean, default=True)
    option_lock_sr: Mapped[bool] = mapped_column(Boolean, default=True)
    option_lock_ssr: Mapped[bool] = mapped_column(Boolean, default=True)
