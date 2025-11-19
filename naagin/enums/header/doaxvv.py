from enum import StrEnum


class DOAXVVHeaderEnum(StrEnum):
    NONCE = "X-DOAXVV-Nonce"
    CLIENT_TYPE = "X-DOAXVV-ClientType"

    SERVER_TIME = "X-DOAXVV-ServerTime"
    ACCESS_TOKEN = "X-DOAXVV-Access-Token"  # noqa: S105
    STATUS = "X-DOAXVV-Status"

    APPLICATION_VERSION = "X-DOAXVV-ApplicationVersion"
    MASTER_VERSION = "X-DOAXVV-MasterVersion"
    RESOURCE_VERSION = "X-DOAXVV-ResourceVersion"

    ENCODING = "X-DOAXVV-Encoding"
    ENCRYPTED = "X-DOAXVV-Encrypted"
