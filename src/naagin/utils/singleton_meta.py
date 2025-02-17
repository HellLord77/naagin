from typing import ClassVar
from typing import Self
from typing import override


class SingletonMeta(type):
    _instances: ClassVar[dict[type[Self], Self]] = {}

    @override
    def __call__(
        cls,
        *args,  # noqa: ANN002
        **kwargs,  # noqa: ANN003
    ) -> Self:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
