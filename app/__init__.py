from flask import Flask
import os

def create_app(setting = None):
    app = Flask(__name__)

    # app.config.from_object(app_config['development'])
    from .config import DevelopmentConfig
    app.config.from_object(DevelopmentConfig)


    from .models import db
    db.init_app(app)

    from .extensions import migrate
    migrate.init_app(app, db)

    return app



