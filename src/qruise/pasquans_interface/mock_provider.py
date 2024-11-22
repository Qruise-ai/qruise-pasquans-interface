from qruise.pasquans_interface.provider import PasquansProvider
from qruise.pasquans_interface.mock_simulator import MockSimulator, MockSimulatorV2
from qruise.pasquans_interface.simulator_backend import SimulatorBackend


class MockProvider(PasquansProvider):
    """
    A concrete implementation of the PasquansProvider class, providing mock simulators.

    This class is designed to offer a mock backend environment for testing and development
    purposes. It overrides the abstract method `_get_simulators` to return a list of simulators
    that can be used for simulation tasks without connecting to real backends.
    """

    def _get_simulators(self) -> list[SimulatorBackend]:
        """
        Return a list of available simulators.

        This method overrides the `_get_simulators` method from the PasquansProvider class.
        It provides a list containing mock simulators, specifically the MockSimulator,
        which can be used for testing backend functionality in a simulated environment.

        Returns
        -------
        list[SimulatorBackend]
            A list of available simulators, in this case, containing only the MockSimulator class.
        """
        return [MockSimulator, MockSimulatorV2]
