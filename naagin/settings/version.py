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
        int | None, Field(validation_alias=AliasChoices("application_global", "application"), exclude=True)
    ] = None
    resource_global: Annotated[
        tuple[int, int, int] | None, Field(validation_alias=AliasChoices("resource_global", "resource"), exclude=True)
    ] = None

    master_japan: Annotated[
        Literal[MasterVersionEnum.JAPAN],
        Field(validation_alias=AliasChoices("master_japan", "master_jp"), exclude=True),
    ] = MasterVersionEnum.JAPAN
    application_japan: Annotated[
        int | None, Field(validation_alias=AliasChoices("application_japan", "application_jp"), exclude=True)
    ] = None
    resource_japan: Annotated[
        tuple[int, int, int] | None, Field(validation_alias=AliasChoices("resource_japan", "resource_jp"), exclude=True)
    ] = None

    strict: bool = True
    japan: bool = False

    @computed_field
    @cached_property
    def master(self) -> MasterVersionEnum:
        return self.master_japan if self.japan else self.master_global

    @computed_field
    @cached_property
    def application(self) -> int | None:
        return self.application_japan if self.japan else self.application_global

    @computed_field
    @cached_property
    def resource(self) -> tuple[int, int, int] | None:
        return self.resource_japan if self.japan else self.resource_global
