# https://docs.pytest.org/en/latest/explanation/fixtures.html#what-fixtures-are
import pytest

from cv_reader import create_app
from cv_reader.config import configs


@pytest.fixture(scope = 'session')
def client():
    app = create_app(configs['dev'])
    app.app_context().push()

    # https://flask.palletsprojects.com/en/2.1.x/api/#test-client
    client = app.test_client()
    yield client
