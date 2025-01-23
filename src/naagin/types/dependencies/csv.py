from typing import Annotated

from fastapi import Depends

from naagin import providers
from naagin.models.csv import EpisodeCSVModel
from naagin.models.csv import GirlCSVModel
from naagin.models.csv import GirlStatusCSVModel

GirlAffectionLevelsCSVDependency = Annotated[
    list[int], Depends(providers.csv.provide_girl_affection_levels)
]
GirlLevelsCSVDependency = Annotated[
    list[int], Depends(providers.csv.provide_girl_levels)
]
GirlsCSVDependency = Annotated[
    dict[int, GirlCSVModel], Depends(providers.csv.provide_girls)
]
GirlStatusesCSVDependency = Annotated[
    list[GirlStatusCSVModel], Depends(providers.csv.provide_girl_statuses)
]
OwnerLevelsCSVDependency = Annotated[
    list[int], Depends(providers.csv.provide_owner_levels)
]
EpisodesCSVDependency = Annotated[
    dict[int, EpisodeCSVModel], Depends(providers.csv.provide_episodes)
]
