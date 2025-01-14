from pydantic import BaseModel


class MaintenancePrivilegeCheckGetResponseModel(BaseModel):
    result: str
