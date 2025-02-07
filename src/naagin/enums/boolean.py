from enum import IntEnum
from typing import NoReturn


class BooleanEnum(IntEnum):
    FALSE = 0
    TRUE = 1

    def __bool__(self) -> NoReturn:
        raise NotImplementedError
