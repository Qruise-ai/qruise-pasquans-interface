from abc import ABC, abstractmethod


class PasquansProvider(ABC):
    """Provider for Pasquans backends"""

    def __init__(self):
        super().__init__()

        self.name = "pasquans_qruise_provider"
        self._backends = self._verify_backends()

    @abstractmethod
    def _get_simulators(self) -> list:
        """Return a list of simulator classes"""
        raise NotImplementedError("Method not implemented")

    def backends(self, name=None):
        """Return a list of backends matching the name

        Parameters
        ----------
        name : str, optional
            name of the backend, by default None

        Returns
        -------
        list[SimulatorBackend]
            A list of backend instances matching the condition
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
        """Return instantiated Backends

        Returns
        -------
        dict[str:BackendV1]
            A dict of the instantiated backends keyed by backend name
        """

        ret = {}
        for backend_cls in self._get_simulators():
            backend_instance = self._get_backend_instance(backend_cls)
            backend_name = backend_instance.name
            ret[backend_name] = backend_instance
        return ret

    def _get_backend_instance(self, backend_cls):
        """Return an instance of a backend from its class

        Parameters
        ----------
        backend_cls : class
            backend class

        Returns
        -------
        BackendV1
            an instance of the backend

        Raises
        ------
        QiskitError
            if the backend can not be instantiated
        """

        # Verify that the backend can be instantiated.
        try:
            backend_instance = backend_cls(provider=self)
        except Exception as err:
            raise ImportError(
                "Backend %s could not be instantiated: %s" % (backend_cls, err)
            )

        return backend_instance

    def get_backend(self, name=None, **kwargs):
        """Return a single backend matching the specified filtering.

        Parameters:
        -----------
            name (str): name of the backend.
            **kwargs: dict used for filtering.

        Returns:
        --------
            Backend: a backend matching the filtering.

        Raises:
        -------
            ValueError: if no backend could be found or
                more than one backend matches the filtering criteria.
        """
        backends = self.backends(name, **kwargs)
        if len(backends) > 1:
            raise ValueError("More than one backend matches the criteria")
        if not backends:
            raise ValueError("No backend matches the criteria")

        return backends[0]
