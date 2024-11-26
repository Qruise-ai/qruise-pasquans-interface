from qruise.pasquans_interface import simulate
from qruise.pasquans_interface import MockProvider
from qruise.pasquans_interface import Q_
import numpy as np


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


def test_simulate_v2():
    result = simulate(
        lattice_sites=np.array([(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)]) * Q_("micrometer"),
        global_rabi_frequency=np.array([1.0, 1.0]) * Q_("MHz"),
        global_phase=np.array([0.0, 0.0]) * Q_("rad"),
        global_detuning=np.array([0.0, 0.0]) * Q_("MHz"),
        local_detuning=np.array([0.0, 0.0]) * Q_("MHz"),
        init_state=[0.0, 0.0],
        timegrid=[0.0, 1.0] * Q_("microsecond"),
        backend="mock_simulator_v2",
        backend_options={},
        provider=MockProvider(),
    )
    assert "error" not in result

    assert result["state_populations"] == [0.5, 0.5]
    assert result["backend_options"] == {}
