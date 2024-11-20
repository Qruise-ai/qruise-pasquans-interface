from qruise.pasquans_interface import ureg, Q_
import numpy as np


def test_ureg():
    assert ureg
    assert Q_(1, "m") == 1 * ureg.meter


def test_conversion_mhz_to_rad_per_s():
    assert Q_(1, "MHz").to("rad/s") == 1e6 * ureg.rad / ureg.s


def test_convert_array_mhz_to_rad_per_s():
    freqs = Q_(np.array([1, 2, 3]), "MHz")

    converted = freqs.to("rad/s")

    # Compare magnitudes using np.testing.assert_allclose
    np.testing.assert_allclose(converted.magnitude, np.array([1e6, 2e6, 3e6]))

    # Compare units
    assert converted.units == ureg.rad / ureg.s
