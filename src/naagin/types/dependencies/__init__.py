from typing import Annotated

from fastapi import Depends

from naagin.classes import CustomAsyncSession
from naagin.providers import provide_owner_id
from naagin.providers import provide_session

SessionDependency = Annotated[CustomAsyncSession, Depends(provide_session)]
OwnerIdDependency = Annotated[int, Depends(provide_owner_id)]
