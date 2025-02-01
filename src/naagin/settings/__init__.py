from .api import APISettings
from .data import DataSettings
from .database import DatabaseSettings
from .environment import EnvironmentSettings
from .game import GameSettings
from .version import VersionSettings

environment = EnvironmentSettings()
version = VersionSettings(_env_file=environment.file)

data = DataSettings(_env_file=environment.file)
database = DatabaseSettings(_env_file=environment.file)

api = APISettings(_env_file=environment.file)
game = GameSettings(_env_file=environment.file)
