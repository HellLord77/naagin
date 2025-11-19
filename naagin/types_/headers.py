from typing import Annotated
from typing import Literal

from fastapi import Header

from naagin import factories
from naagin.enums import ClientTypeEnum
from naagin.enums import DOAXVVHeaderEnum
from naagin.enums import EncodingEnum
from naagin.enums import HeaderEnum
from naagin.enums import MasterVersionEnum

UserAgentHeader = Annotated[str | None, Header(default_factory=factories.null_factory, alias=HeaderEnum.USER_AGENT)]

ContentLengthHeader = Annotated[
    int | None, Header(default_factory=factories.null_factory, alias=HeaderEnum.CONTENT_LENGTH)
]
ContentTypeHeader = Annotated[str, Header(alias=HeaderEnum.CONTENT_TYPE)]

AccessTokenHeader = Annotated[str, Header(alias=DOAXVVHeaderEnum.ACCESS_TOKEN)]
ClientTypeHeader = Annotated[ClientTypeEnum, Header(alias=DOAXVVHeaderEnum.CLIENT_TYPE)]
NonceHeader = Annotated[str, Header(alias=DOAXVVHeaderEnum.NONCE)]

ApplicationVersionHeader = Annotated[
    int,
    Header(default_factory=factories.header.application_version_factory, alias=DOAXVVHeaderEnum.APPLICATION_VERSION),
]
MasterVersionHeader = Annotated[
    MasterVersionEnum,
    Header(default_factory=factories.header.master_version_factory, alias=DOAXVVHeaderEnum.MASTER_VERSION),
]
ResourceVersionHeader = Annotated[
    str, Header(default_factory=factories.header.resource_version_factory, alias=DOAXVVHeaderEnum.RESOURCE_VERSION)
]

EncodingHeader = Annotated[
    Literal[EncodingEnum.DEFLATE] | None,
    Header(default_factory=factories.null_factory, alias=DOAXVVHeaderEnum.ENCODING),
]
EncryptedHeader = Annotated[
    str | None, Header(default_factory=factories.null_factory, alias=DOAXVVHeaderEnum.ENCRYPTED)
]
