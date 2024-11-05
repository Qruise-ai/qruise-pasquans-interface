from .simulator_backend import SimulatorBackend


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
