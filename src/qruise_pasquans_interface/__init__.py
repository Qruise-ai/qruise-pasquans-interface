import sys
import warnings

SIMULATORS = []


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

# Mock simulator
try:
    from qruise_pasquans_interface.mock_simulator import MockSimulator
except ImportError:
    warnings.warn(
        "MockSimulator not available. Please install qruise-pasquans-interface.",
        ImportWarning,
    )
else:
    SIMULATORS.append(MockSimulator)

# Qruise simulator
try:
    from qruise_pasquans.qruise_simulator import QruiseSimulator
except ImportError:
    warnings.warn(
        "QruiseSimulator not available. Please install qruise-pasquans.", ImportWarning
    )
else:
    SIMULATORS.append(QruiseSimulator)
