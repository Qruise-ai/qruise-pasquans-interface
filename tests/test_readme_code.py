from qruise.pasquans_interface import simulate, MockProvider
from qruise.pasquans_interface import SimulatorBackend
from qruise.pasquans_interface import PasquansProvider
from typing import List, Tuple


def test_simulate_function_in_readme():
    result = simulate(
        lattice_sites=[(0.0, 0.0), (1.0, 1.0)],
        global_rabi_frequency=[1.0, 1.0],
        global_phase=[0.0, 0.0],
        global_detuning=[0.0, 0.0],
        local_detuning=[0.0, 0.0],
        init_state=[1.0, 0.0],
        timegrid=[0.0, 1.0],
        backend="mock_simulator",
        backend_options={},
        provider=MockProvider(),
    )

    # Accessing the simulation results
    populations = result["state_populations"]
    assert "error" not in result
    assert populations == [0.5, 0.5]


def test_custom_provider_and_simulator_in_readme():

    class CustomSimulator(SimulatorBackend):
        """Custom simulator backend"""

        def __init__(self, **backend_options):
            """
            Initialize the CustomSimulator with specific backend options.

            Parameters
            ----------
            backend_options : dict
                Dictionary containing backend-specific configuration parameters.
            """
            self.name = "custom_simulator"
            self.custom_parameter = backend_options.get(
                "custom_parameter", 1.0
            )  # Example parameter
            self.backend_options = backend_options

        def simulate(
            self,
            lattice_sites: List[Tuple[float, float]],
            global_rabi_frequency: List[float],
            global_phase: List[float],
            global_detuning: List[float],
            local_detuning: List[float],
            timegrid: List[float],
            init_state: List[float] = None,
            backend_options: dict = None,
        ) -> dict:
            """
            Run a simulation on the custom backend.

            Parameters
            ----------
            lattice_sites : list[Tuple[float, float]]
                List of positions of atoms in the lattice.
            global_rabi_frequency : list[float]
                Time-dependent global Rabi frequencies.
            global_phase : list[float]
                Time-dependent global phase values.
            global_detuning : list[float]
                Time-dependent global detuning values.
            local_detuning : list[float]
                Local detuning values for each lattice site.
            timegrid : list[float]
                Timeline for the simulation.
            init_state : list[float], optional
                Initial state of the quantum system, default is None.
            backend_options : dict, optional
                Additional backend-specific configuration options.

            Returns
            -------
            dict
                Dictionary containing the results of the simulation, such as state populations and metadata.
            """
            # Example of running the simulation with mock data
            state_populations = [0.7, 0.3]  # Mock result for demonstration
            return {
                "state_populations": state_populations,
                "backend_options": self.backend_options,
            }

        def get_backend_information(self) -> dict:
            """
            Retrieve information about the custom backend.

            Returns
            -------
            dict
                Dictionary containing metadata about the backend.
            """
            return {
                "name": self.name,
                "custom_parameter": self.custom_parameter,
            }

    class CustomProvider(PasquansProvider):
        """Custom provider for managing and providing custom simulators."""

        def _get_simulators(self) -> List[SimulatorBackend]:
            """
            Return a list of available simulators provided by this provider.

            Returns
            -------
            list[SimulatorBackend]
                A list of simulator classes available through this provider.
            """
            return [CustomSimulator]  # Register the CustomSimulator here

    # Example usage with the CustomProvider and CustomSimulator
    result = simulate(
        lattice_sites=[(0.0, 0.0), (1.0, 1.0)],
        global_rabi_frequency=[1.0, 1.0],
        global_phase=[0.0, 0.0],
        global_detuning=[0.0, 0.0],
        local_detuning=[0.0, 0.0],
        init_state=[1.0, 0.0],
        timegrid=[0.0, 1.0],
        backend="custom_simulator",
        backend_options={"custom_parameter": 2.0},
        provider=CustomProvider(),
    )

    # Access simulation results
    assert result["state_populations"] == [0.7, 0.3]
