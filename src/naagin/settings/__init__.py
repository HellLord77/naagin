from .api import APISettings
from .api01 import API01Settings
from .data import DataSettings
from .database import DatabaseSettings
from .environment import EnvironmentSettings
from .fastapi import FastAPISettings
from .game import GameSettings
from .logging import LoggingSettings
from .version import VersionSettings

environment = EnvironmentSettings()
logging = LoggingSettings(_env_file=environment.file)
fastapi = FastAPISettings(_env_file=environment.file)

version = VersionSettings(_env_file=environment.file)
data = DataSettings(_env_file=environment.file)
database = DatabaseSettings(_env_file=environment.file)

api = APISettings(_env_file=environment.file)
api01 = API01Settings(_env_file=environment.file)
game = GameSettings(_env_file=environment.file)
