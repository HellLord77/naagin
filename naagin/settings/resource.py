from functools import cached_property
from typing import Annotated
from typing import Literal

from httpx import AsyncClient
from pydantic import AliasChoices
from pydantic import AnyHttpUrl
from pydantic import Field
from pydantic import computed_field

from naagin.bases import SettingsBase
from naagin.enums import URISchemeEnum
from naagin.types_.fields import PortField


class ResourceSettings(SettingsBase):
    offline_mode: Annotated[bool, Field(validation_alias=AliasChoices("offline_mode", "off"))] = True

    scheme: Annotated[
        Literal[URISchemeEnum.HTTP, URISchemeEnum.HTTPS],
        Field(validation_alias=AliasChoices("scheme", "protocol"), exclude=True),
    ] = URISchemeEnum.HTTPS
    host: Annotated[str, Field(validation_alias=AliasChoices("host", "hostname"), exclude=True)]
    port: Annotated[PortField | None, Field(exclude=True)] = None
    path: Annotated[str | None, Field(exclude=True)] = None
    base_url: Annotated[AnyHttpUrl | None, Field(validation_alias=AliasChoices("base_url", "url"), exclude=True)] = None

    user_agent: Annotated[str, Field(validation_alias=AliasChoices("user_agent", "ua"))] = (
        "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko"
    )

    @computed_field
    @cached_property
    def url(self) -> AnyHttpUrl:
        if self.base_url is None:
            return AnyHttpUrl.build(scheme=self.scheme, host=self.host, port=self.port, path=self.path)

        return self.base_url

    @cached_property
    def client(self) -> AsyncClient:
        return AsyncClient(headers={"User-Agent": self.user_agent}, base_url=str(self.url))
