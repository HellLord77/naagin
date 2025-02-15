from pydantic import ConfigDict
from pydantic.alias_generators import to_camel

from . import ModelBase


class HARModelBase(ModelBase):
    comment: str | None = None

    model_config = ConfigDict(alias_generator=to_camel)
