from datetime import datetime
from typing import Literal

from naagin.bases import AutoIndexModelBase


class FileAutoIndexModel(AutoIndexModelBase):
    name: str
    type: Literal["file"] = "file"
    mtime: datetime
    size: int
