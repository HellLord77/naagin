from secrets import choice
from typing import Optional

from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import LargeBinary
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.utils.default_factories import access_token_factory
from naagin.utils.default_factories import pinksid_factory
from .base import BaseSchema
from .owner import OwnerSchema


def choices(population: str, *, k: int = 1) -> list[str]:
    return [choice(population) for _ in range(k)]


class SessionSchema(BaseSchema):
    __tablename__ = "session"

    owner_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True
    )
    access_token: Mapped[str] = mapped_column(
        String(32), default=access_token_factory, index=True
    )
    pinksid: Mapped[str] = mapped_column(
        String(26), default=pinksid_factory, index=True
    )
    session_key: Mapped[Optional[bytes]] = mapped_column(LargeBinary(32), default=None)

    __table_args__ = (
        CheckConstraint(func.char_length(access_token) == 32, "access_token_len"),
        CheckConstraint(func.char_length(pinksid) == 26, "pinksid_len"),
        CheckConstraint(func.octet_length(session_key) == 32, "session_key_len"),
    )
