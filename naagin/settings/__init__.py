from .api import APISettings
from .api01 import API01Settings
from .app import AppSettings
from .data import DataSettings
from .database import DatabaseSettings
from .environment import EnvironmentSettings
from .logging import LoggingSettings
from .resource import ResourceSettings
from .version import VersionSettings

environment = EnvironmentSettings()
logging = LoggingSettings(_env_prefix="log_", _env_file=environment.file)
app = AppSettings(_env_prefix="app_", _env_file=environment.file)

version = VersionSettings(_env_prefix="ver_", _env_file=environment.file)
data = DataSettings(_env_prefix="data_", _env_file=environment.file)
database = DatabaseSettings(_env_prefix="db_", _env_file=environment.file)

api = APISettings(_env_prefix="api_", _env_file=environment.file)
api01 = API01Settings(_env_prefix="api01_", _env_file=environment.file)

game = ResourceSettings(_env_prefix="game_", _env_file=environment.file, host="game.doaxvv.com")
cdn01 = ResourceSettings(_env_prefix="cdn01_", _env_file=environment.file, host="cdn01.doax-venusvacation.jp")
www = ResourceSettings(_env_prefix="www_", _env_file=environment.file, host="doax-venusvacation.jp")
