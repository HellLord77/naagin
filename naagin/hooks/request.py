from functools import wraps

from fastapi import Request

from naagin.imports import json
from naagin.types_ import JSONDecodeType


@wraps(Request.json)
async def request_json(self: Request) -> JSONDecodeType:
    if not hasattr(self, "_json"):
        body = await self.body()
        self._json = json.loads(body)
    return self._json


def attach() -> None:
    Request.json = request_json
