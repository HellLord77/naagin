from datetime import datetime
from typing import Any
from typing import ClassVar
from typing import Self
from typing import Unpack

from pydantic import BaseModel  # noqa: TID251
from pydantic import ConfigDict

from naagin import settings


class CustomBaseModel(BaseModel):
    model_map: ClassVar[dict[frozenset[tuple[str, Any]], set[type[Self]]]] = {}
    if settings.logging.duplicate_model:

        def __init_subclass__(cls, /, **kwargs: Unpack[ConfigDict]) -> None:
            annotations = frozenset(cls.__annotations__.items())
            if len(annotations) >= settings.logging.duplicate_model_length:
                models = cls.model_map.setdefault(annotations, set())
                models.add(cls)
            super().__init_subclass__(**kwargs)

    model_config = ConfigDict(
        from_attributes=True, json_encoders={datetime: lambda value: value.strftime("%Y-%m-%d %H:%M:%S")}
    )
