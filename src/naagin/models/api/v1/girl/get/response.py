from datetime import datetime

from naagin.models.base import CustomBaseModel


class GirlModel(CustomBaseModel):
    owner_id: int
    girl_mid: int
    mood: int
    experience: int
    level: int
    power: int
    additional_power: int
    technic: int
    additional_technic: int
    stamina: int
    additional_stamina: int
    appeal: int
    appeal_up: int
    additional_appeal: int
    hair_item_mid: int
    ring_item_mid: int
    addition_accessory_item_mid: int
    swimsuit_item_mid: int
    accessory_head_item_mid: int
    accessory_face_item_mid: int
    accessory_arm_item_mid: int
    visual_state_flag_a: int
    visual_state_flag_b: int
    visual_state_flag_c: int
    visual_state_flag_d: int
    sunburn: int
    wet: int
    hip_swing: int
    hip_press: int
    bust_swing: int
    bust_press: int
    hip_swing_lock: int
    hip_press_lock: int
    bust_swing_lock: int
    bust_press_lock: int
    panel_experience: int
    display_coordinate: int
    affection_level: int
    affection_point: int
    venus_memory: int
    girly: int
    skin_color: int
    nail_color: int
    partner_count: int
    created_at: datetime
    updated_at: datetime | None


class GirlGetResponseModel(CustomBaseModel):
    girl_list: list[GirlModel]
