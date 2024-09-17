from .simulator_backend import SimulatorBackend

class MockSimulator(SimulatorBackend):

    def __init__(self, **backend_options):
        """
        Constructor for the MockSimulator class.
        """
        self._backend_options = backend_options
        self.name = "mock_simulator"

    def simulate(self,
                    lattice_sites,
                    global_rabi_frequency,
                    global_phase,
                    global_detuning,
                    local_detuning,
                    init_state=None) -> dict:
        """
        Function to run a simulation on a specified backend
        """
        return {
            "state_populations": [0.5, 0.5],
            "backend_configuration": self._backend_options,
        }
    
    def get_backend_information(self) -> dict:
        """
        Method to get information about the backend.
        """
        return {
            "name": self.name,
            "backend_options": self._backend_options,
        }