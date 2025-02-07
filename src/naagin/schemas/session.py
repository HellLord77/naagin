from secrets import choice

from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import LargeBinary
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import BaseSchema
from .owner import OwnerSchema
from .utils.factories import access_token_factory
from .utils.factories import pinksid_factory


def choices(population: str, *, k: int = 1) -> list[str]:
    return [choice(population) for _ in range(k)]


class SessionSchema(BaseSchema):
    __tablename__ = "session"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)
    access_token: Mapped[str] = mapped_column(String(32), default=access_token_factory, index=True)
    pinksid: Mapped[str] = mapped_column(String(26), default=pinksid_factory, index=True)
    session_key: Mapped[bytes | None] = mapped_column(LargeBinary(32), default=None)

    __table_args__ = (
        CheckConstraint(func.regexp_like(access_token, r"^[0-9a-f]{32}$"), "access_token_fmt"),
        CheckConstraint(func.regexp_like(pinksid, r"^[0-9a-z]{26}$"), "pinksid_fmt"),
        CheckConstraint(func.octet_length(session_key) == 32, "session_key_len"),  # noqa: PLR2004
    )
