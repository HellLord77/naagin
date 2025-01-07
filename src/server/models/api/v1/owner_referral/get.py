from pydantic import BaseModel
from pydantic import ConfigDict


class OwnerReferralModel(BaseModel):
    referral_id: str


class OwnerReferralGetGetResponseModel(BaseModel):
    owner_referral: OwnerReferralModel

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"owner_referral": {"referral_id": "-1"}}],
        }
    )
