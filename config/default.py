import os
from dotenv import load_dotenv
from pathlib import Path


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

SECRET_KEY= os.urandom(30)
SQLALCHEMY_TRACK_MODIFICATIONS = False