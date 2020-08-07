from flask_script import Manager
from app import create_app
from app.models import db

app = create_app()
app.config["ENV"] = "DEVELOPMENT"
instance_manager = Manager(app)

print(app.config)

@instance_manager.command
def create_all():
    print("ejecutando comando")
    db.create_all()

if __name__ == "__main__":
    instance_manager.run()

