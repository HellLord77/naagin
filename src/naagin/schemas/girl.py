from typing import Literal

from sqlalchemy import Boolean
from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from naagin.bases import SchemaBase

from .owner import OwnerSchema


class GirlSchema(SchemaBase):
    __tablename__ = "girl"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey(OwnerSchema.owner_id), primary_key=True)
    girl_mid: Mapped[int] = mapped_column(Integer, primary_key=True)
    mood: Mapped[Literal[0]] = mapped_column(Integer, default=0)
    experience: Mapped[int] = mapped_column(Integer, default=0)
    level: Mapped[int] = mapped_column(Integer, default=1)
    power: Mapped[int] = mapped_column(Integer)
    additional_power: Mapped[int] = mapped_column(Integer, default=0)
    technic: Mapped[int] = mapped_column(Integer)
    additional_technic: Mapped[int] = mapped_column(Integer, default=0)
    stamina: Mapped[int] = mapped_column(Integer)
    additional_stamina: Mapped[int] = mapped_column(Integer, default=0)
    appeal: Mapped[int] = mapped_column(Integer)
    appeal_up: Mapped[int] = mapped_column(Integer, default=0)
    additional_appeal: Mapped[int] = mapped_column(Integer, default=0)
    hair_item_mid: Mapped[int] = mapped_column(Integer)
    ring_item_mid: Mapped[int] = mapped_column(Integer, default=0)
    addition_accessory_item_mid: Mapped[int] = mapped_column(Integer, default=0)
    swimsuit_item_mid: Mapped[int] = mapped_column(Integer)
    accessory_head_item_mid: Mapped[int] = mapped_column(Integer, default=0)
    accessory_face_item_mid: Mapped[int] = mapped_column(Integer, default=0)
    accessory_arm_item_mid: Mapped[int] = mapped_column(Integer, default=0)
    visual_state_flag_a: Mapped[bool] = mapped_column(Boolean, default=False)
    visual_state_flag_b: Mapped[bool] = mapped_column(Boolean, default=False)
    visual_state_flag_c: Mapped[bool] = mapped_column(Boolean, default=False)
    visual_state_flag_d: Mapped[bool] = mapped_column(Boolean, default=False)
    sunburn: Mapped[int] = mapped_column(Integer, default=0)
    wet: Mapped[int] = mapped_column(Integer, default=0)
    hip_swing: Mapped[Literal[0]] = mapped_column(Integer, default=0)
    hip_press: Mapped[Literal[0]] = mapped_column(Integer, default=0)
    bust_swing: Mapped[Literal[0]] = mapped_column(Integer, default=0)
    bust_press: Mapped[Literal[0]] = mapped_column(Integer, default=0)
    hip_swing_lock: Mapped[bool] = mapped_column(Boolean, default=False)
    hip_press_lock: Mapped[bool] = mapped_column(Boolean, default=False)
    bust_swing_lock: Mapped[bool] = mapped_column(Boolean, default=False)
    bust_press_lock: Mapped[bool] = mapped_column(Boolean, default=False)
    panel_experience: Mapped[int] = mapped_column(Integer, default=0)
    display_coordinate: Mapped[bool] = mapped_column(Boolean, default=False)
    affection_level: Mapped[int] = mapped_column(Integer, default=1)
    affection_point: Mapped[int] = mapped_column(Integer, default=0)
    venus_memory: Mapped[int] = mapped_column(Integer, default=0)
    girly: Mapped[Literal[0]] = mapped_column(Integer, default=0)
    skin_color: Mapped[Literal[0]] = mapped_column(Integer, default=0)
    nail_color: Mapped[Literal[0]] = mapped_column(Integer, default=0)
    partner_count: Mapped[int] = mapped_column(Integer, default=0)

    __table_args__ = (
        CheckConstraint(mood == 0, "mood_const"),
        CheckConstraint(experience.between(0, 4587309), "experience_range"),
        CheckConstraint(level.between(1, 90), "level_range"),
        CheckConstraint(additional_power >= 0, "additional_power_min"),
        CheckConstraint(additional_technic >= 0, "additional_technic_min"),
        CheckConstraint(additional_stamina >= 0, "additional_stamina_min"),
        CheckConstraint(appeal_up >= 0, "appeal_up_min"),
        CheckConstraint(additional_appeal >= 0, "additional_appeal_min"),
        CheckConstraint(sunburn.between(0, 100), "sunburn_range"),
        CheckConstraint(sunburn % 10 == 0, "sunburn_mod"),
        CheckConstraint(wet.between(0, 100), "wet_range"),
        CheckConstraint(wet % 10 == 0, "wet_mod"),
        CheckConstraint(hip_swing == 0, "hip_swing_const"),
        CheckConstraint(hip_press == 0, "hip_press_const"),
        CheckConstraint(bust_swing == 0, "bust_swing_const"),
        CheckConstraint(bust_press == 0, "bust_press_const"),
        CheckConstraint(affection_level.between(1, 140), "affection_level_range"),
        CheckConstraint(affection_point.between(0, 485000), "affection_point_range"),
        CheckConstraint(venus_memory >= 0, "venus_memory_min"),
        CheckConstraint(girly == 0, "girly_const"),
        CheckConstraint(skin_color == 0, "skin_color_const"),
        CheckConstraint(nail_color == 0, "nail_color_const"),
    )
