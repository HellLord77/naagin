from enum import IntEnum


class BooleanEnum(IntEnum):
    FALSE = 0
    TRUE = 1

    def __bool__(self):
        raise NotImplementedError
