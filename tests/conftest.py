"""
    Dummy conftest.py for qruise_pasquans_interface.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    - https://docs.pytest.org/en/stable/fixture.html
    - https://docs.pytest.org/en/stable/writing_plugins.html
"""
import pytest
from qruise_pasquans_interface.provider import PasquansProvider

# import sys
# import pytest

# def is_debugging():
#     return 'debugpy' in sys.modules
    
    
# # enable_stop_on_exceptions if the debugger is running during a test
# if is_debugging():
#   @pytest.hookimpl(tryfirst=True)
#   def pytest_exception_interact(call):
#     raise call.excinfo.value
    
#   @pytest.hookimpl(tryfirst=True)
#   def pytest_internalerror(excinfo):
#     raise excinfo.value
  
@pytest.fixture
def mock_simulator():
    return PasquansProvider().get_backend("mock_simulator")

