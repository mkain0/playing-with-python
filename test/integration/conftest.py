import base64

import pytest

from project import create_app


@pytest.fixture
def app():
    flask_app = create_app('flask_test.cfg')
    test_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield test_client

    ctx.pop()


@pytest.fixture
def authorization_header():
    return {'Authorization': 'Basic ' + base64.b64encode(bytes('admin:1234', 'ascii')).decode('ascii')}