from typing import Annotated

from fastapi import Depends
from fastapi.security import APIKeyCookie
from fastapi.security import APIKeyHeader

HeaderSecurity = Annotated[str | None, Depends(APIKeyHeader(name="X-DOAXVV-Access-Token", auto_error=False))]
CookieSecurity = Annotated[str | None, Depends(APIKeyCookie(name="PINKSID", auto_error=False))]
