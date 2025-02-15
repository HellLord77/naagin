from typing import Literal

from naagin.bases import HARModelBase

from .browser import BrowserHARModel
from .creator import CreatorHARModel
from .entry import EntryHARModel
from .page import PageHARModel


class LogHARModel(HARModelBase):
    version: Literal["1.2"] = "1.2"
    creator: CreatorHARModel
    browser: BrowserHARModel | None = None
    pages: list[PageHARModel] | None = None
    entries: list[EntryHARModel]
