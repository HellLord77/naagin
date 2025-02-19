from naagin.bases import ModelBase


class MaintenanceGetResponseModel(ModelBase):
    maintenance: bool
    maintenance_datetime: str | None = None
