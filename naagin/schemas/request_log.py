from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase
from naagin.enums import RequestClearRankEnum

from .enums import RequestClearRankEnumSchema
from .owner import OwnerSchema


class RequestLogSchema(SchemaBase):
    __tablename__ = "request_log"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)

    request_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    clear_rank: Mapped[RequestClearRankEnum] = mapped_column(RequestClearRankEnumSchema)
