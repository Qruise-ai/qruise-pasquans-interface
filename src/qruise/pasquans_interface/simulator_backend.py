from abc import ABC, abstractmethod
from typing import Tuple


class SimulatorBackend(ABC):
    """
    Abstract Base Class (ABC) representing a backend for simulators.

    This class defines the interface for simulator backends, requiring any subclass to implement
    core functionalities such as initialization, running simulations, and retrieving backend-specific
    information. It ensures consistency across all backends that inherit from it.

    Attributes:
    -----------
    name : str
        The name of the backend, which should be initialized in the subclass.
    """

    name: str

    @abstractmethod
    def __init__(self, provider, **backend_options):
        """
        Abstract constructor to initialize the backend.

        This method must be implemented by any subclass to handle backend-specific initialization logic.
        It typically involves setting up backend attributes, configurations, and managing any other
        parameters required for running simulations.

        Parameters
        ----------
        provider : object
            The provider that manages this backend.
        **backend_options : dict, optional
            Additional keyword arguments for backend-specific configurations.

        Raises
        ------
        NotImplementedError
            Raised if the subclass does not implement this method.
        """
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def simulate(
        self,
        lattice_sites: list[Tuple[float]],
        global_rabi_frequency: list[float],
        global_phase: list[float],
        global_detuning: list[float],
        local_detuning: list[float],
        init_state: list[float] = None,
        timegrid: list[float] = None,
    ) -> dict:
        """
        Run the simulation on the backend.

        This method is responsible for running a quantum simulation based on the provided parameters.
        Subclasses must implement this method, defining the specific behavior of the backend during
        the simulation.

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
        local_detuning : list[float]
            A list representing the local detuning for each site specified in the lattice.
        init_state : list[float], optional
            An optional list representing the initial state of the system, with the ground state as the default.
        timegrid : list[float], optional
            An optional list defining the time grid over which the simulation is executed.

        Returns
        -------
        dict
            A dictionary containing the results of the simulation. This includes state populations
            and relevant metadata about the backend configuration.

        Raises
        ------
        SimulationError
            Raised if an error occurs during the simulation runtime.
        JobDescriptionError
            Raised if the job description provided to the simulation is invalid or incompatible.
        """
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_backend_information(self) -> dict:
        """
        Retrieve information about the backend.

        This method should return a dictionary containing detailed information about the backend,
        such as its capabilities, configuration, and any other relevant metadata.

        Returns
        -------
        dict
            A dictionary containing backend-specific details, including its configuration and capabilities.

        Raises
        ------
        NotImplementedError
            Raised if the subclass does not implement this method.
        """
        raise NotImplementedError("Method not implemented")
