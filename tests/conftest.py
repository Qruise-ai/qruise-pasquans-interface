import pytest
from qruise.pasquans_interface import MockProvider


@pytest.fixture
def mock_simulator():
    return MockProvider().get_backend("mock_simulator")


@pytest.fixture
def mock_simulator_v2():
    return MockProvider().get_backend("mock_simulator_v2")
