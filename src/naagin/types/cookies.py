from typing import Annotated
from typing import Optional

from fastapi import Cookie

from naagin.utils.default_factories import null_factory

PINKSIDCookie = Annotated[
    Optional[str], Cookie(default_factory=null_factory, alias="PINKSID")
]
