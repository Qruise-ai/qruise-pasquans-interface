import pytest
from qruise_pasquans_interface.provider import PasquansProvider
  
@pytest.fixture
def mock_simulator():
    return PasquansProvider().get_backend("mock_simulator")

