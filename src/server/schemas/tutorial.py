from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from . import NaaginBaseSchema
from . import OwnerSchema


class TutorialSchema(NaaginBaseSchema):
    __tablename__ = "tutorial"

    owner_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(OwnerSchema.owner_id, ondelete="CASCADE"), primary_key=True
    )
    event_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    flag: Mapped[int] = mapped_column(Integer, default=0)

    owner: Mapped[OwnerSchema] = relationship(OwnerSchema)

    __table_args__ = (CheckConstraint(flag >= 0, "flag_min"),)
