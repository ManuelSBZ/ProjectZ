#app/__init__.py
from flask import Flask
import os

def create_app(setting):
    # relative imports are not allowed, it means importing externals modules.

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(setting)
    print(app.config)
    # from ..instance.config import app_config
    # app.config.from_object("instance.config."+setting)

    from .models import db
    db.init_app(app)

    from .extensions import migrate
    migrate.init_app(app, db)

    return app



