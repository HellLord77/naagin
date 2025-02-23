from datetime import datetime
from typing import Literal

from naagin.bases import AutoIndexModelBase


class DirectoryAutoIndexModel(AutoIndexModelBase):
    name: str
    type: Literal["directory"] = "directory"
    mtime: datetime
