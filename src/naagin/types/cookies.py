from typing import Annotated

from fastapi import Cookie


def default_factory():
    return None


PINKSIDCookie = Annotated[str, Cookie(default_factory=default_factory, alias="PINKSID")]
