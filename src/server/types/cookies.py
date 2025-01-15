from typing import Annotated

from fastapi import Cookie

PINKSIDCookie = Annotated[str, Cookie(alias="PINKSID")]
