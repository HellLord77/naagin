from naagin.bases import HARModelBase


class TimingsHARModel(HARModelBase):
    blocked: float | None = -1
    dns: float | None = -1
    connect: float | None = -1
    send: float
    wait: float
    receive: float
    ssl: float | None = -1
