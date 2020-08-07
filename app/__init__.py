#app/__init__.py
from flask import Flask
import os

def create_app(setting):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(setting)

    from .models import db
    db.init_app(app)

    from .extensions import migrate
    migrate.init_app(app, db)

    return app



