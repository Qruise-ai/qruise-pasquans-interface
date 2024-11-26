from .simulator_backend import SimulatorBackend
from .units import ureg
from pint import Quantity


class MockSimulator(SimulatorBackend):
    """
    A concrete implementation of the SimulatorBackend class for mock simulations.

    This class simulates a quantum backend for testing purposes. It mimics the behavior of a
    real backend, allowing developers to test their applications without needing an actual
    quantum system. It stores backend options and provides basic simulation functionality
    by returning mock results.
    """

    def __init__(self, provider, **backend_options):
        """
        Constructor for the MockSimulator class.

        This method initializes the mock simulator by storing the provider and any additional
        backend options. The backend is given the name 'mock_simulator' to indicate its role.

        Parameters
        ----------
        provider : object
            The provider responsible for managing this backend.
        **backend_options : dict, optional
            Additional keyword arguments used for configuring the backend.
        """
        self._backend_options = backend_options
        self.provider = provider
        self.name = "mock_simulator"

    def simulate(
        self,
        lattice_sites,
        global_rabi_frequency,
        global_phase,
        global_detuning,
        local_detuning,
        init_state=None,
        timegrid=None,
        backend_options={},
    ) -> dict:
        """
        Simulate the system.

        This method mimics the simulation process of a quantum system. It takes various
        inputs representing system parameters (such as lattice sites, rabi frequency,
        and detuning values) and returns mock simulation results. The results include
        state populations and the backend options used for the simulation.

        Parameters
        ----------
        lattice_sites : list
            A list of tuples representing the positions of atoms in the lattice.
        global_rabi_frequency : list
            A list of time-dependent global rabi frequencies.
        global_phase : list
            A list of time-dependent global phase values.
        global_detuning : list
            A list of time-dependent global detuning values.
        local_detuning : list
            A list of local detuning values for each lattice site.
        init_state : list, optional
            An optional list representing the initial state of the system. Default is None.
        timegrid : list, optional
            An optional list representing the time grid over which the simulation is run. Default is None.
        backend_options : dict, optional
            A dictionary of options specific to the backend for this simulation.

        Returns
        -------
        dict
            A dictionary containing the simulation results, including state populations
            and the backend options used in the simulation.
        """
        return {
            "state_populations": [0.5, 0.5],  # Mocked simulation result
            "backend_options": backend_options,
        }

    def get_backend_information(self) -> dict:
        """
        Get information about the backend.

        This method provides metadata about the mock backend, including the backend's name
        and the options it was initialized with.

        Returns
        -------
        dict
            A dictionary containing the name of the backend and its configuration options.
        """
        return {
            "name": self.name,
            "backend_options": self._backend_options,
        }


class MockSimulatorV2(SimulatorBackend):
    """
    A concrete implementation of the SimulatorBackend class for mock simulations.

    This class simulates a quantum backend for testing purposes. It mimics the behavior of a
    real backend, allowing developers to test their applications without needing an actual
    quantum system. It stores backend options and provides basic simulation functionality
    by returning mock results.
    """

    def __init__(self, provider, **backend_options):
        """
        Constructor for the MockSimulator class.

        This method initializes the mock simulator by storing the provider and any additional
        backend options. The backend is given the name 'mock_simulator' to indicate its role.

        Parameters
        ----------
        provider : object
            The provider responsible for managing this backend.
        **backend_options : dict, optional
            Additional keyword arguments used for configuring the backend.
        """
        self._backend_options = backend_options
        self.provider = provider
        self.name = "mock_simulator_v2"

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

        return {
            "state_populations": [0.5, 0.5],  # Mocked simulation result
            "backend_options": backend_options,
        }

    def get_backend_information(self) -> dict:
        """
        Get information about the backend.

        This method provides metadata about the mock backend, including the backend's name
        and the options it was initialized with.

        Returns
        -------
        dict
            A dictionary containing the name of the backend and its configuration options.
        """
        return {
            "name": self.name,
            "backend_options": self._backend_options,
        }
