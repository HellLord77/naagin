from typing import Annotated

from fastapi import Depends

from naagin.models.csv import EpisodeCSVModel
from naagin.models.csv import GirlCSVModel
from naagin.models.csv import GirlStatusCSVModel
from naagin.providers.csv import provide_episodes
from naagin.providers.csv import provide_girl_affection_levels
from naagin.providers.csv import provide_girl_levels
from naagin.providers.csv import provide_girl_statuses
from naagin.providers.csv import provide_girls
from naagin.providers.csv import provide_owner_levels

GirlAffectionLevelsCSVDependency = Annotated[list[int], Depends(provide_girl_affection_levels)]
GirlLevelsCSVDependency = Annotated[list[int], Depends(provide_girl_levels)]
GirlsCSVDependency = Annotated[dict[int, GirlCSVModel], Depends(provide_girls)]
GirlStatusesCSVDependency = Annotated[list[GirlStatusCSVModel], Depends(provide_girl_statuses)]
OwnerLevelsCSVDependency = Annotated[list[int], Depends(provide_owner_levels)]
EpisodesCSVDependency = Annotated[dict[int, EpisodeCSVModel], Depends(provide_episodes)]
