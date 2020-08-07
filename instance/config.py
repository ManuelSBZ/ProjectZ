import os
import random


class Config():
    """Parent configuration class."""
    ENV = os.getenv('FLASK_ENV')
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY= os.urandom(20)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://msb:qwe@localhost/test_0'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql//msb:qwe@localhost/test_0'
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