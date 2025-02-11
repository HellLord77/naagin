from datetime import datetime
from typing import Any
from typing import ClassVar
from typing import Unpack

from pydantic import BaseModel
from pydantic import ConfigDict

from naagin import settings


class BaseModel(BaseModel):
    if settings.logging.duplicate_model:
        model_map: ClassVar[dict[frozenset[tuple[str, Any]], set[type[BaseModel]]]] = {}

        def __init_subclass__(cls, /, **kwargs: Unpack[ConfigDict]) -> None:
            annotations = frozenset(cls.__annotations__.items())
            if len(annotations) >= settings.logging.duplicate_model_length:
                models = cls.model_map.setdefault(annotations, set())
                models.add(cls)
            super().__init_subclass__(**kwargs)

    model_config = ConfigDict(
        from_attributes=True, json_encoders={datetime: lambda value: value.strftime("%Y-%m-%d %H:%M:%S")}
    )
