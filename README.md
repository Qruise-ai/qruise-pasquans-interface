# qruise-pasquans-interface

The **qruise-pasquans-interface** package is a flexible and extensible API designed for simulating quantum operations within the Pasquans consortium. This package provides a standardized framework that allows users to manage and interact with various backend simulators, including both real and mock implementations. By using this interface, developers and researchers can simulate complex quantum systems, retrieve backend information, and customize quantum operations without relying on physical quantum hardware, making it an essential tool for testing and development.

## Features

- **Abstract Backend Management**: Provides a base structure for implementing multiple backend simulators, ensuring a consistent API for different simulators.
- **Mock Simulator Support**: Includes a mock backend for testing and development, allowing users to mimic quantum operations in a controlled environment.
- **Customizable Quantum Simulations**: Enables the customization of quantum operations, such as defining lattice sites, Rabi frequencies, phases, detunings, and initial states.
- **Integration with Pasquans Platforms**: Built to support PASQUANS2.1 simulators with minimal modifications, making it easy to integrate with existing Pasquans platforms.

## Installation

To install the `qruise-pasquans-interface` package, use `pip`:

```bash
pip install .
```

## Running Tests
Tests are included to verify the functionality of the package. You can run the tests using pytest:

```bash
pytest
```

## Basic Simulation with Mock Simulator
The following example demonstrates how to run a basic simulation using the mock simulator provided in the package.

```python
from qruise.pasquans_interface import simulate, MockProvider, Q_
import numpy as np

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
```



## How to use the Interface
The `qruise-pasquans-interface` package provides a simple API for simulating quantum operations. To use the interface, follow these steps:
- **Import the `simulate` function**: Import the `simulate` function from the package to run quantum simulations.
- **Define the simulation parameters**: Use Q_ and numpy array to define parameters such as lattice sites, Rabi frequencies, phases, detunings, initial states, and the time grid.
- **Select the provider**: Choose the provider that manages the backend simulators, such as the mock provider or a custom provider.
- **Select the backend simulator**: Choose the backend simulator to use for the simulation, such as the mock simulator or a custom simulator.
- **Run the simulation**: Call the `simulate` function with the specified parameters to run the quantum simulation.
- **Access the simulation results**: Retrieve the simulation results, such as state populations, from the returned result dictionary.

## Custom simulator backend and provider
To create a custom provider and simulator in the qruise-pasquans-interface, you’ll need to extend the SimulatorBackend and PasquansProvider base classes, as these define the required interfaces for interacting with backend simulators. Here’s a guide on how to create derived classes for a custom provider and simulator.

### Custom Simulator Backend
A simulator in the qruise-pasquans-interface must inherit from the SimulatorBackend abstract base class and implement the required methods, such as simulate and get_backend_information.

**Step-by-step**:
```python
from qruise.pasquans_interface import SimulatorBackend
from qruise.pasquans_interface import ureg
from pint import Quantity

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
        self.custom_parameter = backend_options.get("custom_parameter", 1.0)  # Example parameter
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
```
Explanation of CustomSimulator:
- Initialization: The constructor method initializes the custom simulator with options provided in backend_options. You can add custom configuration options here as needed.
- simulate: The simulate method implements the main logic for running a quantum simulation. It takes in various parameters, such as lattice sites, Rabi frequencies, and detunings, as Pint Quantity objects with associated units. You can:
 - Validate: Check if the provided parameters have the correct dimensionality (e.g., [length] for lattice sites, [frequency] for Rabi frequencies).
 - Convert: Convert the parameters to the units expected by the simulator backend if they differ (e.g., converting micrometers to meters or MHz to Hz).
 - Simulate: Perform the actual simulation logic. In this example, the method returns a mock result (state_populations) for demonstration. In a real implementation, this is where the quantum system's behavior would be computed based on the inputs and any backend-specific constraints.
- get_backend_information: Returns metadata about the backend, which can be useful for debugging and configuration checks.

### Custom Provider
A provider in the qruise-pasquans-interface must inherit from the PasquansProvider abstract base class and implement the _get_simulators method, which returns a list of available simulator classes.

**Step-by-step**:
```python
from qruise.pasquans_interface import PasquansProvider
from typing import List

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
```
- **_get_simulators**: This method returns a list of available simulators that the provider manages. By returning [CustomSimulator], this provider allows access to the CustomSimulator backend. If you have multiple simulators, you can add them to the list as well.

### Custom Provider and Simulator
After defining CustomSimulator and CustomProvider, you can use them in your simulation code.

```python
from qruise.pasquans_interface import simulate

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
```

## Summary
- **CustomSimulator**: Implements the SimulatorBackend interface, providing a mock simulate method and returning backend information.
- **CustomProvider**: Implements the PasquansProvider interface, exposing the custom simulator as an available backend.
- **Using the Custom Classes**: By specifying CustomProvider as the provider and "custom_simulator" as the backend, you can run simulations with your custom setup.

These steps enable you to create and integrate a custom simulator backend, allowing flexibility in handling different types of quantum simulators under the qruise-pasquans-interface framework.
