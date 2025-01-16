from __future__ import annotations

from datetime import date
from datetime import datetime
from random import randrange
from typing import Literal
from typing import Optional

from sqlalchemy import CheckConstraint
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import NaaginBaseSchema
from ..types.enums import CheckedLicenseLevelEnum
from ..types.enums import LicenseLevelEnum
from ..types.enums import OwnerStatusEnum
from ..types.enums.schemas import CheckedLicenseLevelEnumSchema
from ..types.enums.schemas import LicenseLevelEnumSchema
from ..types.enums.schemas import OwnerStatusEnumSchema


class OwnerSchema(NaaginBaseSchema):
    __tablename__ = "owner"

    owner_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    status: Mapped[OwnerStatusEnum] = mapped_column(
        OwnerStatusEnumSchema, default=OwnerStatusEnum.CREATED
    )
    name: Mapped[Optional[str]] = mapped_column(String(12), default=None)
    island_name: Mapped[Optional[str]] = mapped_column(String(12), default=None)
    message: Mapped[Optional[str]] = mapped_column(String(20), default=None)
    team_id: Mapped[Literal[0]] = mapped_column(Integer, default=0)
    honor1_mid: Mapped[int] = mapped_column(Integer, default=0)
    honor2_mid: Mapped[int] = mapped_column(Integer, default=0)
    level: Mapped[int] = mapped_column(Integer, default=1)
    experience: Mapped[int] = mapped_column(Integer, default=0)
    stamina: Mapped[int] = mapped_column(Integer, default=30)
    main_girl_mid: Mapped[int] = mapped_column(Integer, default=0)
    lend_girl_mid: Mapped[int] = mapped_column(Integer, default=0)
    spot_mid: Mapped[int] = mapped_column(Integer, default=0)
    spot_phase_mid: Mapped[int] = mapped_column(Integer, default=0)
    license_point: Mapped[int] = mapped_column(Integer, default=0)
    license_level: Mapped[LicenseLevelEnum] = mapped_column(
        LicenseLevelEnumSchema, default=LicenseLevelEnum.F
    )
    checked_license_level: Mapped[CheckedLicenseLevelEnum] = mapped_column(
        CheckedLicenseLevelEnumSchema, default=CheckedLicenseLevelEnum.F
    )
    birthday: Mapped[Optional[date]] = mapped_column(Date, default=None)
    stamina_checked_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.current_timestamp()
    )
    last_logged_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.current_timestamp()
    )
    friend_code: Mapped[str] = mapped_column(
        String(11),
        default=lambda: f"{randrange(1000):03}-{randrange(1000):03}-{randrange(1000):03}",
        unique=True,
    )

    __table_args__ = (
        CheckConstraint(owner_id >= 1, "owner_id_min"),
        CheckConstraint(func.char_length(name).between(1, 12), "name_len_rng"),
        CheckConstraint(func.trim(name) == name, "name_trm"),
        CheckConstraint(
            func.char_length(island_name).between(1, 12), "island_name_len_rng"
        ),
        CheckConstraint(func.trim(island_name) == island_name, "island_name_trm"),
        CheckConstraint(func.char_length(message).between(1, 20), "message_len_rng"),
        CheckConstraint(func.trim(message) == message, "message_trm"),
        CheckConstraint(team_id == 0, "team_id_const"),
        CheckConstraint(level.between(1, 300), "level_rng"),
        CheckConstraint(experience >= 0, "experience_min"),
        CheckConstraint(stamina.between(0, 999), "stamina_rng"),
        CheckConstraint(license_point.between(0, 12480), "license_point_rng"),
        CheckConstraint(
            func.cast(func.cast(license_level, String), Integer)
            >= func.cast(func.cast(checked_license_level, String), Integer),
            "license_level_gte_checked_license_level",
        ),
        CheckConstraint(birthday <= func.current_date(), "birthday_lte_today"),
        CheckConstraint(
            stamina_checked_at <= func.current_timestamp(), "stamina_checked_at_lte_now"
        ),
        CheckConstraint(
            last_logged_at <= func.current_timestamp(), "last_logged_at_lte_now"
        ),
        CheckConstraint(
            stamina_checked_at >= last_logged_at,
            "stamina_checked_at_gte_last_logged_at",
        ),
        CheckConstraint(
            func.regexp_like(friend_code, r"^\d{3}-\d{3}-\d{3}$"), "friend_code_fmt"
        ),
    )
