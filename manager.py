from flask_script import Manager
from app import create_app
from app.models import db
from instance.config import app_config
import os


setting = os.getenv("SETTINGS")
app = create_app(app_config[setting])
instance_manager = Manager(app)

print(app.config)

@instance_manager.command
def create_all():
    print("creating all tables")
    db.create_all()

@instance_manager.command
def delete_tables():
    print("deleting all tables")
    db.drop_all()
if __name__ == "__main__":
    instance_manager.run()

