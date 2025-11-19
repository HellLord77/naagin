from typing import Annotated
from typing import Literal

from fastapi import Header

from naagin import factories
from naagin.enums import ClientTypeEnum
from naagin.enums import EncodingEnum
from naagin.enums import MasterVersionEnum

UserAgentHeader = Annotated[str | None, Header(default_factory=factories.null_factory, alias="User-Agent")]
ContentTypeHeader = Annotated[str, Header(alias="Content-Type")]
ContentLengthHeader = Annotated[int | None, Header(default_factory=factories.null_factory, alias="Content-Length")]

AccessTokenHeader = Annotated[str, Header(alias="X-DOAXVV-Access-Token")]
ClientTypeHeader = Annotated[ClientTypeEnum, Header(alias="X-DOAXVV-ClientType")]
NonceHeader = Annotated[str, Header(alias="X-DOAXVV-Nonce")]

ApplicationVersionHeader = Annotated[
    int, Header(default_factory=factories.header.application_version_factory, alias="X-DOAXVV-ApplicationVersion")
]
MasterVersionHeader = Annotated[
    MasterVersionEnum, Header(default_factory=factories.header.master_version_factory, alias="X-DOAXVV-MasterVersion")
]
ResourceVersionHeader = Annotated[
    str, Header(default_factory=factories.header.resource_version_factory, alias="X-DOAXVV-ResourceVersion")
]

EncodingHeader = Annotated[
    Literal[EncodingEnum.DEFLATE] | None, Header(default_factory=factories.null_factory, alias="X-DOAXVV-Encoding")
]
EncryptedHeader = Annotated[str | None, Header(default_factory=factories.null_factory, alias="X-DOAXVV-Encrypted")]
