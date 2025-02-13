from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import CustomBaseSchema
from .owner import OwnerSchema


class YwrkSkillSchema(CustomBaseSchema):
    __tablename__ = "ywrk_skill"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), index=True)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    girl_mid: Mapped[int] = mapped_column(Integer)
    item_mid: Mapped[int] = mapped_column(Integer)
    skill_mid: Mapped[int] = mapped_column(Integer)
    value: Mapped[int] = mapped_column(Integer)
