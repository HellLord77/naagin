from naagin.bases import ModelBase


class SubscriptionListModel(ModelBase):
    owner_fp: list[int]
    pass_details: list


class SubscriptionGetResponseModel(ModelBase):
    subscription_list: SubscriptionListModel
