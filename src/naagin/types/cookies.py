from typing import Annotated

from fastapi import Cookie

from naagin.utils.default_factories import null_factory

PINKSIDCookie = Annotated[str, Cookie(default_factory=null_factory, alias="PINKSID")]
