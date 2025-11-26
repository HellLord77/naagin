from functools import cached_property
from typing import Annotated
from typing import Literal

from pydantic import AliasChoices
from pydantic import Field
from pydantic import computed_field

from naagin.bases import SettingsBase
from naagin.enums import MasterVersionEnum


class VersionSettings(SettingsBase):
    master_global: Annotated[
        Literal[MasterVersionEnum.GLOBAL], Field(validation_alias=AliasChoices("master_global", "master"), exclude=True)
    ] = MasterVersionEnum.GLOBAL
    application_global: Annotated[
        int, Field(validation_alias=AliasChoices("application_global", "application"), exclude=True)
    ] = 73400
    resource_global: Annotated[
        tuple[int, int, int], Field(validation_alias=AliasChoices("resource_global", "resource"), exclude=True)
    ] = 73400, 73400, 73400

    master_japan: Annotated[
        Literal[MasterVersionEnum.JAPAN],
        Field(validation_alias=AliasChoices("master_japan", "master_jp"), exclude=True),
    ] = MasterVersionEnum.JAPAN
    application_japan: Annotated[
        int, Field(validation_alias=AliasChoices("application_japan", "application_jp"), exclude=True)
    ] = 90100
    resource_japan: Annotated[
        tuple[int, int, int], Field(validation_alias=AliasChoices("resource_japan", "resource_jp"), exclude=True)
    ] = 90100, 84600, 90100

    strict: bool = True
    japan: bool = False

    @computed_field
    @cached_property
    def master(self) -> MasterVersionEnum:
        return self.master_japan if self.japan else self.master_global

    @computed_field
    @cached_property
    def application(self) -> int:
        return self.application_japan if self.japan else self.application_global

    @computed_field
    @cached_property
    def resource(self) -> str:
        return ",".join(map(str, self.resource_japan if self.japan else self.resource_global))
