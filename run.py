from .app import create_app
import os
from .instance.config import app_config


setting = os.getenv("SETTINGS")
obj = app_config[setting]
myapp = create_app(obj)

