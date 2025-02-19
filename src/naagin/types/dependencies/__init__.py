from typing import Annotated

from fastapi import Depends

from naagin.classes import AsyncSession
from naagin.providers import provide_database
from naagin.providers import provide_maintenance
from naagin.providers import provide_owner_id
from naagin.providers import provide_session
from naagin.schemas import MaintenanceSchema
from naagin.schemas import SessionSchema

DatabaseDependency = Annotated[AsyncSession, Depends(provide_database)]
MaintenanceDependency = Annotated[MaintenanceSchema | None, Depends(provide_maintenance)]
SessionDependency = Annotated[SessionSchema, Depends(provide_session)]
OwnerIdDependency = Annotated[int, Depends(provide_owner_id)]
