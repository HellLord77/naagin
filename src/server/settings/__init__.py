from .__base__ import NaaginBaseSettings
from .api01 import API01Settings
from .common.data import DataSettings
from .common.database import DatabaseSettings
from .game import GameSettings

database = DatabaseSettings()
data = DataSettings()
api01 = API01Settings()
game = GameSettings()
