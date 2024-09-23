"""
    Dummy conftest.py for qruise_pasquans_interface.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    - https://docs.pytest.org/en/stable/fixture.html
    - https://docs.pytest.org/en/stable/writing_plugins.html
"""
import pytest
from qruise_pasquans_interface.provider import PasquansProvider
  
@pytest.fixture
def mock_simulator():
    return PasquansProvider().get_backend("mock_simulator")

