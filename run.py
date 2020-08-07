from .app import create_app
from .instance.config import app_config

myapp = create_app(app_config["development"])