from typing import Annotated

from fastapi import Header

from naagin.enums import ClientTypeEnum
from .utils import default_factory

AccessTokenHeader = Annotated[
    str, Header(default_factory=default_factory, alias="X-DOAXVV-Access-Token")
]
ApplicationVersionHeader = Annotated[int, Header(alias="X-DOAXVV-ApplicationVersion")]
ClientTypeHeader = Annotated[ClientTypeEnum, Header(alias="X-DOAXVV-ClientType")]
MasterVersionHeader = Annotated[int, Header(alias="X-DOAXVV-MasterVersion")]
