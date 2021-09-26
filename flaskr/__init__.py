import os

import config
from flask import Flask

from flaskr.controller import hello


def create_app(test_config=None):
    app = Flask(__name__)

    # API 설정
    app.register_blueprint(hello.bp)

    # Config 설정
    if test_config is None:
        app.config.from_object(config)
    else:
        app.config.update(test_config)

    return app
