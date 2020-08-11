from .default import *

SQLALCHEMY_DATABASE_URI =os.getenv("URI")
ENV = "PRODUCTION"
DEBUG = False