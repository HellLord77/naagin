from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Index
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase
from naagin.enums import SceneEnum

from .enums import SceneEnumSchema
from .owner import OwnerSchema


class BgmSchema(SchemaBase):
    __tablename__ = "bgm"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)

    scene_mid: Mapped[SceneEnum] = mapped_column(SceneEnumSchema, primary_key=True)
    list_index: Mapped[int] = mapped_column(Integer, primary_key=True)
    bgm_mid: Mapped[int] = mapped_column(Integer, default=0)

    __table_args__ = (
        Index("owner_id_scene_mid_bgm_mid", owner_id, scene_mid, bgm_mid, postgresql_where=bgm_mid != 0),
        CheckConstraint(list_index.between(0, 48), "list_index_range"),
    )
