from .default import *

SQLALCHEMY_DATABASE_URI = os.getenv("URI")
ENV = "DEVELOPMENT"
DEBUG = True