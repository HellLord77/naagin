from typing import Self

from pydantic import model_validator

from naagin.bases import HARModelBase

from .param import ParamHARModel


class PostDataHARModel(HARModelBase):
    mime_type: str
    params: list[ParamHARModel] | None = None
    text: str | None = None

    @model_validator(mode="after")
    def validator(self) -> Self:
        if self.params is None and self.text is None:
            raise ValueError
        return self
