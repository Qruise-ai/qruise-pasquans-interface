from qruise.pasquans_interface.simulate import simulate
from qruise.pasquans_interface.mock_provider import MockProvider


def test_simulate():
    result = simulate(
        lattice_sites=[(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)],
        global_rabi_frequency=[1.0, 1.0],
        global_phase=[0.0, 0.0],
        global_detuning=[0.0, 0.0],
        local_detuning=[0.0, 0.0],
        init_state=[0.0, 0.0],
        timegrid=[0.0, 1.0],
        backend="mock_simulator",
        backend_options={},
        provider=MockProvider(),
    )
    assert result["state_populations"] == [0.5, 0.5]
    assert result["backend_options"] == {}
    assert "error" not in result

    populations = result["state_populations"]
    assert "error" not in result

    print(populations)
