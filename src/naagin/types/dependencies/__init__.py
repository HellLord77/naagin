from typing import Annotated

from fastapi import Depends

from naagin.classes import AsyncSession
from naagin.providers import provide_owner_id
from naagin.providers import provide_session

SessionDependency = Annotated[AsyncSession, Depends(provide_session)]
OwnerIdDependency = Annotated[int, Depends(provide_owner_id)]
