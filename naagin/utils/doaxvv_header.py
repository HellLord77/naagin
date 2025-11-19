from typing import Self
from typing import override


class DOAXVVHeader(str):
    __slots__ = ()

    @override
    def lower(self) -> Self:
        return self
