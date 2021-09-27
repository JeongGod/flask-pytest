import os

import config
import db_connect
from flask import Flask
from flask_migrate import Migrate


def create_app(test_config=None):
    app = Flask(__name__)

    # API 설정
    from flaskr.controller import auth, hello
    app.register_blueprint(hello.bp)
    app.register_blueprint(auth.bp2)

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
