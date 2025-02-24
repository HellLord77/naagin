from datetime import datetime
from typing import Literal

from pydantic_xml import attr

from ..bases import ModelBase  # noqa: TID252


class DirectoryModel(ModelBase, tag="directory"):
    name: str
    type: Literal["directory"] = "directory"
    mtime: datetime = attr()
