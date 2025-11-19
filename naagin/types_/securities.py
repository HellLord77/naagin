from typing import Annotated

from fastapi import Depends
from fastapi.security import APIKeyCookie
from fastapi.security import APIKeyHeader

from naagin.enums import DOAXVVHeaderEnum

HeaderSecurity = Annotated[str | None, Depends(APIKeyHeader(name=DOAXVVHeaderEnum.ACCESS_TOKEN, auto_error=False))]
CookieSecurity = Annotated[str | None, Depends(APIKeyCookie(name="PINKSID", auto_error=False))]
