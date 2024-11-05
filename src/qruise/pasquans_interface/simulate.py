from typing import Tuple
from qruise.pasquans_interface.provider import PasquansProvider
from qruise.pasquans_interface.mock_provider import MockProvider
from qruise.pasquans_interface.simulator_backend import SimulatorBackend


def simulate(
    lattice_sites: list[Tuple[float]],
    global_rabi_frequency: list[float],
    global_phase: list[float],
    global_detuning: list[float],
    local_detuning: list[float],
    init_state: list[float] = None,
    backend: str = "Bull",
    backend_options: dict = None,
    timegrid: list[float] = None,
    provider: PasquansProvider = MockProvider(),
) -> dict:
    """
    Function to run a quantum simulation on a specified backend.

    This function takes in a variety of parameters describing a quantum system (such as lattice sites,
    rabi frequencies, phase, and detuning) and runs a simulation on the specified backend. The results
    of the simulation, along with backend-specific configuration information, are returned in a dictionary.
    If an error occurs during simulation, it is caught and included in the results.

    Parameters
    ----------
    lattice_sites : list[Tuple[float]]
        A list of tuples representing the positions of atoms in the lattice.
    global_rabi_frequency : list[float]
        A time-dependent list of global rabi frequencies used for the simulation.
    global_phase : list[float]
        A time-dependent list of global phase values.
    global_detuning : list[float]
        A time-dependent list of global detuning values.
    local_detuning : list[float]]
        A list representing the local detuning for each site specified in the lattice.
    init_state : list[float], optional
        An optional list representing the initial state of the system, default is None.
    backend : str, optional
        The name of the backend to use for simulation, default is "Bull".
    backend_options : dict, optional
        A dictionary of key-value pairs for backend-specific configurations, default is None.
    timegrid : list[float], optional
        A time grid list for the simulation, default is None.
    provider : PasquansProvider, optional
        The provider responsible for managing and retrieving backends, default is MockProvider.

    Returns
    -------
    dict
        A dictionary containing the results of the simulation, including:
        - "state_populations": A mock or actual state population result from the simulation.
        - "backend_information": Metadata about the backend used in the simulation.
        - "error": Error information, if any exception occurs during the simulation.

    Raises
    ------
    SimulationError
        Raised if a run-time error is encountered during the simulation.
    JobDescriptionError
        Raised if the job description provided to the simulation is invalid or incompatible.
    """

    # Retrieve the backend object using the specified provider and backend name
    backend_simulator: SimulatorBackend = provider.get_backend(backend)
    result = {}

    # Run the simulation
    try:
        result = backend_simulator.simulate(
            lattice_sites=lattice_sites,
            global_rabi_frequency=global_rabi_frequency,
            global_phase=global_phase,
            global_detuning=global_detuning,
            local_detuning=local_detuning,
            init_state=init_state,
            backend_options=backend_options,
            timegrid=timegrid,
        )
    except Exception as e:
        # Catch any exception that occurs during simulation and add it to the result
        result["error"] = str(e)
    finally:
        # Retrieve and include backend information in the result
        result["backend_information"] = backend_simulator.get_backend_information()

    # Return the result, including simulation data and backend information
    return result
