from abc import ABC, abstractmethod
from typing import Tuple

class SimulatorBackend(ABC):

    name: str
    @abstractmethod
    def __init__(self, **backend_options):
        """
        Abstract constructor.
        Subclasses must implement this to initialize backend-specific attributes.
        """
        # Raise NotImplementedError if the method is not implemented
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def simulate(self, 
    lattice_sites: list[Tuple[float]], 
    global_rabi_frequency: list[float], 
    global_phase: list[float], 
    global_detuning: list[float], 
    local_detuning: list[float], 
    init_state: list[float] = None,
    timegrid: list[float] = None,
    ) -> dict:
        """
        Run simulation
        
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
            Vector of floats describing the local detuning (in the order of the sites specified in the lattice sites) 
        init_state : List[float], optional 
            Vector of floats describing the initial state of the system, by default ground state 

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
        # Raise NotImplementedError if the method is not implemented
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_backend_information(self) -> dict:
        """
        Abstract method to get information about the backend.
        Subclasses must implement this method and return a dictionary containing backend details.
        """
        # Raise NotImplementedError if the method is not implemented
        raise NotImplementedError("Method not implemented")
