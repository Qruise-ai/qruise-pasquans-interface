from qruise.pasquans_interface.provider import PasquansProvider
from qruise.pasquans_interface.mock_simulator import MockSimulator


class MockProvider(PasquansProvider):

    def _get_simulators(self):
        return [MockSimulator]
