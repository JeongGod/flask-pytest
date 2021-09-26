import json

import config
import pytest
from flaskr import create_app
from sqlalchemy import create_engine

TEST_CONFIG = {
    'TESTING' : True,
    'DB_URL' : config.TEST_DB_URL
}

# APP
@pytest.fixture(scope='session') # 전체 테스트 실행시에 한 번만 실행된다.
def app():
    app = create_app({'TESTING' : True})
    return app

# DB
@pytest.fixture(scope='session') # 전체 테스트 실행시에 한 번만 실행된다.
def db():
    pass

# APP + DB
@pytest.fixture
def client(app):
    client = app.test_client()
    return client

def test_hello(client):
    res = client.get('/api/hello')
    data = json.loads(res.data)

    assert res.status_code == 200
    assert data == "Hello World"
