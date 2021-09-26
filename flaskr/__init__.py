import os

import config
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flaskr.controller import hello

db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__)

    # API 설정
    app.register_blueprint(hello.bp)

    # Config 설정
    if test_config is None:
        app.config.from_object(config)
    else:
        app.config.update(test_config)

    # DB와 app 이어주기 및 migration 설정
    db.init_app(app)
    Migrate().init_app(app, db)
    from flaskr.models import user
    
    return app
