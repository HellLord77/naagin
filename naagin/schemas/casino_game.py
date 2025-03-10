from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase
from naagin.enums import CasinoGameEnum

from .enums import CasinoGameEnumSchema
from .owner import OwnerSchema


class CasinoGameSchema(SchemaBase):
    __tablename__ = "casino_game"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)

    game: Mapped[CasinoGameEnum] = mapped_column(CasinoGameEnumSchema, primary_key=True)
    play_count: Mapped[int] = mapped_column(Integer, default=0)
    win_count_total: Mapped[int] = mapped_column(Integer, default=0)
    win_count_series: Mapped[int] = mapped_column(Integer, default=0)
    win_count_series_max: Mapped[int] = mapped_column(Integer, default=0)

    __table_args__ = (
        CheckConstraint(play_count >= 0, "play_count_min"),
        CheckConstraint(win_count_total >= 0, "win_count_total_min"),
        CheckConstraint(win_count_series >= 0, "win_count_series_min"),
        CheckConstraint(win_count_series_max >= 0, "win_count_series_max_min"),
    )
