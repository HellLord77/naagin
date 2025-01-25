from .api import APISettings
from .data import DataSettings
from .database import DatabaseSettings
from .game import GameSettings
from .version import VersionSettings

version = VersionSettings()
data = DataSettings()
database = DatabaseSettings()

api = APISettings()
game = GameSettings()
