from qruise.pasquans_interface import simulate, MockProvider, Q_, ureg
import numpy as np
from qruise.pasquans_interface import SimulatorBackend
from qruise.pasquans_interface import PasquansProvider
from pint import Quantity
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


def test_simulate_function_v2_in_readme():
    result = simulate(
        lattice_sites=np.array([(0.0, 0.0), (1.0, 1.0)]) * Q_("micrometer"),
        global_rabi_frequency=np.array([1.0, 1.0]) * Q_("MHz"),
        global_phase=np.array([0.0, 0.0]) * Q_("rad"),
        global_detuning=np.array([0.0, 0.0]) * Q_("MHz"),
        local_detuning=np.array([0.0, 0.0]) * Q_("MHz"),
        init_state=[1.0, 0.0],
        timegrid=np.array([0.0, 1.0]) * Q_("microsecond"),
        backend="mock_simulator_v2",
        backend_options={},
        provider=MockProvider(),
    )

    assert "error" not in result

    # Accessing the simulation results
    populations = result["state_populations"]

    print("Simulation Results:", populations)


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


def test_custom_provider_and_simulator_v2_in_readme():
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
            lattice_sites: Quantity,
            global_rabi_frequency: Quantity,
            global_phase: Quantity,
            global_detuning: Quantity,
            local_detuning: Quantity,
            init_state: list,
            timegrid: Quantity,
            backend_options={},
        ) -> dict:
            """
            Simulate the system.

            This method simulates the dynamics of a quantum system based on input parameters
            such as lattice configuration, Rabi frequencies, phases, and detuning values. It
            returns a dictionary containing the simulation results and backend options used.

            Parameters
            ----------
            lattice_sites : Quantity
                A Pint Quantity representing the positions of atoms in the lattice. Expected to have
                a unit of [length].
            global_rabi_frequency : Quantity
                A Pint Quantity representing the time-dependent global Rabi frequencies. Expected
                to have a unit of [frequency].
            global_phase : Quantity
                A Pint Quantity representing the time-dependent global phases. Expected to have
                a unit of [angle].
            global_detuning : Quantity
                A Pint Quantity representing the time-dependent global detuning values. Expected
                to have a unit of [frequency].
            local_detuning : Quantity
                A Pint Quantity representing the local detuning values for each lattice site. Expected
                to have a unit of [frequency].
            init_state : list
                A list representing the initial state of the system. Each element corresponds to the
                state of a lattice site.
            timegrid : Quantity
                A Pint Quantity representing the time grid over which the simulation is run. Expected
                to have a unit of [time].
            backend_options : dict, optional
                A dictionary containing options specific to the simulation backend. Default is an
                empty dictionary.

            Returns
            -------
            dict
                A dictionary containing the following keys:
                - "populations": List of state populations over time.
                - "backend_options": The backend options used in the simulation.
            """
            # Check if the lattice sites are in a distance unit
            assert lattice_sites.dimensionality == ureg.meter.dimensionality
            # Check if the global rabi frequency is in a frequency unit
            assert global_rabi_frequency.dimensionality == ureg.hertz.dimensionality
            # Check if the global phase is dimensionless
            assert global_phase.dimensionless
            # Check if the global detuning is in a frequency unit
            assert global_detuning.dimensionality == ureg.hertz.dimensionality
            # Check if the local detuning is in a frequency unit
            assert local_detuning.dimensionality == ureg.hertz.dimensionality
            # Check if the timegrid is in a time unit
            assert timegrid.dimensionality == ureg.second.dimensionality

            # Convert any units if your simulator requires it
            lattice_sites = lattice_sites.to(ureg.meter)
            global_rabi_frequency = global_rabi_frequency.to(ureg.hertz)
            global_phase = global_phase.to(ureg.dimensionless)
            global_detuning = global_detuning.to(ureg.hertz)
            local_detuning = local_detuning.to(ureg.hertz)
            timegrid = timegrid.to(ureg.second)

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
        lattice_sites=np.array([(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)]) * Q_("micrometer"),
        global_rabi_frequency=np.array([1.0, 1.0]) * Q_("MHz"),
        global_phase=np.array([0.0, 0.0]) * Q_("rad"),
        global_detuning=np.array([0.0, 0.0]) * Q_("MHz"),
        local_detuning=np.array([0.0, 0.0]) * Q_("MHz"),
        init_state=[0.0, 0.0],
        timegrid=[0.0, 1.0] * Q_("microsecond"),
        backend="custom_simulator",
        backend_options={},
        provider=CustomProvider(),
    )

    # Access simulation results
    populations = result["state_populations"]
    print("Simulation Results:", populations)
