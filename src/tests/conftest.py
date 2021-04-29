import pytest
from starlette.testclient import TestClient

from main import api
from services import openweather_service

# A fixture provides a defined, reliable and consistent context for the tests.
# This could include environment (for example a database configured with known parameters)
# or content (such as a dataset).
# File must be called conftest.py

@pytest.fixture(scope="module")
def fixture_test_api():
    client = TestClient(api)
    yield client  # testing happens here

