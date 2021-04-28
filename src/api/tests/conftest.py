import pytest
from starlette.testclient import TestClient

from main import api

# A fixture provides a defined, reliable and consistent context for the tests.
# This could include environment (for example a database configured with known parameters)
# or content (such as a dataset).

@pytest.fixture(scope="module")
def test_app():
    client = TestClient(api)
    yield client  # testing happens here
