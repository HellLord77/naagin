from typing import Annotated
from typing import Optional

from fastapi import Cookie

from .utils import null_factory

PINKSIDCookie = Annotated[
    Optional[str], Cookie(default_factory=null_factory, alias="PINKSID")
]
