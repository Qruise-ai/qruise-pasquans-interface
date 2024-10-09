from typing import Tuple
from qruise.pasquans_interface.provider import PasquansProvider


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
) -> dict:
    """
    Function to run a simulation on a specified backend

    Parameters
    ----------
    lattice_sites : List[Tuple[float]]
        List of atom positions
    global_rabi_frequency : List[float]
        Vector of floats describing the time-dependent global rabi frequency
    global_phase : List[float]
        Vector of floats describing the time-dependent global phase profile
    global_detuning : List[float]
        Vector of floats describing the time-dependent global detuning
    local_detuning : List[float]
        Vector of floats describing the local detuning
        (in the order of the sites specified in the lattice sites)
    init_state : List[float], optional
        Vector of floats describing the initial state of the system, by default ground state
    backend : str, optional
        name of the digital twin backend to be used, by default “Bull”
    backend_options : dict, optional
        key-value pair of backend-specific configuration params, by default None

    Returns
    -------
    Dict
        Dictionary containing the simulation results as state populations. Additionally, it also contains the backend configuration metadata.

    Raises
    ------
    SimulationError
        run-time error encountered during the simulation
    JobDescriptionError
        invalid or incompatible simulation job description
    """

    # Create the backend object
    backend_simulator = PasquansProvider().get_backend(backend)
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
        result["error"] = str(e)
    finally:
        result["backend_information"] = backend_simulator.get_backend_information()
    return result
