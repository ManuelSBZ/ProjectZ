import os
import random
from dotenv import load_dotenv
from pathlib import Path


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Config(object):
    """Parent configuration class."""
    DEBUG=False
    CSRF_ENABLED = True
    SECRET_KEY= os.urandom(20)
    SQLALCHEMY_DATABASE_URI = os.getenv("URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Configurations for Development."""
    ENV = "DEVELOPMENT"
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}