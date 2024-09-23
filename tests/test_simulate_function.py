from qruise_pasquans_interface.simulate import simulate

def test_simulate():
    result = simulate(
        lattice_sites=[(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)],
        global_rabi_frequency=[1.0, 1.0],
        global_phase=[0.0, 0.0],
        global_detuning=[0.0, 0.0],
        local_detuning=[0.0, 0.0],
        init_state=[0.0, 0.0],
        backend="mock_simulator",
        backend_options={},
    )
    assert result["state_populations"] == [0.5, 0.5]
    assert result["backend_options"] == {}
    assert "error" not in result