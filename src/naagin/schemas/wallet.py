from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import BaseSchema
from .owner import OwnerSchema


class WalletSchema(BaseSchema):
    __tablename__ = "wallet"

    owner_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True
    )
    zack_money: Mapped[int] = mapped_column(Integer, default=0)
    guest_point: Mapped[int] = mapped_column(Integer, default=0)
    vip_point: Mapped[int] = mapped_column(Integer, default=0)
    paid_vstone: Mapped[int] = mapped_column(Integer, default=0)
    free_vstone: Mapped[int] = mapped_column(Integer, default=0)
    vip_coin: Mapped[int] = mapped_column(Integer, default=0)

    __table_args__ = (
        CheckConstraint(zack_money >= 0, "zack_money_min"),
        CheckConstraint(guest_point >= 0, "guest_point_min"),
        CheckConstraint(vip_point >= 0, "vip_point_min"),
        CheckConstraint(paid_vstone >= 0, "paid_vstone_min"),
        CheckConstraint(free_vstone >= 0, "free_vstone_min"),
        CheckConstraint(vip_coin >= 0, "vip_coin_min"),
    )
