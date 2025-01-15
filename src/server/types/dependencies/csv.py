from typing import Annotated

from fastapi import Depends

from ... import providers
from ...models.csv import EpisodeCSVModel

OwnerLevelsCSVDependency = Annotated[
    list[int], Depends(providers.csv.provide_owner_levels)
]
EpisodesCSVDependency = Annotated[
    dict[int, EpisodeCSVModel], Depends(providers.csv.provide_episodes)
]
