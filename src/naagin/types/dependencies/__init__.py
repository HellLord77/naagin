from typing import Annotated

from fastapi import Depends

from naagin.classes import AsyncSession
from naagin.providers import provide_maintenance
from naagin.providers import provide_owner_id
from naagin.providers import provide_session
from naagin.providers import provide_session_
from naagin.schemas import MaintenanceSchema
from naagin.schemas import SessionSchema

SessionDependency = Annotated[AsyncSession, Depends(provide_session)]
MaintenanceDependency = Annotated[MaintenanceSchema | None, Depends(provide_maintenance)]
SessionDependency_ = Annotated[SessionSchema, Depends(provide_session_)]
OwnerIdDependency = Annotated[int, Depends(provide_owner_id)]
