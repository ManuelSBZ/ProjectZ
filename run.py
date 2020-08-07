from .app import create_app
from .app.config import TestingConfig, DevelopmentConfig

myapp = create_app(DevelopmentConfig)