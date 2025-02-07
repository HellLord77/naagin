from typing import Annotated

from fastapi import Cookie

from .utils import null_factory

PINKSIDCookie = Annotated[str | None, Cookie(default_factory=null_factory, alias="PINKSID")]
