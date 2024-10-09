import pytest
from qruise.pasquans.interface.provider import PasquansProvider


@pytest.fixture
def mock_simulator():
    return PasquansProvider().get_backend("mock_simulator")
