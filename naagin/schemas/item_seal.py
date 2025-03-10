from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase
from naagin.enums import SealRarityEnum

from .enums import SealRarityEnumSchema
from .owner import OwnerSchema


class ItemSealSchema(SchemaBase):
    __tablename__ = "item_seal"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), index=True)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    item_mid: Mapped[int] = mapped_column(Integer)
    type: Mapped[int] = mapped_column(Integer)
    base_mid: Mapped[int] = mapped_column(Integer)
    pvp_base_mid: Mapped[int] = mapped_column(Integer)
    in_lock: Mapped[bool] = mapped_column(Boolean, default=False)
    skill_level: Mapped[int] = mapped_column(Integer, default=1)
    cost: Mapped[int] = mapped_column(Integer)
    rarity: Mapped[SealRarityEnum] = mapped_column(SealRarityEnumSchema)
    experience: Mapped[int] = mapped_column(Integer, default=0)
