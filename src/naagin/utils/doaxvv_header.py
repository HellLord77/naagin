from typing import Any
from typing import Self

from fastapi import Response


class DOAXVVHeader(str):
    __slots__ = ()

    def __new__(cls, alias: str) -> Self:
        return super().__new__(cls, f"X-DOAXVV-{alias}")

    def lower(self) -> Self:
        return self

    @classmethod
    def set(
        cls,
        response: Response,
        key: str,
        value: Any,  # noqa: ANN401
    ) -> None:
        self = cls(key)
        response.headers[self] = str(value)
