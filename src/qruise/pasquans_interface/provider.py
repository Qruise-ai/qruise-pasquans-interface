from abc import ABC, abstractmethod


class PasquansProvider(ABC):
    """Abstract Base Class (ABC) for providing access to Pasquans backends.

    This class represents a provider for various Pasquans backends (e.g., simulators).
    It serves as a blueprint for child classes to implement methods for retrieving
    and managing backend instances.

    Attributes:
    -----------
    name : str
        The name of the provider instance, initialized as 'pasquans_qruise_provider'.
    _backends : dict
        A dictionary storing backend instances keyed by backend names.
    """

    def __init__(self):
        """Initialize the provider and verify the available backends."""
        super().__init__()
        self.name = "pasquans_qruise_provider"
        self._backends = self._verify_backends()

    @abstractmethod
    def _get_simulators(self) -> list:
        """Abstract method to be implemented by child classes to return a list of simulator classes.

        This method should return a list of simulator classes that represent different backends.

        Returns
        -------
        list
            A list of classes representing simulators.

        Raises
        ------
        NotImplementedError
            If the method is not implemented in the subclass.
        """
        raise NotImplementedError("Method not implemented")

    def backends(self, name=None):
        """Return a list of backends, optionally filtered by name.

        This method returns all available backends managed by the provider. If a specific
        backend name is provided, it returns the backend matching that name.

        Parameters
        ----------
        name : str, optional
            The name of the backend to filter for. If None, all backends are returned.

        Returns
        -------
        list[SimulatorBackend]
            A list of backend instances matching the specified name, or all backends if no name is provided.

        Raises
        ------
        ValueError
            If the specified backend name is not found.
        """
        backends = list(self._backends.values())
        if name:
            try:
                backends = [self._backends[name]]
            except LookupError:
                raise ValueError(
                    "The '{}' backend is not installed in your system.".format(name)
                )
        return backends

    def _verify_backends(self):
        """Instantiate and verify available backends.

        This method iterates over the list of backend classes provided by the
        `_get_simulators()` method, instantiates each backend, and stores them in a dictionary.

        Returns
        -------
        dict[str, BackendV1]
            A dictionary of instantiated backend objects, keyed by their names.
        """
        ret = {}
        for backend_cls in self._get_simulators():
            backend_instance = self._get_backend_instance(backend_cls)
            backend_name = backend_instance.name
            ret[backend_name] = backend_instance
        return ret

    def _get_backend_instance(self, backend_cls):
        """Instantiate a backend from its class.

        This method attempts to create an instance of the backend class passed in as a parameter.
        If instantiation fails, an ImportError is raised.

        Parameters
        ----------
        backend_cls : class
            The class representing a backend.

        Returns
        -------
        BackendV1
            An instance of the backend class.

        Raises
        ------
        ImportError
            If the backend class cannot be instantiated for any reason.
        """
        try:
            backend_instance = backend_cls(provider=self)
        except Exception as err:
            raise ImportError(
                "Backend %s could not be instantiated: %s" % (backend_cls, err)
            )
        return backend_instance

    def get_backend(self, name=None, **kwargs):
        """Retrieve a single backend instance matching the specified filtering criteria.

        This method filters the available backends using the provided `name` and additional
        keyword arguments, and returns a single matching backend. If multiple backends match the
        filtering criteria, or if none match, a ValueError is raised.

        Parameters
        ----------
        name : str, optional
            The name of the backend to retrieve. If None, all backends are considered.
        **kwargs : dict
            Additional keyword arguments used for filtering the backends.

        Returns
        -------
        BackendV1
            The backend instance that matches the filtering criteria.

        Raises
        ------
        ValueError
            If no backends match the filtering criteria or more than one backend matches.
        """
        backends = self.backends(name, **kwargs)
        if len(backends) > 1:
            raise ValueError("More than one backend matches the criteria")
        if not backends:
            raise ValueError("No backend matches the criteria")
        return backends[0]
