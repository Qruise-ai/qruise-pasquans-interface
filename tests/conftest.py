import pytest
from qruise.pasquans_interface.provider import PasquansProvider


@pytest.fixture
def mock_simulator():
    return PasquansProvider().get_backend("mock_simulator")
