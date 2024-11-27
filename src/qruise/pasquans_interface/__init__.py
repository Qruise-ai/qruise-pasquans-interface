import sys

from qruise.pasquans_interface.mock_simulator import MockSimulator, MockSimulatorV2
from qruise.pasquans_interface.mock_provider import MockProvider
from qruise.pasquans_interface.provider import PasquansProvider
from qruise.pasquans_interface.simulator_backend import SimulatorBackend
from qruise.pasquans_interface.simulate import simulate
from qruise.pasquans_interface.units import ureg, Q_


__all__ = [
    "MockSimulator",
    "MockSimulatorV2",
    "MockProvider",
    "PasquansProvider",
    "SimulatorBackend",
    "simulate",
    "ureg",
    "Q_",
]


if sys.version_info[:2] >= (3, 8):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.8`
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
else:
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "qruise-pasquans-interface"
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
