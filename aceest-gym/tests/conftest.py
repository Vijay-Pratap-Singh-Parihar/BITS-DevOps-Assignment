import pytest

import app.app as app_module


@pytest.fixture(autouse=True)
def reset_members():
    app_module.members.clear()
    yield
    app_module.members.clear()


@pytest.fixture
def client():
    app_module.app.config["TESTING"] = True
    with app_module.app.test_client() as c:
        yield c
