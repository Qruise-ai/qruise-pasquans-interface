from qruise_pasquans_interface.mock_simulator import MockSimulator


def test_mock_simulator(mock_simulator):
    assert isinstance(mock_simulator, MockSimulator)
    assert mock_simulator.name == "mock_simulator"


def test_backend_information(mock_simulator):
    backend_info = mock_simulator.get_backend_information()
    assert backend_info["name"] == "mock_simulator"
    assert backend_info["backend_options"] == {}
