from typing import ClassVar


class BaseException(Exception):
    code: ClassVar[int]
    message: ClassVar[str]
