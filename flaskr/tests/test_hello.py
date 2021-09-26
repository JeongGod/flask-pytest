import json

import config
import pytest
# Scheme Migration
from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as AlembicConfig
# 롤백하기 위한 세션
from flask import g
from flaskr import create_app
from sqlalchemy import create_engine

TEST_CONFIG = {
    'TESTING' : True,
    'SQLALCHEMY_TRACK_MODIFICATIONS' : False,
    'SQLALCHEMY_DATABASE_URI' : config.TEST_DB_URL
}

# APP
@pytest.fixture(scope='session') # 전체 테스트 실행시에 한 번만 실행된다.
def app():
    app = create_app(TEST_CONFIG)
    app_context = app.app_context()
    app_context.push()
    yield app

    app_context.pop()

@pytest.fixture(scope='session')
def flask_client(app):
    return app.test_client()

# DB
@pytest.fixture(scope='session') # 전체 테스트 실행시에 한 번만 실행된다.
def test_db():
    # Engine Instance, Session Factory를 만든다.
    engine = create_engine(config.TEST_DB_URL, echo=True)

    _db = {
        'engine': engine,
        'session_factory' : db.session
    }

    # Alembic을 이용해 스키마를 동기화 시켜준다.
    alembic_config = AlembicConfig(config.ALEMBIC_INI)
    alembic_config.set_main_option('script_location', 'migrations')
    alembic_config.set_main_option('sqlalchemy.url', config.TEST_DB_URL)
    alembic_upgrade(alembic_config, 'head')

    yield _db
    
    engine.dispose()

# 테스트케이스마다 트랜잭션을 롤백하는 세션
@pytest.fixture(scope='function')
def session(test_db):
    session = test_db['session_factory']
    g.db = session

    yield session
    
    session.rollback()
    session.close()

def test_hello(flask_client):
    res = flask_client.get('/api/hello')
    data = json.loads(res.data)

    assert res.status_code == 200
    assert data == "Hello World"

from flaskr.models.user import *


def test_signin(flask_client, session):
    t_user = user('test1', '1111')
    session.add(t_user)
    session.flush()

    data = json.dumps({'user_id' : "test1", 'user_pw' : "1111"})
    res = flask_client.post('/api/signin', data=data, content_type='application/json')
    result = json.loads(res.data)


    assert res.status_code == 200
    assert result == 'success'
