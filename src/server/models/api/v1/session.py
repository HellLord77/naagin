from pydantic import BaseModel
from pydantic import ConfigDict


class SessionPostRequestModel(BaseModel):
    client_type: int
    environment: str
    is_first: int
    oauth_token: str
    oauth_token_secret: str
    onetime_token: str
    platform_id: str

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "client_type": 0,
                    "environment": "010000000011001",
                    "is_first": 1,
                    "oauth_token": "",
                    "oauth_token_secret": "",
                    "onetime_token": "140000009F7FBD7D19C1EA645804093C01001001D5E47C67180000000100000005000000072650F8299255E03D4C0F0007000000B200000032000000040000005804093C01001001349F0E0010EDD5673CEA15AC0000000067407A67E7EF9567010091C7040000000000488218A031A69110B1C29456289386F3F77209132B69CB62056E6DE6028E71569684EE268EA38CF4F357D47D44C3D9D06B82FBBF754F899494F20BDC9D0D24C8AF04CCD9ACB46100BC748B1438C05FE0025A09ED85450EC28E3E53B24D7FD5F8E708E92F850ED348D9905A2D01E93905E3396A0CF53FC33520D016B9D2D51FE9",
                    "platform_id": "76561198967489624",
                }
            ],
        }
    )


class SessionPostResponseModel(BaseModel):
    auth: bool
    owner_id: int
    owner_status: int

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"auth": True, "owner_id": 288696, "owner_status": 3}],
        }
    )
