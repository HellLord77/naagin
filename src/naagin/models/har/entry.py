from datetime import datetime
from typing import Self

from pydantic import model_validator

from naagin.bases import HARModelBase

from .cache import CacheHARModel
from .request import RequestHARModel
from .response import ResponseHARModel
from .timings import TimingsHARModel


class EntryHARModel(HARModelBase):
    pageref: str | None = None
    started_date_time: datetime
    time: float | None = 0
    request: RequestHARModel
    response: ResponseHARModel
    cache: CacheHARModel
    timings: TimingsHARModel
    server_ip_address: str | None = None
    connection: str | None = None

    @model_validator(mode="after")
    def validator(self) -> Self:
        blocked = 0 if self.timings.blocked == -1 else self.timings.blocked
        dns = 0 if self.timings.dns == -1 else self.timings.dns
        connect = 0 if self.timings.connect == -1 else self.timings.connect

        if (
            self.time
            != blocked + dns + connect + self.timings.send + self.timings.wait + self.timings.receive + self.timings.ssl
        ):
            raise ValueError
        return self
