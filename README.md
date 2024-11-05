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
from qruise_pasquans_interface import simulate, MockProvider

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
print("Simulation Results:", populations)
```



## How to use the Interface
The `qruise-pasquans-interface` package provides a simple API for simulating quantum operations. To use the interface, follow these steps:
- **Import the `simulate` function**: Import the `simulate` function from the package to run quantum simulations.
- **Define the simulation parameters**: Define the parameters for the quantum simulation, such as lattice sites, Rabi frequencies, phases, detunings, initial states, and time grid.
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
from qruise_pasquans_interface import SimulatorBackend
from typing import List, Tuple

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
```
Explanation of CustomSimulator:
- Initialization: The constructor method initializes the custom simulator with options provided in backend_options. You can add custom configuration options here as needed.
- simulate: Implements the main simulation logic. For demonstration purposes, this function returns a mock result (state_populations) and includes backend options. In a real implementation, you would add logic to perform the actual quantum simulation based on the provided parameters.
- get_backend_information: Returns metadata about the backend, which can be useful for debugging and configuration checks.

### Custom Provider
A provider in the qruise-pasquans-interface must inherit from the PasquansProvider abstract base class and implement the _get_simulators method, which returns a list of available simulator classes.

**Step-by-step**:
```python
from qruise_pasquans_interface import PasquansProvider
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
from qruise_pasquans_interface import simulate

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
populations = result["state_populations"]
print("Simulation Results:", populations)
```

## Summary
- **CustomSimulator**: Implements the SimulatorBackend interface, providing a mock simulate method and returning backend information.
- **CustomProvider**: Implements the PasquansProvider interface, exposing the custom simulator as an available backend.
- **Using the Custom Classes**: By specifying CustomProvider as the provider and "custom_simulator" as the backend, you can run simulations with your custom setup.

These steps enable you to create and integrate a custom simulator backend, allowing flexibility in handling different types of quantum simulators under the qruise-pasquans-interface framework.
