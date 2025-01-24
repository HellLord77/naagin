from typing import Annotated

from fastapi import Cookie

from .utils import default_factory

PINKSIDCookie = Annotated[str, Cookie(default_factory=default_factory, alias="PINKSID")]
