def get_backend_information(backend: str) -> dict:
    """Function to query configuration information about a backend

    Parameters
    ----------
    backend : str
        Name of the backend for which to retrieve information

    Returns
    -------
    dict
        Information about the backend, provided as a key-value pair dictionary

    Raises
    ------
    BackendNotFoundError
        When the supplied Backend is not found
    """

    return {"something about backend": None}
