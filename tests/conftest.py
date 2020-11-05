import pytest
from app.user.models import User
from app import create_app


@pytest.fixture
def app():
    app = create_app()
    app.testing = True
    return app


@pytest.fixture(scope="module")
def new_user():
    user = User("Gustavo Daniel", "gustavo@gustavo.com", "00000000000")
    return user
