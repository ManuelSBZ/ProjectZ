from flask_script import Manager
from app import create_app
from app.models import db

app = create_app()
app.config["ENV"] = "DEVELOPMENT"
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

