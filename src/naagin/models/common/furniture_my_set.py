from naagin.models.base import CustomBaseModel


class FurnitureMySetModel(CustomBaseModel):
    id: int
    item_mid: int
    layout_mid: int
    rot_y: int
