from functools import wraps

from fastapi import Request
from orjson import loads

from naagin.types_ import JSONDecodeType


@wraps(Request.json)
async def json(self: Request) -> JSONDecodeType:
    if not hasattr(self, "_json"):
        body = await self.body()
        self._json = loads(body)
    return self._json


def attach() -> None:
    Request.json = json
