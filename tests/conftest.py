import pytest
from qruise.pasquans_interface.mock_provider import MockProvider


@pytest.fixture
def mock_simulator():
    return MockProvider().get_backend("mock_simulator")
