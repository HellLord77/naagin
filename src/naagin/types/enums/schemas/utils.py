from enum import IntEnum


def values_callable(enum: type[IntEnum]) -> tuple[str, ...]:
    return tuple(map(str, enum))
