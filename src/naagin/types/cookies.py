from typing import Annotated

from fastapi import Cookie

from naagin import factories

PINKSIDCookie = Annotated[str | None, Cookie(default_factory=factories.common.null_factory, alias="PINKSID")]
