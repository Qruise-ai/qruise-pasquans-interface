# import pytest

from qruise_pasquans_interface.provider import PasquansProvider
from qruise_pasquans_interface.mock_simulator import MockSimulator

def test_mock_simulator():
    mock_simulator = PasquansProvider().get_backend("mock_simulator")
    assert isinstance(mock_simulator, MockSimulator)
    assert mock_simulator.name == "mock_simulator"

# def test_main(capsys):
#     """CLI Tests"""
#     # capsys is a pytest fixture that allows asserts against stdout/stderr
#     # https://docs.pytest.org/en/stable/capture.html
#     main(["7"])
#     captured = capsys.readouterr()
#     assert "The 7-th Fibonacci number is 13" in captured.out
