from naagin.bases import ModelBase


class SubscriptionModel(ModelBase):
    owner_fp: list[int]
    pass_details: list


class SubscriptionGetResponseModel(ModelBase):
    subscription_list: SubscriptionModel
